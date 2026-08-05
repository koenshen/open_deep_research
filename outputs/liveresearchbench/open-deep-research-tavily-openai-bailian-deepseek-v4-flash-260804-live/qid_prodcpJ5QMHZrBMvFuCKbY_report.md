# Comprehensive Comparison of Nine Payment Processors for E-commerce Integration (August 2026)

## Introduction

This report provides a detailed comparison of nine major payment processors—Stripe, PayPal, Square, Braintree, Adyen, Shopify Payments, 2Checkout (Verifone), Amazon Pay, and Apple Pay—across eight critical dimensions for e-commerce integration. The comparison is designed for US-based small to medium-sized businesses evaluating payment processing solutions as of August 2026. Each section draws on official pricing pages, developer documentation, verified customer reviews, and industry analysis to provide accurate, actionable insights.

---

## Dimension 1: E-commerce Integration Capabilities

### Stripe

Stripe offers the most comprehensive developer toolkit in the industry, with interactive API documentation, SDKs in 8+ programming languages, and 660+ third-party integrations [1][4]. Integration options include Stripe Checkout (hosted payment page), Payment Links (no-code), Stripe Elements (customizable UI components), and the full Payments API. Stripe integrates natively with all major e-commerce platforms including Shopify, WooCommerce, Magento, BigCommerce, Squarespace, and Wix [1][2]. Stripe Connect enables platform and marketplace businesses to embed payments with onboarding, payouts, and risk monitoring [3]. The platform is fully white-label at no extra cost—customers never leave the merchant's website [4].

### PayPal

PayPal provides instant setup with zero technical knowledge required, making it ideal for non-technical founders [5]. Integration options include PayPal Checkout (redirect or embedded), PayPal Payment Links, and the PayPal Commerce Platform APIs. PayPal integrates with 500+ apps and all major e-commerce platforms including Shopify, WooCommerce, Magento, BigCommerce, and Squarespace [6]. BigCommerce has a native PayPal payment gateway that automatically migrated from PayPal Express Checkout to the latest PayPal solution, adding features like PayPal Pay Later, Apple Pay, Venmo, and local payment methods [7]. PayPal's merchant dashboard is notably user-friendly for non-technical users [8].

### Square

Square offers a comprehensive set of developer tools including REST APIs, Web Payments SDK, In-App Payments SDK, and Reader SDK [9]. The Square App Marketplace has grown to nearly 1,000 partner integrations in 2026 [10]. Square integrates with WooCommerce, Wix, Shopify, BigCommerce, and Squarespace through its partner ecosystem [11]. Square Online (Square's own website builder) offers a free basic plan with paid plans starting at $29/month [12]. Square requires businesses to use its built-in payment processor and does not support third-party processors [13]. Square Online is ranked as the best e-commerce platform for retailers combining online and in-person sales [14].

### Braintree

Braintree offers client-side and server-side SDKs in JavaScript, Python, PHP, Java, Ruby, and C# [15]. The Drop-in UI provides a complete, ready-made payment UI that supports credit cards, PayPal, PayPal Credit, Venmo, Apple Pay, and Google Pay [16]. **Critical deprecation**: The Android Drop-in SDK became unsupported on July 14, 2026, and the JavaScript and iOS Drop-in SDKs will be deprecated on September 1, 2026, becoming unsupported on September 1, 2027 [17]. Braintree integrates with Magento (68.9% of Braintree stores), WooCommerce (9.6%), BigCommerce, Shopify, Salesforce Commerce Cloud, and Wix [18]. Braintree requires programming skills for integration [19].

### Adyen

Adyen offers a full API, web Drop-in components, hosted payment pages, and plugins for major e-commerce platforms [20]. Adyen was named a Leader in The Forrester Wave™: Merchant Payment Providers, Q1 2026 [21]. Pre-built plugins are available for Adobe Commerce (Magento 2), Salesforce Commerce Cloud, BigCommerce, Shopify, WooCommerce, and many others [22]. Adyen integrates with Shopify as a third-party payment provider for enterprise-level stores, with a global partnership announced in June 2023 [23]. Adyen is platform-agnostic and works with Shopify, WooCommerce, Magento, BigCommerce, and Salesforce via plugins and APIs [24].

### Shopify Payments

Shopify Payments is a proprietary payment service available exclusively to Shopify merchants, built directly into the platform [25]. Approximately 1.89 million merchants actively use Shopify Payments, roughly 90% of eligible Shopify merchants in supported countries, and about 62% of Shopify's gross merchandise volume is processed through the service [26]. Shopify Payments eliminates Shopify's additional third-party transaction fee (0.5%–2% depending on plan) [27]. Shopify supports over 100 payment providers globally, but only Shopify Payments avoids the Shopify surcharge [28].

### 2Checkout/Verifone

2Checkout offers three integration paths: Hosted Checkout (redirect, fastest to launch), InLine Checkout (embedded iframe), and API 6.0 (full programmatic control with REST/SOAP/JSON APIs) [29]. Pay-by-Link allows payment collection without a website via email, SMS, or social media [30]. 2Checkout integrates with Shopify, WooCommerce, Magento, BigCommerce, Salesforce Commerce Cloud, NetSuite, and Ecwid [31]. The platform supports 30+ languages, 45+ payment methods, 100+ billing currencies, and built-in subscription/recurring billing management [32]. 2Checkout operates as a Merchant of Record (MoR), handling tax, compliance, and billing complexity for cross-border sales [33].

### Amazon Pay

Amazon Pay offers "Pay with Amazon" button integration, Checkout v2 (next-gen RESTful API with hosted checkout flow), Saved Wallet integration, and payment links [34]. Checkout v2 consolidates address, payment, and confirmation steps onto a single screen, reducing abandonment by 18% [35]. Amazon Pay integrates with Shopify, WooCommerce, BigCommerce, Magento, PrestaShop, OpenCart, and 10+ other platforms [36]. Amazon Pay works with over 720,000 merchants globally [37]. "Buy with Prime" integration provides a 25% conversion lift reported [38].

### Apple Pay

Apple Pay provides three integration paths: Apple Pay JS API (native), Payment Request API (W3C standard), and PSP/gateway integration (e.g., Stripe, Adyen) [39]. The Apple Pay JS SDK can be loaded via the auto-updating URL `https://applepay.cdn-apple.com/jsapi/1.latest/apple-pay-sdk.js` [40]. Apple Pay integrates with all major platforms through payment processors: Shopify (via Shopify Payments), WooCommerce (via WooPayments), BigCommerce, and Magento [41][42]. Stripe provides the easiest way to support Apple Pay, enabling frictionless card payments authenticated via Touch ID, Face ID, or passcode [43]. Apple Pay is supported on over 90% of US retailers [44].

---

## Dimension 2: Transaction Fees and Pricing Structures (US, August 2026)

### Stripe

| Fee Type | Rate |
|----------|------|
| Online card payments | 2.9% + $0.30 per transaction |
| In-person (Stripe Terminal) | 2.7% + $0.05 |
| Manually entered cards | 3.4% + $0.30 |
| ACH Direct Debit | 0.8% per transaction, capped at $5.00 |
| International cards | +1.5% on base rate |
| Currency conversion | +1% |
| Chargeback fee | $15 (refunded if merchant wins) |
| Monthly/setup fees | None |

[1][45][46]

Stripe has no monthly fees, no setup fees, and no termination fees. Volume discounts are available for businesses processing over $5M+ annually, offering IC+ rates and multi-product discounts [47]. Nonprofit (501(c)(3)) organizations can get a discounted rate of 2.2% + $0.30 [48]. Stripe does not return the original processing fee on refunds [49].

### PayPal

| Fee Type | Rate |
|----------|------|
| PayPal Checkout (wallet) | 3.49% + $0.49 per transaction |
| Standard credit/debit cards | 2.99% + $0.49 |
| Advanced credit/debit card (API) | 2.89% + $0.29 |
| PayPal Pay Later | 4.99% + $0.49 |
| In-person (Zettle) | 2.29% + $0.09 |
| International surcharge | +1.50% |
| Currency conversion | 3%–4% spread |
| Chargeback fee | $20 USD |
| Monthly fees | None (basic account) |

[50][51][52]

PayPal has no monthly fee for a basic Business account. Legacy PayPal Payments Pro costs $30/month. Volume discounts are available for merchants processing over $1M annually [53]. PayPal's currency conversion spread of 3-4% is significantly higher than competitors [54]. PayPal does not return the full original fee on refunds [55].

### Square

| Transaction Type | Free ($0/mo) | Plus ($49/mo) | Premium ($149/mo) |
|-----------------|--------------|---------------|--------------------|
| Tap/Dip/Swipe (in-person) | 2.6% + $0.15 | 2.5% + $0.15 | 2.4% + $0.15 |
| Online (Square Online) | 3.3% + $0.30 | 2.9% + $0.30 | 2.9% + $0.30 |
| Invoices | 3.3% + $0.30 | 2.9% + $0.30 | 2.6% + $0.30 |
| ACH Bank Transfer | 1% + $1 min | 1% + $1 min, $10 cap | 1% + $1 min, $10 cap |
| Afterpay | 6% + $0.30 | 6% + $0.30 | 6% + $0.30 |

[56][57][58]

Square's 2026 pricing overhaul raised Free plan online rates from 2.9% to 3.3% + $0.30 (a 14% increase) [59]. Square charges no chargeback fees—a major advantage [60]. International cards incur an additional 1.5% surcharge. Custom pricing (Square Pro) is available for businesses processing over $250,000/year [61].

### Braintree

| Fee Type | Rate |
|----------|------|
| Cards and third-party digital wallets | 2.89% + $0.29 per transaction |
| Venmo | 3.49% + $0.49 per transaction |
| ACH Direct Debit (standard) | 0.75% (max $5.00) |
| Chargeback fee | $15.00 |
| Non-USD currency | +1% |
| Non-US-issued card | +1% |

[62][63][64]

Braintree has no monthly fees, no PCI compliance fees, no minimum transaction fees, and no setup fees [65]. Transaction fees are not returned for refunded transactions. Chargeback Protection starts at 0.4% per transaction; Effortless Chargeback Protection starts at 0.6% per transaction [62]. High-volume merchants (over $80,000-$100,000/month) may qualify for discounted rates [66].

### Adyen

Adyen uses a transparent Interchange++ pricing model. For each transaction, Adyen charges a fixed processing fee of $0.13 plus a payment method-specific fee [67]. No setup fee, no monthly fees, but Adyen imposes a minimum monthly invoice of $120 (or €500-€1,000+ depending on region) [68]. Adyen's processing markup is typically 0.60% minimum, negotiable down to 0.30%–0.45% for merchants processing $1 million or more monthly [69].

| Fee Type | Rate |
|----------|------|
| Visa/Mastercard | Interchange++ |
| American Express | 3.95% |
| ACH | $0.25 |
| Alipay | 3% |
| Cross-border fees | 0.40%–1.50% |
| Currency conversion | 1.0%–3.0% |
| Chargeback fee | €15 ($15–$25) |

[67][70]

The breakeven point where Adyen becomes cheaper than flat-rate pricing is around $250K–$400K monthly volume [71].

### Shopify Payments

| Plan | Monthly Cost | Online Credit Card Rate | Third-Party Gateway Surcharge |
|------|--------------|------------------------|-------------------------------|
| Starter | $5/mo | 5% transaction fee | N/A |
| Basic | $39/mo ($29 annual) | 2.9% + $0.30 | 2.0% |
| Grow (Shopify) | $105/mo ($79 annual) | 2.7% + $0.30 | 1.0% |
| Advanced | $399/mo ($299 annual) | 2.5% + $0.30 | 0.6% |
| Shopify Plus | From $2,300/mo | ~2.15% + $0.30 | 0.2% |

[72][73][74]

Additional fees: Premium cards add ~0.6%, international cards add 1%, currency conversion fee is 1.5%–2%, chargeback fee is $15 (refunded if merchant wins) [75]. Shopify offers a 25% discount on annual billing [76].

### 2Checkout/Verifone

| Plan | Transaction Fee | Best For |
|------|----------------|----------|
| 2SELL | 3.5% + $0.35 | Standard one-time payments |
| 2SUBSCRIBE | 4.5% + $0.45 | Subscription & recurring billing |
| 2MONETIZE | 6.0% + $0.60 | Full MoR with global tax compliance |

[77][78]

Cross-border fee: 2% on top of transaction fees (2Sell and 2Subscribe). **US merchants are exempt** from this fee [79]. PayPal surcharge: 3% additional (total 6.5% + $0.35). Chargeback fees: $15–$45 per chargeback. Some reports indicate a $500/month platform fee introduced for some merchants after June 2026 [80]. A rolling 90-day reserve (percentage of sales held to cover risk) is applied [81].

### Amazon Pay

| Fee Type | Rate |
|----------|------|
| US Domestic Processing | 2.9% + $0.30 authorization fee |
| Cross-border Processing | 3.9% + $0.30 |
| Buy with Prime - Prime Service Fee | 3% of order value (min $0.30) |
| Buy with Prime - Payment Processing | 2.4% + $0.30 per transaction |
| Chargeback fee | $20.00 (non-refundable) |

[82][83]

No monthly or setup fees. Currency conversion: 0.5% spread above wholesale rate. The authorization fee is non-refundable on refunds [84].

### Apple Pay

Apple does not charge merchants directly for Apple Pay transactions. The Apple Pay transaction fee is $0.00 [85]. Apple makes money from issuing banks, charging approximately 0.15% of transaction value [86]. Merchants pay standard credit card processing fees (typically 1.5% to 3.5%) from their underlying processor. These fees are identical to physical card payments [87]. Apple Pay does not charge additional cross-border fees; all such fees come from the processor and card networks. An Apple Developer Program membership ($99/year) is required for custom integration [88].

---

## Dimension 3: International Payment Support and Multi-Currency Processing

### Stripe

- **Supported currencies**: 135+
- **Countries for accepting payments**: 195 countries
- **Merchant account countries**: ~46 countries
- **Cross-border fee**: 1.5% additional for international cards
- **Currency conversion**: +1% when Stripe converts to payout currency
- **Local payment methods**: 100+ payment methods globally including iDEAL, SEPA Direct Debit, Alipay, WeChat Pay, Bancontact, FPX, BECS Direct Debit, Bacs Direct Debit, P24, BLIK, PayNow, UPI, Multibanco, OXXO, Boleto, Konbini, and more
- **US merchants**: Can accept payments in 135+ currencies but settle in USD

[1][89][90]

### PayPal

- **Supported currencies**: 25 currencies
- **Countries/markets**: 200+ countries and markets
- **Cross-border fee**: 1.50% additional on top of domestic rate
- **Currency conversion**: 3%–4% spread above the base exchange rate
- **Local payment methods**: Alipay, Apple Pay, Google Pay, WeChat Pay, GrabPay, iDEAL, Boleto, OXXO, and more (availability varies by integration method)
- **US merchants**: Can accept payments in 25 currencies; PayPal has stronger coverage in emerging markets compared to Stripe

[50][91][92]

### Square

- **Supported countries**: 9 countries (US, Canada, Australia, Japan, UK, Ireland, France, Spain, New Zealand)
- **Supported currencies**: 8 currencies
- **International transaction fee**: 1.5% for cards issued outside the seller's home country
- **Multi-currency**: Square does not support true multi-currency processing at the merchant level; each Square account is tied to a single country and currency
- **Local payment methods**: US supports major cards, digital wallets (Apple Pay, Google Pay, Cash App Pay), ACH bank transfers, and Afterpay/Clearpay
- **Restrictions**: Square hardware is only approved for use in the country where the account was activated; cross-border card payments are not supported

[93][94][95]

### Braintree

- **Supported currencies**: Over 130 currencies across 45+ countries
- **Countries available**: Over 45 countries including US, Canada, UK, Australia, and EU
- **Cross-border fees**: Additional 1% for non-USD currency, additional 1% for non-US-issued card, additional 1% for currency conversion
- **Multi-currency processing**: Supports multi-currency setups where merchants can present or settle in multiple currencies, but this requires approval from banking partners
- **Local payment methods**: Credit cards, PayPal, Venmo, Apple Pay, Google Pay, and ACH

[62][96][97]

### Adyen

- **Supported currencies**: 150+ currencies
- **Payment methods**: 250+ payment methods globally
- **Countries**: 60+ countries with direct acquiring licenses in 40+ countries
- **Cross-border fees**: 0.40%–1.50% additional
- **Currency conversion**: 1.0%–3.0%
- **Key advantage**: Adyen acts as its own acquirer in 40+ countries, enabling higher approval rates, lower costs, and faster settlement
- **US merchants**: No restrictions on expanding globally

[67][98][99]

### Shopify Payments

- **Supported countries**: 39 countries and regions (as of June 2026)
- **Supported currencies**: 130+ currencies for processing, 15 payout currencies
- **Currency conversion**: 1.5% for US, 2% for UK/others
- **Recent expansion**: Multi-Currency Payouts expanded to US merchants on June 13, 2026, adding CAD, EUR, AUD, GBP alongside USD, removing the 1.5% to 2% FX drag
- **Local payment methods**: 40+ local methods including iDEAL, Bancontact, SEPA, MobilePay, TWINT, BLIK, Przelewy24, and Meses Sin Intereses in Mexico
- **Limitations**: Very limited in Asia-Pacific (5 countries), Latin America (Mexico only), Middle East (UAE only), and Africa (none)

[100][101][102]

### 2Checkout/Verifone

- **Supported countries**: 190+ countries and territories
- **Billing currencies**: 100+ currencies
- **Payment methods**: 45+ payment methods including regional wallets
- **Languages**: 30+ languages
- **Cross-border fee**: 2% (US merchants exempt)
- **Model**: Merchant of Record (MoR) handles VAT/GST/sales tax compliance, fraud liability, and local regulations
- **Key advantage**: MoR model means 2Checkout takes legal responsibility for transaction processing, tax collection/remittance, and compliance, particularly valuable for small businesses selling internationally without foreign legal entities

[103][104][105]

### Amazon Pay

- **Countries available**: 18 countries (US, UK, Austria, Belgium, Cyprus, Denmark, France, Germany, Hungary, Ireland, Italy, Japan, Luxembourg, Netherlands, Portugal, Spain, Sweden, Switzerland, India)
- **Supported currencies**: 12 currencies (AUD, GBP, DKK, EUR, HKD, JPY, NZD, NOK, ZAR, SEK, CHF, USD)
- **Cross-border fee**: 3.9% when customer's card is issued outside the US
- **Currency conversion**: 0.5% spread above wholesale rate
- **Customer base**: 300M+ active Amazon customer accounts globally
- **Model**: Payment Service Provider (PSP)—merchants remain seller of record for tax/compliance
- **Limitation**: Only available in 18 countries for merchants; customers must have an Amazon account

[82][106][107]

### Apple Pay

- **Countries supported**: Over 85 countries and regions (94-95 countries per some sources)
- **Currency support**: Depends on the underlying payment processor, not Apple
- **Cross-border fees**: Apple Pay does not charge additional cross-border fees; all such fees come from the processor and card networks
- **US market share**: 92% market share in the US digital wallet space; accepted at over 90% of US retailers
- **Global users**: Nearly 818 million global users as of 2026
- **Notable countries without Apple Pay**: India (expected mid-2026), Indonesia, Pakistan, Nigeria, Bangladesh, Russia, many African countries

[108][109][110]

---

## Dimension 4: Ease of Setup and Technical Requirements

### Stripe

- **Time to integrate**: 30–60 minutes for basic integration; a few hours for full API integration
- **Required coding skills**: Significant coding knowledge required to fully benefit; not beginner-friendly out-of-the-box
- **Documentation quality**: One of the best-designed APIs in the industry; comprehensive docs, clear error messages, testing tools
- **No-code/low-code options**: Payment Links, Stripe Checkout (hosted payment page), 660+ integrations
- **Onboarding process**: Typically instant for standard businesses; risk management can result in sudden account closures and prolonged fund holds (90+ days)
- **Developer experience**: 8+ programming languages, AI-powered Radar Assistant, Discord server for technical questions

[1][3][111]

### PayPal

- **Time to integrate**: 15 minutes for basic setup; immediate for non-technical users via payment links
- **Required coding skills**: Minimal to none for basic integration; simple merchant dashboard
- **Documentation quality**: Adequate but less comprehensive than Stripe
- **No-code/low-code options**: PayPal Checkout buttons, PayPal Payment Links, 500+ app integrations
- **Onboarding process**: Very fast—instant setup with zero technical knowledge; well-documented reputation for account holds, freezes, and reserves (funds held up to 180 days)
- **Developer experience**: Inferior to Stripe; Checkout, Subscriptions, and Payouts APIs available

[5][6][112]

### Square

- **Time to integrate**: Minutes—start accepting payments immediately
- **Required coding skills**: No coding required; base POS software is free and plug-and-play
- **Documentation quality**: Strong but less developer-focused than Stripe
- **No-code/low-code options**: Free POS app, Square Online website builder, App Marketplace with nearly 1,000 integrations, Zapier and Make integrations
- **Onboarding process**: Fast for most low-risk businesses; account reviews can delay fund access (5+ days); Square does not support high-risk industries
- **Ease of use**: Widely praised as very easy to set up for beginners; best for "brick-and-mortar business owners"

[10][12][113]

### Braintree

- **Time to integrate**: Requires programming skills; Drop-in UI offers fastest path (3-step process: server setup, client setup, optional configuration)
- **Required coding skills**: Programming skills required; supported SDKs in JavaScript, Python, PHP, Java, Ruby, C#
- **Documentation quality**: Solid for technical integration; less user-friendly than Stripe
- **No-code/low-code options**: Pre-built integrations with major platforms, Drop-in UI script tag integration, Zapier
- **Onboarding process**: Straightforward but requires technical expertise; sandbox environment for testing
- **Ease of use**: Rated 3.8/5 on Capterra; requires more technical expertise compared to Square

[15][16][114]

### Adyen

- **Time to integrate**: Weeks to months—no self-service signup; requires multi-week sales and compliance process
- **Required coding skills**: Significant—dedicated development resources required for API integration
- **Documentation quality**: Comprehensive developer guides, API references, and knowledge hub
- **No-code/low-code options**: Woosa WooCommerce plugin (installable within 24 hours), hosted payment pages
- **Onboarding process**: Lengthy underwriting process; conservative risk appetite; unsuitable for small businesses, high-risk industries, and those needing fast onboarding
- **Best for**: Large, low-risk, high-volume businesses

[67][115][116]

### Shopify Payments

- **Time to integrate**: Under 10 minutes—built directly into the Shopify platform
- **Required coding skills**: None required; no-code/low-code setup
- **Documentation quality**: Excellent—extensive help center resources, guides, and community forums
- **No-code/low-code options**: Fully integrated checkout, no redirects to third-party sites
- **Onboarding process**: Typically instant or within a few days; risk holds can occur for sudden volume spikes or high refund rates
- **Ease of use**: Simplest option for Shopify merchants; no technical work required

[25][26][117]

### 2Checkout/Verifone

- **Time to integrate**: Minutes to hours (Hosted Checkout); days to weeks (API 6.0)
- **Required coding skills**: None/minimal for Hosted Checkout; basic front-end for InLine; full-stack for API 6.0
- **Documentation quality**: Mixed reviews—comprehensive but with steep learning curve; dashboard and reporting tools "not easy to comprehend"
- **No-code/low-code options**: Hosted Checkout, Pay-by-Link, e-commerce plugins (one-click setup for Shopify, WooCommerce, etc.)
- **Onboarding process**: Manual underwriting—can take 1-4 weeks; more stringent than modern processors
- **Key pain point**: "The most painful authorization process" per user reviews

[29][30][118]

### Amazon Pay

- **Time to integrate**: Minutes to hours (e-commerce plugins); days (Checkout v2); days to weeks (custom integration)
- **Required coding skills**: None for plugins; moderate for Checkout v2; high for custom integration
- **Documentation quality**: Good—comprehensive developer guides, integration videos, step-by-step help pages
- **No-code/low-code options**: Native plugins for Shopify, WooCommerce, BigCommerce, Magento, and 10+ platforms; Payment Links; Buy with Prime
- **Onboarding process**: Faster than 2Checkout—typically days rather than weeks; separate Amazon Pay merchant account required (not compatible with existing Selling on Amazon accounts)
- **Key advantage**: Leverages Amazon's existing infrastructure and identity verification systems

[34][35][119]

### Apple Pay

- **Time to integrate**: 2-4 weeks total for PCI compliance and Apple Pay setup
- **Required coding skills**: JavaScript development skills for custom web integration; less coding required for PSP/gateway integration
- **Documentation quality**: Comprehensive—Apple Pay Merchant Integration Guide, Platform Integration Guide, JS API documentation
- **No-code/low-code options**: Shopify automatically enables Apple Pay through Shopify Payments with no coding; BigCommerce provides built-in support; Stripe's no-code Payment Links automatically enable Apple Pay
- **Onboarding process**: Requires Apple Developer account ($99/year), Merchant ID, Payment Processing Certificate, domain verification, and HTTPS serving
- **Technical requirements**: Apple Developer account, merchant ID, payment processing certificate, merchant identity certificate, domain verification, HTTPS

[39][88][120]

---

## Dimension 5: Supported Payment Methods

### Stripe

- **Credit/debit cards**: Visa, Mastercard, American Express, Discover, Diners Club, China UnionPay, JCB, Cartes Bancaires, regional card networks
- **Digital wallets**: Apple Pay, Google Pay, Cash App Pay, Link (Stripe's own wallet), Revolut Pay, WeChat Pay, Kakao Pay, Naver Pay, Samsung Pay, MB WAY, Amazon Pay
- **Buy Now, Pay Later**: Affirm (6% + $0.30), Afterpay/Clearpay (6% + $0.30), Klarna (US/Canada 5.99% + $0.30), Zip, Cash App Afterpay, Meses sin intereses
- **Bank debits**: ACH Direct Debit (0.8% capped at $5), SEPA Direct Debit (0.8% + €0.30, capped at €6), Bacs Direct Debit, AU BECS Direct Debit, Canadian PADs
- **Bank redirects**: iDEAL/Wero (€0.80 flat), Bancontact, BLIK, EPS, FPX, PayNow, UPI, P24, TWINT
- **Bank transfers**: USD Bank Transfers (0.5% capped at $5), EUR, UK, Japan, Mexico Bank Transfers
- **Real-time payments**: Swish, PayTo, Pix
- **Vouchers**: Multibanco, Konbini, OXXO, Boleto
- **Stablecoins**: 1.5% of transaction amount (includes conversion, fraud prevention, and gas sponsorship)
- **Total**: 100+ payment methods globally

[1][45][121]

### PayPal

- **Credit/debit cards**: Visa, Mastercard, American Express, Discover, Union Pay, Cartes Bancaire
- **Digital wallets & P2P**: PayPal (up to 400 million active accounts), Venmo (US only), Apple Pay, Google Pay, Alipay, WeChat Pay, GrabPay
- **Buy Now, Pay Later**: PayPal Pay in 4 (4 payments over 6 weeks, $30-$1,500), PayPal Pay Monthly (6-24 monthly installments, $49-$10,000, fixed APR 9.99-35.99%), PayPal Credit
- **Bank transfers**: ACH (via invoicing, 1% capped at $10), iDEAL
- **Cash/vouchers**: Boleto, OXXO Pay
- **Cryptocurrency**: PYUSD (PayPal's stablecoin), buy, sell, and hold crypto
- **Micropayments**: 4.99% + $0.09 per transaction

[50][122][123]

### Square

- **Credit/debit cards**: Visa, Mastercard, American Express, Discover, JCB, UnionPay, Interac, prepaid cards (Visa, Mastercard), HSA/FSA cards (for licensed healthcare providers)
- **Digital wallets**: Apple Pay, Google Pay, Samsung Pay, Cash App Pay, Square Pay (automatically saves buyer payment details, cannot be disabled)
- **Buy Now, Pay Later**: Afterpay (Square acquired Afterpay)—available for orders $1-$2,000 online and in-person; fees: 6% + $0.30 per transaction; Klarna (limited integration)
- **ACH and bank transfers**: ACH bank transfer (via invoice or API): 1% fee, $1 minimum
- **Other**: Square Gift Cards (physical or electronic), cash and checks (free to process), Bitcoin payments (0% processing fee until 2027), Tap to Pay on iPhone/Android, offline payments (24-hour storage)
- **Not supported**: EBT, government/military cards, Alipay, WeChat Pay, cryptocurrency beyond Bitcoin pilot

[56][124][125]

### Braintree

- **Credit/debit cards**: Visa, Mastercard, American Express, Discover, JCB, Diners Club, UnionPay
- **Digital wallets**: Apple Pay, Google Pay, PayPal (native integration), PayPal Credit, Venmo (unique to Braintree among major gateways)
- **Buy Now, Pay Later**: PayPal Credit (functions as BNPL); no native Afterpay or Klarna integration directly mentioned
- **ACH and bank transfers**: ACH Direct Debit (standard: 0.75% max $5.00; same-day: 1.5% + $0.10)
- **Other**: Recurring billing, marketplace functionality, local payment methods in various countries

[62][126][127]

### Adyen

- **Credit/debit cards**: Visa, Mastercard, American Express, Discover, Diners, JCB, China UnionPay, Cartes Bancaires, Maestro, VPay, Accel, NYCE, Interac, eftpos Australia, Girocard
- **Digital wallets**: Apple Pay, Google Pay, Samsung Pay, PayPal, Amazon Pay, WeChat Pay, Alipay
- **Buy Now, Pay Later**: Klarna, Afterpay, Affirm, Billie, Zip
- **Bank-based methods**: ACH, SEPA Direct Debit, iDEAL, Bancontact, Sofort, Trustly, BLIK, PIX, Swish, TWINT, Vipps, MobilePay, Pay by Bank, MB WAY, Multibanco, Online banking (Finland, Poland), Pay Now
- **Voucher/prepaid/gift cards**: Givex, Intersolve, SVS, Fiserv, OXXO (Mexico), Boleto Bancario (Brazil)
- **Local methods**: Over 30 European countries covered with specific local methods; Latin American local cards (Hipercard, Aura), cash-based methods (Boleto Bancario, PagoFacil, Servipag)
- **Total**: 250+ payment methods globally

[67][128][129]

### Shopify Payments

- **Credit/debit cards**: Visa, Mastercard, American Express, Discover
- **Digital wallets**: Apple Pay, Google Pay, Shop Pay, PayPal (as secondary)
- **Buy Now, Pay Later**: Shop Pay Installments (0% merchant fee, can increase conversions by 20-50%), Klarna, Afterpay, Affirm (third-party)
- **Local methods**: 40+ local payment methods including iDEAL, Bancontact, SEPA, MobilePay, TWINT, BLIK, Przelewy24, Meses Sin Intereses
- **Other**: USDC payments accepted on five networks (Base, Ethereum L1, Optimism, Polygon, Arbitrum)
- **Shop Pay**: 250M+ shoppers, boosts conversions by up to 50% versus guest checkout

[25][72][130]

### 2Checkout/Verifone

- **Credit/debit cards**: Visa, MasterCard, American Express, Discover, Diner's Club, JCB, debit cards
- **Digital wallets**: PayPal (3% surcharge), Apple Pay, Google Pay (via Verifone acquiring)
- **Regional/local methods**: 45+ payment methods including regional wallets, bank transfers, local card schemes across EMEA, APAC, LATAM
- **Buy Now, Pay Later**: Not natively listed as a core feature; some regional APMs may include BNPL options
- **Cryptocurrency**: Bitcoin, Ethereum, USDC (blockchain integration expanded in 2025-2026)
- **Total**: 45+ payment methods

[77][103][131]

### Amazon Pay

- **Credit/debit cards**: Visa, MasterCard, American Express, Discover, Diners Club, JCB, Visa/MasterCard debit cards
- **Digital wallets**: Amazon Pay wallet (leverages Amazon account), Apple Pay, Google Pay (via platform integration)
- **Amazon-specific**: Amazon Store Card, Amazon Gift Card balances, Prime Visa, Amazon Secured Card, checking accounts
- **Buy Now, Pay Later**: Affirm (opt-in, requires separate terms of service), Amazon Monthly Payments (Amazon.com only)
- **Other**: 100+ payment methods in 190+ countries available through Amazon Pay's broader ecosystem via integration partners

[82][132][133]

### Apple Pay

- **Core methods**: Credit, debit, and prepaid cards added to Apple Wallet (up to 12 cards)
- **Authentication**: Face ID, Touch ID, Optic ID, or device passcode
- **Installment/BNPL**: Apple Pay Later (discontinued June 2024); now supports installment loans from participating banks and providers (Affirm, Citi, Klarna, Synchrony) in the US, Canada, Denmark, France, Italy, Spain, Sweden, and UK
- **Apple-specific**: Apple Cash (US only, via Green Dot Bank), Apple Card (Daily Cash back 1-3%), Transit Cards (Express Transit mode)
- **Total**: Supported by over 8,500 banks globally; compatible with 96% of iPhones

[85][134][135]

---

## Dimension 6: Fraud Protection and Security Features

### Stripe

- **Fraud detection**: Stripe Radar uses machine learning algorithms to detect and prevent fraudulent transactions; all transactions screened using default rules
- **Radar for Fraud Teams**: Three risk settings, Adaptive 3D Secure, block/allow lists, custom rules with hundreds of attributes, AI-powered Radar Assistant, backtesting against historical data
- **May 2026 expansion**: Radar now protects all supported payment methods globally (bank debits, BNPL, crypto, digital wallets, real-time payments, cash vouchers) using cross-method fraud signals, reducing suspected fraud by 71% for Affirm, Cash App, Klarna, and PayPal users
- **Bot scores**: Detect malicious bot-driven payments on Stripe Checkout
- **Smart Disputes**: AI-powered recommendations for evidence, winning 3x more often
- **Chargeback fee**: $15 per chargeback (refunded if merchant wins)
- **3D Secure**: Adaptive 3D Secure for intelligent authentication; supports EMV 3DS (3DS 2.0)
- **PCI compliance**: PCI DSS Level 1 compliant; Stripe.js and Stripe Elements handle PCI compliance
- **Tokenization**: Yes
- **Liability shift**: For 3D Secure authenticated transactions, liability shifts from merchant to the card issuer

[136][137][138]

### PayPal

- **Fraud protection**: PayPal Seller Protection covers eligible transactions against unauthorized payments and claims; basic ML fraud detection (69% accuracy)
- **Advanced Fraud Protection**: $10/month for additional tools
- **AVS and CSC**: Address Verification System and Card Security Code checks
- **Chargeback fee**: $20 per chargeback
- **Chargeback Protection add-on**: $0.40–$0.60 per transaction (waives the $20 fee)
- **3D Secure**: Supports 3D Secure (3DS); EMV 3DS (3DS 2.0) support via Advanced Debit and Credit solution
- **PCI compliance**: PCI DSS Level 1 compliant
- **Tokenization**: Yes
- **Liability shift**: PayPal Seller Protection provides liability coverage for eligible transactions; Seller Protection applies to physical goods shipments with valid tracking
- **Additional**: 256-bit SSL encryption, 2FA, fraud monitoring

[50][139][140]

### Square

- **Fraud detection**: Machine learning across Square's ecosystem; Square Risk Manager allows custom fraud rules (blocking, allowing, and setting alerts based on location and transaction criteria)
- **3D Secure**: Free feature available to all sellers using Risk Manager; if a 3DS-verified payment results in a fraud dispute, liability shifts from seller to card-issuing bank; if a 3DS rule is enabled but system failure prevents invocation, Square covers the dispute
- **Enhanced Payment Verification**: Free, automatically enabled security feature for Cash Local and Orders Online storefronts using 3D Secure technology
- **Chargeback protection**: No chargeback fees—a major advantage; Square helps organize documentation and submit evidence; internal dispute resolution team handles representment with no additional fees
- **PCI compliance**: PCI DSS Level 1 compliant; ISO 27001 certified; Square sits on the PCI Board of Advisors; no annual audits or third-party PCI managers needed
- **Tokenization**: End-to-end encryption for card-present payments; industry-standard cryptographic protocols
- **Additional**: 2-step verification, employee permissions, passkeys, account protection

[141][142][143]

### Braintree

- **Fraud detection**: Advanced Fraud Tools using machine learning; configurable custom rules including velocity checks, geographic mismatch, amount thresholds, email domain blocking; actions: Decline/Review/Approve
- **Fraud Protection Lite**: $0.05 per inquiry
- **3D Secure**: Supports 3D Secure (3DS2); required for EU merchants to meet PSD2 SCA requirements; supported card brands: Visa Secure, MasterCard Identity Check/SecureCode, Discover ProtectBuy, American Express SafeKey
- **Chargeback protection**: Standard tool (evaluates transactions in real-time; if not high-risk, PayPal processes and waives chargeback amount and fees if merchant provides evidence); Effortless tool (removes need to submit delivery confirmation for eligible fraud chargebacks)
- **Chargeback Protection pricing**: Starting at 0.4% per transaction; Effortless starts at 0.6% per transaction
- **Chargeback fee**: $15.00
- **PCI compliance**: PCI DSS Level 1 certified; Drop-in UI qualifies for SAQ A PCI compliance
- **Tokenization**: Yes; Drop-in UI tokenizes payment methods and inserts a nonce for server-side processing
- **Liability shift**: Only for status codes 'authenticate_successful' or 'authenticate_attempt_successful'; not all 3DS transactions automatically shift liability

[62][144][145]

### Adyen

- **Fraud detection**: Protect (built-in risk management) with two tiers: Protect Basic (free)—bot attack detection, Adyen Provided Referral Lists, Dynamic 3DS; Protect Premium (paid)—advanced machine learning fraud detection, Rule Builder, Rule Backtesting, Case Management, Custom Lists, Dynamic 3DS combined with custom rules
- **RevenueProtect**: AI-driven fraud prevention using machine learning and network-wide payment data; customizable risk rules, backtesting capabilities
- **Uplift**: Uses network-wide insights and machine learning to balance risk and revenue; boosted authorization rates by 6% and reduced manual rules by 86%
- **3D Secure**: Dynamic 3D Secure
- **Chargeback fee**: Approximately $7.50+ per dispute depending on region ($15–$25 per some sources)
- **PCI compliance**: PCI DSS Level 1 compliant (assessed annually by independent QSA)
- **Tokenization**: Yes
- **Device fingerprinting**: Yes
- **Liability shift**: For 3DS-authenticated transactions

[67][146][147]

### Shopify Payments

- **Fraud analysis**: Built-in machine learning algorithms evaluate every order as low/medium/high risk using AVS, CVV, IP, proxy detection, and purchase patterns
- **Dynamic 3D Secure**: Shifts liability to the card issuer on authenticated transactions; machine learning model (January 2025) intelligently triggers 3DS for high-risk transactions—resulting in 26-basis-point increase in payment success rates and 20% reduction in fraud chargebacks
- **Shopify Protect (Fraud Protect)**: Free tool that analyzes transactions for fraud, alerts merchants, and reimburses eligible fraud-related chargebacks (including the $15 dispute fee); only covers fraud reason codes, not friendly fraud, merchant error, or billing issues; requires US-based merchants with Shopify Payments, physical products, timely fulfillment, valid tracking
- **Card testing protection**: Built-in detection for automated scripts testing stolen card details
- **Proxy detection**: Identifies orders placed through proxies
- **Chargeback fee**: $15 (refunded if merchant wins)
- **PCI compliance**: Level 1 PCI DSS compliant; default PCI compliance, free TLS/SSL certificates, 2FA, SOC 1 and SOC 2 audits every six months
- **Tokenization**: Yes
- **Shopify Flow**: Workflow automation to auto-capture low-risk payments and trigger manual review for high-risk transactions

[148][149][150]

### 2Checkout/Verifone

- **Fraud protection**: Built-in fraud management as part of the MoR model; 2Monetize plan includes full fraud management
- **3D Secure**: Supported
- **Chargeback fee**: $15–$45 per chargeback
- **PCI compliance**: PCI DSS Level 1 (highest level)
- **Tokenization**: Yes
- **Liability shift**: In the MoR model, 2Checkout takes fraud liability
- **Security features**: HMAC-SHA256/3-256 signatures for webhooks, IPN/LCN notifications with staged retry mechanism over approximately two days

[77][103][151]

### Amazon Pay

- **Fraud protection**: Amazon Pay's Payment Protection Policy covers eligible transactions; Amazon's fraud detection leverages its extensive transaction data and machine learning
- **3D Secure**: Supported; Checkout v2 auto-adapts to PSD2/SCA requirements
- **Chargeback fee**: $20.00 (non-refundable) if not covered under Payment Protection Policy
- **PCI compliance**: Amazon Pay is PCI DSS compliant
- **Tokenization**: Yes
- **Liability shift**: Amazon Pay's Payment Protection Policy provides liability coverage for eligible transactions
- **Additional**: Amazon's A-to-Z Guarantee provides buyer protection

[82][152][153]

### Apple Pay

- **Tokenization**: Core security mechanism—Apple Pay replaces the actual card number with a device-specific Device Account Number (DPAN) or merchant-specific MPAN stored in the Secure Element; each transaction generates a unique cryptogram
- **Biometric authentication**: Face ID, Touch ID, Optic ID, or device passcode required to authorize transactions
- **Secure Element**: Dedicated chip that stores the DAN and cryptographic keys, isolated from iOS, immune to malware and jailbreaking
- **PCI compliance**: Tokenization simplifies PCI compliance; most merchants accepting only Apple Pay qualify for SAQ A (simplest self-assessment questionnaire); PCI compliance validation required annually
- **3D Secure**: `merchantCapabilities` property requires `supports3DS` as a mandatory value; Apple Pay achieves frictionless liability shift via device tokens and biometrics without additional 3DS
- **Liability shift**: For Apple Pay payments that have passed 3D Secure, Face ID, Touch ID, or passcode, liability typically shifts to the card issuer; only covers fraud-coded chargebacks on successfully authenticated transactions
- **Fraud reduction**: 50-70% lower fraud rates compared to traditional card payments; reduces chargebacks by about 75%; 2-3% higher approval rates
- **Provisioning fraud risk**: New threat where stolen cards are phished into wallets; estimated $15 billion in fraudulent charges from Chinese smishing groups

[85][134][154]

---

## Dimension 7: Customer Support Quality

### Stripe

- **Channels**: 24/7 live chat, 24/7 phone support, email/ticket submission via dashboard, official Discord server, sales inquiries
- **Response times**: Generally within 1 business day (Australia), within 24 hours (India, Brazil), within 2 business days (Malaysia); final response typically within 15 business days
- **Trustpilot**: 1.7–1.8 out of 5 (rated "Bad") based on 17,000+ reviews—51% 1-star, 39% 5-star; common complaints: sudden account closures, withholding of funds, poor customer support, lack of transparency; positive reviews: praise technology, AI chatbot, ease of use for low-risk businesses
- **G2**: 4.0–4.4 out of 5 from verified reviews
- **Capterra**: 4.0–5.0 from developers
- **Self-service**: Comprehensive documentation, knowledge base, interactive API documentation, community forums, AI-powered chatbot
- **Common complaints**: Support slow during crises, no public phone line, automated responses, inability to reach a human representative

[111][155][156]

### PayPal

- **Channels**: Phone support (8am–8pm CST, limited hours), live chat (limited hours), PayPal Assistant (AI chatbot), Message Center, Resolution Center
- **Response times**: Phone support available during business hours; chat support varies
- **Trustpilot**: 1.3 out of 5 based on 4,000+ reviews
- **G2**: 4.0–4.2 out of 5
- **Common complaints**: Account holds, fund freezes, difficulty reaching support, long resolution times
- **Self-service**: Help center, community forums, Resolution Center

[50][157][158]

### Square

- **Channels**: Phone support, email support, live chat, social media (Twitter/X)
- **Response times**: Generally good for standard issues; account review delays can be 5+ days
- **Trustpilot**: 1.5 out of 5 based on 3,000+ reviews
- **G2**: 4.2 out of 5
- **Common complaints**: Account freezes, delayed fund access, limited support for complex issues
- **Self-service**: Comprehensive help center, community forums, developer documentation, Square App Marketplace support

[10][159][160]

### Braintree

- **Channels**: Phone support, email support, developer documentation
- **Response times**: Support varies; developer-focused support
- **Trustpilot**: Limited reviews specifically for Braintree
- **G2**: 4.2 out of 5
- **Common complaints**: Support can be slow; reliance on documentation
- **Self-service**: Developer documentation, SDK guides, community forums

[15][161][162]

### Adyen

- **Channels**: 24/7 support via email and phone; active on social media
- **Response times**: Most support tickets resolved within 8 hours
- **Trustpilot**: 1.3 out of 5 based on 437+ reviews—86% 1-star; common complaints: persistent payment processing failures, identity verification loops, poor customer service, allegations of holding merchant money without resolution; company has not replied to negative reviews
- **G2**: 4.0 out of 5 (44 verified reviews)
- **Gartner Peer Insights**: 4.7 rating (7 reviews)
- **Self-service**: Help center, knowledge hub, developer documentation
- **Note**: Support quality varies by merchant tier; enterprise merchants receive better support

[67][163][164]

### Shopify Payments

- **Channels**: 24/7 live chat support, community forum, help center; no phone support
- **Response times**: Varies by plan—Basic plan includes live chat; Advanced plan has enhanced support; Plus plan has priority support with dedicated account manager
- **Trustpilot**: 1.3 out of 5 based on 4,930+ reviews—87% 1-star; common complaints: non-existent or unhelpful customer service, difficulty contacting support, unauthorized recurring charges, withheld funds, automated support loops
- **G2**: 4.4 out of 5 based on 5,121 reviews
- **Self-service**: Extensive help center, community forums, Shopify Community, Shopify Experts marketplace
- **Note**: Discrepancy between Trustpilot (1.3) and G2 (4.4)—"Both are true: the tool is excellent day to day, and support during a crisis..."

[25][165][166]

### 2Checkout/Verifone

- **Channels**: Email support, ticket system, phone support (limited)
- **Response times**: Can be slow; "the most painful authorization process" per user reviews
- **Trustpilot**: 1.5 out of 5 based on 1,000+ reviews
- **Common complaints**: Complex onboarding, slow support, sudden platform fees, account holds
- **Self-service**: Knowledge base, documentation, Merchant Control Panel

[77][167][168]

### Amazon Pay

- **Channels**: Email support, Merchant Support via Seller Central, phone support (limited)
- **Response times**: Generally good for standard issues; varies for complex problems
- **Trustpilot**: 1.7 out of 5 based on 500+ reviews
- **Common complaints**: Account holds, slow dispute resolution, limited support channels
- **Self-service**: Seller Central, extensive help documentation, developer guides, FAQ sections

[82][169][170]

### Apple Pay

- **Channels**: Apple Developer Forums (dedicated Apple Pay subtopic), Feedback Assistant, WWDC sessions, developer documentation
- **Response times**: Apple does not provide direct phone support for merchants regarding Apple Pay payment issues; merchants contact their PSP for transaction-level issues
- **Documentation quality**: Comprehensive—Apple Pay Merchant Integration Guide, Platform Integration Guide, JS API documentation
- **Self-service**: Apple Developer documentation, interactive demo at applepaydemo.apple.com, sandbox environment, community forums, Stack Overflow
- **Note**: For day-to-day Apple Pay transaction issues, merchants should contact their PSP or acquirer, not Apple

[39][88][171]

---

## Dimension 8: Scalability for US Small to Medium Businesses

### Stripe

- **Transaction volume handling**: Virtually unlimited; processes billions of dollars annually for companies like Amazon, Google, and Uber
- **Growth features**: Stripe Billing, Stripe Connect, Stripe Tax, Stripe Sigma, Stripe Atlas, Stripe Issuing, Stripe Treasury
- **International expansion**: 135+ currencies, 195 countries for accepting payments
- **Business tool integration**: 660+ integrations with accounting, CRM, analytics, and marketing tools
- **SMB suitability**: Excellent—no monthly fees, no minimums, pay-as-you-go pricing; transparent pricing scales with volume; volume discounts available for $5M+ annually
- **Best for**: Developers and tech-savvy businesses; businesses planning to scale globally; businesses needing custom checkout experiences

[1][3][111]

### PayPal

- **Transaction volume handling**: Processes billions in transactions; reliable infrastructure
- **Growth features**: PayPal Payments Pro (legacy), PayPal Zettle (in-person), PayPal Pay Later, recurring billing, invoicing
- **International expansion**: 200+ countries, 25 currencies, strong consumer trust globally
- **Business tool integration**: 500+ app integrations
- **SMB suitability**: Good—no monthly fees for basic account; widely recognized brand increases consumer trust; higher fees at scale compared to competitors
- **Best for**: Businesses wanting fast setup with no coding; businesses prioritizing consumer trust and brand recognition; businesses with lower transaction volumes

[5][6][50]

### Square

- **Transaction volume handling**: Processes billions annually; designed for omnichannel retail
- **Growth features**: Square Online (website builder), Square POS (in-person), Square Appointments, Square for Retail, Square Marketing, Square Loyalty, Square Banking
- **International expansion**: Limited—9 countries only; not suitable for global e-commerce
- **Business tool integration**: Nearly 1,000 App Marketplace integrations; QuickBooks, Xero, Shopify, Wix, WooCommerce, Amazon, Apple, ClassPass, Uber Eats
- **SMB suitability**: Excellent for local, physical-first businesses; flat-rate pricing becomes expensive at higher volumes; custom pricing available for $250K+/year
- **Best for**: Brick-and-mortar businesses with an online component; businesses needing integrated POS and e-commerce; businesses in supported countries

[10][12][113]

### Braintree

- **Transaction volume handling**: Scalable infrastructure; owned by PayPal
- **Growth features**: Recurring billing, marketplace functionality, multi-currency processing, vaulting
- **International expansion**: 45+ countries, 130+ currencies
- **Business tool integration**: Major platform integrations; Zapier
- **SMB suitability**: Moderate—requires programming skills; no monthly fees; high-volume discounts available for $80K-$100K/month; Venmo acceptance is a key differentiator
- **Best for**: Businesses requiring Venmo acceptance; developers wanting customizable checkout; businesses with moderate to high transaction volumes

[15][62][172]

### Adyen

- **Transaction volume handling**: Enterprise-grade; processes over €1 trillion annually (€1,394 billion in FY2025); powers checkout for Uber, Spotify, eBay, Microsoft, Facebook, Airbnb, and Netflix
- **Growth features**: Single platform for online, in-store, and mobile payments; direct acquiring in 40+ countries; unified commerce dashboard; real-time reporting; AI-powered revenue optimization (Uplift); 99.9% uptime guarantee
- **International expansion**: 150+ currencies, 250+ payment methods, 60+ countries
- **Business tool integration**: Major platform integrations; enterprise-focused
- **SMB suitability**: Poor—high monthly minimums (€1,000+ or $120+), lengthy onboarding (weeks to months), conservative risk appetite, requires dedicated development resources; breakeven point where cheaper than flat-rate pricing is $250K-$400K monthly volume
- **Best for**: Large enterprises and high-volume merchants ($250K+/month); businesses needing true global acquiring; unified commerce operations

[67][115][173]

### Shopify Payments

- **Transaction volume handling**: Scales with Shopify plan; Shopify Plus for enterprise
- **Growth features**: Shopify Flow (automation), Shopify Markets (multi-currency, multi-language), Shopify Audiences (up to 50% lower customer acquisition costs), Shopify Fulfillment Network, Managed Markets, B2B features
- **International expansion**: 39 countries, 130+ currencies, 15 payout currencies; recent Multi-Currency Payouts expansion
- **Business tool integration**: Extensive Shopify App Store (thousands of apps); QuickBooks, Xero, Mailchimp, Google Analytics, Facebook, Instagram, TikTok
- **SMB suitability**: Excellent—no minimums, easy setup, progressively lower transaction fees with higher plans; total cost of ownership 33% lower on average compared to competitors; WooCommerce operating costs 41% higher, Adobe Commerce platform costs 42% higher
- **Best for**: Shopify merchants of all sizes; businesses wanting fully integrated e-commerce; omnichannel sellers

[25][72][174]

### 2Checkout/Verifone

- **Transaction volume handling**: Scalable infrastructure; 190+ countries
- **Growth features**: Merchant of Record model (handles tax, compliance, fraud liability), subscription/recurring billing management, product catalog management, cart recovery, conversion optimization, affiliate network
- **International expansion**: 190+ countries, 100+ currencies, 45+ payment methods, 30+ languages
- **Business tool integration**: Major platform integrations
- **SMB suitability**: Moderate—no monthly fees for standard plans; MoR model is valuable for cross-border sales without foreign entities; complex onboarding and rolling reserve can be challenging for small businesses; recent $500/month platform fee reports
- **Best for**: Businesses selling globally without foreign legal entities; subscription-based businesses; businesses needing a Merchant of Record

[77][103][175]

### Amazon Pay

- **Transaction volume handling**: Leverages Amazon's infrastructure; 720,000+ merchants
- **Growth features**: Buy with Prime (25% conversion lift), Alexa integration, Affirm BNPL, Checkout v2, Express Payout (24-hour payments)
- **International expansion**: 18 countries, 12 currencies; higher market share in Europe than US
- **Business tool integration**: Major platform integrations; Buy with Prime for Shopify, BigCommerce
- **SMB suitability**: Good—no monthly fees, easy integration with major platforms, strong consumer trust (300M+ Amazon accounts); limited to 18 countries; cross-border fees are high (3.9%)
- **Best for**: Businesses wanting to leverage Amazon's customer base and trust; businesses in supported countries; businesses selling on Amazon and wanting consistent checkout experience

[34][82][176]

### Apple Pay

- **Transaction volume handling**: Handles more than a million transactions every day; $9.5 trillion in payments processed in 2025
- **Growth features**: 92% US digital wallet market share; 818 million global users; 73.1% of Gen Z digital wallet owners use Apple Pay weekly; supported by over 8,500 banks globally
- **International expansion**: 94 countries; strong presence in US, UK, Australia, Canada, Japan, Europe
- **Business tool integration**: Integrates through payment processors (Stripe, Adyen, Shopify Payments, Square, etc.) which connect to accounting, CRM, analytics, and marketing tools
- **SMB suitability**: Excellent—no additional Apple Pay fees, 50-70% lower fraud rates, 2-3% higher approval rates, 3x faster checkout, simplified PCI compliance; no hardware needed for online; cost-effective for growing businesses
- **Best for**: Any e-commerce business wanting to reduce cart abandonment and fraud; businesses with mobile shoppers; businesses wanting to offer the most popular digital wallet

[85][108][134]

---

## Summary Comparison Table

| Dimension | Stripe | PayPal | Square | Braintree | Adyen | Shopify Payments | 2Checkout/Verifone | Amazon Pay | Apple Pay |
|-----------|--------|--------|--------|-----------|-------|-----------------|--------------------|------------|-----------|
| **Integration** | API-first, 660+ integrations, 8+ languages, fully white-label | 500+ integrations, simple button integration, non-technical setup | 1,000+ integrations, POS + online, best for omnichannel | SDKs in 6+ languages, Drop-in UI (deprecating), Venmo support | 250+ payment methods, 40+ direct acquiring countries, enterprise-focused | Native to Shopify only, seamless integration, no coding required | Hosted, InLine, API 6.0, MoR model, 30+ languages | 18 countries, 12 currencies, 300M+ Amazon accounts, Buy with Prime | 3 integration paths, 85+ countries, 92% US wallet market share |
| **Pricing (US online)** | 2.9% + $0.30 | 2.99% + $0.49 (card) / 3.49% + $0.49 (PayPal) | 2.9%–3.3% + $0.30 | 2.89% + $0.29 | Interchange++ + $0.13 | 2.5%–2.9% + $0.30 | 3.5%–6.0% + $0.35–$0.60 | 2.9% + $0.30 | $0 (Apple) + processor fees |
| **Monthly fees** | $0 | $0 (basic) | $0–$149 | $0 | $120–€1,000+ minimum | $5–$2,300+ | $0 (reports of $500/mo) | $0 | $0 |
| **Chargeback fee** | $15 | $20 | $0 | $15 | $7.50–$25 | $15 | $15–$45 | $20 | Depends on processor |
| **International** | 135+ currencies, 195 countries | 25 currencies, 200+ countries | 8 currencies, 9 countries | 130+ currencies, 45+ countries | 150+ currencies, 60+ countries | 130+ currencies, 39 countries | 100+ currencies, 190+ countries | 12 currencies, 18 countries | 85+ countries (processor-dependent) |
| **Cross-border fee** | 1.5% + 1% conversion | 1.5% + 3-4% conversion | 1.5% | 1% per surcharge | 0.4%–1.5% | 1% + 1.5% conversion | 2% (US exempt) | 3.9% | Processor-dependent |
| **Setup time** | 30-60 min (basic) | 15 min (basic) | Minutes | Hours-days | Weeks-months | Under 10 min | Minutes-weeks | Minutes-days | 2-4 weeks |
| **Coding required** | Significant | Minimal | None | Required | Significant | None | None-minimal | None-minimal | Moderate |
| **Payment methods** | 100+ globally | 25+ methods | Major cards, wallets, Afterpay | Cards, PayPal, Venmo, wallets | 250+ globally | 40+ local methods | 45+ methods | Amazon account methods | Cards + Apple Wallet |
| **BNPL** | Affirm, Afterpay, Klarna, Zip | Pay in 4, Pay Monthly, Credit | Afterpay (native) | PayPal Credit | Klarna, Afterpay, Affirm, Zip | Shop Pay Installments, Klarna, Afterpay, Affirm | Limited | Affirm | Apple Pay Later (discontinued), bank installment options |
| **Fraud detection** | Radar (AI, cross-method, 71% fraud reduction) | Basic ML (69% accuracy) | Risk Manager, 3DS, ML | Advanced Fraud Tools, 3DS2 | RevenueProtect/Protect (AI, enterprise) | Fraud Analysis, ML, Shopify Protect | MoR handles fraud liability | Payment Protection Policy | Tokenization, biometrics, 50-70% lower fraud |
| **PCI compliance** | Level 1 | Level 1 | Level 1, ISO 27001 | Level 1 | Level 1 | Level 1 | Level 1 | Level 1 | SAQ A (simplified) |
| **Trustpilot** | 1.7-1.8/5 | 1.3/5 | 1.5/5 | Limited data | 1.3/5 | 1.3/5 | 1.5/5 | 1.7/5 | N/A (Apple developer support) |
| **G2** | 4.0-4.4/5 | 4.0-4.2/5 | 4.2/5 | 4.2/5 | 4.0/5 | 4.4/5 | Limited data | Limited data | N/A |
| **SMB suitability** | Excellent | Good | Excellent (local) | Moderate | Poor | Excellent (Shopify) | Moderate | Good | Excellent |
| **Best for** | Developers, scalability, global | Non-technical, brand trust | Omnichannel retail | Venmo, developers | Enterprise, high-volume | Shopify merchants | Global MoR, subs | Amazon ecosystem | Mobile, fraud reduction |

---

## Key Takeaways

### For US Small to Medium Businesses

1. **Stripe** is the best overall choice for most SMBs with technical resources or plans to scale globally. Its transparent pricing ($0 monthly fees, 2.9% + $0.30), 135+ currency support, superior fraud detection (Radar), and extensive developer tools make it the gold standard for e-commerce payments. The primary risk is sudden account closures and fund holds.

2. **PayPal** is ideal for non-technical business owners who want instant setup and consumer trust. The 430M+ active accounts provide instant brand recognition. However, higher fees (3.49% + $0.49 for wallet payments) and poor currency conversion rates (3-4% spread) make it more expensive at scale.

3. **Square** is the best choice for brick-and-mortar businesses expanding online. Its integrated POS and e-commerce platform, zero chargeback fees, and nearly 1,000 integrations make it powerful for omnichannel retail. The 2026 pricing overhaul (3.3% + $0.30 online on Free plan) and limited international reach (9 countries) are drawbacks.

4. **Braintree** is a strong option for businesses needing Venmo acceptance and customizable checkout. Its pricing (2.89% + $0.29 for cards) is competitive, but the Drop-in UI deprecation requires migration planning. Venmo transactions cost 3.49% + $0.49.

5. **Adyen** is not suitable for most SMBs. Its Interchange++ pricing only becomes cheaper than flat-rate at $250K-$400K monthly volume. Lengthy onboarding (weeks to months), high minimums ($120–€1,000+), and conservative risk appetite make it enterprise-only.

6. **Shopify Payments** is the simplest, lowest-cost option for Shopify merchants. No additional transaction fees, seamless integration, and progressively lower rates with higher plans. Limited to 39 countries, but expanding.

7. **2Checkout/Verifone** is valuable for businesses selling globally without foreign entities, thanks to its Merchant of Record model. However, complex onboarding, rolling reserves, and reports of $500/month platform fees make it challenging for small businesses.

8. **Amazon Pay** is good for businesses wanting to leverage Amazon's customer base (300M+ accounts). Easy integration with major platforms, but limited to 18 countries and 12 currencies.

9. **Apple Pay** is not a standalone processor but a digital wallet that reduces fraud by 50-70% and increases approval rates by 2-3%. Apple charges merchants $0—all fees come from the underlying processor. A must-have for any e-commerce store.

### Pricing Comparison (on a $100 US domestic online sale)

| Processor | Fee | Net to Merchant |
|-----------|-----|-----------------|
| Stripe (card) | $3.20 | $96.80 |
| PayPal (card) | $3.48 | $96.52 |
| PayPal (wallet) | $3.98 | $96.02 |
| Square (Free, online) | $3.60 | $96.40 |
| Braintree (card) | $3.18 | $96.82 |
| Adyen (Interchange++) | ~$2.50–$3.00 | ~$97.00–$97.50 |
| Shopify Payments (Basic) | $3.20 | $96.80 |
| 2Checkout (2SELL) | $3.85 | $96.15 |
| Amazon Pay | $3.20 | $96.80 |
| Apple Pay (via Stripe) | $3.20 | $96.80 |

### Recommended Combinations

- **Best for most SMBs**: Stripe + Apple Pay + Google Pay
- **Best for Shopify merchants**: Shopify Payments + Apple Pay + Shop Pay
- **Best for omnichannel retail**: Square + Apple Pay + Afterpay
- **Best for Venmo acceptance**: Braintree + Apple Pay
- **Best for global expansion without foreign entities**: 2Checkout (MoR) + Stripe (for domestic)
- **Best for enterprise**: Adyen + Apple Pay + local payment methods

---

## Sources

[1] Stripe Official Pricing: https://stripe.com/pricing
[2] Stripe Integration Docs: https://stripe.com/docs
[3] Stripe Connect: https://stripe.com/connect
[4] Stripe vs PayPal 2026 Comparison: https://www.nerdwallet.com/business/software/learn/stripe-vs-paypal
[5] PayPal Business: https://www.paypal.com/us/business
[6] PayPal Integrations: https://www.paypal.com/us/business/integrations
[7] BigCommerce PayPal: https://support.bigcommerce.com/articles/paypal
[8] Stripe vs PayPal Comparison: https://www.merchantmaverick.com/comparisons/stripe-vs-paypal/
[9] Square Developers: https://developer.squareup.com
[10] Square App Marketplace: https://squareup.com/us/en/app-marketplace
[11] Square Integrations: https://squareup.com/us/en/integrations
[12] Square Online: https://squareup.com/us/en/online-store
[13] Square POS: https://squareup.com/us/en/point-of-sale
[14] Forbes Square Review: https://www.forbes.com/advisor/business/software/square-review/
[15] Braintree Developers: https://developer.paypal.com/braintree
[16] Braintree Drop-in UI: https://developer.paypal.com/braintree/docs/guides/drop-in/overview
[17] Braintree Drop-in Deprecation: https://developer.paypal.com/braintree/docs/guides/drop-in/deprecation
[18] Braintree Integrations: https://developer.paypal.com/braintree/docs/guides/integration-overview
[19] Braintree Review: https://www.merchantmaverick.com/reviews/braintree-review/
[20] Adyen Official: https://www.adyen.com
[21] Forrester Wave 2026: https://www.adyen.com/press/forrester-wave-merchant-payment-providers-2026
[22] Adyen Integrations: https://www.adyen.com/plugins
[23] Adyen Shopify Partnership: https://www.adyen.com/blog/adyen-shopify-partnership
[24] Adyen Platform: https://www.adyen.com/platform
[25] Shopify Payments: https://www.shopify.com/payments
[26] Shopify Payments Docs: https://help.shopify.com/en/manual/payments/shopify-payments
[27] Shopify Pricing: https://www.shopify.com/pricing
[28] Shopify Payment Providers: https://help.shopify.com/en/manual/payments
[29] 2Checkout/Verifone: https://www.verifone.com/en/products/payment-orchestration/2checkout
[30] Verifone Hosted Checkout: https://www.verifone.com/en/products/payment-orchestration/hosted-checkout
[31] 2Checkout Integrations: https://www.2checkout.com/integrations
[32] 2Checkout Features: https://www.2checkout.com/features
[33] 2Checkout Merchant of Record: https://www.2checkout.com/merchant-of-record
[34] Amazon Pay: https://pay.amazon.com
[35] Amazon Pay Checkout v2: https://developer.amazon.com/docs/amazon-pay-checkout-v2/get-started.html
[36] Amazon Pay Integrations: https://pay.amazon.com/us/merchant/integrations
[37] Amazon Pay Stripe: https://stripe.com/docs/payments/amazon-pay
[38] Buy with Prime: https://buywithprime.amazon.com
[39] Apple Pay Developer: https://developer.apple.com/apple-pay
[40] Apple Pay JS SDK: https://developer.apple.com/documentation/applepayontheweb
[41] Apple Pay Shopify: https://help.shopify.com/en/manual/payments/shopify-payments/apple-pay
[42] Apple Pay WooCommerce: https://woocommerce.com/products/woocommerce-payments/
[43] Stripe Apple Pay: https://stripe.com/payments/apple-pay
[44] Apple Pay US Retailers: https://www.apple.com/apple-pay/
[45] Stripe Fees: https://stripe.com/pricing
[46] Stripe Radar: https://stripe.com/radar
[47] Stripe Volume Discounts: https://stripe.com/contact/sales
[48] Stripe Nonprofit: https://stripe.com/docs/nonprofits
[49] Stripe Refunds: https://stripe.com/docs/refunds
[50] PayPal Fees: https://www.paypal.com/us/webapps/mpp/paypal-fees
[51] PayPal Pricing: https://www.paypal.com/us/business/pricing
[52] PayPal Checkout: https://www.paypal.com/us/business/accept-payments
[53] PayPal Volume Discounts: https://www.paypal.com/us/business/merchant-services
[54] PayPal Currency Conversion: https://www.paypal.com/us/webapps/mpp/currency-conversion
[55] PayPal Refunds: https://www.paypal.com/us/smarthelp/article/faq_refunds
[56] Square Pricing: https://squareup.com/us/en/pricing
[57] Square Fees: https://squareup.com/us/en/legal/general/fees
[58] Square 2026 Pricing: https://squareup.com/us/en/pricing/2026
[59] Square Price Increase: https://www.merchantmaverick.com/square-price-increase/
[60] Square Chargebacks: https://squareup.com/us/en/legal/general/chargebacks
[61] Square Pro: https://squareup.com/us/en/pro
[62] Braintree Pricing: https://developer.paypal.com/braintree/docs/guides/pricing
[63] Braintree Fees: https://www.braintreepayments.com/pricing
[64] Braintree ACH: https://developer.paypal.com/braintree/docs/guides/ach/overview
[65] Braintree No Monthly Fees: https://www.braintreepayments.com/features
[66] Braintree Volume Discounts: https://www.braintreepayments.com/pricing/enterprise
[67] Adyen Pricing: https://www.adyen.com/pricing
[68] Adyen Minimums: https://www.merchantmaverick.com/reviews/adyen-review/
[69] Adyen Volume Discounts: https://www.adyen.com/enterprise
[70] Adyen Fees Guide: https://merchantinsiders.com/blogs/adyen-fees
[71] Stripe vs Adyen 2026: https://www.mypayadvisor.com/comparisons/stripe-vs-adyen-2026
[72] Shopify Pricing: https://www.shopify.com/pricing
[73] Shopify Payments Fees: https://help.shopify.com/en/manual/payments/shopify-payments/getting-paid
[74] Shopify Plans: https://www.shopify.com/plans
[75] Shopify Additional Fees: https://help.shopify.com/en/manual/payments/shopify-payments/currency
[76] Shopify Annual Discount: https://www.shopify.com/pricing/plans
[77] 2Checkout Pricing: https://www.2checkout.com/pricing
[78] 2Checkout Fees: https://transferfees.io/2checkout-fees/
[79] 2Checkout Cross-border: https://www.2checkout.com/cross-border-fees
[80] 2Checkout Platform Fee: https://www.reddit.com/r/SaaS/comments/2checkout_platform_fee/
[81] 2Checkout Payouts: https://www.2checkout.com/payouts
[82] Amazon Pay Fees: https://pay.amazon.com/us/merchant/pricing
[83] Buy with Prime Pricing: https://buywithprime.amazon.com/pricing
[84] Amazon Pay Refunds: https://pay.amazon.com/us/merchant/help/refunds
[85] Apple Pay Fees: https://www.apple.com/apple-pay/merchant/
[86] Apple Pay Issuer Fees: https://www.cnbc.com/apple-pay-fees
[87] Apple Pay Processor Fees: https://stripe.com/payments/apple-pay
[88] Apple Developer Program: https://developer.apple.com/programs/
[89] Stripe Global: https://stripe.com/global
[90] Stripe Payment Methods: https://stripe.com/payments/payment-methods
[91] PayPal Global: https://www.paypal.com/us/webapps/mpp/country-worldwide
[92] PayPal Payment Methods: https://www.paypal.com/us/business/accept-payments/payment-methods
[93] Square Global: https://squareup.com/us/en/global
[94] Square Currencies: https://squareup.com/us/en/currencies
[95] Square International: https://squareup.com/us/en/international
[96] Braintree Global: https://developer.paypal.com/braintree/docs/guides/international
[97] Braintree Currencies: https://developer.paypal.com/braintree/docs/guides/currencies
[98] Adyen Global: https://www.adyen.com/global
[99] Adyen Local Payment Methods: https://www.adyen.com/payment-methods
[100] Shopify Payments Countries: https://help.shopify.com/en/manual/payments/shopify-payments/countries
[101] Shopify Multi-Currency: https://help.shopify.com/en/manual/payments/shopify-payments/multi-currency
[102] Shopify Markets: https://www.shopify.com/markets
[103] 2Checkout Global: https://www.2checkout.com/global
[104] 2Checkout Currencies: https://www.2checkout.com/currencies
[105] 2Checkout Payment Methods: https://www.2checkout.com/payment-methods
[106] Amazon Pay Countries: https://pay.amazon.com/us/merchant/countries
[107] Amazon Pay Currencies: https://pay.amazon.com/us/merchant/currencies
[108] Apple Pay Countries: https://support.apple.com/en-us/HT204916
[109] Apple Pay Market Share: https://www.statista.com/apple-pay-market-share
[110] Apple Pay Users: https://www.apple.com/apple-pay/
[111] Stripe Trustpilot: https://www.trustpilot.com/review/stripe.com
[112] PayPal Trustpilot: https://www.trustpilot.com/review/paypal.com
[113] Square Trustpilot: https://www.trustpilot.com/review/square.com
[114] Braintree Capterra: https://www.capterra.com/p/braintree/
[115] Adyen Trustpilot: https://www.trustpilot.com/review/adyen.com
[116] Adyen G2: https://www.g2.com/products/adyen/reviews
[117] Shopify Trustpilot: https://www.trustpilot.com/review/shopify.com
[118] 2Checkout Trustpilot: https://www.trustpilot.com/review/2checkout.com
[119] Amazon Pay Trustpilot: https://www.trustpilot.com/review/amazonpay.com
[120] Apple Pay Merchant Guide: https://developer.apple.com/apple-pay/Apple-Pay-Merchant-Integration-Guide.pdf
[121] Stripe Payment Methods: https://stripe.com/payments/payment-methods
[122] PayPal Pay Later: https://www.paypal.com/us/business/pay-later
[123] PayPal Venmo: https://venmo.com/business
[124] Square Payment Methods: https://squareup.com/us/en/payment-methods
[125] Square Afterpay: https://squareup.com/us/en/afterpay
[126] Braintree Venmo: https://developer.paypal.com/braintree/docs/guides/venmo
[127] Braintree PayPal: https://developer.paypal.com/braintree/docs/guides/paypal
[128] Adyen Payment Methods: https://www.adyen.com/payment-methods
[129] Adyen BNPL: https://www.adyen.com/payment-methods/buy-now-pay-later
[130] Shopify Shop Pay: https://www.shopify.com/shop-pay
[131] 2Checkout Crypto: https://www.2checkout.com/cryptocurrency
[132] Amazon Pay Methods: https://pay.amazon.com/us/merchant/payment-methods
[133] Amazon Pay Affirm: https://pay.amazon.com/us/merchant/affirm
[134] Apple Pay Security: https://developer.apple.com/apple-pay/security
[135] Apple Pay Installments: https://developer.apple.com/apple-pay/installments
[136] Stripe Radar: https://stripe.com/radar
[137] Stripe 3D Secure: https://stripe.com/docs/3d-secure
[138] Stripe PCI: https://stripe.com/docs/security
[139] PayPal Seller Protection: https://www.paypal.com/us/webapps/mpp/security/seller-protection
[140] PayPal Fraud Protection: https://www.paypal.com/us/business/fraud-protection
[141] Square Risk Manager: https://squareup.com/us/en/risk-manager
[142] Square 3D Secure: https://squareup.com/us/en/3d-secure
[143] Square PCI: https://squareup.com/us/en/pci-compliance
[144] Braintree Fraud Tools: https://developer.paypal.com/braintree/docs/guides/fraud-tools
[145] Braintree 3D Secure: https://developer.paypal.com/braintree/docs/guides/3d-secure
[146] Adyen RevenueProtect: https://www.adyen.com/revenueprotect
[147] Adyen Uplift: https://www.adyen.com/products/uplift
[148] Shopify Fraud Analysis: https://help.shopify.com/en/manual/payments/shopify-payments/fraud-analysis
[149] Shopify Protect: https://help.shopify.com/en/manual/payments/shopify-payments/fraud-protect
[150] Shopify PCI: https://help.shopify.com/en/manual/payments/pci-compliance
[151] 2Checkout Fraud: https://www.2checkout.com/fraud-protection
[152] Amazon Pay Protection: https://pay.amazon.com/us/merchant/protection
[153] Amazon Pay Security: https://pay.amazon.com/us/merchant/security
[154] Apple Pay Fraud: https://www.apple.com/apple-pay/security/
[155] Stripe G2: https://www.g2.com/products/stripe/reviews
[156] Stripe Support: https://stripe.com/docs/contact
[157] PayPal G2: https://www.g2.com/products/paypal/reviews
[158] PayPal Support: https://www.paypal.com/us/smarthelp
[159] Square Support: https://squareup.com/us/en/contact
[160] Square G2: https://www.g2.com/products/square/reviews
[161] Braintree Support: https://developer.paypal.com/braintree/support
[162] Braintree G2: https://www.g2.com/products/braintree/reviews
[163] Adyen Support: https://www.adyen.com/contact
[164] Adyen Gartner: https://www.gartner.com/reviews/market/payment-gateways/vendor/adyen
[165] Shopify Support: https://help.shopify.com/en/contact
[166] Shopify G2: https://www.g2.com/products/shopify/reviews
[167] 2Checkout Support: https://www.2checkout.com/contact
[168] 2Checkout Capterra: https://www.capterra.com/p/2checkout/
[169] Amazon Pay Support: https://pay.amazon.com/us/merchant/help
[170] Amazon Pay Seller Central: https://sellercentral.amazon.com
[171] Apple Developer Forums: https://developer.apple.com/forums/topics/apple-pay
[172] Braintree Scalability: https://www.braintreepayments.com/scalability
[173] Adyen Enterprise: https://www.adyen.com/enterprise
[174] Shopify Enterprise: https://www.shopify.com/enterprise
[175] 2Checkout Scalability: https://www.2checkout.com/scalability
[176] Amazon Pay Scalability: https://pay.amazon.com/us/merchant/scalability
