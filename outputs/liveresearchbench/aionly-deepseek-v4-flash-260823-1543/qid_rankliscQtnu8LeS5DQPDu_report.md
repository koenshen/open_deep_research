# Top 25 Smartphones (as of August 24, 2026): Combined Battery Life, Camera Megapixels, and Retail Price Ranking

## 1. Executive Summary

This report ranks the top 25 smartphones available as of August 24, 2026, using a composite score that combines three factors: battery life (in hours), main camera resolution (in megapixels), and retail price (in USD), with lower-priced smartphones explicitly favored to reward value for money. The ranking covers nine manufacturers across budget, mid-range, and flagship segments: Apple, Samsung, Google, OnePlus, Xiaomi, Motorola, Nothing, ASUS, and Sony.

Key findings:

- The **#1-ranked phone is the Xiaomi Redmi Note 14 Pro 5G** (200MP camera, ~$295), driven by its class-leading camera resolution and rock-bottom price, despite having the lowest battery-hour score in the set.
- The **Samsung Galaxy S26 Ultra (#2) and Galaxy S25 Ultra (#3)** round out the top three, both with 200MP main cameras and 31 hours of official video-playback battery life.
- The best value flagships are the **Galaxy S26** ($799) and **iPhone 17** ($799); the best budget/mid-range values are the **Pixel 9a** ($399), **Galaxy A36** ($399.99), **Pixel 10a** ($499), **Galaxy A56** ($499.99), and **OnePlus 13R** ($499.99 street price).
- Battery-hour data is not standardized across manufacturers. This report uses official manufacturer ratings where published (Apple, Samsung, Google, OnePlus, ASUS) and reputable lab-tested hours elsewhere (GSMArena, PCMag, DxOMark), with every figure flagged by source type.

---

## 2. Ranking Methodology

### 2.1 Data Sources

Specifications and pricing were collected from official manufacturer websites and storefronts (apple.com, samsung.com, store.google.com, oneplus.com, nothing.tech, mi.com, motorola.com, rog.asus.com), reputable e-commerce platforms (Amazon, Best Buy, Newegg), and — for battery lab tests and a few international-only prices — established spec/testing sites (GSMArena, PCMag, DxOMark, Smartprix, Kimovil). Every source is cited inline. Where a manufacturer does not publish an official battery-hour figure or an official US retail price (notably Xiaomi, Sony, and partially Nothing), the specific data source and the nature of the measure are explicitly flagged.

### 2.2 Scoring Model

Each of the three factors was normalized to a 0–100 sub-score using min-max scaling:

- **Battery score** = (battery_hours − min_battery) ÷ (max_battery − min_battery) × 100
- **Camera score** = (camera_MP − min_camera) ÷ (max_camera − min_camera) × 100
- **Price score** = (max_price − retail_price) ÷ (max_price − min_price) × 100

The price score is **inverted by design**: the lowest-priced phone receives 100, and the highest-priced phone receives 0. This is how "lower price = better value" is encoded in the model.

The **overall composite score** is an equal-weighted average of the three sub-scores:

**Composite = (Battery score + Camera score + Price score) ÷ 3**

Equal weighting was chosen because the research brief specifies no hierarchy among the three factors. The weights are transparent and can be adjusted by any reader who wishes to emphasize one factor over another.

### 2.3 Normalization Parameters

Across the 25 ranked phones, the min and max values used for normalization were:

| Factor | Minimum | Maximum | Phone carrying min/max |
|---|---|---|---|
| Battery life | 11.65 h | 39 h | Redmi Note 14 Pro 5G (11.65h lab test) / iPhone 17 Pro Max (39h official) |
| Camera resolution | 48 MP | 200 MP | Most iPhones/Pixels (48MP) / Galaxy S26 Ultra & S25 Ultra (200MP) |
| Retail price | $294.99 | $1,499.99 | Redmi Note 14 Pro 5G / Sony Xperia 1 VII |

**Worked example — Galaxy S26 Ultra (31h, 200MP, $1,299):**
- Battery = (31 − 11.65) ÷ (39 − 11.65) × 100 = 70.75
- Camera = (200 − 48) ÷ (200 − 48) × 100 = 100.00
- Price = (1,499.99 − 1,299) ÷ (1,499.99 − 294.99) × 100 = 16.68
- **Composite = (70.75 + 100.00 + 16.68) ÷ 3 = 62.48**

### 2.4 Handling of Missing or Non-Standard Data

- **Phones excluded because a battery-hour figure is not publicly documented:**
  - **Motorola Edge 2026** — Motorola only claims "up to 2 days of battery life"; no hour-based rating is published, and no reputable lab hour figure was captured [49][50].
  - **Redmi Note 15** — no official hour figure or documented US retail price [43].
  - **Sony Xperia 1 VIII** — announced May 2026, but full specs (including camera MP and US pricing) were not yet published as of the research date.
- **Sony Xperia 5 VII does not exist** — the Xperia 5 compact line has been discontinued, so it cannot be ranked [59][58].
- **OnePlus Nord 4** — never officially sold in the United States, so it is excluded from a US-pricing-based ranking.
- **Google phones** — Google's official battery rating is "30+ hours" of battery life; these phones are scored using 30 hours for normalization consistency [16][21][22].
- **Price basis** — where a current street price was documented on an official storefront or major retailer (e.g., Pixel 9a at $399, OnePlus 13R at $499.99, Nothing Phone 3 at $599), that current retail price is used and flagged in Section 3.3.

---

## 3. Ranked Results: Top 25 Smartphones

### 3.1 Full Ranking Table

| Rank | Smartphone | Battery (hours) | Basis | Main Camera (MP) | Retail Price (USD) | Composite Score |
|---:|---|---|---|---|---:|---:|
| 1 | Xiaomi Redmi Note 14 Pro 5G (Global) | 11.65 | d | 200 | $294.99 | 66.67 |
| 2 | Samsung Galaxy S26 Ultra | 31 | a | 200 | $1,299 | 62.48 |
| 3 | Samsung Galaxy S25 Ultra | 31 | a | 200 | $1,299.99 | 62.45 |
| 4 | Google Pixel 9a | 30 | b | 48 | $399 | 52.82 |
| 5 | Samsung Galaxy A36 5G | 29 | a | 50 | $399.99 | 52.02 |
| 6 | Google Pixel 10a | 30 | b | 48 | $499 | 50.05 |
| 7 | Samsung Galaxy A56 5G | 29 | a | 50 | $499.99 | 49.25 |
| 8 | OnePlus 13R | 24 | c | 50 | $499.99 | 43.16 |
| 9 | Samsung Galaxy S26 | 30 | a | 50 | $799 | 42.19 |
| 10 | Apple iPhone 17 | 30 | a | 48 | $799 | 41.75 |
| 11 | Apple iPhone 17 Pro Max | 39 | a | 48 | $1,199 | 41.66 |
| 12 | Google Pixel 11 | 30 | b | 48 | $899 | 38.99 |
| 13 | Samsung Galaxy S26+ | 31 | a | 50 | $999 | 37.88 |
| 14 | Apple iPhone 17 Pro | 33 | a | 48 | $1,099 | 37.11 |
| 15 | Nothing Phone (3a) | 14.25 | d | 50 | $379 | 34.62 |
| 16 | Google Pixel 11 Pro | 30 | b | 50 | $1,099 | 33.90 |
| 17 | Motorola Moto G Power 2026 | 13.33 | d | 50 | $369.99 | 33.75 |
| 18 | Apple iPhone 17 Air | 27 | a | 48 | $999 | 32.57 |
| 19 | Nothing Phone (3a) Pro | 12.75 | d | 50 | $459 | 30.58 |
| 20 | Google Pixel 11 Pro XL | 30 | b | 50 | $1,299 | 28.36 |
| 21 | Xiaomi 15 | 16.15 | d | 50 | $719.50 | 27.51 |
| 22 | ASUS ROG Phone 9 | 22.1 | c | 50 | $999 | 27.04 |
| 23 | Nothing Phone (3) | 12.93 | d | 50 | $599 | 26.92 |
| 24 | ASUS ROG Phone 9 Pro | 22.1 | c | 50 | $1,199 | 21.50 |
| 25 | Sony Xperia 1 VII | 15.53 | d | 48 | $1,499.99 | 4.73 |

### 3.2 Battery-Hour Basis Legend

- **(a)** Official manufacturer-documented video playback hours — Apple and Samsung.
- **(b)** Official manufacturer "hours of battery life" usage rating — Google's "30+ hours" rating for Pixel devices; scored as 30 hours.
- **(c)** Official manufacturer-documented streaming/use hours — OnePlus 13R ("up to 24 hours of Netflix video playback") [28]; ASUS ROG Phone 9/9 Pro ("22.1 hours video streaming") [51][52].
- **(d)** Independent standardized test hours — GSMArena active-use score (Redmi Note 14 Pro 5G, Moto G Power 2026, Nothing Phone 3, Xperia 1 VII) [46][48][39][56], PCMag video-streaming test (Nothing Phone 3a: 14h15m; Nothing Phone 3a Pro: 12h45m) [34], and DxOMark battery test (Xiaomi 15) [42].

### 3.3 Notes on Selected Entries

- **Xiaomi Redmi Note 14 Pro 5G** — listed at $294.99 (8GB/256GB) at Newegg at the time of research [45][46]. The Global version has a 200MP main sensor; the India-market variant uses a 50MP Sony LYT-600 sensor, and the 5,500mAh India version was not the model scored. Xiaomi does not officially sell phones in the US; this price is an import/retailer price.
- **Pixel 9a** — official MSRP is $499, but Google Store, Amazon, and Best Buy were selling it at $399 in August 2026 during stock clearance ahead of the Pixel 10a launch [25].
- **Pixel 10a** — the official $499 MSRP is used; it has been promoted at $424 on Amazon and Google Store in August 2026 [24].
- **OnePlus 13R** — launched at $599.99 [31], currently $499.99 at Amazon and Best Buy [30]. OnePlus announced in July 2026 that it is exiting the North American market, which will affect future software support and availability.
- **Nothing Phone (3)** — official MSRP was $799 [40]; Amazon's current documented retail price is $599 [37].
- **Nothing Phone (3a) Pro** — official US launch price $459 [41]; Amazon lists it at $429 [35].
- **Galaxy A56 / A36** — prices are Samsung US list prices [11][12]; street prices have at times been lower (e.g., Galaxy A36 at $239.99 with activation at Best Buy).
- **Sony Xperia 1 VII** — priced at $1,499.99 as an "international version" sold via an Amazon third-party seller; Sony has stopped officially selling phones in North America [57][58].
- **iPhone 17 Pro Max** — has the best battery-hour rating in the entire set (39 hours of video playback) [6], but its $1,199 price and 48MP main camera cap its composite score at #11.

---

## 4. Analysis and Rationale

### 4.1 How the Three Factors Shape the Ranking

Because the camera-resolution range is very wide (48MP → 200MP) and the price range is also wide ($295 → $1,500), those two factors drive most of the variation in the composite score. Battery hours, in contrast, range from 11.65h to 39h, so battery mainly separates the weakest budget phones from the best flagships.

A key consequence: **phones with 48–50MP cameras all receive nearly identical camera sub-scores** (0 to 1.32 out of 100). For most of the field — iPhones, Pixels, Galaxy S26/A-series, Nothing, Motorola, Xiaomi 15, ROG, Xperia — the ranking is effectively decided by price and battery. The only phones that earn large camera points are the three 200MP devices: the Redmi Note 14 Pro 5G, Galaxy S26 Ultra, and Galaxy S25 Ultra, which receive a full 100-point camera sub-score. This explains why they occupy the top three positions.

The inverse price normalization means **mid-range and budget phones dominate the top half of the table**. Seven of the top eight phones cost $500 or less. The only flagship in the top five is the Galaxy S26 Ultra, which gets there purely on its 200MP camera and strong 31-hour battery rating.

### 4.2 Value-for-Money Leaders

The model strongly rewards low price, as intended:

- The **Pixel 9a at $399** earns a 91.4 price sub-score and a 67.1 battery sub-score, placing it #4 overall — the best pure value phone from a major brand that officially sells in the US.
- The **Galaxy A36 at $399.99** (91.3 price, 63.4 battery, 1.3 camera) lands at #5, nearly tied with the Pixel 9a with a slightly higher-resolution 50MP camera.
- The **Pixel 10a ($499, #6)** and **Galaxy A56 ($499.99, #7)** are the next value tier; both offer 30-hour-class battery ratings at roughly half the price of a flagship.
- The **OnePlus 13R at its current $499.99 street price** is the best "flagship-killer" value, with a 50MP main + 50MP 2x telephoto setup, 6,000mAh battery, and Snapdragon 8 Gen 3 — it reaches #8 despite a modest (24h Netflix-playback) official battery rating.

### 4.3 Flagship Positioning

Among current-generation flagships, the **Galaxy S26 Ultra** is the standout, ranking #2 overall on the strength of its 200MP camera and 31-hour video playback rating [9][10]. Apple's flagship line is held back by the 48MP main sensor: the **iPhone 17 Pro Max** has the best battery of any phone in the study (39h [6]) but falls to #11 on price; the **iPhone 17 Pro** (33h) sits at #14; the **iPhone 17 Air** (27h) at #18. The **Galaxy S26** at $799 is the best-priced flagship in the ranking, tying the iPhone 17 at #9/#10 with a 50MP camera advantage that pushes it one spot ahead.

At the bottom, the **Sony Xperia 1 VII** illustrates the severity of the price penalty: at $1,499.99 it receives a 0 price sub-score, and with a 48MP camera it also scores 0 on camera. Its 15.53h GSMArena active-use battery score — respectable in real-world testing, with one independent review measuring ~24h40m in a YouTube loop test — is recorded under the stricter lab metric that is not directly comparable to Apple/Samsung video-playback hours. The result is a #25 composite score of 4.73.

### 4.4 Budget and Mid-Range Standouts

The budget tier is exceptionally well represented: **Redmi Note 14 Pro 5G** ($295, #1), **Pixel 9a** ($399, #4), **Galaxy A36** ($399.99, #5), **Pixel 10a** ($499, #6), **Galaxy A56** ($499.99, #7), **Nothing Phone 3a** ($379, #15), and **Moto G Power 2026** ($369.99, #17). The Nothing Phone 3a and Moto G Power are pulled down by lab-tested battery scores (14.25h and 13.33h) that use a stricter test protocol than manufacturer video-playback ratings — a reminder that battery metrics are not perfectly comparable across phones.

Of the two ASUS ROG gaming phones, the standard **ROG Phone 9** (22.1h video streaming, $999, #22) clearly out-ranks the **ROG Phone 9 Pro** ($1,199, #24), since the Pro's extra cost buys RAM/storage and a telephoto camera but not battery or main-camera resolution that the model rewards.

### 4.5 Brand Representation

- **Samsung** leads with 6 phones in the top 25 (S26 Ultra, S25 Ultra, A36, A56, S26, S26+), reflecting both the breadth of its lineup and aggressive mid-range pricing in the A-series [11][12].
- **Google** has 5 phones (Pixel 9a, 10a, 11, 11 Pro, 11 Pro XL), with the freshly released Pixel 11 family (announced August 12, 2026, released August 20, 2026) well represented [16][19].
- **Apple** places 4 phones (iPhone 17, 17 Pro Max, 17 Pro, 17 Air) [3][5].
- **Nothing** places 3, **Xiaomi** 2, **ASUS** 2, and OnePlus, Motorola, and Sony one each.

### 4.6 Caveats and Limitations

- **Megapixels are a crude proxy for camera quality.** Sensor size, lens quality, image stabilization, and computational processing matter enormously. The model rewards high-MP counts by construction, which is why the 200MP Redmi Note 14 Pro 5G and Galaxy S26/S25 Ultra dominate the top of the table.
- **Battery-hour metrics are not standardized.** Apple/Samsung official "video playback" hours, Google's "30+ hours" usage rating, OnePlus's "24 hours Netflix playback" claim, and GSMArena/PCMag/DxOMark lab scores all measure different workloads. Phones whose manufacturers publish generous official ratings are systematically advantaged relative to phones tracked only by stricter lab tests.
- **Prices fluctuate.** The prices shown are documented US retail prices as of August 2026; several are promotional/street prices rather than MSRPs, and all such cases are flagged.
- **Equal weighting is a modeling choice.** A user who cares only about battery would rank the iPhone 17 Pro Max first; a user who cares only about price would rank the Redmi Note 14 Pro 5G first; a user obsessed with camera resolution would pick among the 200MP trio. The composite score is best read as a balanced, transparent value index for the three specified factors.

---

## 5. Conclusion

As of August 24, 2026, the phone that best balances battery life, camera megapixels, and low price under this model is the **Xiaomi Redmi Note 14 Pro 5G**, a 200MP budget phone selling for under $300. The **Samsung Galaxy S26 Ultra** is the strongest flagship, combining a 200MP camera with a 31-hour battery rating, while the **Pixel 9a**, **Galaxy A36**, **Pixel 10a**, **Galaxy A56**, and **OnePlus 13R** represent the best value in the budget-to-mid-range segment from brands with official US presence. The ranking is deliberately transparent: every battery figure is labeled by source type, every price is documented, and the normalization formulas are published above, so the composite scores can be recomputed or reweighted by any reader.

---

### Sources

[1] Apple — iPhone 17 Technical Specifications: https://www.apple.com/iphone-17/specs  
[2] Apple Support — iPhone 17 Tech Specs: https://support.apple.com/en-us/125089  
[3] Apple Store — Shop iPhone 17: https://www.apple.com/shop/buy-iphone/iphone-17  
[4] Apple — iPhone Air: https://www.apple.com/iphone-air  
[5] Apple — iPhone 17 Pro and 17 Pro Max Technical Specifications: https://www.apple.com/iphone-17-pro/specs  
[6] Apple Support — iPhone 17 Pro Max Tech Specs: https://support.apple.com/en-us/125091  
[7] Apple Newsroom — Apple unveils iPhone 17 Pro and iPhone 17 Pro Max: https://www.apple.com/newsroom/2025/09/apple-unveils-iphone-17-pro-and-iphone-17-pro-max  
[8] Samsung US — Galaxy S26 and S26+ product page: https://www.samsung.com/us/smartphones/galaxy-s26  
[9] Samsung Ireland — Galaxy S26 Ultra specs: https://www.samsung.com/ie/smartphones/galaxy-s26-ultra  
[10] MARCA — Samsung Galaxy S26 US pricing: https://www.marca.com/en/technology/2026/02/25/699f4239268e3e046c8b4596.html  
[11] Samsung US — Galaxy A56 5G: https://www.samsung.com/us/smartphones/galaxy-a56-5g  
[12] Samsung US — Galaxy A36 5G: https://www.samsung.com/us/smartphones/galaxy-a36-5g  
[13] Android Headlines — Samsung Galaxy A56 Buyers Guide: https://www.androidheadlines.com/samsung-galaxy-a56  
[14] Samsung New Zealand — Galaxy S25 Ultra specs: https://www.samsung.com/nz/smartphones/galaxy-s25-ultra/specs  
[15] Samsung US — Galaxy S25 Ultra compare: https://www.samsung.com/us/smartphones/galaxy-s25-ultra/compare  
[16] Google Official Blog — The Pixel 11 series: https://blog.google/products-and-platforms/devices/pixel/google-pixel-11-pro-xl  
[17] GSMArena — Google Pixel 11 full specs: https://www.gsmarena.com/google_pixel_11_5g-14799.php  
[18] GSMArena — Google Pixel 11 Pro XL full specs: https://www.gsmarena.com/google_pixel_11_pro_xl_5g-14800.php  
[19] Droid-Life — Pixel 11 Series Official, Starting at $899: https://www.droid-life.com/2026/08/12/pixel-11-series-official-899-preorders-live  
[20] Android Headlines — Google Pixel 11 Series Full Specs and Prices: https://www.androidheadlines.com/google-pixel-11-specifications  
[21] Google Fi — Pixel 10a Tech Specs: https://fi.google.com/about/phones/pixel-10a-specs  
[22] Google Blog — Pixel 10a announcement: https://blog.google/products-and-platforms/devices/pixel/google-pixel-10a  
[23] GSMArena — Google Pixel 10a full specs: https://www.gsmarena.com/google_pixel_10a_5g-14474.php  
[24] TechTimes — Pixel 10a drops to $424: https://www.techtimes.com/articles/323534/20260807/pixel-10a-drops-424-google-vp-confirms-price-hike-no-deadline.htm  
[25] Notebookcheck — Pixel 9a at $399: Google clears stock: https://www.notebookcheck.net/Pixel-9a-at-399-100-off-Google-clears-stock-ahead-of-Pixel-10a-s-arrival.1210039.0.html  
[26] Mashable — Google Pixel 9a launch price/specs: https://mashable.com/article/google-pixel-9a-launch-price-specs  
[27] Android Headlines — Google Pixel 9a Buyers Guide: https://www.androidheadlines.com/google-pixel-9a  
[28] OnePlus US — OnePlus 13R product page: https://www.oneplus.com/us/13r  
[29] OnePlus Global — 13R specs: https://www.oneplus.com/global/13r/specs  
[30] Android Central — OnePlus 13R at $499.99: https://www.androidcentral.com/phones/oneplus/i-dont-believe-any-phone-delivers-better-value-than-the-oneplus-13r  
[31] Droid Life — OnePlus 13R launches at $599: https://www.droid-life.com/2025/01/07/oneplus-13r-launches-alongside-oneplus-13-at-just-599  
[32] Nothing — Phone (3a) product page: https://nothing.tech/products/phone-3a  
[33] Amazon — Nothing Phone (3a) listing: https://www.amazon.com/Nothing-Smartphone-Snapdragon-Processor-Waterproof/dp/B0DYCXGDQF  
[34] PCMag — Nothing Phone (3a) Review: https://www.pcmag.com/reviews/nothing-phone-3a  
[35] Amazon — Nothing Phone (3a) Pro listing: https://www.amazon.com/Nothing-Unlocked-Periscope-Telephoto-Snapdragon/dp/B0DPXR3GSG  
[36] GSMArena — Nothing Phone (3a) Pro specs: https://www.gsmarena.com/nothing_phone_(3a)_pro-13649.php  
[37] Amazon — Nothing Phone (3) listing: https://www.amazon.com/Nothing-Unlocked-Snapdragon-Interface-Smartphone/dp/B0F9XXHSCG  
[38] GSMArena — Nothing Phone (3) full specs: https://www.gsmarena.com/nothing_phone_(3)_5g-13969.php  
[39] GSMArena — Nothing Phone (3) review, lab tests: https://www.gsmarena.com/nothing_phone_3-review-2853p3.php  
[40] 9to5Google — Nothing Phone (3) at $799: https://9to5google.com/2025/07/01/nothing-phone-3-specs-release-date-price  
[41] Notebookcheck — Nothing Phone 3a series US pricing: https://www.notebookcheck.net/Nothing-Phone-3a-series-makes-its-way-to-the-US-with-a-379-starting-price.972258.0.html  
[42] Smartprix US — Xiaomi 15 price/specs: https://us.smartprix.com/mobiles/xiaomi-15-5g-ppd1xdr51755  
[43] Xiaomi Global — Xiaomi 15 official specs: https://www.mi.com/global/product/xiaomi-15/specs  
[44] Kimovil — Xiaomi 15 price comparison: https://www.kimovil.com/en/where-to-buy-xiaomi-15  
[45] Smartprix US — Redmi Note 14 Pro 5G price/specs: https://us.smartprix.com/mobiles/xiaomi-redmi-note-14-pro-5g-ppd1nkx4gnsg  
[46] GSMArena — Redmi Note 14 Pro 5G (Global) full specs: https://www.gsmarena.com/xiaomi_redmi_note_14_pro_5g_(global)-13613.php  
[47] Motorola Support — Specifications: moto g power 2026: https://en-us.support.motorola.com/app/answers/detail/a_id/190571/~/specifications---moto-g-power-2026  
[48] GSMArena — Motorola Moto G Power 5G (2026) full specs: https://www.gsmarena.com/motorola_moto_g_power_5g_(2026)-14359.php  
[49] Motorola US — motorola edge 2026 product page: https://www.motorola.com/us/en/p/phones/motorola-edge/edge-2026/pmipmjr44mu  
[50] Motorola Support — Specifications: motorola edge 2026: https://en-us.support.motorola.com/app/answers/detail/a_id/193052/~/specifications---motorola-edge-2026  
[51] ASUS ROG — ROG Phone 9 official specs: https://rog.asus.com/phones/rog-phone-9/spec  
[52] ASUS ROG — ROG Phone 9 Pro product page: https://rog.asus.com/phones/rog-phone-9-pro  
[53] GSMArena — Asus ROG Phone 9 full specs: https://www.gsmarena.com/asus_rog_phone_9-13503.php  
[54] Smartprix US — Asus ROG Phone 9 price: https://us.smartprix.com/mobiles/asus-rog-phone-9-ppd1wx8s3o7b  
[55] Smartprix US — Asus ROG Phone 9 Pro Edition price: https://us.smartprix.com/mobiles/asus-rog-phone-9-pro-edition-ppd1wsx3h7yz  
[56] GSMArena — Sony Xperia 1 VII full specs: https://www.gsmarena.com/sony_xperia_1_vii_5g-13843.php  
[57] Amazon — Sony Xperia 1 VII (international version): https://www.amazon.com/Sony-Xperia-VII-XQ-FS72-Smartphone/dp/B0FBQFZQM8  
[58] Android Headlines — Sony Xperia 1 VII Buyers Guide: https://www.androidheadlines.com/sony-xperia-1-vii  
[59] Sony — Overview of Xperia devices and Android versions: https://www.sony.com/electronics/support/articles/SX243901
