from __future__ import annotations

import argparse
from pathlib import Path
import numpy as np
import pandas as pd
import yaml
from scipy.stats import qmc


def load_space(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f)


def generate(method: str, samples: int, seed: int, config: dict) -> pd.DataFrame:
    variables = config["variables"]
    names = list(variables)
    lower = np.array([variables[n]["min"] for n in names], dtype=float)
    upper = np.array([variables[n]["max"] for n in names], dtype=float)

    accepted: list[np.ndarray] = []
    batch = max(samples * 4, 64)
    rounds = 0

    while len(accepted) < samples and rounds < 20:
        rounds += 1
        if method == "sobol":
            sampler = qmc.Sobol(d=len(names), scramble=True, seed=seed + rounds)
            unit = sampler.random(batch)
        elif method == "lhs":
            sampler = qmc.LatinHypercube(d=len(names), seed=seed + rounds)
            unit = sampler.random(batch)
        else:
            raise ValueError("method must be lhs or sobol")

        values = qmc.scale(unit, lower, upper)
        for row in values:
            d = dict(zip(names, row))
            if d["l_sp_d_nm"] < d["l_sp_s_nm"]:
                continue
            if d["w_low_k_nm"] > d["l_sp_d_nm"]:
                continue
            accepted.append(row)
            if len(accepted) >= samples:
                break

    if len(accepted) < samples:
        raise RuntimeError("Could not generate enough feasible samples.")

    df = pd.DataFrame(np.array(accepted[:samples]), columns=names)
    df.insert(0, "design_id", [f"DOE_{i:04d}" for i in range(1, len(df) + 1)])
    df["seed"] = seed
    df["sampling_method"] = method
    return df


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--samples", type=int, default=24)
    parser.add_argument("--method", choices=["lhs", "sobol"], default="lhs")
    parser.add_argument("--seed", type=int, default=20260723)
    args = parser.parse_args()

    config = load_space(args.config)
    df = generate(args.method, args.samples, args.seed, config)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.output, index=False)
    print(f"saved {len(df)} feasible designs -> {args.output}")


if __name__ == "__main__":
    main()
