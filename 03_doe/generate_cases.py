from __future__ import annotations

import argparse
from pathlib import Path
import numpy as np
import pandas as pd
import yaml
from scipy.stats import qmc

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=24)
    parser.add_argument("--method", choices=["lhs", "sobol"], default="lhs")
    parser.add_argument("--seed", type=int, default=20260723)
    args = parser.parse_args()

    with (ROOT / "project.yaml").open(encoding="utf-8") as f:
        cfg = yaml.safe_load(f)

    space = cfg["design_space"]
    names = ["l_sp_s_nm", "l_sp_d_nm", "w_low_k_nm"]
    lower = np.array([space[n][0] for n in names], dtype=float)
    upper = np.array([space[n][1] for n in names], dtype=float)

    accepted = []
    attempt = 0
    while len(accepted) < args.samples and attempt < 20:
        attempt += 1
        if args.method == "lhs":
            sampler = qmc.LatinHypercube(d=3, seed=args.seed + attempt)
            unit = sampler.random(max(64, args.samples * 4))
        else:
            sampler = qmc.Sobol(d=3, scramble=True, seed=args.seed + attempt)
            unit = sampler.random(max(64, args.samples * 4))

        for row in qmc.scale(unit, lower, upper):
            lss, lsd, wlk = row
            if lsd < lss or wlk > lsd:
                continue
            accepted.append(row)
            if len(accepted) == args.samples:
                break

    if len(accepted) < args.samples:
        raise RuntimeError("Feasible cases could not be generated.")

    df = pd.DataFrame(accepted, columns=names)
    df.insert(0, "case_id", [f"C{i:03d}" for i in range(1, len(df) + 1)])
    df["status"] = "not_started"

    output = ROOT / "03_doe" / "cases.csv"
    df.to_csv(output, index=False)
    print(f"saved: {output} ({len(df)} cases)")


if __name__ == "__main__":
    main()
