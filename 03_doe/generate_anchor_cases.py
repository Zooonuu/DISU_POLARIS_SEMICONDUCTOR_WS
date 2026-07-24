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
    return (
        space["l_sp_s_nm"][0] <= row["l_sp_s_nm"] <= space["l_sp_s_nm"][1]
        and space["l_sp_d_nm"][0] <= row["l_sp_d_nm"] <= space["l_sp_d_nm"][1]
        and space["w_low_k_nm"][0] <= row["w_low_k_nm"] <= space["w_low_k_nm"][1]
        and row["l_sp_d_nm"] >= row["l_sp_s_nm"]
        and row["w_low_k_nm"] <= row["l_sp_d_nm"]
    )


def main() -> None:
    cfg = load_config()
    anchor_cfg = cfg.get("anchor_cases", {})
    space = cfg["design_space"]

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / anchor_cfg.get("output", "03_doe/cases/anchor_cases.csv"),
    )
    args = parser.parse_args()

    rows: list[dict] = []
    if anchor_cfg.get("include_baseline_reference", True):
        spacer = float(anchor_cfg.get("baseline_spacer_nm", space["l_sp_s_nm"][0]))
        rows.append(
            {
                "case_id": "A000",
                "case_group": "anchor",
                "anchor_kind": "baseline_reference",
                "structure": "baseline",
                "l_sp_s_nm": spacer,
                "l_sp_d_nm": spacer,
                "w_low_k_nm": 0.0,
                "grid_snapped": True,
                "status": "not_started",
            }
        )

    if anchor_cfg.get("include_center", True):
        center = {
            name: sum(space[name]) / 2.0
            for name in PARAM_NAMES
        }
        if feasible(center, space):
            rows.append(
                {
                    "case_id": f"A{len(rows):03d}",
                    "case_group": "anchor",
                    "anchor_kind": "center",
                    "structure": "proposed",
                    **center,
                    "grid_snapped": True,
                    "status": "not_started",
                }
            )

    if anchor_cfg.get("include_feasible_corners", True):
        bounds = [[float(space[name][0]), float(space[name][1])] for name in PARAM_NAMES]
        for values in product(*bounds):
            row = dict(zip(PARAM_NAMES, values, strict=True))
            if not feasible(row, space):
                continue
            rows.append(
                {
                    "case_id": f"A{len(rows):03d}",
                    "case_group": "anchor",
                    "anchor_kind": "feasible_corner",
                    "structure": "proposed",
                    **row,
                    "grid_snapped": True,
                    "status": "not_started",
                }
            )

    result = pd.DataFrame(rows)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(args.output, index=False)
    print(f"saved: {args.output} ({len(result)} anchor cases)")


if __name__ == "__main__":
    main()
