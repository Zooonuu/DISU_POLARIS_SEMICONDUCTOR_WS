# TODO

이 문서는 프로젝트 전체 진행을 **공정/소자설계 파트**와 **회로설계 파트**로 나누어 정리한다.

전체 목표:

```text
SOI FinFET에서 drain-side low-k composite spacer 구조를 설계하고,
소자 지표뿐 아니라 FO4 회로 성능과 공정 편차 robust성까지 기준으로 최적 후보를 선정한다.
```

전체 흐름:

```text
환경 확인
→ Baseline 소자 확보
→ Proposed 소자 확보
→ DOE/device screening
→ 회로 DTCO
→ local refinement
→ robust validation
→ 최종 발표/보고서
```

---

## 1. 전체 진행표: 소자 / 회로 분담

| 단계 | 공정/소자설계 파트 | 회로설계 파트 | 두 파트 연결 산출물 |
|---|---|---|---|
| 1. 환경 확인 | TCAD 로그인, Sentaurus/Silvaco 실행 확인, 원본 FinFET example 실행, 결과 파일 복사 테스트, repo 이동 확인 | MixedMode/회로 예제 확인, inverter/FO4 template 확인, 회로 실행 가능 여부 확인 | TCAD 실행 가능 여부, tool/version, 원본 example 경로, 결과 회수 방법 |
| 2. Baseline 소자 | 대칭 Si3N4 spacer SOI FinFET 구현, NMOS/PMOS Id-Vg/Id-Vd 수렴, Ion/Ioff/Vth/SS/DIBL/Cgd 추출 | baseline NMOS/PMOS를 inverter에 연결하기 위한 입력 파일/컬럼 정리, unit inverter 연결 규칙 정리 | baseline NMOS/PMOS 결과 파일, baseline metric CSV |
| 3. Proposed 소자 | `L_sp_S`, `L_sp_D`, `W_low_k` 적용, drain-side low-k composite spacer 구현, baseline 대비 device metric 비교 | proposed device의 drain-side composite spacer가 OUT 쪽을 향하도록 회로 연결 방향 정리 | proposed NMOS/PMOS 결과 파일, source/drain 방향 정보 |
| 4. DOE 실행 | initial DOE 48개, anchor case 생성/실행, 실패 case 기록, `all_results.csv` 정리 | DOE 결과를 회로 후보로 넘길 수 있도록 case_id/파일명/변수값 표준화 | DOE 결과 CSV, 실패 case 목록 |
| 5. Device screening | Ion/Ioff/SS/DIBL/Cgd 기준 Pareto 계산, active DOE 후보 추천, 회로 검증 후보 3~5개 선정 | 후보 3~5개에 대한 회로 실행 조건 준비: VDD, input pulse, transient time, load, 측정 기준 | 회로 검증 후보 목록 |
| 6. 회로 DTCO | 후보별 NMOS/PMOS 파일 제공, 소자 방향/source-drain 방향 검토 | unit inverter VTC, FO4 transient, tpHL/tpLH, delay, power, energy, EDP 추출, circuit Pareto 계산 | circuit-level 결과 CSV, FO4 waveform, circuit Pareto |
| 7. Local refinement | circuit Pareto 후보 주변 0.5 nm grid-snapped case 생성/실행 | local refinement 후보의 FO4 재평가, circuit Pareto 업데이트 | grid-snapped 최종 후보 |
| 8. Robust validation | 최종 후보 주변 ±0.3/±0.5 nm variation case 생성/실행, Ion/Cgd 유지율 계산 | robust case의 FO4 delay/EDP 열화율 계산, nominal vs robust optimum 비교 | robust summary table, robust optimum |
| 9. 최종 정리 | 구조도, 공정 흐름도, Id-Vg, device metric, DOE/Pareto 결과 정리 | FO4 회로도, waveform, delay/power/energy/EDP 그래프 정리 | 발표자료, 보고서, 포스터, 예상 질문 답변 |

---

## 2. 공정/소자설계 파트 진행 과정

이 파트의 목표:

```text
좋아 보이는 소자를 만든다.
즉 baseline 대비 Cgd, DIBL, SS, Ioff를 줄이면서 Ion 손실을 관리한다.
```

### 2.1 환경 및 원본 example

- [ ] 학교 TCAD PC 로그인
- [ ] Sentaurus/Silvaco 실행 환경 로드 방법 기록
- [ ] Sentaurus Process 또는 공정 시뮬레이터 실행 확인
- [ ] Sentaurus Device 또는 소자 시뮬레이터 실행 확인
- [ ] Sentaurus Visual/Inspect 또는 결과 viewer 실행 확인
- [ ] 실행 가능한 3D FinFET example 확보
- [ ] 원본 example을 수정하지 않고 1회 실행
- [ ] structure/mesh/Id-Vg 결과 확인
- [ ] 결과 파일 USB/외장 SSD로 복사 테스트
- [ ] 우리 repo를 TCAD PC로 복사 또는 `git clone` 가능 여부 확인

산출물:

- [ ] 원본 example 경로
- [ ] TCAD tool/version
- [ ] 실행 명령어 또는 GUI 실행 순서
- [ ] 실행 성공 스크린샷
- [ ] 결과 회수 방법

### 2.2 Baseline SOI FinFET

Baseline 정의:

```text
Source spacer = Si3N4
Drain spacer = Si3N4
양쪽 spacer 길이 동일
```

- [ ] 원본 FinFET example을 baseline 작업 폴더로 복사
- [ ] substrate/BOX/fin/gate/spacer/source/drain/contact 구조 확인
- [ ] 대칭 Si3N4 spacer 구조 확인
- [ ] 3D mesh 생성 및 viewer에서 확인
- [ ] NMOS Id-Vg 수렴
- [ ] NMOS Id-Vd 수렴
- [ ] PMOS Id-Vg 수렴
- [ ] PMOS Id-Vd 수렴
- [ ] Ion, Ioff, Vth, SS, DIBL, Cgd 추출
- [ ] baseline 구조와 지표 동결

산출물:

- [ ] baseline structure 그림
- [ ] baseline Id-Vg/Id-Vd 그래프
- [ ] baseline metric CSV

### 2.3 Proposed SOI FinFET

Proposed 정의:

```text
Source-side spacer = 짧은 Si3N4
Drain-side spacer = 긴 composite spacer
Drain-side spacer 내부 = SiO2 low-k 구간
```

설계 변수:

```text
L_sp_S  = source-side spacer 길이
L_sp_D  = drain-side spacer 길이
W_low_k = drain-side SiO2 low-k 구간 길이
```

- [ ] source-side 짧은 Si3N4 spacer 구현
- [ ] drain-side 긴 spacer 구현
- [ ] drain-side SiO2 low-k 구간 구현
- [ ] 실제 생성된 `L_sp_S`, `L_sp_D`, `W_low_k` 확인
- [ ] source/drain 방향 고정: x축 = Source → Drain
- [ ] proposed NMOS Id-Vg/Id-Vd 수렴
- [ ] proposed PMOS Id-Vg/Id-Vd 수렴
- [ ] baseline과 동일 bias/mesh/physics 조건인지 확인
- [ ] Ion, Ioff, Vth, SS, DIBL, Cgd 비교
- [ ] electric field, current density, Cgd 변화 확인

산출물:

- [ ] proposed structure 그림
- [ ] baseline vs proposed 비교표
- [ ] Id-Vg/Id-Vd 비교 그래프
- [ ] Cgd/Ion/DIBL 변화율

### 2.4 DOE 및 Device Screening

- [ ] `project.yaml`의 설계공간 확정
- [ ] `fabrication_grid.step_nm` 확정
- [ ] `python3 03_doe/generate_cases.py`로 initial DOE case 생성
- [ ] `python3 03_doe/generate_anchor_cases.py`로 anchor case 생성
- [ ] baseline, center, feasible corner 우선 실행
- [ ] DOE case 실행
- [ ] 실패 case와 원인 기록
- [ ] 모든 결과를 `05_results/summary/all_results.csv` 형태로 정리
- [ ] device screening 목적함수 확정: maximize Ion, minimize Ioff/DIBL/Cgd
- [ ] `python3 05_results/pareto.py`로 device Pareto 계산
- [ ] Cgd-Ion trade-off 확인
- [ ] `python3 03_doe/suggest_active_cases.py --mode device_screening`으로 active DOE 후보 추천
- [ ] 회로 검증 후보 3~5개 선정

산출물:

- [ ] `03_doe/cases/initial_doe_cases.csv`
- [ ] `03_doe/cases/anchor_cases.csv`
- [ ] `05_results/summary/all_results.csv`
- [ ] 실패 case 목록
- [ ] device Pareto plot
- [ ] Cgd vs Ion trade-off 그래프
- [ ] 회로 검증 후보 3~5개 목록

### 2.5 Local Refinement 및 Robust Case

- [ ] 회로 DTCO 결과를 받아 최종 후보 1~2개 선정
- [ ] `python3 03_doe/generate_local_refinement_cases.py`로 grid-snapped case 생성
- [ ] local refinement case 실행
- [ ] local refinement 결과를 `all_results.csv`에 병합
- [ ] `python3 03_doe/generate_robust_cases.py`로 robust case 생성
- [ ] 최종 후보 주변 ±0.3/±0.5 nm variation case 실행
- [ ] robust result CSV 작성
- [ ] Ion 유지율, Cgd 개선 유지율 계산

산출물:

- [ ] local refinement case list
- [ ] grid-snapped 최종 후보
- [ ] robust case list
- [ ] robust 소자 결과 CSV

---

## 3. 회로설계 파트 진행 과정

이 파트의 목표:

```text
소자에서 좋아 보이는 후보가 실제 inverter/FO4 회로에서도 좋은지 판정한다.
즉 Cgd 감소가 delay, power, energy, EDP 개선으로 이어지는지 확인한다.
```

### 3.1 회로 환경 및 benchmark 준비

- [ ] MixedMode 또는 회로 시뮬레이션 사용 가능 여부 확인
- [ ] 회로 예제 또는 TCAD-to-circuit 예제 위치 확인
- [ ] `04_circuit/inverter/inverter.cmd.template` 내용 확인
- [ ] `04_circuit/fo4/fo4_inverter_benchmark.cmd.template` 내용 확인
- [ ] unit inverter 구성 정리
- [ ] FO4 구성 정리: `IN -> INV_driver -> INV_DUT -> INV_load_4x`
- [ ] 회로 결과 CSV 템플릿 작성

산출물:

- [ ] unit inverter 연결 그림
- [ ] FO4 benchmark 그림
- [ ] 회로 결과 CSV 템플릿

### 3.2 회로 입력 조건 고정

- [ ] VDD 확정
- [ ] temperature 확정
- [ ] input pulse rise/fall/time period 조건 확정
- [ ] transient simulation time 확정
- [ ] load 조건 확정
- [ ] tpHL/tpLH 측정 기준 확정
- [ ] output slew 측정 기준 확정
- [ ] average power 계산 구간 확정
- [ ] energy per transition 계산식 확정
- [ ] EDP 계산식 확정

산출물:

- [ ] 회로 측정 기준 문서 또는 표
- [ ] delay/power/energy/EDP 계산식

### 3.3 Baseline 회로 sanity check

- [ ] baseline NMOS/PMOS 결과 파일 수령
- [ ] PMOS source = VDD, NMOS source = GND 연결 확인
- [ ] PMOS/NMOS gate = IN 연결 확인
- [ ] PMOS/NMOS drain = OUT 연결 확인
- [ ] unit inverter VTC 실행
- [ ] switching 정상 여부 확인
- [ ] baseline FO4 transient 실행
- [ ] baseline tpHL/tpLH/delay/power/energy/EDP 추출

산출물:

- [ ] baseline inverter VTC
- [ ] baseline FO4 waveform
- [ ] baseline 회로 metric CSV

### 3.4 Proposed 후보 회로 검증

중요 규칙:

```text
Proposed device의 drain-side composite spacer는 switching output node, 즉 OUT 쪽을 향해야 한다.
```

- [ ] 소자 파트에서 회로 검증 후보 3~5개 수령
- [ ] 후보별 NMOS/PMOS 파일 존재 여부 확인
- [ ] 후보별 source/drain 방향 확인
- [ ] unit inverter VTC 실행
- [ ] 정상 switching 후보만 FO4로 이동
- [ ] FO4 transient 실행
- [ ] tpHL/tpLH 추출
- [ ] FO4 delay 계산
- [ ] output slew 추출
- [ ] average power 추출
- [ ] energy per transition 추출
- [ ] EDP 계산
- [ ] circuit Pareto 계산

산출물:

- [ ] 후보별 inverter VTC
- [ ] 후보별 FO4 waveform
- [ ] delay/power/energy/EDP 표
- [ ] circuit Pareto plot
- [ ] 회로 기준 최종 후보 1~2개

### 3.5 Local Refinement 및 Robust 회로 검증

- [ ] 소자 파트에서 local refinement 후보 결과 수령
- [ ] local refinement 후보 FO4 재평가
- [ ] circuit Pareto 업데이트
- [ ] 소자 파트에서 robust case 결과 수령
- [ ] robust case의 FO4 delay/EDP 열화율 계산
- [ ] nominal optimum과 robust optimum 비교

산출물:

- [ ] local refinement 회로 결과 CSV
- [ ] robust 회로 결과 CSV
- [ ] robust summary table
- [ ] 최종 회로 결론

---

## 4. 두 파트 사이 데이터 전달 규칙

### 소자 파트 → 회로 파트

```csv
case_id,structure,l_sp_s_nm,l_sp_d_nm,w_low_k_nm,nmos_file,pmos_file,ion_A,ioff_A,vth_V,ss_mV_dec,dibl_mV_V,cgd_F,vdd_V,temperature_K,drain_direction,status,note
```

필수 전달 내용:

- [ ] case_id
- [ ] structure: baseline/proposed/doe/local_refinement/robust
- [ ] `L_sp_S`, `L_sp_D`, `W_low_k`
- [ ] NMOS 결과 파일
- [ ] PMOS 결과 파일
- [ ] Ion, Ioff, Vth, SS, DIBL, Cgd
- [ ] source/drain 방향
- [ ] VDD, temperature
- [ ] 수렴 여부와 warning

### 회로 파트 → 소자 파트

```csv
case_id,unit_inverter_ok,tpHL_s,tpLH_s,fo4_delay_s,output_slew_s,average_power_W,energy_per_transition_J,edp_Js,status,note
```

필수 전달 내용:

- [ ] unit inverter 정상 switching 여부
- [ ] tpHL
- [ ] tpLH
- [ ] FO4 delay
- [ ] output slew
- [ ] average power
- [ ] energy per transition
- [ ] EDP
- [ ] 회로 수렴 여부와 실패 원인
- [ ] waveform 파일

---

## 5. 최종 제출물

### 소자 중심 그림/표

- [ ] baseline/proposed 3D 구조 비교
- [ ] 공정 흐름도
- [ ] Id-Vg 및 Id-Vd 그래프
- [ ] Ion/Ioff/Vth/SS/DIBL/Cgd 비교표
- [ ] electric field/current density contour
- [ ] DOE response map
- [ ] device Pareto plot
- [ ] Cgd-Ion trade-off 그래프

### 회로 중심 그림/표

- [ ] unit inverter schematic
- [ ] FO4 benchmark schematic
- [ ] inverter VTC
- [ ] FO4 transient waveform
- [ ] delay/power/energy/EDP 비교표
- [ ] circuit Pareto plot
- [ ] robust EDP degradation plot

### 공통 문서

- [ ] 선행연구 비교표
- [ ] 연구윤리/표절 방지 문장
- [ ] 보고서
- [ ] 포스터
- [ ] 발표자료
- [ ] 예상 질문 답변

최종 스토리:

```text
기존 asymmetric/low-k spacer 연구는 존재한다.
본 프로젝트는 SOI FinFET에서 drain-side low-k composite spacer 설계공간을 정의하고,
device metric뿐 아니라 FO4 회로 성능과 공정 편차 robust성까지 기준으로 최적 후보를 선정했다.
```

---

## 6. 연구윤리 및 표절 방지

- [ ] R01 Pal et al. 2015를 asymmetric dual-spacer/device-circuit codesign 직접 선행연구로 본문에 인용
- [ ] R03 또는 R05를 spacer capacitance와 inverter delay 연결 근거로 인용
- [ ] R06 또는 R08을 electric field, underlap, spacer trade-off 물리 근거로 인용
- [ ] R11 또는 R12를 low-k/hybrid spacer 공정 및 parasitic capacitance reduction 근거로 인용
- [ ] R16을 LHS/DOE 방법론 근거로 인용
- [ ] "최초 제안", "최초 연결", "실제 제작 검증", "실측 결과" 표현이 남아 있지 않은지 확인
- [ ] `suggest_active_cases.py` 구현 범위를 lightweight surrogate-assisted active DOE로 설명
- [ ] 실제 구현하지 않은 ANN/MOBO/NSGA-II 사용 주장을 제거
- [ ] 논문 figure를 그대로 복제하지 않고 직접 작성한 schematic과 출처 인용만 사용
- [ ] 유료 논문 PDF와 proprietary Sentaurus/Silvaco deck이 Git에 포함되지 않았는지 확인
- [ ] TCAD 결과, mock 결과, 실제 측정 결과를 표/그림 caption에서 명확히 구분

---

## 7. Codex에 다시 물어볼 때 쓰는 양식

```text
현재 파트: 공정/소자설계 또는 회로설계
현재 단계:
내가 하려는 작업:
현재 가진 파일/결과:
막힌 부분:
오늘 확보해야 하는 산출물:
```

TCAD 실행 1건마다 기록할 내용:

```text
날짜:
실행자:
case_id:
structure: baseline / proposed / doe / fo4 / robust
사용 deck:
변수:
  L_sp_S:
  L_sp_D:
  W_low_k:
실행 명령어:
결과:
  success / fail / partial
생성 파일:
에러 메시지 또는 warning:
다음에 확인할 점:
```

Codex에 에러를 물어볼 때 붙여 넣을 최소 정보:

- [ ] 실행한 deck 파일 또는 수정한 부분
- [ ] terminal/log의 마지막 50~100줄
- [ ] structure/mesh 또는 plot screenshot
- [ ] 기대한 결과와 실제 결과의 차이
- [ ] case_id와 변수값

---

## 8. 최소 성공 기준

- [ ] 환경 확인: 원본 example 1회 실행
- [ ] Baseline: baseline NMOS Id-Vg 확보
- [ ] Proposed: proposed NMOS Id-Vg 확보
- [ ] DOE: anchor + DOE 15~20개 이상 확보
- [ ] Device screening: 회로 후보 3~5개 선정
- [ ] 회로 DTCO: 최소 1~2개 후보 FO4 delay/EDP 확보
- [ ] Robust validation: 최종 후보 1개 variation 검증
- [ ] 제출: 표절 위험 표현 제거, 직접 만든 그림 사용
