from __future__ import annotations

import argparse
from pathlib import Path
import numpy as np
import pandas as pd


def pareto_mask(values: np.ndarray) -> np.ndarray:
    n = values.shape[0]
    efficient = np.ones(n, dtype=bool)
    for i in range(n):
        if not efficient[i]:
            continue
        dominated_by_other = np.any(
            np.all(values <= values[i], axis=1)
            & np.any(values < values[i], axis=1)
        )
        if dominated_by_other:
            efficient[i] = False
    return efficient


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--minimize", nargs="+", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    missing = [c for c in args.minimize if c not in df.columns]
    if missing:
        raise KeyError(f"missing objective columns: {missing}")

    clean = df.dropna(subset=args.minimize).copy()
    mask = pareto_mask(clean[args.minimize].to_numpy(dtype=float))
    out = clean.loc[mask].copy()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(args.output, index=False)
    print(f"pareto points: {len(out)} / {len(clean)} -> {args.output}")


if __name__ == "__main__":
    main()
