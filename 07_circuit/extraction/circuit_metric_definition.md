# Circuit Metric Definition

- `tpHL`: input 50% crossing to output falling 50% crossing
- `tpLH`: input 50% crossing to output rising 50% crossing
- `delay_avg = (tpHL + tpLH) / 2`
- `static_power`: stable logic states에서의 VDD current 평균
- `dynamic_energy`: one transition 또는 one period의 VDD current 적분
- `PDP`: average power × delay
- `EDP`: transition energy × delay

Load capacitance, input slew, VDD, temperature와 측정 window를 고정한다.
