# OASIS-FinFET

## 주제

**SOI 기반 출력 노드 지향 비대칭 Composite Spacer 3D FinFET의 공정–소자–회로 공동 최적화**

영문 가제:

**Process–Device–Circuit Co-Optimization of an Output-Oriented Asymmetric Composite Spacer in a 3D SOI FinFET**

---

## 핵심 아이디어

기준 소자는 Source와 Drain 양쪽에 같은 `Si3N4` spacer를 갖는 3D SOI FinFET이다.

제안 구조는 다음처럼 바꾼다.

- Source-side spacer: 짧은 `Si3N4`
- Drain-side spacer: 더 긴 composite spacer
- Drain-side spacer 내부: `SiO2` low-k 구간
- NMOS와 PMOS의 Drain이 CMOS inverter의 출력 노드 `OUT`을 향하도록 배치

목표는 Drain 쪽의 `Cgd`, 전계 집중, DIBL, 누설전류를 낮추면서 Source 쪽의 구동전류 손실을 최소화하는 것이다.

---

## 소자 구조 참고 그림

![Device structure sketch](05_results/figures/device_structure_sketch.jpg)

위 손그림은 제안 SOI FinFET의 source-side spacer, TiN/HfO2 gate stack, drain-side composite spacer, `L_sp_S`, `L_sp_D`, `W_low_k` 정의를 정리한 소자 구조 참고 그림이다.

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

- CMOS inverter VTC
- Noise margin
- tpHL, tpLH
- Static power
- Switching energy
- PDP 또는 EDP
- Ring oscillator frequency 및 power

### 최적화

- 전체 DOE 결과
- Pareto front
- Hold-out 검증
- 최적점 주변 재검증
- 공정 편차에 강한 robust optimum

---

## 폴더 구조

```text
00_original_example/   원본 TCAD example 보존
01_baseline/           대칭 spacer SOI FinFET
02_proposed/           비대칭 composite spacer SOI FinFET
03_doe/                설계공간, case 생성, batch 실행
04_circuit/            inverter와 ring oscillator
05_results/            원본 결과, 요약 CSV, 최종 그림
06_submission/         보고서, 포스터, 발표자료
README.md              연구 전체 설명
TODO.md                실제 진행 순서
project.yaml           공통 파라미터
```

불필요한 계획 문서는 추가하지 않는다. 새로운 결정과 현재 진행상황은 `TODO.md`에만 갱신한다.

---

## 진행 순서

```text
원본 example 실행
→ SOI single-fin baseline 재현
→ baseline 전기특성 검증
→ proposed spacer 구현
→ DOE
→ 후보 선정
→ PMOS 및 회로 검증
→ robust optimum
→ 최종 그림과 제출물
```

---

## 파일 원칙

1. `00_original_example`의 원본 파일은 수정하지 않는다.
2. 실행 가능한 baseline이 생기기 전에는 DOE case를 대량 생성하지 않는다.
3. Baseline과 Proposed는 핵심 spacer 조건 외에 동일한 조건을 사용한다.
4. 실패한 case와 log도 삭제하지 않는다.
5. 결과가 나온 뒤 목적함수와 합격조건을 임의로 변경하지 않는다.
6. TCAD 결과를 실제 제작 결과처럼 표현하지 않는다.
7. 대용량 raw output은 Git에 올리지 않는다.

---

## 파일 이름 예시

```text
baseline_nmos_idvg.tdr
proposed_nmos_LSS05_LSD09_WLK03.tdr
case_LSS05_LSD09_WLK03.csv
inverter_LSS05_LSD09_WLK03_vtc.csv
```

---

## 시작 명령

이 폴더를 현재 작업공간에 복사한 뒤:

```bash
cd ~/DISU_POLARIS_WS/DISU_WS
code .
```

Python 환경:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python check_project.py
```

DOE 파일 생성 예시:

```bash
python 03_doe/generate_cases.py \
  --samples 24 \
  --method lhs \
  --seed 20260723
```

---

## 완료 기준

- Baseline SOI 3D FinFET 구조 및 NMOS/PMOS 수렴
- Proposed composite spacer 구조 및 NMOS/PMOS 수렴
- 공정·소자 결과의 공정 조건별 정량 비교
- CMOS inverter Power/Delay 검증
- DOE와 Pareto 분석
- 독립 검증 및 robust optimum
- 보고서·포스터·발표자료 완성
