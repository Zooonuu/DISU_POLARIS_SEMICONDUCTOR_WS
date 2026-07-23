from __future__ import annotations

import argparse
from pathlib import Path
import numpy as np
import pandas as pd


def pareto_mask(values: np.ndarray) -> np.ndarray:
    mask = np.ones(len(values), dtype=bool)
    for i in range(len(values)):
        if np.any(
            np.all(values <= values[i], axis=1)
            & np.any(values < values[i], axis=1)
        ):
            mask[i] = False
    return mask


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--objectives", nargs="+", required=True)
    args = parser.parse_args()

    df = pd.read_csv(args.input).dropna(subset=args.objectives)
    result = df.loc[pareto_mask(df[args.objectives].to_numpy(float))]
    output = Path("05_results/summary/pareto.csv")
    output.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(output, index=False)
    print(f"saved: {output}")


if __name__ == "__main__":
    main()
