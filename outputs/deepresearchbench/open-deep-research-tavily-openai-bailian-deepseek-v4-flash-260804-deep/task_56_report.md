# A Comprehensive Answer: Solving Asymmetric First-Price Sealed-Bid Auctions

## Introduction

The problem of solving a first-price sealed-bid auction with two bidders who have independent private values drawn from different (ex-ante asymmetric) distributions is a classic and deep problem in auction theory. The short answer is: **there is no general closed-form solution for arbitrary continuous, strictly increasing value distributions.** However, there is a well-established general method for characterizing and numerically solving the equilibrium, which proceeds through a system of differential equations governing the inverse bidding functions. This report provides a comprehensive overview of the theoretical framework, conditions under which closed-form solutions exist, and the standard numerical techniques used when closed-form solutions are unavailable.

---

## The Theoretical Framework: The System of Differential Equations

### The Characterization via Inverse Bid Functions

The foundational result for asymmetric first-price auctions is that the equilibrium bidding strategies can be characterized through a system of differential equations governing the inverse bid functions. In the two-bidder case with independent private values, where bidder \(i\) has valuation \(X_i\) distributed according to \(F_i\) on support \([\underline{v}_i, \bar{v}_i]\), the equilibrium bid functions \(\beta_i(\cdot)\) are strictly increasing, and their inverses \(g_i(b) = \beta_i^{-1}(b)\) satisfy a system of differential equations derived from the first-order conditions of the bidders' expected payoff maximization problems.

The system takes the form:

\[
g_1'(b) = \frac{F_1(g_1(b))}{f_1(g_1(b))} \cdot \frac{1}{g_2(b) - b}
\]

\[
g_2'(b) = \frac{F_2(g_2(b))}{f_2(g_2(b))} \cdot \frac{1}{g_1(b) - b}
\]

This is a system of coupled first-order ordinary differential equations (ODEs) for the inverse bid functions, where \(f_i\) are the density functions corresponding to \(F_i\). As Krishna's *Auction Theory* textbook explains, the standard symmetric approach breaks down when bidders have different distributions, and the analysis proceeds via these inverse bid functions [Krishna (2010), Chapter 8].

### The Boundary Conditions

The system forms a **two-point boundary value problem with a free boundary**. The boundary conditions are:

- **Lower boundary**: At the minimum bid \(b_{\min}\), the inverse bid functions satisfy \(g_i(b_{\min}) = \underline{v}_i\), meaning the lowest-valuation bidders map to the minimum bid. In many cases, \(b_{\min} = \underline{v}_i\) if the lower supports are equal.
- **Upper boundary**: At the maximum bid \(\bar{b}\), both inverse bid functions satisfy \(g_1(\bar{b}) = g_2(\bar{b}) = \bar{v}\), meaning bidders with the highest possible valuations all submit the same maximum bid. Critically, **\(\bar{b}\) is unknown a priori** and must be determined as part of the solution.

This creates a **free boundary value problem** that is overidentified, as noted by Hubbard and Paarsch in their survey [Hubbard & Paarsch (2011)].

### The "Gap" Problem

A key complication arises when the two bidders have different lower supports for their valuations. In this case, the weaker bidder (with the lower valuation support) may not find it profitable to bid below some threshold, creating a **"gap"** where low-valuation bidders of one type do not participate. The equilibrium bid functions must then satisfy specific boundary conditions at the lower end that account for this endogenous participation threshold.

As Dan Quint's lecture notes explain, "the weaker bidder's bid function may start at a positive value," meaning that bidders with very low valuations may not be able to bid, creating a gap in the bid distribution [Quint (2007), Econ 805 Lecture 9].

---

## The General Result: No Closed-Form Solution for Arbitrary Distributions

The literature is unanimous that for arbitrary continuous distributions, **closed-form solutions for the equilibrium bidding strategies do not exist**.

Hubbard and Paarsch state: "The system of first-order differential equations that characterizes a Bayes–Nash equilibrium usually does not have a convenient closed-form solution: typically, approximate solutions can only be calculated numerically" [Hubbard & Paarsch (2011)].

Marshall, Meurer, Richard, and Stromquist similarly note: "The differential equations that characterize these bid functions are mostly untractable, hence numerical techniques can play an important role in the analysis of asymmetric (first price) auctions" [Marshall et al. (1994)].

The paper "First-Price Auctions when the Ranking of Valuations is Common Knowledge" (Hebrew University) states: "We prove existence and uniqueness of a pure-strategy equilibrium for any distribution satisfying mild regularity conditions. We show that the system of differential equations governing equilibrium bid functions generally has no closed-form solution, even for the uniform distribution" [Hebrew University DP 117].

---

## Conditions Under Which Closed-Form Solutions Exist

Closed-form analytical solutions exist only under specific parametric families or distributional assumptions. The main known cases are:

### Uniform Distributions (Kaplan and Zamir, 2012)

The most comprehensive closed-form results are for the case where both bidders have valuations uniformly distributed on possibly different intervals. Kaplan and Zamir (2012) provide **analytic solutions for any asymmetric first-price auction with two uniform bidders**, both with and without a minimum bid \(m\), solving a problem originally posed by Vickrey in 1961 [Kaplan & Zamir (2012), *Economic Theory*].

The paper covers:
- Cases where the minimum bid is non-binding (\(m \leq (\underline{v}_1 + \underline{v}_2)/2\))
- Cases where the minimum bid is binding (\(m > (\underline{v}_1 + \underline{v}_2)/2\) and \(m \neq \underline{v}_2\))
- The special case where \(m = \underline{v}_2\)
- Limit cases where one buyer's value becomes commonly known (recovering mixed-strategy equilibria)

The solutions are shown to be continuous in all parameters (\(\underline{v}_1, \bar{v}_1, \underline{v}_2, \bar{v}_2, m\)). The paper also presents a class where both bid functions are linear, characterized by \(m = (2\underline{v}_2 + \underline{v}_1)/3\) and equal ranges above \(m\).

### Equal Lower Bounds (Plum, 1992)

Plum (1992) analyzed the two-bidder case for arbitrary continuous distributions and proved that the first-price auction has a unique pure strategy equilibrium. He provided **closed-form solutions for the case where the lower bounds of the two distributions are the same**.

### Weak Asymmetry (Fibich and Gavious, 2003)

Fibich and Gavious (2003) provide **explicit approximations** for equilibrium bids under weak asymmetry, expanding around the symmetric case. The equilibrium bids are approximated as:

\[
b_i(v) = b_{\text{sym}}(v) + \varepsilon \cdot B_i(v) + O(\varepsilon^2)
\]

where \(B_i\) is given by a closed-form integral involving the perturbation functions. The seller's expected revenue equals the symmetric revenue (using the average distribution) plus \(O(\varepsilon^2)\), meaning all asymmetric auctions are revenue equivalent to \(O(\varepsilon^2)\) [Fibich & Gavious (2003), *Mathematics of Operations Research*].

### Constructed Examples

There are specific constructed examples where closed-form linear equilibrium strategies exist. For instance, one Stack Exchange example demonstrates a case where the equilibrium strategies are \(\beta_1(x) = x - 1\) and \(\beta_2(x) = (2/3)x\) for distributions \(F_1(x) = \frac{1}{4}(x-1)^2\) over \([1,3]\) and \(F_2(x) = \exp(\frac{2}{3}x - 2)\) over \([0,3]\). The solution is found by guessing affine inverse bid functions \(g_1(b) = \alpha b + \gamma\) and \(g_2(b) = \delta b + \lambda\), and solving the system of differential equations with boundary conditions [Stack Exchange: Math & Economics].

---

## Numerical Methods for Solving Asymmetric First-Price Auctions

Given the general absence of closed-form solutions, numerical methods are essential. The literature has developed several approaches, each with its own strengths and limitations.

### 1. The Backward Shooting Method

The standard approach historically has been the **shooting method**:

1. Treat the unknown common high bid \(\bar{b}\) as an initial condition and integrate backwards from \(\bar{b}\) to the lower bound.
2. Begin with a guess for \(\bar{b}\), then integrate the system of ODEs backward from the right endpoint.
3. Check the solution against the left boundary condition \(g_i(b_{\min}) = \underline{v}_i\).
4. Iteratively adjust \(\bar{b}\) until the left boundary condition is satisfied.

**Critical finding**: The backward-shooting method is **inherently unstable**. Fibich and Gavish (2011) have proven analytically that this instability is not a "technical issue" but rather an analytic property of backward integration in this setting. The instability becomes more severe as the number of players increases and cannot be eliminated by changing the numerical methodology of the backward solver. The system of differential equations does not satisfy the Lipschitz condition in a neighborhood of the lower bound because a singularity obtains there [Fibich & Gavish (2011), *Games and Economic Behavior*].

### 2. The Boundary Value Method (Fibich and Gavish, 2011)

Fibich and Gavish (2011) introduced a novel **boundary-value method** that:

- Transforms the system of ODEs to a fixed domain, allowing stable solution via fixed-point or Newton iterations
- Works for any number of players, mixed distribution types, and reserve prices
- Is considerably more robust than backward shooting
- Simulations demonstrate robustness for up to 450 players

This method reformulates the problem into a system with well-defined initial and terminal conditions, making it amenable to standard boundary value problem solvers [Fibich & Gavish (2011), *Games and Economic Behavior*].

### 3. The Dynamical-Systems Approach (Fibich and Gavish, 2012)

Fibich and Gavish (2012) introduced a **dynamical-systems approach** that:

- Provides a proof of existence and uniqueness of equilibrium strategies for two coalitions and two types of players
- Shows that for \(n\) players, the singular point at \(b=0\) corresponds to a **saddle point** with \(n-1\) admissible directions
- Enables stable **forward-shooting** numerical methods, unlike the unstable backward-shooting approaches
- Is particularly simple for two types of players, requiring no shooting

The dynamical-systems approach provides an intuitive explanation for why the standard backward-shooting method is inherently unstable and enables the devising of a stable forward-shooting method [Fibich & Gavish (2012), *Mathematics of Operations Research*].

### 4. The Taylor-Series Expansion Method (Marshall et al., 1994; Gayle and Richard, 2008)

Marshall, Meurer, Richard, and Stromquist (1994) developed a numerical algorithm using **backward piecewise low-order Taylor series expansions**. This method:

- Uses backward integration from the upper endpoint to avoid numerical instability at the lower boundary
- Overcomes singularities at the origin
- Proves numerically stable despite the inherent instability of the differential equations

Gayle and Richard (2008) extended this approach into a fully automated, numerically robust algorithm that:

- Relies upon a built-in algebra of local Taylor-series expansions
- Accommodates arbitrary distributions (with common support), multiple bidder types, reserve prices, and non-inclusive coalitions
- Computes inverse bid functions, expected revenues, probabilities of winning, probability of retention under reserve pricing, and optimal reserve prices
- Includes built-in distributions (Weibull, beta, normal, lognormal) and handles user-supplied distributions (analytical or tabulated)
- Accuracy is assessed via root mean squared error between equilibrium bids and computed best responses; computational time increases linearly with grid size and order of Taylor expansion

The algorithm is designed for both theoretical investigation and empirical inference [Gayle & Richard (2008), *Computational Economics*].

### 5. The Chebyshev Polynomial / MPEC Approach (Hubbard, Kirkegaard, and Paarsch, 2013)

Hubbard, Kirkegaard, and Paarsch (2013) propose approximating the inverse-bid functions using **Chebyshev polynomials** of varying degrees and solving a constrained optimization problem (MPEC approach) that incorporates boundary conditions and theoretical properties.

Key findings:
- Low-degree polynomial approximations (e.g., \(K=3, 5\)) perform poorly and can lead to incorrect policy recommendations concerning auction design
- Higher-degree approximations (e.g., \(K=25\)) yield stable, theory-consistent solutions
- The authors propose using the exogenous ratio of cumulative distribution functions and the endogenous ratio of expected payoffs to visually check whether approximations satisfy theoretical properties
- Poor approximations can reverse the expected revenue ranking of first-price vs. second-price auctions, leading to misguided policy recommendations

Even without a formal convergence proof, these theoretical checks provide minimal standards for numerical solutions used in empirical work or dynamic game simulations [Hubbard, Kirkegaard & Paarsch (2013), *Computational Economics*].

### 6. The BID Algorithm (Au, Banks, and Guo, 2021)

Au, Banks, and Guo (2021) introduced the **Backward Indifference Derivation (BID) algorithm**, which:

- Constructs a sequence of finite-action pure-strategy Nash equilibria that converge to the continuum-action equilibrium
- Finds where bidders are indifferent between actions, avoiding the system of poorly behaved differential equations
- The authors prove convergence (conditional on knowing the maximum bid)
- The algorithm is evaluated on four examples, two of which had not been previously addressed [Au, Banks & Guo (2021), *Decision Analysis*].

### 7. The Perturbation Approach (Dharanan and Ellis, 2024)

Dharanan and Ellis (2024) study first-price auctions with independent private valuations that have **asymmetric distributions and supports** (different lower and upper bounds). They:

- Prove existence of equilibrium through a perturbation approach
- Approximate the original auction with asymmetric supports by a sequence of auctions with common support (perturbed games)
- Show that the limit of Bayesian Nash equilibria of the perturbed games converges to the BNE of the original auction
- Characterize the BNE: bidding functions are continuous and piecewise differentiable
- Show that the BNE of the perturbed auction is an \(\varepsilon\)-BNE of the original asymmetric-support auction
- Discuss numerical implementation in Julia using MIRK4 methods (a type of implicit Runge-Kutta method for boundary value problems)
- Provide three numerical examples with different distributions (uniform, quadratic, and shifted supports)

This approach bridges the gap between theoretical existence results and practical computation, particularly for the challenging case of asymmetric supports [Dharanan & Ellis (2024), *Games and Economic Behavior*].

### 8. Kirkegaard's Winning-Probability Approach (2009)

Kirkegaard (2009) proposed a **different approach** that circumvents the need to examine bidding strategies directly, instead focusing on buyers' winning probabilities. This approach:

- Exploits the mechanism-design link between winning probabilities and expected payoffs using the envelope theorem
- Derives bids and compares outcomes without solving the complex system of differential equations
- Is particularly useful for comparative statics and revenue comparisons

Key results from this approach:
- In any first-price auction, no buyer can win consistently more often than another
- Under first-order stochastic dominance (a strong buyer vs. a weak buyer), the strong buyer's winning probability is a mean-preserving spread of the weak buyer's, and the strong buyer is strictly better off for every valuation
- The strong buyer's bid distribution first-order stochastically dominates the weak buyer's
- With reverse hazard rate dominance, the weak buyer bids more aggressively than the strong buyer for all valuations
- The approach extends to "predictable vs. unpredictable" buyers (mean-preserving spread) and to asymmetric all-pay auctions

This approach is valuable for deriving qualitative results without numerical computation [Kirkegaard (2009), *Journal of Economic Theory*].

---

## Existence and Uniqueness of Equilibrium

### Existence Results

**Lebrun (1996)** proved that if the supports of the valuation distributions share the same minimum and that minimum is not a mass point, a Nash equilibrium exists for the first-price auction with an arbitrary number of bidders [Lebrun (1996), *Economic Theory*].

**Lebrun (1999)** further showed that every Bayesian equilibrium is an "essentially" pure equilibrium formed by bid functions whose inverses are solutions of a system of differential equations with boundary conditions, and proved the existence of an equilibrium for the general asymmetric \(N\)-bidder case [Lebrun (1999), *International Economic Review*].

**Maskin and Riley (2000, 2003)** established existence under the single-crossing property and finite support of valuations with positive mass at the lower endpoint. For more than two bidders, additional assumptions are needed: identical preferences for identical valuations, nonincreasing absolute risk aversion, and equal upper endpoints of supports [Maskin & Riley (2003)].

**Olszewski, Reny, and Siegel (2026)** provide the most general existence result to date in *Econometrica*. The key statistic is the **minimum high-value (mHV)** — defined as the lowest value in the support of the highest-value distribution. The standard first-price auction possesses an equilibrium whenever the mHV satisfies any one of the following conditions:
- The mHV is zero
- There is exactly one player whose value is always at least the mHV
- There are at least two players whose values always exceed the mHV
- No player's value ever exceeds the mHV

If none of these sufficient conditions hold and an equilibrium fails to exist, modifying the standard tie-breaking rule at precisely one bid — the mHV — is enough to restore equilibrium existence. The results accommodate non-quasi-linear utilities, value-distributions that contain atoms, and values that exhibit positive or negative correlation [Olszewski, Reny & Siegel (2026), *Econometrica*].

### Uniqueness Results

**Lebrun (2006)** provides the main uniqueness result in *Games and Economic Behavior*. The sufficient condition is that the cumulative distribution functions of valuations are **strictly log-concave at the highest lower extremity of their supports**. The proof uses a geometric "sliding" argument, showing that two distinct equilibria would lead to a contradiction. Uniqueness holds under three alternative conditions:
1. A binding reserve price above the highest lower extremity
2. Distinct lower extremities of supports
3. Strict log-concavity of the cdfs in a right-neighborhood of the highest lower extremity

**Maskin and Riley (2003)** prove uniqueness under the assumptions that reservation prices are drawn independently from a distribution with finite support and positive mass at the lower endpoint, and that the single-crossing property holds. For two buyers, uniqueness holds under those assumptions alone. For more than two buyers, additional assumptions are required: buyers with the same reservation price have the same preferences, absolute risk aversion is nonincreasing, and the supports of the distributions have the same upper endpoint.

**A 2026 Economics Letters paper** proves uniqueness assuming only that "valuation distributions share a common support and have continuously differentiable, strictly positive densities," without requiring log-concavity or mass points at the lower support boundary.

**Important caveat**: Kaplan and Zamir (2011) show that if the assumption that "a buyer never bids above his value" is relaxed, multiple "substantial" equilibria can exist in asymmetric first-price auctions. Although in each of these additional equilibria no buyer wins with a bid above his value, the allocation of the object and the selling price may vary among the equilibria. Such phenomena can only occur under asymmetry in the distributions of values [Kaplan & Zamir (2011), Federmann Center].

---

## Key Assumptions and Regularity Conditions

The literature establishes several key assumptions that allow for the characterization of equilibrium:

### Regularity Conditions
- **Atomless distributions**: Lebrun (1999) assumes atomless valuation distributions with a common minimum support
- **Strict log-concavity**: Lebrun (2006) requires that the value cumulative distribution functions are strictly log-concave at the highest lower extremity of their supports
- **Finite support with positive mass at lower endpoint**: Maskin and Riley (2003) assume this for their uniqueness proof
- **Common support with continuously differentiable densities**: The 2026 Economics Letters paper assumes this
- **Radon-Nikodym derivative bounded away from zero**: Olszewski, Reny, and Siegel (2026) require this regularity condition

### Monotonicity
- Equilibrium bid functions are strictly increasing in the bidder's private value (proved in the literature)
- Inverse bid functions are strictly increasing and differentiable
- Maskin and Riley (2003) establish strict monotonicity of bid distributions, differentiability of inverse bid functions, and characterization of the minimum winning bid

### Stochastic Dominance and Hazard Rate Orderings
- **Conditional Stochastic Dominance (CSD)**: Maskin and Riley (2000) use this as a stronger assumption than first-order stochastic dominance (FOSD) to compare the two bidders' value distributions
- **First-Order Stochastic Dominance (FOSD)**: Under FOSD, the stronger bidder is consistently better off but less aggressive for high valuations, and bid distributions exhibit FOSD. FOSD is necessary for bidding strategies never to cross
- **Reverse Hazard Rate Dominance**: This is sufficient for consistent aggressiveness of the weaker bidder — the weak buyer bids more aggressively than the strong buyer for all valuations
- **Low-type invariance**: For low types (valuations near 0), equilibrium bids are invariant across all distributions and coincide with the symmetric uniform case: each bidder bids approximately \((n-1)/n \cdot v\). This means low-type behavior does not depend on the distributional asymmetries [Fibich, Gavious & Sela (2002)].

---

## Key Insights from the Literature

### Bidder Preferences Over Auction Formats
One of the most robust results in the literature is that:
- **Strong bidders prefer second-price (or ascending) auctions**
- **Weak bidders prefer first-price (sealed-bid) auctions**

This holds both ex-ante and once bidders have learned their types. The proof uses the envelope theorem and a "matching function" [Maskin & Riley (2000); Kirkegaard (2009)].

### Revenue Ranking
There is **no universal revenue ranking** between first-price and second-price auctions under asymmetry:
- **First-price can be better**: When the strong bidder's distribution is shifted right or stretched, the first-price auction generates higher revenue (up to 37.2% more in numerical examples)
- **Second-price can be better**: When probability mass is shifted to the lower endpoint of the weak bidder's distribution, the open auction is superior (up to 48.5% more revenue)
- **Collusion-induced asymmetry**: First-price auctions yield higher expected revenue than English auctions under the type of asymmetry induced by collusion, because the disadvantaged coalition bids more aggressively [Marshall et al. (1994)]

### Efficiency
Asymmetric first-price auctions are **generally inefficient**: the winner of the auction may not be the person who values the object the most. The weak bidder can win when his type is slightly below the strong bidder's type because the weak bidder bids more aggressively. This inefficiency creates a motive for post-auction resale. The degree of inefficiency is \(O(\varepsilon)\) under weak asymmetry [Fibich & Gavious (2003)].

---

## Practical Steps for Implementation

For researchers who need to compute equilibrium bidding functions for arbitrary distributions, the following practical steps are recommended:

1. **Formulate the problem**: Set up the system of differential equations for the inverse bid functions with the appropriate boundary conditions.

2. **Choose a numerical method**:
   - For two bidders with common support: The boundary value method (Fibich & Gavish, 2011) or the Taylor-series expansion method (Gayle & Richard, 2008) are robust choices
   - For two bidders with different supports: The perturbation approach (Dharanan & Ellis, 2024) is specifically designed for this case
   - For more than two bidders: The forward-shooting method (Fibich & Gavish, 2012) or the Chebyshev polynomial/MPEC approach (Hubbard, Kirkegaard & Paarsch, 2013) are recommended

3. **Validate the solution**: Use theoretical checks such as the ratio of expected payoffs relative to the ratio of CDFs to verify that the numerical solution satisfies theoretical properties.

4. **Use available software**:
   - **Penn State software** (Gayle & Richard FORTRAN-90 code): Numerically calculates inverse bid functions for asymmetric IPV first-price auctions with built-in distributions (Weibull, beta, normal, lognormal) and user-defined distributions via FORTRAN subroutines
   - **Julia implementations**: Dharanan and Ellis (2024) use Julia with MIRK4 methods for their perturbation approach
   - **BIDCOMP2**: A freeware program to compute equilibrium bids and compare expected revenue

---

## Conclusion

To summarize the answer to the research brief:

1. **No general closed-form solution exists** for arbitrary continuous, strictly increasing value distributions. The system of differential equations that characterizes the equilibrium is generally intractable analytically.

2. **The general method** for characterizing the equilibrium is through the system of coupled ODEs for the inverse bid functions, with boundary conditions forming a two-point boundary value problem with a free boundary (the unknown maximum bid).

3. **Closed-form solutions exist only in special cases**: uniform distributions (Kaplan & Zamir, 2012), equal lower bounds (Plum, 1992), weak asymmetry approximations (Fibich & Gavious, 2003), and specific constructed examples.

4. **Numerical methods** are the standard approach for arbitrary distributions. The most robust methods include:
   - The boundary value method (Fibich & Gavish, 2011)
   - The dynamical-systems forward-shooting method (Fibich & Gavish, 2012)
   - The Taylor-series expansion method (Gayle & Richard, 2008)
   - The Chebyshev polynomial/MPEC approach (Hubbard, Kirkegaard & Paarsch, 2013)
   - The perturbation approach for asymmetric supports (Dharanan & Ellis, 2024)

5. **Conditions for characterization** include strict log-concavity at the lower extremity (Lebrun, 2006), first-order stochastic dominance, reverse hazard rate dominance, and conditional stochastic dominance (Maskin & Riley, 2000).

6. **Existence and uniqueness** have been established under various regularity conditions, with the most recent general existence result from Olszewski, Reny, and Siegel (2026).

---

### Sources

[1] Krishna, V. (2010). "Auction Theory," 2nd Edition, Academic Press/Elsevier. Chapter 8: "Asymmetries and Other Complications."

[2] Maskin, E. and Riley, J. (2000). "Asymmetric Auctions." *Review of Economic Studies*, 67(3), 413-438. Available at: https://www.isid.ac.in/~dmishra/topicsdoc/maskin_riley.pdf

[3] Maskin, E. and Riley, J. (2003). "Uniqueness of Equilibrium in Sealed High-Bid Auctions." Available at: https://www.ias.edu/sites/default/files/sss/papers/econpaper31.pdf

[4] Lebrun, B. (1999). "First Price Auctions in the Asymmetric N Bidder Case." *International Economic Review*, 40(1), 125-142. Available at: https://www.jstor.org/stable/2648842

[5] Lebrun, B. (1996). "Existence of an Equilibrium in First Price Auctions." *Economic Theory*, 7, 421-443. Available at: https://ideas.repec.org/a/spr/joecth/v7y1996i3p421-443.html

[6] Lebrun, B. (2006). "Uniqueness of the Equilibrium in First-Price Auctions." *Games and Economic Behavior*, 55(1), 131-151. Available at: https://www.sciencedirect.com/science/article/pii/S0899825605000540

[7] Kaplan, T.R. and Zamir, S. (2012). "Asymmetric First-Price Auctions with Uniform Distributions: Analytic Solutions to the General Case." *Economic Theory*, 50(2), 269-302. Available at: https://link.springer.com/article/10.1007/s00199-010-0563-9

[8] Kirkegaard, R. (2009). "Asymmetric First Price Auctions." *Journal of Economic Theory*. Available at: https://rene-kirkegaard.squarespace.com/s/AFPAold.pdf

[9] Marshall, R.C., Meurer, M.J., Richard, J.-F., and Stromquist, W. (1994). "Numerical Analysis of Asymmetric First Price Auctions." *Games and Economic Behavior*. Available at: https://capcp.la.psu.edu/wp-content/uploads/sites/11/numericalanalysis.pdf

[10] Gayle, W.-R. and Richard, J.-F. (2008). "Numerical Solutions of Asymmetric, First-Price, Independent Private Values Auctions." *Computational Economics*, 32(3), 245-278. Available at: https://link.springer.com/article/10.1007/s10614-008-9125-7

[11] Fibich, G. and Gavish, N. (2011). "Numerical Simulations of Asymmetric First-Price Auctions." *Games and Economic Behavior*. Available at: http://www.math.tau.ac.il/~fibich/Manuscripts/Numerical-simulations-of-asymmetric-first-price-auctions.pdf

[12] Fibich, G. and Gavish, N. (2012). "Asymmetric First-Price Auctions—A Dynamical-Systems Approach." *Mathematics of Operations Research*, 37(2), 219-243.

[13] Fibich, G. and Gavious, A. (2003). "Asymmetric First-Price Auctions: A Perturbation Approach." *Mathematics of Operations Research*, 28(4), 836-852. Available at: http://www.math.tau.ac.il/~fibich/Manuscripts/Asymmetric-first-price-auctions.pdf

[14] Fibich, G., Gavious, A., and Sela, A. (2002). "Low and High Types in Asymmetric First-Price Auctions." *Economics Letters*, 75(2), 283-287.

[15] Dharanan, G.V.A. and Ellis, C. (2024). "Asymmetric Auctions: Perturbations, ε-Equilibrium, and Equilibrium." *Games and Economic Behavior*, 147. Available at: https://www.sciencedirect.com/science/article/pii/S0899825624000848

[16] Olszewski, W., Reny, P., and Siegel, R. (2026). "Equilibrium Existence in First-Price Auctions With Private Values." *Econometrica*. Available at: https://www.econometricsociety.org/publications/econometrica/2026/01/01/Equilibrium-Existence-in-First-Price-Auctions-with-Private-Values/file/ecta70003.pdf

[17] (2026). "Uniqueness of Equilibrium in Asymmetric First-Price Auctions." *Economics Letters*, 263. Available at: https://www.sciencedirect.com/science/article/abs/pii/S0165176526001369

[18] Hubbard, T.P. and Paarsch, H.J. (2011). "On the Numerical Solution of Equilibria in Auction Models with Asymmetric Bidders." Working Paper No. 291, Collegio Carlo Alberto. Available at: https://www.carloalberto.org/wp-content/uploads/2018/11/no.291.pdf

[19] Hubbard, T.P., Kirkegaard, R., and Paarsch, H.J. (2013). "Using Economic Theory to Guide Numerical Analysis: Solving for Equilibria in Models of Asymmetric First-Price Auctions." *Computational Economics*, 42(2), 241-266.

[20] Quint, D. (2007). "Econ 805 – Advanced Micro Theory I, Lecture 9: Asymmetric Auctions." Available at: https://users.ssc.wisc.edu/~dquint/econ805%202007/econ%20805%20lecture%209.pdf

[21] Klemperer, P. (1999). "Auction Theory: A Guide to the Literature." *Journal of Economic Surveys*. Available at: https://www.cs.princeton.edu/courses/archive/spr10/cos444/papers/klemperer_guide.pdf

[22] Menezes, F. and Monteiro, P. (2005). "An Introduction to Auction Theory." Oxford University Press.

[23] Plum, M. (1992). "First Price Auctions with Asymmetric Bidders." Working Paper.

[24] Au, P.H., Banks, J., and Guo, Z. (2021). "Numerical Solution of Asymmetric Auctions." *Decision Analysis*, 18(4), 321-334.

[25] Stack Exchange (Math). "System of Differential Equations- Asymmetric First-Price Auction." Available at: https://math.stackexchange.com/questions/1385728/system-of-differential-equations-asymmetric-first-price-auction

[26] Stack Exchange (Economics). "System of Differential Equations- Asymmetric First-Price Auction." Available at: https://economics.stackexchange.com/questions/6808/system-of-differential-equations-asymmetric-first-price-auction

[27] Kaplan, T.R. and Zamir, S. (2011). "Multiple Equilibria in Asymmetric First-Price Auctions." Federmann Center for the Study of Rationality, Hebrew University.

[28] "First-Price Auctions when the Ranking of Valuations is Common Knowledge." Hebrew University Discussion Paper 117. Available at: https://ratio.huji.ac.il/files/dp117.pdf

[29] Lebrun, B. (2002). "Continuity of the First Price Auction Nash Equilibrium Correspondence." *Economic Theory*, 20, 435-453.

[30] Griesmer, J.H., Levitan, R.E., and Shubik, M. (1967). "Toward a Study of Bidding Processes, Part IV." *Naval Research Logistics Quarterly*, 14, 415-433.

[31] Vickrey, W. (1961). "Counterspeculation, Auctions, and Competitive Sealed Tenders." *Journal of Finance*, 16(1), 8-37.

[32] Bajari, P. (2001). "Comparing Competition and Collusion: A Numerical Approach." *Economic Theory*, 18, 187-205.

[33] Li, H. and Riley, J. (2007). "Auction Choice." *International Journal of Industrial Organization*, 25, 1269-1298.

[34] Athey, S. (2001). "Single Crossing Properties and the Existence of Pure Strategy Equilibria in Games of Incomplete Information." *Econometrica*, 69(4), 861-889.
