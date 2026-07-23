# TODO

## 0. 환경 및 원본

- [ ] Git 원격 저장소를 개인 노트북과 학교 TCAD PC 양쪽에서 clone/pull/push 가능하게 설정
- [ ] 학교 TCAD PC에서 `python check_project.py` 실행
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
- [ ] NMOS Id–Vg 수렴
- [ ] NMOS Id–Vd 수렴
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

## 3. DOE

- [ ] 실제 공정 가능 범위 확정
- [ ] `project.yaml` 범위 확정
- [ ] LHS 또는 Sobol 초기 case 생성
- [ ] Baseline 및 corner case 우선 실행
- [ ] 전체 case 실행
- [ ] 실패 case와 원인 기록
- [ ] 모든 결과를 하나의 CSV로 정리
- [ ] Pareto front 계산
- [ ] 후보 3개 선정

## 4. 회로

- [ ] NMOS/PMOS 데이터를 회로에 연결
- [ ] CMOS inverter VTC
- [ ] Noise margin
- [ ] tpHL, tpLH
- [ ] Static power
- [ ] Switching energy
- [ ] PDP 또는 EDP
- [ ] Ring oscillator frequency
- [ ] Ring oscillator power

## 5. 검증

- [ ] Pareto 후보 직접 재실행
- [ ] `generate_robust_cases.py`로 후보 주변 ±0.3~0.5 nm 공정 편차 case 생성
- [ ] 공정 편차 case TCAD 재실행
- [ ] `robust_optimum.py` 입력용 `robust_results.csv` 작성
- [ ] Ion 유지율, EDP 열화율, Cgd 개선 유지율 계산
- [ ] Cgd 개선 대비 Ion 손실 보상율 계산
- [ ] Hold-out case 검증
- [ ] Mesh sensitivity 확인
- [ ] VDD 및 온도 조건 확인
- [ ] Nominal optimum과 robust optimum 비교

## 6. 제출

- [ ] 구조 정의도
- [ ] Baseline–Proposed 3D 비교
- [ ] 공정 흐름도
- [ ] Id–Vg 및 핵심 지표 그래프
- [ ] 전계/Cgd Heatmap
- [ ] Inverter Power–Delay 결과
- [ ] Pareto front
- [ ] 보고서
- [ ] 포스터
- [ ] 발표자료
