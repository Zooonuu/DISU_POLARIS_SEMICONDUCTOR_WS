# Validation Plan

## 1. Hold-out
초기 surrogate 학습에 사용하지 않은 점을 최소 3개 선택한다.

## 2. Neighborhood
최종 후보의 각 주요 변수에 대해 가능한 범위 내에서 ±0.3~0.5 nm 조건을 추가한다.

## 3. Mesh
최소 2개 mesh density에서 핵심 metric의 변화율을 확인한다.

## 4. Variation
Nominal 성능뿐 아니라 평균, 표준편차, worst-case 또는 yield를 비교한다.

## 5. Fair comparison
Baseline과 Proposed의 비핵심 공정·bias·metric definition을 동일하게 유지한다.
