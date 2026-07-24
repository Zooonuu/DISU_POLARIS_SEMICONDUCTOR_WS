# OASIS-FinFET

## 주제

**Surrogate-Assisted TCAD DTCO of a Fabrication-Aware Asymmetric Low-k Composite Spacer in SOI FinFETs**

한국어 주제:

**공정 가능성 제약과 surrogate 기반 능동 DOE를 이용한 비대칭 Low-k Composite Spacer SOI FinFET 최적화**

---

## 핵심 아이디어

기준 소자는 Source와 Drain 양쪽에 같은 `Si3N4` spacer를 갖는 3D SOI FinFET이다.

제안 구조는 다음처럼 바꾼다.

- Source-side spacer: 짧은 `Si3N4`
- Drain-side spacer: 더 긴 composite spacer
- Drain-side spacer 내부: `SiO2` low-k 구간
- NMOS와 PMOS의 Drain이 3-stage ring oscillator 각 stage의 switching output node를 향하도록 배치

목표는 Drain 쪽의 `Cgd`, 전계 집중, DIBL, 누설전류를 낮추면서 Source 쪽의 구동전류 손실을 최소화하고, 최종적으로 3-stage ring oscillator의 stage delay, power, energy 및 EDP를 개선하는 것이다.

이 프로젝트의 추가 기여는 **TCAD 실행 횟수가 제한된 상황에서 설계공간을 더 빠르고 신뢰성 있게 탐색하기 위한 알고리즘 흐름**이다. 초기 DOE 48개만으로 최종 신뢰성을 주장하지 않고, anchor case, surrogate-assisted active DOE, fabrication-aware grid snapping, local refinement, robust validation을 순차적으로 적용한다.

---

## 알고리즘 기여

### 문제 상황

3D TCAD는 실행 시간이 길기 때문에 수백~수천 개 조합을 무작정 돌리기 어렵다. 또한 LHS/Sobol DOE는 `3.12 nm`처럼 실제 공정 단위로 설명하기 애매한 연속값을 만들 수 있다. 따라서 단순히 48개 DOE만 수행하면 다음 문제가 남는다.

- 48개 sample만으로 전역 최적이나 신뢰성을 강하게 주장하기 어렵다.
- TCAD 실행 예산이 부족해 brute-force sweep이 불가능하다.
- 연속 DOE 값이 실제 fabrication grid와 맞지 않을 수 있다.
- nominal optimum 하나만 고르면 공정 편차에 취약할 수 있다.

### 해결 전략

본 프로젝트는 이를 위해 **TCAD-Aware Fabrication-Constrained Active DOE Algorithm**을 사용한다.

```text
1. Initial DOE 48개 생성
2. Baseline, center, feasible corner anchor case 추가
3. TCAD 결과 수집 및 공통 CSV 정리
4. Device-level screening으로 회로 검증 후보 축소
5. Surrogate model 기반 active DOE 후보 추천
6. 후보를 fabrication-aware grid로 snapping
7. Grid-snapped 후보의 circuit-level RO3 검증
8. Circuit-level DTCO Pareto front 계산
9. 최종 후보 주변 ±0.3/±0.5 nm robust validation
10. nominal optimum이 아니라 robust DTCO optimum 선정
```

핵심 주장은 다음과 같다.

> 48개 DOE는 최종 증명 데이터가 아니라 설계공간을 탐색하기 위한 초기 sample이다. 소자 지표는 비싼 회로 시뮬레이션 전에 후보를 줄이는 screening 지표로 사용하고, 최종 DTCO Pareto와 robust optimum 선정은 3-stage ring oscillator의 stage delay, power, energy, EDP 같은 회로 지표를 기준으로 수행한다.

### 공정 grid 설명

TCAD 탐색 단계에서는 설계공간의 민감도와 소자 screening 방향성을 보기 위해 연속적인 spacer 값을 허용한다. 단, 최종 DTCO 후보는 `0.5 nm` 또는 설정된 fabrication grid로 반올림한 뒤 소자 및 회로 수준에서 재시뮬레이션한다.

```text
exploration value: L_sp_S = 3.12 nm
grid-snapped candidate: L_sp_S = 3.0 nm
robust validation: 3.0 nm 주변 ±0.3/±0.5 nm
```

따라서 최종 보고서에서는 grid-snapped candidate의 circuit-level DTCO 결과와 robust validation 결과만 최종 성능 주장에 사용한다.

---

## 좌표축

프로젝트 전체에서 좌표축을 아래처럼 고정한다.

- `x`: Source → Drain 방향
- `y`: Fin 폭 방향
- `z`: Fin 높이 방향

---

## 주요 변수

| 변수 | 의미 |
|---|---|
| `L_sp_S` | Gate와 Source 사이의 source-side spacer 길이 |
| `L_sp_D` | Gate와 Drain 사이의 drain-side spacer 총길이 |
| `W_low_k` | Drain-side spacer 내부 SiO2 구간 길이 |

초기에는 `L_g`, `H_fin`, `W_fin`, EOT, doping, work function을 고정한다.

제약조건:

```text
L_sp_D >= L_sp_S
0 <= W_low_k <= L_sp_D
```

현재 기본 설계공간:

```text
L_sp_S: 3.0 ~ 7.0 nm
L_sp_D: 5.0 ~ 11.0 nm
W_low_k: 0.0 ~ 4.0 nm
```

---

## 최종 평가 항목

### 소자

- Ion
- Ioff
- Ion/Ioff
- Vth
- SS
- DIBL
- Cgd, Cgs, Cgg
- Drain-side electric field
- Current density

### 회로

- Unit inverter VTC 및 switching 정상 동작 확인
- 3-stage ring oscillator oscillation frequency
- Stage delay
- Average power
- Energy per cycle
- PDP 또는 EDP

### 최적화 및 신뢰성

- Initial DOE 48개 결과
- Baseline, center, feasible corner anchor case
- Device-level screening 후보
- Surrogate-assisted active DOE 추천 후보
- Fabrication-aware grid-snapped 후보
- 후보 주변 local refinement
- Circuit-level DTCO Pareto front
- 공정 편차 robust validation
- 공정 편차 방어율 및 spacer trade-off 보상율
- Nominal circuit optimum과 robust DTCO optimum 비교

Hold-out 검증은 현재 프로젝트 범위에서 제외한다.

---

## 폴더 구조

```text
00_original_example/   원본 TCAD example 보존
01_baseline/           대칭 spacer SOI FinFET
02_proposed/           비대칭 composite spacer SOI FinFET
03_doe/                DOE, anchor case, active DOE, local refinement, robust case 생성
04_circuit/            unit inverter와 3-stage ring oscillator
05_results/            원본 결과, 요약 CSV, Pareto/robust 분석, 최종 그림
06_submission/         보고서, 포스터, 발표자료
README.md              연구 전체 설명
TODO.md                실제 진행 순서
FILE_GUIDE.md          모든 파일의 역할
project.yaml           공통 파라미터 및 알고리즘 설정
```

불필요한 계획 문서는 추가하지 않는다. 새로운 결정과 현재 진행상황은 `TODO.md`에만 갱신한다.

---

## 진행 순서

```text
원본 example 실행
→ SOI single-fin baseline 재현
→ baseline 전기특성 검증
→ proposed spacer 구현
→ initial DOE 48개 및 anchor case 실행
→ device-level screening
→ surrogate-assisted active DOE 후보 추천
→ grid-snapped local refinement
→ PMOS 및 3-stage ring oscillator 검증
→ circuit-level DTCO Pareto front 계산
→ robust DTCO optimum
→ 최종 그림과 제출물
```

---

## 실행 예시

Python 환경:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 check_project.py
```

Initial DOE 48개 생성:

```bash
python3 03_doe/generate_cases.py
```

Anchor case 생성:

```bash
python3 03_doe/generate_anchor_cases.py
```

Device-level screening Pareto 계산 예시:

```bash
python3 05_results/pareto.py \
  --input 05_results/summary/all_results.csv \
  --maximize ion_A \
  --minimize ioff_A dibl_mV_V cgd_F \
  --output 05_results/summary/device_screening_pareto.csv
```

Circuit-level DTCO Pareto 계산 예시:

```bash
python3 05_results/pareto.py \
  --input 05_results/summary/all_results.csv \
  --maximize oscillation_frequency_Hz \
  --minimize stage_delay_s average_power_W energy_per_cycle_J edp_Js \
  --output 05_results/summary/circuit_dtco_pareto.csv
```

Device screening용 active DOE 후보 추천 예시:

```bash
python3 03_doe/suggest_active_cases.py \
  --input 05_results/summary/all_results.csv \
  --mode device_screening
```

Circuit DTCO용 active DOE 후보 추천 예시:

```bash
python3 03_doe/suggest_active_cases.py \
  --input 05_results/summary/all_results.csv \
  --mode circuit_dtco
```

Circuit-level Pareto 후보 주변 grid-snapped local refinement 생성:

```bash
python3 03_doe/generate_local_refinement_cases.py \
  --candidates 05_results/summary/circuit_dtco_pareto.csv
```

Robust 검증 case 생성:

```bash
python3 03_doe/generate_robust_cases.py \
  --candidates 05_results/summary/circuit_dtco_pareto.csv \
  --max-candidates 3
```

TCAD/회로 실행 후 `base_case_id`, `variation_kind`, `ion_A`, `cgd_F`, `stage_delay_s`, `average_power_W`, `energy_per_cycle_J`, `edp_Js`를 포함하는 결과 CSV를 만들고, baseline reference와 비교해 robust DTCO optimum을 계산한다.

---

## 작업 환경 분리

이 프로젝트는 개인 노트북과 학교 TCAD PC를 Git 저장소로 동기화해서 진행한다.

```text
개인 노트북 / VS Code:
deck template 작성, Python 후처리 코드 작성, README/TODO 정리, 결과 해석

학교 TCAD PC:
Sentaurus/Silvaco 실행, 원본 example 검증, TCAD raw output 생성
```

기본 왕복 흐름:

```text
1. 노트북에서 deck/template/code 수정
2. Git push
3. 학교 PC에서 Git pull
4. 학교 PC에서 TCAD 실행
5. raw output은 학교 PC에 보존
6. 요약 CSV, 핵심 figure, 필요한 log excerpt만 Git에 반영
7. 노트북에서 Git pull 후 분석/문서화
```

TCAD 대용량 파일인 `.tdr`, `.plt`, `.log`, `.msh`, `.str` 등은 Git에 올리지 않는다. 실패 case도 삭제하지 않되, 대용량 raw output은 학교 PC의 작업 디렉토리와 `05_results/raw/` 로컬 사본에 보관하고, Git에는 요약 결과만 남긴다.

---

## 파일 원칙

1. `00_original_example`의 원본 파일은 수정하지 않는다.
2. 실행 가능한 baseline이 생기기 전에는 DOE case를 대량 생성하지 않는다.
3. Baseline과 Proposed는 핵심 spacer 조건 외에 동일한 조건을 사용한다.
4. Initial DOE 48개는 탐색용 sample로만 설명한다.
5. 최종 후보는 fabrication grid로 snapping한 뒤 재시뮬레이션한다.
6. 실패한 case와 log도 삭제하지 않는다.
7. 결과가 나온 뒤 목적함수와 합격조건을 임의로 변경하지 않는다.
8. TCAD 결과를 실제 제작 결과처럼 표현하지 않는다.
9. 대용량 raw output은 Git에 올리지 않는다.

---

## 파일 이름 예시

```text
baseline_nmos_idvg.tdr
proposed_nmos_LSS05_LSD09_WLK03.tdr
initial_doe_cases.csv
anchor_cases.csv
active_suggested_cases.csv
local_refinement_cases.csv
robust_cases.csv
case_LSS05_LSD09_WLK03.csv
ro3_LSS05_LSD09_WLK03_waveform.csv
ro3_LSS05_LSD09_WLK03_summary.csv
```
