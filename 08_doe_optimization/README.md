# 08 DOE and Optimization

초기 설계공간은 결과 확인 전에 `config/design_space.yaml`에 고정한다.

권장 흐름:
1. LHS 또는 Sobol 초기점 16–24개
2. TCAD batch 실행
3. metric parsing
4. Pareto front
5. surrogate 또는 Bayesian optimization
6. 독립 검증점
7. Robust optimum
