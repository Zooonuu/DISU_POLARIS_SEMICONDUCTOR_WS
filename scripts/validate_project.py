from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "README.md",
    "project_config.yaml",
    "00_project_management/experiment_registry.csv",
    "03_baseline_process/sprocess/finfet_baseline.cmd.template",
    "05_proposed_process/sprocess/finfet_asymmetric_spacer.cmd.template",
    "08_doe_optimization/config/design_space.yaml",
]

errors = []
for rel in REQUIRED:
    if not (ROOT / rel).exists():
        errors.append(f"missing: {rel}")

try:
    with (ROOT / "project_config.yaml").open(encoding="utf-8") as f:
        yaml.safe_load(f)
except Exception as exc:
    errors.append(f"invalid project_config.yaml: {exc}")

if errors:
    print("[FAIL]")
    for err in errors:
        print(" -", err)
    sys.exit(1)

print("[OK] 프로젝트 기본 구조와 YAML 파일을 확인했습니다.")
