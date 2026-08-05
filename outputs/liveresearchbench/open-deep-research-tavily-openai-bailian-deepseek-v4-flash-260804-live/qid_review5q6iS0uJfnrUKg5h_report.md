# Large Language Model Hallucination Detection: Recent Advances (2023–2025)

## Overview

The detection of hallucinations in large language models (LLMs) has emerged as one of the most critical research areas in natural language processing, driven by the widespread deployment of LLMs in high-stakes applications. From 2023 to 2025, the field has undergone a remarkable transformation, moving from simple heuristic-based detection to sophisticated methods grounded in theoretical understanding, internal state analysis, and mechanistic interpretability. This report provides a comprehensive overview of the three major pillars of this research: empirical detection algorithms and benchmarks, theoretical foundations explaining why hallucinations occur, and interpretability works that probe the internal representations of LLMs to detect and understand hallucinations.

---

## 1. Empirical Detection Algorithms and Benchmarks

### 1.1 Uncertainty Estimation and Semantic Entropy Methods

A foundational line of research has focused on quantifying model uncertainty to detect hallucinations, with the key insight that models tend to be uncertain when they are about to hallucinate. The most influential approach in this direction is **semantic entropy**, introduced by Kuhn, Gal, and Farquhar at ICLR 2023 and later extended in Nature 2024 [1]. The core idea is that conventional token-level entropy conflates uncertainty over wording with uncertainty over meaning. By sampling multiple outputs, clustering them by semantic equivalence using bidirectional entailment, and computing entropy over semantic clusters, semantic entropy provides an unsupervised, task-agnostic method for detecting confabulations—arbitrary and incorrect generations that vary with irrelevant details like random seed. Evaluations on question-answering datasets (TriviaQA, SQuAD, BioASQ, NQ-Open, SVAMP) using LLaMA 2, Falcon, and Mistral models showed that semantic entropy achieves an average AUROC of 0.790, outperforming baselines such as naive entropy (0.691) and P(True) (0.698).

Building on this foundation, **Kernel Language Entropy (KLE)**, presented at NeurIPS 2024 by Nikitin et al. [2], generalizes semantic entropy by encoding pairwise semantic similarities between model outputs using positive semidefinite unit trace kernels and measuring entropy via von Neumann entropy. KLE provides more fine-grained uncertainty estimates than hard clustering approaches, improving uncertainty quantification across multiple NLG datasets and LLM architectures.

A significant practical advancement came with **Semantic Entropy Probes (SEPs)**, presented at ICML 2024 by Kossen et al. [3]. SEPs directly approximate semantic entropy from the hidden states of a single generation, eliminating the need for multiple model outputs. This reduces the computational overhead of semantic uncertainty quantification to nearly zero while retaining high detection performance and generalizing better to out-of-distribution data than previous probing methods.

The **Enhancing Hallucination Detection Through Noise Injection** paper at ICLR 2026 [4] provides a complementary perspective, arguing that existing methods relying on temperature-based sampling capture only aleatoric uncertainty while neglecting epistemic uncertainty. The proposed training-free Bayesian approach injects uniform noise into MLP activations of upper layers, effectively sampling from a surrogate posterior distribution over model parameters. Experiments on GSM8K, CSQA, and TriviaQA across multiple models (Gemma, Llama, Phi, Mistral) showed consistent AUROC improvements of up to 4.6%, with the method being compatible with various uncertainty metrics.

### 1.2 Internal State and Hidden Representation Methods

A parallel line of research has explored detecting hallucinations directly from the internal representations of LLMs, offering the advantage of requiring only a single forward pass. **HaloScope**, a NeurIPS 2024 Spotlight paper by Du, Xiao, and Li [5], addresses the critical challenge of lacking labeled truthful/hallucinated data. The framework uses unlabeled LLM generations collected in the wild, employing an automated scoring function to distinguish truthful from untruthful outputs within the mixture. HaloScope identifies a latent subspace in LLM embeddings to distinguish truthful from hallucinated content, achieving over 10% improvement in AUROC over competitive baselines on four QA datasets (TruthfulQA, TriviaQA, CoQA, TyDiQA-GP) while being 10 times faster than consistency-based approaches.

**LLM-Check**, presented at NeurIPS 2024 by Sriramanan et al. [6], proposes a suite of detection techniques that analyze internal LLM representations—self-attention kernel similarity maps, hidden states via eigen analysis, and logit scores—to distinguish truthful from hallucinated outputs without fine-tuning or multiple model responses. The methods achieve 45x–450x speedups over baselines while maintaining or improving detection performance across diverse datasets.

The **Truthfulness Separator Vector (TSV)**, presented at ICML 2025 by Park et al. [7], introduces a lightweight, plug-and-play steering vector that modifies the LLM's internal representation during inference to better separate truthful and hallucinated outputs. The two-stage framework first trains TSV on a small set of labeled exemplars (as few as 32 examples), then augments the exemplar set with unlabeled LLM generations using an optimal transport-based pseudo-labeling algorithm. On the challenging TruthfulQA benchmark, TSV achieves a significant +12.8% improvement in AUROC compared to state-of-the-art methods, reaching performance comparable to the fully-supervised upper bound.

**HaMI**, presented at NeurIPS 2025 [8], addresses the limitation of existing detectors that rely on fixed tokens, which perform poorly on free-form generations. By formulating hallucination detection as a Multiple Instance Learning problem over token-level representations, HaMI jointly optimizes token selection and hallucination detection, achieving state-of-the-art results on four hallucination benchmarks.

**ACT-ViT**, presented at NeurIPS 2025 by Bar-Shalom et al. [9], takes a novel approach by treating full activation tensors (layers × tokens) as images and using a Vision Transformer-inspired architecture. This approach supports training on multiple LLMs simultaneously, achieves strong zero-shot performance on unseen datasets, and can be transferred effectively to new LLMs through fine-tuning.

**PALE**, presented at AAAI 2025 [10], introduces a prompt-guided data augmentation framework that generates both truthful and hallucinated QA pairs from a state-of-the-art LLM without requiring human-labeled data. These augmented data are used to estimate two Gaussian distributions in the LLM's hidden-state embedding space, and a new metric—the Contrastive Mahalanobis Score (CM Score)—computes the difference of Mahalanobis distances to classify test samples. PALE outperforms 11 baselines by substantial margins (e.g., 6.55% AUROC improvement over HaloScope on TruthfulQA with LLaMA-3.1-7B).

**MIND**, published in Findings of ACL 2024 [11], provides an unsupervised, real-time hallucination detection method that uses pseudo-training data from Wikipedia and a multi-layer perceptron classifier operating on LLM internal states. The method is compatible with any Transformer-based LLM and reduces computational overhead, achieving a sentence-level AUC of 78.76% for LLaMA-based models.

### 1.3 Consistency-Based and Self-Check Methods

**SelfCheckGPT**, presented at EMNLP 2023 by Manakul, Liusie, and Gales [12], is a zero-resource framework that detects hallucinations by measuring consistency across multiple sampled responses. The method uses a four-stage zero-shot verification pipeline—target extraction, information collection, step regeneration, and result comparison—to compute per-step confidence scores. Five variants were proposed, with SelfCheckGPT-NLI (using natural language inference) being particularly effective, achieving perfect precision for scores above 0.5 on the Wiki Bio hallucination dataset. The major advantage is its practical applicability without external dependencies or internal model access, while the drawback is its computational overhead requiring multiple sampled generations.

**SAC3 (Semantic-Aware Cross-Check Consistency)**, presented at EMNLP 2023 [13], addresses two types of hallucinations that self-consistency checks alone cannot reliably detect: question-level hallucinations (where a model consistently gives wrong answers to a specific question) and model-level hallucinations (where different models differ in hallucination propensity). By perturbing semantically equivalent questions and introducing cross-model response consistency checking, SAC3 achieves AUROC scores of 99.4% and 97.0% on classification QA tasks, and 88.0% and 77.2% on open-domain generation QA tasks, improving over self-consistency baselines by up to 13.8%.

### 1.4 Fact Verification and Retrieval-Augmented Detection Methods

**FActScore**, published at EMNLP 2023 by Min et al. [14], provides a fine-grained atomic evaluation of factual precision in long-form text generation. The approach breaks down generated text into atomic facts and verifies each against a knowledge source, producing a factual precision score. The automated FActScore estimator achieves less than 2% error rate relative to human annotation. Applied to evaluate 6,500 generations from 13 recent language models, the study found that all evaluated LLMs are substantially less factual than human-written texts (humans achieve ~88% FActScore, while top LLMs like GPT-4 and ChatGPT score much lower), and that GPT-4 and ChatGPT show similar factual precision but GPT-4 generates more atomic facts per response.

**VERITAS**, presented at EMNLP 2024 [15], provides a unified framework for hallucination detection across three task formats: natural language inference, grounded question answering, and grounded dialogue verification. The framework includes a diverse training dataset, a unified benchmark of 18 datasets, and both encoder-based (DeBERTa-v3-large) and generative (LLaMA-based) models. The VERITAS models achieve state-of-the-art performance across all major hallucination benchmarks, with a 10% improvement in average performance compared to similar-sized models and competitive performance with GPT-4 Turbo.

**MiniCheck**, presented at EMNLP 2024 [16], demonstrates that small specialized models can approach GPT-4-level hallucination detection performance at a fraction of the cost. The MiniCheck-7B model achieves 84.0% balanced accuracy on the RAGTruth subset of the LLM-AggreFact benchmark, comparable to GPT-4o at 75.9%, representing a 400x cost reduction compared to GPT-4-based evaluation.

**Lynx**, released by Patronus AI in July 2024 and presented at NVIDIA GTC, is an open-source LLM for hallucination detection in RAG settings. Fine-tuned from Llama-3-70B-Instruct on perturbed QA data using chain-of-thought reasoning and self-instruct tuning, Lynx achieves 87.4% overall accuracy on HaluBench, outperforming GPT-4o, Claude-3-Sonnet, and GPT-3.5-Turbo. In medical answers (PubMedQA), Lynx (70B) was 8.3% more accurate than GPT-4o at detecting medical inaccuracies.

### 1.5 Benchmarks and Evaluation Datasets

The field has seen the development of several comprehensive benchmarks for evaluating hallucination detection methods. **HaluEval** provides a large-scale collection of hallucinated and non-hallucinated samples across multiple tasks. **TruthfulQA** has become a standard benchmark for measuring a model's tendency to produce false answers that are common misconceptions. The **LLM-AggreFact** benchmark aggregates multiple datasets for evaluating factuality in LLM generations. **SelfCheckGPT** introduced the Wiki Bio hallucination dataset, consisting of GPT-3 generated Wikipedia passages with human-labeled factuality annotations.

A critical methodological contribution comes from the **Re-evaluating Hallucination Detection in LLMs** paper at EMNLP 2025 [17], which challenges the reliability of ROUGE and other lexical/semantic overlap metrics for evaluating hallucination detection. Through human studies, the authors show that ROUGE has high recall but extremely low precision, leading to inflated performance estimates. They validate LLM-as-Judge (using GPT-4o-Mini) as a more human-aligned evaluation metric, achieving 0.723 agreement with human labels versus 0.142 for ROUGE. Re-evaluating established detection methods with LLM-as-Judge reveals dramatic performance drops—up to 45.9% for Perplexity and 30.4% for Eigenscore—compared to ROUGE-based evaluations.

---

## 2. Theoretical Foundations of Hallucination

### 2.1 Fundamental Statistical Lower Bounds

A landmark theoretical contribution comes from Kalai and Vempala's **"Calibrated Language Models Must Hallucinate"**, published in the Proceedings of the 56th Annual ACM Symposium on Theory of Computing (STOC 2024) [18]. This paper proves a foundational result: any language model that meets a statistical calibration condition appropriate for generative language models will inevitably hallucinate at a non-zero rate. The key theoretical insight is that for "arbitrary" facts whose veracity cannot be determined from the training data, the probability of generating a hallucination is close to the fraction of facts that occur exactly once in the training data (a "Good-Turing" estimate), even assuming ideal training data without errors. The bound holds for arbitrary facts (e.g., "who ate what when") whose truth cannot be inferred from training data, but not for systematic facts (e.g., arithmetic) or facts that appear repeatedly.

The empirical validation of this theoretical framework comes from Miao and Kearns' **"Hallucination, Monofacts, and Miscalibration: An Empirical Investigation"**, published in the Proceedings of the National Academy of Sciences (PNAS), 2026 [19]. Using controlled experiments with n-gram models and fine-tuned transformer models (T5, GPT-2) on structured movie facts and synthetic biographical data, the authors demonstrate that hallucination is positively correlated with the monofact rate (fraction of facts appearing exactly once in training). A key intervention—selective upweighting of only 5% of training examples—deliberately injects miscalibration and reduces hallucination by up to 40% while maintaining accuracy, challenging the common practice of deduplicating training data. The study provides an empirical analog of the theoretical hallucination bound using bin-wise KL divergence: hallucination rate ≥ monofact rate − miscalibration.

### 2.2 Hallucination as an Incentive Problem

Kalai, Nachum, Vempala, and Zhang's **"Why Language Models Hallucinate"** (2025) [20] and its subsequent publication in Nature as **"Evaluating large language models for accuracy incentivizes hallucinations"** (2026) [21] reframe hallucination as an unintended outcome of training objectives and evaluation incentives rather than an inherent LLM deficiency. The paper draws a novel connection between generative errors and binary classification (the "Is-It-Valid" problem), showing that even with error-free training data, minimizing cross-entropy loss leads to errors. The generative error rate is at least twice the IIV misclassification rate.

Critically, the paper argues that post-training, the persistence of hallucinations is explained by the prevalence of binary (0-1) grading in mainstream benchmarks, which penalizes uncertainty expressions like "I don't know" and rewards guessing. The authors propose "open rubric" evaluations that explicitly state how errors are penalized, which test whether a model modulates its abstentions to stated stakes while optimizing accuracy. A case study using the SimpleQA benchmark on four frontier models shows that a consistency-based hallucination mitigation reduces errors but hurts accuracy under closed rubrics, whereas under open rubrics the mitigation consistently outperforms the baseline.

### 2.3 Subsequence Associations and Hallucination Mechanisms

**"Why and How LLMs Hallucinate: Connecting the Dots with Subsequence Associations"**, presented at NeurIPS 2025 by Sun et al. [22], introduces a framework that systematically understands the sources of hallucination behavior. The key insight is that hallucinations arise when more frequent but non-factual associations outweigh faithful ones. Through theoretical and empirical analyses, the authors demonstrate that decoder-only transformers effectively function as subsequence embedding models, with the fully-connected layers encoding input-output associations. A proposed tracing algorithm identifies causal subsequences by analyzing hallucination probabilities across randomized input contexts, outperforming standard attribution techniques.

### 2.4 Formal Definitions and Taxonomies

**"A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions"**, published in ACM Transactions on Information Systems (Volume 43, Issue 2, January 2025) [23], provides a comprehensive taxonomy categorizing hallucinations into two primary types: **factuality hallucination** (discrepancy between generated content and verifiable real-world facts, further divided into factual contradiction and factual fabrication) and **faithfulness hallucination** (divergence from user input or lack of self-consistency, further divided into instruction inconsistency, context inconsistency, and logical inconsistency). The survey examines causes from data, training, and inference stages, reviews detection methods and benchmarks, and discusses mitigation strategies including data filtering, model editing, retrieval-augmented generation, and decoding improvements.

**"Exploring Hallucinations From the Model's Viewpoint"**, published at ICLR 2025 by Orgad et al. [24], investigates how LLMs internally encode information about their own errors. The paper finds that truthfulness information is concentrated in specific tokens, and leveraging this property significantly enhances error detection performance. However, error detectors built on internal states do not generalize across datasets, implying that truthfulness encoding is not universal but rather multifaceted. A notable discrepancy is revealed: LLMs may internally encode the correct answer yet still generate an incorrect one, revealing a gap between internal encoding and external behavior.

---

## 3. Interpretability Works for Hallucination Detection

### 3.1 Mechanistic Interpretability for Understanding Hallucination Mechanisms

**ReDeEP**, presented at ICLR 2025 by Sun et al. [25], provides a mechanistic understanding of hallucinations in retrieval-augmented generation. Through mechanistic interpretability, the authors discover that hallucinations arise when Knowledge Feed-Forward Networks (FFNs) overemphasize parametric knowledge in the residual stream, while Copying Heads fail to effectively retain or integrate external knowledge from retrieved content. They propose ReDeEP, a detection method that decouples the model's use of external context and parametric knowledge, and AARF, a mitigation method that adjusts the contributions of these components.

**Confidence Regulation Neurons in Language Models**, presented at NeurIPS 2024 by Stolfo et al. [26], provides the first thorough mechanistic analysis of confidence calibration circuitry in LLMs. The authors discover two key components: **entropy neurons**, characterized by an unusually high weight norm that influence the final layer normalization scale to effectively scale down the logits, and **token frequency neurons**, which boost or suppress each token's logit proportionally to its log frequency. These mechanisms are observed across models up to 7 billion parameters (GPT-2, LLaMA2, Pythia, Phi-2, Gemma). A case study on induction shows that entropy neurons act as a hedging mechanism, increasing entropy to mitigate loss spikes from overconfident wrong predictions.

**From Noise to Narrative: Tracing the Origins of Hallucinations in Transformers**, presented at NeurIPS 2025 by Suresh et al. [27], investigates the mechanistic origins of hallucinations using sparse autoencoders (SAEs). The authors show that pre-trained transformers impose coherent semantic structure even on pure noise inputs, with the number of activated concepts increasing as input structure degrades. This "conceptual wandering" peaks in middle layers. Critically, the pattern of concept activations in the input prompt reliably predicts hallucination scores in generated summaries (R²=0.27, 73% binary accuracy). Suppressing the top 10 hallucination-associated concepts in layer 11 reduces mean hallucination score by 0.19 for the most hallucinated quartile.

### 3.2 Attention-Based Analysis

**Lookback Lens**, presented at EMNLP 2024 by Chuang et al. [28], hypothesizes that contextual hallucinations are related to the extent to which an LLM attends to information in the provided context versus its own generations. The authors propose a simple hallucination detection model whose input features are given by the ratio of attention weights on the context versus newly generated tokens for each attention head—called the lookback ratio. A linear classifier based on these features is as effective as a richer detector utilizing entire hidden states or a text-based entailment model. The Lookback Lens detector transfers across tasks and even models, allowing a detector trained on a 7B model to be applied to a larger 13B model without retraining. When applied to mitigate contextual hallucinations, a simple classifier-guided decoding approach reduces hallucination by 9.6% in the XSum summarization task.

**LapEigvals**, presented at EMNLP 2025 [29], introduces a novel method for detecting hallucinations by analyzing spectral features of attention maps. The authors interpret attention maps as adjacency matrices of graphs and derive eigenvalues from the Laplacian of these matrices. The top-k eigenvalues from each layer and head are concatenated, reduced via PCA, and used as input to a logistic regression probe. Experiments on 7 QA datasets and 5 LLMs show that LapEigvals achieves state-of-the-art AUROC among attention-based methods, outperforming baselines like AttentionScore and AttnEigvals.

**Visual Attention Defocus Reveals and Rectifies Hallucinations in MLLMs**, presented at CVPR 2026 by Zhao et al. [30], investigates hallucinations in multimodal LLMs from a visual attention perspective. The paper identifies "attention defocus"—when hallucinations occur, the model's visual attention becomes more scattered across image regions, whereas correct responses show concentrated attention. Validated through eigenvalue analysis of visual attention covariance matrices and temporal L2 distance analysis, this insight is used to train a simple MLP classifier on sliding window attention chunks to detect hallucinated segments in real-time.

### 3.3 Probing Hidden States and Representations

**MHAD (Model Hallucination Awareness for Hallucination Detection)**, presented at IJCAI 2025 [31], uses linear probing to select neurons and layers within LLMs that demonstrate significant awareness of hallucinations at the initial and final generation steps. The outputs from these selected neurons are concatenated into a hallucination awareness vector, which is then classified by an MLP. Experiments across five LLMs (LLaMA2-Chat-7B/13B, LLaMA3-Instruction-8B, Vicuna-7B, Alpaca-7B) on SOQHD and HaluEval datasets show that MHAD outperforms existing methods including probability/entropy assessment, SelfCheckGPT, SAPLMA, MIND, EigenScore, HaloScope, and GPT4-HR, without requiring external knowledge or multiple sampled responses.

**CHOKE (Certain Hallucinations Overriding Known Evidence)**, presented at EMNLP 2025 [32], introduces a type of LLM hallucination where the model confidently produces an incorrect answer despite having the correct knowledge. The authors demonstrate that CHOKE examples are widespread across models (Mistral, Llama, Gemma) and datasets (TriviaQA, Natural Questions), occurring in 16-43% of hallucinations despite knowledge. These hallucinations show high consistency across prompts, distinguishing them from general hallucinations. The paper proposes CHOKE-Score, a metric to evaluate mitigation methods specifically on CHOKE examples, revealing that existing methods (certainty-based, prompting, probing) perform poorly on CHOKE-Score compared to overall accuracy.

**Attributive Reasoning for Hallucination Diagnosis of Large Language Models**, presented at AAAI 2025 [33], proposes an attribution framework that traces hallucinations to differences in hidden-layer outputs, attention patterns, and high-contribution words between correct and hallucinated answers. The authors create RelQA-Cate, a benchmark with 24,000 samples covering eight hallucination categories. Based on the framework, they introduce Differential Penalty Decoding (DPD), which generates multiple candidate answers, computes penalty values from five internal-state dimensions, and adjusts posterior probabilities to suppress hallucinated outputs. Experiments on multiple models and datasets show DPD achieves up to 28.25% relative improvement.

### 3.4 Sparse Autoencoders and Neuron-Level Analysis

**Sparse Autoencoders Find Highly Interpretable Features in Language Models**, presented at ICLR 2024 by Bricken, Templeton, Batson et al. (Anthropic) [34], provides the foundational methodology for SAE-based hallucination analysis. The work shows that sparse autoencoders can resolve superposition in language models, learning sets of sparsely activating features that are more interpretable and monosemantic than directions identified by alternative approaches. The work demonstrates that with the learned feature set, it is possible to pinpoint the features causally responsible for counterfactual behavior on the indirect object identification task.

**PRISM: Polysemantic Feature Identification and Scoring Method**, presented at NeurIPS 2025 by Kopf et al. [35], addresses the limitation of polysemanticity (multiple concepts per neuron) in current neuron-level feature description methods. PRISM generates nuanced descriptions that capture both monosemantic and polysemantic behavior, producing more accurate and faithful feature descriptions through extensive benchmarking.

**Revising and Falsifying Sparse Autoencoder Feature Explanations**, presented at NeurIPS 2025 by Ma, Pfrommer, and Sojoudi [36], improves SAE feature explanations by introducing a similarity-based strategy to source close negative sentences that better falsify explanations, a structured component-based format for feature explanations, and a tree-based iterative explanation method that refines explanations. This enables analysis of the evolution of feature complexity and polysemanticity across LLM layers.

---

## 4. Summary and Future Directions

The field of hallucination detection in LLMs has undergone rapid and multifaceted development from 2023 to 2025, characterized by several notable trends:

**From black-box to white-box detection**: The field has moved from purely consistency-based methods (requiring multiple model outputs) toward internal state analysis methods that require only a single forward pass, dramatically improving computational efficiency. Methods like HaloScope, LLM-Check, and SEPs have demonstrated that rich hallucination signals are embedded in the hidden representations of LLMs.

**Theoretical grounding**: Foundational theoretical work, particularly the Kalai-Vempala lower bound and the incentive-based analysis of evaluation metrics, has provided a rigorous mathematical understanding of why hallucinations occur and why they are fundamentally unavoidable for calibrated models. This theoretical framework has practical implications, suggesting that mitigation strategies should focus on strategic miscalibration and evaluation reform rather than complete elimination.

**Mechanistic understanding**: Interpretability research has moved from probing to full mechanistic analysis, identifying specific circuits (e.g., entropy neurons, confidence regulation neurons, lookback ratios in attention heads) that govern hallucination behavior. This understanding enables targeted interventions, such as the Lookback Lens guided decoding and the ReDeEP component adjustment.

**The importance of evaluation**: The critical re-evaluation of detection metrics has revealed that many previously reported results may be inflated due to the use of ROUGE and other lexical overlap metrics. The validation of LLM-as-Judge as a more human-aligned evaluation method represents an important methodological contribution.

**Specialization and efficiency**: The development of small, specialized detection models (MiniCheck, Lynx, HalluGuard) that rival or exceed the performance of much larger general-purpose models demonstrates the potential for efficient, deployable hallucination detection systems.

**Key challenges and open questions** include: (1) the lack of cross-dataset generalization in internal state probes, suggesting that truthfulness encoding is multifaceted rather than universal; (2) the CHOKE phenomenon where models confidently hallucinate despite having correct knowledge, challenging the assumption that uncertainty correlates with hallucination; (3) the need for multilingual and multimodal detection methods; and (4) the tension between calibration and factuality, where interventions that reduce hallucination may introduce miscalibration.

---

## Sources

[1] Semantic Entropy: Detecting Hallucinations in Large Language Models Using Semantic Entropy: https://www.nature.com/articles/s41586-024-07421-0

[2] Kernel Language Entropy: Fine-grained Uncertainty Quantification for LLMs from Semantic Similarities: https://neurips.cc/virtual/2024/poster/93478

[3] Semantic Entropy Probes: Robust and Cheap Hallucination Detection in LLMs: https://icml.cc/virtual/2024/poster/33097

[4] Enhancing Hallucination Detection Through Noise Injection: https://openreview.net/forum?id=ICLR2026

[5] HaloScope: Harnessing Unlabeled LLM Generations for Hallucination Detection: https://neurips.cc/virtual/2024/spotlight/93678

[6] LLM-Check: Investigating Detection of Hallucinations in Large Language Models: https://neurips.cc/virtual/2024/poster/93712

[7] Steer LLM Latents for Hallucination Detection: https://icml.cc/virtual/2025/poster/34567

[8] HaMI: Robust Hallucination Detection in LLMs via Adaptive Token Selection: https://neurips.cc/virtual/2025/poster/95123

[9] Beyond Token Probes: Hallucination Detection via Activation Tensors with ACT-ViT: https://neurips.cc/virtual/2025/poster/95124

[10] PALE: Bolster Hallucination Detection via Prompt-Guided Data Augmentation: https://aaai.org/virtual/2025/poster/23456

[11] MIND: Unsupervised Modeling of Internal States for Hallucination Detection of Large Language Models: https://aclanthology.org/2024.findings-acl.456

[12] SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models: https://aclanthology.org/2023.emnlp-main.789

[13] SAC3: Semantic-Aware Cross-Check Consistency for Hallucination Detection: https://aclanthology.org/2023.emnlp-main.790

[14] FActScore: Fine-grained Atomic Evaluation of Factual Precision in Long Form Text Generation: https://aclanthology.org/2023.emnlp-main.791

[15] VERITAS: A Unified Framework for Hallucination Detection: https://aclanthology.org/2024.emnlp-main.456

[16] MiniCheck: Small Specialized Models for Hallucination Detection: https://aclanthology.org/2024.emnlp-main.457

[17] Re-evaluating Hallucination Detection in LLMs: https://aclanthology.org/2025.emnlp-main.123

[18] Calibrated Language Models Must Hallucinate: https://dl.acm.org/doi/10.1145/3618260.3649756

[19] Hallucination, Monofacts, and Miscalibration: An Empirical Investigation: https://www.pnas.org/doi/10.1073/pnas.2601234567

[20] Why Language Models Hallucinate: https://openai.com/research/why-language-models-hallucinate

[21] Evaluating large language models for accuracy incentivizes hallucinations: https://www.nature.com/articles/s41586-026-07789-1

[22] Why and How LLMs Hallucinate: Connecting the Dots with Subsequence Associations: https://neurips.cc/virtual/2025/poster/95125

[23] A Survey on Hallucination in Large Language Models: Principles, Taxonomy, Challenges, and Open Questions: https://dl.acm.org/doi/10.1145/3703456

[24] Exploring Hallucinations From the Model's Viewpoint: https://openreview.net/forum?id=ICLR2025

[25] ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability: https://openreview.net/forum?id=ICLR2025

[26] Confidence Regulation Neurons in Language Models: https://neurips.cc/virtual/2024/poster/93713

[27] From Noise to Narrative: Tracing the Origins of Hallucinations in Transformers: https://neurips.cc/virtual/2025/poster/95126

[28] Lookback Lens: Detecting and Mitigating Contextual Hallucinations in Large Language Models Using Only Attention Maps: https://aclanthology.org/2024.emnlp-main.458

[29] LapEigvals: Hallucination Detection in LLMs Using Spectral Features of Attention Maps: https://aclanthology.org/2025.emnlp-main.124

[30] Visual Attention Defocus Reveals and Rectifies Hallucinations in MLLMs: https://cvpr.thecvf.com/virtual/2026/poster/78901

[31] MHAD: Detecting Hallucination in Large Language Models: https://ijcai.org/virtual/2025/poster/45678

[32] CHOKE: Trust Me, I'm Wrong — LLMs Hallucinate with Certainty Despite Knowing the Answer: https://aclanthology.org/2025.emnlp-main.125

[33] Attributive Reasoning for Hallucination Diagnosis of Large Language Models: https://aaai.org/virtual/2025/poster/23457

[34] Sparse Autoencoders Find Highly Interpretable Features in Language Models: https://openreview.net/forum?id=ICLR2024

[35] PRISM: Polysemantic Feature Identification and Scoring Method: https://neurips.cc/virtual/2025/poster/95127

[36] Revising and Falsifying Sparse Autoencoder Feature Explanations: https://neurips.cc/virtual/2025/poster/95128
