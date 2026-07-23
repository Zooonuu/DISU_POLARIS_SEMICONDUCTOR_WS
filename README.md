# DISU FinFET Process–Circuit Co-Optimization Project

## 1. 프로젝트 제목

**출력 노드 지향 비대칭 복합 Gate Spacer 3D FinFET CMOS 인버터의 공정–회로–Virtual R2R 통합 최적화**

영문 가제:

**Output-Oriented Asymmetric Composite-Spacer 3D FinFET CMOS Inverter with Process–Circuit Co-Optimization and Virtual Run-to-Run Control**

프로젝트 별칭: **OASIS-FinFET**

---

## 2. 프로젝트 핵심 아이디어

기존의 대칭 Gate Spacer FinFET은 Source 쪽과 Drain 쪽에 동일한 길이와 재료의 Spacer를 사용한다. 그러나 두 영역은 요구 성능이 다르다.

- **Source 쪽**: Source access resistance를 작게 유지하여 `Ion`과 구동 속도를 확보해야 한다.
- **Drain 쪽**: Gate–Drain 기생 커패시턴스, Miller coupling, Drain 전계 침투, DIBL 및 누설전류를 줄여야 한다.

따라서 본 프로젝트는 다음 구조를 직접 설계한다.

1. Source-side Spacer는 상대적으로 짧은 solid dielectric 구조로 설계한다.
2. Drain-side Spacer는 상대적으로 길게 설계한다.
3. Drain-side Spacer 내부에 low-k 구간을 포함한 composite 구조를 적용한다.
4. NMOS와 PMOS 모두 긴 Drain-side composite Spacer가 CMOS 인버터의 공통 출력 노드 `OUT`을 향하도록 배치한다.
5. 공정 파라미터 변화가 소자 특성과 회로 Power/Delay에 미치는 영향을 함께 분석한다.
6. 공정 편차를 가상으로 주입하고 Ring Oscillator 또는 Inverter metric을 피드백 신호로 사용하는 Virtual R2R proof-of-concept를 구현한다.

---

## 3. 좌표축 정의

모든 공정 Deck, 그림, 결과 파일에서 아래 좌표계를 고정한다.

- `x`: Source → Drain 방향, 전류가 흐르는 방향
- `y`: Fin 폭 방향
- `z`: Fin 높이 방향

좌표계가 다른 자료를 참고할 경우에도 이 프로젝트 내부에서는 반드시 위 정의로 변환해서 기록한다.

---

## 4. 핵심 설계 파라미터

### 주 최적화 변수

| 변수 | 물리적 의미 | 위치 | 초기 탐색 범위(가안) |
|---|---|---|---|
| `L_sp_S` | Source-side Spacer 길이 | Gate와 Source 사이, x 방향 | 3–7 nm |
| `L_sp_D` | Drain-side Spacer 총 길이 | Gate와 Drain 사이, x 방향 | 5–11 nm |
| `W_low_k` | Drain-side Spacer 내부 low-k 구간 길이 | Drain-side Spacer 내부, x 방향 | 0–4 nm |

### 초기 고정 변수

`L_g`, `H_fin`, `W_fin`, EOT, Gate work function, Source/Drain doping, 온도 및 공급전압은 baseline 검증 전까지 최적화 변수로 사용하지 않는다.  
고정값은 문헌과 사용 가능한 TCAD Deck/공정 조건을 확인한 뒤 `project_config.yaml`에 기록한다.

### 구조 제약조건

- `L_sp_D >= L_sp_S`
- `0 <= W_low_k <= L_sp_D`
- 물리적으로 형성 불가능하거나 mesh가 붕괴하는 조건은 사전에 정의된 제외 규칙에 따라 기록한다.
- 수렴 실패 조건도 삭제하지 않고 `experiment_registry.csv`에 남긴다.

---

## 5. 연구 문제와 가설

### 연구 문제

대칭 Spacer FinFET에서 Spacer를 길게 하면 기생 커패시턴스와 누설은 줄어들 수 있지만, access resistance 증가로 `Ion`과 회로 속도가 악화될 수 있다.

### 가설

Source 쪽은 짧은 solid Spacer로 구동전류를 유지하고, Drain 쪽은 긴 composite low-k Spacer로 기생 커패시턴스와 누설을 감소시키면, 대칭 Spacer 대비 더 낮은 회로 EDP를 갖는 내부 최적점이 존재한다.

### 예상 Trade-off

- `L_sp_D ↑` → `Cgd`, DIBL, `Ioff` 감소 가능 / `Ion` 및 Delay 악화 가능
- `W_low_k ↑` → 기생 커패시턴스 감소 가능 / 공정 민감도 및 전계 분포 변화 가능
- `L_sp_S ↓` → Source resistance 감소 및 `Ion` 유지 / Source-side coupling 증가 가능

---

## 6. 최종 평가 지표

### 소자 수준

- `Ion`
- `Ioff`
- `Ion/Ioff`
- Threshold voltage
- Subthreshold Swing
- DIBL
- `Cgg`, `Cgd`, `Cgs`
- Electric field distribution
- Current density
- Potential distribution

### 회로 수준

- CMOS Inverter VTC
- Switching threshold
- `NMH`, `NML`
- `tpHL`, `tpLH`
- Rise/Fall time
- Static power
- Dynamic energy
- PDP 또는 EDP
- Ring Oscillator frequency
- Energy per transition

### 제조·제어 수준

- 공정 편차에 따른 성능 평균과 표준편차
- Nominal optimum과 Robust optimum 비교
- Open-loop와 Closed-loop Virtual R2R 비교
- Target tracking error
- 수렴 Run 수

---

## 7. 전체 수행 순서

### `00_project_management`
연구 범위, 역할, 일정, 실험 이력, 의사결정을 관리한다.

### `01_environment`
사용 툴 버전, Python 환경, 환경 설정 스크립트를 관리한다.

### `02_reference`
논문, 수상작 분석, TCAD 매뉴얼 노트를 관리한다. 원문 PDF의 무단 재배포는 하지 않는다.

### `03_baseline_process`
대칭 Spacer 3D FinFET의 공정 구조를 생성한다.  
이 단계의 성공 기준은 재현 가능한 baseline `.tdr` 또는 해당 시뮬레이터 구조 파일을 생성하는 것이다.

### `04_baseline_device`
Baseline NMOS/PMOS의 DC 및 capacitance 특성을 추출한다.

### `05_proposed_process`
비대칭 composite Spacer 구조를 직접 공정 단계로 구현한다.

### `06_proposed_device`
Proposed NMOS/PMOS의 전기적 특성과 물리 분포를 분석한다.

### `07_circuit`
NMOS/PMOS를 CMOS Inverter와 Ring Oscillator로 연결하고 Power/Delay를 평가한다.

### `08_doe_optimization`
사전에 정의한 설계 범위에서 DOE를 생성하고 Pareto 및 Robust optimum을 계산한다.

### `09_virtual_r2r`
공정 drift를 가상으로 주입하고 전기적 metric을 이용해 다음 Run recipe를 보정한다.

### `10_validation`
Hold-out 조건, 최적점 주변 조건, 공정 variation을 이용해 재검증한다.

### `11_figures_report`
최종 Heatmap, Pareto front, 구조도, 회로 waveform, R2R 그래프와 보고서·포스터를 제작한다.

### `12_release`
재현성 점검 후 제출본과 실행 기록을 고정한다.

---

## 8. Cherry-picking 방지 원칙

1. 결과를 보기 전에 설계 범위와 목적함수를 문서에 고정한다.
2. 임의 간격 Sweep만 사용하지 않고 Sobol 또는 Latin Hypercube DOE를 사용한다.
3. 모든 성공·실패 조건을 `experiment_registry.csv`에 기록한다.
4. Pareto 후보는 학습에 쓰지 않은 Hold-out 조건으로 다시 계산한다.
5. 최적점 주변의 미세 조건을 재시뮬레이션한다.
6. 가장 좋은 한 점뿐 아니라 전체 설계공간 Heatmap과 Pareto front를 공개한다.
7. Nominal 최고점과 공정 편차에 강한 Robust optimum을 구분한다.
8. Random seed, simulator version, mesh 기준, 제외 기준을 모두 남긴다.

---

## 9. 권장 Tool Stack

### TCAD

- Synopsys Sentaurus Workbench
- Sentaurus Process
- Sentaurus Device
- Sentaurus Visual / Inspect
- MixedMode 사용 가능 시 Sentaurus MixedMode

대체 경로:

- Silvaco Victory Process
- Silvaco Victory Device
- TonyPlot
- MixedMode 또는 외부 SPICE 연동

### 자동화 및 분석

- Python 3.10 이상 권장
- NumPy
- pandas
- SciPy
- Matplotlib
- scikit-learn
- scikit-optimize
- PyYAML

### 협업 및 문서

- Ubuntu
- VS Code
- Git / GitHub
- PowerPoint, Figma 또는 Inkscape

PADS는 PCB 제작이 포함되지 않는 한 본 프로젝트의 필수 도구가 아니다.

---

## 10. 팀 역할 제안

### 공정설계 A
- Baseline SProcess
- Fin, STI, Gate, Spacer, Source/Drain 형성
- Mesh 및 구조 검증

### 공정설계 B
- Proposed composite Spacer
- DOE 공정 파라미터 반영
- 공정 가능 범위 및 failure rule 관리

### 회로설계 A
- SDevice NMOS/PMOS 특성 추출
- Inverter VTC 및 transient 분석
- Power/Delay metric 정의

### 회로설계 B
- Ring Oscillator
- Pareto/Robust optimization
- Virtual R2R controller
- 결과 시각화

담당자는 `00_project_management/roles.md`에 이름을 기입한다.

---

## 11. 첫 실행 순서

```bash
cd ~/DISU_POLARIS_WS/DISU_WS
code .
```

Python 환경:

```bash
bash 01_environment/setup_python.sh
source .venv/bin/activate
```

설정 검사:

```bash
python scripts/validate_project.py
```

DOE 예시 생성:

```bash
python 08_doe_optimization/generate_doe.py \
  --config 08_doe_optimization/config/design_space.yaml \
  --output 08_doe_optimization/data/doe/initial_doe.csv \
  --samples 24 \
  --method lhs \
  --seed 20260723
```

Pareto 계산 예시:

```bash
python 08_doe_optimization/pareto.py \
  --input 08_doe_optimization/data/processed/all_metrics.csv \
  --minimize ioff_A cgd_F edp_Js \
  --output 08_doe_optimization/results/pareto_front.csv
```

---

## 12. 파일 및 Run 이름 규칙

Run ID:

```text
BAS_N_0001
BAS_P_0001
PRO_N_0001
PRO_P_0001
CIR_INV_0001
R2R_0001
```

구조 파일 이름 예시:

```text
PRO_N_LSS5.0_LSD8.5_WLK2.0.tdr
```

모든 숫자의 단위는 파일 내부 또는 CSV header에 명시한다.

---

## 13. Git 사용 원칙

Git 연결 전에도 각 실험은 `experiment_registry.csv`에 남긴다.

권장 브랜치:

```text
main
process/baseline
process/proposed
device/extraction
circuit/inverter
optimization/doe
control/r2r
docs/report
```

커밋 예시:

```text
feat(process): build baseline single-fin geometry
fix(device): stabilize drain bias ramp
feat(opt): add constrained LHS generator
docs(report): add spacer mechanism figure
```

대용량 결과 파일 `.tdr`, raw log, mesh 파일은 기본적으로 Git에 올리지 않는다. 필요한 대표 결과만 `12_release/archive`에 별도 정리한다.

---

## 14. 완료 정의

아래 항목을 모두 만족하면 프로젝트 본체를 완료한 것으로 본다.

- [ ] Baseline 3D FinFET 구조 재현
- [ ] Baseline NMOS/PMOS 수렴
- [ ] Proposed asymmetric composite Spacer 구조 재현
- [ ] Proposed NMOS/PMOS 수렴
- [ ] 동일 조건의 Baseline–Proposed 비교
- [ ] Inverter VTC 및 transient 결과
- [ ] Power/Delay/PDP 또는 EDP 계산
- [ ] DOE 전체 결과표
- [ ] Pareto front와 독립 검증
- [ ] 공정 variation 분석
- [ ] Virtual R2R open-loop/closed-loop 비교
- [ ] 구조도·Heatmap·그래프 완성
- [ ] 보고서·포스터·발표자료 완성
- [ ] 실행 환경과 seed 기록
