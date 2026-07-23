# Risk Register

| 위험 | 영향 | 조기 신호 | 대응 |
|---|---|---|---|
| 3D mesh 발산 | 높음 | 첫 bias step 실패 | 2D 단면 검증 후 3D 확장, mesh 완화 |
| PMOS 수렴 지연 | 높음 | NMOS만 수렴 | 물리 모델 최소 세트부터 단계 추가 |
| MixedMode 미지원 | 중간 | 라이선스 오류 | TCAD I–V/C–V 추출 후 SPICE fallback |
| DOE 계산량 과다 | 높음 | 1 Run 시간이 과도 | 16–24 초기점, surrogate 기반 추가점 |
| low-k 재료 모델 불명확 | 중간 | 재료 정의 오류 | SiO2 baseline 후 검증된 low-k로 확장 |
