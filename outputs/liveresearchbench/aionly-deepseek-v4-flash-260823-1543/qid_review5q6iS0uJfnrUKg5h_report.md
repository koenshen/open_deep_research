# Hallucination Detection in Large Language Models: A Review

## 1. Introduction

The widespread adoption of large language models (LLMs) has been accompanied by a critical challenge: the tendency to generate plausible but factually incorrect or unverifiable content—a phenomenon broadly termed hallucination. Over the 2023–2025 period, the research community has produced a substantial body of work addressing hallucination detection, spanning theoretical foundations, benchmark construction, empirical detection algorithms, and mechanistic interpretability. This review synthesizes contributions from top-tier venues (ICML, NeurIPS, ICLR, EMNLP, ACL, AAAI, IJCAI, COLM, Nature, STOC, and others) to trace the progression of coherent research lines in this rapidly evolving area.

## 2. Theoretical Underpinnings of Hallucination

A foundational theoretical result established by Kalai and Vempala (STOC 2024) proves that any calibrated language model must hallucinate, regardless of the quality of its training data. The argument connects hallucination rates to the prevalence of “monofacts”—facts appearing exactly once in the training corpus—and shows that the hallucination rate is lower-bounded by the rare-fact rate minus a small miscalibration term. This work formalizes the intuition that heavy-tailed factual distributions inevitably lead to errors, even under idealized conditions.

Building on this, Nie et al. (ICML 2025) introduced FactTest, a statistical framework for factuality testing with finite-sample and distribution-free guarantees. FactTest formulates hallucination detection as a hypothesis test that controls the Type I error (mistakenly classifying a truthful answer as hallucinated) at a user-specified significance level, while also providing strong Type II error control under mild conditions. The method is model-agnostic and maintains effectiveness under covariate shifts, enabling LLMs to abstain from answering unknown questions with provable guarantees.

At the same workshop, Karbasi et al. (ICML 2025 Workshop on Reliable and Responsible Foundation Models) established a theoretical equivalence between automated hallucination detection and language identification, proving that detection is impossible for most collections of languages unless the detector is provided with both positive and explicitly labeled negative examples. This underscores the fundamental importance of expert-labeled feedback (e.g., RLHF) for practical detection.

These theoretical contributions clarify that while hallucination cannot be eliminated entirely, it can be bounded and mitigated through appropriate statistical tools and training strategies.

## 3. Benchmarks for Evaluating Hallucination

The development of high-quality benchmarks has been a central empirical thrust. Li et al. (EMNLP 2023) released **HaluEval**, a large-scale benchmark containing 35,000 hallucinated and normal samples across question answering, dialogue, and summarization. The benchmark includes both automatically generated and human-annotated examples, revealing that ChatGPT hallucinates in approximately 19.5% of user queries. HaluEval has since been extended to wild adversarial queries and broader domains, and it remains a widely used evaluation suite.

Min et al. (EMNLP 2023) proposed **FActScore**, a fine-grained evaluation metric that decomposes a generation into atomic facts and computes the percentage supported by a reliable knowledge source. Human evaluation of commercial models (InstructGPT, ChatGPT, PerplexityAI) showed that ChatGPT achieves only 58% factual precision on biographies. The automated FActScore estimator, based on retrieval and a strong LLM, achieves less than 2% error rate and has been used to evaluate 6,500 generations from 13 recent LMs.

The **ANAH** project (Ji et al., ACL 2024) introduced a bilingual (English/Chinese) dataset with ~12k sentence-level annotations for ~4.3k LLM responses, covering over 700 topics. A generative annotator trained on ANAH surpassed all open-source LLMs and GPT-3.5, achieving performance competitive with GPT-4. Its successor, **ANAH-v2** (NeurIPS 2024), scales the annotation pipeline through iterative self-training based on Expectation-Maximization, expanding to ~196k model responses and ~822k annotated sentences. The final 7B detector surpasses GPT-4 on HaluEval and HalluQA by zero-shot inference.

**RAGTruth** (Niu et al., ACL 2024) targets word-level hallucinations in retrieval-augmented generation (RAG). It contains nearly 18,000 naturally generated responses from diverse LLMs using RAG, with meticulous manual annotations at both case and word levels. The corpus has enabled systematic benchmarking of hallucination frequencies across different LLMs and demonstrated that fine-tuning a relatively small LLM can achieve competitive detection performance compared to prompt-based GPT-4.

**FactCHD** (Zhejiang University et al., IJCAI 2024) provides 51,383 factual/non-factual samples for training and 6,960 for evaluation across domains such as health, medicine, climate, and science. It covers diverse factuality patterns (vanilla, multi-hop, comparison, set operations) and introduces the TRUTH-TRIANGULATOR framework that combines tool-enhanced ChatGPT with LoRA-tuned Llama2 for improved detection.

**HalluLens** (Bang et al., ACL 2025) establishes a clear taxonomy distinguishing extrinsic hallucinations (inconsistent with training data) from intrinsic hallucinations (inconsistent with input context). The benchmark includes three evaluation tasks: PreciseWikiQA (5,000 dynamically generated questions), LongWiki (long-form generation), and NonExistentRefusal (evaluating refusal on nonexistent entities). GPT-4o achieves the highest correct answer rate (52.59%) while maintaining a low false refusal rate.

**PHANTOM** (Ji et al., NeurIPS 2025) addresses the financial domain with long-context QA, revealing that out-of-the-box models struggle to detect real-world hallucinations in financial documents, but fine-tuning on PHANTOM shows promise. Other notable benchmarks include **MHaluBench** (ACL 2024) for multimodal hallucination detection, **FACTOR** (2024) for factuality comparison, and **Med-HALT** (2023) for medical domain evaluation.

## 4. Detection Methods

### 4.1 Consistency-Based Detection

Uncertainty estimation through response consistency has emerged as a powerful paradigm. **SelfCheckGPT** (Manakul et al., EMNLP 2023) pioneered the zero-resource, black-box approach: multiple stochastic responses are sampled from the LLM, and the consistency between them is measured using variants such as BERTScore, NLI, or question-answering. The method achieves 93.42 AUC-PR for sentence-level non-factual detection on WikiBio passages, outperforming grey-box methods that rely on token probabilities.

Farquhar et al. (Nature 2024) proposed **Semantic Entropy**, a statistically grounded estimator that clusters multiple sampled answers by meaning (using bidirectional entailment) and computes entropy over meaning clusters. High semantic entropy indicates confabulation—arbitrary and incorrect generations. The method achieves an average AUROC of 0.790 across 30 task-model combinations, outperforming naive entropy (0.691) and P(True) (0.698). It is unsupervised, generalizes across tasks, and works with both white-box and black-box models (via a discrete approximation). A limitation is that it does not catch cases where the model was trained on incorrect reasoning or deliberate deception.

**HaMI** (Niu et al., NeurIPS 2025) reformulates hallucination detection as a Multiple Instance Learning problem, where each response sequence is a “bag” of token instances. The method adaptively selects the most indicative tokens for hallucination and integrates three levels of predictive uncertainty (token-level probability, sentence-level perplexity, semantic consistency). On four QA benchmarks (TriviaQA, SQuAD, Natural Questions, BioASQ) using LLaMA-3.1-8B, Mistral-Nemo-Instruct, and LLaMA-3.3-70B, HaMI achieves 8.1–11.9% average AUROC improvement over the state-of-the-art MARS-SE method.

### 4.2 Internal State and Probing-Based Detection

Exploiting the hidden states of LLMs for hallucination detection has been a fertile direction. **HaloScope** (Du et al., NeurIPS 2024 Spotlight) leverages unlabeled LLM generations by modeling them as a mixture of truthful and hallucinated distributions. It identifies a latent subspace in the LLM activation space associated with hallucinated statements via SVD, then trains a binary classifier. Without any labeled data, HaloScope outperforms prior methods by 10.69% AUROC on TruthfulQA (78.64%) and achieves 94.04% AUROC on TYDIQA-GP with LLaMA-2-7b. It requires only a single sampling pass, making it computationally efficient, and shows strong cross-dataset transferability.

**LLM-Check** (Sriramanan et al., NeurIPS 2024) detects hallucinations within a single LLM response by analyzing internal hidden states, attention maps, and output prediction probabilities of an auxiliary LLM. The method achieves speedups of up to 45×–450× over consistency-based baselines while delivering significant improvements across diverse datasets.

**TSV** (Park et al., ICML 2025) introduces a lightweight, plug-and-play steering vector that reshapes the LLM’s representation space during inference to enhance separation between truthful and hallucinated outputs. With only 4K trainable parameters (0.00005% of the model), TSV achieves +12.8% AUROC on TruthfulQA compared to prior methods, and with as few as 32 labeled examples it outperforms fully supervised SAPLMA by 6.0%.

**MIND** (Su et al., Findings of ACL 2024) is an unsupervised real-time detection framework that extracts pseudo-training data from Wikipedia, trains a simple MLP classifier on internal states, and achieves 78.76% AUC at sentence level on LLaMA-7B. The accompanying HELM benchmark provides human-annotated hallucination labels for six LLMs.

**ICR Probe** (Zhang et al., ACL 2025) shifts focus from static hidden states to the dynamic update process across layers, defining the ICR Score that quantifies the contribution of attention and feed-forward modules to hidden state updates. A lightweight MLP trained on these scores achieves AUROC scores of 0.84 on HaluEval and 0.81 on SQuAD, and maintains strong cross-dataset generalization.

**Lookback Lens** (Chuang et al., EMNLP 2024 Oral) uses only attention maps to detect contextual hallucinations. The method computes the “lookback ratio”—the proportion of attention weights attending to the input context versus newly generated tokens—and trains a linear classifier on these features. Despite its simplicity, the detector transfers across tasks and even across model sizes (e.g., trained on 7B, applied to 13B without retraining). Lookback Lens also enables classifier-guided decoding, achieving a 9.6% reduction in hallucination rates on XSum summarization.

### 4.3 Attention-Based Detection

Beyond Lookback Lens, several works have specifically analyzed attention patterns. **Attention Divergence** (ACL 2026 SRW) measures KL divergence between each attention head’s distribution and a uniform reference, then trains a logistic regression probe. On TruthfulQA, AUROC exceeds 0.89 across LLaMA-3.2-3B, Qwen3-4B, and Mistral-7B. The signal peaks at factual tokens (named entities and numbers) and is concentrated in middle layers.

**TOHA** (2025, venue unknown) interprets attention matrices as weighted graphs and computes a minimal spanning forest cost to detect hallucinated tokens. **Spectral Features** (2025, venue unknown) analyzes structural properties of attention mechanisms using eigenvalues. Both are listed in the Awesome-HalDetection repository and represent emerging directions.

### 4.4 Detection in Retrieval-Augmented Generation

RAG introduces a unique challenge: the model must faithfully ground its response in retrieved context. **RAG-HAT** (Song et al., EMNLP 2024 Industry) is a hallucination-aware tuning pipeline that achieves the best reported F1 (0.84) on the RAGTruth dataset’s response-level classification task, using a substantially larger model trained on RAGTruth.

**ReDeEP** (ICLR 2025) provides a mechanistic interpretability analysis of RAG hallucinations. It identifies that hallucinations occur when the Knowledge FFNs overemphasize parametric knowledge in the residual stream, while Copying Heads fail to effectively retain external knowledge. Based on this, ReDeEP decouples the LLM’s utilization of external context (via the External Context Score) and parametric knowledge (via the Parametric Knowledge Score) to detect hallucinations. Causal intervention experiments confirm that both attention heads and FFN modules significantly impact hallucination occurrence. The accompanying AARF mitigation strategy (Add Attention Reduce FFN) reduces hallucinations without requiring retraining.

## 5. Interpretability and Mechanistic Insights

Understanding the internal mechanisms underlying hallucination has become a vibrant research area. **DoLa** (Chuang et al., ICLR 2024) exploits the observation that factual knowledge in transformer LLMs is localized to specific layers. By contrasting logits from later (mature) layers against earlier (premature) layers, DoLa amplifies factual knowledge and achieves 12–17% absolute improvement on TruthfulQA without external retrieval or fine-tuning. The dynamic selection of the premature layer at each decoding step uses Jensen-Shannon Divergence.

**LLMs Know More Than They Show** (Orgad et al., ICLR 2025) reveals that internal representations encode truthfulness information concentrated in exact answer tokens, achieving probe AUC scores of 0.85–0.95 across datasets. However, the paper also demonstrates that truthfulness encoding is not universal: probes fail to generalize across tasks, implying multiple “skill-specific” truthfulness mechanisms. A striking finding is the discrepancy between internal encoding and external behavior: the model may encode the correct answer yet consistently generate an incorrect one. Using probes to select answers from resampled outputs improved accuracy by 30–40 points.

**On the Universal Truthfulness Hyperplane** (EMNLP 2024) investigates whether a single linear hyperplane can separate factually correct from incorrect outputs across diverse tasks. Training on a curated collection of over 40 datasets spanning 17 tasks, probes achieve ~70% cross-task generalization, with attention head outputs being better representations than layer residual activations. The study confirms that stronger models exhibit more pronounced truthfulness hyperplanes.

**ReDeEP** (ICLR 2025), described above, provides mechanistic interpretability specifically for RAG settings. **Failure by Interference** (NeurIPS 2025) proposes a “top-down mechanism decomposition” showing that even when models achieve 0% accuracy, they contain internal mechanisms that could solve the task successfully, but faulty mechanisms overshadow the sound ones. The RaSTEER method amplifies sound mechanisms, yielding up to 100% performance boosts.

**ModCirc** (He et al., ICML 2025) proposes a modular circuit vocabulary for global-level mechanistic interpretability. By identifying task-agnostic functional units, the approach enables reuse across different applications, including medical AI. **FSPO** (NeurIPS 2025) reveals that reasoning models using chain-of-thought actually hallucinate more than base models on complex factual questions, as extended generation provides more surface area for factuality drift.

## 6. Critical Assessments and Emerging Challenges

Several recent works have critically re-evaluated the assumptions underlying existing detection methods. **The Illusion of Progress** (EMNLP 2025) systematically demonstrates that ROUGE-based evaluation, the most widely used metric for hallucination detection, has alarmingly low precision (0.401) compared to human judgments. When re-evaluated with LLM-as-Judge, established detection methods show performance drops of up to 45.9% (Perplexity on Mistral/NQ-Open) and 30.4% (EigenScore). Simple length-based heuristics can rival or exceed sophisticated detection methods, exposing a fundamental flaw in current evaluation practices.

**Reasoning Models Hallucinate More** (NeurIPS 2025) confirms that chain-of-thought reasoning models, despite their improved accuracy on reasoning tasks, exhibit higher hallucination rates on complex factual questions. This finding has significant implications for the deployment of reasoning models in high-stakes domains.

**Trust Me, I’m Wrong** (Center for AI Safety, 2025) introduces the phenomenon of CHOKE (Certain Hallucinations Overriding Known Evidence)—hallucinations that occur with high certainty even when the model possesses the correct knowledge. Using token probability, probability difference, and semantic entropy, the authors find that 10–40% of hallucinations exceed the certainty threshold, and existing certainty-based mitigation methods fail to address them.

## 7. Conclusion

The 2023–2025 period has witnessed explosive growth in hallucination detection research, producing a rich ecosystem of theoretical frameworks, comprehensive benchmarks, and increasingly sophisticated detection algorithms. Theoretical results have established fundamental limits and guarantees, while empirical methods have progressed from simple consistency checks to probing internal representations, analyzing attention patterns, and leveraging mechanistic interpretability. Emerging critical evaluations underscore the need for rigorous metric validation and highlight the unique challenges posed by reasoning models. As LLMs continue to be deployed in high-stakes applications, the development of reliable, efficient, and theoretically grounded hallucination detection methods remains a pressing research priority.

### Sources

[1] Calibrated Language Models Must Hallucinate (Kalai & Vempala, STOC 2024): https://arxiv.org/abs/2311.14648

[2] FactTest: Factuality Testing in LLMs with Finite-Sample and Distribution-Free Guarantees (Nie et al., ICML 2025): https://icml.cc/virtual/2025/poster/43756

[3] (Im)possibility of Automated Hallucination Detection in Large Language Models (Karbasi et al., ICML 2025 Workshop): https://icml.cc/virtual/2025/50949

[4] HaluEval: A Large-Scale Hallucination Evaluation Benchmark (Li et al., EMNLP 2023): https://aclanthology.org/2023.emnlp-main.397

[5] FActScore: Fine-grained Atomic Evaluation of Factual Precision (Min et al., EMNLP 2023): https://aclanthology.org/2023.emnlp-main.741

[6] ANAH: Analytical Annotation of Hallucinations in Large Language Models (Ji et al., ACL 2024): https://aclanthology.org/2024.acl-long.442

[7] ANAH-v2: Scaling Analytical Hallucination Annotation (Ji et al., NeurIPS 2024): https://neurips.cc/virtual/2024/poster/95407

[8] RAGTruth: A Hallucination Corpus for Developing Trustworthy Retrieval-Augmented Language Models (Niu et al., ACL 2024): https://aclanthology.org/2024.acl-long.585

[9] FactCHD: Benchmarking Fact-Conflicting Hallucination Detection (Zhejiang University et al., IJCAI 2024): https://www.ijcai.org/proceedings/2024/687

[10] HalluLens: LLM Hallucination Benchmark (Bang et al., ACL 2025): https://aclanthology.org/2025.acl-long.1176

[11] PHANTOM: A Benchmark for Hallucination Detection in Financial Long-Context QA (Ji et al., NeurIPS 2025): https://neurips.cc/virtual/2025/poster/121830

[12] SelfCheckGPT: Zero-Resource Black-Box Hallucination Detection (Manakul et al., EMNLP 2023): https://aclanthology.org/2023.emnlp-main.557

[13] Detecting Hallucinations in Large Language Models Using Semantic Entropy (Farquhar et al., Nature 2024): https://www.nature.com/articles/s41586-024-07421-0

[14] Robust Hallucination Detection in LLMs via Adaptive Token Selection (HaMI) (Niu et al., NeurIPS 2025): https://neurips.cc/virtual/2025/poster/116745

[15] HaloScope: Harnessing Unlabeled LLM Generations for Hallucination Detection (Du et al., NeurIPS 2024): https://proceedings.neurips.cc/paper_files/paper/2024/file/ba92705991cfbbcedc26e27e833ebbae-Paper-Conference.pdf

[16] LLM-Check: Investigating Detection of Hallucinations in Large Language Models (Sriramanan et al., NeurIPS 2024): https://neurips.cc/virtual/2024/poster/95584

[17] Steer LLM Latents for Hallucination Detection (TSV) (Park et al., ICML 2025): https://icml.cc/virtual/2025/poster/45122

[18] MIND: Unsupervised Modeling of Internal States for Hallucination Detection (Su et al., Findings of ACL 2024): https://aclanthology.org/2024.findings-acl.854

[19] ICR Probe: Tracking Hidden State Dynamics for Reliable Hallucination Detection (Zhang et al., ACL 2025): https://aclanthology.org/2025.acl-long.880

[20] Lookback Lens: Detecting and Mitigating Contextual Hallucinations Using Only Attention Maps (Chuang et al., EMNLP 2024): https://aclanthology.org/2024.emnlp-main.84

[21] RAG-HAT: A Hallucination-Aware Tuning Pipeline for LLM in RAG (Song et al., EMNLP 2024 Industry): https://aclanthology.org/2024.emnlp-industry.113

[22] ReDeEP: Detecting Hallucination in Retrieval-Augmented Generation via Mechanistic Interpretability (ICLR 2025): https://iclr.cc/virtual/2025/poster/27644

[23] DoLa: Decoding by Contrasting Layers Improves Factuality (Chuang et al., ICLR 2024): https://arxiv.org/abs/2309.03883

[24] LLMs Know More Than They Show: On the Intrinsic Representation of LLM Hallucinations (Orgad et al., ICLR 2025): https://iclr.cc/virtual/2025/poster/30060

[25] On the Universal Truthfulness Hyperplane Inside LLMs (EMNLP 2024): https://aclanthology.org/2024.emnlp-main.1012

[26] Failure by Interference (Rai et al., NeurIPS 2025): https://neurips.cc/virtual/2025/poster/118673 (via LinkedIn)

[27] ModCirc: Towards Global-level Mechanistic Interpretability (He et al., ICML 2025): https://icml.cc/virtual/2025/poster/44616

[28] The Illusion of Progress: Re-evaluating Hallucination Detection in LLMs (EMNLP 2025): https://aclanthology.org/2025.emnlp-main.1761.pdf

[29] Reasoning Models Hallucinate More (FSPO, NeurIPS 2025): https://github.com/EdinburghNLP/awesome-hallucination-detection

[30] Trust Me, I’m Wrong: High-Certainty Hallucinations in LLMs (Center for AI Safety, 2025): https://arxiv.org/abs/2502.12964 (arXiv preprint, but included for completeness)

[31] MHaluBench: Meta-evaluation Benchmark for Multimodal Hallucination Detection (ACL 2024): https://github.com/zjunlp/EasyDetect
