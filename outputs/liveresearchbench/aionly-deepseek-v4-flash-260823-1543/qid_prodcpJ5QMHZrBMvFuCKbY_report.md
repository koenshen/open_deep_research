# Payment Platform Comparison for US E-Commerce (2026): Stripe, PayPal, Square, Braintree, Adyen, Shopify Payments, 2Checkout (Verifone), Amazon Pay, and Apple Pay

## 1. Introduction and Framing

This report compares nine payment platforms for US-based small-to-medium e-commerce businesses as of August 2026, across nine dimensions: integration capabilities, fees, international support, setup, payment methods, fraud/security, customer support, scalability, and overall suitability. All fees are in US dollars for US-based businesses.

A structural distinction matters from the outset. Six of the platforms — **Stripe, PayPal, Square, Braintree, Adyen, and 2Checkout/Verifone** — are full payment processors (or processor + gateway combinations) that can serve as a merchant's primary payments stack. **Shopify Payments** is a full processor but is exclusive to the Shopify platform. **Amazon Pay** is a consumer wallet that processes transactions routed through it and charges its own fee, but it is typically layered on top of a primary processor. **Apple Pay** is explicitly *not* a payment processor — it is a wallet/checkout method that requires an underlying processor or gateway (e.g., Stripe, Adyen, Braintree) to function, and Apple charges merchants no fee of its own [20][9].

---

## 2. Platform Overviews

### 2.1 Stripe
Stripe is a developer-first payments platform offering a full-stack API, hosted checkout, payment links, and 18+ APIs with 11 official SDKs. Standard US online card rate is **2.9% + $0.30**, with no monthly fees. Stripe operates in 46 fully supported countries and supports charging customers in over 135 currencies [1][10][25].

### 2.2 PayPal
PayPal is the most widely recognized consumer wallet and a full processor, operating in ~200 markets with 439 million active accounts as of year-end 2025. US rates are **2.99% + $0.49** for standard card payments and **3.49% + $0.49** for PayPal Checkout/wallet transactions. PayPal owns Braintree and also serves as an additional card processor for Shopify Payments under a 2024 expanded partnership [2][66][14].

### 2.3 Square
Square (Block, Inc.) is an omnichannel payments ecosystem combining POS hardware, online payments, banking, payroll, and e-commerce tools. Online card-not-present rates range from **3.3% + $0.30** on the Free plan to **2.9% + $0.30** on Plus ($49/month) and Premium ($149/month) plans. Square operates in only 8 countries, limiting international reach [3][22].

### 2.4 Braintree
Braintree, a PayPal subsidiary, is a developer-focused gateway + merchant account provider offering a Drop-in UI, Hosted Fields, and a full GraphQL API. The current published US card rate is **2.89% + $0.29** (as of May 7, 2026), with interchange-plus pricing available for established merchants. Braintree supports cards plus PayPal, Venmo, Apple Pay, and Google Pay through a single integration [21][4][16].

### 2.5 Adyen
Adyen is a global processor-and-acquirer serving large enterprises (Uber, Spotify, eBay). It uses **interchange-plus pricing** in the US (Visa/Mastercard: ~$0.13 + Interchange++ + 0.60%) with no monthly fees, but a minimum monthly invoice applies (~€1,000+), and reported qualification thresholds are high (~$500K/month). Adyen operates in 70+ countries and supports 150+ currencies [5][15][61].

### 2.6 Shopify Payments
Shopify Payments is Shopify's native payment processor, available exclusively to Shopify merchants. US online rates are **2.9% + $0.30** (Basic plan, $39/month), **2.7% + $0.30** (Grow plan, $105/month), and **2.5% + $0.30** (Advanced plan, $399/month). Merchants who use Shopify Payments avoid Shopify's third-party gateway transaction fees of 2.0%/1.0%/0.6% [29][18][62].

### 2.7 2Checkout (Verifone)
2Checkout, acquired by Verifone in 2020, operates as Verifone's digital commerce division. It is a full merchant-of-record (MoR) and payment processor with tiered plans: **2Sell (3.5% + $0.35)**, **2Subscribe (4.5% + $0.45)**, and quote-based 2Monetize/4Enterprise. It supports sales in 200 countries/territories and 100+ currencies, making it attractive for international and digital-goods sellers [7][30][39].

### 2.8 Amazon Pay
Amazon Pay lets Amazon customers pay on merchant sites using their Amazon accounts. US pricing is **2.9% + $0.30** for domestic web/mobile transactions (including a non-refundable $0.30 authorization fee) and **3.9% + $0.30** for cross-border. It is available to merchants in 18+ countries and offers multi-currency checkout in 12 currencies [8][31][36].

### 2.9 Apple Pay
Apple Pay is a digital wallet enabling payments via Safari (Apple Pay JS API) and the W3C Payment Request API, live in 75+ markets. **Apple charges merchants no fee** for Apple Pay; merchants pay their processor's standard card rate. Apple's revenue comes from a ~0.15% fee paid by card issuers, not merchants [20][9][56].

---

## 3. Dimension-by-Dimension Comparison

### 3.1 E-commerce Integration Capabilities

**Stripe** offers the deepest developer toolchain: 11 official SDKs (Ruby, Python, Go, Java, Node, PHP, .NET, React, iOS, Android, React Native), a full REST API, MCP agent tooling, and official plugins for Adobe Commerce/Magento, Salesforce B2C Commerce Cloud, Shopify, WooCommerce, and Wix. Stripe supports both hosted checkout (Checkout, Payment Links) and fully custom/headless builds, and describes its model as "building blocks" for custom payment experiences [10][11][12][1].

**PayPal** provides the JavaScript SDK v6 (supporting PayPal, Pay Later, Venmo, Google Pay, Apple Pay, Fastlane, and cards), REST/NVP-SOAP APIs, and Braintree Graph. It has official upgrade/integration guides for WooCommerce and Adobe Commerce/Magento, and its Pay Later product is available on Adyen, Shopify, Shopware, WooCommerce, Magento, BigCommerce, PrestaShop, OpenCart, Salesforce Commerce Cloud, and SAP. Under the September 2024 expanded partnership, PayPal also processes credit/debit card transactions for Shopify Payments [13][14][66].

**Square** connects to 16 e-commerce platforms including Wix, WooCommerce (free official plugin), BigCommerce, Magento, Ecwid, and OpenCart, and offers an eCommerce API for custom sites plus the Square Online website builder. The Wix integration syncs products, inventory, and orders; the WooCommerce plugin syncs products/categories/inventory but not order data [15][3].

**Braintree** offers the Drop-in UI (a script-tag integration that is "the quickest way to integrate"), Hosted Fields (customizable iframes keeping card data off merchant servers), server SDKs (Ruby, Python, PHP, Java, .NET, Node.js), mobile SDKs (iOS, Android), and a GraphQL API. It has documented integrations with BigCommerce, WooCommerce, Magento, and Drupal Commerce, and uniquely enables PayPal + Venmo + cards through a single integration [16][17][37].

**Adyen** provides four payment interfaces — Pay by Link, Drop-in, Components (per-method), and API-only — plus pre-packaged plugins for Salesforce, Microsoft, Adobe Commerce, commercetools, PrestaShop, and Oracle. "Adyen for Platforms" supports marketplaces and SaaS platforms with hosted or API-only onboarding, and Unified Commerce connects online, in-app, and POS [18][5][34].

**Shopify Payments** is not a standalone gateway: it is built into Shopify's checkout with zero-code setup and cannot be used on WooCommerce, BigCommerce, Magento, or headless stores outside Shopify. It supports Shop Pay, Apple Pay, Google Pay, and PayPal Express within the Shopify ecosystem. ~1.89 million merchants use Shopify Payments, processing ~62% of Shopify's GMV [29][6].

**2Checkout (Verifone)** integrates with 120+ carts and offers APIs & connectors on all plans, with documented plugins for Shopify, Salesforce Commerce Cloud, NetSuite, Adobe Commerce, BigCommerce, WooCommerce, and Magento. The 4Enterprise plan adds custom integration and professional services [7][30].

**Amazon Pay** provides the Checkout API v2 (CheckoutSession, ChargePermission, Charge, Refund objects), official SDKs for PHP, .NET, Java, and Node.js, and plugins for 3dcart, BigCommerce, FoxyCart, PrestaShop, Magento, Miva, OpenCart, Recurly, Shopify, ShopSite, Volusion, WooCommerce, and X-Cart. Custom/headless and mobile app integrations are supported [19][36].

**Apple Pay** is enabled through the Apple Pay JS API and Payment Request API in Safari, plus merchant tokens for recurring payments. There are no Apple platform plugins — integration is delivered by the merchant's processor (e.g., Stripe, Adyen, Braintree, Shopify Payments). Merchants need an Apple Developer account, a merchant identifier, and a Payment Processing certificate [9][20][65].

### 3.2 Transaction Fees and Pricing Structures (US, Card-Not-Present, August 2026)

**Stripe** charges a flat **2.9% + $0.30** per successful domestic card/wallet transaction, with no setup, monthly, or hidden fees. Key add-ons: +0.5% manually entered cards, +1.5% international cards, +1% currency conversion, Klarna 5.99% + $0.30, ACH Direct Debit 0.8% (capped at $5), disputes $15 (refunded if the merchant wins), Radar fraud tools from $10/month or $0.05/transaction. Nonprofits (501(c)(3)) pay 2.2% + $0.30. Custom interchange-plus (IC+) pricing and volume discounts are available for high-volume businesses [1][23].

**PayPal** charges **2.99% + $0.49** for standard credit/debit card payments and **3.49% + $0.49** for PayPal Checkout, Guest Checkout, and Venmo. Advanced Checkout (API) is 2.89% + $0.29. ACH is 0.80% (capped at $5). Chargeback fees: $15 standard dispute, $20 chargeback, $30 high-volume disputes. International transactions add 1.50%, and currency conversion carries a 3–4% spread. Interchange-plus-plus (IC++) pricing is available via negotiation at high volume ($1M+ annually). PayPal charges no monthly fee [2][24].

**Square** tiers by plan: Free plan online/invoice rate is **3.3% + $0.30**; Plus ($49/month/location) and Premium ($149/month/location) online rate is **2.9% + $0.30**; the Online API rate is 2.9% + $0.30 on all plans. Afterpay is 6% + $0.30. Manual entry is 3.5% + $0.15. International cards add 1.5%. Square charges **no chargeback/dispute fees**. Custom pricing (Pro) is available above $250K/year [3][22][24].

**Braintree** publishes a standard US rate of **2.89% + $0.29** for cards and third-party digital wallets (per PayPal's official Braintree fee page, updated May 7, 2026). Venmo is 3.49% + $0.49; ACH standard is 0.75% (capped at $5); same-day ACH is 1.5% + $0.10. Chargebacks are $15. Non-USD transactions and international cards each add 1%. Braintree offers both flat-rate and **interchange-plus** pricing — custom rates are negotiated for established businesses. No monthly, setup, gateway, or PCI fees. Verified charities pay 2.19% + $0.29 [21][4][16].

**Adyen** uses **Interchange++** pricing in the US: Visa/Mastercard at approximately **$0.13 + Interchange++ + 0.60%**; Amex at $0.13 + 3.95%. BNPL fees: Klarna ~$0.13 + 4.19%–5.19% + $0.30; Affirm $0.13 + 4.49%; Afterpay ~$0.13 + 4.99% + $0.30. Adyen states there are no monthly, setup, integration, or closure fees, but a **minimum monthly invoice** applies (~€1,000+ reported), and all published fees are "indicative" — final pricing comes from the Adyen sales team. Chargebacks are ~$10 [5][61][34].

**Shopify Payments** rates depend on the Shopify plan: **Basic (2.9% + $0.30)**, **Grow (2.7% + $0.30)**, **Advanced (2.5% + $0.30)**. Some 2026 sources cite 2.6%/2.4% for Grow/Advanced from older pricing; the official Shopify pricing page is authoritative. Monthly plan fees are $39/$105/$399 (annual billing discounts apply). Premium cards (Amex) add 3.5%/3.3%/3.1% + $0.30. International cards add 1%. Merchants **not** using Shopify Payments pay additional third-party gateway fees of 2.0% (Basic), 1.0% (Grow), and 0.6% (Advanced) on top of the gateway's own fees [29][18][62].

**2Checkout (Verifone)** publishes tiered pricing: **2Sell at 3.5% + $0.35**, **2Subscribe at 4.5% + $0.45**, and quote-based 2Monetize/4Enterprise. There are no setup fees or hidden charges, and fraud protection/recurring billing are included. A 2% cross-border fee may apply in specific countries. Chargebacks cost $15–45 (per third-party reporting; not on the official pricing page) [7][30][60].

**Amazon Pay** charges **2.9% + $0.30** for domestic web/mobile transactions and **3.9% + $0.30** for cross-border (payment method issued outside the US). The $0.30 authorization fee is non-refundable. Disputed chargeback fees are $20. No setup, monthly, annual, or termination fees. On refunds, the percentage fee is refunded but the authorization fee is not. Amazon Pay transactions via Shopify Payments follow the Shopify Payments fee schedule [8][63].

**Apple Pay** charges merchants **no fee**. Merchants pay their processor's standard card-not-present rate (e.g., 2.9% + $0.30 on Stripe). Apple receives ~0.15% from card issuers, not merchants [20][56].

### 3.3 International Payment Support and Multi-Currency Processing

**Stripe** operates in 46 fully supported countries (where merchants can open accounts), with an Extended Network of 5 additional countries (Nigeria, Kenya, Ghana, South Africa, Côte d'Ivoire) and preview markets in India and Indonesia. Merchants can accept payments from customers in 195+ countries, charge in **135+ currencies**, and receive funds in a preferred currency. The platform is available in 30+ languages. Cross-border fees: +1.5% for international cards, +1% currency conversion; FX Quotes API at 1% per transaction [25][1].

**PayPal** operates in ~200 markets and supports 130+ currencies for display, with 24 currencies supported as payment/settlement balances. Expanded Checkout is available in 37 countries and 22 currencies. International transactions add 1.50%, and PayPal's currency conversion spread is 3–4% above the mid-market rate (4% for payment conversions, 3% otherwise). Payouts are supported in 90+ countries [26][27][2].

**Square** is the most limited of the full processors: available in only **8 countries** (US, Canada, Australia, Japan, UK, Ireland, France, Spain) with 8 currencies. International cards incur +1.5%. ACH is US-only. Afterpay/Clearpay is supported in the US, Canada, Australia, and UK only. Square does not publish a merchant currency-conversion fee [28][3].

**Braintree** processes in 45+ countries and supports **130+ currencies**. Scheme settlement currencies include USD, EUR, GBP, CAD, AUD, JPY, and others. Non-USD transactions add 1%; international cards add 1%. Multi-currency presentment/settlement requires banking-partner approval and setup during onboarding. Note: as of January 1, 2026, Bulgaria adopted the euro and BGN is no longer supported [29][21].

**Adyen** has the broadest global acquiring footprint: operations in **70+ countries** (described as "almost 100"), supporting **150+ currencies** with local payout currencies in 40+ markets. Local acquiring reduces cross-border costs. Like-for-like settlement avoids currency conversion when the settlement currency is supported. DCC is available for POS with a default 3% cardholder fee. POS terminals support 30+ languages [5][15][30].

**Shopify Payments** is available in **40+ countries** (recent expansions added Poland, Norway, Greece, Hungary, and other EU markets in 2025–2026). The Shopify platform supports 200+ currencies and 20+ languages via Shopify Markets. Currency conversion fees are 1.5% (international) / 2% (US). International cards add 1%. Post-Brexit, UK/EU transactions are classified as international [6][29].

**2Checkout (Verifone)** supports sales in **200 countries/territories**, billing in **100+ currencies**, and checkout in 30+ languages — the broadest country reach of any platform in this report. A 2% cross-border fee may apply in specific countries. 2Monetize adds global tax and regulatory compliance as a merchant of record [7][30][39].

**Amazon Pay** is available to merchants in 18+ countries (US, UK, EU markets, Japan, Switzerland, and India per contact pages). Multi-currency checkout lets customers pay in **12 supported currencies** while merchants receive disbursements in their base currency; merchants can hold EUR accounts with any SEPA bank. Cross-border fee is 3.9% + $0.30 [31][36][8].

**Apple Pay on the Web** is live in **75+ markets worldwide**. Apple publishes a country/region list (US, Canada, UK, EU, Japan, Australia, and many more) but not a standalone currency count — currency follows the merchant's payment request and card issuer. Apple imposes no cross-border or DCC fees; those are determined by the underlying processor [32][9][20].

### 3.4 Ease of Setup and Technical Requirements

**Stripe** offers no-code options (Payment Links, prebuilt Checkout, plugins for Shopify/WooCommerce/Wix) and best-in-class developer documentation with a complete REST API reference, official SDKs, and a status page. Standard plugin setup requires no coding; custom checkout requires developer expertise. Stripe claims a 73% integration-time reduction using Checkout vs. custom forms, and typical PCI compliance implementation takes 1–2 weeks [33][1].

**PayPal** is the easiest standard setup of the nine — merchants can convert a personal account, and no-code checkout buttons are a headline feature. Custom Advanced Checkout/API integrations require developer work (the JS SDK v6 needs server-side token generation for Fastlane). Technical skill needed: low for standard, moderate for custom [13][2].

**Square** requires no coding for its website builder, invoices, payment links, and platform plugins. The eCommerce API is available for custom sites. Square is characterized as "fast setup, real-time authorization" and ideal for non-technical merchants [3][15].

**Braintree** offers the Drop-in UI as the fastest script-tag integration (minimal coding), while Hosted Fields and custom integrations require a developer. Client tokens expire after 24 hours. Onboarding can be slower and more selective than Stripe/PayPal — third-party reviews note "longer approval times" and that Braintree is "picky about clients" (it does not work with high-risk merchants) [16][17][37].

**Adyen** onboarding typically takes 2–3 business days once documents are submitted. Drop-in/Components integrations require minimal-to-moderate development; API-only integration requires prior Adyen approval and PCI DSS certification. Adyen is enterprise-oriented, with reported minimum volume requirements (~5,000 transactions/month or $500K+/month in some industries) [34][61].

**Shopify Payments** has the lowest technical barrier: setup is from the Shopify admin with no coding, and activation is instant for eligible merchants. Eligibility requires a supported country, permitted business type, and age 18+ (under-18 requires a parent/guardian). Custom checkout requires Shopify Plus [35][29].

**2Checkout (Verifone)** claims setup in "a few minutes" for standard plugin installs, but manual underwriting can take weeks (contrasted with Stripe's instant onboarding). Advanced setups (subscriptions, 100+ currencies, custom dashboards) take longer. The platform is typically managed by e-commerce heads, finance leads, or founders; custom integration requires developers [30][7][39].

**Amazon Pay** claims integration in as little as 15 minutes via plugins. US registration requires a US credit card, US checking account, business taxpayer ID, US phone number, and US business address. Custom API integration requires developers; a sandbox is provided. New sellers face a reserve policy (100% of payments reserved for 7 days initially) [36][63].

**Apple Pay** has no Apple-side merchant onboarding — merchants onboard with their processor. Apple-side setup requires an Apple Developer account, a merchant identifier, a Payment Processing certificate, and domain verification (a file at `/.well-known/`). Standard processor-hosted checkouts need no Apple-specific coding; custom Apple Pay JS integration requires a developer. A demo site and sandbox are available [9][20].

### 3.5 Supported Payment Methods

**Stripe** supports **100+ payment methods** across cards (Visa, Mastercard, Amex, Diners, Discover, JCB, UnionPay), bank debits (ACH Direct Debit, Instant Bank Payments, SEPA, BECS), bank redirects (iDEAL, Bancontact, BLIK, P24), bank transfers, BNPL (Affirm, Afterpay/Clearpay, Klarna, Zip), real-time payments (Pix, PayNow, PromptPay), vouchers (OXXO, Boleto, Konbini), and wallets (Apple Pay, Google Pay, Cash App Pay, WeChat Pay, Revolut Pay, Samsung Pay, and stablecoins). PayPal is also accepted as a payment method on Stripe [38][39][1].

**PayPal** supports PayPal wallet, Venmo (US only), Pay Later/PayPal Credit, Google Pay, Apple Pay, Fastlane guest checkout, and credit/debit cards (Visa, Mastercard, Amex, Discover, China UnionPay, JCB, Diners in the US). Local methods via Expanded Checkout include Bancontact, BLIK, EPS, iDEAL, Multibanco, MyBank, Przelewy24, and Trustly. ACH is available at 0.80% (capped at $5) [13][27][2].

**Square** accepts Visa, Mastercard, American Express, Discover, JCB, and UnionPay; wallets include Apple Pay, Google Pay, Samsung Pay, and Cash App Pay (US); ACH bank transfers (US only); Afterpay BNPL (6% + $0.30); gift cards; Bitcoin; and EBT SNAP. Square does not support Affirm or Klarna natively [28][40][3].

**Braintree** supports Visa, Mastercard, Amex, Discover, JCB, and Diner's Club; wallets PayPal, Venmo (US), Apple Pay, Google Pay, and Samsung Pay; ACH direct debit (standard and same-day); and PayPal Credit. The Drop-in supports 34 locales. BNPL beyond PayPal Credit is not documented in official Braintree sources [16][21][4].

**Adyen** supports 100+ payment methods globally, including Visa, Mastercard, Amex, Discover, Diners, JCB, Maestro, UnionPay; wallets Apple Pay, Google Pay, Samsung Pay, PayPal; ACH Direct Debit; and BNPL Klarna, Afterpay, Affirm, Zip, and Scalapay. Amex and Diners are priced at 3.95% [5][61].

**Shopify Payments** supports Visa, Mastercard, Amex, Discover (selected countries), Diners, Elo, JCB, and UnionPay; wallets Apple Pay, Google Pay, Shop Pay (with 100+ million Shop users), and PayPal Express; BNPL via Shop Pay Installments (~5–6%) and Klarna; and manual methods (cash, COD, bank transfers) without third-party fees [29][42][18].

**2Checkout (Verifone)** supports **45+ payment methods** on 2Monetize and 14 on 2Sell/2Subscribe, including Visa, Mastercard, PayPal, Apple Pay, Amex, JCB, and regional wallets. Ecwid documentation additionally lists Discover, Diner's Club, and debit cards [7][43].

**Amazon Pay** draws on payment methods stored in the buyer's Amazon account: credit cards (Visa, Mastercard, Discover, Amex, Diners, JCB) and debit cards (Visa, Mastercard). **Amazon.com Gift Cards cannot be used with Amazon Pay** (explicitly stated in official documentation). Amazon Pay supports one-time, recurring/subscription, digital goods, pre-orders, and micropayments, and can be offered alongside other wallets [36][8].

**Apple Pay** supports credit, debit, and prepaid cards from participating banks/issuers (Visa, Mastercard, Amex, Discover, JCB), plus Apple Cash (US only). Apple's own BNPL product, **Apple Pay Later, was discontinued in 2024**; installment options are now provided by card issuers and lenders (Affirm is the first partner) at checkout. Merchants may present other payment methods alongside Apple Pay [44][32][57].

### 3.6 Fraud Protection and Security Features

**Stripe** provides Radar, a machine-learning fraud engine scoring every transaction in real time across Stripe's network. Basic Radar is included; Radar for Fraud Teams starts at $10/month or $0.05/screened transaction. Disputes cost $15 (refunded if the merchant wins); Smart Disputes costs 30% of the won amount. Stripe is PCI Level 1 compliant; Checkout is SAQ-A eligible. Native tokenization, 3D Secure authentication, SCA support, and end-to-end encryption are included. Stripe processes 30+ billion transactions/year and $1.5 trillion in volume [1][23].

**PayPal** offers the Seller Protection Program (updated January 26, 2026), which covers eligible Unauthorized Transactions and Item Not Received claims (physical goods, shipped to the address on file, with valid proof). A 2024 rule change removed INR coverage for card-funded chargeback claims filed directly with issuers. Chargeback Protection costs 0.40% per transaction (0.60% for Effortless) and covers unauthorized transactions and INR with fee waivers. Fraud Protection Advanced is $10/month; Buyer Authentication/3D Secure is $10/month. Dispute/chargeback fees: $15 standard, $20 chargeback, $30 high-volume. PayPal uses tokenization and hosted payment pages to reduce PCI scope [45][46][2].

**Square** provides machine-learning fraud detection and Risk Manager (custom alerts/rules for online transactions). **Square charges no fees for dispute management**, but merchants have only **7 days** to respond to a dispute, and Square allows only first representment (no arbitration). The paid Chargeback Protection program was discontinued in April 2019. Square is PCI Level 1 certified and acts as merchant of record, so sellers do not individually validate compliance. Tokenization is built into the platform; 2-Step Verification and passkeys protect accounts. 3D Secure support is not publicly documented [47][48][3].

**Braintree** offers Premium Fraud Management Tools in two tiers: Fraud Protection Lite (customizable rules, ML risk scores, block lists) and Fraud Protection Advanced (enterprise features: review queues, custom filters, 200+ data features, allow/block lists, and a Transaction Risk Filter scoring 0–1000). Chargeback Protection and Effortless Chargeback Protection (US/Brazil) waive chargeback fees for eligible fraud chargebacks. 3D Secure (3DS 2) is supported via Drop-in and Hosted Fields, with possible per-transaction fees depending on pricing model. Drop-in/Hosted Fields are PCI SAQ-A compliant; Braintree is Level 1 PCI compliant. Chargeback fee: $15 [49][50][16].

**Adyen** provides RevenueProtect, a rule-based and ML-powered fraud engine with customizable risk rules, backtesting, A/B testing, manual review queues, and network signals (anonymous cross-merchant data sharing). Transactions are categorized Safe/Suspicious/Fraudulent. Case study: True Alliance reduced fraud from 3.5% to under 0.1%. Adyen supports 3D Secure/3DS2 (mandatory under PSD2 in certain countries), tokenization, network token optimization, PCI Level 1 DSS 3.2, and P2PE for POS. Chargeback fee is ~$10. Adyen notes it "does not guarantee fraud prevention" and merchants should configure their own settings [41][34][5].

**Shopify Payments** includes Fraud Analysis on all plans with ML-powered fraud recommendations (low/medium/high risk) for online credit card orders. **Shopify Protect** (free for Shop Pay orders) automatically covers the order value and chargeback fee on fraudulent transactions for eligible US stores. **Fraud Protect** (paid) classifies orders as protected/not protected and guarantees payment on fraudulent chargebacks. Dynamic 3D Secure is automatically enabled with liability shift. Card-testing protection, proxy detection, tokenization, and Level 1 PCI DSS compliance are built in, with automated dispute management [51][52][29].

**2Checkout (Verifone)** supports 3D Secure 2.0, AVS, CVV, PSD2 two-factor authentication, and transaction review. Verifone's Fraud Protection Service provides real-time AI fraud scoring, device fingerprinting, behavior analytics, blocking rulesets, and tokenized payments with built-in PCI compliance, available for all card-not-present transactions. Chargeback handling is included in all plans [53][7].

**Amazon Pay** provides the **A-to-Z Guarantee**: buyers are covered up to **$2,500** (item + shipping) for non-receipt, late delivery, damaged/not-as-described items, and unfulfilled refunds. Sellers have 5 business days to respond to claims; failure results in automatic debit. Amazon Pay includes fraud detection, chargeback controls, and risk management at no extra cost, and merchants never receive full card numbers, reducing PCI scope. The disputed chargeback fee is $20. New sellers face a reserve policy that relaxes after 100 orders and a <1% order defect rate [54][55][36][63].

**Apple Pay** uses tokenization (device account numbers replacing PANs), a dynamic security code per transaction, and biometric authentication (Face ID, Touch ID, passcode). Because of built-in authentication, Apple Pay transactions benefit from **liability shift** — 3DS can be bypassed while merchants retain protection, improving acceptance rates. Card data never reaches merchant systems, reducing PCI scope. Disputes/chargebacks are handled by the underlying processor (e.g., Stripe applies its standard dispute process to Apple Pay transactions) [56][57][20].

### 3.7 Customer Support Quality

**Stripe** includes **24x7 support on the standard plan** at no cost. Premium support is quote-based. Self-service resources are extensive: developer docs, Discord server, YouTube tutorials, and a developer newsletter [1][23].

**PayPal** offers phone support at 888-221-1161 (Mon–Sun, 6am–6pm PT), a 24/7 Business Support Center (402-935-2050), and 24/7 Merchant Services (855-456-1330). There is no direct email; chat begins with a virtual assistant. Third-party data indicates long hold times (89-minute average), with only ~21% of callers reaching a person and a ~10% issue-resolution rate in one sample. The Resolution Center and Help Center are robust self-service resources [58][59][2].

**Square** provides chat and email support on all plans. Phone support hours: 6am–6pm PT Mon–Fri for Free (first 90 days only) and Plus; **Premium includes 24/7 phone support**. Square's Support Center, Seller Community, and dispute dashboards are self-service resources. Notably, restaurants on Free/Plus must pay for phone support after the first 90 days (October 2025 pricing change) [22][24].

**Braintree** offers phone, email, tickets, a knowledge base, and tutorials, with 24/7 emergency email support. There is no live chat or dedicated account manager. Third-party reviews are mixed: Braintree is "famous for outstanding support" per one review, but has "many negative reviews" per another (long setup times, chargeback issues, account holds) [4][16].

**Adyen** provides a named account/support manager approach for enterprise merchants, with dedicated Merchant Onboarding Managers during setup. Self-service resources include a knowledge hub, docs.adyen.com, and the Customer Area. Support hours and paid tiers are not publicly disclosed; Adyen's model is relationship-based rather than tiered [34][5].

**Shopify Payments** includes **24/7 support on all plans** (Basic, Grow, Advanced) per multiple 2026 sources, plus an extensive Help Center and active community forums. Shopify Plus adds a dedicated Merchant Success Manager and launch engineer [29][18].

**2Checkout (Verifone)** includes email and chat support on all plans; TrustRadius cites phone, live chat, email, FAQ/knowledge base, social media, and video tutorials. A paid **2Service** premium support tier is available as an add-on, and 4Enterprise includes dedicated support [7][60].

**Amazon Pay** provides phone, email, and live chat via Amazon Pay Merchant Support in Seller Central, plus extensive help pages, developer guides, and a case-study library. No paid support tiers are publicly disclosed [36][8].

**Apple Pay** has Apple Pay Merchant Support (referenced in developer docs) and deep self-service resources (developer documentation, HIG, sample code, tech talks, demo site). Published phone/chat hours and paid support tiers for merchants are **not publicly disclosed**; day-to-day support is provided by the merchant's processor [65][9][20].

### 3.8 Scalability for Small to Medium-Sized Businesses

**Stripe** scales from startup to enterprise without switching platforms. Custom interchange-plus pricing and volume discounts are available at scale (typically $100K+/month processing). Stripe reports 99.999% average historical uptime, 250M+ API requests daily, and handles "millions of dollars" in transaction volume well. Third-party analysis: Stripe's flat rates become relatively expensive at high volume, making IC+ pricing the trigger point for migration [1][23].

**PayPal** is cost-competitive for SMBs processing $50K–$500K annually; above $500K, alternatives like Stripe reportedly save $1,400+/year. IC++ pricing is negotiable at $1M+ annually. PayPal serves from solopreneurs to enterprises (Ticketmaster, HelloFresh, Southwest Airlines refund case study). Merchant volume discounts exist at $3K+/month tiered pricing [2][66].

**Square** offers a clear upgrade path: Free → Plus ($49/mo) → Premium ($149/mo) → Pro (custom, $250K+/yr). However, third-party analysis suggests Square is best up to ~$25K/month online volume before custom pricing is needed, and Square Online is limited to roughly $500K GMV. Adding locations incurs per-location subscription fees [22][24][3].

**Braintree** scales from small shops to enterprise, with custom flat rates and interchange-plus pricing available for established businesses (reportedly ~$80K+/month). Braintree offers **dedicated merchant accounts** (vs. aggregator-style shared accounts), which is a stability advantage, plus marketplace/split-payment capabilities and no monthly minimums [21][4][16].

**Adyen** is the least SMB-friendly of the full processors: reported minimums of ~5,000 transactions/month or $500K+/month in volume, and a minimum monthly invoice (~€1,000+). The breakeven point vs. Stripe is around $250K–$400K/month processing. At $500K/month, Adyen costs roughly $10,270 vs. Stripe's ~$15,700 per third-party modeling. Adyen also has a conservative risk appetite, frequently rejecting high-risk categories [61][5][34].

**Shopify Payments** scales within the Shopify ecosystem from Starter ($5/month) to Basic, Grow, Advanced, and Plus ($2,300+/month), with lower card rates at higher plan tiers. Plan-upgrade break-evens: Basic→Grow at ~$22K–$25K/month card volume; Grow→Advanced at ~$110K/month (annual billing). Shopify Plus handles ~4,000 checkouts/minute baseline. A 2026 study found Shopify's TCO is 33% lower on average than alternatives [29][18].

**2Checkout (Verifone)** scales via its tier ladder (2Sell → 2Subscribe → 2Monetize → 4Enterprise) without switching platforms, and handles 1B+ transactions/year with 20,000+ customers. It is best suited to international sellers, subscription brands, and high-AOV digital merchants; it is "not ideal for US-only sellers or low-volume/low-AOV merchants" [7][30].

**Amazon Pay** uses flat-rate pricing with no volume discounts published. Reserve tiers relax with track record (100+ orders, <1% defect rate over 60 days). Express Payout provides 24-hour payouts (excluding weekends). Daily disbursements land in 1–5 business days. Amazon Pay is suitable for SMBs as a checkout add-on, with 300M+ customer reach [36][63][8].

**Apple Pay** scales with the underlying processor — there are no Apple-imposed tier changes or volume pricing. Merchant identifiers and certificates are reusable across websites and apps, and merchant tokens support recurring and auto-reload payments, making it viable from small stores to enterprise [65][20].

### 3.9 Overall Suitability for US-Based SMB E-Commerce in 2026

**Stripe** is the best all-around choice for online-first US SMBs with some technical capability: lowest standard flat rate (2.9% + $0.30), deepest developer tooling, 135+ currencies, and a path to IC+ pricing at scale. It is especially strong for subscription businesses, custom/headless commerce, and international expansion. The trade-off: flat-rate pricing carries higher interchange markups at high volume, and accounts can be more vulnerable to freezes with large transactions [1][23].

**PayPal** is best for SMBs prioritizing consumer trust and conversion: 439M active accounts, the easiest standard setup, Venmo and Pay Later support, and ~200-market reach. It is the most expensive of the three "default" processors for wallet checkout (3.49% + $0.49), and its currency conversion spread (3–4%) and complex dispute fee structure are drawbacks. A $100 online sale costs $3.98 via PayPal Checkout vs. $3.20 via Stripe — 24% more [2][66].

**Square** is best for omnichannel retailers, restaurants, and service businesses already using Square POS: unified in-person/online payments, no chargeback fees, and an all-in-one ecosystem (banking, payroll, loans). Its online rate on the Free plan (3.3% + $0.30) is the highest of the major processors, international reach is limited to 8 countries, and it is best suited to merchants processing under ~$25K/month online [3][22][24].

**Braintree** is a strong choice for SMBs with developer resources wanting a single integration for cards + PayPal + Venmo, a dedicated merchant account, and negotiable IC+ rates at ~$80K+/month. It is not ideal for non-technical merchants, those needing in-person POS, or businesses processing under $10K/month [4][16][21].

**Adyen** is generally **not recommended for early-stage SMBs** due to minimum volume requirements, minimum monthly invoices, and enterprise-oriented onboarding. It is the best platform for established high-volume merchants ($500K+/month) needing Interchange++ transparency, global local acquiring, and unified commerce [5][61][34].

**Shopify Payments** is the lowest-friction, most cost-effective option for US SMBs committed to the Shopify platform: competitive rates (2.9%/2.7%/2.5% + $0.30), no third-party gateway fees, built-in fraud tools, and 24/7 support. The caveat is vendor lock-in — Shopify Payments cannot be used outside Shopify, and merchants in unsupported countries must use third-party gateways and pay additional platform fees [29][18][62].

**2Checkout (Verifone)** is best for international sellers, digital goods, and subscription businesses wanting merchant-of-record services (tax compliance in 75+ countries, 45+ payment methods, 200-country reach). For US-only SMBs selling physical goods domestically, it is not cost-effective: the entry rate (3.5% + $0.35) is higher than standard US processors, and manual underwriting slows onboarding [7][30][39].

**Amazon Pay** is a strong checkout add-on for US SMBs wanting the Amazon trust factor, reduced cart abandonment, and A-to-Z buyer protection at a competitive flat rate (2.9% + $0.30). It is **not a full replacement** for a primary processor — merchants still need a base gateway for cards and other methods. Watch for the non-refundable $0.30 authorization fee, the $20 dispute fee, platform gaps (no Squarespace/Wix/Square Online), and the new-seller reserve policy [8][36][63].

**Apple Pay** is the highest-conversion, lowest-risk checkout add-on available: **zero Apple fee**, tokenization, biometric authentication, liability shift, and reduced PCI scope. It should be enabled by virtually every US e-commerce SMB through their existing processor. It is not a standalone processor and requires developer work for fully custom web integration [20][56][9].

---

## 4. Summary Comparison Table

### Table 1: Core Facts and Fees (US, Card-Not-Present, August 2026)

| Platform | Type | Standard US Online Rate | Monthly/Setup Fees | Pricing Model | BNPL Support |
|---|---|---|---|---|---|
| **Stripe** | Full processor + gateway | 2.9% + $0.30 | None / None | Flat (IC+ custom at volume) | Klarna (5.99% + $0.30), Affirm, Afterpay, Zip |
| **PayPal** | Full processor + wallet | 2.99% + $0.49 (cards); 3.49% + $0.49 (Checkout) | None / None | Flat (IC++ at $1M+) | Pay Later (4.99% + $0.49) |
| **Square** | Full processor + POS ecosystem | 3.3% + $0.30 (Free); 2.9% + $0.30 (Plus/Premium) | $0 / $49 / $149 per month | Flat only | Afterpay (6% + $0.30) |
| **Braintree** | Gateway + dedicated merchant account | 2.89% + $0.29 | None / None | Flat and IC+ (negotiated) | PayPal Credit |
| **Adyen** | Processor + acquirer | Interchange++ + 0.60% + ~$0.13 (Visa/MC); Amex 3.95% | None (min. monthly invoice ~€1,000) | Interchange++ | Klarna, Affirm, Afterpay, Zip, Scalapay |
| **Shopify Payments** | Native Shopify processor | 2.9% + $0.30 (Basic); 2.7% + $0.30 (Grow); 2.5% + $0.30 (Advanced) | $39 / $105 / $399 per month | Flat (plan-tiered) | Shop Pay Installments (~5–6%), Klarna |
| **2Checkout (Verifone)** | Processor + merchant of record | 3.5% + $0.35 (2Sell); 4.5% + $0.45 (2Subscribe) | None / None | Flat (quote-based tiers) | Available via 45+ methods (2Monetize) |
| **Amazon Pay** | Consumer wallet (processes via Amazon) | 2.9% + $0.30 (incl. $0.30 auth fee) | None / None | Flat | No native BNPL |
| **Apple Pay** | Consumer wallet (requires processor) | No Apple fee; processor rate applies (e.g., Stripe 2.9% + $0.30) | None / None | N/A (processor-dependent) | Issuer/lender installments (Apple Pay Later discontinued) |

### Table 2: International, Methods, Fraud, and Suitability

| Platform | Countries (Merchant) | Currencies | Key Methods | Fraud/Chargeback Highlights | Best For |
|---|---|---|---|---|---|
| **Stripe** | 46 + 5 extended + 2 preview; accepts from 195+ | 135+ | 100+ methods: cards, ACH, wallets, BNPL, vouchers, real-time | Radar ML; $15 disputes (refunded if win); PCI Level 1; 3DS | Online-first SMBs, subscriptions, custom/headless, international |
| **PayPal** | ~200 markets | 130+ (24 settlement) | PayPal, Venmo, cards, Apple/Google Pay, Fastlane, Pay Later, ACH | Seller Protection; Chargeback Protection 0.4–0.6%; $15–30 fees | Conversion via trust, simplest setup, international sellers |
| **Square** | 8 | 8 | Cards, Apple/Google/Samsung Pay, Cash App Pay, Afterpay, ACH, gift cards | No chargeback fees; 7-day response; Risk Manager; PCI Level 1 MoR | Omnichannel/POS retailers, restaurants, local SMBs |
| **Braintree** | 45+ | 130+ | Cards, PayPal, Venmo, Apple/Google Pay, ACH | Fraud Protection Lite/Advanced; 3DS 2; $15 chargebacks; PCI SAQ-A | Dev-enabled SMBs wanting cards + PayPal + Venmo in one integration |
| **Adyen** | 70+ (almost 100) | 150+ | 100+ methods: cards, wallets, ACH, BNPL | RevenueProtect ML; 3DS2; ~$10 chargebacks; PCI Level 1 | Established high-volume merchants ($500K+/mo), global enterprises |
| **Shopify Payments** | 40+ | 200+ (platform) | Cards, Shop Pay, Apple/Google Pay, PayPal Express, Shop Pay Installments | Fraud Analysis ML; Shopify Protect (free); Fraud Protect (paid); dynamic 3DS | Shopify merchants wanting lowest friction and no third-party fees |
| **2Checkout (Verifone)** | 200 territories | 100+ | 45+ methods (2Monetize), 14 (2Sell): cards, PayPal, Apple Pay, regional | Verifone Fraud Protection; 3DS2; AVS/CVV; $15–45 chargebacks | International/digital/subscription sellers wanting MoR tax compliance |
| **Amazon Pay** | 18+ | 12 checkout currencies | Amazon-account cards; no gift cards; recurring | A-to-Z Guarantee ($2,500); fraud detection included; $20 disputes | Adding Amazon trust to checkout; reducing cart abandonment |
| **Apple Pay** | 75+ markets (web) | Processor-dependent | Cards in Wallet, Apple Cash (US); installments via issuers | Tokenization; biometrics; liability shift; reduced PCI scope | Any e-commerce merchant wanting higher conversion and lower fraud |

---

## 5. Key Takeaways

1. **For most US SMB e-commerce merchants in 2026, Stripe, Shopify Payments, and PayPal are the default shortlist.** Stripe offers the lowest standard rate (2.9% + $0.30) and best developer experience; Shopify Payments is the clear winner for merchants on Shopify (avoiding 0.6–2.0% third-party gateway fees); PayPal maximizes consumer trust and international reach but costs more per transaction.

2. **Braintree is the value pick for developers** — the same 2.89% + $0.29 rate as Stripe's standard pricing, plus dedicated merchant accounts, IC+ negotiation at ~$80K/month, and PayPal/Venmo in a single integration.

3. **Adyen and 2Checkout serve specific niches, not the general SMB market.** Adyen's Interchange++ model and local acquiring shine at $500K+/month; 2Checkout's merchant-of-record model shines for international/digital sellers who need tax compliance handled.

4. **Amazon Pay and Apple Pay are force-multiplier add-ons, not replacements.** Amazon Pay adds trust and A-to-Z protection at a competitive 2.9% + $0.30; Apple Pay costs nothing extra and delivers tokenization, liability shift, and higher conversion. Both should be enabled alongside a primary processor.

5. **Fee transparency varies.** Stripe, PayPal, Square, Braintree, Shopify Payments, and Amazon Pay publish full US fee schedules. Adyen publishes indicative Interchange++ pricing but requires a sales conversation for final rates. 2Checkout publishes tiered rates but keeps 2Monetize/4Enterprise quote-based. Apple Pay publishes no merchant fee because it charges none.

---

### Sources

[1] Stripe Pricing & Fees (official): https://stripe.com/pricing
[2] PayPal Business Merchant Fees (official, July 15, 2026): https://www.paypal.com/us/business/paypal-business-fees
[3] Square Fees Help Article (official): https://squareup.com/help/us/en/article/5068-what-are-square-s-fees
[4] Braintree FAQ (official): https://www.braintreepayments.com/faq
[5] Adyen Pricing for Supported Payment Methods (official): https://www.adyen.com/pricing
[6] Shopify Payments Supported Countries (official Help Center): https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries
[7] 2Checkout Official Pricing Page: https://www.2checkout.com/pricing
[8] Amazon Pay Fees (official US help page): https://pay.amazon.com/help/201212280
[9] Apple Developer — Apple Pay on the Web: https://developer.apple.com/documentation/applepayontheweb
[10] Stripe SDKs Documentation: https://docs.stripe.com/sdks
[11] Stripe Payments, Billing, and Tax Plugin for Adobe Commerce: https://docs.stripe.com/use-stripe-apps/adobe-commerce/payments
[12] Stripe App for Salesforce B2C Commerce Cloud: https://docs.stripe.com/use-stripe-apps/salesforce-commerce-cloud
[13] PayPal JavaScript SDK v6 Setup (Developer): https://developer.paypal.com/sdk/js/set-up
[14] PayPal Commerce Platforms Overview (Developer): https://developer.paypal.com/v5/pay-later/commerce-platforms
[15] Square — How to Connect Square to Your eCommerce Site (official): https://squareup.com/us/en/the-bottom-line/selling-anywhere/how-to-connect-square-payments-to-your-online-store
[16] Braintree Drop-in UI (Developer): https://developer.paypal.com/braintree/docs/start/drop-in
[17] Braintree Hosted Fields (Developer): https://developer.paypal.com/braintree/docs/start/hosted-fields
[18] Adyen — Accept Payments Everywhere (official): https://www.adyen.com/accept-payments
[19] Amazon Pay API Introduction (Developer): https://developer.amazon.com/docs/amazon-pay-api-v2/v1-introduction.html
[20] Stripe Documentation — Apple Pay: https://docs.stripe.com/apple-pay
[21] PayPal Braintree Fees & Pricing (official, May 7, 2026): https://www.paypal.com/us/enterprise/paypal-braintree-fees
[22] Square Online Store Pricing & Plans (official): https://squareup.com/us/en/online-store/plans
[23] NerdWallet — Stripe Fees: https://www.nerdwallet.com/business/software/learn/stripe-fees
[24] NerdWallet — Square Fees for 2026: https://www.nerdwallet.com/business/software/learn/square-fees
[25] Stripe Supported Currencies (official docs): https://docs.stripe.com/currencies
[26] PayPal Supported Currencies (Developer): https://developer.paypal.com/docs/reports/reference/paypal-supported-currencies
[27] PayPal Expanded Checkout Eligibility (Developer, Aug 2026): https://developer.paypal.com/expanded/eligibility
[28] Square Supported Payment Methods by Country (Developer): https://developer.squareup.com/docs/payment-card-support-by-country
[29] Braintree Currencies (Developer reference): https://developer.paypal.com/braintree/docs/reference/general/currencies
[30] Adyen Supported Payout Currencies: https://docs.adyen.com/account/supported-currencies
[31] Amazon Pay Blog — Simplify Cross-Border Selling with Multi-Currency: https://pay.amazon.com/blog/product-spotlight/simplify-cross-border-selling-with-multi-currency
[32] Apple Support — Countries and Regions That Support Apple Pay: https://support.apple.com/en-us/102775
[33] Stripe Developer Resources: https://docs.stripe.com/development
[34] Adyen Terms and Conditions: https://www.adyen.com/legal/adyen-terms-and-conditions
[35] Shopify Payments Eligibility (official Help Center): https://help.shopify.com/en/manual/payments/shopify-payments/onboarding/eligibility
[36] Amazon Pay — Merchant Frequently Asked Questions (official): https://pay.amazon.com/help/201810860
[37] Braintree Web Drop-in Documentation: https://braintree.github.io/braintree-web-drop-in/docs/current/module-braintree-web-drop-in.html
[38] Stripe Supported Payment Methods Overview: https://docs.stripe.com/payments/payment-methods/overview
[39] Stripe Payment Method Support (official docs): https://docs.stripe.com/payments/payment-methods/payment-method-support
[40] Square Accepted Cards (official): https://squareup.com/help/us/en/article/5085-accepted-cards
[41] Adyen — What Is Payment Fraud and How to Prevent It: https://www.adyen.com/knowledge-hub/payment-fraud
[42] Shopify — Average Credit Card Processing Fees 2026: https://www.shopify.com/blog/credit-card-processing-fees
[43] Ecwid Help Center — 2Checkout (now Verifone): https://support.ecwid.com/hc/en-us/articles/207806825-2Checkout-now-Verifone
[44] Equipifi — Apple Discontinues Apple Pay Later: https://www.equipifi.com/blog/apple-discontinues-apple-pay-later
[45] PayPal Seller Protection Program (official, Jan 26, 2026): https://www.paypal.com/us/legalhub/paypal/seller-protection
[46] Chargeback.io — What Is PayPal Chargeback Protection: https://www.chargeback.io/blog/what-is-paypal-chargeback-protection
[47] Square Payment Disputes Walkthrough (official): https://squareup.com/help/us/en/article/3882-payment-disputes-walkthrough
[48] Square Secure Payments (official): https://squareup.com/us/en/payments/secure
[49] Braintree Premium Fraud Management Tools Overview (Developer): https://developer.paypal.com/braintree/articles/guides/fraud-tools/premium/overview
[50] Braintree 3D Secure Documentation: https://articles.braintreepayments.com/guides/fraud-tools/3d-secure
[51] Shopify Fraud Analysis (official Help Center): https://help.shopify.com/en/manual/fulfillment/managing-orders/protecting-orders/fraud-analysis
[52] Shopify — Shopify Protect Is Shop Pay's Free Fraud Protection: https://www.shopify.com/blog/shopify-protect
[53] Verifone — Fraud Management and Regulatory Compliance: https://www.verifone.com/en-us/fraud-management-and-compliance
[54] Amazon Pay — A-to-Z Guarantee Policy for Sellers: https://pay.amazon.com/help/201212330
[55] Amazon Pay — A-to-Z Guarantee Protection for Buyers: https://pay.amazon.com/help/201212340
[56] Checkout.com — Apple Pay: A Guide for Merchants: https://www.checkout.com/blog/apple-pay-for-business
[57] Apple Developer — Human Interface Guidelines, Apple Pay: https://developer.apple.com/design/human-interface-guidelines/apple-pay
[58] Elliott Report — PayPal Customer Service Contacts (May 2026): https://www.elliott.org/company-contacts/paypal
[59] GetHuman — PayPal Merchant Services Phone Number: https://gethuman.com/phone-number/PayPal/customer-service/~18371
[60] TrustRadius — 2Checkout from Verifone Pricing: https://www.trustradius.com/products/verifone-2checkout/pricing
[61] Gravity Forms — Stripe vs Adyen: https://www.gravityforms.com/blog/stripe-vs-adyen-comparison
[62] Shopify Community — Why Does Shopify Charge a 2% Transaction Fee for Third-Party Providers: https://community.shopify.com/t/why-does-shopify-charge-a-2-transaction-fee-for-third-party-providers/246613
[63] NerdWallet — Amazon Pay Review: https://www.nerdwallet.com/business/software/learn/amazon-pay
[64] Shopify Pricing Plans (official Help Center): https://help.shopify.com/en/manual/intro-to-shopify/pricing-plans/pricing-overview
[65] Apple Developer — Apple Pay Merchant Tokens: https://developer.apple.com/apple-pay/merchant-tokens
[66] PayPal — History and Facts (official corporate): https://about.pypl.com/who-we-are/history-and-facts/default.aspx
