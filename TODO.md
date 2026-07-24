# TODO

## 0. 환경 및 원본

- [ ] Git 원격 저장소를 개인 노트북과 학교 TCAD PC 양쪽에서 clone/pull/push 가능하게 설정
- [ ] 개인 노트북에서 `python3 check_project.py` 실행
- [ ] 학교 TCAD PC에서 `python3 check_project.py` 실행
- [ ] 학교 TCAD PC에서 Sentaurus/Silvaco 실행 환경 로드 방법 기록
- [ ] Sentaurus Process 사용 가능 확인
- [ ] Sentaurus Device 사용 가능 확인
- [ ] Sentaurus Visual/Inspect 사용 가능 확인
- [ ] MixedMode 사용 가능 여부 확인
- [ ] 실행 가능한 3D FinFET example 확보
- [ ] 원본 example을 `00_original_example/`에 그대로 보존
- [ ] 원본 example을 수정하지 않고 1회 실행

## 1. Baseline SOI FinFET

- [ ] substrate와 BOX 생성
- [ ] single Si Fin 생성
- [ ] gate dielectric 형성
- [ ] gate metal 형성
- [ ] 대칭 Si3N4 spacer 형성
- [ ] source/drain 형성
- [ ] contact와 electrode 지정
- [ ] 3D mesh 검증
- [ ] NMOS Id-Vg 수렴
- [ ] NMOS Id-Vd 수렴
- [ ] SS, Vth, DIBL, Ion, Ioff 추출
- [ ] PMOS baseline 수렴
- [ ] baseline 구조와 지표 동결

## 2. Proposed 구조

- [ ] source-side 짧은 Si3N4 spacer 구현
- [ ] drain-side 긴 spacer 구현
- [ ] drain-side SiO2 low-k 구간 구현
- [ ] 실제 생성된 L_sp_S, L_sp_D, W_low_k 측정
- [ ] Proposed NMOS 수렴
- [ ] Baseline과 동일 조건 비교
- [ ] 전계, current density, Cgd 변화 확인
- [ ] Proposed PMOS 수렴

## 3. DOE 및 Anchor Case

- [ ] 실제 공정 가능 범위 확정
- [ ] `project.yaml`의 `design_space` 범위 확정
- [ ] `project.yaml`의 `fabrication_grid.step_nm` 확정
- [ ] Initial DOE sample 수를 48개로 유지할지 최종 확인
- [ ] `generate_cases.py`로 initial DOE 48개 생성
- [ ] `generate_anchor_cases.py`로 baseline, center, feasible corner case 생성
- [ ] Baseline 및 anchor case 우선 실행
- [ ] Initial DOE 전체 case 실행
- [ ] 실패 case와 원인 기록
- [ ] 모든 결과를 `05_results/summary/all_results.csv`로 정리

## 4. Device Screening 및 Surrogate-Assisted Active DOE

- [ ] Device screening 목적함수 확정: maximize Ion, minimize Ioff/DIBL/Cgd
- [ ] `pareto.py`로 initial DOE + anchor 결과의 device screening Pareto 계산
- [ ] `suggest_active_cases.py --mode device_screening`으로 추가 실행할 active DOE 후보 추천
- [ ] 추천 후보가 기존 case와 충분히 떨어져 있는지 확인
- [ ] 추천 후보의 fabrication grid snapping 여부 확인
- [ ] Device active DOE 후보 TCAD 실행
- [ ] Active DOE 결과를 `all_results.csv`에 병합
- [ ] Active DOE 전후 device screening Pareto 변화 비교

## 5. Circuit-Level DTCO 및 Fabrication-Aware Local Refinement

- [ ] Device screening으로 살아남은 후보의 PMOS 및 회로 검증 우선순위 선정
- [ ] Unit inverter VTC로 switching 정상 후보만 유지
- [ ] FO4 inverter benchmark 기준 `fo4_delay_s`, `average_power_W`, `energy_per_transition_J`, `edp_Js` 추출
- [ ] Circuit DTCO 목적함수 확정: minimize FO4 delay/power/energy/EDP
- [ ] `pareto.py`로 circuit-level DTCO Pareto 계산
- [ ] Circuit DTCO Pareto 후보 3개 선정
- [ ] `generate_local_refinement_cases.py`로 circuit Pareto 후보 주변 grid-snapped case 생성
- [ ] 3.12 nm 같은 연속 DOE 후보가 최종 주장에 직접 쓰이지 않도록 확인
- [ ] Local refinement case TCAD 실행
- [ ] Local refinement 결과를 `all_results.csv`에 병합
- [ ] Grid-snapped 후보 기준으로 circuit-level DTCO Pareto 재계산

## 6. Robust Validation

- [ ] `generate_robust_cases.py`로 후보 주변 ±0.3/±0.5 nm 공정 편차 case 생성
- [ ] 공정 편차 case TCAD 재실행
- [ ] `robust_optimum.py` 입력용 `robust_results.csv` 작성
- [ ] Ion 유지율, EDP 열화율, Cgd 개선 유지율 계산
- [ ] Cgd 개선 대비 Ion 손실 보상율 계산
- [ ] Mesh sensitivity 확인
- [ ] VDD 및 온도 조건 확인
- [ ] Nominal circuit optimum과 robust DTCO optimum 비교

## 7. 회로

- [ ] NMOS/PMOS 데이터를 회로에 연결
- [ ] Unit inverter VTC로 NMOS/PMOS 연결 방향 및 switching 정상 동작 확인
- [ ] FO4 inverter benchmark 구성
- [ ] FO4 transient switching 수렴
- [ ] tpHL/tpLH 추출
- [ ] FO4 delay 추출
- [ ] Output slew 추출
- [ ] Average power 추출
- [ ] Energy per transition 추출
- [ ] FO4 기준 PDP 또는 EDP 계산

## 8. 제출

- [ ] 구조 정의도
- [ ] Baseline-Proposed 3D 비교
- [ ] 공정 흐름도
- [ ] Id-Vg 및 핵심 지표 그래프
- [ ] 전계/Cgd Heatmap
- [ ] Active DOE 알고리즘 흐름도
- [ ] Grid snapping 및 local refinement 설명 그림
- [ ] FO4 waveform 및 Power-Delay 결과
- [ ] Device screening Pareto front
- [ ] Circuit-level DTCO Pareto front
- [ ] Robust optimum summary
- [ ] 보고서
- [ ] 포스터
- [ ] 발표자료

## 9. 연구윤리 및 표절 방지

- [ ] R01 Pal et al. 2015를 asymmetric dual-spacer/device-circuit codesign 직접 선행연구로 본문에 인용
- [ ] R03 또는 R05를 spacer capacitance와 inverter delay 연결 근거로 인용
- [ ] R06 또는 R08을 electric field, underlap, spacer trade-off 물리 근거로 인용
- [ ] R11 또는 R12를 low-k/hybrid spacer 공정 및 parasitic capacitance reduction 근거로 인용
- [ ] R16을 LHS/DOE 방법론 근거로 인용
- [ ] "최초 제안", "최초 연결", "실제 제작 검증", "실측 결과" 표현이 남아 있지 않은지 확인
- [ ] `suggest_active_cases.py` 구현 범위를 lightweight surrogate-assisted active DOE로 설명하고, 실제 구현하지 않은 ANN/MOBO/NSGA-II 사용 주장을 제거
- [ ] 논문 figure를 그대로 복제하지 않고 직접 작성한 schematic과 출처 인용만 사용
- [ ] 유료 논문 PDF와 proprietary Sentaurus/Silvaco deck이 Git에 포함되지 않았는지 확인
- [ ] TCAD 결과, mock 결과, 실제 측정 결과를 표/그림 caption에서 명확히 구분
