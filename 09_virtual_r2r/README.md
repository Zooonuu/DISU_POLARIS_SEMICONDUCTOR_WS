# 09 Virtual R2R

실제 장비 제어가 아니라 TCAD-generated process drift를 사용한 proof-of-concept이다.

예시:
- deposition rate drift
- etch rate drift
- spacer CD bias
- fin width bias

출력:
- inverter delay
- RO frequency
- standby leakage

제어기는 먼저 EWMA로 구현하고, 필요할 때 Kalman 또는 multivariable controller로 확장한다.
