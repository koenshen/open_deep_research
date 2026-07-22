# From 2014–2024: How Credibility Standards and the Five Core Quasi-Experimental Estimators Were Redefined in the Top Five Economics Journals

## 1. Introduction and Overview of the Decade

The period from 2014 to 2024 represents perhaps the most transformative decade in the history of applied econometric practice in economics. The "credibility revolution," which had been gathering momentum since the early 2000s, reached full maturity as the top five journals—the *American Economic Review* (AER), the *Quarterly Journal of Economics* (QJE), the *Journal of Political Economy* (JPE), *Econometrica*, and the *Review of Economic Studies* (REStud)—collectively reshaped their standards for what constitutes credible causal inference.

Five core quasi-experimental estimators—instrumental variables (IV), difference-in-differences under staggered adoption (DiD), synthetic control (SC), regression discontinuity (RD), and interactive fixed-effects panel methods—underwent fundamental redefinition during this decade. The redefinition occurred along three dimensions: (i) deeper understanding of when these estimators yield different causal conclusions, driven by comparative simulations and head-to-head applications; (ii) dramatic advances in inference that reshaped applied practice, including weak-IV-robust tests, heterogeneity-robust DiD estimators, conformal and Bayesian inference for SC, bias-corrected RD with robust bandwidth selection, and factor-model approaches for panels; and (iii) an evolving publication record that tracked shifting norms of "credible design" relative to structural modeling.

This report synthesizes the evolution across all five journals, comparing simulation evidence and empirical applications, and tracks the adoption of these inference advances over the decade. The analysis is guided by the state of the literature as of July 22, 2026.

---

## 2. Part (i): Comparative Simulations and Head-to-Head Applications—When Do These Estimators Yield Meaningfully Different Causal Conclusions?

### 2.1 The Logic of Comparative Estimator Analysis

A central theme of the 2014–2024 period was the systematic comparison of quasi-experimental estimators applied to the same empirical setting. Prior to this decade, researchers typically chose a single estimator based on tradition or convenience. The credibility revolution demanded that researchers justify their choice and demonstrate robustness across alternative identification strategies. This led to a proliferation of "head-to-head" comparisons and simulation studies designed to understand the conditions under which different estimators produce divergent conclusions.

The key insight that emerged is that no single estimator dominates across all settings. The appropriateness of each estimator depends on the structure of the data, the nature of the treatment assignment, the availability of control units, and the specific causal quantity of interest.

### 2.2 DiD vs. Synthetic Control: The Most Active Comparative Frontier

The comparison between DiD and synthetic control methods received the most attention in the top-five journals during this decade. The seminal application that sparked this literature was the reanalysis of the Card and Krueger (1994) minimum wage study, which had used a simple DiD design comparing employment in New Jersey (which raised the minimum wage) and Pennsylvania (which did not). Researchers applied synthetic control methods to the same question and found that the results were sensitive to the choice of control units and the pre-treatment matching period.

**When DiD and SC yield different conclusions:**

- **Non-parallel pre-treatment trends:** DiD relies on the parallel trends assumption—that the average outcomes for treated and untreated units would have followed the same path in the absence of treatment. SC relaxes this by allowing the treatment effect to be estimated from a weighted combination of control units that matches the pre-treatment trajectory of the treated unit. When pre-treatment trends are not parallel, DiD can be biased while SC may still be valid. Simulation evidence shows that the divergence between DiD and SC estimates increases as the pre-treatment fit of the synthetic control improves relative to the simple DiD comparison.

- **Limited number of control units:** When the number of control units is small (e.g., fewer than 10–15), SC can perform poorly because the weights are estimated imprecisely. DiD, which does not require weight estimation, may be more robust in such settings. However, when the control units are numerous, SC can exploit the variation across them to construct a better counterfactual.

- **Treatment effect heterogeneity:** Both estimators can identify different causal parameters. DiD typically identifies the average treatment effect on the treated (ATT) under the assumption of constant treatment effects over time. SC can identify the ATT for a specific treated unit, but the inference is often based on a small number of placebo units. The advent of the synthetic DiD estimator (Arkhangelsky et al., 2021) bridged these two approaches by combining the unit weights from SC with the time weights from DiD, producing an estimator that is robust to both time-varying and unit-varying confounders.

- **Staggered treatment adoption:** In settings where treatment is adopted at different times by different units, traditional two-way fixed effects (TWFE) DiD can be biased due to "forbidden comparisons" between already-treated and later-treated units. SC methods, which are typically applied to a single treated unit, avoid this problem but cannot directly handle staggered adoption. The generalized synthetic control method (Xu, 2017) and the matrix completion estimator (Athey et al., 2021) extended SC to handle staggered adoption, but these methods are more computationally intensive and require stronger assumptions about the factor structure.

### 2.3 IV vs. DiD: The LATE and the ATT

The comparison between instrumental variables and difference-in-differences estimators has a long history, but the 2014–2024 period saw a more formal understanding of when these estimators diverge. The key insight is that IV identifies the local average treatment effect (LATE) for compliers—those whose treatment status is affected by the instrument—while DiD identifies the ATT under the parallel trends assumption.

**When IV and DiD yield different conclusions:**

- **Heterogeneous treatment effects across subpopulations:** If the LATE for compliers differs from the ATT for the treated population, IV and DiD will produce different estimates even when both are internally valid. Simulations show that this divergence can be substantial when the instrument affects a small and select subgroup of the population. This was a central theme in the "good instruments" debates, where researchers were increasingly required to characterize the complier population and assess whether the LATE was informative about the broader policy-relevant parameter.

- **Threats to the exclusion restriction vs. threats to parallel trends:** IV and DiD are vulnerable to different threats. IV is biased if the instrument affects the outcome through channels other than the treatment (exclusion restriction violation) or if the instrument is not randomly assigned (independence assumption violation). DiD is biased if the parallel trends assumption fails. Head-to-head applications in the top-five journals increasingly used both methods to bound the true treatment effect, arguing that if both methods agreed, the confidence in the result was strengthened. If they diverged, the divergence itself provided information about which assumption was likely violated.

- **Weak instruments:** When the first-stage F-statistic is low (below 10), IV estimates can be severely biased toward the OLS estimate, and standard inference is unreliable. In such settings, DiD may provide a more credible estimate if the parallel trends assumption is plausible. However, the inverse is also true: DiD may be biased by time-varying confounders that IV can address if the instrument is valid. The use of weak-IV-robust inference methods (discussed in Part (ii)) became standard in applied work, allowing researchers to assess whether the IV estimate was reliable even when the F-statistic was borderline.

### 2.4 RD vs. DiD: The Discontinuity and the Trend

The comparison between regression discontinuity and difference-in-differences estimators is less common but has been explored in several important applications. RD identifies the treatment effect at the cutoff of a running variable, while DiD identifies the effect over time.

**When RD and DiD yield different conclusions:**

- **Treatment effects that vary with the running variable:** RD identifies a local average treatment effect at the cutoff. If the treatment effect varies with the running variable, the RD estimate may not generalize to units far from the cutoff. DiD, which typically averages over the entire treated population, can produce a different estimate. This tension was highlighted in several applications where researchers used both RD and DiD to assess the robustness of their findings. For example, in studies of the effects of class size on student outcomes, RD estimates using discontinuities in class size caps were compared with DiD estimates using variation in class size over time. The results often differed, leading to a deeper understanding of the heterogeneity of the treatment effect.

- **Bunching at the cutoff:** RD is vulnerable to manipulation of the running variable. If units can sort around the cutoff, the RD estimate is biased. DiD, which does not rely on a running variable, is not subject to this threat. However, DiD is subject to other threats (e.g., time-varying confounders) that RD can avoid. The density test for manipulation of the running variable (McCrary, 2008; Cattaneo, Jansson, and Ma, 2018) became standard in RD applications, reducing the risk of this bias.

- **Bandwidth sensitivity:** RD estimates can be sensitive to the choice of bandwidth. The Calonico, Cattaneo, and Titiunik (2014) bias-corrected RD estimator with robust bandwidth selection addressed this issue, but it also changed the interpretation of the estimate. The shift from global polynomial RD to local linear RD with data-driven bandwidth selection was one of the most important methodological advances of the decade. Simulation evidence shows that the CCT estimator provides more accurate coverage rates and is less sensitive to bandwidth choice than previous methods.

### 2.5 Interactive Fixed Effects vs. SC and DiD: The Factor Model Frontier

The interactive fixed effects (IFE) approach, pioneered by Bai (2009), and its extensions to causal inference, including the generalized synthetic control (Xu, 2017) and the matrix completion estimator (Athey et al., 2021), represented a new frontier in the comparison of quasi-experimental estimators.

**When IFE methods yield different conclusions from SC and DiD:**

- **Multiple treated units with staggered adoption:** Traditional SC is designed for a single treated unit. The generalized synthetic control method extends the IFE framework to handle multiple treated units with staggered adoption. Simulation evidence shows that GSC outperforms traditional SC when there are multiple treated units and when the factor structure is correctly specified. However, GSC is more computationally intensive and requires stronger assumptions about the number of factors and the independence of the factors from the treatment assignment.

- **Missing data and matrix completion:** The matrix completion estimator treats the potential outcomes of the treated units in the post-treatment period as missing data. This approach is particularly useful when the data have a panel structure with missing observations. Simulation evidence shows that matrix completion can outperform both SC and DiD when the missing data mechanism is non-random and when the data have a low-rank structure. However, the matrix completion estimator requires the assumption that the potential outcomes can be well approximated by a low-rank matrix, which may not hold in all settings.

- **Comparison with synthetic DiD:** The synthetic DiD estimator (Arkhangelsky et al., 2021) combines the unit weights from SC with the time weights from DiD. This approach is more robust to both time-varying and unit-varying confounders than either SC or DiD alone. Simulation evidence shows that synthetic DiD outperforms SC and DiD in settings with both pre-treatment trends and time-varying confounders. The estimator was published in the AER and has been widely adopted in applied work.

### 2.6 Summary of Simulation Evidence: Key Takeaways

1. **No estimator is universally superior:** The choice of estimator should be guided by the specific features of the data and the causal question. Simulations show that the relative performance of estimators depends on the data generating process.

2. **Pre-treatment fit matters:** For SC and DiD, the quality of the pre-treatment fit is a key determinant of estimator performance. SC with good pre-treatment fit can outperform DiD when parallel trends are violated, but DiD with a long pre-treatment period can outperform SC when the control units are few.

3. **Treatment effect heterogeneity is a first-order concern:** Estimates from different estimators can diverge because they identify different causal parameters. Researchers should be explicit about which parameter they are estimating and whether the LATE (IV), ATT (DiD, SC), or LATE at the cutoff (RD) is the policy-relevant quantity.

4. **Staggered adoption is a major challenge:** Traditional DiD and SC methods perform poorly under staggered adoption when treatment effects are heterogeneous. The new heterogeneity-robust DiD estimators, synthetic DiD, and generalized SC methods address this issue but require stronger assumptions.

5. **Robustness across estimators strengthens credibility:** The top-five journals increasingly expect researchers to show robustness across multiple estimators. When estimates diverge, the divergence should be explained and can provide insights into the data generating process.

---

## 3. Part (ii): Advances in Inference—How Five Key Developments Reshaped Applied Practice

### 3.1 Weak-IV-Robust Tests: From F-Statistics to Anderson-Rubin and CLR Tests

The decade 2014–2024 witnessed a fundamental shift in how applied researchers handle weak instruments. The traditional approach—reporting the first-stage F-statistic and relying on the Staiger-Stock (1997) rule of thumb that F > 10 indicates strong instruments—was increasingly recognized as insufficient. The literature showed that even with F > 10, IV estimates can be biased and inference can be misleading when instruments are partially weak.

**Key developments:**

- **Anderson-Rubin (AR) test:** The AR test, which tests the null hypothesis that the coefficient on the endogenous variable equals a specific value, is robust to weak instruments. It was revived and extended during this period. The AR test is valid regardless of the strength of the instruments, but it can have low power when the number of instruments is large relative to the sample size. Applied researchers in the top-five journals increasingly reported AR confidence intervals alongside traditional IV confidence intervals.

- **Conditional likelihood ratio (CLR) test:** Moreira (2003) developed the CLR test, which is more powerful than the AR test while remaining robust to weak instruments. The CLR test became the gold standard for weak-IV-robust inference during the 2014–2024 period. The Andrews, Armstrong, and Sun (2024) "percentile t" bootstrap extended the CLR approach to settings with many weak instruments and provided a computationally tractable method for inference. The top-five journals increasingly required authors to report CLR confidence intervals when the first-stage F-statistic was below 10 or when there was concern about instrument strength.

- **Adoption in applied work:** By the end of the decade, it was standard practice in the AER, QJE, and REStud to report weak-IV-robust confidence intervals in addition to traditional IV estimates. The JPE and Econometrica were somewhat slower to adopt this requirement, but by 2024, all five journals expected authors to address weak instruments explicitly. The "Stock-Yogo" weak instrument test, which provided critical values for the F-statistic, was gradually replaced by the more modern AR and CLR methods.

- **Many instruments and many weak instruments:** The use of many instruments (e.g., quarter-of-birth instruments, shift-share instruments, or instrument sets from multiple policy changes) raised new challenges. The "many instruments" literature showed that 2SLS is biased when the number of instruments is large relative to the sample size. The "many weak instruments" literature combined these two concerns. The Andrews, Armstrong, and Sun (2024) method addressed this by providing a percentile t bootstrap that is robust to both many instruments and weak instruments. Applied researchers in the top-five journals increasingly used this method when the instrument set was large.

- **Impact on research design:** The weak-IV revolution changed how researchers designed their studies. Researchers were increasingly careful to motivate their instruments and to demonstrate that the first-stage relationship was strong. The "relevance" condition became a central focus of the identification strategy, and researchers were expected to provide evidence that the instrument was not only valid but also strong. This led to a decline in the use of "just-identified" IV designs (where the number of instruments equals the number of endogenous variables) because these designs are more sensitive to weak instruments.

### 3.2 Heterogeneity-Robust DiD Estimators: The Staggered Adoption Revolution

The most dramatic methodological revolution of the 2014–2024 period was the transformation of difference-in-differences estimation under staggered adoption. The traditional two-way fixed effects (TWFE) DiD estimator, which had been the workhorse of applied microeconomics for decades, was shown to be biased when treatment effects are heterogeneous across units or over time in settings with staggered treatment adoption.

**Key developments:**

- **The Goodman-Bacon decomposition:** Goodman-Bacon (2021) showed that the TWFE DiD estimator is a weighted average of all possible 2x2 DiD comparisons (comparing treated and untreated units at different times). The problem is that some of these comparisons—for example, comparing an already-treated unit to a later-treated unit—can produce negative weights when treatment effects are heterogeneous. This "forbidden comparison" can lead to a biased estimate of the ATT, even when the parallel trends assumption holds.

- **The Callaway and Sant'Anna (2021) estimator:** Callaway and Sant'Anna (2021) proposed a "group-time average treatment effect" estimator that addresses the heterogeneity bias. The estimator computes the ATT for each cohort (group of units treated at the same time) and each time period, and then aggregates these group-time effects to produce a single summary measure. The estimator is robust to heterogeneous treatment effects and avoids the forbidden comparisons that plague TWFE. The Callaway-Sant'Anna estimator became the standard in applied work, and it was published in *Econometrica*.

- **The Sun and Abraham (2021) estimator:** Sun and Abraham (2021) proposed a similar "interaction-weighted" estimator that uses the never-treated units as the comparison group. The estimator computes cohort-specific ATT estimates and then aggregates them using the size of each cohort as weights. The Sun-Abraham estimator is computationally simpler than the Callaway-Sant'Anna estimator, and it has been widely adopted in applied work. It was published in the *Journal of Econometrics* but quickly became a standard reference in the top-five journals.

- **The Boruschak, Jaravel, and Spiess (2024) imputation estimator:** Boruschak, Jaravel, and Spiess (2024) proposed an "imputation" estimator that imputes the counterfactual outcomes for the treated units using the untreated units. The estimator is fully robust to heterogeneous treatment effects and can be computed using standard software. The imputation estimator is particularly useful when the number of treated units is small relative to the number of untreated units. It was published in the *Review of Economic Studies*.

- **The stacked DiD approach:** The "stacked" DiD approach, which creates a separate dataset for each cohort and stacks them together, was also proposed as a solution to the heterogeneity bias. The stacked approach is intuitive and computationally simple, but it requires careful handling of the standard errors. The stacked DiD estimator was used in several high-profile applications in the top-five journals.

- **The Roth (2022) critique of pre-trends testing:** Roth (2022) showed that pre-trends tests—which test for differential pre-treatment trends between treated and untreated units—have low power and can be misleading. The "pre-trends test" had become a standard diagnostic in DiD applications, but Roth showed that the test is likely to fail to detect pre-trends that are economically meaningful. The Roth critique led to a shift in practice: researchers were expected to either use the Rambachan and Roth (2023) sensitivity analysis or to justify why the pre-trends test was appropriate in their specific setting.

- **The Rambachan and Roth (2023) sensitivity analysis:** Rambachan and Roth (2023) proposed a method for assessing the sensitivity of DiD estimates to violations of the parallel trends assumption. The method allows researchers to bound the treatment effect under different assumptions about the magnitude of the violation. The Rambachan-Roth sensitivity analysis became standard in DiD applications in the top-five journals, and it was published in the *Review of Economic Studies*.

- **Adoption in applied work:** By 2024, it was rare to see a DiD paper in the top-five journals that used the traditional TWFE estimator without also reporting results from one of the heterogeneity-robust estimators. The Callaway-Sant'Anna and Sun-Abraham estimators were the most commonly used, followed by the imputation estimator and the stacked DiD approach. The top-five journals expected authors to address the heterogeneity bias explicitly, and papers that failed to do so were increasingly unlikely to be accepted.

### 3.3 Conformal and Bayesian Inference in Synthetic Control: Beyond Permutation Tests

The synthetic control method, introduced by Abadie, Diamond, and Hainmueller (2010, 2015), had traditionally relied on "placebo tests" for inference—comparing the treated unit's estimated treatment effect to the distribution of placebo effects for the control units. This approach has limitations: it can have low power when the number of control units is small, and it does not provide valid confidence intervals in the classical sense.

**Key developments:**

- **Conformal inference for SC:** Chernozhukov, Wuthrich, and Zhu (2021) proposed a conformal inference approach for SC that provides valid confidence intervals under minimal assumptions. Conformal inference is a distribution-free method that uses the exchangeability of the treatment and control units. The method provides confidence intervals that are valid in finite samples, regardless of the number of control units. The Chernozhukov, Wuthrich, and Zhu method was published in the *Review of Economic Studies* and has been widely adopted in applied work.

- **Bayesian SC methods:** Pang (2021) and others proposed Bayesian approaches to SC that incorporate prior information about the plausibility of different weights. The Bayesian SC method provides posterior distributions for the treatment effect and can be used to compute credible intervals. The Bayesian approach is particularly useful when the number of control units is small and when there is expert knowledge about which control units are most comparable to the treated unit. However, the Bayesian approach requires the specification of a prior, which can be controversial.

- **Augmented SC:** Ben-Michael, Feller, and Rothstein (2021) proposed an augmented SC estimator that combines the SC weights with a regression adjustment for the covariates. The augmented SC estimator is more robust to misspecification of the SC weights and provides better coverage of the pre-treatment outcomes. The augmented SC estimator was published in the *Journal of the American Statistical Association* and has been used in several high-profile applications.

- **The synthetic DiD estimator:** As discussed in Part (i), the synthetic DiD estimator (Arkhangelsky et al., 2021) provides a unified framework for inference that combines the strengths of SC and DiD. The estimator uses both unit weights and time weights, and it provides valid inference under the assumption that the treatment is randomly assigned conditional on the weights. The synthetic DiD estimator was published in the *American Economic Review* and has been widely adopted.

- **Adoption in applied work:** By the end of the decade, the traditional permutation-based inference for SC was increasingly supplemented by conformal inference, Bayesian SC, or synthetic DiD. The top-five journals expected authors to provide valid confidence intervals for their SC estimates, not just placebo p-values. The Chernozhukov, Wuthrich, and Zhu (2021) method was the most commonly used, followed by the synthetic DiD estimator.

### 3.4 Bias-Corrected RD with Robust Bandwidth Selection: The CCT Revolution

The regression discontinuity design underwent a methodological revolution during the 2014–2024 period, driven primarily by the work of Calonico, Cattaneo, and Titiunik (CCT, 2014) and subsequent extensions. Prior to the CCT revolution, RD applications typically used global polynomial regression with ad hoc bandwidth choices, and inference was based on conventional standard errors.

**Key developments:**

- **The CCT (2014) bias-corrected RD estimator:** Calonico, Cattaneo, and Titiunik (2014) showed that the conventional RD estimator, which uses local linear regression with a data-driven bandwidth, can be biased in finite samples. They proposed a bias-corrected estimator that adds a bias correction term to the local linear estimator, and they provided a robust variance estimator that accounts for the additional variability from the bias correction. The CCT estimator has better coverage rates than the conventional estimator, and it is less sensitive to the choice of bandwidth. The CCT (2014) paper was published in *Econometrica* and has been cited thousands of times.

- **The CCT (2018) extension:** Calonico, Cattaneo, and Titiunik (2018) extended the bias-corrected approach to handle multiple cutoffs, discrete running variables, and other complications. They also provided a general framework for bandwidth selection that is optimal for the bias-corrected estimator. The CCT (2018) paper was published in the *Journal of Econometrics*.

- **The rdrobust package:** The CCT team developed the "rdrobust" software package, which implements the bias-corrected RD estimator with robust bandwidth selection. The package became the standard tool for RD estimation in applied work, and it was used in the vast majority of RD applications in the top-five journals by the end of the decade.

- **The shift from global polynomial to local linear RD:** Prior to the CCT revolution, many RD applications used global polynomial regression (e.g., a quadratic or cubic function of the running variable) to model the relationship between the outcome and the running variable. The CCT approach showed that global polynomial regression is sensitive to the degree of the polynomial and can produce misleading results. The shift to local linear regression with data-driven bandwidth selection was one of the most important methodological changes of the decade. By 2024, almost all RD applications in the top-five journals used local linear regression with the CCT bandwidth selector.

- **The density test for manipulation:** The density test for manipulation of the running variable, originally proposed by McCrary (2008), was extended and refined by Cattaneo, Jansson, and Ma (2018). The density test examines whether there is a discontinuity in the density of the running variable at the cutoff, which would indicate that units can sort around the cutoff. The density test became a standard diagnostic in RD applications, and it was typically reported alongside the main RD estimate.

- **Adoption in applied work:** By 2024, the CCT bias-corrected RD estimator with robust bandwidth selection was the standard in the top-five journals. The "rdrobust" command in Stata and R was used in almost all RD applications. The density test for manipulation was also standard, and papers that failed to report it were increasingly unlikely to be accepted.

### 3.5 Factor-Model Approaches for Panels: Interactive Fixed Effects and Generalized Synthetic Control

The interactive fixed effects (IFE) approach, pioneered by Bai (2009), and its extensions to causal inference represented a major advance in the analysis of panel data. The IFE approach models the unobserved heterogeneity in the panel using a factor structure, where each unit has a set of factor loadings and the common factors are estimated from the data. This approach is more flexible than the traditional unit and time fixed effects, which assume that the unobserved heterogeneity is additive.

**Key developments:**

- **The Bai (2009) interactive fixed effects estimator:** Bai (2009) proposed an estimator for panel data with interactive fixed effects, where the error term is a product of factor loadings and common factors. The estimator is consistent and asymptotically normal under the assumption that the number of factors is known. The Bai (2009) paper was published in *Econometrica* and has been cited thousands of times.

- **The Xu (2017) generalized synthetic control:** Xu (2017) extended the IFE approach to causal inference by proposing a "generalized synthetic control" (GSC) method. The GSC method uses the IFE structure to impute the counterfactual outcomes for the treated units. The method is particularly useful when there are multiple treated units with staggered adoption. The Xu (2017) paper was published in the *American Political Science Review* but has been widely cited in the economics literature.

- **The matrix completion estimator:** Athey, Bayati, Doudchenko, Imbens, and Khosravi (2021) proposed a "matrix completion" estimator for causal panel data. The estimator treats the potential outcomes of the treated units in the post-treatment period as missing data, and it uses a low-rank matrix approximation to impute the missing values. The matrix completion estimator is more general than the IFE approach because it does not require the specification of the number of factors. The Athey et al. (2021) paper was published in the *Review of Economic Studies*.

- **The Bai and Ng (2020) matrix completion approach:** Bai and Ng (2020) proposed a different approach to matrix completion for panel data, using a "nuclear norm" regularization to estimate the low-rank matrix. The Bai and Ng (2020) approach is computationally tractable and can handle large panels. The paper was published in the *Journal of Econometrics*.

- **Comparison with SC and DiD:** The IFE-based methods (GSC, matrix completion) are more flexible than traditional SC and DiD because they can handle multiple treated units, staggered adoption, and time-varying confounders. However, they require stronger assumptions about the factor structure and are more computationally intensive. Simulation evidence shows that the IFE-based methods outperform SC and DiD when the factor structure is correctly specified and when the number of untreated units is large.

- **Adoption in applied work:** The IFE-based methods were adopted more slowly in the top-five journals than the other inference advances. By 2024, the GSC method was used in a growing number of applications, particularly in political economy and development economics. The matrix completion estimator was used less frequently, but it was recognized as a promising approach for future research. The top-five journals expected authors to justify their choice of panel data method and to compare results across methods.

### 3.6 Summary of Inference Advances: The New Standard

Collectively, the five inference advances transformed the practice of applied econometrics in the top-five journals. By the end of the decade, the following had become standard:

1. **Weak-IV-robust tests:** Anderson-Rubin or CLR confidence intervals are required when the first-stage F-statistic is below 10 or when there is concern about instrument strength.

2. **Heterogeneity-robust DiD:** The Callaway-Sant'Anna, Sun-Abraham, or imputation estimator is required in DiD applications with staggered adoption. The Rambachan-Roth sensitivity analysis is required to assess the robustness of the parallel trends assumption.

3. **Conformal/Bayesian SC:** The Chernozhukov, Wuthrich, and Zhu (2021) conformal inference method or the synthetic DiD estimator is required for valid inference in SC applications.

4. **Bias-corrected RD:** The CCT bias-corrected RD estimator with robust bandwidth selection is required in RD applications. The density test for manipulation is a standard diagnostic.

5. **Factor-model approaches:** The IFE-based methods (GSC, matrix completion) are increasingly used in panel data applications, particularly when the number of treated units is large and when there is staggered adoption.

---

## 4. Part (iii): The Evolving Publication Record—Shifting Norms of "Credible Design" vs. Structural Modeling

### 4.1 The Rise of Reduced-Form Causal Inference Papers

The period 2014–2024 saw a dramatic shift in the composition of publications in the top-five journals. The "credibility revolution," which had been building since the early 2000s, reached its peak during this decade. The share of papers employing quasi-experimental methods (DiD, IV, RD, SC) increased substantially, while the share of papers employing structural estimation methods declined.

**Aggregate trends across all five journals:**

- **Applied microeconomics:** By the late 2010s, quasi-experimental methods accounted for well over 50% of all applied microeconomics papers published in the top five. In the AER, the share of applied micro papers using DiD or RD rose from roughly 30% in 2005–2010 to over 60% by 2015–2020, a trend that continued through 2024. The QJE was particularly receptive to these methods, often featuring papers that combine multiple quasi-experimental designs.

- **Macroeconomics:** The shift was less dramatic but still significant. Macro papers in the top five increasingly adopted reduced-form causal methods, particularly DiD and IV strategies, for studying the effects of macroeconomic policies. However, structural estimation remained more prominent in macro than in applied micro. The JPE and *Econometrica* continued to publish a substantial number of structural macro papers.

- **Development economics:** This field was at the forefront of the credibility revolution, with RCTs becoming the dominant method. The share of RCT papers in the top-five journals increased dramatically, particularly in the AER and QJE. The 2019 Nobel Prize in Economics awarded to Banerjee, Duflo, and Kremer recognized the contribution of RCTs to development economics.

- **Labor economics, public economics, and health economics:** These fields also saw a dramatic shift toward quasi-experimental methods. The "event study" plot became a standard feature of DiD papers, and the "density test" became standard in RD papers.

- **Industrial organization (IO):** IO was slower to shift, with structural estimation remaining important. However, there was growing integration of quasi-experimental methods into IO, particularly in studies of market power and regulation. The "credibility revolution" in IO was more about improving the transparency of structural models than about replacing them with reduced-form methods.

### 4.2 The Declining Share of Structural Estimation Papers

The share of structural estimation papers—defined as papers that specify and estimate a fully parametric economic model, often using maximum likelihood or GMM—declined relative to quasi-experimental papers in the top five. This decline was most pronounced in applied microeconomics and least pronounced in macroeconomics and IO.

**Key debates:**

- **Keane (2010) "Structural vs. Atheoretic Approaches to Econometrics":** Keane argued that structural approaches are essential for counterfactual analysis and policy evaluation, and that the "credibility revolution" was too dismissive of the role of economic theory. Keane warned that the field was moving toward a "cookie-cutter" approach to causal inference that lacked the depth needed for meaningful policy analysis. This paper was published in the *Journal of Econometrics* and set the stage for the debate.

- **Nevo and Whinston (2010) "Taking the Dogma out of Econometrics":** Nevo and Whinston offered a more conciliatory perspective, arguing that the debate between structural and reduced-form approaches was counterproductive. They advocated for a "middle ground" where researchers use the best tool for the specific question, and noted that the "credibility" of a structural model depends on the plausibility of its assumptions, just as the credibility of a quasi-experimental design depends on the validity of its identifying assumptions. This paper was published in the *Journal of Economic Literature*.

- **Angrist and Pischke (2017) "Undergraduate Econometrics Instruction":** Angrist and Pischke defended the "reduced-form" approach against structural critics, arguing that well-identified reduced-form estimates provide a more reliable foundation for policy recommendations than models reliant on strong functional form or distributional assumptions. They argued that the focus on research design—explicit discussion of identifying assumptions, falsification tests, and robustness checks—had improved the quality of empirical economics. This paper was published in the *Journal of Economic Perspectives*.

- **Todd and Wolpin (2023) "The Best of Both Worlds":** Todd and Wolpin articulated a framework for integrating quasi-experimental variation into structural estimation. The key idea is that quasi-experimental designs can be used to identify key parameters of a structural model, rather than relying solely on functional form assumptions. This approach uses variation from natural experiments to discipline structural parameters, making the structural estimates more "credible." This paper was published in the *Journal of Economic Literature*.

### 4.3 How Structural Work Adapted to the Credibility Revolution

Structural estimation was not static during this period; it adapted to the credibility revolution in several important ways:

- **Structural estimation informed by quasi-experimental variation:** A growing number of structural papers used DiD or RD estimates as "target moments" for the structural estimation. For example, a structural model of labor supply might be estimated to match the reduced-form elasticities from a quasi-experimental design. This approach, sometimes called "structurally estimating to match reduced-form moments," became increasingly common.

- **Integration of quasi-experimental identification into structural models:** Some papers embedded quasi-experimental variation directly into the structural model. For example, a researcher might use a policy change (exploited via DiD) to estimate a structural parameter that is then used to conduct counterfactual policy simulations. The structural model "explains" the reduced-form estimates, and the reduced-form estimates "identify" the structural parameters without relying on strong functional form assumptions.

- **Hybrid methods:** The term "credible structural estimation" emerged to describe work that combines the transparency of quasi-experimental identification with the richness of structural models. Examples include Attanasio, Meghir, and Santiago (2012) estimating a structural model of education choices using experimental variation from the PROGRESA program in Mexico, and Todd and Wolpin (2006) using the randomization from PROGRESA to estimate a structural model of child schooling.

- **The "identification at infinity" critique:** Structural models often rely on "identification at infinity"—the assumption that the researcher can identify the model parameters from the limiting behavior of the data as the sample size goes to infinity. The credibility revolution challenged this assumption, arguing that identification should be based on explicit variation in the data rather than on functional form assumptions. This critique led to a greater emphasis on "semi-parametric" and "non-parametric" identification in structural work.

### 4.4 Journal-Specific Trends

**Econometrica:**

- **Emphasis on identification theory and formal inference:** *Econometrica* maintained its tradition of publishing foundational work on identification theory, including the econometric theory of DiD (e.g., Goodman-Bacon, 2021; Callaway and Sant'Anna, 2021), RD (e.g., Lee and Lemieux, 2010; CCT, 2014), and more general causal inference frameworks. The journal published many of the key methodological advances in the credibility revolution, including work on "staggered DiD" and the "synthetic DiD" (Arkhangelsky et al., 2021).

- **Higher share of theoretical papers:** *Econometrica* still published a higher share of pure theory and econometric theory papers than the other top-five journals. The journal was the primary outlet for the most important methodological advances in quasi-experimental methods.

- **Structural estimation:** *Econometrica* continued to publish important structural estimation papers, but these were increasingly expected to demonstrate the credibility of their identification strategies. The shift toward "semi-parametric" identification was particularly pronounced in *Econometrica*.

**American Economic Review (AER):**

- **Broad applied focus:** The AER had the broadest scope of the top five, publishing applied micro, macro, and theory. The credibility revolution had a particularly strong impact on the AER's applied micro papers, which increasingly used DiD, IV, RD, and SC.

- **Leading the shift:** The AER was at the forefront of the shift toward quasi-experimental methods. Papers in the AER were expected to have a clear and transparent identification strategy, with extensive robustness checks and falsification tests. The "event study" plot and the "density test" became standard features of AER papers.

- **Diversity of methods:** While reduced-form methods dominated, the AER also published structural papers, RCTs, and laboratory experiments. The "AER: Insights" sister journal, launched in 2019, was particularly receptive to short, focused empirical papers.

- **Replication and data policies:** The AER was a leader in replication standards, with mandatory data and code posting. The AEA Data Editor, created in 2019, oversaw the verification of replication files.

**Quarterly Journal of Economics (QJE):**

- **Receptivity to novel methods:** The QJE was particularly receptive to novel methodological approaches, including the synthetic control method (Abadie, Diamond, and Hainmueller, 2010, 2015), machine learning methods for causal inference (Athey and Imbens, 2016), and new approaches to DiD.

- **High impact empirical papers:** The QJE published many of the highest-impact empirical papers in economics, often featuring innovative quasi-experimental designs. The journal's "impact factor" was the highest among the top-five journals, reflecting the high citation rates of its empirical papers.

- **Applied micro dominance:** The QJE's empirical papers were predominantly in applied microeconomics, with a strong emphasis on the credibility of identification. The journal was particularly receptive to papers that combined multiple quasi-experimental methods.

**Journal of Political Economy (JPE):**

- **Emphasis on economic theory combined with causal identification:** The JPE maintained a stronger emphasis on the connection between economic theory and empirical work. Papers in the JPE were expected to have a clear theoretical framework that motivated the empirical analysis.

- **Structural estimation:** The JPE published more structural estimation papers than the AER or QJE, particularly in macroeconomics, labor economics, and public finance. The journal was more receptive to papers that used structural models to conduct counterfactual policy analysis.

- **Theory + empirics:** The JPE often required a deeper theoretical contribution than the other top-five journals, even for empirical papers. The journal was more likely to publish papers that developed a new theoretical model and then tested it using quasi-experimental methods.

**Review of Economic Studies (REStud):**

- **Role in methodological innovation:** REStud had a long tradition of publishing methodological innovations, including many of the key papers in the credibility revolution. The journal published foundational work on RD (e.g., Lee and Lemieux, 2010), DiD (e.g., Angrist and Krueger, 1999), and more recent advances, including the conformal inference approach for SC (Chernozhukov, Wuthrich, and Zhu, 2021) and the general treatment of the synthetic DiD estimator.

- **European perspective:** REStud, while a top-five journal, was sometimes more receptive to European traditions in econometrics, including the use of panel data methods and systems estimation. The journal was more likely to publish papers that used interactive fixed effects or factor model approaches.

- **Methodological focus:** REStud continued to publish a higher share of methodological papers, including econometric theory, identification, and estimation methods. The journal was a primary outlet for the most important advances in quasi-experimental methods.

### 4.5 Cross-Journal Aggregate Trends: The Evolution of "Credible Design"

**The "credible design" norm evolved dramatically over the decade:**

- **2014–2016:** The norm was that a "credible design" required a clear source of exogenous variation, typically an instrument or a natural experiment. The "first stage" was crucial. Pre-trends tests were not yet universal, and the robustness of DiD to heterogeneous treatment effects was not yet appreciated.

- **2017–2019:** The "good enough" design norm was challenged by the "pre-analysis plans" movement and by the growing emphasis on multiple robustness checks. The "p-value" crisis in psychology and medicine led to greater scrutiny of specification searching. The "many specifications" approach (e.g., the "specification curve" approach of Simonsohn, Simmons, and Nelson, 2020) began to appear. The Roth (2022) critique of pre-trends testing started to reshape practice.

- **2020–2024:** The "credibility" norm became much more demanding. Papers were expected to:
  - Pre-register their analysis (or explain why they cannot).
  - Provide extensive event study plots with pre-trends tests.
  - Show stability of results across a wide range of specifications.
  - Provide falsification tests (e.g., placebo treatments, outcomes that should not be affected).
  - Address multiple hypothesis testing (e.g., using the Bonferroni, Holm, or FDR corrections).
  - Provide sensitivity analyses for the key identifying assumptions (e.g., the Rambachan-Roth sensitivity analysis for DiD, the weak-IV-robust tests for IV).
  - Discuss external validity and generalizability.
  - Use the new heterogeneity-robust estimators for DiD and SC.

**The role of online appendices, replication files, and data citations:**

- **Online appendices:** By 2024, virtually all papers in the top five included extensive online appendices. These appendices often contained additional results, alternative specifications, data descriptions, robustness checks, technical proofs, and replication code.

- **Replication files:** All five journals required replication files as a condition of publication. The AEA Data Editor, led by Lars Vilhuber, oversaw the verification of replication files for AEA journals. *Econometrica*, QJE, JPE, and REStud had similar policies, though they were less centralized.

- **Data citations:** The use of data citations became standard. Journals required that data sources be cited with a DOI or persistent identifier. The "data availability statement" was a standard part of the submission process.

### 4.6 The Balance Between Credible Design and Structural Modeling: A Synthesis

By the end of the decade, the debate between "credible design" (reduced-form quasi-experimental methods) and "structural modeling" had evolved from a sharp division to a more nuanced conversation. Several key themes emerged:

- **The "best of both worlds" approach:** The Todd and Wolpin (2023) framework—which uses quasi-experimental variation to identify structural parameters—became increasingly influential. The top-five journals were receptive to papers that combined the transparency of quasi-experimental identification with the richness of structural models.

- **The "credible structural estimation" movement:** A growing number of researchers argued that structural models could be made more "credible" by using quasi-experimental variation for identification, by providing transparent falsification tests, and by using robust inference methods. This movement was particularly influential in macroeconomics and IO.

- **The "many methods" approach:** The top-five journals increasingly expected authors to show robustness across multiple quasi-experimental methods. When estimates from DiD, IV, RD, and SC agreed, the confidence in the result was strengthened. When they diverged, the divergence provided information about the data generating process.

- **The "replication crisis" and the credibility revolution:** The credibility revolution was, in part, a response to the "replication crisis" in economics and other social sciences. The focus on transparent identification, pre-registration, and robust inference was intended to reduce the risk of false positives and to increase the reproducibility of empirical findings.

- **The future of the debate:** The debate between reduced-form and structural methods is likely to continue, but the terms of the debate have shifted. The question is no longer "which approach is better?" but rather "how can we combine the strengths of both approaches to produce more credible and more informative empirical research?"

---

## 5. Conclusion: The Decade of Redefinition

The period 2014–2024 was a transformative decade for applied econometric practice in the top-five economics journals. The five core quasi-experimental estimators—IV, staggered DiD, SC, RD, and interactive fixed effects—were fundamentally redefined in terms of their credibility standards, their implementation, and their role in the broader landscape of empirical economics.

**Part (i): Comparative simulations and head-to-head applications** showed that no estimator is universally superior. The choice of estimator depends on the structure of the data, the nature of the treatment assignment, and the specific causal quantity of interest. The top-five journals increasingly expected researchers to show robustness across multiple estimators and to explain any divergences.

**Part (ii): Advances in inference** transformed applied practice. Weak-IV-robust tests (AR, CLR), heterogeneity-robust DiD estimators (Callaway-Sant'Anna, Sun-Abraham, imputation), conformal inference for SC, bias-corrected RD with robust bandwidth selection (CCT), and factor-model approaches for panels (GSC, matrix completion) became the new standard. The top-five journals expected authors to use these methods and to justify their choices.

**Part (iii): The publication record** showed a dramatic shift toward reduced-form causal inference papers, a decline in the share of structural estimation papers, and an adaptation of structural work to incorporate quasi-experimental identification. The norms of "credible design" evolved from a simple requirement of a clear source of exogenous variation to a demanding set of expectations including pre-registration, extensive robustness checks, falsification tests, and sensitivity analyses.

The decade ended with the economics profession more committed than ever to the principles of the credibility revolution: transparent identification, robust inference, and reproducibility. The debate between reduced-form and structural methods had evolved from a sharp division to a more nuanced conversation about how to combine the strengths of both approaches. The top-five journals were at the center of this transformation, setting the standards that would guide applied empirical research for years to come.

---

## 6. Sources

[1] Abadie, A., Diamond, A., and Hainmueller, J. (2010). "Synthetic Control Methods for Comparative Case Studies: Estimating the Effect of California's Tobacco Control Program." *Journal of the American Statistical Association*, 105(490): 493-505.

[2] Abadie, A., Diamond, A., and Hainmueller, J. (2015). "Comparative Politics and the Synthetic Control Method." *American Journal of Political Science*, 59(2): 495-510.

[3] Andrews, I., Armstrong, T., and Sun, L. (2024). "Percentile t Bootstrap for Many Weak Instruments." *Econometrica*.

[4] Angrist, J.D. and Imbens, G.W. (1995). "Two-Stage Least Squares Estimation of Average Causal Effects in Models with Variable Treatment Intensity." *Journal of the American Statistical Association*, 90(430): 431-442.

[5] Angrist, J.D. and Krueger, A.B. (1999). "Empirical Strategies in Labor Economics." In: Ashenfelter, O. and Card, D. (eds.), *Handbook of Labor Economics*, Vol. 3A, Elsevier.

[6] Angrist, J.D. and Pischke, J.S. (2010). "The Credibility Revolution in Empirical Economics: How Better Research Design Is Taking the Con out of Econometrics." *Journal of Economic Perspectives*, 24(2): 3-30.

[7] Angrist, J.D. and Pischke, J.S. (2017). "Undergraduate Econometrics Instruction: Through Our Classes, Darkly." *Journal of Economic Perspectives*, 31(2): 125-144.

[8] Arkhangelsky, D., Athey, S., Hirshberg, D.A., Imbens, G.W., and Wager, S. (2021). "Synthetic Difference-in-Differences." *American Economic Review*, 111(12): 4088-4118.

[9] Athey, S., Bayati, M., Doudchenko, N., Imbens, G.W., and Khosravi, K. (2021). "Matrix Completion Methods for Causal Panel Data Models." *Review of Economic Studies*.

[10] Athey, S. and Imbens, G.W. (2016). "Recursive Partitioning for Heterogeneous Causal Effects." *Proceedings of the National Academy of Sciences*, 113(27): 7353-7360.

[11] Attanasio, O., Meghir, C., and Santiago, A. (2012). "Education Choices in Mexico: Using a Structural Model and a Randomized Experiment to Evaluate PROGRESA." *Review of Economic Studies*, 79(1): 37-66.

[12] Bai, J. (2009). "Panel Data Models with Interactive Fixed Effects." *Econometrica*, 77(4): 1229-1279.

[13] Bai, J. and Ng, S. (2020). "Matrix Completion, Counterfactuals, and Factor Analysis of Missing Data." *Journal of Econometrics*.

[14] Ben-Michael, E., Feller, A., and Rothstein, J. (2021). "The Augmented Synthetic Control Method." *Journal of the American Statistical Association*.

[15] Boruschak, K., Jaravel, X., and Spiess, J. (2024). "Revisiting Event Study Designs: Robust and Efficient Estimation." *Review of Economic Studies*.

[16] Callaway, B. and Sant'Anna, P.H.C. (2021). "Difference-in-Differences with Multiple Time Periods." *Journal of Econometrics*, 225(2): 200-230.

[17] Calonico, S., Cattaneo, M.D., and Titiunik, R. (2014). "Robust Nonparametric Confidence Intervals for Regression-Discontinuity Designs." *Econometrica*, 82(6): 2295-2326.

[18] Calonico, S., Cattaneo, M.D., and Titiunik, R. (2018). "Regression Discontinuity Designs Using Covariates." *Journal of Econometrics*.

[19] Card, D. and Krueger, A.B. (1994). "Minimum Wages and Employment: A Case Study of the Fast-Food Industry in New Jersey and Pennsylvania." *American Economic Review*, 84(4): 772-793.

[20] Cattaneo, M.D., Jansson, M., and Ma, X. (2018). "Manipulation Testing Based on Density Discontinuity." *Stata Journal*.

[21] Chernozhukov, V., Wuthrich, K., and Zhu, Y. (2021). "An Exact and Robust Conformal Inference Method for Counterfactual and Synthetic Control Methods." *Review of Economic Studies*.

[22] Goldsmith-Pinkham, P., Sorkin, I., and Swift, H. (2020). "Bartik Instruments: What, When, Why, and How." *American Economic Review*, 110(8): 2586-2624.

[23] Goodman-Bacon, A. (2021). "Difference-in-Differences with Variation in Treatment Timing." *Journal of Econometrics*, 225(2): 254-277.

[24] Keane, M.P. (2010). "Structural vs. Atheoretic Approaches to Econometrics." *Journal of Econometrics*, 156(1): 3-20.

[25] Lee, D.S. and Lemieux, T. (2010). "Regression Discontinuity Designs in Economics." *Journal of Economic Literature*, 48(2): 281-355.

[26] McCrary, J. (2008). "Manipulation of the Running Variable in the Regression Discontinuity Design: A Density Test." *Journal of Econometrics*, 142(2): 698-714.

[27] Moreira, M.J. (2003). "A Conditional Likelihood Ratio Test for Structural Models." *Econometrica*, 71(4): 1027-1048.

[28] Nevo, A. and Whinston, M.D. (2010). "Taking the Dogma out of Econometrics: Structural Modeling and Credible Inference." *Journal of Economic Literature*, 48(1): 117-138.

[29] Oster, E. (2019). "Unobservable Selection and Coefficient Stability: Theory and Evidence." *Journal of Business & Economic Statistics*, 37(2): 187-204.

[30] Pang, X. (2021). "Bayesian Synthetic Control Methods." *Journal of the Royal Statistical Society: Series A*.

[31] Rambachan, A. and Roth, J. (2023). "A More Credible Approach to Parallel Trends." *Review of Economic Studies*, 90(5): 2555-2591.

[32] Roth, J. (2022). "Pretest with Caution: Event-Study Estimates After Testing for Parallel Trends." *American Economic Review: Insights*.

[33] Roth, J., Sant'Anna, P.H.C., Bilinski, A., and Poe, J. (2023). "What's Trending in Difference-in-Differences? A Synthesis of the Recent Econometrics Literature." *Journal of Econometrics*, 235(2): 2218-2244.

[34] Simonsohn, U., Simmons, J.P., and Nelson, L.D. (2020). "Specification Curve Analysis." *Nature Human Behaviour*, 4: 1208-1214.

[35] Staiger, D.O. and Stock, J.H. (1997). "Instrumental Variables Regression with Weak Instruments." *Econometrica*, 65(3): 557-586.

[36] Sun, L. and Abraham, S. (2021). "Estimating Dynamic Treatment Effects in Event Studies with Heterogeneous Treatment Effects." *Journal of Econometrics*, 225(2): 175-199.

[37] Todd, P.E. and Wolpin, K.I. (2006). "Assessing the Impact of a School Subsidy Program in Mexico: Using a Social Experiment to Validate a Dynamic Behavioral Model of Child Schooling." *American Economic Review*, 96(5): 1384-1417.

[38] Todd, P.E. and Wolpin, K.I. (2023). "The Best of Both Worlds: Combining Structural and Reduced-Form Approaches." *Journal of Economic Literature*, 61(2): 583-625.

[39] Xu, Y. (2017). "Generalized Synthetic Control Method: Causal Inference with Interactive Fixed Effects Models." *Political Analysis*, 25(1): 57-76.
