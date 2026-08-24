# Redefining Credibility Standards in Quasi-Experimental Econometrics (2014–2024): A Comprehensive Analysis

## Introduction

The decade from 2014 to 2024 witnessed a fundamental transformation in how the top five economics journals—*American Economic Review* (AER), *Quarterly Journal of Economics* (QJE), *Journal of Political Economy* (JPE), *Econometrica*, and *Review of Economic Studies* (REStud)—evaluate and implement quasi-experimental methods. This report synthesizes evidence from Monte Carlo simulations, head-to-head empirical comparisons, advances in inference, and publication trends to document how credibility standards for five core estimators have been redefined.

---

## Part I: Comparative Simulations and Head-to-Head Applications

### 1.1 When Estimators Yield Meaningfully Different Causal Conclusions

The evidence from Monte Carlo studies, replication exercises, and empirical applications reveals systematic patterns of divergence across the five estimators. These divergences are not random; they arise predictably under specific data-generating processes, assumption violations, and treatment effect heterogeneity patterns.

#### 1.1.1 Difference-in-Differences (DiD) vs. Synthetic Control (SC)

The canonical California Proposition 99 study—estimating the effect of California's 1988 cigarette tax on cigarette consumption—provides a clear benchmark. **Arkhangelsky, Athey, Hirshberg, Imbens, and Wager (2021)** report the following estimates:

- DiD estimate: -27.34 packs per capita (SE 17.7)
- Synthetic Control estimate: -19.51 (SE 9.9)
- Synthetic DiD (SDID) estimate: -15.60 (SE 8.4)

The SDID estimate lies between the two, with time weights showing that only the last three pre-treatment periods (1986–1988) receive non-zero weights, allowing the model to focus on the most relevant pre-treatment trend. This example illustrates the fundamental tension: when parallel trends fail, DiD and SC can diverge substantially, and the choice of estimator matters for the magnitude—and sometimes sign—of the conclusion.

**O'Neill et al. (2016)** conducted the first comprehensive Monte Carlo simulation comparing DiD, synthetic control, lagged dependent variable (LDV) regression, and matching. Their key findings:

- **Under parallel trends**: DiD performs best (least biased, most precise).
- **When parallel trends is violated**: LDV reports the least biased, most efficient estimates.
- **Synthetic control and matching methods** are relatively inefficient compared to LDV.

In their empirical reanalysis of the English NHS Best Practice Tariffs (BPT) for hip fractures, the conclusions were sensitive to method choice. For surgery within 48 hours, DiD estimated a 4.03 percentage point increase (p=0.196), while LDV estimated 5.39 points (p=0.005). For mortality within 30 days, DiD reported a 0.8 percentage point reduction (p=0.037), while alternative approaches reported smaller reductions. [O'Neill et al., 2016](https://pmc.ncbi.nlm.nih.gov/articles/PMC4869762)

**Clarke, Steventon, and O'Neill (2023)** compared four synthetic control variants (Original SC, Generalized SC, Micro SC, and Bayesian SC) through Monte Carlo simulations across three scenarios: parallel trends, non-parallel trends, and non-parallel trends with serially correlated errors. The key finding: "None of the methods dominated all simulation scenarios." Generalized SC was generally preferred, performing well across a range of scenarios, though it showed bias under serial correlation with short pre-intervention periods. [Clarke et al., 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10012235)

#### 1.1.2 DiD vs. Interactive Fixed Effects (IFE)

**Gobillon and Magnac (2013)** demonstrate that "difference in differences are generically biased" when the true data generating process has interactive effects. They show that synthetic controls are equivalent to interactive effect methods when matching variables of treated areas belong to the support of control areas. Through extensive Monte Carlo experiments comparing six estimation methods, they find that methods controlling for interactive factors exhibit little bias in the baseline case, while constrained methods achieve the lowest standard errors. [Gobillon & Magnac, 2013](https://www.tse-fr.eu/sites/default/files/medias/doc/wp/etrie/wp_tse_419.pdf)

**Cummins, Smith, Miller, and Simon (2023)** identify a systematic bias in the synthetic control estimator that arises when there are finite pre-treatment periods. The bias occurs because the estimator matches on idiosyncratic error terms (noise). The bias is most severe when the treated unit's structural parameters are in the tails of the donor distribution. They find that the Interactive Fixed Effects model performs well without this "matching on noise" bias, and that bias corrections can be large enough to change qualitative interpretation and even produce estimates of differing sign. [Cummins et al., 2023](https://media.economics.uconn.edu/working/2023-07.pdf)

#### 1.1.3 Staggered DiD: TWFE vs. Heterogeneity-Robust Estimators

**Baker, Larcker, and Wang (2022)** provide the most influential demonstration of staggered DiD bias. Using Compustat data (176,670 observations, 1980–2015) with ROA as the outcome, they show that TWFE DiD estimates are unbiased only with a single treatment period or homogeneous treatment effects. When staggered timing combines with dynamic effects, biases arise that can produce wrong signs—negative estimates despite all ATTs being positive. They document that 407 of 744 DiD papers (55%) in top finance/accounting journals from 2000–2019 used staggered designs, with 97% published since 2010.

In their reanalysis of three canonical papers:
- **Beck et al. (2010)** on bank deregulation and income inequality: applying robust DiD alternatives makes the previously reported effects statistically indistinguishable from zero.
- **Fauver et al. (2017)** on board governance reforms and firm value: same result—effects become statistically indistinguishable from zero.
- **Wang et al. (2021)** on stock repurchase legalization and firm investment: "After applying various alternative DiD estimators that correct for the use of prior treated firms as comparison units, the empirical evidence does not support the conclusion that the legalization of open market repurchases significantly lowered repurchasing firms' investing behavior." [Baker et al., 2022](https://www.hbs.edu/ris/Publication%20Files/21-112_8a5a4ab3-b9e7-447d-a0fe-a504b3890fb9.pdf)

**Wang, Hamad, and White (2024)** conducted Monte Carlo simulations comparing TWFE and four heterogeneity-robust estimators (Callaway-Sant'Anna, Borusyak et al., Sun-Abraham, de Chaisemartin & D'Haultfœuille). Key results:

- TWFE performs well only under constant homogeneous effects.
- Under dynamic effects, TWFE has substantial bias (up to -78.62%).
- Heterogeneity-robust estimators perform well under parallel trends, with Callaway-Sant'Anna having the lowest bias under dynamic effects.
- When parallel trends assumption is violated, all estimators show significant bias increases.
- "Some weights may be negative... causing the DiD to have a flipped sign." [Wang et al., 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11305929)

**Goodman-Bacon (2021)** provides the decomposition that explains why: TWFE equals a weighted average of all possible 2×2 DD estimators. "A causal interpretation of two-way fixed effects DD estimates requires both a parallel trends assumption and treatment effects that are constant over time." The "forbidden comparisons"—later vs. earlier treated units—can introduce bias when treatment effects vary over time. [Goodman-Bacon, 2021](https://ideas.repec.org/a/eee/econom/v225y2021i2p254-277.html)

#### 1.1.4 Synthetic DiD as a Unifying Framework

**Arkhangelsky et al. (2021)** test SDID against DiD, SC, matrix completion, and a synthetic control with intercept in two simulation studies: one based on CPS wage data (mimicking DiD-type applications) and one based on Penn World Table GDP data (mimicking SC-type applications). Their findings:

- "SDID has excellent performance relative to the benchmarks—both in terms of bias and root-mean squared error."
- "SDID is particularly successful at mitigating bias while keeping variance in check."
- "SDID is competitive with (or dominates) DID in applications where DID methods have been used in the past, and likewise is competitive with (or dominates) SC in applications where SC methods have been used in the past." [Arkhangelsky et al., 2021](https://arxiv.org/html/1812.09970v4)

**Doudchenko and Imbens (2016)** develop a general framework that nests all these approaches, identifying five key restrictions that differentiate methods: NO-INTERCEPT, ADDING-UP, NON-NEGATIVITY, EXACT-BALANCE, and CONSTANT-WEIGHTS. They propose a new estimator using elastic-net penalty that selects 8 states for California, 13 countries (with 2 negative weights) for West Germany, and 22 control units for the Mariel boatlift study. [Doudchenko & Imbens, 2016](https://www.nber.org/system/files/working_papers/w22791/w22791.pdf)

#### 1.1.5 Pre-Testing and Pre-Trends Bias

**Roth (2022)** surveyed 70 papers from top economics journals (AER, AEJ: Applied, AEJ: Economic Policy, 2014–2018) using event-study plots. His Monte Carlo simulations reveal:

- Linear violations of parallel trends detected only 50% of the time can produce biases larger than the estimated treatment effect itself.
- In the most extreme case, a nominal 95% confidence interval contained the true parameter only 24% of the time.
- The bias conditional on passing the pre-test is often larger than the unconditional bias (up to 103% larger in some specifications).
- Under homoskedasticity and monotone violations of parallel trends, the bias after pre-testing is always worse than the unconditional bias. [Roth, 2022](https://www.ehealthecon.org/pdfs/Roth.pdf)

**Li and Strezhnev (2025)** show that the default "in-sample" imputation method for pre-trends tests creates attenuation bias that severely understates actual pre-trends. Under an equal treated/control split, in-sample estimates are roughly half the magnitude of leave-one-out estimates. [Li & Strezhnev, 2025](https://files.osf.io/v1/resources/ngr3d_v1/providers/osfstorage/68706f96563cf6854f3280e5)

#### 1.1.6 Summary of Conditions for Divergence

| Condition | Preferred Estimator | Key Finding |
|-----------|-------------------|-------------|
| Parallel trends holds | DiD | Least biased, most precise [O'Neill 2016] |
| Parallel trends violated | LDV or SC | LDV least biased; SC matches on noise [O'Neill 2016; Cummins 2023] |
| Interactive effects DGP | IFE or SC | DiD generically biased; SC works if interpolation holds [Gobillon & Magnac 2013] |
| Staggered + homogeneous effects | TWFE | Unbiased [Baker et al. 2022] |
| Staggered + dynamic effects | Heterogeneity-robust | TWFE bias up to -78.62% [Wang 2024] |
| Weak instruments | AR/CLR | 2SLS coverage collapses [Lee et al. 2022] |
| Random treatment timing | Roth-Sant'Anna | SEs 1.4–8.4× smaller than CS [Roth & Sant'Anna 2023] |

---

## Part II: Advances in Inference Reshaping Applied Practice

### 2.1 Instrumental Variables: Weak-IV-Robust Tests

The decade's most transformative change in IV practice is the recognition that conventional 2SLS Wald confidence intervals are unreliable even with first-stage F-statistics well above the traditional threshold of 10. **Lee, McCrary, Moreira, and Porter (2022)** examined 1,311 specifications from 61 AER papers (2013–2019) and found that for one-quarter of specifications, corrected standard errors are at least 49% larger at the 5% significance level and 136% larger at the 1% level compared to conventional 2SLS standard errors. [Lee et al., 2022](https://www.aeaweb.org/articles?id=10.1257/aer.20211063)

**Keane and Neal (2023, 2024)** identify a critical problem that persists even with strong instruments: the "power asymmetry." "2SLS standard errors tend to be artificially small when the estimate is close to OLS and artificially large when it is far from OLS, causing the t-test to have inflated power to detect false positive effects in the direction of OLS bias. This problem persists even with strong instruments (F well above 10)." They found 49 replicable papers where first-stage F was below 50 or not reported, and in 12 of these (24%), using AR rather than the t-test overturns a key result. [Keane & Neal, 2024](https://www.annualreviews.org/content/journals/10.1146/annurev-economics-092123-111021)

**Andrews, Stock, and Sun (2019)** surveyed 230 specifications from 17 AER papers (2014–2018) and found that many first-stage F-statistics fall in ranges raising concerns about weak instruments. Their recommendations:
1. Use the effective F-statistic of Montiel Olea & Pflueger (2013) to judge instrument strength.
2. Report Anderson-Rubin (AR) confidence intervals when there is a single instrument.
3. Choose from available robust procedures for overidentified cases. [Andrews et al., 2019](https://www.annualreviews.org/doi/10.1146/annurev-economics-080218-025643)

**The Conditional Likelihood Ratio (CLR) test** (Moreira, 2003) retains AR's weak-IV robustness while improving power with many instruments. **Andrews, Moreira, and Stock (2006)** proved that CLR is "numerically nearly uniformly most powerful invariant (UMPI) among two-sided tests—its power function is essentially on the power envelope." They recommend the use of the CLR test in empirical practice. [Andrews et al., 2006](http://dido.econ.yale.edu/~dwka/pub/p1168.pdf)

**Practical implications for applied work:**

- **F > 10 is not enough**: The tF procedure requires F > 104.7 for standard critical values to be valid. Alternatively, if keeping F=10, the t-stat critical value should be at least 3.43.
- **AR is now the primary recommendation**: Keane and Neal advocate "abandoning the t-test altogether and using AR even when the instrument is strong."
- **Stata 19** now includes `estat weakrobust` for AR and CLR tests, supporting all ivregress estimators.

### 2.2 Difference-in-Differences: Heterogeneity-Robust Estimators

The development of heterogeneity-robust DiD estimators is the most significant methodological advance of the decade. The core problem is that TWFE regression with staggered adoption produces a weighted average of cohort-specific treatment effects where some weights can be negative, potentially yielding estimates with the wrong sign.

**Callaway and Sant'Anna (2021)** propose a divide-and-conquer strategy: break the staggered panel into many 2×2 DiD estimates, then combine with user-chosen weights. Key features:
- Uses ATT(g,t) as a building block.
- Doubly robust by default: combines outcome regression and inverse propensity weighting; consistent if either model is correct.
- Produces simultaneous (uniform) confidence bands valid across the full event-study path.
- Three estimators supported: outcome regression, inverse propensity weighting, and doubly robust (recommended). [Callaway & Sant'Anna, 2021](https://www.sciencedirect.com/science/article/abs/pii/S0304407620303948)

**Sun and Abraham (2021)** show that TWFE event-study coefficients are contaminated by effects from other periods, and apparent pretrends can arise solely from treatment effects heterogeneity. Their interaction-weighted estimator computes cohort-specific dynamic treatment effects and aggregates them with sample-size weights, eliminating the negative-weight contamination. [Sun & Abraham, 2021](https://ideas.repec.org/a/eee/econom/v225y2021i2p175-199.html)

**Borusyak, Jaravel, and Spiess (2024)** develop the imputation estimator, which:
1. Runs OLS on untreated observations to estimate unit + time fixed effects.
2. Imputes counterfactual Y(0) for treated observations.
3. Aggregates imputed treatment effects with researcher-chosen weights.

The imputation estimator produces ~50% shorter CIs than Callaway-Sant'Anna and Sun-Abraham (2–3.5× shorter) under homogeneous treatment effects. However, the survey by **de Chaisemartin & D'Haultfœuille** notes that "The estimators in Borusyak et al. (2021) may be more biased than those in Callaway and Sant'Anna (2021) or Sun and Abraham (2021) when parallel trends does not exactly hold." [Borusyak et al., 2024](https://ideas.repec.org/a/oup/restud/v91y2024i6p3253-3285.html)

**de Chaisemartin and D'Haultfœuille (2020, 2023, 2024)** developed the DID_M estimator for binary or non-binary treatments, and extended the framework to several treatments. Their 2023 paper shows that "TWFE regressions with several treatments... may be contaminated by other treatments' effects." They provide tools (the `twowayfeweights` Stata and R packages) to compute the weights attached to TWFE regressions. [de Chaisemartin & D'Haultfœuille, 2023](https://www.sciencedirect.com/science/article/abs/pii/S0304407623001963)

**Gardner (2021)** developed a one-stage robust DiD regression that is numerically equivalent to the two-stage estimator and the imputation estimator, but can be obtained via a single regression with automatically valid asymptotic standard errors.

**Roth and Sant'Anna (2023)** show that if treatment timing is as good as randomly assigned, one can obtain more precise estimates than those provided by DiD-based methods. In the Chicago police procedural justice training application, standard errors are 1.4 to 8.4 times smaller than the Callaway & Sant'Anna (2021) estimator. [Roth & Sant'Anna, 2023](https://arxiv.org/pdf/2102.01291)

**Pass condition for staggered DiD papers**: Either (a) the paper uses a heterogeneity-robust estimator as its primary specification, OR (b) the paper uses TWFE but reports robustness to a heterogeneity-robust estimator and discusses the Goodman-Bacon decomposition explicitly. [Research Unit Tests](https://www.ricardodahis.com/research-unit-tests/tests/did-staggered-heterogeneous-effects)

### 2.3 Synthetic Control: Conformal and Bayesian Inference

**Chernozhukov, Wüthrich, and Zhu (2021)** introduce conformal inference methods for synthetic controls that are "valid under weak and easy-to-verify conditions, and are provably robust against misspecification." Their permutation inference procedure works with various approaches for predicting counterfactual mean outcomes, including synthetic controls, difference-in-differences, factor and matrix completion models, and time series panel data models. The method demonstrates excellent small-sample performance in simulations. [Chernozhukov et al., 2021](https://www.tandfonline.com/doi/abs/10.1080/01621459.2021.1920957)

The `coresynth` R package implements the permutation-based conformal inference procedure via the `conformal_inference()` function, which tests a sharp null hypothesis H0: τ = τ0 by imputing treated post-treatment counterfactuals, re-estimating the counterfactual proxy on all T periods, and computing a moving-block permutation p-value.

**Firpo and Possebom (2018)** extend inference for the synthetic control method in two ways: (1) introducing a parametric form for treatment assignment probabilities, enabling sensitivity analysis around the uniform distribution assumption; (2) modifying the RMSPE statistic to test any sharp null hypothesis and inverting the test to construct confidence sets. In Monte Carlo experiments, the RMSPE statistic has good properties with respect to size, power, and robustness. [Firpo & Possebom, 2018](https://econpapers.repec.org/RePEc:bpj:causin:v:6:y:2018:i:2:p:26:n:1)

**Bayesian approaches** have emerged as an alternative inference framework. **Martinez and Vives-i-Bastida (2022, revised 2024)** propose a Bayesian alternative that preserves the main features of the standard method and provides a new way of doing valid inference, with a Bernstein-von Mises result linking Bayesian and frequentist inference. **Xu and Pang (2020)** develop a dynamic multilevel latent factor model with hierarchical shrinkage that assigns observation-specific parameters to covariates of treated units and exploits high-order relationships between treated and control time series, producing smaller biases, higher efficiency, and narrower uncertainty intervals.

**Sakaguchi & Tagawa (2026) Bayesian Spatial Synthetic Control** applied to California's Proposition 99 reveals that classical SCM's sparsity is partly a constraint artifact. The Bayesian horseshoe SCM (no spillovers) gives ATT = -15.84 packs/capita with 23 active donors (vs. 4 in classical SC). The Bayesian Spatial SAR model (horseshoe + spatial autocorrelation) gives ATT = -16.59 packs/capita with 27 active donors and ρ = 0.223—clearly non-zero, confirming SUTVA violation. Nevada absorbs a dominant spillover effect of -3.75 packs/capita, demonstrating that classical SCM's "sparsity" is partly an artifact of the simplex constraint. [Mendez, 2026](https://carlos-mendez.org/post/r_sc_bayes_spatial)

**Abadie (2020)** provides comprehensive guidance: synthetic control estimators preclude extrapolation, make transparent the actual discrepancy between the treated unit and the convex combination of untreated units, and have bias bounded under a linear factor model when the synthetic control closely reproduces treated unit characteristics. Risk of overfitting increases with donor pool size, especially when T0 is small. [Abadie, 2020](https://www.aeaweb.org/content/file?id=12409)

### 2.4 Regression Discontinuity: Bias-Corrected RD with Robust Bandwidth Selection

**Calonico, Cattaneo, and Titiunik (2014, Econometrica)** introduced robust bias-corrected (RBC) confidence intervals for RD designs, fundamentally changing applied practice. The key innovation is that conventional local polynomial RD confidence intervals based on undersmoothing suffer from coverage error that decays slowly, while bias-corrected intervals achieve better coverage properties by explicitly estimating and removing the bias term. [Calonico et al., 2014](https://www.econometricsociety.org/publications/econometrica/2014/11/01/robust-nonparametric-confidence-intervals-regression-discontinuity)

**Calonico, Cattaneo, Farrell, and Titiunik (2019)** extended the framework to incorporate pre-intervention covariates, which can improve precision and address potential biases.

**Calonico, Cattaneo, and Farrell (2020)** derived the crucial distinction between MSE-optimal bandwidths (for point estimation) and CER-optimal bandwidths (for inference). Key findings:

- "The MSE-optimal bandwidth yields an MSE-optimal RD treatment effect estimator, but is by construction invalid for inference."
- RBC confidence intervals have "strictly smaller (i.e., vanishing faster) coverage error than those of interval estimators based on undersmoothing."
- For p=1 (local linear RD) and n=500, the CER-optimal bandwidth is approximately 27% smaller than the MSE-optimal bandwidth.
- They provide data-driven implementations: a rule-of-thumb (ROT) rescaling and a direct plug-in (DPI) estimator. [Calonico et al., 2020](https://maxhfarrell.com/research/Calonico-Cattaneo-Farrell2020_ECTJ.pdf)

The `rdrobust` R package (version 4.0.0) implements these methods, supporting sharp, fuzzy, and kink RD designs, with data-driven bandwidth selection procedures (MSE-optimal and CER-optimal), and robust bias-corrected confidence intervals.

**How CCT changed practice:**

- Replaced "undersmoothing" (using a smaller bandwidth to reduce bias at the cost of higher variance) with a formal bias-correction procedure that allows larger bandwidths and better coverage properties.
- Provided data-driven bandwidth selection methods (CCT) that became the de facto standard.
- Disseminated through widely-used software packages (rdrobust in R, Stata, and Python).
- Clarified that different bandwidth choices are appropriate for different inferential goals.

### 2.5 Interactive Fixed Effects: Factor-Model Approaches

**Bai (2009, Econometrica)** developed the foundational estimation and inference framework for panel data models with interactive fixed effects, where the error term has a factor structure: u_it = λ'_i F_t + ε_it. The least squares estimator is √NT consistent under large N and T, but asymptotic biases arise when both dimensions have correlations/heteroskedasticity. Bai provides bias-corrected estimators and develops Hausman tests for testing additive versus interactive effects. [Bai, 2009](https://ideas.repec.org/a/ecm/emetrp/v77y2009i4p1229-1279.html)

**Moon and Weidner (2015, Econometrica)** provide a crucial practical result: "The limiting distribution of the LS estimator is independent of the number of factors used in the estimation as long as this number is not underestimated." This means practitioners can conservatively overestimate the number of factors without harming inference on the regression coefficients. [Moon & Weidner, 2015](https://ideas.repec.org/a/wly/emetrp/v83y2015i4p1543-1579.html)

**Moon and Weidner (2017, Econometric Theory)** extend the framework to dynamic models with predetermined regressors, identifying two sources of asymptotic bias: bias due to correlation or heteroscedasticity of the idiosyncratic error term, and bias due to predetermined regressors. They provide bias-corrected LS estimators and bias-corrected versions of Wald, LR, and LM tests. [Moon & Weidner, 2017](https://www.cambridge.org/core/journals/econometric-theory/article/dynamic-linear-panel-regression-models-with-interactive-fixed-effects/CE84629C05BB652892D7B7659A1D5CD5)

**Armstrong, Kolesár, and Plagborg-Møller (2023)** address a critical gap: existing estimators might be "heavily biased and size-distorted when some of the factors are weak." Their approach applies the theory of minimax linear estimation to form a debiased estimate using a nuclear norm bound. In Monte Carlo experiments, they find substantial improvement over conventional approaches when factors are weak, with little cost when factors are strong. The debiased estimator achieves a rate of O(1/min{N,T}) compared to the slower rate of conventional approaches. [Armstrong et al., 2023](https://tbarmstr.github.io/files/2023/07/robust_IFEs.pdf)

**Callaway and Karami (2023)** develop a new approach for identifying and estimating the ATT when untreated potential outcomes are generated by an interactive fixed effects model, but without requiring the number of time periods to go to infinity. The ATT can be identified with as few as three time periods, using either panel or repeated cross-sections data. [Callaway & Karami, 2023](https://www.sciencedirect.com/science/article/abs/pii/S030440762200029X)

**Brown and Butts (2023)** introduce a method for estimating dynamic ATEs in staggered intervention settings when parallel trends hold only after conditioning on unobserved interactive fixed effects. Their factor imputation estimator is unbiased across all scenarios in Monte Carlo simulations, including when parallel trends fail, while TWFE estimators exhibit severe bias (e.g., bias of -4.90 for τ_8 in the factor model with non-parallel trends). In their empirical application to Walmart openings and county-level employment, "TWFE event-study estimates show positive pre-trends, suggesting selection bias. Their factor model estimator ameliorates these pre-trend violations, isolating the causal effect of Walmart openings." [Brown & Butts, 2023](https://www.econ.queensu.ca/sites/econ.queensu.ca/files/Nick%20Brown%20Brown%20Bag%20Talk.pdf)

---

## Part III: Publication Record and Shifting Norms

### 3.1 Quantitative Trends in Top-Five Journals

**Goldsmith-Pinkham (2026)** provides the most comprehensive and up-to-date quantitative analysis, examining approximately 44,000 papers—31,500 NBER working papers (1982–2025) and 12,300 articles from top economics and finance journals (2011–2024). Three main findings:

1. **Uneven spread across fields**: "As of 2024, 63 percent of applied micro papers mention experimental or quasi-experimental methods, compared to 47 percent in finance and 39 percent in macro/other." The current levels in finance and macro/other are comparable to where applied micro was in 2008–2010.

2. **A difference-in-differences revolution**: "The credibility revolution outside applied micro has been—to a first approximation—a difference-in-differences revolution." "Including DiD raises the finance methods share by roughly 55 percent versus 30 percent for applied micro."

3. **Gap between econometric theory and applied practice**: "I document a pronounced gap between the methods studied in the Journal of Econometrics—where nonparametric estimation, bootstrap methods, and asymptotic theory dominate—and those used by applied researchers, where DiD and identification strategies are the dominant tools."

The paper validates its keyword matching approach against hand-coded labels and LLM classification, achieving 80–92% agreement rates. Published journal articles confirm the NBER patterns, showing slightly higher rates of credibility revolution methods—consistent with a publication selection effect favoring methodologically rigorous papers. [Goldsmith-Pinkham, 2026](https://www.nber.org/system/files/working_papers/w35051/w35051.pdf)

**Causal Claims in Economics (2025)** analyzes over 44,000 NBER and CEPR working papers from 1980–2023 using a custom large language model. Key findings:

- "We document a substantial rise in the share of causal claims—from roughly 4% in 1990 to nearly 28% in 2020—reflecting the growing influence of the 'credibility revolution.'"
- "Causal narrative complexity (e.g., the depth of causal chains) strongly predicts both publication in top-5 journals and higher citation counts, whereas non-causal complexity tends to be uncorrelated or negatively associated with these outcomes."
- "Novelty is also pivotal for top-5 publication, but only when grounded in credible causal methods: introducing genuinely new causal edges or paths markedly increases both the likelihood of acceptance at leading outlets and long-run citations, while non-causal novelty exhibits weak or even negative effects."
- Methods like DiD, IV, RCTs, and RDDs have seen substantial growth, while theoretical work has declined. [Causal Claims in Economics, 2025](https://arxiv.org/html/2501.06873v1)

**Galofré-Vilà (2026)** examines knowledge production patterns in the top-five journals from 2000 to 2024. The study documents that "the share of theoretical work has declined, while empirical fields, particularly development, labor, and public economics, have expanded and received substantially higher citation counts." Despite these changes, the structure of scholarly knowledge production remains hierarchical, "suggesting that intellectual innovation occurs within a stable institutional core of elite U.S. universities." [Galofré-Vilà, 2026](https://www.sciencedirect.com/science/article/pii/S0147596726000296)

**Currie, Kleven, and Zwiers (2020)** used text mining to track methods in top-five economics journals, observing that "the larger trends toward demanding greater credibility and transparency from researchers in applied economics and a 'collage' approach to assembling evidence will likely continue." [Currie et al., 2020](https://www.aeaweb.org/articles?id=10.1257/pandp.20201058)

### 3.2 Journal-Specific Patterns

**Reuben et al. (2022)** investigates trends in experimental economics publications from 2000 to 2021 across seven leading general-interest economics journals. Key findings:

- 4.3% of all articles were lab experiments; 5.3% were other experiments.
- The share of experimental articles increased by 2.7 percentage points over 22 years.
- "The share of lab experiments has more than halved in the AER and remained low in other Top 5 journals."
- "It is currently four times more difficult to publish a lab experiment in a Top 5 journal than other types of experiments."
- Lab experiments receive fewer 3-year citations (78.42 in AER) than other experiments (142.54, p<0.001). [Reuben et al., 2022](http://ereuben.net/research/ExpEconPubs.pdf)

**Gschwent et al. (2025)** finds that health economics grew from 2% to 6% of top-5 journal articles between the mid-1990s and 2020, with health economics papers scoring consistently higher on "quality" than other economics fields. [Gschwent et al., 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12680912)

### 3.3 The Credibility vs. Structure Debate

The 2010 *Journal of Economic Perspectives* symposium crystallized the debate that has shaped the decade. **Angrist and Pischke (2010)** argued that "the primary engine driving improvement has been a focus on the quality of empirical research designs," contrasting with Leamer's (1983) proposed remedy of sensitivity analysis. They noted progress has been slower in macroeconomics and industrial organization. [Angrist & Pischke, 2010](https://www.nber.org/system/files/working_papers/w15794/w15794.pdf)

**Rust (2010)** countered: "The fact is, economics is not an experimental science and cannot be. 'Natural' experiments and 'quasi' experiments are not in fact experiments." [Rust, 2010](https://www.aeaweb.org/articles?id=10.1257%2Fjep.24.2.59)

**Nevo and Whinston (2010)** argued that structural analysis and credible identification are complements, not substitutes. Using merger analysis as a case study, they showed that structural methods can provide extrapolation to not-yet-observed changes, while treatment effects face difficulties in defining "similar" mergers, ensuring exogeneity, and producing welfare measures. [Nevo & Whinston, 2010](https://www.aeaweb.org/articles?id=10.1257%2Fjep.24.2.69)

**Keane (2010)** argued that "all econometric work relies heavily on a priori assumptions. The main difference between structural and experimental (or 'atheoretic') approaches is not in the number of assumptions but the extent to which they are made explicit." Using the Angrist (1990) Vietnam draft lottery study, he demonstrated that "despite having an 'ideal' instrument, the estimate of -15% effect of military service on earnings cannot be meaningfully interpreted without theoretical assumptions." [Keane, 2010](https://www.sciencedirect.com/science/article/abs/pii/S0304407609001948)

**Einav and Levin (2010)** argued that "the use of economic theory and the search for compelling sources of identifying variation are not enemies," defending the IO approach of theory-guided empirical work. [Einav & Levin, 2010](https://www.nber.org/system/files/working_papers/w15786/w15786.pdf)

**Heckman and Urzúa (2009)** demonstrated that structural models can identify separate gains at each margin, while IV only produces a single net effect that masks heterogeneous gains. They argued that "the choice between IV and structural approaches should be driven by the economic question being asked, not by convenience or tradition." [Heckman & Urzúa, 2009](https://www.cemmap.ac.uk/wp-content/uploads/2020/08/CWP0810.pdf)

### 3.4 The 2021 Nobel Prize and Its Impact

The 2021 Nobel Prize in Economics was awarded to **David Card, Joshua Angrist, and Guido Imbens** "for their methodological contributions to the analysis of causal relationships." The Nobel Committee stated: "The work of the Laureates has revolutionised empirical research in the social sciences and significantly improved the ability of the research community to answer questions of great importance to us all." [Nobel Prize Committee, 2021](https://www.nobelprize.org/prizes/economic-sciences/2021/popular-information)

The LATE framework (Imbens and Angrist, 1994, *Econometrica*) showed that "even when natural experiments are imperfect (like the Vietnam draft lottery), researchers can still estimate causal effects for specific subpopulations—those who receive treatment only because of the instrument." The paper was initially largely ignored; Harvard rejected Imbens' tenure application in 1997. By 2022, it had over 6,500 citations. [Stanford GSB, 2021](https://www.gsb.stanford.edu/insights/unexpected-result-how-nobelist-guido-imbens-helped-kick-start-credibility-revolution)

### 3.5 How Credible is the Credibility Revolution?

**Lang (2023)** critically examines the credibility revolution, finding that "65% of narrowly rejected null hypotheses and 41% of all rejected null hypotheses with |t|<10 are likely to be false rejections." "For the null to have only a .05 probability of being true requires a t of 5.48." The paper finds little evidence of p-hacking; instead, there is weak evidence of publication bias against marginally significant results. [Lang, 2023](https://www.nber.org/system/files/working_papers/w31666/w31666.pdf)

**Angrist, Azoulay, Ellison, Hill, and Lu (2020)** find that economics has become the most widely cited social science in 7 of 16 disciplines examined, and that "much of the rise in economics' extramural influence reflects growth in citations to empirical work." [Angrist et al., 2020](https://economics.mit.edu/sites/default/files/2024-07/angrist-et-al-2020-inside-job-or-deep-impact-extramural-citations-and-the-influence-of-economic-scholarship.pdf)

### 3.6 What the Publication Record Shows About Shifting Norms

The evidence from the publication record reveals several key shifts in norms:

1. **Quasi-experimental methods are now the baseline expectation**: As of 2024, 63% of applied micro papers mention experimental or quasi-experimental methods. The "credibility revolution" is no longer a revolution but the established paradigm.

2. **Structural modeling persists but adapts**: Structural estimation remains common in IO and macro (where papers are roughly twice as likely to rely on structural models without complementary quasi-experimental methods), but the bar has risen. Papers that combine structural modeling with credible identification are increasingly favored.

3. **DiD has become the dominant method**: The credibility revolution outside applied micro has been "a difference-in-differences revolution." DiD is mentioned in 55% more finance papers and 30% more applied micro papers than would be the case without it.

4. **The gap between theory and applied practice persists**: Methods studied in the *Journal of Econometrics*—nonparametric estimation, bootstrap methods, asymptotic theory—differ markedly from those used by applied researchers, where DiD and identification strategies dominate.

5. **Causal complexity predicts publication success**: Causal narrative complexity (depth of causal chains) strongly predicts both publication in top-5 journals and higher citation counts, while non-causal complexity is uncorrelated or negatively associated.

6. **The field hierarchy remains**: Despite changes in research topics and methods, a small group of U.S. universities continues to account for a disproportionate share of highly cited work.

---

## Conclusions

The decade 2014–2024 transformed the practice of causal inference in economics. The canonical implementations of 2014—TWFE DiD, simple 2SLS with F>10, synthetic control with permutation tests, RD with MSE-optimal bandwidths, and additive fixed effects—are no longer sufficient for top-5 publication. The new standards require:

- **For IV**: Weak-IV-robust inference (AR or CLR) as primary or secondary specification, acknowledgment that F>10 is insufficient, and reporting of effective F-statistics.
- **For staggered DiD**: Heterogeneity-robust estimators (Callaway-Sant'Anna, Sun-Abraham, Borusyak et al., or de Chaisemartin & D'Haultfœuille) as primary specification, or TWFE with explicit Goodman-Bacon decomposition and robustness checks. Pre-trends testing is recognized as potentially misleading.
- **For synthetic control**: Conformal inference, sensitivity analysis (Firpo-Possebom), or Bayesian approaches that relax the simplex constraint and address SUTVA violations. Pre-intervention fit length is recognized as critical.
- **For RD**: Robust bias-corrected confidence intervals with CER-optimal bandwidth selection (CCT/CCF). Using covariates for precision improvement is standard practice.
- **For interactive fixed effects**: Factor-model approaches that handle weak factors (Armstrong et al.) and work with short panels (Callaway-Karami). The number of factors can be conservatively overestimated without harming inference.

The credibility revolution has been won, but the battle over its interpretation continues. The most impactful work now combines careful design, credible inference, and thoughtful modeling—recognizing that the choice between estimators should be driven by the economic question, not by convenience or tradition.

---

### Sources

[1] O'Neill et al. (2016): https://pmc.ncbi.nlm.nih.gov/articles/PMC4869762

[2] Wang, Hamad, White (2024): https://pmc.ncbi.nlm.nih.gov/articles/PMC11305929

[3] Clarke, Steventon, O'Neill (2023): https://pmc.ncbi.nlm.nih.gov/articles/PMC10012235

[4] Gobillon & Magnac (2013): https://www.tse-fr.eu/sites/default/files/medias/doc/wp/etrie/wp_tse_419.pdf

[5] Cummins et al. (2023): https://media.economics.uconn.edu/working/2023-07.pdf

[6] Arkhangelsky et al. (2021): https://arxiv.org/html/1812.09970v4

[7] Roth (2022): https://www.ehealthecon.org/pdfs/Roth.pdf

[8] Li & Strezhnev (2025): https://files.osf.io/v1/resources/ngr3d_v1/providers/osfstorage/68706f96563cf6854f3280e5

[9] Baker, Larcker, Wang (2022): https://www.hbs.edu/ris/Publication%20Files/21-112_8a5a4ab3-b9e7-447d-a0fe-a504b3890fb9.pdf

[10] Doudchenko & Imbens (2016): https://www.nber.org/system/files/working_papers/w22791/w22791.pdf

[11] Goodman-Bacon (2021): https://ideas.repec.org/a/eee/econom/v225y2021i2p254-277.html

[12] Callaway & Sant'Anna (2021): https://www.sciencedirect.com/science/article/abs/pii/S0304407620303948

[13] Sun & Abraham (2021): https://ideas.repec.org/a/eee/econom/v225y2021i2p175-199.html

[14] Borusyak, Jaravel, Spiess (2024): https://ideas.repec.org/a/oup/restud/v91y2024i6p3253-3285.html

[15] de Chaisemartin & D'Haultfœuille (2023): https://www.sciencedirect.com/science/article/abs/pii/S0304407623001963

[16] Roth & Sant'Anna (2023): https://arxiv.org/pdf/2102.01291

[17] Callaway & Karami (2023): https://www.sciencedirect.com/science/article/abs/pii/S030440762200029X

[18] Chernozhukov, Wüthrich, Zhu (2021): https://www.tandfonline.com/doi/abs/10.1080/01621459.2021.1920957

[19] Firpo & Possebom (2018): https://econpapers.repec.org/RePEc:bpj:causin:v:6:y:2018:i:2:p:26:n:1

[20] Abadie (2020): https://www.aeaweb.org/content/file?id=12409

[21] Calonico, Cattaneo, Titiunik (2014): https://www.econometricsociety.org/publications/econometrica/2014/11/01/robust-nonparametric-confidence-intervals-regression-discontinuity

[22] Calonico, Cattaneo, Farrell (2020): https://maxhfarrell.com/research/Calonico-Cattaneo-Farrell2020_ECTJ.pdf

[23] Bai (2009): https://ideas.repec.org/a/ecm/emetrp/v77y2009i4p1229-1279.html

[24] Moon & Weidner (2015): https://ideas.repec.org/a/wly/emetrp/v83y2015i4p1543-1579.html

[25] Moon & Weidner (2017): https://www.cambridge.org/core/journals/econometric-theory/article/dynamic-linear-panel-regression-models-with-interactive-fixed-effects/CE84629C05BB652892D7B7659A1D5CD5

[26] Armstrong, Kolesár, Plagborg-Møller (2023): https://tbarmstr.github.io/files/2023/07/robust_IFEs.pdf

[27] Lee, McCrary, Moreira, Porter (2022): https://www.aeaweb.org/articles?id=10.1257/aer.20211063

[28] Keane & Neal (2024): https://www.annualreviews.org/content/journals/10.1146/annurev-economics-092123-111021

[29] Andrews, Stock, Sun (2019): https://www.annualreviews.org/doi/10.1146/annurev-economics-080218-025643

[30] Andrews, Moreira, Stock (2006): http://dido.econ.yale.edu/~dwka/pub/p1168.pdf

[31] Xu (2017): https://www.cambridge.org/core/journals/political-analysis/article/generalized-synthetic-control-method-causal-inference-with-interactive-fixed-effects-models/B63A8BD7C239DD4141C67DA10CD0E4F3

[32] Brown & Butts (2023): https://www.econ.queensu.ca/sites/econ.queensu.ca/files/Nick%20Brown%20Brown%20Bag%20Talk.pdf

[33] Goldsmith-Pinkham (2026): https://www.nber.org/system/files/working_papers/w35051/w35051.pdf

[34] Causal Claims in Economics (2025): https://arxiv.org/html/2501.06873v1

[35] Galofré-Vilà (2026): https://www.sciencedirect.com/science/article/pii/S0147596726000296

[36] Currie, Kleven, Zwiers (2020): https://www.aeaweb.org/articles?id=10.1257/pandp.20201058

[37] Reuben et al. (2022): http://ereuben.net/research/ExpEconPubs.pdf

[38] Gschwent et al. (2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12680912

[39] Angrist & Pischke (2010): https://www.nber.org/system/files/working_papers/w15794/w15794.pdf

[40] Rust (2010): https://www.aeaweb.org/articles?id=10.1257%2Fjep.24.2.59

[41] Nevo & Whinston (2010): https://www.aeaweb.org/articles?id=10.1257%2Fjep.24.2.69

[42] Keane (2010): https://www.sciencedirect.com/science/article/abs/pii/S0304407609001948

[43] Einav & Levin (2010): https://www.nber.org/system/files/working_papers/w15786/w15786.pdf

[44] Heckman & Urzúa (2009): https://www.cemmap.ac.uk/wp-content/uploads/2020/08/CWP0810.pdf

[45] Nobel Prize Committee (2021): https://www.nobelprize.org/prizes/economic-sciences/2021/popular-information

[46] Stanford GSB (2021): https://www.gsb.stanford.edu/insights/unexpected-result-how-nobelist-guido-imbens-helped-kick-start-credibility-revolution

[47] Lang (2023): https://www.nber.org/system/files/working_papers/w31666/w31666.pdf

[48] Angrist et al. (2020): https://economics.mit.edu/sites/default/files/2024-07/angrist-et-al-2020-inside-job-or-deep-impact-extramural-citations-and-the-influence-of-economic-scholarship.pdf

[49] Mendez (2026): https://carlos-mendez.org/post/r_sc_bayes_spatial

[50] Research Unit Tests (DiD): https://www.ricardodahis.com/research-unit-tests/tests/did-staggered-heterogeneous-effects
