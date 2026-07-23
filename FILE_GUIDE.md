# FILE GUIDE

이 문서는 `DISU_FinFET_Simple_WS` 프로젝트에 존재하는 **모든 파일의 역할, 수정 시점, 생성 주체**를 한 곳에 정리한 문서다.

별도의 폴더별 설명 문서는 두지 않는다. 프로젝트 설명은 `README.md`, 진행 상황은 `TODO.md`, 모든 파일 설명은 이 `FILE_GUIDE.md`만 사용한다.

---

# 1. 최상위 파일

## `README.md`

### 역할
프로젝트의 전체 연구 방향을 설명하는 대표 문서다.

### 포함 내용
- 연구 주제
- Baseline 구조와 Proposed 구조
- 좌표축 정의
- 주요 공정 변수
- 소자 및 회로 평가 지표
- 전체 프로젝트 진행 흐름
- 파일 관리 원칙
- 완료 기준

### 언제 수정하는가
연구 주제, 구조, 평가 기준처럼 **프로젝트 전체에 영향을 주는 내용이 확정적으로 바뀔 때만** 수정한다.

### 누가 수정하는가
팀 전체 합의 후 한 명이 정리한다.

---

## `TODO.md`

### 역할
프로젝트의 실제 진행 순서를 체크박스로 관리한다.

### 포함 내용
- 환경 확인
- Baseline 구조 생성
- Proposed 구조 생성
- DOE
- 회로 검증
- 최적점 검증
- 제출물 제작

### 언제 수정하는가
작업을 시작하거나 완료할 때 체크 상태를 갱신한다.

### 주의
실험 결과나 긴 설명을 이 파일에 적지 않는다.  
`TODO.md`는 **현재 무엇을 해야 하는지**만 보여줘야 한다.

---

## `FILE_GUIDE.md`

### 역할
현재 프로젝트에 존재하는 모든 파일과 폴더의 용도를 설명한다.

### 언제 수정하는가
새 파일을 추가하거나 기존 파일의 역할이 바뀌었을 때 수정한다.

### 주의
프로젝트의 연구 배경은 `README.md`, 진행률은 `TODO.md`에 적는다.  
이 문서는 오직 **파일 설명서**로 사용한다.

---

## `project.yaml`

### 역할
프로젝트 전체에서 공통으로 사용할 설정과 설계변수를 저장한다.

### 현재 포함 내용

#### 프로젝트 정보
- 프로젝트명
- 소자 종류

#### 좌표축
- `x`: Source → Drain
- `y`: Fin 폭
- `z`: Fin 높이

#### 고정 파라미터
- Gate length
- Fin height
- Fin width
- EOT
- VDD
- Temperature

#### 재료
- Fin: Silicon
- BOX: SiO2
- Gate dielectric: HfO2
- Gate metal: TiN
- Baseline spacer: Si3N4
- Low-k: SiO2

#### DOE 변수 범위
- `L_sp_S`
- `L_sp_D`
- `W_low_k`

#### 제약조건
- `L_sp_D >= L_sp_S`
- `W_low_k <= L_sp_D`

#### 재현성 설정
- Random seed
- 실패 Run 보존 여부

### 언제 수정하는가
Baseline 치수와 실제 공정 가능 범위가 확정될 때 수정한다.

### 주의
결과를 확인한 뒤 좋은 결과가 나오도록 범위를 몰래 바꾸면 안 된다.  
범위 변경 시 Git commit과 이유를 남긴다.

---

## `requirements.txt`

### 역할
Python 분석 환경에서 필요한 패키지 목록을 저장한다.

### 현재 패키지
- `numpy`: 수치 계산
- `pandas`: CSV 및 표 데이터 처리
- `scipy`: LHS/Sobol 등 DOE 계산
- `matplotlib`: 그래프 작성
- `PyYAML`: `project.yaml` 읽기

### 실행 방법

```bash
pip install -r requirements.txt
```

### 언제 수정하는가
새 Python 라이브러리가 실제로 필요할 때만 추가한다.

---

## `check_project.py`

### 역할
필수 파일과 폴더가 존재하는지 검사한다.

### 검사 대상
- `README.md`
- `TODO.md`
- `project.yaml`
- 번호별 주요 폴더

### 실행 방법

```bash
python check_project.py
```

### 정상 출력

```text
[OK] 간소화 프로젝트 구조가 정상입니다.
```

### 언제 수정하는가
필수 폴더 구조가 바뀔 때 검사 목록을 수정한다.

---

## `install_here.sh`

### 역할
배포받은 프로젝트 골격을 실제 작업 폴더에 복사한다.

### 기본 설치 위치

```text
~/DISU_POLARIS_WS/DISU_WS
```

### 실행 예시

```bash
bash install_here.sh
```

다른 경로에 설치하려면:

```bash
bash install_here.sh /원하는/경로
```

### 언제 사용하는가
프로젝트 골격을 처음 설치할 때만 사용한다.

### 설치 후
정상 설치 후에는 삭제해도 프로젝트 실행에 영향이 없다.

---

## `.gitignore`

### 역할
Git에 올리지 않을 파일을 지정한다.

### 제외되는 주요 항목
- `.venv/`
- Python cache
- VS Code 개인 설정
- TCAD 결과 파일
- Mesh 및 구조 파일
- Log와 임시 파일
- 자동 생성 DOE case
- 대용량 raw output

### 왜 필요한가
TCAD 결과 파일은 크기가 크고 다시 생성할 수 있기 때문에 저장소를 불필요하게 무겁게 만든다.

### 언제 수정하는가
새로운 자동 생성 파일 형식이 생겼을 때 추가한다.

---

## `TREE.txt`

### 역할
현재 폴더 구조를 텍스트로 보여준다.

### 주의
자동으로 프로젝트 동작에 사용되는 파일은 아니다.  
사람이 구조를 빠르게 확인하기 위한 참고 파일이다.

### 갱신 방법

```bash
find . -maxdepth 3 -not -path "./.git/*" | sort > TREE.txt
```

---

# 2. `00_original_example`

## `00_original_example/.gitkeep`

### 역할
폴더가 비어 있어도 Git이 `00_original_example` 폴더를 추적하게 한다.

### 수정 여부
수정하지 않는다.

### 삭제 가능 여부
실제 원본 예제 파일이 폴더에 들어오면 삭제해도 된다.

---

## 이 폴더에 나중에 들어갈 파일

학교 서버 또는 Sentaurus 설치환경에서 제공하는 원본 FinFET 예제를 그대로 복사한다.

예상 파일:
- SProcess Deck
- SDevice Deck
- Workbench project
- Parameter file
- 실행 script
- 예제 결과

### 원칙
원본 예제는 수정하지 않는다.  
수정이 필요한 파일은 `01_baseline`으로 복사한 뒤 변경한다.

---

# 3. `01_baseline`

Baseline은 양쪽에 동일한 `Si3N4` spacer를 가진 SOI single-fin FinFET이다.

## `01_baseline/process/baseline_sprocess.cmd.template`

### 역할
Baseline 3D SOI FinFET 구조를 만드는 SProcess Deck의 초안이다.

### 구현할 구조
1. Si substrate
2. BOX
3. Silicon Fin
4. HfO2 gate dielectric
5. TiN gate
6. 대칭 Si3N4 spacer
7. Source/Drain
8. Contact
9. Mesh

### 파일 확장자 의미
- `.cmd`: Sentaurus 입력 Deck에서 자주 쓰는 확장자
- `.template`: 아직 실행 가능한 최종 Deck이 아니라는 표시

### 언제 수정하는가
원본 예제가 정상 실행된 뒤, 설치된 Sentaurus 버전 문법에 맞춰 채운다.

### 최종 상태
검증이 끝나면 다음처럼 실행용 파일을 별도로 만들 수 있다.

```text
baseline_sprocess.cmd
```

원본 template은 남겨두거나 실제 실행 Deck으로 이름을 변경한다.

---

## `01_baseline/device/baseline_nmos_sdevice.cmd.template`

### 역할
Baseline NMOS의 전기적 특성을 계산하는 SDevice Deck 초안이다.

### 입력
Baseline SProcess에서 생성한 3D 구조 및 mesh.

### 계산할 항목
- Equilibrium
- Low-VDS Id–Vg
- High-VDS Id–Vg
- Id–Vd
- Ion
- Ioff
- Vth
- SS
- DIBL
- Cgd, Cgs, Cgg

### 언제 수정하는가
Baseline SProcess 구조의 region과 contact 이름이 확정된 뒤 수정한다.

### 주의
Proposed NMOS와 동일한 physics model, bias 조건, metric 정의를 사용해야 한다.

---

## `01_baseline/device/baseline_pmos_sdevice.cmd.template`

### 역할
Baseline PMOS의 전기적 특성을 계산하는 SDevice Deck 초안이다.

### NMOS 파일과 다른 부분
- Source/Drain doping type
- Channel doping type
- Gate work function
- Bias 부호
- 전류 부호 처리

### 동일하게 유지할 부분
- Mesh 기준
- 온도
- Metric 추출법
- VDD 절댓값
- Solver 기준

---

## `01_baseline/output/.gitkeep`

### 역할
`output` 폴더가 비어 있어도 Git에 유지되게 한다.

### 나중에 이 폴더에 들어갈 파일
- `.tdr`: 구조 및 mesh 결과
- `.plt`: 전기적 결과
- `.log`: 실행 log
- `.csv`: 추출 metric
- 구조 screenshot

### 수정 여부
수정하지 않는다.

### 삭제 가능 여부
실제 결과 파일이 생성되면 삭제해도 된다.

---

# 4. `02_proposed`

Proposed 구조는 Source와 Drain의 spacer를 다르게 설계한 SOI FinFET이다.

## `02_proposed/process/proposed_sprocess.cmd.template`

### 역할
비대칭 composite spacer 구조를 만드는 SProcess Deck 초안이다.

### 주요 입력 변수
- `L_SP_S_NM`: Source-side spacer 길이
- `L_SP_D_NM`: Drain-side spacer 총길이
- `W_LOW_K_NM`: Drain-side spacer 내부 low-k 구간 길이

### 구현할 변화
- Source-side: 짧은 Si3N4 spacer
- Drain-side: 긴 spacer
- Drain-side 내부: SiO2 low-k 영역

### Baseline과 동일하게 유지할 항목
- Gate length
- Fin width
- Fin height
- EOT
- Gate material
- Channel doping
- Source/Drain doping
- Temperature

### 언제 수정하는가
Baseline SProcess Deck이 완전히 검증된 뒤 복사하여 spacer 부분만 변경한다.

---

## `02_proposed/device/proposed_nmos_sdevice.cmd.template`

### 역할
Proposed NMOS를 해석하는 SDevice Deck 초안이다.

### 비교 대상
`01_baseline/device/baseline_nmos_sdevice.cmd.template`

### 특별히 확인할 항목
- Drain-side electric field
- Cgd
- Ioff
- DIBL
- Ion 감소량
- Potential distribution
- Current density

### 원칙
Baseline과 같은 bias와 같은 metric 추출 기준을 사용한다.

---

## `02_proposed/device/proposed_pmos_sdevice.cmd.template`

### 역할
Proposed PMOS를 해석하는 SDevice Deck 초안이다.

### 목적
3-stage ring oscillator를 구성하려면 NMOS뿐 아니라 PMOS의 Proposed 구조도 필요하다.

### 확인할 항목
- NMOS와 같은 device metric
- PMOS drive current
- NMOS/PMOS drive balance
- Unit inverter switching 및 ring oscillator stage 동작 변화

---

## `02_proposed/output/.gitkeep`

### 역할
빈 `output` 폴더를 Git에 유지한다.

### 나중에 저장될 파일
- Proposed 3D 구조
- NMOS/PMOS 결과
- Field map
- Capacitance 결과
- Metric CSV
- 실행 log

---

# 5. `03_doe`

DOE 폴더는 임의의 몇 점만 선택하는 Cherry-picking을 막고 전체 설계공간을 체계적으로 탐색한다.

## `03_doe/generate_cases.py`

### 역할
`project.yaml`의 설계범위를 읽어서 DOE 조건을 생성한다.

### 지원 방식
- LHS: Latin Hypercube Sampling
- Sobol sequence

### 입력 인자
- `--samples`: 생성할 case 수
- `--method`: `lhs` 또는 `sobol`
- `--seed`: Random seed

### 실행 예시

```bash
python 03_doe/generate_cases.py \
  --samples 24 \
  --method lhs \
  --seed 20260723
```

### 생성 파일

```text
03_doe/cases.csv
```

### 생성되는 열
- `case_id`
- `l_sp_s_nm`
- `l_sp_d_nm`
- `w_low_k_nm`
- `status`

### 자동 적용 제약
- `L_sp_D >= L_sp_S`
- `W_low_k <= L_sp_D`

### 언제 수정하는가
설계변수 개수 또는 제약조건이 바뀔 때 수정한다.

---

## `03_doe/template/master_case.cmd.template`

### 역할
검증된 Proposed Golden Deck을 DOE case별로 복제할 때 사용하는 공통 template이다.

### 치환 변수
- `{{CASE_ID}}`
- `{{L_SP_S_NM}}`
- `{{L_SP_D_NM}}`
- `{{W_LOW_K_NM}}`

### 사용 흐름
1. 검증된 Proposed Deck 내용을 넣는다.
2. Python script가 각 변수 값을 치환한다.
3. `03_doe/cases`에 case별 실행 Deck을 생성한다.

### 주의
Baseline 또는 Proposed Golden Deck이 검증되기 전에는 이 template을 확정하지 않는다.

---

## `03_doe/cases/.gitkeep`

### 역할
자동 생성 case가 없을 때 폴더를 유지한다.

### 나중에 들어갈 파일
- `C001/`
- `C002/`
- `C003/`
- Case별 `.cmd`
- Case별 parameter file

### 수정 여부
수정하지 않는다.

---

## `03_doe/output/.gitkeep`

### 역할
DOE 결과 폴더를 Git에 유지한다.

### 나중에 들어갈 파일
- Case별 log
- Case별 metric CSV
- 수렴 실패 기록
- Batch 실행 요약

---

# 6. `04_circuit`

공정 및 소자 변화가 3-stage ring oscillator의 Power와 Delay에 미치는 영향을 검증한다.

## `04_circuit/inverter/inverter.cmd.template`

### 역할
NMOS와 PMOS를 CMOS unit inverter로 연결하는 sanity-check용 MixedMode 또는 회로 Deck 초안이다.

### 회로 연결
- PMOS Source → VDD
- NMOS Source → GND
- PMOS/NMOS Gate → IN
- PMOS/NMOS Drain → OUT

### 구조 방향
NMOS와 PMOS 모두 긴 Drain-side composite spacer가 출력 노드 `OUT` 방향을 향해야 한다.

### 계산할 항목
- VTC
- Switching threshold
- NMH
- NML
- transient switching 정상 동작

### 언제 수정하는가
Baseline과 Proposed NMOS/PMOS가 모두 수렴한 뒤, 3-stage ring oscillator 구성 전에 수정한다.

---

## `04_circuit/ring_oscillator/ring_oscillator.cmd.template`

### 역할
3-stage ring oscillator를 구성하는 primary circuit validation Deck 초안이다.

### 계산할 항목
- Oscillation frequency
- Stage delay
- Average power
- Energy per cycle
- PDP 또는 EDP

### 프로젝트 내 역할
- 공정 변화가 실제 반복 스위칭 성능에 미치는 영향 확인
- 회로 성능 중심 Pareto 후보 선정에 사용할 primary metric 제공
- 필요하면 Virtual R2R의 circuit sentinel로 확장 가능

### 언제 수정하는가
Unit inverter가 정상 동작한 뒤 확장한다.

---

## `04_circuit/output/.gitkeep`

### 역할
회로 결과 폴더를 Git에 유지한다.

### 나중에 들어갈 파일
- VTC CSV
- Transient waveform
- Delay summary
- Power summary
- Ring oscillator waveform
- 회로 log

---

# 7. `05_results`

공정, 소자, 회로 결과를 한 곳에 모으고 최종 분석을 수행한다.

## `05_results/pareto.py`

### 역할
여러 목적함수에 대해 Pareto front를 계산한다.

### 입력
Case별 metric이 포함된 CSV.

### 실행 예시

```bash
python 05_results/pareto.py \
  --input 05_results/summary/all_metrics.csv \
  --objectives ioff_A cgd_F edp_Js
```

### 출력

```text
05_results/summary/pareto.csv
```

### 계산 의미
다른 후보보다 모든 목적함수에서 동시에 나쁜 조건을 제거하고 비지배해만 남긴다.

### 주의
- `Ion`처럼 최대화할 값은 부호를 바꾸거나 constraint로 처리해야 한다.
- NaN이 있는 case는 원인을 별도로 기록해야 한다.
- Pareto 결과만으로 최종 구조를 선택하지 않고 재검증해야 한다.

---

## `05_results/raw/.gitkeep`

### 역할
원본 결과 폴더를 유지한다.

### 나중에 들어갈 파일
- TCAD에서 직접 추출한 CSV
- Circuit raw CSV
- Case별 metric 원본
- 원본 값 변환 전 데이터

### 원칙
Raw 파일의 값을 수동으로 수정하지 않는다.

---

## `05_results/summary/.gitkeep`

### 역할
요약 결과 폴더를 유지한다.

### 나중에 들어갈 대표 파일

#### `all_metrics.csv`
한 행이 한 DOE case인 통합 데이터.

예상 열:
- Case ID
- L_sp_S
- L_sp_D
- W_low_k
- Ion
- Ioff
- SS
- DIBL
- Cgd
- Delay
- Power
- EDP
- Status

#### `pareto.csv`
Pareto front에 포함된 후보.

#### `validated_candidates.csv`
직접 재시뮬레이션으로 검증된 후보.

---

## `05_results/figures/.gitkeep`

### 역할
최종 Figure 폴더를 유지한다.

### 나중에 들어갈 그림
- Baseline vs Proposed 3D 구조
- Id–Vg
- Ion/Ioff
- SS
- DIBL
- Electric field
- Cgd heatmap
- Unit inverter VTC
- 3-stage ring oscillator waveform
- RO3 Delay–Power
- Pareto front
- Robust optimum

### 원칙
Figure 파일명에 내용이 드러나도록 이름을 붙인다.

예:

```text
fig01_structure_comparison.png
fig02_idvg_nmos.png
fig03_pareto_edp_ioff.png
```

---

# 8. `06_submission`

대회에 실제 제출하는 최종 산출물을 관리한다.

## `06_submission/report/.gitkeep`

### 역할
보고서 폴더를 유지한다.

### 나중에 들어갈 파일
- 보고서 원본
- 제출 PDF
- 표와 부록

예:

```text
final_report.docx
final_report.pdf
```

---

## `06_submission/poster/.gitkeep`

### 역할
포스터 폴더를 유지한다.

### 나중에 들어갈 파일
- 포스터 편집본
- 인쇄용 PDF
- 최종 이미지

예:

```text
final_poster.pptx
final_poster.pdf
```

---

## `06_submission/presentation/.gitkeep`

### 역할
발표자료 폴더를 유지한다.

### 나중에 들어갈 파일
- 발표 슬라이드
- 발표 PDF
- 발표 대본

예:

```text
final_presentation.pptx
presentation_script.md
```

---

# 9. `.gitkeep` 파일 공통 설명

현재 프로젝트에는 다음 `.gitkeep` 파일이 있다.

```text
00_original_example/.gitkeep
01_baseline/output/.gitkeep
02_proposed/output/.gitkeep
03_doe/cases/.gitkeep
03_doe/output/.gitkeep
04_circuit/output/.gitkeep
05_results/raw/.gitkeep
05_results/summary/.gitkeep
05_results/figures/.gitkeep
06_submission/report/.gitkeep
06_submission/poster/.gitkeep
06_submission/presentation/.gitkeep
```

Git은 빈 폴더를 추적하지 않기 때문에 빈 파일인 `.gitkeep`을 넣어 폴더를 유지한다.

실제 파일이 들어온 뒤에도 남겨둬도 문제없지만, 필요하면 삭제할 수 있다.

---

# 10. 현재 파일 분류

## 사람이 직접 관리하는 파일

```text
README.md
TODO.md
FILE_GUIDE.md
project.yaml
requirements.txt
.gitignore
```

## 실행 또는 분석 코드

```text
check_project.py
install_here.sh
03_doe/generate_cases.py
05_results/pareto.py
```

## TCAD/회로 입력 초안

```text
01_baseline/process/baseline_sprocess.cmd.template
01_baseline/device/baseline_nmos_sdevice.cmd.template
01_baseline/device/baseline_pmos_sdevice.cmd.template
02_proposed/process/proposed_sprocess.cmd.template
02_proposed/device/proposed_nmos_sdevice.cmd.template
02_proposed/device/proposed_pmos_sdevice.cmd.template
03_doe/template/master_case.cmd.template
04_circuit/inverter/inverter.cmd.template
04_circuit/ring_oscillator/ring_oscillator.cmd.template
```

## 폴더 유지용 파일

모든 `.gitkeep`

## 자동 참고 파일

```text
TREE.txt
```

---

# 11. 파일 수정 우선순위

프로젝트 초반에는 아래 파일만 우선 수정한다.

1. `project.yaml`
2. `01_baseline/process/baseline_sprocess.cmd.template`
3. `01_baseline/device/baseline_nmos_sdevice.cmd.template`
4. `01_baseline/device/baseline_pmos_sdevice.cmd.template`
5. `TODO.md`

Baseline이 완성된 다음에 수정한다.

6. `02_proposed/process/proposed_sprocess.cmd.template`
7. `02_proposed/device/proposed_nmos_sdevice.cmd.template`
8. `02_proposed/device/proposed_pmos_sdevice.cmd.template`

Proposed 단일 조건이 수렴한 다음에 수정한다.

9. `03_doe/template/master_case.cmd.template`
10. `03_doe/generate_cases.py`
11. `04_circuit/inverter/inverter.cmd.template`
12. `04_circuit/ring_oscillator/ring_oscillator.cmd.template`
13. `05_results/pareto.py`

---

# 12. 새 파일 추가 규칙

새 파일을 추가할 때는 다음 중 하나에 해당해야 한다.

- TCAD 입력 Deck
- 실행 script
- Metric 추출 script
- Raw 결과
- Summary 결과
- Figure
- 최종 제출물

불필요한 계획 문서나 역할별 메모 파일은 만들지 않는다.

새 파일을 추가하면 이 `FILE_GUIDE.md`에도 다음 내용을 추가한다.

- 파일 경로
- 역할
- 입력
- 출력
- 수정 시점
- 주의사항
