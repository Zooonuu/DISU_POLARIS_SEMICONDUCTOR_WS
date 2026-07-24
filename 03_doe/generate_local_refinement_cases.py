from __future__ import annotations

import argparse
from itertools import product
from pathlib import Path

import numpy as np
import pandas as pd
import yaml

ROOT = Path(__file__).resolve().parents[1]
PARAM_NAMES = ("l_sp_s_nm", "l_sp_d_nm", "w_low_k_nm")


def load_config() -> dict:
    with (ROOT / "project.yaml").open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def snap(value: float, step: float) -> float:
    return round(round(value / step) * step, 6)


def feasible(row: dict[str, float], space: dict) -> bool:
    return (
        space["l_sp_s_nm"][0] <= row["l_sp_s_nm"] <= space["l_sp_s_nm"][1]
        and space["l_sp_d_nm"][0] <= row["l_sp_d_nm"] <= space["l_sp_d_nm"][1]
        and space["w_low_k_nm"][0] <= row["w_low_k_nm"] <= space["w_low_k_nm"][1]
        and row["l_sp_d_nm"] >= row["l_sp_s_nm"]
        and row["w_low_k_nm"] <= row["l_sp_d_nm"]
    )


def main() -> None:
    cfg = load_config()
    space = cfg["design_space"]
    refine_cfg = cfg.get("local_refinement", {})
    grid_step = float(refine_cfg.get("grid_step_nm", cfg.get("fabrication_grid", {}).get("step_nm", 0.5)))
    radius_steps = int(refine_cfg.get("radius_steps", 1))

    parser = argparse.ArgumentParser()
    parser.add_argument("--candidates", type=Path, default=ROOT / "05_results/summary/pareto.csv")
    parser.add_argument("--max-candidates", type=int, default=int(refine_cfg.get("max_candidates", 3)))
    parser.add_argument("--grid-step-nm", type=float, default=grid_step)
    parser.add_argument("--radius-steps", type=int, default=radius_steps)
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / refine_cfg.get("output", "03_doe/cases/local_refinement_cases.csv"),
    )
    args = parser.parse_args()

    candidates = pd.read_csv(args.candidates)
    missing = {"case_id", *PARAM_NAMES} - set(candidates.columns)
    if missing:
        raise ValueError(f"candidate file is missing columns: {sorted(missing)}")

    if args.max_candidates > 0:
        candidates = candidates.head(args.max_candidates)

    offsets = range(-args.radius_steps, args.radius_steps + 1)
    rows: list[dict] = []
    seen: set[tuple[float, float, float]] = set()
    for _, candidate in candidates.iterrows():
        source_case_id = str(candidate["case_id"])
        snapped = {
            name: snap(float(candidate[name]), args.grid_step_nm)
            for name in PARAM_NAMES
        }
        for steps in product(offsets, repeat=len(PARAM_NAMES)):
            row = {
                name: snap(snapped[name] + step * args.grid_step_nm, args.grid_step_nm)
                for name, step in zip(PARAM_NAMES, steps, strict=True)
            }
            if not feasible(row, space):
                continue
            key = tuple(row[name] for name in PARAM_NAMES)
            if key in seen:
                continue
            seen.add(key)
            distance_nm = float(np.sqrt(sum((row[name] - float(candidate[name])) ** 2 for name in PARAM_NAMES)))
            rows.append(
                {
                    "case_id": f"L{len(rows) + 1:03d}",
                    "case_group": "local_refinement",
                    "source_case_id": source_case_id,
                    "structure": "proposed",
                    **row,
                    "grid_step_nm": args.grid_step_nm,
                    "grid_snapped": True,
                    "distance_from_source_nm": distance_nm,
                    "status": "not_started",
                }
            )

    result = pd.DataFrame(rows)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(args.output, index=False)
    print(f"saved: {args.output} ({len(result)} local refinement cases)")


if __name__ == "__main__":
    main()
