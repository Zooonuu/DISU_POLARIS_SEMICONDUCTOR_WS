from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parent
required = [
    "README.md",
    "TODO.md",
    "project.yaml",
    "00_original_example",
    "01_baseline/process",
    "01_baseline/device",
    "02_proposed/process",
    "02_proposed/device",
    "03_doe",
    "04_circuit",
    "05_results",
    "06_submission",
]

missing = [item for item in required if not (ROOT / item).exists()]

try:
    with (ROOT / "project.yaml").open(encoding="utf-8") as f:
        yaml.safe_load(f)
except Exception as exc:
    missing.append(f"project.yaml error: {exc}")

if missing:
    print("[FAIL]")
    for item in missing:
        print(" -", item)
    sys.exit(1)

print("[OK] 간소화 프로젝트 구조가 정상입니다.")
