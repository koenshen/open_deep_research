# Solving Asymmetric Two-Bidder First-Price Sealed-Bid Auctions: A General Method

## 1. Overview

The first-price sealed-bid auction with two bidders whose private values are drawn from *different* distributions (ex-ante asymmetric bidders) is one of the foundational problems in auction theory. Unlike the symmetric independent private values (IPV) model—where a single differential equation yields the closed-form equilibrium bid function—the asymmetric case has no general closed-form solution. Instead, the standard method characterizes equilibrium by a **coupled system of ordinary differential equations (ODEs)** derived from each bidder's first-order condition for expected-payoff maximization. This system is almost always solved numerically (or analytically only for special distributions such as uniforms), and it must be treated as a **two-point boundary value problem** with delicate boundary conditions—especially the so-called "gap at the top" that arises when the two value distributions have different upper supports.

This report lays out (1) the theoretical framework and derivation of the coupled ODE system, (2) the standard inverse-bid-function transformation, (3) the boundary conditions, (4) existence, uniqueness, and regularity conditions, (5) the numerical methods used in practice, and (6) the key academic references that establish and extend the method.

---

## 2. The Theoretical Framework: Setup and First-Order Conditions

### 2.1 Model Setup

There are two bidders, \(i = 1, 2\). Bidder \(i\)'s private value \(v_i\) is an independent draw from a cumulative distribution function \(F_i\) with density \(f_i\) on support \([\underline{v}_i, \bar{v}_i]\). The crucial feature is that \(F_1 \neq F_2\). Both bidders are risk-neutral, the item is awarded to the highest bidder, and the winner pays his own bid. A Bayesian Nash equilibrium is a pair of strictly increasing bid functions \(\beta_1(v_1)\), \(\beta_2(v_2)\), where \(\beta_i\) maps bidder \(i\)'s value into a bid.

### 2.2 Expected Payoff and First-Order Conditions

Consider bidder 1 with value \(v_1\) who bids \(b\). Since bidder 2's equilibrium bid is \(\beta_2(v_2)\) and \(\beta_2\) is strictly increasing, bidder 1 wins whenever \(b > \beta_2(v_2)\), i.e., whenever \(v_2 < \beta_2^{-1}(b)\). Bidder 1's expected payoff is therefore [1], [2]:

\[
\Pi_1(v_1, b) = (v_1 - b) \cdot F_2(\beta_2^{-1}(b))
\]

Similarly:

\[
\Pi_2(v_2, b) = (v_2 - b) \cdot F_1(\beta_1^{-1}(b))
\]

At an interior optimum, \(b = \beta_1(v_1)\), and the first-order condition \(\partial \Pi_1/\partial b = 0\) gives:

\[
-F_2(\beta_2^{-1}(b)) + (v_1 - b) \cdot f_2(\beta_2^{-1}(b)) \cdot \frac{1}{\beta_2'(\beta_2^{-1}(b))} = 0
\]

### 2.3 The Coupled ODE System (Direct Bid Functions)

Rearranging the first-order conditions evaluated at the equilibrium bids yields the following **coupled system of ODEs** for the direct bid functions [1], [2]:

\[
\beta_1'(v_1) = \frac{F_2(\beta_2^{-1}(\beta_1(v_1)))}{f_2(\beta_2^{-1}(\beta_1(v_1)))} \cdot \frac{\beta_2'(\beta_2^{-1}(\beta_1(v_1)))}{v_1 - \beta_1(v_1)}
\]

\[
\beta_2'(v_2) = \frac{F_1(\beta_1^{-1}(\beta_2(v_2)))}{f_1(\beta_1^{-1}(\beta_2(v_2)))} \cdot \frac{\beta_1'(\beta_1^{-1}(\beta_2(v_2)))}{v_2 - \beta_2(v_2)}
\]

The system is *coupled* because each equation involves the other bidder's bid function and its inverse. This is the direct characterization used throughout the literature. However, solving the system in this form is awkward because the two functions are defined on different domains (their own value supports) but linked through their inverse images at common bid levels.

---

## 3. The Inverse Bid Function Transformation

### 3.1 Definition

The standard and much more tractable approach—used by Maskin and Riley, Lebrun, and virtually all numerical implementations—is to work with the **inverse bid functions** [1], [2], [3]:

\[
\phi_1(b) = \beta_1^{-1}(b), \qquad \phi_2(b) = \beta_2^{-1}(b)
\]

These give the value of the bidder who submits bid \(b\) in equilibrium. Both inverse functions are defined on the *common* interval of bids \([\underline{b}, \bar{b}]\), which makes the system far easier to handle, especially numerically.

### 3.2 The ODE System in Inverse Form

Since \(\beta_i'(\phi_i(b)) = 1/\phi_i'(b)\), substituting into the first-order conditions and rewriting at the common bid level \(b\) yields the **inverse ODE system** [1], [2], [3]:

\[
\phi_1'(b) = \frac{F_2(\phi_2(b))}{f_2(\phi_2(b))} \cdot \frac{1}{\phi_1(b) - b}
\]

\[
\phi_2'(b) = \frac{F_1(\phi_1(b))}{f_1(\phi_1(b))} \cdot \frac{1}{\phi_2(b) - b}
\]

Or, using the reverse hazard rate \(\lambda_i(v) = f_i(v)/F_i(v)\) [2]:

\[
\phi_1'(b) = \frac{1}{\lambda_2(\phi_2(b))} \cdot \frac{1}{\phi_1(b) - b}, \qquad
\phi_2'(b) = \frac{1}{\lambda_1(\phi_1(b))} \cdot \frac{1}{\phi_2(b) - b}
\]

This system appears in Maskin and Riley's "Asymmetric Auctions" [1] and is the central object in Lebrun's characterization of equilibrium [3], [4]. In Lebrun's formulation for \(n\) bidders, the system generalizes to:

\[
v_i'(b) = \frac{F_i(v_i(b))}{f_i(v_i(b))} \left( \frac{1}{n-1} \sum_{j} \frac{1}{v_j(b) - b} - \frac{1}{v_i(b) - b} \right)
\]

which reduces to the two-bidder system above [5].

### 3.3 Why This Form Is Standard

The inverse transformation has three major advantages [2], [6]:

1. **Fixed common domain**: Both \(\phi_1\) and \(\phi_2\) are defined on the same bid interval \([\underline{b}, \bar{b}]\), which is essential for numerical solution methods.
2. **Simpler structure**: The right-hand sides no longer contain the other bidder's derivative; the coupling is only through the values \(\phi_j(b)\).
3. **Transparent boundary conditions**: The endpoint conditions (especially at the top, see Section 4) become simple equalities of valuations.

---

## 4. Boundary Conditions

### 4.1 The Lower Boundary: "No Gap at the Bottom"

At the lowest possible valuations, the standard condition is that the lowest participating type bids his own value, earning zero expected surplus. If the lower supports coincide, \(\underline{v}_1 = \underline{v}_2 = \underline{v}\), then [2], [6]:

\[
\beta_1(\underline{v}) = \beta_2(\underline{v}) = \underline{v}, \qquad \phi_1(\underline{b}) = \phi_2(\underline{b}) = \underline{v}, \qquad \underline{b} = \underline{v}
\]

If the lower supports differ or a binding reserve price \(r\) exists, the effective lower bound of the bid interval is \(\underline{b} = \max(\underline{v}_1, \underline{v}_2, r)\). Lebrun emphasizes that the system is "very poorly behaved" at this lower endpoint—the derivative terms diverge—which is a key source of numerical difficulty [6], [7]. Technically, the system has a **singularity at the origin**, and standard initial-value-problem (IVP) solvers cannot simply be started there [7], [8].

### 4.2 The Upper Boundary: The "Gap at the Top" When Supports Differ

The subtle part of the boundary conditions concerns the upper endpoints. Suppose \(\bar{v}_1 > \bar{v}_2\), so bidder 1's distribution has a higher upper support than bidder 2's. Then bidder 2 is "constrained" at the top, and the equilibrium exhibits a form of **bunching or pooling**: the maximum bid submitted by both bidders is the same, \(\bar{b}\), but it is generated by different valuations [1], [2], [6]:

\[
\phi_1(\bar{b}) = \phi_2(\bar{b}) = \bar{v}_2
\]

That is, bidder 1's types in the interval \((\bar{v}_2, \bar{v}_1]\) **all submit the same maximum bid** \(\bar{b} = \beta_2(\bar{v}_2)\). The maximum bid \(\bar{b}\) is endogenous and must be solved for as part of the boundary value problem—it is not known in advance [2], [6]. Maskin and Riley explain that when the strong buyer's distribution is shifted rightward, the strong buyer shades his bid more, and the highest type of the weaker bidder determines the top bid [1].

This phenomenon is sometimes called the "gap at the top" or "bid separation / bid bifurcation." Hubbard and Kirkegaard study it systematically in auctions where bidders have different type supports, showing that when supports differ, bidders from different groups may submit bids over different supports, so they do not share a common maximum bid [9], [10]. In the two-bidder case, the standard resolution is that the bidder with the higher upper support pools at the top with the constrained bidder's maximum bid.

### 4.3 Summary: A Two-Point Boundary Value Problem

The equilibrium is therefore characterized by the inverse ODE system (Section 3.2) together with [2], [6], [8]:

- **Left boundary**: \(\phi_1(\underline{b}) = \underline{v}_1\), \(\phi_2(\underline{b}) = \underline{v}_2\), where \(\underline{b} = \max(\underline{v}_1, \underline{v}_2)\) (or the reserve price).
- **Right boundary**: if \(\bar{v}_1 > \bar{v}_2\), then \(\phi_1(\bar{b}) = \phi_2(\bar{b}) = \bar{v}_2\), with \(\bar{b}\) determined endogenously.

Because the value at any interior point depends on boundary conditions at *both* ends, this is inherently a **two-point boundary value problem**, and IVP solvers that use only one boundary condition are inappropriate in principle [8].

---

## 5. Existence, Uniqueness, and Regularity Conditions

### 5.1 Existence

Existence of a Bayesian Nash equilibrium in asymmetric first-price auctions was established by **Lebrun (1999)** in "First Price Auctions in the Asymmetric N Bidder Case," published in the *International Economic Review* [3]. Lebrun proved that:

- Every Bayesian equilibrium is an "essentially" pure equilibrium formed by bid functions whose inverses solve the system of differential equations with the boundary conditions described above [3].
- Existence holds for arbitrary numbers of bidders with heterogeneous value distributions [3].

### 5.2 Uniqueness

Uniqueness is more delicate and has a layered history:

- **Lebrun (1999)** proved uniqueness when the valuation distributions have a **mass point at the lower extremity** of their support, and gave sufficient conditions when all distributions are one of two atomless distributions [3].
- **Maskin and Riley (2003)**, "Uniqueness of Equilibrium in Sealed High-Bid Auctions," proved uniqueness for two bidders under fairly general conditions (with additional assumptions required for \(n > 2\)), using the Fundamental Theorem of ODEs applied to the inverse-bid system [11].
- **Lebrun (2006)**, "Uniqueness of the Equilibrium in First-Price Auctions," *Games and Economic Behavior*, proved uniqueness when the value CDFs are **strictly log-concave at the highest lower extremity of their supports**—i.e., the reverse hazard rate \(f_i/F_i\) is strictly decreasing near the lower boundary. The proof uses a geometric "sliding" argument and covers both common and different upper supports [4], [12].
- **Tumenjargal (2026)**, "Uniqueness of equilibrium in asymmetric first-price auctions," *Economics Letters*, proves uniqueness under weaker assumptions: only that the valuation distributions have **common support with continuously differentiable, strictly positive densities**—no mass points and no log-concavity required. The proof uses a "shifting argument" that avoids the divergence difficulties at the lower boundary in the atomless case [13].

### 5.3 Regularity Conditions

The standard regularity conditions underlying these characterizations are [3], [4], [13]:

- Value distributions are atomless with connected (interval) supports \([\underline{v}_i, \bar{v}_i]\).
- CDFs \(F_i\) are differentiable, with densities \(f_i\) locally bounded away from zero on the interior of the supports.
- The inverse hazard rate conditions (e.g., strict log-concavity of the CDF near the lower boundary) hold for uniqueness in the atomless case without mass points.
- Equilibrium bid functions are strictly increasing under these conditions, so the inverse transformation is well defined.

A weaker uniqueness assumption was recently established by Tumenjargal (2026), who proves that common support plus continuously differentiable, strictly positive densities suffice for uniqueness—no log-concavity or mass points needed [13].

### 5.4 Caveats: Non-Standard Equilibria and Bid Bifurcation

Two important caveats qualify the uniqueness results:

1. **Non-standard equilibria**: Kaplan and Zamir (2011) show that if one relaxes the standard assumption that bidders never bid above their values, asymmetric first-price auctions admit additional "substantial" equilibria in which bidders sometimes bid above their values (though never winning with such bids). These can produce different allocations and prices [14]. The standard uniqueness theorems (Maskin–Riley, Lebrun) rely on ruling out overbidding, so confidence in a unique equilibrium requires maintaining that assumption.

2. **Bid bifurcation / bid separation**: When bidders have different upper supports, equilibrium behavior changes qualitatively—bidders may submit bids over different intervals, and the maximum bids of the two groups are mechanically linked. Hubbard and Kirkegaard show that this "bid bifurcation" becomes more likely as the number of bidders grows and as bidders become "stronger" in terms of their reverse hazard rates, and they provide a method to reduce the dimensionality of the problem in such cases [9], [10]. For the two-bidder case, the standard treatment is the "pooling at the top" described in Section 4.2.

---

## 6. Closed-Form Solutions and When They Exist

For **arbitrary** distributions \(F_1, F_2\), no closed-form solution exists; the coupled ODE system must be solved numerically. Closed-form solutions are available only for special parametric families:

- **Symmetric case** (\(F_1 = F_2\)): the system decouples and yields the classical result; e.g., for two bidders with values uniform on \([0,1]\), \(\beta(v) = v/2\) [15].
- **Uniform distributions on different intervals**: **Kaplan and Zamir (2012)**, "Asymmetric First-Price Auctions with Uniform Distributions: Analytic Solutions to the General Case," *Economic Theory*, provides analytic solutions for two bidders with values uniform on \([\underline{v}_1, \bar{v}_1]\) and \([\underline{v}_2, \bar{v}_2]\), with and without a binding minimum bid—a problem originally posed by Vickrey in 1961 [16]. They identify classes of linear equilibrium bid functions (e.g., \(b_1(v) = v/2 + m/2\), \(b_2(v) = v/2 + m/4\) under specific parameter conditions) and provide the first known example where bid functions cross despite one distribution stochastically dominating the other [16].
- **Other parametric families**: Plum (1992) provided explicit solutions for a parametric class of distributions used in experimental work (e.g., Güth, Ivanova-Stenzel, and Wolfstetter, 2005, use the Plum class with supports \([50, 150]\) and \([50, 200]\)) [17].

- **Perturbation/small-asymmetry results**: Lebrun (2009), "Auctions with almost homogeneous bidders," shows that around the symmetric case, the equilibrium is jointly differentiable in bidder-specific parameters, and revenue equivalence between first- and second-price auctions holds to first order in the size of the asymmetry [18].

Outside these cases, numerical methods are required.

---

## 7. Numerical Methods

Because the coupled ODE system is a nonlinear two-point boundary value problem with a singularity at the lower endpoint, specialized numerical techniques are required. The literature has developed several approaches.

### 7.1 Backward (Reverse) Shooting Method

The classic approach, introduced by **Marshall, Meurer, Richard, and Stromquist (MMRS, 1994)** in "Numerical Analysis of Asymmetric First Price Auctions" (*Games and Economic Behavior*), is **backward shooting** [6], [19]:

- Guess the unknown terminal point \(\bar{b}\) (the maximum bid, which is endogenous).
- Integrate the inverse-ODE system **backward** from \(\bar{b}\) using the upper boundary condition \(\phi_1(\bar{b}) = \phi_2(\bar{b}) = \bar{v}_2\) (or the appropriate common upper support).
- Check whether the computed solution satisfies the lower boundary condition \(\phi_i(\underline{b}) = \underline{v}_i\); iterate on \(\bar{b}\) until it does.

MMRS implement this using backward Taylor-series expansions, noting that forward integration fails because of "nuisance linear solutions acting as attractors" near the origin [6], [19]. Their recommendation: "systems of differential equations such as those consisting of Eqs. (2) and (3) should be solved backward starting from an assumed terminal point using the initial condition (4) as an indicator of whether or not we have used the correct value for \(t^*\)" [6], [19].

**However**, **Fibich and Gavish (2011)** proved that the backward-shooting method is **inherently unstable**, and that this instability cannot be eliminated by changing the numerical methodology of the backward solver. The instability worsens as the number of bidders increases [20], [21].

### 7.2 Boundary-Value Methods

Fibich and Gavish (2011), "Numerical simulations of asymmetric first-price auctions," *Games and Economic Behavior*, propose a **novel boundary-value method** as a robust alternative [20], [21]:

- Change the independent variable from the bid \(b\) to one bidder's value \(v_n\), placing the system on a **fixed domain** (e.g., \([0,1]\)).
- Solve the resulting nonlinear system on the fixed domain using fixed-point iterations (converging linearly in 25–50 iterations) or Newton's method (converging quadratically).
- The method handles reserve prices by transforming the system so the left boundary no longer has infinite derivatives.
- It works for any number of players and for mixed types of distributions, including distributions with multiple crossings [20], [21].

Nir Gavish provides MATLAB code implementing this method on his website [22].

### 7.3 Taylor-Series Expansion Methods

**Gayle (2004)** and **Gayle and Richard (2008)** develop fully automated algorithms using recursive piecewise low-order Taylor-series expansions to solve the inverse-bid ODE system [7], [23]:

- The system is solved backward from an assumed terminal point, with the endpoint found via a simplex search.
- The transformation \(l_i(t) = F_i(\phi_i(t))\) is used to reduce dimensionality and improve numerical stability [7].
- Accuracy depends on grid fineness (500–10,000 points) and Taylor-series order (2–5).
- The algorithms accommodate user-supplied distributions (analytical or tabulated) via automatic B-spline interpolation, and compute expected revenues, winning probabilities, and reservation probabilities under reserve pricing.
- A pointwise best-response verification checks numerical accuracy [7], [23].

### 7.4 Polynomial Approximation of Inverse Bid Functions

**Hubbard, Kirkegaard, and Paarsch (2013)**, "Using Economic Theory to Guide Numerical Analysis: Solving for Equilibria in Models of Asymmetric First-Price Auctions," *Computational Economics*, approximate the inverse-bid functions with polynomials, using theoretical results both to solve for the polynomial coefficients and to evaluate the quality of the approximation [24]. Their key warning: **low-degree polynomial approximations perform poorly and can lead to incorrect policy recommendations** regarding auction design, so researchers must take care to obtain high-quality numerical solutions [24].

### 7.5 Perturbation Methods for Asymmetric Supports

**Dharanan et al. (2022)**, "Equilibrium in Asymmetric Auctions," identify a critical flaw in the direct characterization approach when bidders' valuation supports are asymmetric: the problem reduces to an **ill-posed differential-algebraic equations (DAE) problem** that cannot be solved numerically [8]. They develop a **perturbation method**:

- Approximate the auction with asymmetric supports by a sequence of auctions with common support.
- Prove that the limit of equilibria of the perturbed games is the equilibrium of the limit game (their Theorem 1), and that the equilibrium of the perturbed game is an \(\varepsilon\)-BNE of the original auction (their Theorem 4).
- Characterize the equilibrium as continuous and piecewise differentiable [8].

They emphasize that because the problem is a genuine two-point BVP, **specialized BVP solvers (e.g., MIRK 4) are necessary**—standard IVP solvers or shooting methods are inappropriate in principle [8].

### 7.6 Discrete-Distribution Algorithms

**Wang, Shen, and Zuo (2020)** provide an efficient algorithm for the discrete-value case that avoids ODEs entirely, using a "bidding set" backward-shooting procedure. It is substantially faster and more accurate than continuous-approximation methods, and uniqueness holds without the technical log-concavity assumptions required in continuous settings [25].

### 7.7 Practical Guidance

The current state of practice for the two-bidder asymmetric problem is:

1. Formulate the equilibrium as the inverse-ODE system (Section 3.2).
2. Treat it as a two-point boundary value problem with the boundary conditions of Section 4.
3. Use either the backward-shooting method with Taylor expansions (MMRS-style) or, preferably, a modern boundary-value method (Fibich–Gavish style), finite-difference BVP solvers, or the perturbation approach for asymmetric supports.
4. Validate the solution with pointwise best-response checks [7], [24].

---

## 8. Key References in the Literature

The following papers and books constitute the core literature establishing and extending the general solution method for asymmetric first-price auctions:

1. **Maskin and Riley (2000), "Asymmetric Auctions," *Review of Economic Studies* 67(3), 413–438.** The seminal paper. Establishes the equilibrium characterization via inverse bid functions and the coupled differential equation system; proves the strong buyer shades more, the strong buyer prefers open auctions while the weak buyer prefers sealed high-bid auctions; analyzes revenue ranking ("Getty effect"); provides formal propositions (3.3–3.5) and numerical examples with revenue differences from 6% to 48% [1].

2. **Lebrun (1999), "First Price Auctions in the Asymmetric N Bidder Case," *International Economic Review* 40(1), 125–142.** Proves existence of Bayesian equilibrium; characterizes all equilibria as "essentially pure" with inverses solving the differential system with boundary conditions; proves uniqueness with mass points at the lower extremity; establishes stochastic-dominance inequalities between strategies [3].

3. **Lebrun (2006), "Uniqueness of the Equilibrium in First-Price Auctions," *Games and Economic Behavior* 55(1), 131–151.** Proves uniqueness under strict log-concavity of the value CDFs near the highest lower extremity of the supports, using a geometric "sliding" argument; extends the result to different lower and upper extremities [4], [12].

4. **Maskin and Riley (2003), "Uniqueness of Equilibrium in Sealed High-Bid Auctions."** Proves uniqueness for two buyers under general conditions by applying the Fundamental Theorem of ODEs to the inverse-bid system [11].

5. **Krishna (2009), *Auction Theory*, 2nd ed., Academic Press.** The standard textbook treatment; Chapter 4 ("Asymmetries and Other Complications") derives the coupled ODE system, the inverse-bid transformation, and the boundary conditions [2].

6. **Marshall, Meurer, Richard, and Stromquist (1994), "Numerical Analysis of Asymmetric First Price Auctions," *Games and Economic Behavior* 7, 193–220.** Introduces the backward Taylor-series expansion algorithm for solving the system; analyzes collusion-induced asymmetries; shows the more optimistic bidder shades more [6], [19].

7. **Fibich and Gavish (2011), "Numerical Simulations of Asymmetric First-Price Auctions," *Games and Economic Behavior* 73(2), 479–495.** Proves the backward-shooting method is inherently unstable; introduces a robust boundary-value method solvable on a fixed domain; demonstrates performance for auctions with hundreds of players [20], [21].

8. **Kaplan and Zamir (2012), "Asymmetric First-Price Auctions with Uniform Distributions: Analytic Solutions to the General Case," *Economic Theory* 50(2), 269–302.** Solves the Vickrey (1961) problem analytically for uniform distributions on different intervals, with or without a binding minimum bid; provides the first example of crossing bid functions under stochastic dominance [16].

9. **Gayle and Richard (2008), "Numerical Solutions of Asymmetric, First-Price, Independent Private Values Auctions," *Computational Economics* 32(3), 245–278.** Fully automated Taylor-series algorithm for arbitrary numbers of bidders, heterogeneous distributions, coalitions, and reserve prices [7], [23].

10. **Bajari (2001), "Comparing Competition and Collusion: A Numerical Approach," *Economic Theory* 18(1), 187–205.** Describes three algorithms for computing inverse equilibrium bid functions in asymmetric procurement auctions; uses them to compare competitive and collusive bidding and to assess damages from bid-rigging [5].

11. **Hubbard, Kirkegaard, and Paarsch (2013), "Using Economic Theory to Guide Numerical Analysis: Solving for Equilibria in Models of Asymmetric First-Price Auctions," *Computational Economics* 42, 241–266.** Polynomial approximation of inverse-bid functions; warns that low-degree approximations perform poorly; proposes payoff-ratio checks for solution quality [24].

12. **Hubbard and Kirkegaard (2015), "Asymmetric Auctions with More Than Two Bidders."** Introduces and analyzes "bid bifurcation" when bidders have different type supports; provides a dimensionality-reduction method and precise conditions for the uniform case [9].

13. **Kirkegaard (2006, 2009), "A Simple Approach to Analyzing Asymmetric First Price Auctions"; "Asymmetric First Price Auctions," *Journal of Economic Theory* 144(4), 1617–1635.** Develops an approach based on winning probabilities and payoff ratios rather than bid functions directly, simplifying analysis and producing new comparative statics (weak bidders bid more aggressively under reverse hazard rate dominance; FOSD is necessary for bid functions not to cross) [26], [27].

14. **Tumenjargal (2026), "Uniqueness of Equilibrium in Asymmetric First-Price Auctions," *Economics Letters* 263.** Proves uniqueness under the minimal assumptions of common support and continuously differentiable, strictly positive densities—no log-concavity or mass points required [13].

15. **Dharanan et al. (2022), "Equilibrium in Asymmetric Auctions."** Identifies the ill-posed nature of the direct characterization when supports are asymmetric; develops a perturbation method with convergence theorems; recommends specialized BVP solvers [8].

16. **Kaplan and Zamir (2011), "Multiple Equilibria in Asymmetric First-Price Auctions."** Shows that relaxing the no-overbidding assumption admits additional "substantial" equilibria in asymmetric auctions [14].

17. **Vickrey (1961), "Counterspeculation, Auctions, and Competitive Sealed Tenders," *Journal of Finance* 16(1), 8–37.** The founding paper of auction theory; poses the asymmetric uniform-distribution problem later solved by Kaplan and Zamir [16], [28].

18. **Myerson (1981), "Optimal Auction Design," *Mathematics of Operations Research* 6(1), 58–73.** Establishes the mechanism-design framework (revelation principle, revenue-equivalence theorem, virtual valuations) underlying the modern analysis of asymmetric auctions [29].

19. **Mares and Swinkels (2014), "On the Analysis of Asymmetric First Price Auctions," *Journal of Economic Theory* 152, 1–40.** Provides new tools connecting equilibria to the \(\rho\)-concavity of type distributions; shows each bidder's bid-function slope equals 1 minus the local \(\rho\)-concavity of interim expected surplus [30].

20. **Campo, Perrigne, and Vuong (2003) and Campo, Guerre, Perrigne, and Vuong (2011).** The econometric side of the literature: derive the differential equations for asymmetric affiliated private values, rewrite them in terms of observed bid distributions, and establish identification and semiparametric estimation of asymmetric first-price auction models [31], [32].

21. **Cantillon (2008), "The Effect of Bidders' Asymmetries on Expected Revenue in Auctions," *Games and Economic Behavior* 62(1), 1–25.** Shows the expected revenue from a symmetric "benchmark" auction always dominates that from the asymmetric auction, formalizing the idea that asymmetry reduces competition [33].

---

## 9. Conclusion

The general method for solving a first-price sealed-bid auction with two ex-ante asymmetric bidders is well established:

1. **Derive the coupled ODE system** from each bidder's first-order condition for expected-payoff maximization—either for the direct bid functions \(\beta_1, \beta_2\), or, more usefully, for the inverse bid functions \(\phi_1(b) = \beta_1^{-1}(b)\), \(\phi_2(b) = \beta_2^{-1}(b)\), which live on the common bid interval and take the symmetric tractable form \(\phi_i'(b) = [F_j(\phi_j(b))/f_j(\phi_j(b))] \cdot 1/(\phi_i(b) - b)\).

2. **Complete the system with boundary conditions**: at the bottom, the lowest effective type bids his value (no gap); at the top, if the upper supports differ, the bidder with the higher support pools at the maximum bid set by the constrained bidder (the "gap at the top"), with the maximum bid determined endogenously. The problem is therefore a genuine two-point boundary value problem.

3. **Impose regularity conditions** for existence and uniqueness: atomless distributions with interval supports and positive densities; for uniqueness without mass points, strict log-concavity of the CDFs near the lower boundary (Lebrun 2006) or, under the weakest assumptions to date, only common support with continuously differentiable strictly positive densities (Tumenjargal 2026).

4. **Solve numerically** in general: backward-shooting with Taylor expansions (MMRS 1994; Gayle–Richard 2008), modern boundary-value methods (Fibich–Gavish 2011), polynomial approximation of inverse bid functions (Hubbard–Kirkegaard–Paarsch 2013), perturbation methods for asymmetric supports (Dharanan et al. 2022), or analytic solutions in the special uniform case (Kaplan–Zamir 2012).

5. **Consult the core references**: Maskin and Riley (2000) and Lebrun (1999, 2006) for the theory; Krishna (2009) for the textbook treatment; Marshall et al. (1994), Fibich and Gavish (2011), Gayle and Richard (2008), and Hubbard, Kirkegaard, and Paarsch (2013) for numerical methods.

The method is fully general: it accommodates arbitrary (well-behaved) distribution pairs, different supports, reserve prices, and even coalitions/asymmetric groups, and it is the foundation for both theoretical revenue comparisons and structural econometric estimation of asymmetric auctions.

---

### Sources

[1] Maskin, E. and Riley, J. (2000), "Asymmetric Auctions," *Review of Economic Studies* 67(3), 413–438: http://www.econ.ucla.edu/riley/research/asyRES.PDF

[2] Krishna, V. (2009), *Auction Theory*, 2nd ed., Academic Press: https://books.google.com/books/about/Auction_Theory.html?id=qW1128ktG1gC

[3] Lebrun, B. (1999), "First Price Auctions in the Asymmetric N Bidder Case," *International Economic Review* 40(1), 125–142: https://ideas.repec.org/a/ier/iecrev/v40y1999i1p125-42.html

[4] Lebrun, B. (2006), "Uniqueness of the Equilibrium in First-Price Auctions," *Games and Economic Behavior* 55(1), 131–151: https://www.sciencedirect.com/science/article/pii/S0899825605000540

[5] Bajari, P. (2001), "Comparing Competition and Collusion: A Numerical Approach," *Economic Theory* 18(1), 187–205: https://ideas.repec.org/a/spr/joecth/v18y2001i1p187-205.html

[6] Marshall, R.C., Meurer, M.J., Richard, J.-F., and Stromquist, W. (1994), "Numerical Analysis of Asymmetric First Price Auctions," *Games and Economic Behavior* 7, 193–220: https://capcp.la.psu.edu/wp-content/uploads/sites/11/numericalanalysis.pdf

[7] Gayle, W.-R. (2004), "Numerical Analysis of Asymmetric First Price Auctions with Reserve Prices": http://repec.org/sce2005/up.18137.1108489875.pdf

[8] Dharanan, G.V.A. et al. (2022), "Equilibrium in Asymmetric Auctions": https://www.isid.ac.in/~epu/acegd2022/papers/G_V_A_Dharanan.pdf

[9] Hubbard, T.P. and Kirkegaard, R. (2015), "Asymmetric Auctions with More Than Two Bidders": https://www.uoguelph.ca/economics/repec/workingpapers/2015/2015-02.pdf

[10] Hubbard, T.P. and Kirkegaard, R. (2019), "Bid-Separation in Asymmetric Auctions": https://static1.squarespace.com/static/5594040ce4b0cd95241433b7/t/5d4af694a426880001550589/1565193878442/BidSeparationAugust2019.pdf

[11] Maskin, E. and Riley, J. (2003), "Uniqueness of Equilibrium in Sealed High-Bid Auctions": https://www.ias.edu/sites/default/files/sss/papers/econpaper31.pdf

[12] Lebrun, B. (2004), "Uniqueness of the Equilibrium in First-Price Auctions," York University Working Paper: https://econ.laps.yorku.ca/files/2015/10/lebrunb-u.pdf

[13] Tumenjargal, E. (2026), "Uniqueness of Equilibrium in Asymmetric First-Price Auctions," *Economics Letters* 263: https://www.sciencedirect.com/science/article/abs/pii/S0165176526001369

[14] Kaplan, T.R. and Zamir, S. (2011), "Multiple Equilibria in Asymmetric First-Price Auctions": https://mpra.ub.uni-muenchen.de/34937/1/MPRA_paper_34937.pdf

[15] Vickrey, W. (1961), "Counterspeculation, Auctions, and Competitive Sealed Tenders," *Journal of Finance* 16(1), 8–37: https://cramton.umd.edu/market-design-papers/vickrey-counterspeculation-auctions-and-competitive-sealed-tenders.pdf

[16] Kaplan, T.R. and Zamir, S. (2012), "Asymmetric First-Price Auctions with Uniform Distributions: Analytic Solutions to the General Case," *Economic Theory* 50(2), 269–302: https://ideas.repec.org/a/spr/joecth/v50y2012i2p269-302.html

[17] Güth, W., Ivanova-Stenzel, R., and Wolfstetter, E. (2005), "Bidding Behavior in Asymmetric Auctions: An Experimental Study," *European Economic Review* 49(7), 1891–1913: https://www.sciencedirect.com/science/article/abs/pii/S0014292104000753

[18] Lebrun, B. (2009), "Auctions with Almost Homogeneous Bidders," *Journal of Economic Theory* 144(3), 1341–1351: https://ideas.repec.org/a/eee/jetheo/v144y2009i3p1341-1351.html

[19] Marshall, R.C., Meurer, M.J., Richard, J.-F., and Stromquist, W. (1994), "Numerical Analysis of Asymmetric First Price Auctions," *Games and Economic Behavior* 7: https://capcp.la.psu.edu/wp-content/uploads/sites/11/numericalanalysis.pdf

[20] Fibich, G. and Gavish, N. (2011), "Numerical Simulations of Asymmetric First-Price Auctions," *Games and Economic Behavior* 73(2), 479–495: https://www.sciencedirect.com/science/article/pii/S0899825611000509

[21] Fibich, G. and Gavish, N., "Numerical Simulations of Asymmetric First-Price Auctions," Tel Aviv University manuscript: http://www.math.tau.ac.il/~fibich/Manuscripts/Numerical-simulations-of-asymmetric-first-price-auctions.pdf

[22] Gavish, N., MATLAB codes for asymmetric first-price auctions: https://ngavish.net.technion.ac.il/matlab-code-for-asymmetric-first-price-auctions

[23] Gayle, W.-R. and Richard, J.-F. (2008), "Numerical Solutions of Asymmetric, First-Price, Independent Private Values Auctions," *Computational Economics* 32(3), 245–278: https://link.springer.com/article/10.1007/s10614-008-9125-7

[24] Hubbard, T.P., Kirkegaard, R., and Paarsch, H.J. (2013), "Using Economic Theory to Guide Numerical Analysis: Solving for Equilibria in Models of Asymmetric First-Price Auctions," *Computational Economics* 42, 241–266: https://link.springer.com/article/10.1007/s10614-012-9333-z

[25] Wang, Z., Shen, W., and Zuo, S. (2020), "Bayesian Nash Equilibrium in First-Price Auction with Discrete Value Distributions," AAMAS 2020: http://ai.ruc.edu.cn/uploads/20210806/9cfc7d231ac6d0e488a3667763f5011b.pdf

[26] Kirkegaard, R. (2006), "A Simple Approach to Analyzing Asymmetric First Price Auctions," Brock University Working Paper No. 0504: https://brocku.ca/repec/pdf/0504.pdf

[27] Kirkegaard, R. (2009), "Asymmetric First Price Auctions," *Journal of Economic Theory* 144(4), 1617–1635: https://www.sciencedirect.com/science/article/pii/S0022053109000295

[28] Vickrey, W. (1961), "Counterspeculation, Auctions, and Competitive Sealed Tenders," *Journal of Finance* 16(1): https://ideas.repec.org/a/bla/jfinan/v16y1961i1p8-37.html

[29] Myerson, R.B. (1981), "Optimal Auction Design," *Mathematics of Operations Research* 6(1), 58–73: https://www.math.utoronto.ca/mccann/assignments/477/Myerson81.pdf

[30] Mares, V. and Swinkels, J.M. (2014), "On the Analysis of Asymmetric First Price Auctions," *Journal of Economic Theory* 152, 1–40: https://www.sciencedirect.com/science/article/abs/pii/S0022053114000507

[31] Campo, S., Perrigne, I., and Vuong, Q.H. (2003), "Asymmetry in First-Price Auctions with Affiliated Private Values," *Journal of Applied Econometrics* 18(2), 179–207: https://ideas.repec.org/a/jae/japmet/v18y2003i2p179-207.html

[32] Campo, S., Guerre, E., Perrigne, I., and Vuong, Q. (2011), "Semiparametric Estimation of First-Price Auctions with Risk-Averse Bidders," *Review of Economic Studies* 78(1), 112–147: https://academic.oup.com/restud/article-abstract/78/1/112/1533004

[33] Cantillon, E. (2008), "The Effect of Bidders' Asymmetries on Expected Revenue in Auctions," *Games and Economic Behavior* 62(1), 1–25: https://ideas.repec.org/a/eee/gamebe/v62y2008i1p1-25.html
