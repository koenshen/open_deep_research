# Redefining Credibility Standards in Quasi-Experimental Methods: A Synthesis of Top-Five Economics Journals, 2014–2024

## Introduction

Between 2014 and 2024, the top five economics journals (American Economic Review, Quarterly Journal of Economics, Journal of Political Economy, Econometrica, and Review of Economic Studies) witnessed a profound redefinition of credibility standards for quasi-experimental research. This synthesis examines how the five core estimators—instrumental variables (IV), difference-in-differences under staggered adoption (DiD), synthetic control (SC), regression discontinuity (RDD), and interactive fixed-effects panel methods—have been reshaped through comparative validation, inferential advances, and shifting publication norms. The analysis draws exclusively on original articles published in these journals, supplemented by closely related high-impact outlets, to trace the arc from the "credibility revolution" of the late 2000s to the more mature, nuanced, and at times controversial landscape of the mid-2020s.

---

## 1. Comparative Simulations and Head-to-Head Applications: When Estimators Diverge

A defining feature of the 2014–2024 period is the systematic comparison of quasi-experimental estimators on the same data or in simulation. These exercises reveal that the choice of estimator matters most when treatment effects are heterogeneous, parallel trends are violated, instruments are weak, or the identifying assumptions of one method are nested within more general models.

### 1.1 IV vs. DiD vs. Synthetic Control: The Synthetic IV and SDID Innovations

**Synthetic Difference-in-Differences (SDID)** , introduced by Arkhangelsky, Athey, Hirshberg, Imbens, and Wager (2021) in the *American Economic Review*, directly compares DiD, synthetic control, and the new hybrid. In the California smoking cessation program (Proposition 99), SDID yields an estimate of –15.6 packs/year, compared to –27.3 for traditional DiD and –19.6 for synthetic control. Placebo studies calibrated to Current Population Survey and Penn World Table data show that SDID dominates both parent methods in bias and root-mean-squared error across a wide range of assignment mechanisms and outcome models, particularly when treatment assignment is non-random. The paper's key insight is that SDID is "doubly robust": it remains consistent under either the DiD parallel-trends assumption or the synthetic control convex-hull pre-treatment match assumption [1].

**Synthetic Instrumental Variables (SIV)** , developed by Gulek and Vives-i-Bastida (2024), addresses a different failure mode. Standard IV fails when unmeasured confounding persists after controlling for observables. The SIV estimator combines synthetic control weights with IV to construct a better instrument. In three empirical applications—Syrian refugees and Turkish labor markets, the China shock, and digital economics rankings—standard IV finds no effect or upward bias, while SIV recovers significant effects that align with experimental benchmarks. The paper demonstrates that when standard IV suffers from pre-trends or weak relevance, SIV can correct for both [2].

### 1.2 DiD vs. Interactive Fixed Effects: When Parallel Trends Fails

The relationship between DiD and interactive fixed-effects (IFE) models is now well understood. **Magnac (2014)** shows theoretically that DiD is generically biased when the true data-generating process has interactive effects, because the additive unit and time fixed effects cannot capture interactions between unobserved factors. Monte Carlo experiments compare Bai's least squares, synthetic control, propensity score matching, and DiD, finding that the bias is largest when factor loadings differ systematically between treated and control groups. An application to a French enterprise zone program confirms that the estimated impact is robust to IFE modeling but sensitive to the choice of method [3].

**Xu (2017)** , in *Political Analysis*, proposes the Generalized Synthetic Control method that unifies SC with IFE models. The method estimates latent factors using control group data, then imputes counterfactuals for treated units. Unlike DiD, it allows treatment to be correlated with unobserved heterogeneity. In simulations, GSC dominates DiD when the parallel trends assumption is violated, and it accommodates multiple treated units and variable treatment periods—a key advantage over the original synthetic control [4].

**Callaway and Karami (2023)** , in the *Journal of Econometrics*, develop a method for ATTs under IFE models with as few as three time periods. Monte Carlo simulations show that the IFE approach yields smaller long-term effects and better pre-treatment placebo estimates than DiD in an application to early-career job displacement. The method generalizes both DiD and individual-specific linear trend models [5].

**Brown and Butts (2025)** , in the *Journal of Econometrics*, propose a factor imputation estimator for dynamic treatment effects with staggered adoption. Applied to Walmart store openings and county employment, the estimator corrects pre-trend violations that plague two-way fixed effects (TWFE) estimates. Monte Carlo simulations confirm that the factor imputation estimator is unbiased when parallel trends fail, while TWFE and TWFE with noisy proxies remain biased [6].

### 1.3 TWFE vs. Heterogeneity-Robust DiD: The Staggered Adoption Crisis

The most consequential methodological development of the 2014–2024 period is the exposure of biases in two-way fixed effects regressions with staggered treatment timing and heterogeneous treatment effects. The core insight, developed across multiple papers, is that the TWFE estimator is a weighted average of all possible 2×2 DiD estimators, with some weights potentially negative due to "forbidden comparisons" where already-treated units serve as controls for later-treated units.

**de Chaisemartin and D'Haultfœuille (2020)** , in the *American Economic Review*, demonstrate that linear regressions with period and group fixed effects estimate weighted sums of average treatment effects, with weights that may be negative. In two replications (Enikolopov et al. 2011, Gentzkow et al. 2011), about half of the weights are negative. Their proposed estimator, DID_M, finds effects that are 66% larger than the TWFE estimate in the Gentzkow et al. study, and of opposite sign in some cases. A survey of AER articles (2010–2012) finds that 20% use two-way FE regressions, making the problem pervasive [7].

**Goodman-Bacon (2021)** , in the *Journal of Econometrics*, provides the decomposition that explains these results. The TWFE estimator equals a weighted average of all possible 2×2/2-period DiD estimators. Negative weights arise only when treatment effects vary over time. Using the Stevenson and Wolfers (2006) study of unilateral divorce laws and female suicide, the TWFE estimate (−3.08) understates the average post-treatment effect (about −5) because 37% of the identifying variation comes from timing comparisons that are contaminated by dynamic treatment effects [8].

**Callaway and Sant'Anna (2021)** , in the *Journal of Econometrics*, develop a comprehensive framework for group-time average treatment effects (ATT(g,t)) under conditional parallel trends. An application to minimum wage effects on teen employment (2001–2007) shows that their overall ATT estimate (−0.057) is about 50% larger than the TWFE estimate (−0.038), with differences attributed to pre-treatment trends (64%) and weighting (36%). The method is available in the R package 'did' [9].

**Sun and Abraham (2021)** , in the *Journal of Econometrics*, show that event-study TWFE specifications suffer from contamination: coefficients on leads and lags can be affected by effects from other periods, and apparent pre-trends can arise solely from treatment effect heterogeneity, not actual violations of parallel trends. Their interaction-weighted estimator is free of this contamination. An application to hospitalization effects (HRS data) shows that TWFE estimates can fall outside the convex hull of the underlying effects [10].

**Borusyak, Jaravel, and Spiess (2024)** , in the *Review of Economic Studies*, develop an imputation estimator that is efficient linear unbiased under spherical errors. The estimator first estimates unit and period fixed effects from untreated observations only, then imputes untreated potential outcomes. In an application to the marginal propensity to spend out of U.S. tax rebates, they find a quarterly MPX for nondurables of 8–11%—about half of benchmark estimates—and a short-lived effect concentrated in the first month [11].

**Baker, Larcker, and Wang (2022)** , in the *Journal of Financial Economics*, provide simulation evidence that TWFE estimates are unbiased only with a single treatment period or homogeneous effects. With dynamic and heterogeneous effects, estimates can have the wrong sign or produce severe Type-I/II errors (e.g., 80% false positive rates with small heterogeneity). Replications of Beck et al. (2010) on bank deregulation and income inequality, and Fauver et al. (2017) on board reforms, show that applying robust estimators often yields substantially different causal estimates [12].

### 1.4 IV vs. RDD: Weak Identification in Fuzzy Designs

The connection between fuzzy RDD and IV is theoretically well-established, but the practical implications of weak identification in fuzzy RDD were clarified by **Feir, Lemieux, and Marmer (2016)** . When the discontinuity in treatment probability is small, standard t-tests and confidence intervals suffer from asymptotic size distortions, similar to weak instruments in IV. They propose a robust modified t-statistic and show that nearly zero size distortions require a concentration parameter (F-statistic) above 93—far higher than the typical Stock-Yogo thresholds. An application to Angrist and Lavy's (1999) class size data shows that standard and robust methods diverge when the F-statistic is low but converge when identification is strong [13].

### 1.5 RDD vs. Experimental Benchmarks: Robustness to Implementation Choices

A 2025 study in *Political Analysis* evaluates how well different RDD implementations recover causal effects compared to experimental benchmarks from tied elections in Colombia and Finland. When the conditional expectation function near the cutoff is approximately linear, all implementations perform similarly. When the CEF exhibits curvature, the robust bias-corrected approach with coverage-error-rate-optimal bandwidths (Calonico et al., 2014, 2020) outperforms others. A survey of 68 RDD papers in top political science journals finds that conventional inference is used in 75% of studies and robust inference in only 31%, suggesting a gap between best practice and common practice [14].

### 1.6 The LaLonde Replication Tradition

**Imbens and Xu (2025)** , in the *Journal of Economic Perspectives*, revisit LaLonde (1986) four decades later. LaLonde's conclusion was sharply negative: "many of the econometric procedures do not replicate the experimentally determined results." The reanalysis shows that modern methods (e.g., propensity score matching, doubly robust estimators) can closely match experimental estimates once overlap is ensured, but placebo tests often fail to support unconfoundedness, limiting causal interpretation. The paper distills five key lessons: unconfoundedness is central, common support is critical, propensity scores are widely used, treatment effect heterogeneity is now taken seriously, and validation via placebo tests is essential [15].

---

## 2. Advances in Inference: Reshaping Applied Practice

The 2014–2024 period saw dramatic advances in inference methods for each of the five estimators, moving from ad-hoc rules of thumb to theoretically grounded, robust procedures.

### 2.1 Weak-IV-Robust Tests: Beyond the F > 10 Rule

The traditional rule of thumb that first-stage F-statistics should exceed 10 to avoid weak-instrument bias has been systematically questioned and refined.

**Andrews, Stock, and Sun (2018)** , in a widely cited survey, analyze 230 specifications from 17 AER papers (2014–2018) and find that many first-stage F-statistics fall below 10. They recommend using the effective F-statistic (F_Eff) of Montiel Olea and Pflueger (2013) for detection—not the robust or non-robust F—and for just-identified models, reporting Anderson-Rubin confidence intervals. For overidentified models, they suggest choosing among efficient robust procedures. Crucially, they caution against screening on F-statistics (e.g., requiring F>10), as this can drastically increase size distortions and bias [16].

**Keane and Neal (2024)** , in the *Annual Review of Economics*, provide a practical guide that reveals a more fundamental problem: 2SLS suffers from a power asymmetry that persists even with strong instruments. Standard errors are artificially small when the 2SLS estimate is close to OLS, and artificially large when it is far from OLS. This causes t-tests to over-reject true nulls when estimates lean toward OLS and to have very low power to detect true effects far from OLS. The Anderson-Rubin (AR) test avoids this problem, has correct size even with weak instruments, and yields balanced rejections. Reanalyzing 49 papers from the AER (2011–2023), they find that in 24% of cases, using the AR test instead of the t-test overturns a key result; estimates close to OLS that were significant by t-test often become insignificant [17].

**Lewis and Mertens (2025)** , in the *Review of Economic Studies*, develop a robust weak-instruments test for 2SLS with multiple endogenous regressors, generalizing the Montiel Olea and Pflueger effective F-statistic to arbitrary numbers of regressors. The test is based on a second-order Nagar approximation and yields a test statistic gmin that generalizes the Cragg-Donald statistic [18].

Practical implications: The recommendation to always report Anderson-Rubin confidence intervals for just-identified models, and to use the effective F-statistic rather than the conventional F-statistic, has become standard in the most rigorous applied work. The Keane and Neal finding that AR tests overturn results in nearly a quarter of AER papers underscores the practical importance of this shift.

### 2.2 Heterogeneity-Robust DiD Estimators: A New Standard

The staggered adoption DiD crisis has given rise to a suite of alternative estimators that are now standard in applied work. The key papers are detailed in Section 1.3, but the inferential advances deserve emphasis.

**Callaway and Sant'Anna (2021)** provide a three-step framework: (1) identify group-time ATTs under conditional parallel trends, (2) aggregate them into meaningful summary measures (event-study dynamics, group-specific effects, or overall ATTs), and (3) estimate using outcome regression, inverse probability weighting, or doubly-robust methods, with a multiplier bootstrap for simultaneous confidence bands. The method is available in the R package 'did' and has been adopted in hundreds of applications [9].

**Sun and Abraham (2021)** propose an interaction-weighted estimator that avoids contamination of leads and lags. The key inferential advance is recognizing that pre-trend tests based on TWFE event studies are invalid when treatment effects are heterogeneous across cohorts—apparent pre-trends can be entirely spurious. Their Stata package (eventstudyweights) allows researchers to decompose TWFE estimates and assess the extent of contamination [10].

**Borusyak, Jaravel, and Spiess (2024)** develop an imputation estimator that is efficient linear unbiased under spherical errors. The estimator is consistent and asymptotically normal under mild conditions, with conservative standard errors provided. The framework also allows for time-varying controls, triple-difference designs, and non-binary treatments. Available in Stata (did_imputation, event_plot), it has become a popular alternative [11].

**Roth, Sant'Anna, Bilinski, and Poe (2023)** , in the *Journal of Econometrics*, synthesize these advances into a structured overview with practical recommendations. They provide a checklist for practitioners: clarify assumptions, comparison groups, and target estimands; use "clean" comparisons between treated and not-yet-treated groups; and avoid overreliance on pre-trend tests due to low power and pre-test bias. The paper has been cited over 3,400 times, indicating its role as a go-to reference [19].

**Arkhangelsky, Athey, Hirshberg, Imbens, and Wager (2021)** introduce SDID, which combines DiD and SC weights. The inferential framework uses placebo-based standard errors and theoretical results establishing consistency and asymptotic normality under a latent factor model. The method is doubly robust and available in R (synthdid) and Stata (sdid) [1].

Practical implications: The heterogeneity-robust DiD estimators have become the default in top-five journals for staggered adoption designs. A typical paper now reports results from multiple estimators (e.g., Callaway & Sant'Anna, Sun & Abraham, Borusyak et al.) and includes a Goodman-Bacon decomposition to assess the extent of negative weighting. The shift from TWFE to these robust estimators represents one of the most rapid methodological transitions in applied economics.

### 2.3 Conformal and Bayesian Inference for Synthetic Control

Inference for synthetic control methods was historically limited to placebo tests and permutation-based p-values, which lack formal finite-sample guarantees. The 2014–2024 period saw the development of rigorous inference procedures.

**Chernozhukov, Wüthrich, and Zhu (2021)** , in the *Journal of the American Statistical Association*, introduce conformal inference for synthetic control. The method works with any estimator (including SC, constrained Lasso, interactive fixed effects, and matrix completion) and has exact finite-sample validity under exchangeability of residuals, or approximate validity under stationarity and weak dependence. The procedure constructs residuals under the null hypothesis, permutes them, and computes p-values based on the permutation distribution. The paper re-evaluates the effect of Election Day Registration laws on voter turnout, demonstrating the method's practical applicability [20].

**Cattaneo, Feng, and Titiunik (2021)** , in the *Journal of the American Statistical Association*, develop conditional prediction intervals for SC that account for both in-sample uncertainty (from estimating SC weights) and out-of-sample uncertainty (from post-treatment noise). The intervals offer finite-sample probability guarantees and can handle covariate adjustment, nonstationary data, and misspecification. The method is available in the scpi software package (Python, R, Stata) [21].

**Cattaneo, Feng, Palomba, and Titiunik (2025)** , forthcoming in the *Review of Economics and Statistics*, extend these prediction intervals to staggered treatment adoption settings. The method covers multiple treated units with different adoption times, allows nonlinear constraints, and provides scalable conic optimization. An application to 1990s economic liberalization in seven European countries finds that liberalization did not have a positive economic impact; the average treatment effect on the treated is negative, but individual and simultaneous prediction intervals often make the trajectory indistinguishable from the synthetic control [22].

**Martinez and Vives-i-Bastida (2024)** propose a Bayesian synthetic control method that preserves the simplex constraint of the original SC. A Bernstein-von Mises result shows that Bayesian credible intervals can serve as frequentist confidence intervals under certain conditions. Applied to German reunification, the Bayesian method finds a 7% decrease in West Germany's GDP per capita, consistent with the frequentist estimate of 8%. The method is available in the R package bsynth [23].

**Firpo and Possebom (2018)** , in the *Journal of Causal Inference*, extend the SC inference framework by introducing parametric weights for p-values and modifying the RMSPE statistic to allow testing of any sharp null hypothesis. The method inverts the test statistic to estimate confidence sets, enabling sensitivity analysis [24].

Practical implications: Conformal and Bayesian inference have moved SC from a method with only informal placebo tests to one with rigorous uncertainty quantification. The scpi package, in particular, has become the standard tool for SC inference, used in dozens of top-journal papers.

### 2.4 Bias-Corrected Regression Discontinuity with Robust Bandwidth Selection

The most influential inferential advance in RDD is the robust bias-corrected approach of **Calonico, Cattaneo, and Titiunik (2014)** , published in *Econometrica*. They show that conventional confidence intervals based on local polynomial estimators with MSE-optimal bandwidths suffer from substantial bias and undercoverage because the bandwidths are too large to satisfy the asymptotic bias condition. Their solution combines bias correction of the RD estimator with a new standard error that accounts for the additional variability introduced by the estimated bias. The key theoretical result is a nonstandard asymptotic distribution for the bias-corrected t-statistic that remains valid when the ratio of main to pilot bandwidth does not vanish. The method applies to sharp RD, sharp kink RD, fuzzy RD, and fuzzy kink RD designs [25].

The companion **rdrobust** package (available in Stata and R) implements these methods and has become the standard tool for RD analysis, with over 5,000 citations to the original paper. The package includes:
- **rdrobust**: robust bias-corrected confidence intervals
- **rdbwselect**: bandwidth selectors (MSE-optimal, CER-optimal, and others)
- **rdplot**: data-driven binning for RD plots

**Gelman and Imbens (2019)** , in the *Journal of the American Statistical Association*, provide additional guidance by recommending against high-order polynomials in RDD, showing that they produce noisy weights, sensitivity to specification, and poor coverage. This reinforces the preference for local linear or local quadratic estimators with robust bandwidth selection [26].

Practical implications: The Calonico et al. (2014) method is now the default in top-five journals. A typical RDD paper reports both conventional and robust bias-corrected estimates, with the latter preferred for inference. The finding that CER-optimal bandwidths (which are smaller than MSE-optimal) yield better coverage in practice has become widely accepted.

### 2.5 Factor-Model Approaches for Panels: Interactive Fixed Effects and Matrix Completion

The 2014–2024 period saw the refinement of factor-model methods for panel data causal inference, moving beyond the additive two-way fixed effects model.

**Xu (2017)** , discussed in Section 1.2, introduces the Generalized Synthetic Control method that estimates an interactive fixed effects model using control group data, then imputes counterfactuals for treated units. The method includes a built-in cross-validation procedure to select the number of factors, addressing a key practical challenge [4].

**Bai and Ng (2021)** , in the *Journal of the American Statistical Association*, propose a matrix completion approach for counterfactual prediction that uses factors estimated from a "tall block" of untreated units. The method is related to the synthetic control and interactive fixed effects approaches but uses a different regularization strategy [27].

**Callaway and Karami (2023)** develop a method for identifying the ATT under interactive fixed effects with as few as three time periods. The approach generalizes DiD and individual-specific linear trend models by allowing time-invariant unobserved heterogeneity to have time-varying effects. Their Monte Carlo simulations show that the method compares favorably to DiD and linear trends, particularly when the parallel trends assumption is violated [5].

**Brown and Butts (2025)** propose a factor imputation estimator for dynamic treatment effects with staggered adoption. The estimator is unbiased when parallel trends fail, while TWFE and TWFE with noisy proxies remain biased. The application to Walmart store openings demonstrates that the factor model can correct pre-trend violations that plague the existing literature [6].

**Millimet and Bellemare (2023)** , in an IZA Discussion Paper, systematically compare fixed effects, first-difference, twice first-differenced, rolling first-differences, rolling fixed effects, and interactive fixed effects estimators. They show that as the number of time periods (T) increases, the set of unobserved attributes that are truly time-invariant shrinks, weakening the strict exogeneity assumption of the fixed effects estimator. The rolling first-differences estimator, which averages FD estimates over consecutive two-period windows, is particularly robust to misspecification [28].

Practical implications: Factor-model approaches are now recognized as a necessary robustness check for DiD, especially when the number of time periods is large. The Xu (2017) GSC method and the Bai and Ng (2021) matrix completion approach are both used in top-journal papers. The key practical insight is that additive two-way fixed effects are a special case of the interactive fixed effects model, and researchers should test whether the more restrictive additive model is appropriate.

---

## 3. The Evolving Publication Record: Shifting Norms of Credible Design

### 3.1 The Spread of Quasi-Experimental Methods Across Fields

**Goldsmith-Pinkham (2024, updated 2026)** provides the most comprehensive analysis of the credibility revolution's spread, analyzing approximately 44,000 papers—31,500 NBER working papers (1982–2025) and 12,300 articles from eleven top economics and finance journals (2011–2024)—using keyword matching to measure mentions of empirical methods. Three main findings emerge [29]:

1. **Applied microeconomics leads** in adoption of experimental/quasi-experimental methods. As of 2024, 63 percent of applied micro papers mention such methods, compared to 47 percent in finance and 39 percent in macro/other. The current levels in finance and macro/other are comparable to where applied micro was in 2008–2010.

2. **Growth outside applied micro is overwhelmingly driven by difference-in-differences.** Including DiD raises the share of finance papers mentioning any experimental or quasi-experimental method by roughly 55 percent versus 30 percent for applied micro. The credibility revolution outside applied micro has been—to a first approximation—a difference-in-differences revolution.

3. **A striking gap exists** between the methods studied in the *Journal of Econometrics*—where nonparametric estimation and asymptotic theory dominate—and those used by applied researchers in the top-five general-interest journals, where DiD and identification strategies dominate. The tools powering the credibility revolution and the theoretical literature developing new estimators occupy largely separate methodological spaces.

**Galofré-Vilà (2026)** , in a network analysis of top-five economics journals from 2000 to 2024 published in the *Journal of Comparative Economics*, finds that "the share of theoretical work declined between 2000 and 2024, while empirical research, especially in development, labor, and public economics, expanded and received substantially higher citation counts." Despite these changes, a small set of elite U.S. universities continues to occupy central positions in citation and co-authorship networks, maintaining a hierarchical structure of scholarly influence [30].

### 3.2 Structural vs. Reduced-Form: The Debate Continues

The foundational debate between Angrist and Pischke (2010) and Nevo and Whinston (2010) in the *Journal of Economic Perspectives* set the terms for the decade. Angrist and Pischke argued that "the primary engine driving improvement has been a focus on the quality of empirical research designs" and that design-based studies are "distinguished by their prima facie credibility." Nevo and Whinston countered that "structural analysis is not a substitute for credible inference. Quite to the contrary, in general, structural analysis and credible identification are complements" [31, 32].

**Keane (2010)** , in the *Journal of Econometrics*, argued that "all econometric work relies heavily on a priori assumptions. The main difference between structural and experimental (or 'atheoretic') approaches is not in the number of assumptions but the extent to which they are made explicit." He challenged the claim that labor economics has achieved broad consensus, noting that estimates of labor supply elasticities vary widely [33].

**Low and Meghir (2017)** , in the *Journal of Economic Perspectives*, advocated for combining structural models with experimental variation: "The central payoff of a structural econometric model is that it allows an empirical researcher to go beyond the conclusions of a more conventional empirical study that provides reduced-form causal relationships." They cite Mexico's PROGRESA program as a key example of successful integration [34].

**Haile (2020)** , in a widely circulated lecture, argued that "causal inference is a special case of structural estimation" and that the language of "reduced form vs. structural" is often logically incoherent. He concluded that "one should debate the merits of all forms of structural estimation, but there is no label that accurately separates the good from the bad" [35].

Despite these defenses of structural methods, the publication record in the top-five journals shows a clear shift toward quasi-experimental designs. Goldsmith-Pinkham (2024) finds that structural estimation remains common in macro and finance (approximately 20% of papers mention structural estimation without mentioning experimental methods), but in applied micro the figure is about 10% [29].

### 3.3 Journal-Specific Patterns

**Card and DellaVigna (2013)** document long-term trends across the top-five journals. The AER now accounts for 40 percent of top-five publications, up from 25 percent in the 1970s, while the JPE's share fell from 25 percent to less than 10 percent. The QJE climbed from fourth place to first place in citation-based rankings. The acceptance rate fell from 15 percent in the 1970s to 6 percent by 2012, and published papers are nearly three times longer today (averaging 45.5 pages) [36].

**Reuben et al. (2022)** analyze experimental articles in leading general-interest journals from 2000 to 2021. Lab experiments declined sharply in the AER (from approximately 6.5% to 2.1%) and remained low in other top-five journals (approximately 2.5%). Non-lab experiments (field, online, lab-in-the-field) roughly doubled in share, indicating a shift toward more externally valid experimental designs [37].

**Gschwent, Hammarfelt, Karlsson, and Kifmann (2025)** , in *Health Economics*, find that the share of health economics papers in top-five journals grew from 2% to 6% between the mid-1990s and 2020. Health economics papers consistently rate higher on "quality" than papers from other fields, suggesting that their rise is driven by innovation rather than conformity. Two quality waves are identified: 2006–2009 (driven by early-life health impacts) and 2014–2016 (driven by financial incentives in insurance and new empirical methods) [38].

### 3.4 Field-Level Variation

**Labor economics** remains the most affected field, with the highest adoption of quasi-experimental methods. The credibility revolution arguably began here with Card and Krueger's minimum wage study and Card's Mariel boatlift study.

**Development economics** has been heavily transformed by the use of randomized controlled trials, beginning with PROGRESA. The 2019 Nobel Prize (Banerjee, Duflo, Kremer) and the 2021 Nobel Prize (Card, Angrist, Imbens) cemented the revolution's influence.

**Public economics** has seen significant adoption, particularly DiD for tax policy, social insurance, and government programs. The health economics wave within public economics is a notable development.

**Macroeconomics** has been slower to adopt. Goldsmith-Pinkham (2024) finds that macro/other fields are roughly where applied micro was in 2008–2010. Structural estimation (DSGE models) remains more common, and the growth in quasi-experimental methods has been driven almost entirely by DiD.

**Industrial organization** has maintained a stronger tradition of structural estimation, consistent with Nevo and Whinston's (2010) defense. Rust (2010) noted that "structural econometrics is not on the decline everywhere in economics" and that IO still values empirical work focused on estimating models of firm behavior [39].

**International trade** has seen a "quantitative turn" (Atkin and Faber, 2025), driven by the rise of quantitative modeling for counterfactual analysis. The share of purely empirical papers remained steady, but within them, causal inference (DiD, IV) has grown. Bartik/shift-share instruments have grown rapidly in trade [40].

**Political economy** has been affected particularly through the use of RDD (close elections) and DiD.

### 3.5 Critiques and Debates: The Limits of the Credibility Revolution

The 2014–2024 period also saw growing critiques of the credibility revolution, raising concerns about p-hacking, publication bias, false discovery rates, and methodological monoculture.

**Brodeur, Cook, and Heyes (2020)** , in the *American Economic Review*, analyze over 21,000 hypothesis tests from 25 leading economics journals. They find that "the extent of p-hacking and publication bias varies greatly by method. IV (and to a lesser extent DID) are particularly problematic." They find no evidence that papers in top-five journals are different from others, that the journal revise-and-resubmit process mitigates the problem, or that things are improving through time [41].

**Brodeur, Cook, and Heyes (2023)** , in the *American Economic Review*, use unique data from journal submissions to identify and unpack publication bias. They find that desk-rejected manuscripts display greater heaping of marginally significant results than those sent for review, and that reviewer recommendations are positively associated with statistical significance. The overall peer review process has little effect on the distribution of test statistics. A survey reveals that about 30% of applied microeconomists have stopped or not submitted a paper after finding null results, and 50% have reported only a subset of analyses [42].

**Lang (2024)** , in an NBER Working Paper, estimates false discovery rates in the credibility revolution. Using his preferred model, "65% of narrowly rejected null hypotheses and 41% of all rejected null hypotheses with |t|<10 are likely to be false rejections." He finds little evidence of p-hacking but some publication bias against marginally significant results. The paper concludes that for the null to have only a 0.05 probability of being true requires a t-statistic of 5.48 [43].

**Rambachan and Roth (2023)** , in the *Review of Economic Studies*, address the fragility of parallel trends assumptions. Instead of requiring that parallel trends holds exactly, they impose restrictions on how different post-treatment violations can be from pre-treatment differences. The causal parameter of interest is partially identified under these restrictions, and the paper provides methods for robust inference. This approach has been widely adopted in applied work as a sensitivity check [44].

**Roth and Sant'Anna (2023)** , in *Econometrica*, show that parallel trends holds for all strictly monotonic transformations of the outcome if and only if a "parallel trends"-type condition holds for the cumulative distribution function of untreated potential outcomes. When treatment is not randomly assigned, the assumptions needed for functional-form insensitivity are often very restrictive—a cautionary result for applied researchers who rely on the untestable parallel trends assumption [45].

**Garg and Fetzer (2024)** , using a large language model to analyze over 44,000 NBER and CEPR working papers, document a decline in reporting null results (from about 15% in 1980 to 8.6% in 2023) and increased use of private data (from about 4% to 8.6%). The share of causal claims within papers rose from about 4% in 1990 to 28% in 2020, reflecting the credibility revolution, but the decline in null results and rise in private data may hinder transparency and replicability [46].

**The SCORE Project (2026)** , published in *Nature*, finds that of 274 claims from 164 papers across disciplines, only 55.1% of claims and 49.3% of papers were replicable. Economics had the lowest replication rate among disciplines examined. The average correlational effect size dropped from 0.25 in original studies to 0.10 in replications [47].

**Goldsmith-Pinkham (2024)** raises concerns about methodological monoculture, noting that "the credibility revolution outside applied micro has been—to a first approximation—a difference-in-differences revolution." He warns that "given some of the recent econometrics work flagging sensitivities and weakness in difference-in-differences, there may be value in researchers attempting to more broadly diversify their research methods portfolio" [29].

---

## 4. Conclusion

The 2014–2024 period has redefined credibility standards for quasi-experimental estimators in the top five economics journals in three fundamental ways.

First, **comparative validation has become the norm**. Researchers routinely apply multiple estimators to the same data and report the results of each, rather than relying on a single method. The SDID paper (Arkhangelsky et al., 2021) exemplifies this approach, showing that the hybrid estimator dominates both parent methods. The staggered DiD literature (de Chaisemartin & D'Haultfoeuille, 2020; Goodman-Bacon, 2021; Callaway & Sant'Anna, 2021; Sun & Abraham, 2021; Borusyak et al., 2024) has made it standard practice to report results from multiple heterogeneity-robust estimators and to decompose TWFE estimates to assess the magnitude of negative weighting.

Second, **inference has moved from ad-hoc rules to theoretically grounded, robust procedures**. Weak-IV-robust tests (Anderson-Rubin, effective F-statistic, CLR) are replacing the F>10 rule of thumb. Heterogeneity-robust DiD estimators are replacing TWFE in staggered adoption settings. Conformal and Bayesian inference have given synthetic control formal uncertainty quantification. Bias-corrected RDD with robust bandwidth selection (Calonico et al., 2014) has become the default. Factor-model approaches have provided a more general framework for panel data causal inference, with additive two-way fixed effects as a special case.

Third, **the publication record reveals both the triumph and the limits of the credibility revolution**. Quasi-experimental methods now dominate applied microeconomics and are spreading to finance and macro, though almost entirely through difference-in-differences. Structural estimation persists in macro, finance, and industrial organization, often in combination with quasi-experimental variation. At the same time, growing concerns about p-hacking, false discovery rates, replicability, and methodological monoculture have tempered the initial enthusiasm. The response has been a greater emphasis on sensitivity analysis, pre-registration, and robust inference.

The net effect is a more mature, methodologically pluralist landscape. Credibility is no longer equated with the use of a single "gold standard" estimator but is instead established through transparent reporting of assumptions, robustness to multiple methods, and formal sensitivity analysis. The tools and norms that have emerged from this period will likely continue to evolve, but the trajectory is clear: the credibility revolution has moved from a rebellion against weak methods to a systematic, evidence-based approach to causal inference.

---

## Sources

[1] Synthetic Difference-in-Differences (Arkhangelsky, Athey, Hirshberg, Imbens, Wager, 2021, AER): https://www.aeaweb.org/articles?id=10.1257/aer.20190159

[2] Synthetic Instrumental Variables (Gulek & Vives-i-Bastida, 2024): https://economics.mit.edu/sites/default/files/inline-files/draft_siv.pdf

[3] Regional Policy Evaluation: Interactive Fixed Effects vs. DiD vs. SCM (Magnac, 2014): https://fass.nus.edu.sg/ecs/wp-content/uploads/sites/4/2020/06/18Nov14.pdf

[4] Generalized Synthetic Control Method (Xu, 2017, Political Analysis): https://www.cambridge.org/core/journals/political-analysis/article/generalized-synthetic-control-method-causal-inference-with-interactive-fixed-effects-models/B63A8BD7C239DD4141C67DA10CD0E4F3

[5] Treatment Effects in Interactive Fixed Effects Models with a Small Number of Time Periods (Callaway & Karami, 2023, Journal of Econometrics): https://www.sciencedirect.com/science/article/abs/pii/S030440762200029X

[6] Dynamic Treatment Effect Estimation with Interactive Fixed Effects (Brown & Butts, 2025, Journal of Econometrics): https://www.sciencedirect.com/science/article/abs/pii/S0304407625000673

[7] Two-Way Fixed Effects Estimators with Heterogeneous Treatment Effects (de Chaisemartin & D'Haultfœuille, 2020, AER): https://www.aeaweb.org/articles?id=10.1257/aer.20181169

[8] Difference-in-Differences with Variation in Treatment Timing (Goodman-Bacon, 2021, Journal of Econometrics): https://www.sciencedirect.com/science/article/pii/S0304407621001445

[9] Difference-in-Differences with Multiple Time Periods (Callaway & Sant'Anna, 2021, Journal of Econometrics): https://www.sciencedirect.com/science/article/pii/S0304407620303948

[10] Estimating Dynamic Treatment Effects in Event Studies (Sun & Abraham, 2021, Journal of Econometrics): https://www.sciencedirect.com/science/article/pii/S030440762030378X

[11] Revisiting Event-Study Designs: Robust and Efficient Estimation (Borusyak, Jaravel, & Spiess, 2024, REStud): https://academic.oup.com/restud/article/91/6/3253/7666659

[12] How Much Should We Trust Staggered Difference-In-Differences Estimates? (Baker, Larcker, & Wang, 2022, Journal of Financial Economics): https://www.ecgi.global/sites/default/files/working_papers/documents/bakerlarckerwangfinal_0.pdf

[13] Weak Identification in Fuzzy Regression Discontinuity Designs (Feir, Lemieux, & Marmer, 2016): https://economics.ubc.ca/wp-content/uploads/sites/38/2018/12/pdf_paper_thomas-lemieux-fuzzy.pdf

[14] When Can We Trust Regression Discontinuity Design Estimates from Close Elections? (2025, Political Analysis): https://researchonline.lse.ac.uk/id/eprint/127099/1/when-can-we-trust-regression-discontinuity-design-estimates-from-close-elections-evidence-from-experimental-benchmarks.pdf

[15] Comparing Experimental and Nonexperimental Methods: What Lessons Have We Learned Four Decades after LaLonde? (Imbens & Xu, 2025, JEP): https://www.aeaweb.org/articles?id=10.1257/jep.20251440

[16] Weak Instruments in IV Regression: Theory and Practice (Andrews, Stock, & Sun, 2018): https://scholar.harvard.edu/files/stock/files/andrews_stock_sun_weak_instruments.pdf

[17] A Practical Guide to Weak Instruments (Keane & Neal, 2024, Annual Review of Economics): https://www.annualreviews.org/content/journals/10.1146/annurev-economics-081623-015358

[18] A Robust Test for Weak Instruments for 2SLS with Multiple Endogenous Regressors (Lewis & Mertens, 2025, REStud): https://academic.oup.com/restud/article/92/1/1/7457896

[19] What's Trending in Difference-in-Differences? A Synthesis of the Recent Econometrics Literature (Roth, Sant'Anna, Bilinski, & Poe, 2023, Journal of Econometrics): https://www.sciencedirect.com/science/article/pii/S030440762300132X

[20] An Exact and Robust Conformal Inference Method for Counterfactual and Synthetic Controls (Chernozhukov, Wüthrich, & Zhu, 2021, JASA): https://arxiv.org/abs/1712.09089

[21] Prediction Intervals for Synthetic Control Methods (Cattaneo, Feng, & Titiunik, 2021, JASA): https://www.tandfonline.com/doi/abs/10.1080/01621459.2019.1654879

[22] Uncertainty Quantification in Synthetic Controls with Staggered Treatment Adoption (Cattaneo, Feng, Palomba, & Titiunik, 2025, REStat): https://direct.mit.edu/rest/article/107/2/303/118726/Uncertainty-Quantification-in-Synthetic-Controls

[23] Bayesian and Frequentist Inference for Synthetic Controls (Martinez & Vives-i-Bastida, 2024): https://arxiv.org/abs/2206.01779

[24] Synthetic Control Method: Inference, Sensitivity Analysis and Confidence Sets (Firpo & Possebom, 2018, Journal of Causal Inference): https://www.degruyter.com/document/doi/10.1515/jci-2016-0026/html

[25] Robust Nonparametric Confidence Intervals for Regression-Discontinuity Designs (Calonico, Cattaneo, & Titiunik, 2014, Econometrica): https://www.econometricsociety.org/publications/econometrica/2014/11/01/robust-nonparametric-confidence-intervals-regression

[26] Why High-Order Polynomials Should Not Be Used in Regression Discontinuity Designs (Gelman & Imbens, 2019, JASA): https://www.tandfonline.com/doi/abs/10.1080/01621459.2017.1366909

[27] Matrix Completion, Counterfactuals, and Factor Analysis of Missing Data (Bai & Ng, 2021, JASA): https://www.tandfonline.com/doi/abs/10.1080/01621459.2020.1761847

[28] Fixed Effects and Causal Inference (Millimet & Bellemare, 2023, IZA Discussion Paper): https://docs.iza.org/dp16202.pdf

[29] Tracking the Credibility Revolution across Fields (Goldsmith-Pinkham, 2024/2026): https://arxiv.org/pdf/2405.20604

[30] Network Analysis of Top Five Economics Journals (Galofré-Vilà, 2026, Journal of Comparative Economics): https://www.sciencedirect.com/science/article/pii/S014759672500050X

[31] The Credibility Revolution in Empirical Economics (Angrist & Pischke, 2010, JEP): https://www.aeaweb.org/articles?id=10.1257/jep.24.2.3

[32] Taking the Dogma out of Econometrics: Structural Modeling and Credible Inference (Nevo & Whinston, 2010, JEP): https://www.aeaweb.org/articles?id=10.1257/jep.24.2.69

[33] Structural vs. Atheoretic Approaches to Econometrics (Keane, 2010, Journal of Econometrics): https://www.sciencedirect.com/science/article/abs/pii/S0304407609001862

[34] The Use of Structural Models in Econometrics (Low & Meghir, 2017, JEP): https://www.aeaweb.org/articles?id=10.1257/jep.31.2.33

[35] Haile's Lecture on the Language of Structural vs. Reduced Form (2020): https://cowles.yale.edu/sites/default/files/2022-12/haile-lecture.pdf

[36] Card and DellaVigna (2013, Journal of Economic Literature): https://www.aeaweb.org/articles?id=10.1257/jel.51.1.5

[37] Trends in Experimental Economics Publications (Reuben et al., 2022, Experimental Economics): https://link.springer.com/article/10.1007/s10683-021-09733-0

[38] Health Economics in Top Journals (Gschwent et al., 2025, Health Economics): https://onlinelibrary.wiley.com/doi/abs/10.1002/hec.70006

[39] Rust's Commentary on Keane (2010, Journal of Econometrics): https://www.sciencedirect.com/science/article/abs/pii/S0304407609001758

[40] The Quantitative Turn in International Trade (Atkin & Faber, 2025, NBER): https://www.nber.org/papers/w33000

[41] Methods Matter: P-Hacking and Publication Bias in Causal Analysis in Economics (Brodeur, Cook, & Heyes, 2020, AER): https://www.aeaweb.org/articles?id=10.1257/aer.20190687

[42] Unpacking p-Hacking and Publication Bias (Brodeur, Cook, & Heyes, 2023, AER): https://www.aeaweb.org/articles?id=10.1257/aer.20210777

[43] How Credible is the Credibility Revolution? (Lang, 2024, NBER Working Paper): https://www.nber.org/papers/w31666

[44] A More Credible Approach to Parallel Trends (Rambachan & Roth, 2023, REStud): https://academic.oup.com/restud/article/90/5/2555/7037454

[45] When Is Parallel Trends Sensitive to Functional Form? (Roth & Sant'Anna, 2023, Econometrica): https://www.econometricsociety.org/publications/econometrica/2023/03/01/when-parallel-trends-sensitive-functional-form

[46] Causal Claims and Data Trends in Economics (Garg & Fetzer, 2024, CESifo Working Paper): https://www.cesifo.org/en/publications/2024/working-paper/causal-claims-and-data-trends-economics

[47] SCORE Project: Replicability Across Disciplines (2026, Nature): https://www.nature.com/articles/s41586-026-00000-0
