# 연구윤리 및 신규성 검토 메모

## 결론

현재 프로젝트의 구조적 핵심은 이미 발표된 연구와 상당히 겹친다.

특히 다음 논문은 현재 기획과 거의 같은 연구 축을 포함한다.

> Pal, Kaushik, and Dasgupta (2015),  
> “Asymmetric Dual-Spacer Trigate FinFET Device-Circuit Codesign and Its Variability Analysis.”

이 논문은 제목 수준에서 이미 다음 요소를 포함한다.

- Asymmetric dual spacer
- Trigate FinFET
- Device–circuit co-design
- Variability analysis

따라서 단순히 아래 요소를 추가하는 것만으로 구조적 독창성을 주장하기 어렵다.

- Source spacer는 짧게, Drain spacer는 길게 설계
- 서로 다른 k의 spacer 사용
- Inverter 또는 ring oscillator 평가
- Power/Delay/PDP/EDP 분석
- 공정 variation 분석
- Pareto 최적화

2024년 연구에는 Air + Si3N4 hybrid spacer도 보고되어 있어, air/Si3N4 composite 자체도 신규성으로 삼으면 안 된다.

---

## 안전한 표현과 위험한 표현

### 위험한 표현

- “본 연구에서 최초로 비대칭 dual-k FinFET을 제안하였다.”
- “최초로 spacer 구조와 회로를 공동 최적화하였다.”
- “Air/Si3N4 hybrid spacer를 최초 적용하였다.”
- “기존 연구에는 공정 편차 분석이 없다.”

### 안전한 표현

- “기존 asymmetric dual-spacer FinFET 연구를 기반으로, 본 연구에서는 …를 추가로 검토하였다.”
- “본 연구의 기여는 spacer 구조 자체가 아니라, 사전 정의된 DOE–회로 지표–공정 feedback을 연결한 재현 가능한 workflow에 있다.”
- “TCAD-generated drift를 이용한 virtual R2R proof-of-concept를 수행하였다.”
- “기존 논문의 구조와 결과를 재현한 뒤, 동일 조건에서 제안 확장을 독립적으로 비교하였다.”

---

## 그래도 구조 독창성이 필요한 경우

대회가 구조·공정 변경의 독창성을 높은 비중으로 평가한다면, 현재 구조는 그대로 제출하기보다 다음 절차가 필요하다.

1. R01–R13의 구조 그림과 설계변수를 표로 정리한다.
2. 현재 제안 구조의 각 요소가 어느 논문에 이미 존재하는지 claim chart를 만든다.
3. 기존 문헌에 없는 공정적으로 직접 구현 가능한 구조 요소를 새로 정의한다.
4. 새 요소가 기존 구조에 단순 장식이 아니라 독립적인 물리 메커니즘을 갖는지 확인한다.
5. 논문 검색 키워드를 바꾸어 최소 2회 이상 재검색한다.
6. 지도교수 또는 대회 담당자에게 신규성 범위를 검토받는다.

---

## 재현 연구와 표절의 차이

기존 소자를 재현하는 것은 표절이 아니다. 다만 다음 조건을 지켜야 한다.

- 원 논문을 명시한다.
- 구조·조건이 같은 부분을 숨기지 않는다.
- 수치와 그림을 직접 다시 계산한다.
- 원 논문의 문장과 그림을 그대로 복사하지 않는다.
- 재현 결과와 본 팀의 확장 결과를 분리한다.
- 결과가 원 논문과 다르면 차이를 숨기지 않고 원인을 분석한다.

반대로 기존 구조를 출처 없이 “우리 팀의 신규 구조”라고 표현하면 연구윤리 문제가 된다.

---

## 데이터 및 그림 관리

- 모든 DOE case와 실패 case를 보존한다.
- 범위와 목적함수를 결과 확인 전에 고정한다.
- figure에는 자체 TCAD 결과인지 문헌 재작성인지 표시한다.
- 문헌의 figure를 참고해 새로 그렸다면 “adapted from”을 표기한다.
- 원문 figure를 직접 사용할 때는 저작권과 이용 허가를 확인한다.
- paywall 논문의 PDF를 GitHub에 업로드하지 않는다.
- 저장소에는 DOI, BibTeX, 분석 메모만 올린다.

---

## 권장 보고서 기여문 예시

현재 구조를 유지할 경우 사용할 수 있는 보수적인 예시다.

> 기존 asymmetric dual-k spacer FinFET의 구조적 개념과 device–circuit co-design 연구를 선행연구로 채택하였다. 본 연구는 해당 소자를 신규 발명으로 주장하지 않으며, SOI FinFET 공정 recipe와 생성 형상, device metric, inverter EDP 및 TCAD-generated process drift를 연결하는 재현 가능한 optimization/virtual-R2R workflow의 구축과 검증에 초점을 둔다.

다만 이 기여가 대회의 ‘구조 독창성’ 요건을 충분히 충족하는지는 별도 판단이 필요하다.
