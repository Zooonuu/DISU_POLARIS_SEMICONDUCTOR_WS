# Device Metric Definition

각 metric의 추출법을 결과 확인 전에 고정한다.

- `Ion`: VGS=VDD, VDS=VDD에서의 drain current
- `Ioff`: VGS=0, VDS=VDD에서의 drain current
- `SS`: 지정한 subthreshold current 구간에서 log10(Id)–Vg slope
- `Vth`: constant-current 또는 gm method 중 하나를 선택해 고정
- `DIBL`: low/high VDS에서 추출한 Vth 차이를 VDS 차이로 나눔
- `Cgd`: AC 조건, 주파수, DC bias를 반드시 함께 기록
