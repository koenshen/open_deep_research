# How to Design a Standardized, Multi-Dimensional Evaluation Framework for Quantitative Trading Strategies

## Introduction

The lack of a single standardized benchmark for evaluating diverse quantitative trading strategies—ranging from multi-factor and high-frequency to statistical arbitrage and machine learning–based approaches—presents a fundamental challenge in quantitative finance. Traditional performance metrics like the Sharpe ratio, while useful, capture only one dimension of performance and can be misleading when applied to strategies with non-normal return distributions, tail risk, or regime-dependent behavior. The 2008 financial crisis, for instance, demonstrated that risk models calibrated to calm conditions dramatically underestimated losses during stress periods [1].

To address this, I propose a rigorous yet flexible evaluation framework that assesses strategies across three core dimensions—returns, risk, and adaptability—while remaining open to additional metrics such as liquidity, scalability, and interpretability. The framework integrates established risk-adjusted performance ratios, advanced risk measurement techniques, market regime detection, transaction cost and capacity modeling, and multi-criteria decision analysis (MCDA) to produce a composite, reproducible score. Crucially, it incorporates corrections for backtest overfitting and multiple testing, ensuring that the selected strategy is not a statistical fluke. This report details each component and provides a step-by-step reproducible methodology.

---

## 1. Core Dimension 1: Returns – Risk-Adjusted Performance Ratios

No single ratio captures all dimensions of return. The most robust strategy passes multiple filters. The following ratios are recommended, each with specific strengths and limitations.

### 1.1 Sharpe Ratio (Sharpe 1966, 1994)

The Sharpe ratio measures excess return per unit of total risk: \( S = (R_p - R_f) / \sigma_p \). It is the industry’s default yardstick due to its simplicity and universality [2][3]. However, it assumes normally distributed returns, treats upside and downside volatility equally, and can be gamed via options or leverage [4][5]. In practice, a Sharpe ratio above 1.0 is considered good, above 2.0 excellent, and above 3.0 exceptional. The S&P 500 long-run Sharpe ratio is approximately 0.4–0.6 [2].

### 1.2 Sortino Ratio (Sortino & van der Meer 1991)

The Sortino ratio replaces standard deviation with downside deviation, focusing only on downside risk: \( \text{Sortino} = (R_p - R_f) / \text{DD} \). It is more meaningful for strategies with asymmetric returns, such as trend-following or options overlays [6][7]. A Sortino ratio of 1.0 or above is solid; above 3.0 is exceptional. The difference between the Sharpe and Sortino ratios (the Sharpe–Sortino gap) quickly indicates skew: if the Sortino is much higher than the Sharpe, the strategy has positive skew [8].

### 1.3 Calmar Ratio (Young 1991)

The Calmar ratio measures annualized return relative to maximum drawdown: \( \text{Calmar} = \text{CAGR} / |\text{Maximum Drawdown}| \). It captures the specific danger of a catastrophic drawdown, which is critical for retirement portfolios, hedge funds, and CTAs [9][10]. A Calmar ratio above 1.0 is good, above 3.0 excellent, and above 5.0 exceptional. However, it is dominated by a single data point (the maximum drawdown) and is sensitive to the evaluation period [11].

### 1.4 Omega Ratio (Keating & Shadwick 2002)

The Omega ratio captures the entire distribution of returns—not just mean and variance—by defining the probability-weighted ratio of gains to losses relative to a threshold: \( \Omega(\theta) = \int_{\theta}^{\infty} [1-F(r)] dr / \int_{-\infty}^{\theta} F(r) dr \). It is valid for non-normal, asymmetric, and fat-tailed returns, making it particularly useful for hedge funds and options strategies [12][13]. An Omega ratio above 1.0 indicates a favorable risk-return profile.

### 1.5 Information Ratio

The Information Ratio measures excess return over a benchmark per unit of tracking error: \( \text{IR} = (R_p - R_b) / \text{Tracking Error} \). It is the standard metric for active management evaluation [14]. An IR above 0.5 is good, above 0.75 very good, and above 1.0 exceptional. The Fundamental Law of Active Management decomposes IR into skill (IC) and breadth (BR): \( \text{IR} \approx \text{IC} \times \sqrt{\text{BR}} \) [15].

### 1.6 Treynor Ratio and M²

The Treynor ratio measures excess return per unit of systematic risk (beta), making it suitable for well-diversified portfolios [16]. The Modigliani-Modigliani (M²) measure expresses risk-adjusted performance as a percentage return, making it intuitive: \( M² = S \times \sigma_B + \overline{R_f} \) [17].

### 1.7 Recommendations for a Multi-Dimensional Return Assessment

- **Use multiple metrics, not one.** A common hurdle is: Sharpe >1.0, Sortino >1.5, Calmar >0.8, SQN >2.0, K-Ratio >1.5 [18].
- **Cross-reference ratios for red flags.** A high Sharpe but mediocre Sortino suggests vulnerability to severe drawdowns. A high Sharpe but low Calmar indicates hidden drawdown risk [8].
- **Consider the strategy type.** For asymmetric returns, favor Sortino and Omega. For catastrophic loss concerns, emphasize Calmar. For active management, rely on Information Ratio.

---

## 2. Core Dimension 2: Risk – Comprehensive Risk Measurement

Beyond simple volatility, the framework must incorporate drawdown analysis, downside risk, tail risk, autocorrelation, and stress testing.

### 2.1 Maximum Drawdown and Drawdown-Based Metrics

- **Maximum Drawdown (MDD):** The worst peak-to-trough decline. A 50% drawdown requires a 100% gain to recover [19].
- **Ulcer Index (UI):** Measures the depth and duration of drawdowns: \( \text{UI} = \sqrt{\Sigma(\text{Percentage Drawdown}^2) / N} \). Excellent <3, good 3–7, average 7–14, poor >14 [20].
- **Conditional Drawdown at Risk (CDaR):** Averages the worst drawdowns, analogous to CVaR [21].

### 2.2 Downside Volatility and Semi-Deviation

Semi-deviation measures only negative returns relative to a benchmark. The Sortino ratio uses downside deviation, which specifies a minimum acceptable return (MAR) [22]. Even Markowitz stated that "semivariance is the more plausible measure of risk" [23]. In practice, realized semivariance from high-frequency data has stronger predictive power for future volatility than standard realized variance [24].

### 2.3 Value at Risk (VaR) and Conditional VaR (Expected Shortfall)

- **VaR:** Maximum loss at a given confidence level (e.g., 99% VaR). Three calculation methods: parametric (normal distribution), historical simulation, and Monte Carlo [25].
- **CVaR (Expected Shortfall):** The average loss beyond VaR. It satisfies all four properties of a coherent risk measure (monotonicity, translation invariance, positive homogeneity, subadditivity) [26]. Under Basel III, CVaR at 97.5% confidence replaced VaR as the market risk capital standard [27].
- **EVT-based VaR/ES:** Extreme Value Theory (EVT) provides significantly more accurate tail estimates. For S&P 500 data, at 99.9% confidence, EVT VaR = 5.6% vs. normal 3.1% (+81%) [28].

### 2.4 Autocorrelation and Serial Dependence

Autocorrelation of returns can inflate Sharpe ratios. Lo (2002) showed that positive serial correlation can grossly exaggerate risk-adjusted performance [29]. The framework should compute the autocorrelation function (ACF) of returns and squared returns. For daily stock returns, first-order autocorrelation of returns is near zero, but squared returns show significant positive autocorrelation (volatility clustering) [30].

### 2.5 Stress Testing and Scenario Analysis

Regime-aware risk estimation involves estimating separate parameters for each regime and blending them by probability [1]. Stress tests should include historical crises (e.g., 2008, COVID-19), hypothetical scenarios (e.g., interest rate spike, liquidity freeze), and transition periods between regimes. A prescribed stress scenario from the Basel Committee includes credit rating downgrades, deposit runs, and loss of wholesale funding [31].

---

## 3. Core Dimension 3: Adaptability – Regime Detection, Transaction Costs, and Capacity

A strategy that performs well in one regime may fail in another. The framework must evaluate adaptability to changing market conditions, transaction costs, and capacity constraints.

### 3.1 Market Regime Detection

#### 3.1.1 Hidden Markov Models (HMM)

HMMs treat market conditions as latent states (e.g., bull, bear, high/low volatility) and observed returns as emissions. The Baum-Welch algorithm estimates transition probabilities, and the Viterbi algorithm decodes the most likely state sequence [32]. A study using HMM on SPY weekly returns and volatility identified two regimes (risk-on and risk-off) and improved the Sharpe ratio from 0.37 to 0.48 while reducing max drawdown from 56% to 24% [33].

#### 3.1.2 Markov Switching Models (Hamilton 1989)

Hamilton’s Markov switching model allows parameters (mean, variance) to change according to a latent Markov chain. The expected duration of each regime is \( 1/(1-p_{ii}) \) [34]. Extensions include time-varying transition probabilities and multivariate settings [35].

#### 3.1.3 Clustering-Based Approaches

- **Gaussian Mixture Models (GMM):** Two Sigma’s research applied GMM to 17 factors and identified four regimes: Crisis, Steady State, Inflation, and Walking on Ice [36].
- **K-Means and Wasserstein Distance:** Clustering distributions of time series segments can detect changes in mean, variance, and correlation [37].

#### 3.1.4 Practical Regime-Aware Evaluation

The evaluation standard is not classification accuracy but whether regime detection helps the strategy make more money. Key metrics include net value-add after switching costs [38]. The framework should report performance in each identified regime (e.g., momentum strategies in trending vs. mean-reverting regimes).

### 3.2 Transaction Cost Modeling

#### 3.2.1 Almgren-Chriss Market Impact Model

The Almgren-Chriss framework models optimal execution by balancing market impact and price risk. Permanent impact shifts the price by \( \gamma v_t dt \), and temporary impact adds slippage \( \eta v_t \). The optimal inventory trajectory solves a linear ODE, yielding a closed-form solution for risk-averse traders [39][40]. Empirical calibrations show permanent impact exponent α ≈ 1 (linear) and temporary impact exponent β ≈ 0.6 (rejecting square-root) [41].

#### 3.2.2 Implementation Shortfall (Perold 1988)

Implementation shortfall is the most comprehensive transaction cost framework, capturing explicit costs (commissions, fees) and implicit costs (bid-ask spread, market impact, delay, opportunity cost). The Plexus Group found that delay accounted for 84 of 153 total basis points of institutional equity costs—more than four times commissions [42].

#### 3.2.3 Frazzini, Israel, Moskowitz (2012/2017) Study

Using $1.7 trillion in live trades from AQR, the study found that real trading costs are an order of magnitude smaller than previous estimates. Average market impact is just under 9 basis points, with ~85% permanent. Break-even fund sizes for long-short factors are vast: $275 billion for SMB, $214 billion for HML, $56 billion for UMD in the U.S. alone [43][44]. This has profound implications for strategy capacity.

### 3.3 Capacity Estimation

Capacity is the maximum capital a strategy can absorb before performance degrades. The Landier, Simon, and Thesmar (2015) framework provides a closed-form performance-to-scale frontier: \( \text{Vol} = \frac{2SR}{\lambda \phi^2} \left( \left( \frac{SR^*}{SR} \right)^{2/3} - 1 \right)^2 \), where \( SR^* \) is the frictionless Sharpe ratio, \( \lambda \) is liquidity, and \( \phi \) is signal persistence [45]. For a 30% Sharpe reduction, capacity is \( SR^* / (10 \lambda \phi^2) \). Quality-based strategies have order-of-magnitude larger capacity than value or momentum.

The framework should estimate capacity by simulating strategy performance at increasing AUM levels, incorporating market impact models. High-frequency strategies may cap at ~$20 million, while systematic macro trend-following can absorb billions [46].

### 3.4 Walk-Forward Analysis and Cross-Validation

Walk-forward analysis is the gold standard for validating strategy robustness. It repeatedly optimizes on an in-sample window and tests on a subsequent out-of-sample window, producing multiple out-of-sample performance results [47].

- **Window Types:** Anchored (expanding) for stable relationships; rolling (fixed-length) for non-stationary markets [48].
- **Key Metrics:** Walk-forward efficiency ratio (OOS return / IS return) >0.5 acceptable, >0.7 strong; OOS win rate >60%; OOS profit factor >1.2; OOS Sharpe ratio >0.8 [49].
- **Purging and Embargo:** To prevent data leakage, purge training observations whose labels overlap the test period, and impose an embargo period after the test set [50].

**Combinatorial Purged Cross-Validation (CPCV):** An advanced method that evaluates all combinations of training/test splits, yielding a distribution of performance metrics. For N=6 groups, k=2 test folds, there are 15 folds and 5 paths [51].

---

## 4. Multi-Criteria Decision Analysis (MCDA) for Aggregation

MCDA provides a structured approach to combine multiple, often conflicting, criteria into a single evaluation score. The framework should use a hybrid MCDA approach that is transparent, reproducible, and flexible.

### 4.1 Selecting and Weighting Criteria

Criteria should be grouped into dimensions:
- **Returns:** Annualized return, Sharpe ratio (or Deflated Sharpe), Sortino ratio, Calmar ratio, Omega ratio
- **Risk:** Maximum drawdown, Ulcer Index, CVaR (95%), EVT-adjusted VaR, autocorrelation of returns
- **Adaptability:** Walk-forward efficiency ratio, regime-specific Sharpe ratios, capacity ceiling, transaction cost drag
- **Liquidity:** Amihud illiquidity ratio, bid-ask spread, market impact cost at capacity
- **Interpretability:** SHAP feature importance, partial dependence plots, model complexity

**Weighting via Analytic Hierarchy Process (AHP):** AHP uses pairwise comparisons from expert judgment to derive weights. A study on portfolio performance gave highest preference to return measures (39.7%), followed by risk (25.7%), stability (23.4%), and predictability (11.2%) [52]. For a more objective approach, the entropy weight method or CRITIC can be used [53].

### 4.2 Normalization

Metrics must be normalized to a common scale before aggregation:
- **Min-Max:** Rescales to [0,1]; sensitive to outliers.
- **Z-Score:** Standardizes to mean 0, std 1; robust to outliers.
- **Rank-Based:** Maps to uniform distribution; for non-parametric comparisons.
- **Winsorization:** Clips extreme values to reduce outlier impact.

For financial metrics, z-score normalization is generally preferred because it maintains distribution shape and is less affected by outliers [54].

### 4.3 Aggregation Methods

#### 4.3.1 Weighted Sum Model (WSM)

Composite Score = Σ w_i × Normalized Metric_i. Simple and transparent, but assumes full compensation (poor performance on one criterion can be offset by good performance on another). Sensitive to weight choices [55].

#### 4.3.2 TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)

TOPSIS identifies the ideal solution (best on each criterion) and anti-ideal solution (worst on each), then ranks alternatives by their relative closeness to the ideal. It is robust and widely used in financial evaluation [56]. A combined AHP-TOPSIS approach has been successfully applied to stock portfolio selection [57].

#### 4.3.3 PROMETHEE and ELECTRE

These outranking methods handle non-compensatory preferences, where a poor performance on a critical criterion cannot be fully offset by good performance on others. PROMETHEE II provides a complete ranking, while ELECTRE III is suitable for uncertain, imprecise data [58][59]. A combined AHP-PROMETHEE approach for portfolio performance comparison found that the minimax portfolio performed best [52].

#### 4.3.4 Data Envelopment Analysis (DEA)

DEA is a non-parametric method that evaluates the relative efficiency of strategies (decision-making units) by comparing inputs (e.g., risk, capital, costs) to outputs (e.g., return, Sharpe ratio). It identifies the efficient frontier without requiring pre-specified weights [60]. A hybrid DEA–integrated system modeling approach has been used to evaluate short-term HFT, cross-market arbitrage, and long-term value strategies [61].

#### 4.3.5 Fuzzy MCDA

Fuzzy MCDA methods (e.g., fuzzy AHP, fuzzy TOPSIS) handle uncertainty and vagueness in financial data. They convert linguistic assessments into fuzzy numbers, capturing expert hesitation [62]. An interval-valued picture fuzzy MARCOS method was developed for financial risk management, incorporating market risk and return on investment [63].

### 4.4 Recommended Hybrid Approach

A practical hybrid approach:
1. **Define criteria** and normalize using z-score.
2. **Derive weights** using AHP (expert judgment) and cross-validate with entropy method.
3. **Apply TOPSIS** to rank strategies, as it provides a clear geometric interpretation.
4. **Conduct sensitivity analysis** on weights to ensure robustness.
5. **Use PROMETHEE or ELECTRE** as a secondary check for non-compensatory preferences.

---

## 5. Addressing Overfitting and Multiple Testing

The most critical issue in quantitative strategy evaluation is backtest overfitting. The framework must incorporate formal corrections.

### 5.1 Deflated Sharpe Ratio (DSR)

The DSR, introduced by Bailey and López de Prado (2014), adjusts the Sharpe ratio for selection bias (multiple testing) and non-normality of returns. The formula is:

\[
\text{DSR} = \Phi\left( \frac{\widehat{SR} - SR_0}{\sqrt{\frac{1 - \hat{\gamma}_3 \widehat{SR} + \frac{\hat{\gamma}_4 - 1}{4} \widehat{SR}^2}{T-1}}} \right)
\]

where \( SR_0 = E[\max\{\widehat{SR}\}] \) under the null hypothesis [64]. After only 1,000 independent backtests, the expected maximum Sharpe ratio can be 3.26 even if the true Sharpe is zero [65]. A DSR above 0.95 indicates that the best observed Sharpe likely reflects genuine skill.

### 5.2 Probability of Backtest Overfitting (PBO)

The PBO framework, using Combinatorially Symmetric Cross-Validation (CSCV), estimates the probability that the best in-sample strategy underperforms the median out-of-sample. The method divides data into S subsamples, trains on half, tests on the other, and computes the relative rank of the in-sample optimal strategy across all combinations. A PBO above 0.50 indicates more-likely-than-not overfitting [66].

### 5.3 Minimum Track Record Length

The DSR can also be inverted to determine the minimum track record length (in years) needed to have confidence that the observed Sharpe is not due to luck. For a strategy with an annualized Sharpe of 1.0, skewness -1, and kurtosis 5, the required sample length is about 5 years [67].

### 5.4 The False Strategy Theorem

The theorem states that with enough trials, any Sharpe ratio threshold can be exceeded by chance. Even as few as three independent trials can produce a likely false strategy [68]. Therefore, the framework must report the number of trials (backtests) conducted and apply the DSR or PBO correction.

---

## 6. A Concrete Reproducible Methodology

Below is a step-by-step methodology that any researcher or practitioner can implement using open-source tools.

### Step 1: Data Preparation and Backtesting
- Use point-in-time data with survivorship bias removed (e.g., from CRSP, Compustat, or open-source datasets).
- Implement the strategy in an event-driven backtesting framework (e.g., LEAN [69], backtrader [70], or Zipline [71]).
- Include transaction costs using the Almgren-Chriss model or the Frazzini-Israel-Moskowitz empirical estimates.
- Record all backtest outcomes: daily returns, Sharpe ratio, Sortino ratio, Calmar ratio, Omega ratio, maximum drawdown, Ulcer Index, VaR, CVaR, autocorrelation of returns, and walk-forward efficiency ratio.

### Step 2: Walk-Forward Validation
- Use a rolling window of 3 years in-sample, 1 year out-of-sample (for daily strategies).
- Implement purging and embargo to prevent data leakage (use `purgedcv` library [72] or `skfolio`’s `CombinatorialPurgedCV` [73]).
- Compute the walk-forward efficiency ratio, OOS win rate, and OOS Sharpe ratio.
- If using CPCV, generate a distribution of OOS performance metrics.

### Step 3: Regime Classification
- Apply a Hidden Markov Model (2–4 states) or Gaussian Mixture Model to classify market regimes based on returns and volatility.
- Compute strategy performance in each regime. Report the Sharpe ratio in the most adverse regime (e.g., crisis or high-volatility regime).
- Use regime-aware risk estimation: blend risk parameters across regimes by probability [1].

### Step 4: Capacity Estimation
- Simulate the strategy at increasing AUM levels (e.g., $10M, $50M, $100M, $500M, $1B).
- Use the Almgren-Chriss market impact model with parameters calibrated to the strategy’s asset universe.
- Estimate the break-even AUM (where net returns drop to zero after costs) and the 30% degradation AUM using the Landier et al. formula [45].
- Report the capacity ceiling as a key metric.

### Step 5: Multiple Testing Correction
- Record the total number of backtests (parameter combinations) \( N \) that led to the selected strategy.
- Compute the Deflated Sharpe Ratio using the `pyfolio` or `purgedcv` library.
- Compute the Probability of Backtest Overfitting using CSCV (available in `purgedcv`).
- If DSR < 0.95 or PBO > 0.50, reject the strategy as likely overfit.

### Step 6: Multi-Criteria Aggregation
- Normalize all metrics using z-score based on the sample of all candidate strategies.
- Derive weights using AHP (e.g., using the `pyDecision` library [74]).
- Apply TOPSIS to rank strategies. The positive ideal solution is the best observed value on each metric; the negative ideal is the worst.
- Perform sensitivity analysis by varying weights ±20% and checking if top-ranked strategies remain stable.
- Optionally, apply PROMETHEE II or ELECTRE III as a robustness check.

### Step 7: Interpretability Check
- For ML-based strategies, compute SHAP values to explain predictions. Use the `shap` library [75].
- Generate partial dependence plots (PDP) for the most important features.
- Report the model complexity (e.g., number of parameters, depth of tree, number of features) and flag any black-box components that may hinder auditability.

### Step 8: Final Report
- Present a summary table with all metrics for the top strategies, including the DSR and PBO.
- Include a radar chart (spider plot) comparing the top strategy against the benchmark (e.g., S&P 500) on key dimensions.
- Document the evaluation environment, data sources, and parameter choices to ensure reproducibility.

### Open-Source Implementation Ecosystem

| Library | Purpose |
|---------|---------|
| LEAN (QuantConnect) | Event-driven backtesting, multi-asset, slippage models |
| pyfolio-reloaded | Performance and risk analysis tear sheets |
| quantstats | Portfolio profiling, HTML reports |
| alphalens | Factor performance analysis |
| backtrader | Walk-forward optimization, live trading |
| purgedcv | Purged cross-validation, DSR, PBO |
| skfolio | CombinatorialPurgedCV, portfolio optimization |
| pyDecision | 70+ MCDA methods (AHP, TOPSIS, PROMETHEE, ELECTRE) |
| shap | SHAP for model interpretability |
| scikit-learn | Gaussian Mixture Models, PCA, K-Means |

---

## 7. Flexibility to Accommodate Additional Metrics

The framework is designed to be extended. For example:

- **Liquidity:** Add the Amihud illiquidity ratio and bid-ask spread as criteria. Use the Almgren-Chriss model to quantify market impact at the strategy’s scale.
- **Scalability:** Include the capacity ceiling (AUM at which Sharpe degrades by 30%) as a criterion.
- **Interpretability:** Add a metric such as the number of SHAP-dominant features or the fraction of decisions that can be explained by a simple decision tree.
- **Environmental, Social, and Governance (ESG):** Incorporate ESG scores as criteria, using outranking or fuzzy MCDA to handle potential conflicts with return objectives [76].

The normalization and aggregation steps remain the same; only the criteria list expands.

---

## Conclusion

Designing a standardized, multi-dimensional evaluation framework for quantitative trading strategies requires integrating insights from financial econometrics, risk management, machine learning, and operations research. The proposed framework addresses all key dimensions—returns, risk, and adaptability—while incorporating corrections for backtest overfitting and multiple testing that are essential for separating genuine skill from statistical noise. By using a hybrid MCDA approach (AHP for weighting, TOPSIS for ranking, and PROMETHEE or ELECTRE for robustness) and adopting open-source tools for reproducibility, the framework is both rigorous and flexible. It can be applied to any strategy type—multi-factor, HFT, statistical arbitrage, or ML-based—and can be extended to include additional metrics like liquidity, scalability, and interpretability as needed. The ultimate goal is not to produce a single number, but to illuminate the trade-offs between competing objectives, enabling informed decisions in the constant pursuit of alpha.

---

### Sources

[1] Foxholm Financial – Risk-Adjusted Return Metrics: https://foxholm.com/q/concepts/risk-adjusted-returns  
[2] Sharpe Ratio – Wikipedia: https://en.wikipedia.org/wiki/Sharpe_ratio  
[3] Sharpe Ratio – Investopedia: https://www.investopedia.com/terms/s/sharperatio.asp  
[4] Implications of Sharpe Ratio as a Performance Measure – Bank of Canada: https://www.bankofcanada.ca/wp-content/uploads/2010/09/lazrak.pdf  
[5] Sharpe Ratio vs. Sortino vs. Calmar – Optimized Portfolio: https://www.optimizedportfolio.com/risk-adjusted-return  
[6] Sortino Ratio – TradesViz: https://www.tradesviz.com/glossary/sortino-ratio  
[7] Sortino Ratio – Quantt: https://www.quantt.co.uk/resources/sortino-ratio-explained  
[8] Sharpe Ratio vs Sortino Ratio – PicturePerfectPortfolios: https://pictureperfectportfolios.com/sharpe-ratio-vs-sortino-ratio  
[9] Calmar Ratio – QuantVPS: https://www.quantvps.com/blog/how-to-calculate-the-calmar-ratio  
[10] Calmar Ratio – Campaign for a Million: https://www.campaignforamillion.com/post/the-calmar-ratio-explained-why-drawdown-matters-more-than-most-investors-realise  
[11] Calmar Ratio – TradesViz: https://www.tradesviz.com/glossary/calmar-ratio  
[12] Omega Ratio – Wikipedia: https://en.wikipedia.org/wiki/Omega_ratio  
[13] Omega Ratio – LinkedIn: https://www.linkedin.com/posts/trichyravis_omega-ratio-in-portfolio-evaluation-activity-7411259538596818944-lEg5  
[14] Information Ratio – Investopedia: https://www.investopedia.com/terms/i/informationratio.asp  
[15] Fundamental Law of Active Management – CFA Institute: https://www.cfainstitute.org/en/membership/professional-development/refresher-readings/fundamental-law-active-management  
[16] Treynor Ratio – Corporate Finance Institute: https://corporatefinanceinstitute.com/resources/treynor-ratio/  
[17] Modigliani-Modigliani Measure – Wikipedia: https://en.wikipedia.org/wiki/Modigliani-Modigliani_measure  
[18] Advanced Trading Metrics: Sharpe, Sortino, Calmar, SQN & K-Ratio (2026): https://tradingwyckoff.com/en/algorithmic-trading/advanced-trading-metrics  
[19] Maximum Drawdown – TradingStrategy.ai: https://tradingstrategy.ai/glossary/maximum-drawdown  
[20] Ulcer Index – TradingStrategy.ai: https://tradingstrategy.ai/glossary/ulcer-index  
[21] Conditional Drawdown at Risk – Wikipedia: https://en.wikipedia.org/wiki/Conditional_drawdown_at_risk  
[22] Downside Deviation – CFA Institute: https://rpc.cfainstitute.org/sites/default/files/-/media/documents/code/gips/the-sortino-ratio.pdf  
[23] Markowitz 1959 – Downside Risk: https://research.rug.nl/en/publications/downside-risk-capturing-whats-at-stake-in-investment-situations  
[24] Realised Semivariance – Barndorff-Nielsen et al.: https://www.econ.uzh.ch/dam/jcr:00000000-0000-0000-0000-000000000000/RS.pdf  
[25] Value at Risk – Quantt: https://www.quantt.co.uk/resources/value-at-risk  
[26] Coherent Risk Measures – Wikipedia: https://en.wikipedia.org/wiki/Coherent_risk_measure  
[27] FRTB – Basel III: https://www.bis.org/basel_framework/standard/MAR.htm  
[28] Extreme Value Theory – Quantt: https://www.quantt.co.uk/resources/extreme-value-theory  
[29] Lo (2002) – Autocorrelation and Sharpe Ratio: https://www.pm-research.com/content/iijinvest/29/3/36  
[30] Autocorrelation of Squared Returns – Graham Capital Management: https://www.grahamcapital.com/research/autocorrelation-of-squared-returns  
[31] Basel Committee – Liquidity Risk Framework: https://www.bis.org/publ/bcbs188.pdf  
[32] Hidden Markov Model for Regime Detection – QuantInsti: https://blog.quantinsti.com/hidden-markov-models/  
[33] HMM Strategy Backtest – QSTrader: https://www.quantstart.com/articles/Hidden-Markov-Models-for-Regime-Detection  
[34] Hamilton (1989) Markov Switching – Palgrave: https://link.springer.com/referenceworkentry/10.1057/978-1-349-95121-5_2954-1  
[35] Time-Varying Transition Probabilities – Filardo (1994): https://www.jstor.org/stable/1391591  
[36] Two Sigma – GMM Regime Modeling: https://www.twosigma.com/articles/a-machine-learning-approach-to-regime-modeling/  
[37] Wasserstein K-Means for Regime Detection – Macrosynergy: https://macrosynergy.com/research/wasserstein-k-means-for-market-regime-detection/  
[38] Regime Detection Evaluation Standard – Foxholm: https://foxholm.com/q/concepts/market-regime-detection  
[39] Almgren-Chriss Model – Optimal Execution: https://www.math.nyu.edu/faculty/chriss/optliq_f.pdf  
[40] Almgren-Chriss – Wikipedia: https://en.wikipedia.org/wiki/Almgren%E2%80%93Chriss_model  
[41] Almgren et al. (2005) – Direct Estimation of Market Impact: https://www.courant.nyu.edu/~almgren/papers/costestim.pdf  
[42] Implementation Shortfall – Investopedia: https://www.investopedia.com/terms/i/implementation-shortfall.asp  
[43] Frazzini, Israel, Moskowitz (2017) – Trading Costs: https://www.aqr.com/Insights/Research/Journal-Article/Trading-Costs  
[44] Frazzini, Israel, Moskowitz (2012) – Break-Even Capacities: https://www.aqr.com/Insights/Research/Working-Paper/Trading-Costs-of-Asset-Pricing-Anomalies  
[45] Landier, Simon, Thesmar (2015) – Capacity of Trading Strategies: https://www.sciencedirect.com/science/article/abs/pii/S0304405X15001736  
[46] Capacity Estimation – Algotrader.ch: https://algotrader.ch/2023/05/15/capacity-estimation-for-trading-strategies/  
[47] Walk-Forward Analysis – Investopedia: https://www.investopedia.com/terms/w/walk-forward-analysis.asp  
[48] Anchored vs. Rolling Windows – purgedcv Documentation: https://purgedcv.readthedocs.io/en/latest/  
[49] Walk-Forward Efficiency Ratio – QuantStart: https://www.quantstart.com/articles/Walk-Forward-Optimization  
[50] Purging and Embargo – López de Prado (2018): https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086  
[51] Combinatorial Purged Cross-Validation – skfolio: https://skfolio.readthedocs.io/en/stable/auto_examples/6_cross_validation/plot_combinatorial_purged_cv.html  
[52] AHP-PROMETHEE for Portfolio Performance – International Journal of Financial Studies: https://www.mdpi.com/2227-7072/11/2/68  
[53] Entropy Weight Method – Wikipedia: https://en.wikipedia.org/wiki/Entropy_weight_method  
[54] Z-Score vs. Min-Max Normalization – Medium: https://medium.com/@navnoorbawa/z-score-vs-min-max-normalization  
[55] Weighted Sum Model – Wikipedia: https://en.wikipedia.org/wiki/Weighted_sum_model  
[56] TOPSIS – Wikipedia: https://en.wikipedia.org/wiki/TOPSIS  
[57] AHP-TOPSIS for Stock Portfolio – Risks MDPI: https://www.mdpi.com/2227-9091/9/5/81  
[58] PROMETHEE – Wikipedia: https://en.wikipedia.org/wiki/PROMETHEE  
[59] ELECTRE – Wikipedia: https://en.wikipedia.org/wiki/ELECTRE  
[60] Data Envelopment Analysis – Wikipedia: https://en.wikipedia.org/wiki/Data_envelopment_analysis  
[61] DEA Hybrid for Trading Strategies – Academic Journal of Computing & Information Science: https://www.ewadirect.com/proceedings/ace/article/view/2502  
[62] Fuzzy MCDA – MDPI: https://www.mdpi.com/2071-1050/12/10/4096  
[63] IVPF-MARCOS for Financial Risk – Journal of Risk and Financial Management: https://www.mdpi.com/1911-8074/18/1/12  
[64] Deflated Sharpe Ratio – Bailey & López de Prado (2014): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2465678  
[65] Expected Maximum Sharpe – QuantStart: https://www.quantstart.com/articles/Deflated-Sharpe-Ratio  
[66] Probability of Backtest Overfitting – Bailey et al. (2014): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=2326253  
[67] Minimum Track Record Length – López de Prado (2026): https://www.adialab.com/research  
[68] False Strategy Theorem – López de Prado (2018): https://www.wiley.com/en-us/Advances+in+Financial+Machine+Learning-p-9781119482086  
[69] LEAN Engine – QuantConnect: https://www.lean.io/  
[70] Backtrader: https://www.backtrader.com/  
[71] Zipline: https://github.com/quantopian/zipline  
[72] purgedcv: https://github.com/eslazarev/purged-cross-validation  
[73] skfolio: https://skfolio.readthedocs.io/  
[74] pyDecision: https://github.com/Valdecy/pyDecision  
[75] SHAP: https://github.com/shap/shap  
[76] Multicriteria Portfolio Optimization with ESG – EURO 2025: https://www.euro2025.eu/
