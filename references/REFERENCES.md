# OASIS-FinFET 참고문헌 및 출처 기록
## 0. 출처 범위에 대한 정직한 설명
이 목록은 **이 대화에서 구체적으로 언급·인용된 자료**, 사용자가 제공한 수상작 포스터, 그리고 현재 주제의 중복성을 점검하기 위해 추가로 확인한 핵심 1차 문헌을 구분해 정리한 것이다.

제가 학습 과정에서 접했을 수 있는 모든 원문이나 내부 학습데이터의 목록을 제공할 수는 없으며, 초기 아이디어가 특정 논문 한 편을 읽고 그대로 옮겨 만든 것도 아니다. 그러나 제출 연구의 연구윤리를 위해서는 ‘아이디어를 떠올릴 때 실제로 명시적으로 사용한 출처’뿐 아니라 **현재 구조와 실질적으로 중복되는 선행연구**도 반드시 조사·인용해야 한다. 따라서 아래 목록은 이 프로젝트에 필요한 추적 가능한 provenance set으로 사용한다.
## 1. 가장 중요한 연구윤리 경고
**현재 주제의 핵심 표현인 ‘비대칭 dual/composite spacer FinFET + device–circuit co-design + variability/robust optimization’은 Pal et al. (2015)의 연구와 매우 직접적으로 겹친다.** 또한 대칭/비대칭 dual-k spacer의 delay, capacitance, SRAM, ring oscillator, SOI 및 hybrid low-k/air spacer 역시 이미 다수 연구되어 있다.

따라서 현재 구조를 그대로 두고 다음과 같이 주장하면 안 된다.

- “비대칭 spacer를 최초로 제안했다.”
- “dual-k/composite spacer와 회로 co-design을 최초로 결합했다.”
- “Air/Si3N4 또는 low-k hybrid spacer를 최초로 제안했다.”
- “공정 편차를 포함한 device–circuit 최적화를 최초로 수행했다.”

현재 안을 계속 사용한다면 **기존 AsymD-k/dual-spacer 구조의 재현·확장 연구**임을 명시하고, 새로운 기여는 별도로 증명해야 한다. 구조 독창성이 평가 핵심이라면 제출 전 구조 자체를 다시 차별화하는 편이 안전하다.
## 2. 문헌 분류 기준
- **직접 중복 핵심**: 현재 device 구조와 연구 흐름이 직접 겹치므로 필수 인용
- **Spacer 재료/구조**: low-k, hybrid, air-gap 및 underlap 메커니즘의 근거
- **FinFET/SOI 기초**: 구조 배경
- **DOE/Pareto/MOBO**: Cherry-picking 방지와 최적화 방법
- **R2R/Virtual metrology**: 공정 feedback 확장 방법
- **TCAD 공식 문서**: 툴 지원 근거
- **폐기된 초기 GAA 방향**: 초기 아이디어에는 사용했지만 현재 보고서에는 원칙적으로 제외

## R01. P. K. Pal, B. K. Kaushik, and S. Dasgupta, “Asymmetric Dual-Spacer Trigate FinFET Device-Circuit Codesign and Its Variability Analysis,” IEEE Transactions on Electron Devices, vol. 62, no. 4, pp. 1105–1112, 2015.
- **분류:** 직접 중복 핵심
- **출처 상태:** 이 대화의 기존 제안과 가장 직접적으로 겹쳐 이번 검증에서 반드시 확인
- **현재 보고서 인용:** YES
- **중복 위험:** 매우 높음
- **DOI:** `10.1109/TED.2015.2400053`
- **공식/식별 링크:** https://doi.org/10.1109/TED.2015.2400053
- **프로젝트와의 관계:** 비대칭 dual-spacer FinFET, device–circuit co-design, variability 분석이라는 현재 주제의 핵심 조합과 직접 중복한다.
- **안전한 사용법:** 반드시 선행연구로 전면 인용하고, 현재 구조 자체를 최초라고 주장하지 않는다.

## R02. P. K. Pal, B. K. Kaushik, and S. Dasgupta, “High-Performance and Robust SRAM Cell Based on Asymmetric Dual-k Spacer FinFETs,” IEEE Transactions on Electron Devices, vol. 60, no. 10, pp. 3371–3377, 2013.
- **분류:** 직접 중복 핵심
- **출처 상태:** 현재 회로 연계 아이디어의 중복성 검증
- **현재 보고서 인용:** YES
- **중복 위험:** 매우 높음
- **DOI:** `10.1109/TED.2013.2278201`
- **공식/식별 링크:** https://doi.org/10.1109/TED.2013.2278201
- **프로젝트와의 관계:** 비대칭 dual-k spacer를 회로 수준 SRAM 성능·강건성과 연결한다.
- **안전한 사용법:** 회로 응용을 넣는 것 자체가 신규성이 아님을 설명하는 선행연구로 사용한다.

## R03. P. K. Pal, B. K. Kaushik, and S. Dasgupta, “Investigation of Symmetric Dual-k Spacer Trigate FinFETs From Delay Perspective,” IEEE Transactions on Electron Devices, vol. 61, no. 11, pp. 3579–3585, 2014.
- **분류:** 직접 중복 핵심
- **출처 상태:** spacer–capacitance–delay 연결 검증
- **현재 보고서 인용:** YES
- **중복 위험:** 높음
- **DOI:** `10.1109/TED.2014.2351616`
- **공식/식별 링크:** https://doi.org/10.1109/TED.2014.2351616
- **프로젝트와의 관계:** dual-k spacer와 fringe capacitance, circuit delay 및 noise-margin 관계를 다룬다.
- **안전한 사용법:** Cgd 및 delay 개선 메커니즘의 근거로 인용한다.

## R04. P. K. Pal, B. K. Kaushik, B. Anand, and S. Dasgupta, “A Comparative Analysis of Symmetric and Asymmetric Dual-k Spacer FinFETs from Device and Circuit Perspectives,” in Proc. 16th International Symposium on Quality Electronic Design (ISQED), pp. 594–598, 2015.
- **분류:** 직접 중복 핵심
- **출처 상태:** 대칭/비대칭 구조의 device–circuit 비교 선행 검증
- **현재 보고서 인용:** YES
- **중복 위험:** 매우 높음
- **DOI:** `10.1109/ISQED.2015.7085494`
- **공식/식별 링크:** https://doi.org/10.1109/ISQED.2015.7085494
- **프로젝트와의 관계:** baseline 대칭 구조와 proposed 비대칭 구조를 device/circuit 관점에서 비교하는 현재 연구 흐름과 직접 겹친다.
- **안전한 사용법:** 비교 프레임을 참고하되, 동일 그래프 구성·문장·수치를 복제하지 않는다.

## R05. P. K. Pal, B. K. Kaushik, and S. Dasgupta, “A Detailed Capacitive Analysis of Symmetric and Asymmetric Dual-k FinFETs for Improved Circuit Delay Metrics,” in Proc. International Conference on Emerging Devices and Smart Systems (ICEDSS), pp. 13–18, 2016.
- **분류:** 직접 중복 핵심
- **출처 상태:** 기생용량과 inverter/ring oscillator 지연 분석 중복 검증
- **현재 보고서 인용:** YES
- **중복 위험:** 높음
- **DOI:** `10.1109/ICEDSS.2016.7587790`
- **공식/식별 링크:** https://doi.org/10.1109/ICEDSS.2016.7587790
- **프로젝트와의 관계:** Cgd/Miller capacitance와 inverter 및 ring-oscillator delay를 직접 연결한다.
- **안전한 사용법:** 회로 검증 지표의 근거로 인용하고, 회로 검증 자체를 신규성으로 주장하지 않는다.

## R06. A. Dutta, K. Koley, S. K. Saha, and C. K. Sarkar, “Physical Insights Into Electric Field Modulation in Dual-k Spacer Asymmetric Underlap FinFET,” IEEE Transactions on Electron Devices, vol. 63, no. 8, pp. 3019–3027, 2016.
- **분류:** 직접 중복 핵심
- **출처 상태:** 물리 메커니즘 검증
- **현재 보고서 인용:** YES
- **중복 위험:** 높음
- **DOI:** `10.1109/TED.2016.2580625`
- **공식/식별 링크:** https://doi.org/10.1109/TED.2016.2580625
- **프로젝트와의 관계:** dual-k spacer와 asymmetric underlap이 전계와 inversion charge를 어떻게 바꾸는지 설명한다.
- **안전한 사용법:** 전계 contour 해석 및 가설 설정의 물리적 근거로 인용한다.

## R07. K. P. Pradhan et al., “Benefits of Asymmetric Underlap Dual-k Spacer Hybrid Fin Field-Effect Transistor over Bulk Fin Field-Effect Transistor,” IET Circuits, Devices & Systems, 2016.
- **분류:** 직접 중복 핵심
- **출처 상태:** SOI 플랫폼에서의 비대칭 spacer 중복 검증
- **현재 보고서 인용:** YES
- **중복 위험:** 매우 높음
- **DOI:** `10.1049/IET-CDS.2016.0125`
- **공식/식별 링크:** https://doi.org/10.1049/IET-CDS.2016.0125
- **프로젝트와의 관계:** SOI 플랫폼에서 asymmetric underlap dual-k spacer hybrid FinFET을 다룬다.
- **안전한 사용법:** ‘SOI + 비대칭 dual-k’ 결합 역시 신규가 아님을 명시한다.

## R08. A. B. Sachid, C. R. Manoj, D. K. Sharma, and V. R. Rao, “Gate Fringe-Induced Barrier Lowering in Underlap FinFET Structures and Its Optimization,” IEEE Electron Device Letters, vol. 29, no. 1, pp. 128–130, 2008.
- **분류:** Spacer/underlap 물리
- **출처 상태:** underlap trade-off 설명을 위한 핵심 선행연구
- **현재 보고서 인용:** YES
- **중복 위험:** 중간
- **DOI:** `10.1109/LED.2007.911974`
- **공식/식별 링크:** https://doi.org/10.1109/LED.2007.911974
- **프로젝트와의 관계:** underlap에서 gate fringe field가 barrier와 성능을 바꾸는 GFIBL 현상을 제시한다.
- **안전한 사용법:** Spacer 길이가 무조건 길수록 좋다는 단순 설명을 피하고 trade-off 근거로 인용한다.

## R09. V. Bharath Sreenivasulu and V. Narendar, “Performance Improvement of Spacer Engineered n-Type SOI FinFET at 3-nm Gate Length,” AEU - International Journal of Electronics and Communications, vol. 137, Art. 153803, 2021.
- **분류:** Spacer 재료/구조
- **출처 상태:** 이전 답변의 SOI spacer-engineering 근거
- **현재 보고서 인용:** YES
- **중복 위험:** 높음
- **DOI:** `10.1016/j.aeue.2021.153803`
- **공식/식별 링크:** https://doi.org/10.1016/j.aeue.2021.153803
- **프로젝트와의 관계:** SOI FinFET에서 spacer 재료/구조가 성능에 미치는 영향을 다룬다.
- **안전한 사용법:** 재료 후보와 비교 지표를 정할 때 인용한다.

## R10. N. Huang, W. Liu, Q. Li, W. Bai, X. Tang, and T. Yang, “Thermal and Electrical Performance Investigation of FinFET with Encased Air-gap Gate Sidewalls from Spacer Encapsulation Layer Material and Structure Parameter Perspectives,” Microelectronics Journal, vol. 103, Art. 104846, 2020.
- **분류:** Spacer 재료/구조
- **출처 상태:** air-gap 확장 아이디어의 근거
- **현재 보고서 인용:** YES
- **중복 위험:** 높음
- **DOI:** `10.1016/j.mejo.2020.104846`
- **공식/식별 링크:** https://doi.org/10.1016/j.mejo.2020.104846
- **프로젝트와의 관계:** encased air-gap spacer의 전기·열 특성과 구조 파라미터를 다룬다.
- **안전한 사용법:** air-gap을 확장안으로 사용할 경우 반드시 인용한다.

## R11. T. Yamashita et al., “A Novel ALD SiBCN Low-k Spacer for Parasitic Capacitance Reduction in FinFETs,” in Proc. Symposium on VLSI Technology, pp. T154–T155, 2015.
- **분류:** Spacer 재료/구조
- **출처 상태:** 실제 저유전 spacer 공정 가능성의 근거
- **현재 보고서 인용:** YES
- **중복 위험:** 중간
- **DOI:** `10.1109/VLSIT.2015.7223659`
- **공식/식별 링크:** https://doi.org/10.1109/VLSIT.2015.7223659
- **프로젝트와의 관계:** ALD SiBCN low-k spacer와 parasitic capacitance/RO delay 개선의 실제 공정 사례다.
- **안전한 사용법:** SiO2를 단순히 ‘low-k 신소재’처럼 표현하지 말고 실제 low-k 공정 문헌과 구분한다.

## R12. M. Gu et al., “Hybrid Low-k Spacer Scheme for Advanced FinFET Technology Parasitic Capacitance Reduction,” Electronics Letters, vol. 56, no. 10, pp. 514–516, 2020.
- **분류:** Spacer 재료/구조
- **출처 상태:** hybrid low-k spacer 공정 선행 검증
- **현재 보고서 인용:** YES
- **중복 위험:** 높음
- **DOI:** `10.1049/el.2019.3954`
- **공식/식별 링크:** https://doi.org/10.1049/el.2019.3954
- **프로젝트와의 관계:** advanced FinFET에서 hybrid low-k spacer를 이용한 parasitic capacitance 저감을 제시한다.
- **안전한 사용법:** composite/hybrid spacer 자체는 신규가 아님을 명시한다.

## R13. V. Bharath Sreenivasulu, S. Bhandari, M. Prasad, P. Mani, C. Subba Reddy, and M. Durga Prakash, “Spacer Engineering on Multi-channel FinFET for Advanced Wireless Applications,” AEU - International Journal of Electronics and Communications, vol. 178, Art. 155298, 2024.
- **분류:** Spacer 재료/구조
- **출처 상태:** 최신 동향 검증
- **현재 보고서 인용:** YES
- **중복 위험:** 매우 높음
- **DOI:** `10.1016/j.aeue.2024.155298`
- **공식/식별 링크:** https://doi.org/10.1016/j.aeue.2024.155298
- **프로젝트와의 관계:** Air + Si3N4 hybrid spacer와 capacitance/회로 구동 관련 지표를 최신 FinFET 문맥에서 다룬다.
- **안전한 사용법:** Air/Si3N4 hybrid 구조를 신규 구조로 주장하지 않는다.

## R14. D. Hisamoto, T. Kaga, Y. Kawamoto, and E. Takeda, “A Fully Depleted Lean-Channel Transistor (DELTA)—A Novel Vertical Ultra Thin SOI MOSFET,” in IEDM Technical Digest, pp. 833–836, 1989.
- **분류:** FinFET/SOI 기초
- **출처 상태:** SOI fin 구조의 역사·기초
- **현재 보고서 인용:** 권장
- **중복 위험:** 낮음
- **DOI:** `10.1109/IEDM.1989.74182`
- **공식/식별 링크:** https://doi.org/10.1109/IEDM.1989.74182
- **프로젝트와의 관계:** 수직 ultrathin SOI multi-gate 계열의 초기 기초 연구다.
- **안전한 사용법:** 연구 배경에서 짧게 인용한다.

## R15. D. Hisamoto et al., “FinFET—A Self-Aligned Double-Gate MOSFET Scalable to 20 nm,” IEEE Transactions on Electron Devices, vol. 47, no. 12, pp. 2320–2325, 2000.
- **분류:** FinFET/SOI 기초
- **출처 상태:** FinFET 구조 정의의 대표 원전
- **현재 보고서 인용:** YES
- **중복 위험:** 낮음
- **DOI:** `10.1109/16.887014`
- **공식/식별 링크:** https://doi.org/10.1109/16.887014
- **프로젝트와의 관계:** FinFET 구조와 short-channel control의 대표 기초문헌이다.
- **안전한 사용법:** FinFET 구조 설명과 배경에 인용한다.

## R16. M. D. McKay, R. J. Beckman, and W. J. Conover, “A Comparison of Three Methods for Selecting Values of Input Variables in the Analysis of Output from a Computer Code,” Technometrics, vol. 21, no. 2, pp. 239–245, 1979.
- **분류:** DOE/표본설계
- **출처 상태:** Cherry-picking 방지용 LHS 방법론
- **현재 보고서 인용:** YES
- **중복 위험:** 낮음
- **DOI:** `10.1080/00401706.1979.10489755`
- **공식/식별 링크:** https://doi.org/10.1080/00401706.1979.10489755
- **프로젝트와의 관계:** Latin Hypercube Sampling의 고전적 근거다.
- **안전한 사용법:** DOE 방법 섹션에 인용하고 seed와 전체 case를 공개한다.

## R17. K. Deb, A. Pratap, S. Agarwal, and T. Meyarivan, “A Fast and Elitist Multiobjective Genetic Algorithm: NSGA-II,” IEEE Transactions on Evolutionary Computation, vol. 6, no. 2, pp. 182–197, 2002.
- **분류:** Pareto/최적화
- **출처 상태:** 다목적 Pareto 최적화 방법론
- **현재 보고서 인용:** 조건부
- **중복 위험:** 낮음
- **DOI:** `10.1109/4235.996017`
- **공식/식별 링크:** https://doi.org/10.1109/4235.996017
- **프로젝트와의 관계:** NSGA-II를 실제 사용할 경우의 원전이다.
- **안전한 사용법:** 단순 비지배해 필터만 사용한다면 NSGA-II를 사용했다고 쓰지 않는다.

## R18. S. Daulton, M. Balandat, and E. Bakshy, “Differentiable Expected Hypervolume Improvement for Parallel Multi-Objective Bayesian Optimization,” Advances in Neural Information Processing Systems 33, 2020.
- **분류:** Bayesian multi-objective
- **출처 상태:** MOBO/qEHVI를 제안했던 방법론 근거
- **현재 보고서 인용:** 조건부
- **중복 위험:** 낮음
- **공식/식별 링크:** https://arxiv.org/abs/2006.05078
- **프로젝트와의 관계:** qEHVI 기반 multi-objective Bayesian optimization의 원전이다.
- **안전한 사용법:** 실제로 qEHVI/MOBO를 구현한 경우에만 인용하고 사용했다고 쓴다.

## R19. H. Jeong, J. Suk, J.-T. Kong, and S. Kim, “ML-Driven Optimization of Standard Cell Performance and Timing in Advanced Nodes,” Journal of Semiconductor Technology and Science, vol. 26, no. 2, pp. 130–140, 2026.
- **분류:** Device–circuit/ML 최적화
- **출처 상태:** 이전 답변에서 Sobol–surrogate–MOBO–circuit 흐름의 직접 근거
- **현재 보고서 인용:** YES
- **중복 위험:** 중간
- **DOI:** `10.5573/JSTS.2026.26.2.130`
- **공식/식별 링크:** https://doi.org/10.5573/JSTS.2026.26.2.130
- **프로젝트와의 관계:** Sobol sampling, ANN surrogate, MOBO, TCAD/compact model/SPICE를 연결한 최신 표준셀 최적화 방법론이다.
- **안전한 사용법:** 알고리즘 흐름을 참고하되 코드·그림·문장을 그대로 복제하지 않는다.

## R20. A.-C. Lee, Y.-R. Pan, and M.-T. Hsieh, “Output Disturbance Observer Structure Applied to Run-to-Run Control for Semiconductor Manufacturing,” IEEE Transactions on Semiconductor Manufacturing, vol. 24, no. 1, pp. 27–43, 2011.
- **분류:** R2R 제어
- **출처 상태:** 이전 제안의 EWMA/Virtual R2R 근거
- **현재 보고서 인용:** YES
- **중복 위험:** 낮음
- **DOI:** `10.1109/TSM.2010.2088990`
- **공식/식별 링크:** https://doi.org/10.1109/TSM.2010.2088990
- **프로젝트와의 관계:** EWMA, double-EWMA 및 반도체 R2R 제어의 통합 프레임을 제공한다.
- **안전한 사용법:** Virtual R2R를 넣을 경우 실제 Fab 제어가 아닌 proof-of-concept임을 명시한다.

## R21. P. Kang, H.-J. Lee, S. Cho, D. Kim, J. Park, C. K. Park, and S. Doh, “A Virtual Metrology System for Semiconductor Manufacturing,” Expert Systems with Applications, vol. 36, no. 10, pp. 12554–12561, 2009.
- **분류:** Virtual metrology
- **출처 상태:** 가상 측정/공정 피드백 아이디어의 근거
- **현재 보고서 인용:** 조건부
- **중복 위험:** 낮음
- **DOI:** `10.1016/j.eswa.2009.05.053`
- **공식/식별 링크:** https://doi.org/10.1016/j.eswa.2009.05.053
- **프로젝트와의 관계:** 공정 센서/recipe 데이터에서 품질값을 예측하는 virtual metrology의 대표 사례다.
- **안전한 사용법:** 실제 센서 데이터가 없다면 ‘virtual metrology 구현’이라고 과장하지 말고 개념적 참고로만 둔다.

## R22. J. Wan, S. Pampuri, P. G. O’Hara, A. B. Johnston, and S. McLoone, “On Regression Methods for Virtual Metrology in Semiconductor Manufacturing,” in Proc. ISSC 2014/CIICT 2014, 2014.
- **분류:** Virtual metrology
- **출처 상태:** 회귀 기반 VM 방법론 보조
- **현재 보고서 인용:** 조건부
- **중복 위험:** 낮음
- **DOI:** `10.1049/cp.2014.0718`
- **공식/식별 링크:** https://doi.org/10.1049/cp.2014.0718
- **프로젝트와의 관계:** Virtual metrology 회귀모델 선택과 noisy/high-dimensional predictor 문제를 다룬다.
- **안전한 사용법:** VM 회귀를 실제 구현할 경우 인용한다.

## R23. Synopsys, “Sentaurus TCAD: Industry-Standard Process and Device Simulators,” product datasheet.
- **분류:** TCAD 공식 문서
- **출처 상태:** 툴 지원 가능성 확인에 직접 사용
- **현재 보고서 인용:** YES
- **중복 위험:** 낮음
- **공식/식별 링크:** https://www.synopsys.com/content/dam/synopsys/silicon/datasheets/sentaurus_ds.pdf
- **프로젝트와의 관계:** Sentaurus suite가 process/device simulation을 연결한다는 공식 근거다.
- **안전한 사용법:** 툴 기능 설명에만 사용한다.

## R24. Synopsys, “Sentaurus Device: Multidimensional (1D/2D/3D) Device Simulator,” official product page.
- **분류:** TCAD 공식 문서
- **출처 상태:** FinFET/FDSOI device simulation 지원 확인
- **현재 보고서 인용:** YES
- **중복 위험:** 낮음
- **공식/식별 링크:** https://www.synopsys.com/manufacturing/tcad/device-simulation/sentaurus-device.html
- **프로젝트와의 관계:** Sentaurus Device의 FinFET/FDSOI 및 3D 해석 지원을 확인한다.
- **안전한 사용법:** 실제 학교 라이선스와 버전은 별도 확인한다.

## R25. Synopsys, “Sentaurus Workbench,” official product page.
- **분류:** TCAD 공식 문서
- **출처 상태:** parameterization/DOE workflow 설명에 사용
- **현재 보고서 인용:** YES
- **중복 위험:** 낮음
- **공식/식별 링크:** https://www.synopsys.com/manufacturing/tcad/framework.html
- **프로젝트와의 관계:** TCAD project parameterization, execution 및 결과관리 기능의 공식 근거다.
- **안전한 사용법:** 사용 가능한 기능은 설치된 버전에서 검증한다.

## R26. TSMC, “N2 Technology,” official technology page.
- **분류:** 폐기된 초기 GAA 방향
- **출처 상태:** FinFET 전환 전 초기 GAA 아이디어에서 인용
- **현재 보고서 인용:** 현재 보고서에는 불필요
- **중복 위험:** 낮음
- **공식/식별 링크:** https://www.tsmc.com/english/dedicatedFoundry/technology/logic/l_2nm
- **프로젝트와의 관계:** 초기 GAA nanosheet 주제의 산업 동향 근거였다.
- **안전한 사용법:** 현재 FinFET 보고서에는 직접 관련이 없으면 넣지 않는다.

## R27. imec, “Entering the Nanosheet Transistor Era,” technical article.
- **분류:** 폐기된 초기 GAA 방향
- **출처 상태:** FinFET 전환 전 초기 GAA 아이디어에서 인용
- **현재 보고서 인용:** 현재 보고서에는 불필요
- **중복 위험:** 낮음
- **공식/식별 링크:** https://www.imec-int.com/en/articles/entering-nanosheet-transistor-era-0
- **프로젝트와의 관계:** nanosheet inner-spacer 공정 난제의 배경으로 사용했다.
- **안전한 사용법:** 현재 SOI FinFET 주제에는 혼입하지 않는다.

## R28. IEEE IRDS, “2024 IRDS More Moore,” roadmap report, 2024.
- **분류:** 폐기된 초기 GAA 방향
- **출처 상태:** FinFET 전환 전 초기 GAA/CFET 동향에서 인용
- **현재 보고서 인용:** 현재 보고서에는 불필요
- **중복 위험:** 낮음
- **공식/식별 링크:** https://irds.ieee.org/images/files/pdf/2024/2024IRDS_MM.pdf
- **프로젝트와의 관계:** GAA/CFET 및 scaling 동향의 배경으로 사용했다.
- **안전한 사용법:** 현재 보고서에서 최신 로직 로드맵을 언급할 때만 제한적으로 사용한다.

## 3. 사용자가 제공한 수상작 포스터
아래 자료는 외부 논문이 아니라 사용자가 이 대화에 업로드한 수상작 포스터 이미지다. 프로젝트 아이디어를 구성할 때 문제–가설–구조변경–TCAD 정량검증–파급효과라는 발표 형식을 분석하는 데 사용했다.

- DRAM의 GIDL 저감을 위한 Dual Work-Function Metal Gate(DWMG) 최적 구조 설계 및 분석
- FinFET의 Leakage 개선과 Aspect Ratio 증가로 인한 bending 현상을 보완한 Layered-FinFET
- 2차원 반도체 기반 트랜지스터 공정
- MOSFET의 Concave Channel과 Dual Material Gate 구조 결합을 통한 Short Channel Effect 개선
- Reducing Parasitic Capacitance in RCAT with Air-gap Spacer and Underlap
- A Novel Approach to Suppress Short Channel Effects in NAND Flash Using High-k Dielectrics
- Nitride Hard Mask 기반 Self-Aligned 공정을 이용한 MOSFET Short Channel Effect 개선

보고서에서는 이 포스터를 학술 근거 대신 사용하지 않는다. 포스터가 인용한 원 논문을 별도로 찾아 인용해야 하며, 포스터의 도식·문장·배치를 그대로 복제하지 않는다.
