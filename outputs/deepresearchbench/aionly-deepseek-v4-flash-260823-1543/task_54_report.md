# Classical Portfolio Theory vs. Deep Learning for Asset Allocation: Core Differences, Market-Conditional Strengths, and Hybrid Integration Paths

## 1. Introduction

The practice of asset allocation sits at the intersection of statistical estimation, economic theory, and computational power. Three families of models dominate the modern FinTech landscape: the **Mean-Variance (Markowitz) model**, the **Black-Litterman model**, and **deep learning approaches** (neural networks, LSTMs, transformers, and reinforcement learning). Each family answers three fundamental questions differently: *How is risk measured? How are returns predicted? How are portfolio weights determined?*

This report provides a systematic comparison of these three families across those dimensions, evaluates their relative advantages and disadvantages under different market conditions, and investigates the practical feasibility of hybrid frameworks that combine the theoretical foundation of classical models with the flexibility of deep learning. The central finding is that the most promising path is not "deep learning replaces classical optimization" but rather "deep learning estimates, classical optimizes" — a division of labor in which machine learning improves the quality of inputs (returns, views, covariances, risk measures) while Markowitz-style optimization or Black-Litterman Bayesian blending provides the structural discipline, interpretability, and regulatory acceptability of the final portfolio.

---

## 2. The Mean-Variance Model (Markowitz, 1952)

Harry Markowitz's seminal paper **"Portfolio Selection"** (Journal of Finance, 1952), for which he received the Nobel Prize in 1990, founded Modern Portfolio Theory (MPT) [1]. Its core intellectual rupture was the insight that risk is not a property of individual assets in isolation, but a property of portfolios: it emerges from the covariance *between* assets [2]. Before Markowitz, diversification was a rule of thumb; after Markowitz, it became a mathematical optimization problem.

### 2.1 Risk Measurement Approach (Variance-Based)

MPT defines risk as the **variance (or standard deviation) of portfolio returns**. The portfolio return is the weighted average of constituent returns, E[Rp] = wᵀμ, while portfolio variance is a quadratic form, σp² = wᵀΣw, in which the off-diagonal covariances matter as much as the diagonal variances [1][3]. This formulation captures the crucial insight that two volatile assets that move out of sync can combine into a portfolio calmer than either asset alone — a US equity fund at 15% annual volatility paired with a commodity ETF at 20% volatility can produce a 50/50 mix below 13% volatility [3].

The risk measure is inherently parametric: it assumes that the covariance matrix Σ fully characterizes the joint distribution of returns, and that variance is the appropriate summary of "danger." As the portfolio-optimization literature documents, this choice has well-known drawbacks: variance penalizes losses *and* gains equally, measures only the width of the main mode of the return distribution, and misses the critical tail of large losses [4]. Alternative measures (semi-variance, downside risk, VaR, CVaR, drawdown) exist, but in classical MVO, risk is always summarized by a single number derived from Σ [4].

### 2.2 Return Prediction Methodology

The Markowitz model takes **historical or expected returns as direct inputs**. Expected returns are typically estimated as historical sample means — an approach that is computationally trivial but statistically fragile. The optimization problem is solved by minimizing wᵀΣw − qRᵀw for varying risk-tolerance factors q, producing the **efficient frontier**: the set of Pareto-optimal portfolios offering the lowest risk for a given level of expected return (or highest return for a given risk) [1][3].

Analytical solutions exist for special cases [3]:

- Minimum-variance portfolio: w_mv = Σ⁻¹1 / (1ᵀΣ⁻¹1)
- Tangency (maximum Sharpe) portfolio: w_tan = Σ⁻¹μ / (1ᵀΣ⁻¹μ)

### 2.3 Asset Allocation Framework

The allocation mechanism is a **convex quadratic optimization** with closed-form solutions. For a given risk aversion λ, the optimal weights are w* = (1/λ)Σ⁻¹μ. The model assumes investors are risk-averse and prefer the efficient frontier's upper-left boundary [1][3]. In practice, three steps are followed: pick a target return, compute the asset combination achieving that return with minimum risk, and repeat for all return targets to trace the frontier [2].

### 2.4 Limitations

The limitations of MVO are extensively documented and are central to the case for both Black-Litterman and deep learning alternatives:

1. **Normality assumption**: MVO assumes returns are normally distributed, but real returns exhibit fat tails, negative skewness, and excess kurtosis. The 2008 financial crisis was a "25-sigma event" under normal assumptions [3]. Correlations also spike toward 1.0 during crises (2008, March 2020), so diversification evaporates precisely when it is most needed [3].

2. **Parameter estimation sensitivity ("error maximization")**: Richard Michaud's 1989 paper in the *Financial Analysts Journal* demonstrated empirically that MVO portfolios performed no better out-of-sample than naive equal-weight portfolios, coining the term **"error maximizer"** [5]. Because optimal weights are w = (1/λ)Σ⁻¹μ, the portfolio amplifies estimation errors in μ through the inverse covariance matrix — it systematically overweight assets with positive estimation errors and underweights those with negative ones [6]. A canonical demonstration: perturbing a single expected-return estimate by 0.5 percentage points shifted an asset's optimal weight from 0% to 38–40%, displacing positions in five other asset classes [7]. Best and Grauer (1991) similarly documented that expected returns are the most sensitive inputs in the optimization [8]. Chopra and Ziemba (1993) found that estimation errors in the mean cause far greater performance shortfall than errors in the covariance matrix [6]. A counter-perspective is offered by Kritzman (2006, 2014), who argues that when assets are close substitutes, the incorrect portfolio's return distribution is similar to the truly optimal one, making the "error maximization" critique more hype than reality in many practical cases [6].

3. **Corner solutions and concentration**: Unconstrained MVO tends to produce extreme, concentrated portfolios. Standard MVO across 12 asset classes allocated 61% to a single asset [7]. Perturbing inputs by just 0.2% noise changed a stock's allocation from 60% to 37% and moved another from 0% to 15% [9]. These portfolios are "one of the most aggressive active management models," concentrating on a small number of bets [10].

4. **Backward-looking inputs**: MVO relies entirely on historical data to estimate expected returns, volatilities, and correlations — it "looks backward, using past performance to predict future results" [11].

5. **Covariance instability**: The covariance matrix itself is not stable over time, and its inversion (required for MVO) amplifies estimation noise. This is why Ledoit-Wolf shrinkage (2004) — blending the sample covariance with an "agnostic" identity-scaled target — has become standard practice in classical implementations [12].

---

## 3. The Black-Litterman Model

The Black-Litterman (BL) model was developed at Goldman Sachs by Fischer Black and Robert Litterman, circulated internally from 1990, and published as **"Global Portfolio Optimization" in the *Financial Analysts Journal* in September 1992** [7][13]. It was designed explicitly to overcome the two fatal flaws of MVO: input sensitivity and unintuitive concentrated portfolios. The model's core principle, stated by Black and Litterman: "The degree of departure from market equilibrium should be proportional to the strength of your conviction — and no view, however confidently stated, should be allowed to destabilise the entire portfolio" [7].

### 3.1 Risk Measurement Approach (Equilibrium Prior + Bayesian Update)

The BL model starts from the assumption that **market-capitalization weights represent an equilibrium portfolio** — a defensible, low-cost baseline [7][14]. Through **reverse optimization** using the CAPM formula, it derives the vector of implied equilibrium excess returns:

**Π = δΣw_mkt**

where δ is the market-implied risk aversion (typically 2.5–3.5, calibrated to a market Sharpe ratio of 0.3–0.5) [7][15]. The prior distribution of returns is N(Π, τΣ), where τ is a scalar (typically 0.025–0.05) controlling uncertainty in the equilibrium prior [7][15][16]. With zero views, the model reduces exactly to the market portfolio — a "graceful degradation" that raw MVO lacks [14].

Risk is thus measured through the same variance-covariance machinery as MVO, but the covariance estimate is embedded in a Bayesian structure that explicitly separates market risk (Σ), prior uncertainty (τΣ), and view uncertainty (Ω).

### 3.2 Return Prediction Methodology (Blending Equilibrium with Views)

The BL model blends market equilibrium expected returns with subjective investor views via **Bayesian updating** — "essentially a weighted average based on the confidence levels in the views" [7]. Three ingredients define the model [7]:

1. **Market equilibrium prior**: reverse optimization from market-cap weights (Π = δΣw_mkt).
2. **Investor views**: absolute views ("Apple will return 10%") or relative views ("Google will outperform Tesla by 6%"), expressed through the pick matrix P and view vector Q. Views need not cover all assets — uncovered assets revert to equilibrium [7][16].
3. **Confidence levels**: each view carries uncertainty captured in the Ω matrix (the He-Litterman method sets Ω = diag(PτΣPᵀ); Idzorek's 2005 method maps intuitive percentage confidences to Ω entries) [7][16].

The master formula for the posterior mean is:

**E(R) = μ_BL = [(τΣ)⁻¹ + PᵀΩ⁻¹P]⁻¹ × [(τΣ)⁻¹Π + PᵀΩ⁻¹Q]**

with posterior covariance **Σ_BL = [(τΣ)⁻¹ + PᵀΩ⁻¹P]⁻¹** [7][14][15][16]. The same result can be derived via Theil's mixed estimation or a fully Bayesian argument — "the formula for the expected excess returns vector is the same from either perspective" [17]. An intuitive property (He & Litterman, 1999): the unconstrained BL optimal portfolio is the scaled market equilibrium portfolio plus a weighted sum of portfolios representing the investor's views [7].

### 3.3 Asset Allocation Methodology

BL portfolios **tilt gently away from the market portfolio in the direction of investor views**, rather than concentrating or shorting aggressively [14][15]. The practical contrast with MVO is stark: standard MVO across 12 asset classes allocated 61% to one asset, while Black-Litterman with identical views held all 12, with the largest weight at 24% and no position below 3%. Average pairwise portfolio correlation dropped from 0.84 (MVO) to 0.47 (BL) [7].

The stability advantage is quantifiable: perturbing parameter space by 0.5% caused a 17% total subset shift in MVO weights, but only ~0.5% shift in Black-Litterman weights [9]. The model produces portfolios managers are willing to implement, reduces the need for ad hoc constraints, handles partial view coverage symmetrically, and forces managers to quantify their conviction [14][15]. Lee (2000) argues BL "essentially mitigates" the error-maximization problem by dispersing errors throughout the vector of expected returns [8].

Institutional adoption is extensive: Goldman Sachs Asset Management (its origin), BlackRock/Aladdin, sovereign wealth funds (Norway's GPFG, GIC, ADIA), pension funds, and robo-advisors including Wealthfront [7][18]. It is explicitly covered in the CFA Level 3 curriculum [7].

### 3.4 Subjectivity Issues and Limitations

The BL model's central weakness is that it **does not generate alpha — it translates existing alpha into allocations**. Wrong views produce worse results than the equilibrium prior alone [7]. Key limitations:

1. **View quality and subjectivity**: There are no formal guidelines for generating views or setting confidence levels; the model does not improve view quality [13][14][19].
2. **τ (tau) sensitivity**: The uncertainty of the equilibrium prior is compressed into a single scalar τ, which is difficult to calibrate and introduces rigidity [20]. Common practice (τ ≈ 0.025–0.05, or 1/T) helps, but under the common calibration Ω = τPΣPᵀ, τ can cancel out in the posterior mean — a subtlety many implementations miss [7].
3. **Risk-aversion parameter ambiguity**: The λ parameter has no consensus value; small changes produce proportional changes in implied returns [7][13].
4. **Model risk under stress**: BL inherits the normality assumption and assumes a stable covariance matrix — assumptions that "break down during market crises" [14]. The market equilibrium prior can be distorted during bubbles [13].
5. **Michaud's critique of BL**: BL "inherits many flaws from Markowitz's original Mean-Variance optimization because it can be characterized as a Markowitz optimization with particular inputs." Specifically: (a) it assumes precise inputs despite estimation error; (b) its use of reverse-engineered "inverse returns" is inconsistent with statistical inference because it also neutralizes information from historical data; and (c) it produces a single optimal portfolio without accommodating the investor's risk tolerance [8].
6. **Roll's critique**: The true market portfolio cannot be observed; only proxies (e.g., S&P 500) are available [9].
7. **Single-period framework**: No rebalancing costs, taxes, or multi-period dynamics [14].
8. **Sensitivity to views**: View changes can dramatically alter allocations — in one demonstration, a view that Canada would beat the US by 3% increased Canadian equity allocation by 95% and reduced US by ~67% [16].

**Extensions**: Meucci (2010) provided the full derivation of the original model and extensions, and his **"Fully Flexible Views" (entropy pooling)** framework generalizes BL beyond normality and linear return views, finding the posterior distribution that minimizes relative entropy subject to arbitrary views (including views on correlations, volatilities, and tail behavior) [21][22]. Bertsimas, Gupta, and Paschalidis (2012) provided an inverse-optimization interpretation of BL that permits views on volatility and market dynamics and extends the framework to coherent risk measures like CVaR [23].

---

## 4. Deep Learning Models

Deep learning (DL) approaches to asset allocation differ fundamentally from the classical models: instead of assuming a parametric return distribution and solving a closed-form optimization, they **learn** risk measures, return predictions, and allocation policies directly from data. The literature spans feedforward networks, LSTMs, GRUs, CNNs, transformers, attention mechanisms, GANs, deep belief networks, and deep reinforcement learning [24][25].

### 4.1 Risk Measurement Approaches

Deep learning enables **non-parametric, learned risk measures** that relax the normality and stationarity assumptions of variance-based risk:

- **Deep quantile regression for Value-at-Risk**: Chronopoulos, Raftapostolos, and Kapetanios (2024, *Journal of Financial Econometrics*) propose a deep neural network quantile estimator that examines non-linear associations between conditional quantiles and predictors. Forecasting 10-day-ahead VaR for US stock returns (1985–2020), the deep quantile estimator outperformed linear and MIDAS quantile models with gains up to 98% relative to linear quantile regression. The framework supports deep LASSO, deep Ridge, and deep Elastic Net penalties, and the authors contributed to interpretability by comparing SHAP values with partial derivatives — finding partial derivatives more stable, computationally cheaper, and better at capturing stressful events (COVID-19, 2008) [26][27].
- **GAN-based Expected Shortfall**: Wang et al. (2024, *Financial Innovation*) combine quantile-regression LSTMs (QRMogLSTM/QRMogGRU) for VaR with GANs that generate future tail-risk scenarios for Expected Shortfall estimation, aligned with the heterogeneous market hypothesis (different market participants operate on different time horizons) [28].
- **Neural nonlinear shrinkage of covariance matrices**: A 2026 preprint starts from Ledoit-Wolf linear shrinkage and applies a lightweight transformer to learn a *nonlinear* eigenvalue shrinkage function, trained directly with out-of-sample portfolio risk as the loss. It consistently yields the lowest realized risk across both n≤N and n>N regimes, outperforming sample covariance, Ledoit-Wolf, and direct weight estimation [29].
- **Learned risk budgeting**: Agal, Raulji, and Odedra (2025, *Scientific Reports*) integrate LSTM volatility forecasting, Gaussian Mixture Model regime switching, and **differentiable risk-budgeting layers** that adjust risk targets dynamically based on VIX, TED spread, and yield-curve dynamics — achieving out-of-sample Sharpe of 1.38 (55% improvement over traditional risk parity) and reducing maximum drawdowns by 41% during stress periods, including de-risking two weeks before the COVID-19 market trough [30].

A key caveat: non-parametric risk estimates are data-hungry and can overfit historical tail patterns. The EURUSD VaR study found neural network models "generally quite unstable" compared to gradient-boosted ensembles [31].

### 4.2 Return Prediction Capabilities

The landmark reference is **Gu, Kelly & Xiu (2020, *Review of Financial Studies*)**, "Empirical Asset Pricing via Machine Learning" — a comparative analysis of generalized linear models, dimension reduction, boosted trees, random forests, and neural networks on nearly 30,000 US stocks (1957–2016) with ~900 predictive signals (94 stock characteristics × macro interactions + industry dummies) [32]. Key findings:

- **Nonlinearity matters**: trees and neural networks achieve monthly out-of-sample R² of 0.33%–0.40%, roughly double the 0.16% of a three-factor linear benchmark (OS3), with gains traced to "allowance of nonlinear predictor interactions that are missed by other methods."
- **Shallow learning beats deep learning**: NN performance peaks at three hidden layers and declines thereafter; trees average fewer than six leaves.
- **Feature engineering beats parameter regularization**: Elastic net with 900 features achieved only 0.11% R² (worse than OS3); PCR achieved 0.26% — "it's the regularization of the features (z) which is much more important than regularizing the parameters" [32][33].
- **Dominant signals**: momentum, liquidity, and volatility; "accounting information does not matter."
- **Economic value**: NN-based S&P 500 timing raises annualized out-of-sample Sharpe from 0.51 (buy-and-hold) to 0.77; long-short decile portfolios sorted on NN predictions earn annualized Sharpes of 1.35 (value-weighted) and 2.45 (equal-weighted), vs. 0.61 and 0.83 for OLS [32].

A critical assessment of GKX notes the best NN's 0.40% R² is "statistically not significantly different" from the simple three-factor linear model, and that the NN's long-short edge comes almost entirely from predicting the *worst*-performing decile of stocks — in 9 of 10 deciles, NN and OS3 perform the same. The implication: long-only investors may prefer simple factor models, while long-short funds benefit from neural networks specifically for shorting the worst performers [33].

**LSTM evidence**: Fischer and Krauss (2018, *European Journal of Operational Research*) deployed LSTMs to predict out-of-sample directional movements for S&P 500 constituents (1992–2015), achieving daily returns of 0.46% and a pre-transaction-cost Sharpe ratio of 5.8 (3.8 after 5bps costs), outperforming random forests, deep nets, and logistic regression [34]. However, replications temper the result: Hasner (2023) on the STOXX Europe 600 found initial accuracy up to 52.52% but steady deterioration from 2017 onward, "attributed to the low signal-to-noise environment, increased technology distribution, and lower entry barriers for smaller investors" [35]. Härkönen (2025) found LSTM-based trading underperformed buy-and-hold for individual stocks across NYSE, NSE, and OMXH, but succeeded in *ranking* stocks for allocation strategies (Rank-Based Allocation consistently beat equal weight) — suggesting LSTM is better at cross-sectional ranking than absolute price prediction [36].

**Transformer approaches**: The Enhanced Multi-Aspect Attention Transformer (EMAT, 2025) explicitly models temporal decay, trend dynamics, and volatility regimes through a multi-aspect attention mechanism with a multi-objective loss (point-wise accuracy + volatility consistency), outperforming state-of-the-art baselines on Chinese and global indices [37]. "Stockformer" (2025) models cross-stock relationships within industries for one-hour-ahead prediction and outperformed LSTM on profitability, though the authors caution that "Transformer training was harder than expected; learning rate selection was critical" [38].

### 4.3 Asset Allocation Approaches

Deep learning approaches to allocation fall into three categories:

1. **End-to-end weight output**: Neural networks directly output portfolio weights. Bertani's University of Bologna thesis trained TCNs, LSTMs, and Transformers to predict the *best asset allocation strategy* directly (rather than asset prices), finding temporal convolutional networks superior to LSTMs and transformers, with average annual revenue increases of 2–5% [39]. The portfolio-optimization textbook documents end-to-end architectures using softmax (no shorting), sign-modified softmax (shorting), generalized sigmoid (position caps), and long-short quintile layers. The best result (single LSTM layer, Sharpe 2.6 vs. benchmarks ≤1.6) "disappears with even 2bps transaction costs, performing no better than a simple benchmark" [40].

2. **Deep reinforcement learning**: J.P. Morgan's DRL vs. MVO study trained PPO agents on a multi-asset environment (2006–2021), optimizing the **Differential Sharpe Ratio** directly. Averaged across 10 backtests (2012–2021), DRL achieved annual return 12.11% vs. MVO 6.53%, Sharpe 1.17 vs. 0.68, and comparable max drawdown (−0.33 vs. −0.33) with lower turnover [41]. However, the WorldQuant comparative evaluation found the opposite: MVO achieved the highest cumulative return (461%) and Sharpe (1.09), while standalone DRL (PPO) underperformed significantly (CAGR 4.62%, Sharpe 0.37) "due to limited structural awareness, supporting literature that naive DRL lacks robustness" [42]. The Uysal et al. (2024) comparison is instructive: a *model-free* architecture (FC + softmax) achieved Sharpe ~0.31–0.56, while a *model-based* approach (neural features fed into a risk-parity optimization block) achieved ~1.10–1.15 — "likely due to overfitting from lack of structural guidance" [40].

3. **DL forecasts feeding classical optimizers**: This hybrid category (detailed in Section 6) is the most successful in the literature: LSTM/CNN predictions feeding Mean-Variance [43][44], Black-Litterman [45][46][47][48][49][50], or risk-parity frameworks [30] consistently outperform both pure classical and pure deep approaches.

### 4.4 Interpretability Challenges

The black-box nature of deep learning is the single most cited obstacle to adoption in regulated investment contexts [25][51][52]. Key challenges:

- **Opacity**: Deep networks do not provide analytical expressions for how inputs map to outputs. The CQF guide notes regulators require demonstrating that models satisfy no-arbitrage conditions, capture risk factors, and behave consistently across regimes — relevant under SR 11-7 and similar model risk management frameworks [51].
- **Non-stationarity**: Models trained on historical data silently extrapolate stale regimes; "training takes days while market data fluctuates hourly or by the minute, meaning models may be trained on outdated data" [52].
- **Data bias**: Survivorship bias (≈45% of S&P 500 constituents were replaced between 2000–2025) and look-ahead bias (a 2024 *Review of Financial Studies* study found correcting for it reduced average Sharpe ratios from 2.1 to 0.8) are pervasive [53].
- **Mitigations**: SHAP values (used in VaR forecasting [31], LSTM evaluation [36], and risk attribution [30]); partial derivatives (more stable than SHAP) [26]; attention visualization (multi-head attention can capture momentum, cycles, volatility patterns) [38]; and component-wise ablation studies (EMAT quantifies each attention component's contribution) [37]. The classical frameworks — especially Black-Litterman — provide interpretable "shells" into which DL predictions can be plugged, preserving a transparent narrative ("equilibrium + ML-derived views + confidence").

---

## 5. Systematic Comparison Across Dimensions

### 5.1 Comparison Table

| Dimension | Mean-Variance (Markowitz) | Black-Litterman | Deep Learning |
|---|---|---|---|
| **Risk measurement** | Parametric variance/covariance; σp² = wᵀΣw; penalizes upside and downside equally; misses tails [4] | Same covariance machinery, but embedded in Bayesian prior (τΣ) and view uncertainty (Ω); still assumes normality and stable Σ [14][16] | Non-parametric, learned risk: deep quantile regression for VaR [26][27], GAN-based ES [28], neural covariance shrinkage [29], differentiable risk budgeting [30]; data-hungry and overfitting-prone |
| **Return prediction** | Historical sample means — extremely imprecise; estimation errors in μ dominate [4][6] | Reverse-optimized equilibrium returns (Π = δΣw_mkt) blended with subjective views via Bayesian updating [7] | Non-linear predictions from high-dimensional features (GKX: 0.40% monthly R² for NNs vs. 0.16% linear); LSTMs/transformers for sequence modeling [32][34][37] |
| **Allocation mechanism** | Closed-form QP: w* = (1/λ)Σ⁻¹μ; efficient frontier; convex, analytically tractable [1][3] | Posterior returns fed into MVO: w* = (δΣ_BL)⁻¹μ_BL; tilts from market portfolio; stable, diversified [7][15] | Direct weight output (end-to-end nets), RL policies (PPO, DQN), or DL forecasts fed into classical optimizers; no convexity required [40][41] |
| **Key assumptions** | Normality; known μ and Σ; risk aversion; stationarity [1][3] | CAPM equilibrium; normality; τ and λ calibration; stable covariance [7][14] | Weak distributional assumptions, but *implicitly* assumes training distribution persists; requires large data [25] |
| **Strengths** | Interpretable; low data/compute needs; theoretical elegance; competitive with well-calibrated inputs [42] | Stable, intuitive portfolios; solves MVO concentration/sensitivity; institutional adoption; graceful degradation to market portfolio [7][14] | Captures non-linearity and interactions; handles high-dimensional/unstructured data (news, text, images); adapts to regimes; optimizes realistic objectives (Sortino, drawdown, ESG, transaction costs) [30][32][41] |
| **Limitations** | Error maximization (Michaud 1989); corner solutions; covariance instability in crises; normality assumption [3][5][7] | Subjective views; τ/λ sensitivity; no alpha generation; normality and equilibrium assumptions break in crises [7][13][14] | Black-box opacity; overfitting (regularization insufficient); >90% of backtested ML strategies fail in production; high data/compute costs; regime staleness [35][53] |

### 5.2 Relative Advantages Under Different Market Conditions

**Stable, normal markets with reliable inputs**: Mean-variance optimization performs well when estimation inputs are reliable and return distributions approximate normality [3]. WorldQuant's comparative evaluation found MVO achieved the highest cumulative return (461.31%) and Sharpe ratio (1.09) in their backtest — "challenging previous critiques (e.g., DeMiguel et al., 2009) by showing traditional methods remain competitive when paired with well-calibrated predictive inputs" [42]. In calm conditions, a three-factor linear model is nearly as good as a neural network for long-only investors [33].

**High estimation uncertainty**: Black-Litterman dominates. Its equilibrium anchoring produces portfolios ~34x less sensitive to input perturbations than MVO (0.5% vs. 17% weight shift) [9]. When genuine alpha views exist, BL translates them into tilts; when they don't, it collapses gracefully to the market portfolio [7]. Empirical studies show BL portfolios are smoother and generate higher excess returns than equilibrium-only portfolios [54].

**Crisis / volatile markets**: All classical models suffer because correlations spike toward 1.0 and covariance estimates lag regime changes [3]. Deep learning with explicit regime-switching can help: Agal et al. (2025) reduced drawdowns by 41% during stress and de-risked two weeks before the COVID trough [30]. J.P. Morgan's DRL showed lower turnover and more consistent monthly returns than MVO during March 2020 [41]. However, the 2022 bear market was challenging for RL systems, and deep models without regime-switching silently extrapolate stale regimes [53][55].

**Non-normal return distributions**: Variance-based measures systematically miss skewness and tail risk [4]. Deep quantile regression and GAN-based ES estimation are purpose-built for fat tails and outperformed linear quantile models by up to 98% [26][28]. BL's normality assumption "breaks down during market crises" [14].

**Efficient vs. inefficient markets**: Deep learning's edge erodes as markets become more efficient and accessible — the STOXX Europe 600 replication found DL accuracy fell behind benchmarks from 2017 onward [35]. Predictive accuracy declined in the larger, more efficient NYSE, while allocation strategies performed best there, "suggesting prevailing market trends matter more than structural factors" [36]. In retail-dominated markets (e.g., China), ML models significantly outperform OLS because technical and trading information is more influential [56].

**Data-rich vs. data-scarce environments**: Deep learning requires large, clean panels (GKX used ~30,000 stocks × 60 years; the Vietnam study had only 59 stocks after filtering) [32][44]. Classical models remain viable with modest data. The MarketXLS practical guidance suggests basic MPT for portfolios under $1M, Black-Litterman for $50M+ with research teams, and AI-driven approaches for $100M+ with significant infrastructure [11].

---

## 6. Hybrid and Ensemble Frameworks

The comparative evidence points toward integration rather than substitution. Three hybrid architectures have strong empirical support.

### 6.1 Deep Learning Improving Parameter Estimation for Mean-Variance

**ML-predicted returns replacing historical averages** is the most direct hybrid:

- **Chaweewanchon & Chaysiri (2022, *Int. J. Financial Studies*)**: A hybrid R-CNN-BiLSTM model with robust input features (Huber's location estimator) predicts stock returns, and the predictions feed a Markowitz MV optimizer on SET50 data. The R-CNN-BiLSTM+MV approach outperformed LSTM/BiLSTM/CNN-BiLSTM baselines on MAE (1.4582 vs. up to 1.7219), Sharpe ratio, mean return, and risk. Their two contributions: a novel predictive model for portfolio formation, and a stock-selection process for high-quality MV inputs [43].
- **Nguyen (2025, *PLoS One*)**: LSTM and 1D-CNN predictions combined with three classical frameworks — Mean-Variance with Forecasting (return-seeking), Risk Parity (moderate-risk), and Maximum Drawdown (conservative) — on VN-100 stocks. The study "demonstrates the value of aligning predictive models with appropriate optimization strategies for improved investment outcomes" [44].
- **Butler & Kwon (2023)**: A linear return-forecasting network integrated with a mean-variance optimization layer, backpropagating through the portfolio solution's partial derivatives. Tested on 24 global futures markets (1986–2020), it achieved significant Sharpe improvement over MSE-trained benchmarks [40].
- **Gu, Kelly & Xiu (2020)** themselves: NN predictions improve long-short Sharpe precisely because classical decile construction captures the NN's edge in predicting the worst-performing stocks [32][33].

**DL for covariance estimation**: The neural nonlinear shrinkage transformer (trained with portfolio risk as the loss function) outperforms Ledoit-Wolf and sample covariance in both n≤N and n>N regimes, particularly in volatile periods. Its authors explicitly frame future work as "extending the framework to jointly estimate covariance and expected returns for optimization under objectives like Sharpe ratio maximization or classical Markowitz mean-variance formulation" [29]. López de Prado, Simonian, Fabozzi and Fabozzi (2024, *Annals of Operations Research*) formalize this agenda — "Enhancing Markowitz's portfolio selection paradigm with machine learning" — covering SVMs, clustering/HRP, RL, and LSTM applications, and showing how ML advances "robust mathematical strategies necessary for modern financial markets," including CVaR optimization [57].

### 6.2 Machine Learning Modeling the Subjective Views in Black-Litterman

This is the most active and successful hybrid frontier. The core idea: use ML to generate **objective, data-driven views** (P, Q) and **confidence levels** (Ω), replacing subjective analyst judgment.

- **Su, Lu & Yen (2026, *Expert Systems with Applications*) — CGL-BL Model**: CEEMDAN time-series decomposition into intrinsic mode functions, each forecast by a genetic-algorithm-optimized LSTM, with a second LSTM for nonlinear aggregation. These DL-generated views feed the classical BL model, producing "objective, data-driven investor views rather than subjective ones." Results: excess returns of 49.91%–70.27% on the SSE 50 and 59.43%–76.81% on the DJIA, outperforming all benchmarks on excess return, Sharpe, and max drawdown, with walk-forward validation demonstrating robust generalization [45].
- **Colasanto et al. (2022, *Neural Computing and Applications*)**: **FinBERT** (BERT fine-tuned on financial text; accuracy 0.86, F1 0.84) generates sentiment scores from Financial Times articles, which are converted into BL views via a Monte Carlo price-path method. On 10 NASDAQ-100 stocks, the FinBERT-view BL achieved Sharpe 1.14 vs. 1.07 without views — "a method to 'quantify' the intensity of news that will influence the choice of stocks in a financial portfolio" [46].
- **Hung, Hsia, Kuang & Lin (2024, *International Review of Economics & Finance*)**: Google's BERT measures news sentiment; sentiment features feed vanilla RNN, LSTM, and GRU price predictors. The **Black-Litterman portfolio with BERT-sentiment + GRU predictions achieved the highest annualized return of 46.6%, Sharpe of 13.0, and Sortino of 17.9%**, directly addressing the "view distribution construction has traditionally been challenging due to subjective judgment requirements" [47].
- **Pantoja Robayo et al. (2025, *Computational Economics*)**: LSTM networks generate "expert opinions" for iterative active portfolio management using Twitter (X) sentiment (FinBERT) plus fundamentals for S&P 500 stocks (2010–2022). **Portfolios with LSTM-generated views outperform standard BL portfolios with Jensen alpha up to 31% annualized** and notably outperform the S&P 500 [48].
- **LLM-Enhanced Black-Litterman (CIKM 2025, arXiv:2504.14345)**: Translates return forecasts and predictive uncertainty from four LLMs (Gemma-7B, Qwen-2-7B, LLaMA-3.1-8B, GPT-4o-mini) into BL views and confidence matrices. Each LLM is queried 100 times per stock; the mean forms the view vector and the variance forms Ω. Results: BLM-Qwen achieved the highest CAGR (0.2811), BLM-Llama the highest annualized Sharpe (1.2286), both significantly outperforming equal-weight (CAGR 0.1907, Sharpe 0.8937) and MVO (CAGR 0.0607, Sharpe 0.2793) baselines. Critically, "the selection of an LLM is not a search for a single best forecaster, but a strategic choice of an investment style whose success is contingent on its alignment with the prevailing market regime" [49].
- **Mantshimuli & Mwamba (2025, *Investment Management and Financial Innovations*)**: An LSTM aggregates sentiment scores from three finance-domain fine-tuned LLMs into a robust Meta-LLM sentiment score incorporated into BL. S&P 500 results: annualized return 31.22% (vs. 24.57% market cap-weighted), Sharpe 3.02, Jensen's alpha 1.95% — outperforming both benchmarks and single-LLM portfolios, while addressing the risk that "existing approaches often rely on single-model sentiment scores that may suffer from biases or hallucinations" [50].

A cautionary note from the literature: "BL does not generate alpha — it translates existing alpha into allocations" [7]. The LLM-BL study confirms that performance is directly linked to how well the LLM's sentiment aligns with the market regime: Gemma's persistent pessimism and GPT's vacillation hurt performance during a generally bullish test period [49]. View quality remains the binding constraint; ML improves objectivity but does not guarantee correctness.

### 6.3 Ensemble and Hybrid Allocation Architectures

Beyond input generation, several frameworks blend classical and ML components at the allocation level:

- **WorldQuant (2024)**: Hybrid models (Autoencoder+DRL, Transformer+GNN) "offered competitive risk-adjusted returns with enhanced robustness compared to standalone models." Transformer+GNN achieved the lowest volatility (14.67%) and lowest max drawdown (−18.81%) across all strategies, while MVO achieved the highest Sharpe. The authors conclude "combining deep learning feature extraction with classical optimization frameworks (MVO) is a promising direction" [42].
- **Agal et al. (2025)**: Integrated architecture jointly optimizing LSTM volatility forecasting, GMM regime detection, and differentiable risk-budgeting layers — a modern analog of risk parity with DL inputs. Walk-forward validation (2005–2022) with 5-year training windows; Sharpe 1.38 out-of-sample; 55% improvement over traditional risk parity; linear scaling to 50 assets in under 25ms [30].
- **Uysal et al. (2024)**: The model-based approach (neural features + risk-parity optimization block, Sharpe ~1.10–1.15) decisively outperformed model-free (Sharpe ~0.31–0.56) on the same data — the clearest evidence that classical structural constraints prevent DL overfitting [40].
- **Shigolakov & Byers (JIBF)**: BL as foundation with view matrix construction from ML/DL/RL predictions, hypothesizing "an ML/DL-based Black-Litterman model will demonstrate higher cumulative returns and Sharpe ratios compared to classical Markowitz and BL models" [58].
- **López de Prado (2016) HRP**: Hierarchical Risk Parity uses ML clustering (hierarchical clustering on correlation structure) to avoid covariance inversion entirely — a classical risk-parity construction informed by unsupervised learning [57].

### 6.4 Practical Feasibility of Integration

**The dominant architecture**: The evidence converges on a **"deep learning estimates, classical optimizes"** pipeline with five components:

1. **ML predicts returns/views/volatility** (GKX-style return models [32], FinBERT sentiment [46], LSTM views [48], LLM views [49], neural covariance shrinkage [29]).
2. **Classical MVO or BL performs construction and risk management** — preserving convexity, interpretability, and regulatory familiarity [7][57].
3. **ML-learned confidence levels in BL replace subjective judgment** — the Ω matrix becomes an empirical object (e.g., variance across LLM queries [49], or across Monte Carlo simulations [46]).
4. **Rigorous walk-forward validation with cost and bias correction is mandatory** — the "90/10 Rule": "spend 90% of time on validation methodology and 10% on model architecture. A simple model with rigorous backtesting outperforms a sophisticated model with sloppy backtesting" [53].
5. **Pure end-to-end deep allocation should be treated with skepticism** outside well-resourced hedge-fund contexts, given documented fragility (WorldQuant DRL Sharpe 0.37 [42]; Uysal model-free 0.31–0.56 [40]; Zhang et al. cost sensitivity — Sharpe 2.6 disappears with 2bps transaction costs [40]).

**Implementation considerations**:

- **Data requirements**: Classical models need only historical prices and market caps; DL components need large clean panels (GKX: 30,000 stocks × 60 years [32]), alternative data (news [46], Twitter [48]), or multi-LLM sentiment pipelines [49][50]. Emerging markets often lack data depth [44].
- **Computational costs**: Deep RL is heavy (J.P. Morgan: 7.5M training timesteps per round, ~6 hours on GPU) [41][58]. Hybrids add walk-forward retraining loops. Neural covariance shrinkage and sparse-attention risk budgeting are comparatively lightweight (50 assets in <25ms) [29][30].
- **Overfitting risk — the dominant concern**: "Industry estimates from firms like Man AHL and Two Sigma suggest that over 90% of backtested ML strategies fail to generate positive returns in production" [53]. A rigorous walk-forward validation framework (arXiv 2512.12924) testing an RL system across 34 independent periods found modest returns (Sharpe 0.33), statistically insignificant aggregate performance (p = 0.34), and only 12% statistical power — a rare honest counterpoint to typical claims of 15–30% annual returns [55]. Look-ahead bias correction reduces average Sharpe ratios from 2.1 to 0.8 [53].
- **Validation protocol**: Strictly chronological splits (train/validation/test) with embargo gaps; purged K-fold cross-validation and combinatorial purged CV (López de Prado) [53][59]; walk-forward analysis with rolling windows (3–5 years best for equities) [60]; transaction costs included (Fischer-Krauss Sharpe collapsed from 5.8 to 3.8 with 5bps; Zhang et al. vanished with 2bps) [34][40]. Deploy at 25% position size, scale up after 6+ months; live performance typically 30–50% worse than backtested [53].
- **Regulatory and interpretability**: Black-Litterman's Bayesian structure provides a transparent narrative ("equilibrium + ML-derived views + confidence"), making ML-enhanced BL the most regulation-friendly hybrid [49][50]. SHAP-based risk attribution, attention visualization, and component ablation are the standard interpretability toolkits [26][30][37]. Model risk management frameworks (SR 11-7) require demonstrating no-arbitrage consistency and regime stability [51].
- **Calibration pitfalls**: Ledoit-Wolf shrinkage for covariance (not raw sample covariance) [12]; τ in 0.025–0.05 range (not 1.0) [7]; 2–4 differentiated views with Idzorek confidence calibration (not dozens of binary views) [7]; market-cap-weighted global indices as the BL prior universe [7].

---

## 7. Conclusion

The three model families answer the core questions of asset allocation from fundamentally different epistemological positions. **Mean-Variance** is a parametric, closed-form optimization that assumes risk is variance and returns are historical averages — elegant and interpretable, but fragile to estimation error, concentration-prone, and blind to non-normal tails. **Black-Litterman** preserves MVO's optimization machinery but replaces historical returns with equilibrium-implied returns and subjective views, dramatically improving stability and intuition at the cost of introducing subjectivity in views, confidence, and calibration parameters. **Deep learning** abandons parametric assumptions entirely, learning risk measures, return predictions, and allocation policies from data — capturing non-linear interactions and adapting to regimes, but at the cost of black-box opacity, severe overfitting risk, and high data/compute requirements.

The comparative evidence across market conditions supports a nuanced conclusion: classical models hold their own when inputs are well-calibrated and markets are stable; BL excels under estimation uncertainty; DL's edge appears in non-linear, data-rich, less-efficient environments and for tail-risk measurement — but its advantages erode in efficient markets and often vanish after transaction costs.

The most promising path forward is therefore **hybridization with a clear division of labor**: deep learning generates objective views, return forecasts, volatility estimates, and confidence levels; classical Mean-Variance or Black-Litterman frameworks perform the final optimization, providing structure, interpretability, and regulatory acceptability. The empirical record — from R-CNN-BiLSTM+MV on SET50 [43], to FinBERT-BL on NASDAQ-100 [46], to LLM-enhanced BL on the S&P 500 [49] — consistently shows hybrid portfolios outperforming both pure classical and pure deep alternatives. The binding constraints are not architectural but methodological: rigorous walk-forward validation, honest bias correction, and transaction-cost awareness. As one practitioner framework puts it, the selection of a forecasting engine is "not a search for a single best forecaster, but a strategic choice of an investment style whose success is contingent on its alignment with the prevailing market regime" [49] — and the classical frameworks provide the discipline to survive when that alignment breaks.

---

### Sources

[1] Modern Portfolio Theory — Wikipedia: https://en.wikipedia.org/wiki/Modern_Portfolio_Theory

[2] B&F NOB-35 | Harry Markowitz (1990) — Portfolio Selection and Risk Diversification: https://www.youtube.com/watch?v=-Elgc80NFQg

[3] Modern Portfolio Theory from Scratch: The Efficient Frontier — Sesen.ai: https://sesen.ai/blog/modern-portfolio-theory-markowitz-efficient-frontier

[4] Portfolio Optimization Textbook, Section 7.5 "Drawbacks" (Markowitz Mean-Variance Portfolio): https://portfoliooptimizationbook.com/book/7.5-MVP-drawbacks.html

[5] The Markowitz Optimization Enigma: Is 'Optimized' Optimal? (Michaud, 1989): https://www.researchgate.net/publication/247883727_The_Markowitz_Optimization_Enigma_Is_'Optimized'_Optimal

[6] Markowitz mean-variance optimization as "error maximization" (Quantitative Finance Stack Exchange): https://quant.stackexchange.com/questions/4132/markowitz-mean-variance-optimization-as-error-maximization

[7] The Black-Litterman Model: Bayesian Portfolio Optimization — A.L. Capital Advisory: https://alcapitaladvisory.com/research/frameworks/black-litterman.html

[8] Deconstructing Black-Litterman Optimization: A Brief Overview — New Frontier Advisors: https://www.newfrontieradvisors.com/insights/all-insights/deconstructing-black-litterman-optimization-a-brief-overview

[9] Black-Litterman vs. Mean-Variance Portfolio Optimization (MVO) in Python — Quant Guild: https://www.youtube.com/watch?v=o1mCFVt79Y8

[10] How Machine Learning Can Improve Portfolio Allocation of Robo-Advisors — Thierry Roncalli (Amundi): http://www.thierry-roncalli.com/download/SwissQuant-Conference-Robo-Roncalli-2019.pdf

[11] Portfolio Optimization — Black-Litterman, AI & Advanced Methods — MarketXLS: https://marketxls.com/blog/advanced-portfolio-optimization-black-litterman-ai

[12] Covariance matrix shrinkage: Ledoit and Wolf (2004) — NEDL: https://www.youtube.com/watch?v=heXLyuCTP1Y

[13] Black & Litterman (1992): Global Portfolio Optimization — Foxholm Financial: https://foxholm.com/q/research/black-litterman-model

[14] The Black-Litterman Model — Ryan O'Connell, CFA: https://ryanoconnellfinance.com/black-litterman-model

[15] Bayesian Portfolio Optimisation: Introducing the Black-Litterman Model — Hudson & Thames: https://hudsonthames.org/bayesian-portfolio-optimisation-the-black-litterman-model

[16] Bayesian Portfolio Optimisation: The Black-Litterman Model — Hudson & Thames: https://hudsonthames.org/bayesian-portfolio-optimisation-the-black-litterman-model

[17] Reading on Black-Litterman Model — Medium: https://medium.com/@li.ying.explore/reading-on-black-litterman-model-beecfcd0a82c

[18] How Robo-Advisors Actually Invest Your Money — Investopedia: https://www.investopedia.com/how-robo-advisors-actually-invest-your-money-11776454

[19] Black-Litterman Model — Financial Edge Training: https://www.fe.training/free-resources/portfolio-management/black-litterman-model

[20] Uncertainty in the Black-Litterman Model — A Practical Note (Fuhrer & Hock, 2019): https://www.oth-aw.de/files/oth-aw/Aktuelles/Veroeffentlichungen/WEN-Diskussionspapier/WEN-DPs-PDF/DP68.pdf

[21] The Black-Litterman Approach: Original Model and Extensions — SSRN (Meucci): https://papers.ssrn.com/sol3/papers.cfm?abstract_id=1117574

[22] Fully flexible views: theory and practice — Risk.net (Meucci): https://www.risk.net/derivatives/structured-products/1500207/fully-flexible-views-theory-and-practice

[23] Inverse Optimization: A New Perspective on the Black-Litterman Model (Bertsimas, Gupta & Paschalidis, Operations Research 2012): https://pmc.ncbi.nlm.nih.gov/articles/PMC4224190

[24] Deep Learning in Finance: A Survey of Applications and Techniques (MDPI AI, 2024): https://www.mdpi.com/2673-2688/5/4/101

[25] Enhancing portfolio management using artificial intelligence: literature review (Frontiers in Artificial Intelligence, 2024): https://pmc.ncbi.nlm.nih.gov/articles/PMC11033520

[26] Forecasting Value-at-Risk Using Deep Neural Network Quantile Regression (Journal of Financial Econometrics, 2024): https://academic.oup.com/jfec/article/22/3/636/7163191

[27] Forecasting Value-at-Risk Using Deep Neural Network Quantile Regression (Essex repository PDF): https://repository.essex.ac.uk/35621/1/crk2023.pdf

[28] Forecasting VaR and ES by using deep quantile regression, GANs-based scenario generation, and heterogeneous market hypothesis (Financial Innovation, 2024): https://link.springer.com/article/10.1186/s40854-023-00564-5

[29] Neural Nonlinear Shrinkage of Covariance Matrices for Minimum Variance Portfolio Optimization: https://arxiv.org/html/2601.15597v1

[30] A machine learning approach to risk based asset allocation in portfolio optimization (Scientific Reports, 2025): https://www.nature.com/articles/s41598-025-26337-x

[31] Estimating Value-at-Risk in the EURUSD Currency Cross from Implied Volatilities Using Machine Learning Methods and Quantile Regression (JRFM, 2023): https://www.mdpi.com/1911-8074/16/7/312

[32] Empirical Asset Pricing via Machine Learning (Gu, Kelly & Xiu, Review of Financial Studies 2020; NBER WP 25398): https://www.nber.org/system/files/working_papers/w25398/revisions/w25398.rev1.pdf

[33] Gu, Kelly Xiu (2020, RFS): Empirical Asset Pricing via Machine Learning — Critical Lecture (Financial Data Science 2025): https://www.youtube.com/watch?v=DQNLCiIRuFs

[34] Deep learning with long short-term memory networks for financial market predictions (Fischer & Krauss, EJOR 2018): https://ideas.repec.org/p/zbw/iwqwdp/112017.html

[35] Predictive Capabilities of LSTM Networks: A Case Study of the STOXX Europe 600 Index (Hasner, 2023): https://plexusinvestments.com/site/wp-content/uploads/2024/04/Hasner-Bachelorthesis.pdf

[36] Stock Market Prediction with Long Short-Term Memory Networks (Härkönen, University of Turku, 2025): https://www.utupub.fi/bitstreams/d55b5be9-e88a-4c42-ac00-3216017969e7/download

[37] EMAT: Enhanced Multi-Aspect Attention Transformer for Financial Time Series Forecasting (Entropy, 2025): https://www.mdpi.com/1099-4300/27/10/1029

[38] Transformer Based Time-Series Forecasting For Stock (Stockformer, arXiv:2502.09625): https://arxiv.org/html/2502.09625v1

[39] Deep Learning methods for Portfolio Optimization (Bertani, University of Bologna): https://amslaurea.unibo.it/id/eprint/24245/1/federico_bertani_tesi.pdf

[40] Portfolio Optimization Textbook, Section 16.4 "Deep Learning Portfolio Case Studies": https://portfoliooptimizationbook.com/book/16.4-deep-learning-portfolio-case-studies.html

[41] Deep Reinforcement Learning for Optimal Portfolio Allocation: A Comparative Study with Mean-Variance Optimization (J.P. Morgan, ICAPS FinPlan'23): https://arxiv.org/html/2602.17098

[42] Comparative Evaluation of Modern Deep Learning Methodologies for Portfolio Optimization (WorldQuant University): https://arxiv.org/pdf/2604.24486

[43] Markowitz Mean-Variance Portfolio Optimization with Predictive Stock Selection Using Machine Learning (Chaweewanchon & Chaysiri, 2022): https://www.mdpi.com/2227-7072/10/3/64

[44] Advanced investing with deep learning for risk-aligned portfolio optimization (Nguyen, PLoS One 2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12364330

[45] Objective Black-Litterman views through deep learning: A novel hybrid model for enhanced portfolio returns (Su, Lu & Yen, Expert Systems with Applications 2026): https://www.sciencedirect.com/science/article/abs/pii/S0957417425024856

[46] BERT's sentiment score for portfolio optimization: a fine-tuned view in Black and Litterman model (Colasanto et al., 2022): https://pmc.ncbi.nlm.nih.gov/articles/PMC9150638

[47] Intelligent portfolio construction via news sentiment analysis (Hung et al., International Review of Economics & Finance 2024): https://www.sciencedirect.com/science/article/abs/pii/S1059056023003131

[48] Iterative Deep Learning Approach to Active Portfolio Management with Sentiment Factors (Pantoja Robayo et al., Computational Economics 2025): https://link.springer.com/article/10.1007/s10614-024-10702-5

[49] LLM-Enhanced Black-Litterman Portfolio Optimization (CIKM '25, arXiv:2504.14345): https://arxiv.org/html/2504.14345v2

[50] Enhancing portfolio optimization with multi-LLM sentiment aggregation: A Black-Litterman integration approach (Mantshimuli & Mwamba, 2025): https://businessperspectives.org/publishing-policies2/enhancing-portfolio-optimization-with-multi-llm-sentiment-aggregation-a-black-litterman-integration-approach

[51] A Guide to Applying Deep Learning in Quantitative Finance — CQF: https://www.cqf.com/blog/guide-applying-deep-learning-quantitative-finance

[52] A Comprehensive Review: Applicability of Deep Neural Networks in Business Decision Making and Market Prediction Investment (arXiv:2502.00151): https://arxiv.org/html/2502.00151v1

[53] Machine Learning Backtesting: How to Train and Validate ML Trading Models — TradeAlgo: https://www.tradealgo.com/trading-guides/ai-trading/machine-learning-backtesting-guide

[54] Testing the Black-Litterman Model (Lund University thesis): https://lup.lub.lu.se/luur/download?func=downloadFile&recordOId=2155310&fileOId=2155313

[55] A Rigorous Walk-Forward Validation Framework for Market... (arXiv:2512.12924): https://arxiv.org/html/2512.12924v1

[56] Empirical Asset Pricing via Machine Learning – Evidence from the Chinese stock market (Stockholm School of Economics, 2023): http://arc.hhs.se/download.aspx?MediumId=5617

[57] Enhancing Markowitz's portfolio selection paradigm with machine learning (López de Prado, Simonian, Fabozzi & Fabozzi, Annals of Operations Research 2024): https://link.springer.com/article/10.1007/s10479-024-06257-1

[58] Black-Litterman Portfolio Optimization using Machine-Learning, Deep Learning and Reinforcement Learning Algorithms (Shigolakov & Byers, JIBF): https://www.opastpublishers.com/peer-review/blacklitterman-portfolio-optimization-using-machinelearning-deep-learning-and-reinforcement-learning-algorithms-10301.html

[59] Portfolio Optimization Textbook, Section 8.3 "The Dangers of Backtesting": https://portfoliooptimizationbook.com/book/8.3-dangers-backtesting.html

[60] Walk-Forward Optimization: How It Works, Its Limitations, and Backtesting Implementation — QuantInsti: https://blog.quantinsti.com/walk-forward-optimization-introduction
