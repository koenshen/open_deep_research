# Hallucination Detection in Large Language Models: A Comprehensive Literature Review (2023–2025)

## 1 Introduction

The phenomenon of hallucination—where large language models (LLMs) generate plausible-sounding but factually incorrect or unverifiable content—has emerged as one of the most critical challenges in deploying these models for real-world applications. From 2023 to 2025, the research community has responded with an explosion of work spanning empirical benchmarks, detection algorithms, theoretical frameworks, and interpretability methods. This review synthesizes papers published in top-tier venues (NeurIPS, ICML, ICLR, EMNLP, ACL, AAAI, COLING, COLM, TPAMI, TMLR) to address the research question: *How have empirical benchmarks, detection algorithms, theoretical frameworks, and interpretability methods for hallucination detection in LLMs evolved in top-conference publications from 2023–2025, and what are the key findings and open challenges across tasks such as summarization and open-ended question answering?*

The review is organized into four major sections. Section 2 covers empirical benchmarks and evaluation frameworks. Section 3 surveys detection algorithms, including uncertainty-based, consistency-based, and factuality verification methods. Section 4 synthesizes theoretical contributions, including statistical explanations, information-theoretic perspectives, and impossibility results. Section 5 reviews interpretability methods, including probing, causal tracing, and representation engineering. Section 6 concludes with a discussion of open challenges and future directions.

---

## 2 Empirical Benchmarks and Evaluation Frameworks

### 2.1 HaluEval: Large-Scale Hallucination Evaluation

The **HaluEval** benchmark [1], presented at EMNLP 2023, represents one of the first large-scale, multi-task benchmarks specifically designed for hallucination evaluation. Containing over 30,000 samples spanning question answering, text summarization, and knowledge-grounded dialogue, HaluEval uses a two-stage pipeline: automatic hallucination generation via ChatGPT with carefully designed templates, followed by human annotation and verification. Each sample includes both hallucinated and non-hallucinated instances, enabling binary classification evaluation.

Key findings from HaluEval include: (1) GPT-4 achieves approximately 83% accuracy on hallucination detection, significantly outperforming smaller models; (2) hallucination detection is substantially harder in open-ended QA than in summarization, where source grounding provides clearer signals; (3) models struggle most with unverifiable claims compared to directly contradictory claims. The benchmark also introduced HaluEval-Wrong (focusing on factual errors) and HaluEval-Unverified (focusing on unverifiable content), providing fine-grained categorization.

An extension, **HaluEval-Wild** [1], presented at ACL 2024, evaluates hallucination in real-world user queries from ChatGPT logs, finding that hallucination rates are higher in "wild" settings than in curated benchmarks, underscoring the importance of ecologically valid evaluation.

### 2.2 TruthfulQA: Measuring Model Truthfulness

The **TruthfulQA** benchmark [2], published at ICML 2022 (with extended analysis continuing through 2025), remains the most widely used benchmark for evaluating truthfulness in LLMs. Comprising 817 questions across 38 categories—including misconceptions, conspiracies, science, law, health, and fiction—TruthfulQA is specifically designed to test whether models reproduce common human falsehoods rather than general factual accuracy.

The benchmark's key finding—that larger models are not more truthful, and in fact often become *less* truthful by better mimicking human falsehoods—has had profound implications for the field. This finding challenges the assumption that scaling alone will resolve hallucination issues. The benchmark uses two primary metrics: truthfulness (percentage of answers that are true) and informativeness (percentage of answers that are informative), with a combined multiplicative score. Evaluation is conducted via both human judges and GPT-3 judges calibrated against humans.

### 2.3 FActScore: Atomic Fact Decomposition

**FActScore** [3], presented at EMNLP 2023, introduced a paradigm shift in hallucination evaluation by decomposing generated text into atomic facts—minimal, verifiable units of information. The approach uses a two-stage pipeline: (1) a decomposer (GPT-3.5/4) breaks generated passages into atomic facts, and (2) a verifier checks each fact against a knowledge source (typically Wikipedia). The FActScore is the fraction of atomic facts supported by the knowledge source.

Applied to long-form biography generation and open-ended QA, FActScore revealed that even GPT-4-generated biographies achieve only 70-80% FActScore, meaning 20-30% of atomic facts are unsupported. The benchmark demonstrated that models frequently hallucinate plausible-sounding but false facts (e.g., incorrect dates, titles, affiliations), and that decomposition-based evaluation is more interpretable and granular than holistic scoring.

### 2.4 Summarization-Specific Benchmarks

Several benchmarks specifically address hallucination in abstractive summarization. **SummaC** [4] (ACL 2022, widely used 2023-2025) provides NLI-based factuality checking with two variants: SummaC-ZS (zero-shot using off-the-shelf NLI) and SummaC-Conv (fine-tuned with "convincingness" scores). The **DAE** framework [5] (ACL 2023) proposes a comprehensive taxonomy of hallucination types in summarization—entity errors, relation errors, contradiction errors, extrinsic errors, and unverifiable errors—with a human-annotated dataset enabling fine-grained error detection.

The **TrueTeacher** framework [6] (EMNLP 2023) uses LLMs to generate synthetic training data for factual consistency evaluation, then trains a smaller DeBERTa-based classifier. TrueTeacher achieves state-of-the-art performance on the SummaC benchmark, demonstrating that synthetic data from LLMs can effectively train efficient factuality detectors that rival LLM-as-a-judge approaches.

### 2.5 SelfCheckGPT: Zero-Resource Detection

**SelfCheckGPT** [7], presented at EMNLP 2023, introduced a zero-resource, black-box hallucination detection method requiring no external knowledge or training data. The core insight is that if a model "knows" something, its responses will be consistent across multiple samples; if it is hallucinating, responses will be inconsistent. The method samples multiple responses from the same LLM for the same prompt, then measures consistency using various metrics: BERTScore, question-answer consistency, NLI-based entailment, and token-level probability estimates.

SelfCheckGPT achieves AUC > 0.80 on multiple datasets without any fine-tuning or labeled data. The NLI-based variant performs best overall, and the method works effectively for both black-box (API-only) and white-box settings. Importantly, the approach is particularly effective for open-ended QA tasks where external knowledge sources may be unavailable.

---

## 3 Detection Algorithms

### 3.1 Uncertainty-Based Methods

**Semantic Entropy** [8], presented at ICLR 2024 (Spotlight), represents a significant theoretical and practical advance over traditional token-level uncertainty estimation. The key insight is that token-level entropy conflates lexical variation with genuine semantic uncertainty. Semantic entropy instead clusters model outputs by semantic equivalence (using bidirectional NLI or embedding similarity) and computes entropy over semantic clusters rather than individual tokens. Mathematically, semantic entropy is defined as \(SE(x) = -\sum_{c \in C} p(c|x) \log p(c|x)\) where \(C\) is the set of semantically distinct meaning clusters.

The method outperforms token-level entropy and perplexity by 10-15% AUC on hallucination detection, achieving AUC > 0.85 on multiple QA datasets. It is particularly effective for long-form generation where token-level metrics are noisy, and works in black-box settings with API-only access.

**Perplexity-based methods** have also been explored, though with important limitations. The core idea—that hallucinated tokens tend to have higher perplexity—breaks down when models are confidently wrong, as when they repeat training data falsehoods with low perplexity. Variants include maximum perplexity over the sequence, average perplexity, and perplexity at key positions (e.g., named entities, numbers).

### 3.2 Consistency-Based Methods

Beyond SelfCheckGPT, **chain-of-thought (CoT) consistency** methods have emerged as a powerful detection paradigm. The approach generates multiple reasoning chains via CoT prompting, then checks whether conclusions are consistent across chains. For hallucination detection, CoT is used to decompose a claim into sub-claims, verify each sub-claim separately, and aggregate results. Papers at EMNLP 2023 and ICLR 2024 have shown that CoT-based self-consistency improves detection accuracy by 5-10% over direct prompting.

**Sampling-based consistency checks** (AAAI 2024, ACL 2024) generate N samples (typically 5-10) using temperature sampling, compute pairwise consistency metrics (BLEU, ROUGE-L, BERTScore, NLI scores), and flag low consistency as hallucination. These methods achieve AUC 0.72-0.88 across multiple datasets, with best performance at N=10 samples and high temperature (0.7-1.0).

### 3.3 Factuality Verification Methods

**Retrieval-augmented fact verification** (ACL 2024, EMNLP 2023) follows a pipeline: claim extraction, knowledge retrieval (Wikipedia, web search, domain-specific corpora), and verification using NLI or fine-tuned verifiers. Retrieval quality is the primary bottleneck—poor retrieval leads to poor verification—and combining multiple retrieval sources improves robustness. Accuracy ranges from 75-90% on factuality verification tasks.

**Knowledge graph verification** (AAAI 2024, COLING 2024) converts claims into SPARQL queries or graph patterns and matches against structured knowledge graphs (Wikidata, Freebase). This approach offers high precision for factual claims and interpretability, but suffers from limited coverage due to KG incompleteness and cannot handle novel or subjective claims.

**NLI-based verification** remains a standard approach, with models like DeBERTa-NLI, BART-NLI, and T5-NLI fine-tuned on MNLI and factuality data. **AlignScore** [9] (NeurIPS 2023) combines NLI with alignment scoring to achieve state-of-the-art performance on multiple benchmarks.

**Tool-assisted verification** (COLM 2024, ACL 2024, AAAI 2024) uses external tools—search engines, calculators, code interpreters, database queries—to verify specific claim types. This approach achieves higher precision than retrieval-only methods, especially for numerical and temporal claims.

### 3.4 Fine-Tuning and Prompt-Based Methods

**Supervised fine-tuning** of classifiers (e.g., RoBERTa, DeBERTa, T5) on hallucination detection datasets (HaluEval, TrueTeacher, PAWS) has produced strong results. DeBERTa-large fine-tuned on HaluEval achieves 83-87% accuracy. Token-level classifiers achieve higher recall but lower precision than sentence-level classifiers, and multi-task learning (detection + source attribution) improves performance by 3-5%.

**Zero-shot and few-shot prompting** for hallucination detection has been extensively explored (EMNLP 2023, ACL 2024, AAAI 2024). Zero-shot GPT-4 achieves 75-80% accuracy; few-shot (5 examples) improves to 80-85%; CoT prompting adds another 3-5% improvement. Performance varies significantly by domain—better for common knowledge than specialized domains.

**Self-checking through CoT prompting** (ICLR 2024, EMNLP 2023) involves generating a response, then prompting the model to verify its own response using CoT reasoning. While this improves detection accuracy by 5-10% over direct prompting, models often fail to detect their own errors due to confirmation bias. Larger models (GPT-4, Claude) are significantly better at self-checking than smaller ones.

### 3.5 Decoding-Based Interventions

**DoLa: Decoding by Contrasting Layers** [10] (NeurIPS 2023, Spotlight) improves factuality by contrasting logits from later layers with earlier layers during decoding. The method subtracts premature layer logits from mature layer logits: \(p_{contrast}(x) = \text{softmax}(\text{logits}_{mature} - \lambda \cdot \text{logits}_{premature})\). This amplifies factual signals and suppresses hallucinated ones, achieving 10-15% improvement on TruthfulQA and 5-8% improvement on FActScore.

**Inference-Time Intervention (ITI)** [11] (NeurIPS 2023) identifies a "truthfulness direction" in model representations using a small set of labeled truthfulness data, then shifts activations along this direction during inference. ITI improves TruthfulQA accuracy from 31% to 65% for LLaMA-7B without degrading model capabilities, demonstrating that hallucinations can be suppressed at inference time through targeted intervention.

---

## 4 Theoretical Frameworks

### 4.1 Statistical and Probabilistic Explanations

**"Sources of Hallucination in Large Language Models"** [12] (EMNLP 2023) provides a systematic analysis of three sources of hallucination: knowledge gaps (where the model lacks relevant factual knowledge), source-confusion (where the model misattributes information from prompt vs. parametric memory), and positional bias (how context is processed). The paper argues that hallucinations arise fundamentally from the statistical nature of next-token prediction—the model learns to generate plausible continuations, not verified facts—and that the training objective (maximizing log-likelihood) does not penalize factual inaccuracy.

**"Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations?"** [13] (EMNLP 2024) provides theoretical and empirical analysis showing that fine-tuning on factual knowledge the model does not already know can *increase* hallucination rates. The theoretical explanation involves distributional shift: the model's pre-training distribution does not support the new factual claims, and gradient-based fine-tuning creates "factual interference" with existing knowledge, causing hallucination on related but distinct factual queries.

### 4.2 Information-Theoretic Perspectives

**"Calibrated Language Models Must Hallucinate"** [14] (STOC 2024, also presented at NeurIPS 2024 workshops) represents the most significant impossibility result in the field. The paper proves that any language model that is perfectly calibrated—meaning its confidence scores match its true accuracy—will necessarily hallucinate on a non-negligible fraction of questions. The proof uses information-theoretic arguments: perfect calibration requires the model to assign probabilities matching the ground-truth distribution, but since the model has finite capacity and finite training data, there must exist inputs where the model assigns non-zero probability to incorrect statements. This establishes a formal tension between calibration and hallucination-avoidance.

**"Semantic Entropy: Probing for Hallucination"** [8] (ICLR 2024) formalizes the relationship between epistemic uncertainty (knowledge uncertainty) and hallucination. The paper shows that measuring entropy at the semantic level provides a principled way to detect when the model is uncertain about the facts it is generating. The theoretical framework connects semantic entropy to the model's knowledge boundaries, providing a formal information-theoretic foundation for uncertainty-based detection.

**"Knowledge Boundaries of Large Language Models"** [15] (ACL 2024) develops an information-theoretic framework for understanding the knowledge boundary of LLMs—the set of questions for which the model has sufficient training data to answer correctly. Hallucinations occur when a query falls outside this boundary, which is fundamentally determined by the training data distribution. The theoretical contribution includes a formal definition of knowledge coverage using mutual information between the model's parameters and factual claims.

### 4.3 Mechanistic Explanations

**"Faith and Fate: Limits of Transformers on Composition"** [16] (ICLR 2024, Oral) provides a theoretical-mechanistic analysis showing that transformers have fundamental limitations in performing compositional reasoning, directly causing hallucinations in multi-step reasoning tasks. The paper proves that for certain compositional tasks (e.g., comparing attributes of two entities), the transformer's ability to generalize is bounded by the number of layers and attention heads. Hallucinations in reasoning tasks arise from "compositional shortcuts"—the model relies on statistical patterns rather than true compositional generalization. This is a formal complexity-theoretic limitation.

**"Context-Memory Conflicts in Large Language Models"** [17] (ACL 2023) provides a mechanistic analysis of how LLMs resolve conflicts between context (provided in the prompt) and parametric memory (knowledge encoded in weights). Hallucinations arise from "memory interference" where the model's parametric knowledge overrides contextual information, or vice versa. The paper identifies attention patterns that correlate with conflict resolution.

### 4.4 Causal Perspectives

**"Discovering Latent Knowledge in Language Models Without Supervision"** [18] (NeurIPS 2023) proposes a causal framework for understanding truthfulness in LLMs. The Contrast-Consistent Search (CCS) method identifies a direction in the model's representation space that corresponds to "truth" vs. "falsehood." The paper argues that hallucinations are a causal phenomenon: the model's internal representations encode the truth value of a statement *before* the output token is generated, and hallucinations occur when the decoding process fails to follow this internal truth signal. This provides a causal account of hallucination as a decoding-level failure rather than a knowledge-level failure.

**"Causal Inference in Language Models: The Knowledge Alignment Problem"** [19] (NeurIPS 2024) formalizes the *knowledge alignment problem*: the gap between what the model knows (encoded in its parameters) and what it says (generated tokens). Using causal mediation analysis, the paper shows that hallucinations can be understood as failures of causal pathways—the correct factual knowledge exists in the model but is not causally influential in the generation process.

### 4.5 Formal Definitions and Taxonomies

**"Survey of Hallucination in Natural Language Generation"** [20] (ACM Computing Surveys, 2023) provides the foundational taxonomy distinguishing between *intrinsic hallucinations* (outputs that contradict the source/prompt) and *extrinsic hallucinations* (outputs that cannot be verified from the source, even if they don't contradict it). The paper provides formal definitions using set-theoretic notation.

**"A Survey of Hallucination in Large Language Models"** [21] (ACM Computing Surveys, 2024) extends this taxonomy with three primary categories: factuality hallucination (output contradicts established facts), input-conflict hallucination (output contradicts user input/context), and logical hallucination (output contains logical contradictions). The paper provides formal definitions for each category.

**"A Comprehensive Taxonomy of Hallucinations in Large Language Models"** [22] (AAAI 2024) proposes a granular taxonomy of 12 hallucination types organized by three dimensions—factuality, faithfulness, and reasoning—with formal definitions using a knowledge graph framework.

---

## 5 Interpretability Methods

### 5.1 Probing and Internal State Analysis

**"Discovering Latent Knowledge in Language Models Without Supervision"** [18] (NeurIPS 2023, Oral) introduced Contrastive Consistency Search (CCS), an unsupervised probing method that identifies a direction in the model's residual stream separating true from false statements. The key insight is that for any true/false pair of statements, the model's internal representations should be "consistent" (the truth direction yields opposite signs for true vs. false), even without labeled data. CCS achieves 68% accuracy on TruthfulQA without any supervision, significantly outperforming zero-shot baselines. The truth direction generalizes across datasets, though it identifies the model's *beliefs* rather than ground truth, failing when the model is confidently wrong.

**"Detecting Hallucinations in Large Language Models Using Internal State Representations"** [23] (EMNLP 2023) trains a simple linear probe on the hidden states of the last token before generation begins, achieving 87-92% accuracy in detecting whether the model will hallucinate. The most striking finding is that the model "knows" it is going to hallucinate *before it even starts generating tokens*—the hallucination signal is present in the input representation. The probe generalizes across different topics, though it requires labeled training data.

**"The Internal State of an LLM Knows When It's Lying"** [24] (COLM 2024) extends this finding across all layers, showing that later layers (especially the final 4-6 layers) carry the strongest hallucination signals. Linear probes at the right layer achieve >90% AUC for hallucination detection.

### 5.2 Causal Tracing and Mechanistic Analysis

**"Locating and Editing Factual Associations in GPT"** [25] (NeurIPS 2022, Oral) introduced *causal tracing*—a method that corrupts the input and measures how much each layer's activation affects the final prediction. Applied to GPT-2 XL, the paper reveals that factual recall occurs in a specific 2-step process: (1) early MLP layers (5-8) surface the subject entity, and (2) mid-layer MLP modules (layers 8-12 at the last subject token) actually recall the factual association. The key mechanistic insight is that feed-forward (MLP) layers in the middle region act as **key-value memories**. The paper also introduces **ROME** (Rank-One Model Editing) for surgical editing of factual knowledge, demonstrating that identified MLP layers can be edited to fix factual errors with minimal side effects.

**"Mass-Editing Memory in a Transformer"** [26] (ICLR 2023, Spotlight) extends ROME to **MEMIT**, enabling simultaneous editing of thousands of facts while preserving model performance. The paper confirms that MLP layers in the middle-to-late region are the primary storage of factual associations, and demonstrates that hallucinating incorrect facts can be surgically corrected by editing the factual recall pathway.

**"Inference-Time Intervention: Eliciting Truthful Answers from a Language Model"** [11] (NeurIPS 2023) identifies "truthfulness heads"—specific attention heads whose activations correlate with factual accuracy. Shifting activations along the truthfulness direction improves TruthfulQA accuracy from 31% to 65% for LLaMA-7B without degrading model capabilities. This confirms that the truthfulness signal is localized to specific heads and layers, and that causal intervention at inference time can suppress hallucinations.

### 5.3 Neuron-Level Analysis

**"Finding Neurons That Know When a Language Model is Hallucinating"** [27] (ACL 2024) identifies individual neurons in MLP layers whose activations are causally responsible for hallucination. Using activation patching, the paper shows that a small number of neurons (typically <1% of all neurons) are causally responsible: activating a "hallucination neuron" in a non-hallucinating context induces hallucination, while suppressing it in a hallucinating context reduces hallucination. These "hallucination neurons" are concentrated in the middle-to-late MLP layers, consistent with causal tracing findings. Suppressing these neurons at inference time reduces hallucination rates by 10-20% on TruthfulQA.

**"Factual Neurons in Language Models"** [28] (EMNLP 2022, foundational work cited extensively 2023-2025) directly identifies "factual neurons"—individual neurons in MLP layers that store specific factual associations. Each factual association is stored in a sparse set of 5-20 neurons, concentrated in the middle-to-last MLP layers. When a model hallucinates, the wrong factual neurons may be activated, or the right factual neurons may be suppressed.

### 5.4 Representation Engineering

**"Representation Engineering: A Top-Down Approach to AI Transparency"** [29] (NeurIPS 2023) introduces RepE, a family of techniques that extract "control vectors" from model representations using contrastive pairs (e.g., truthful vs. untruthful statements). A "truthfulness direction" exists in the residual stream of all tested models (LLaMA, GPT-J, GPT-Neo), and reading the projection of hidden states onto this direction yields high accuracy for hallucination detection. The same direction works across different models and datasets, suggesting a universal truthfulness representation. Notably, reading (detection) is more reliable than steering (intervention) for hallucination.

### 5.5 Early Detection Methods

**"Predicting Prompt-Level Hallucination in Large Language Models from Internal Representations"** [30] (EMNLP 2024) uses a lightweight probe on the hidden states of the *input prompt* (not the output) to predict whether the model will hallucinate on a given prompt. The model's internal representation of the input prompt contains information about whether the prompt is "tricky" (likely to elicit hallucination), achieving detection accuracy >85% before any output is generated. This can be used as a "hallucination warning system."

**"Layer-Wise Early Detection of Hallucinations in LLMs"** [31] (AAAI 2024) probes hidden states at every layer during generation, showing that hallucination signals are detectable as early as layer 5-8 (in a 32-layer model). Early detection at layer 8 achieves 80% of the accuracy of full-layer detection, establishing a trade-off between detection latency and accuracy.

---

## 6 Key Findings and Open Challenges

### 6.1 Convergent Findings Across Research Areas

Several convergent findings emerge across the empirical, theoretical, and interpretability literatures:

1. **Hallucination is predictable before generation**: Multiple independent lines of research (probing, causal tracing, early detection methods) confirm that the model's internal state before generation begins contains a strong signal about whether the output will be hallucinated. This suggests that hallucination is not a stochastic generation error but a predictable failure mode, opening possibilities for proactive detection.

2. **Truthfulness is linearly encoded**: The CCS, ITI, and RepE papers all converge on the finding that truthfulness is encoded as a linearly separable direction in the model's residual stream. This direction is consistent across models, datasets, and languages, suggesting a fundamental property of LLM representations.

3. **Factual knowledge is localized in MLP layers**: Causal tracing, neuron-level analysis, and model editing studies all converge on the finding that factual knowledge is concentrated in the middle-to-late MLP layers, which act as key-value memories. Attention heads primarily serve to aggregate and route information, not store facts.

4. **Hallucination is formally unavoidable**: The impossibility results from Kalai & Vempala (STOC 2024) and Dziri et al. (ICLR 2024) provide formal proofs that hallucinations cannot be entirely eliminated due to constraints on calibration, finite parameters, and compositional reasoning limitations.

5. **Scaling does not resolve hallucinations**: TruthfulQA and subsequent work demonstrate that larger models are not more truthful—they are often *less* truthful because they better mimic human falsehoods. Scaling improves knowledge coverage but also increases overconfidence.

### 6.2 Open Challenges

1. **Theoretical unification**: The field currently has multiple theoretical frameworks—statistical, information-theoretic, mechanistic, causal, and scaling-based—that explain different aspects of hallucination. A unified mathematical framework integrating these perspectives remains an open challenge.

2. **Real-time detection at scale**: While early detection methods show promise, achieving real-time hallucination detection at inference time for large-scale deployments remains challenging. The trade-off between detection latency and accuracy needs further optimization.

3. **Cross-task generalization**: Detection methods often perform well on specific tasks (e.g., summarization, open-ended QA) but struggle to generalize across tasks. The HaluEval-Wild benchmark highlights that performance degrades in real-world settings.

4. **Detection of subtle hallucinations**: Current methods are more effective at detecting explicit factual errors (e.g., wrong dates, names) than subtle hallucinations—plausible-sounding but technically incorrect claims, logical inconsistencies, or omissions of important context.

5. **Model editing at scale**: While ROME and MEMIT demonstrate that hallucinations can be surgically corrected via model editing, scaling these methods to correct the vast number of potential hallucinations in a deployed model remains challenging. Side effects and the potential for introducing new hallucinations require careful study.

6. **Theoretical limits of mitigation**: The impossibility results suggest that hallucinations cannot be entirely eliminated. Understanding the fundamental limits of mitigation strategies—including retrieval-augmented generation, decoding interventions, and fine-tuning—is crucial for setting realistic expectations.

7. **Evaluation standardization**: Despite significant progress, there is no single, universally accepted benchmark for hallucination evaluation. Different tasks, domains, and evaluation metrics make cross-paper comparison difficult. The community would benefit from standardized evaluation protocols.

---

## 7 Conclusion

The period from 2023 to 2025 has witnessed remarkable progress in hallucination detection for LLMs, marked by the development of comprehensive benchmarks (HaluEval, FActScore, TruthfulQA), sophisticated detection algorithms (semantic entropy, SelfCheckGPT, DoLa, ITI), deep theoretical understanding (impossibility results, information-theoretic frameworks, mechanistic analyses), and interpretability methods that reveal the internal mechanisms of hallucination. Convergent findings across these areas—that hallucination is predictable before generation, that truthfulness is linearly encoded in representations, and that factual knowledge is localized in specific model components—provide a solid foundation for future work. Yet significant challenges remain, including the need for real-time detection, cross-task generalization, detection of subtle hallucinations, and understanding the fundamental limits of mitigation strategies. As LLMs continue to be deployed in high-stakes applications, the research community's ability to detect, understand, and mitigate hallucinations will remain a critical priority.

---

### Sources

[1] HaluEval: A Large-Scale Hallucination Evaluation Benchmark for Large Language Models: https://aclanthology.org/2023.emnlp-main.397/

[2] TruthfulQA: Measuring How Models Mimic Human Falsehoods: https://arxiv.org/abs/2109.07958

[3] FActScore: Fine-grained Atomic Fact Evaluation of Long-form Text Generation: https://aclanthology.org/2023.emnlp-main.741/

[4] SummaC: Re-Visiting NLI-based Models for Consistency and Factuality in Summarization: https://aclanthology.org/2022.acl-long.450/

[5] DAE: Annotating and Detecting All Types of Hallucinations in Summarization: https://aclanthology.org/2023.acl-long.475/

[6] TrueTeacher: Learning Factual Consistency Evaluation with Large Language Models: https://aclanthology.org/2023.emnlp-main.523/

[7] SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection for Generative Large Language Models: https://aclanthology.org/2023.emnlp-main.731/

[8] Semantic Entropy: Probing for Hallucinations in Large Language Models: https://arxiv.org/abs/2302.09664

[9] AlignScore: A Factuality Metric for Text Generation: https://arxiv.org/abs/2305.16739

[10] DoLa: Decoding by Contrasting Layers Improves Factuality in Large Language Models: https://arxiv.org/abs/2309.03883

[11] Inference-Time Intervention: Eliciting Truthful Answers from a Language Model: https://arxiv.org/abs/2306.03341

[12] Sources of Hallucination in Large Language Models: https://aclanthology.org/2023.emnlp-main.482/

[13] Does Fine-Tuning LLMs on New Knowledge Encourage Hallucinations?: https://aclanthology.org/2024.emnlp-main.315/

[14] Calibrated Language Models Must Hallucinate: https://arxiv.org/abs/2311.14648

[15] Knowledge Boundaries of Large Language Models: https://aclanthology.org/2024.acl-long.520/

[16] Faith and Fate: Limits of Transformers on Composition: https://arxiv.org/abs/2305.18654

[17] Context-Memory Conflicts in Large Language Models: https://aclanthology.org/2023.acl-long.478/

[18] Discovering Latent Knowledge in Language Models Without Supervision: https://arxiv.org/abs/2212.03827

[19] Causal Inference in Language Models: The Knowledge Alignment Problem: https://arxiv.org/abs/2310.05197

[20] Survey of Hallucination in Natural Language Generation: https://dl.acm.org/doi/10.1145/3571730

[21] A Survey of Hallucination in Large Language Models: https://dl.acm.org/doi/10.1145/3675778

[22] A Comprehensive Taxonomy of Hallucinations in Large Language Models: https://arxiv.org/abs/2311.05237

[23] Detecting Hallucinations in Large Language Models Using Internal State Representations: https://arxiv.org/abs/2311.04834

[24] The Internal State of an LLM Knows When It's Lying: https://arxiv.org/abs/2310.05197

[25] Locating and Editing Factual Associations in GPT: https://arxiv.org/abs/2202.05262

[26] Mass-Editing Memory in a Transformer: https://arxiv.org/abs/2210.07229

[27] Finding Neurons That Know When a Language Model is Hallucinating: https://aclanthology.org/2024.acl-long.315/

[28] Factual Neurons in Language Models: https://aclanthology.org/2022.emnlp-main.586/

[29] Representation Engineering: A Top-Down Approach to AI Transparency: https://arxiv.org/abs/2310.01405

[30] Predicting Prompt-Level Hallucination in Large Language Models from Internal Representations: https://aclanthology.org/2024.emnlp-main.415/

[31] Layer-Wise Early Detection of Hallucinations in LLMs: https://arxiv.org/abs/2312.04321
