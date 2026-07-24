from __future__ import annotations

import argparse
from itertools import product
from pathlib import Path

import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
PARAM_NAMES = ("l_sp_s_nm", "l_sp_d_nm", "w_low_k_nm")


def load_config() -> dict:
    with (ROOT / "project.yaml").open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def feasible(row: dict[str, float], space: dict) -> bool:
    for name in PARAM_NAMES:
        low, high = space[name]
        if row[name] < low or row[name] > high:
            return False
    return row["l_sp_d_nm"] >= row["l_sp_s_nm"] and row["w_low_k_nm"] <= row["l_sp_d_nm"]


def snap(value: float, step: float) -> float:
    return round(round(value / step) * step, 6)


def add_case(
    rows: list[dict],
    seen: set[tuple],
    candidate: pd.Series,
    varied: dict[str, float],
    variation_kind: str,
    delta_nm: float,
    space: dict,
) -> None:
    if not feasible(varied, space):
        return

    base_case_id = str(candidate["case_id"])
    key = (
        base_case_id,
        variation_kind,
        round(varied["l_sp_s_nm"], 6),
        round(varied["l_sp_d_nm"], 6),
        round(varied["w_low_k_nm"], 6),
    )
    if key in seen:
        return
    seen.add(key)

    robust_index = sum(1 for row in rows if row["base_case_id"] == base_case_id)
    rows.append(
        {
            "robust_case_id": f"{base_case_id}_R{robust_index:03d}",
            "base_case_id": base_case_id,
            "variation_kind": variation_kind,
            "delta_nm": delta_nm,
            "l_sp_s_nm": varied["l_sp_s_nm"],
            "l_sp_d_nm": varied["l_sp_d_nm"],
            "w_low_k_nm": varied["w_low_k_nm"],
            "structure": "proposed",
            "status": "not_started",
        }
    )


def main() -> None:
    cfg = load_config()
    robust_cfg = cfg.get("robust_validation", {})

    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", type=Path, default=ROOT / "05_results/summary/pareto.csv")
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / robust_cfg.get("output", "03_doe/cases/robust_cases.csv"),
    )
    parser.add_argument("--max-candidates", type=int, default=3)
    parser.add_argument("--deltas-nm", nargs="*", type=float)
    parser.add_argument("--snap-nominal", action="store_true")
    parser.add_argument("--no-snap-nominal", action="store_true")
    parser.add_argument("--grid-step-nm", type=float)
    args = parser.parse_args()

    space = cfg["design_space"]
    grid_cfg = cfg.get("fabrication_grid", {})
    deltas = args.deltas_nm or robust_cfg.get("absolute_variation_nm", [0.3, 0.5])
    include_oat = bool(robust_cfg.get("include_one_at_a_time", True))
    include_corners = bool(robust_cfg.get("include_combined_corners", True))
    snap_nominal = bool(grid_cfg.get("snap_final_candidates", True))
    if args.snap_nominal:
        snap_nominal = True
    if args.no_snap_nominal:
        snap_nominal = False
    grid_step = args.grid_step_nm or float(grid_cfg.get("step_nm", 0.5))

    candidates = pd.read_csv(args.candidates)
    missing = {"case_id", *PARAM_NAMES} - set(candidates.columns)
    if missing:
        raise ValueError(f"candidate file is missing columns: {sorted(missing)}")

    if args.max_candidates > 0:
        candidates = candidates.head(args.max_candidates)

    rows: list[dict] = []
    seen: set[tuple] = set()
    for _, candidate in candidates.iterrows():
        nominal = {name: float(candidate[name]) for name in PARAM_NAMES}
        if snap_nominal:
            nominal = {name: snap(value, grid_step) for name, value in nominal.items()}
        add_case(rows, seen, candidate, nominal, "nominal", 0.0, space)

        for delta in deltas:
            if include_oat:
                for name in PARAM_NAMES:
                    for direction, label in ((-1.0, "m"), (1.0, "p")):
                        varied = nominal.copy()
                        varied[name] += direction * delta
                        add_case(rows, seen, candidate, varied, f"{name}_{label}{delta:g}nm", delta, space)

            if include_corners:
                for signs in product((-1.0, 1.0), repeat=len(PARAM_NAMES)):
                    varied = {
                        name: nominal[name] + sign * delta
                        for name, sign in zip(PARAM_NAMES, signs, strict=True)
                    }
                    sign_label = "_".join(
                        f"{name}_{'p' if sign > 0 else 'm'}"
                        for name, sign in zip(PARAM_NAMES, signs, strict=True)
                    )
                    add_case(rows, seen, candidate, varied, f"corner_{sign_label}_{delta:g}nm", delta, space)

    result = pd.DataFrame(rows)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(args.output, index=False)
    print(f"saved: {args.output} ({len(result)} robust validation cases)")


if __name__ == "__main__":
    main()
