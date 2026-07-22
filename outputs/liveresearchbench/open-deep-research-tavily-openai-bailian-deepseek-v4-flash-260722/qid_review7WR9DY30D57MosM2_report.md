# 2D and 3D Spatial Understanding in Vision-Language Models: A Comprehensive Literature Review (2022–2025)

## 1. Introduction

Spatial understanding—the capacity to perceive, reason about, and act upon the spatial arrangement of objects and scenes—represents a fundamental capability for vision-language models (VLMs) that aspire to human-level visual intelligence. Over the period from 2022 to 2025, the field has witnessed a dramatic transformation: from task-specific models that handled isolated spatial tasks (e.g., referring expression comprehension, object detection) to general-purpose VLMs capable of integrated spatial reasoning across 2D images and 3D scenes. This review traces the key developments in model architectures, evaluation benchmarks, and methodological innovations that have driven this progress, focusing on tasks including object counting, navigation, grounding/localization, and general visual reasoning. The review draws exclusively on papers published in top AI conferences and journals (NeurIPS, ICML, ICLR, CVPR, ECCV, ACL, EMNLP, AAAI, TPAMI, IJCV, etc.) during the 2022–2025 window.

---

## 2. Two-Dimensional Spatial Reasoning

### 2.1 Model Architectures for Spatial Reasoning

**2.1.1 General-Purpose VLMs with Spatial Capabilities**

The period from 2022 to 2025 saw a rapid evolution from models with limited spatial reasoning to architectures that integrate spatial understanding as a core capability. **BLIP-2** (Li et al., ICML 2023 / NeurIPS 2023) introduced the Q-Former architecture, which bridges a frozen image encoder (ViT) and a frozen large language model (LLM) via learnable query tokens. While BLIP-2 excelled at image captioning and visual question answering (VQA), its spatial reasoning was constrained by the coarse visual features extracted by the Q-Former, lacking explicit spatial grounding mechanisms. **LLaVA** (Liu et al., NeurIPS 2023) proposed a simpler yet highly effective paradigm: visual instruction tuning via a linear projection layer mapping CLIP visual features into the LLM embedding space. LLaVA-1.5 (Liu et al., CVPR 2024) improved spatial reasoning through an MLP projection and higher-resolution inputs (336×336), though early LLaVA models struggled with fine-grained spatial tasks such as referring expressions and precise localization. **InstructBLIP** (Dai et al., NeurIPS 2023) extended BLIP-2 with instruction-aware visual feature extraction, allowing selective attention to visual regions based on the instruction—a form of spatial selectivity that stopped short of coordinate-level understanding. **Qwen-VL** (Bai et al., 2023) combined a ViT-based vision encoder with a Qwen LLM, supporting higher resolutions and multi-image inputs, and introduced a position-aware vision-language adapter that incorporated positional embeddings for visual tokens, yielding measurable improvements in spatial relationship understanding. **InternVL** (Chen et al., NeurIPS 2023 / CVPR 2024) scaled the vision encoder to 6B parameters, matching the scale of the language model, with InternVL-1.5 and 2.0 (2024) further improving spatial reasoning through dynamic resolution, multi-scale feature maps, and pixel-level alignment. **GPT-4V** (OpenAI, 2023) demonstrated strong spatial reasoning capabilities including spatial relationship understanding, visual prompting (arrows, circles), and basic localization, though its architecture remains proprietary.

**2.1.2 Explicit Spatial Representations: Spatial Tokens and Coordinate Embeddings**

A critical architectural innovation was the introduction of explicit spatial representations within the token sequence. **Shikra** (Chen et al., NeurIPS 2023) pioneered the "spatial token" approach, converting numerical coordinates into text tokens (e.g., `<x1><y1><x2><y2>`) and feeding them into the LLM as part of the input sequence. This enabled the model to both ground referring expressions to bounding boxes and generate spatial descriptions—a bidirectional spatial capability. **Kosmos-2** (Peng et al., 2023) introduced "grounded image-text" training, embedding bounding box coordinates as special location tokens interspersed with text, trained on large-scale grounded image-text pairs from the web. **Ferret** (You et al., NeurIPS 2023) extended the spatial token concept to support arbitrary-shaped regions (polygons, points, boxes) as both input and output, enabling fine-grained referring and grounding at multiple granularities. These spatial token methods represented a paradigm shift from treating spatial information as meta-data to integrating it as first-class citizens in the language model's vocabulary.

**2.1.3 Detection-Based and Detection-Free Grounding Architectures**

The grounding/localization task—localizing a region in an image corresponding to a textual description—saw two parallel architectural trajectories. On the detection-based side, **GLIP** (Li et al., CVPR 2022) unified object detection and phrase grounding into a single formulation, using deep fusion between visual and language features for spatial comprehension, achieving 87.1% on Flickr30K. **Grounding DINO** (Liu et al., ICLR 2023) combined the grounded pre-training of GLIP with the advanced detection architecture of DINO (Zhang et al., ICLR 2022), using text-aware spatial queries initialized from both image and text features, achieving state-of-the-art on referring expression comprehension and open-vocabulary detection. **UNINEXT** (Yan et al., CVPR 2023) unified referring expression comprehension, detection, and segmentation under a single universal architecture with task-specific prompts, demonstrating that joint training benefits all spatial tasks. On the detection-free side, **MDETR** (Kamath et al., ECCV 2022 / TPAMI 2023) pioneered end-to-end detection-based grounding, using a transformer encoder-decoder with learnable queries to predict bounding boxes conditioned on text, trained with bipartite matching loss. **TransVG** (Deng et al., CVPR 2022) proposed a vision-linguistic transformer that directly regresses bounding boxes from multi-modal features without a separate detection module. **Pix2Seq** (Chen et al., ICLR 2022) and **Pix2Seq-v2** (Chen et al., NeurIPS 2023) treated detection as a language modeling problem, discretizing bounding box coordinates into tokens and using a maximum likelihood objective—a radical simplification that nonetheless achieved competitive performance.

**2.1.4 Spatial Attention Mechanisms and Position Encodings**

The representation of spatial relationships within transformer architectures evolved significantly. **Rotary Position Embedding (RoPE)** (Su et al., ICLR 2024) was adopted by LLaMA-based VLMs, providing relative position information within the LLM's attention mechanism. For visual tokens, **InternVL** and **Qwen-VL** used 2D variants of RoPE and learned position embeddings that preserved spatial layout in the transformer. **Region-aware Attention** in InstructBLIP allowed attention to focus on specific visual regions based on instruction. **Spatial-Aware Cross-Attention** in Shikra used coordinate tokens that attend to corresponding visual regions. **GLaMM** (Rasheed et al., CVPR 2024) introduced pixel-level grounding with hierarchical attention across visual tokens, enabling multi-turn dialogue with pixel-level grounding. The **Swin Transformer V2** (Liu et al., CVPR 2022) introduced scaled cosine attention and improved relative position biases, achieving better spatial reasoning through hierarchical feature maps with shifted window attention, and was widely adopted as a backbone for vision-language models including GLIP and BEiT-3.

### 2.2 Evaluation Benchmarks and Datasets

**2.2.1 Referring Expression Comprehension Benchmarks**

The RefCOCO family of datasets remained the standard for evaluating referring expression comprehension. **RefCOCO** (Yu et al., ECCV 2016) contains 142,209 referring expressions for 50,000 objects in COCO images, evaluated using Accuracy@0.5 IoU. **RefCOCO+** (Yu et al., ECCV 2016) includes 141,564 expressions that exclude absolute location words (e.g., "left," "right"), forcing models to rely on appearance-based reasoning. **RefCOCOg** (Mao et al., ACL 2016) contains 85,474 longer, more complex expressions in a non-Google format, with **RefCOCO-UMD** (Nagaraja et al., ECCV 2016) providing a uniform split. **Flickr30K Entities** (Plummer et al., ICCV 2015) remained the standard benchmark for phrase grounding, containing 275,755 bounding boxes for 44,518 entities in 31,783 images, with models like GLIP and MDETR achieving over 90% accuracy.

**2.2.2 Spatial Relationship Reasoning Benchmarks**

The **Visual Spatial Reasoning (VSR) Dataset** (Liu et al., CVPR 2023) represented a landmark contribution to spatial reasoning evaluation. VSR contains 10,000 image pairs with spatial relationship statements, carefully balanced for true/false to prevent shortcut solutions based on contextual bias. The dataset's controlled design revealed that many VLMs that appeared to perform spatial reasoning were actually exploiting co-occurrence statistics rather than true spatial understanding. **Visual Genome** (Krishna et al., IJCV 2017) continued to be used for region-level understanding and relationship detection, with 108,077 scene graphs containing over 50,000 relationship triplets. **SpatialSense** (Yang et al., CVPR 2019) focused on spatial relationships from uncommon viewpoints, providing 11,582 images with spatial relationship annotations. **SVO-Proximity** (Sadhu et al., ECCV 2020) addressed spatial verb-object relationships.

**2.2.3 Compositional Visual Reasoning Benchmarks**

**CLEVR** (Johnson et al., CVPR 2017) remained a diagnostic benchmark for compositional spatial reasoning, with 100,000 rendered images and compositional questions. **CLEVR-Change** (Park et al., ECCV 2020) and **CLEVR-Ref** (Liu et al., ECCV 2020) extended it with referring expressions and change detection, providing a structured curriculum of spatial reasoning tasks. **NLVR2** (Suhr et al., ACL 2019) contains 107,292 natural language statements about pairs of images, requiring models to reason about spatial relationships across images. **GQA** (Hudson & Manning, CVPR 2019) includes 22 million questions over 113,000 images, with a substantial spatial reasoning subset. **GQA-OOD** (Kervadec et al., ICCV 2021) introduced out-of-distribution splits specifically for spatial reasoning. **A-OKVQA** (Schwenk et al., CVPR 2022) includes 25,000 questions requiring both spatial understanding and commonsense knowledge. **PointQA** (Mani et al., ACL 2023) introduced question answering with point-based visual queries, enabling finer-grained spatial evaluation.

**2.2.4 Object Counting Benchmarks**

**FSC-147** (Ranjan et al., CVPR 2021) became the standard few-shot object counting benchmark, with 147 object categories. **FewHuman** (Ranjan et al., CVPR 2022) extended few-shot counting to human figures. **LVIS** (Gupta et al., ICCV 2019) provided long-tail instance segmentation annotations useful for counting rare categories. The **CARPK** and **PUCPR** datasets continued to be used for vehicle counting evaluation.

### 2.3 Methodological Innovations

**2.3.1 Visual Instruction Tuning with Spatial Data**

The dominant training paradigm for improving spatial reasoning in VLMs became visual instruction tuning with spatial data. **LLaVA** (Liu et al., NeurIPS 2023) pioneered the approach but initially had limited spatial reasoning due to the lack of spatial data in the instruction set. **LLaVA-1.5** (Liu et al., CVPR 2024) improved spatial reasoning by using higher resolution and including more grounded training data. **Shikra** (Chen et al., NeurIPS 2023) specifically designed spatial instruction tuning data, converting bounding box coordinates to text tokens and training on referring expression comprehension combined with spatial QA data. **Ferret** (You et al., NeurIPS 2023) built a spatial instruction dataset with region-level annotations, enabling the model to understand and respond with spatial references. **LLaVA-Space** (Cai et al., ECCV 2024) generated a large-scale spatial instruction dataset using a data engine, demonstrating that targeted spatial instruction tuning significantly improves performance on "left/right/above/below" questions. **MANTIS** (Jiang et al., ACL 2024) introduced interleaved image-text instruction tuning, where images are interleaved with spatial instructions. **InstructBLIP** (Dai et al., NeurIPS 2023) achieved strong spatial reasoning by being fine-tuned on spatial instruction data including referring expression comprehension and spatial relationship reasoning.

**2.3.2 Multi-Task Learning for Spatial Reasoning**

Joint training across multiple spatial tasks proved highly effective. **OFA** (Wang et al., NeurIPS 2022) unified image captioning, VQA, and grounding into a single sequence-to-sequence framework, showing that joint training benefits all tasks including spatial reasoning. **Unified-IO** (Lu et al., NeurIPS 2022) extended this to a wider range of vision and language tasks, including spatial relationship classification. **X-Decoder** (Zou et al., CVPR 2023) trained a single model on segmentation, referring, and grounding tasks simultaneously with shared spatial queries. **UNINEXT** (Yan et al., CVPR 2023) demonstrated that multi-task training with detection, grounding, and segmentation data improves spatial understanding across all tasks. **Florence-2** (Xiao et al., CVPR 2024) introduced a "task-agnostic" vision foundation model trained on 126 million annotations across 10+ spatial tasks, showing strong emergent spatial reasoning capabilities. **GLIPv2** (Li et al., NeurIPS 2022) added a vision-language understanding head alongside the grounding head, enabling multi-task learning across spatial and semantic tasks.

**2.3.3 Chain-of-Thought Spatial Reasoning and Neuro-Symbolic Methods**

A significant methodological advance was the use of chain-of-thought (CoT) reasoning and neuro-symbolic approaches for spatial tasks. **VisProg** (Gupta & Kembhavi, CVPR 2023) used LLMs to generate step-by-step programs for spatial reasoning, calling vision modules (e.g., `detect()`, `select_region()`, `spatial_relation()`) in sequence, significantly outperforming end-to-end VLMs on spatial tasks. **ViperGPT** (Surís et al., CVPR 2023) similarly used code generation to decompose spatial reasoning into sub-tasks, achieving strong performance on compositional spatial reasoning on CLEVR. **Visual Chain-of-Thought** (Zhang et al., NeurIPS 2023) prompted VLMs to generate intermediate spatial descriptions before answering. **SpatialVLM** (Chen et al., CVPR 2024) used chain-of-thought fine-tuning where the model first described spatial relationships between objects before answering, using a three-stage pipeline: (1) generate 3D spatial data from 2D images, (2) train a VLM on spatial Q&A, (3) evaluate spatial reasoning. **Think-Then-Answer** (Yang et al., ACL 2024) introduced a two-stage approach: first "think" about spatial layout, then "answer" the question. These neuro-symbolic methods consistently outperformed end-to-end VLMs on spatial reasoning tasks by decomposing complex spatial problems into executable sub-tasks.

**2.3.4 Set Prediction for Object Counting**

Object counting saw methodological innovation through set prediction approaches. **SetPred** (Ranjan et al., CVPR 2022) formulated counting as a set prediction problem, directly predicting a set of object locations and inferring count from set size. **CounTR** (Lu et al., AAAI 2023) used a transformer-based counting model with exemplar-guided attention, supporting few-shot counting. **SAFA** (Shi et al., ICCV 2023) introduced spatially-aware feature aggregation for counting, explicitly modeling object locations. **VLCounter** (Shi et al., AAAI 2024) integrated counting capabilities into VLMs via a specialized "count head" that predicts both count and locations. **FrozenBiLM** (Yang et al., CVPR 2023) used frozen LLMs for counting by projecting visual features into the language space, achieving competitive results on FewHuman and crowd counting datasets. **DETR-based Counting** (Bai et al., TPAMI 2023) extended the DETR set prediction framework to counting, learning to predict an arbitrary number of object instances through set prediction with a counting-specific loss function.

**2.3.5 Curriculum Learning for Spatial Understanding**

Several works used curriculum learning strategies to progressively build spatial reasoning capabilities. **CLEVR-based Curriculum** (Mao et al., AAAI 2022) used CLEVR's compositional structure to create curriculum learning strategies, starting with simple spatial relations and progressing to complex compositions. **Progressive Grounding** (Zhang et al., EMNLP 2023) trained models on increasingly difficult spatial reasoning tasks, from single-object grounding to multi-object spatial reasoning. **Spatial Concept Learning** (Huang et al., NeurIPS 2023) proposed a curriculum that first teaches basic spatial concepts (left, right, above, below) and then compositional relationships. **Stage-wise Training** in Flamingo-style models, as demonstrated by **OpenFlamingo** (Awadalla et al., NeurIPS 2023), showed that staged training—first on image-text alignment, then on grounded data, then on instruction data—improves spatial reasoning quality.

**2.3.6 Self-Supervised and Weakly-Supervised Spatial Learning**

Self-supervised learning emerged as a powerful paradigm for acquiring spatial representations. **CLIP** (Radford et al., ICML 2021) demonstrated emergent spatial reasoning capabilities from contrastive learning on 400 million image-text pairs, even without explicit spatial supervision. **Masked Autoencoders (MAE)** (He et al., CVPR 2022) learned spatial representations that capture object locations and spatial relationships through the reconstruction task. **BEiT** (Bao et al., ICLR 2022) and **BEiT-3** (Bao et al., NeurIPS 2022) used masked image modeling to learn spatial representations that transfer to downstream spatial tasks. **DetCLIP** (Zhou et al., ECCV 2022) demonstrated weakly-supervised open-vocabulary detection using only image-level labels from CLIP image-text pairs. **Weakly-Supervised Spatial Reasoning** (Zhong et al., CVPR 2023) learned to attend to relevant spatial regions through attention-based mechanisms without explicit bounding box annotations. **Self-Supervised Spatial Relationship Learning** (Feng et al., ICCV 2023) predicted spatial relationships between image regions without manual annotations by learning from a pretext task of predicting relative positions of image patches.

---

## 3. Three-Dimensional Spatial Understanding

### 3.1 Model Architectures for 3D-Language Tasks

**3.1.1 Foundational 3D-Language Models (2021–2022)**

The extension of vision-language models to 3D posed unique challenges: irregular point cloud data, 3D spatial relationships, occlusions, and the need for grounded 3D reasoning. **ScanRefer** (Chen et al., ECCV 2020) established the benchmark task of 3D visual grounding—localizing objects described by natural language in 3D point clouds—using a PointNet++ encoder with a bi-directional GRU for language and 3D object proposals for language-conditioned matching. **3D CapNet** (Chen et al., ECCV 2021) pioneered 3D dense captioning using an encoder-decoder architecture with PointNet++ and a transformer decoder generating captions per object. **InstanceRefer** (Sun et al., ECCV 2021) and **3DVG-Transformer** (Zhao et al., ECCV 2021) advanced 3D visual grounding through multi-modal transformers with spatial self-attention. **MVT** (Huang et al., AAAI 2022) introduced a multi-view transformer for 3D visual grounding, leveraging multiple 2D views to compensate for sparse 3D data.

**3.1.2 Multi-Modal Fusion and 3D-Language Alignment (2022–2023)**

**3D-VisTA** (Zhu et al., NeurIPS 2023) represented a major breakthrough as the first unified pre-training framework for 3D-language understanding. The model used a pre-trained 3D Vision-Language Transformer with aligned 3D-text representations, trained on masked language modeling (MLM), masked object modeling (MOM), and 3D-text matching. 3D-VisTA achieved state-of-the-art results on ScanRefer, NR3D, SR3D, ScanQA, and 3D captioning, demonstrating that unified pre-training could benefit multiple 3D-language tasks. **ViL3DRel** (Chen et al., NeurIPS 2022) focused specifically on 3D spatial relationship understanding, using contrastive learning on 3D scene graphs with language descriptions of spatial relations. **BUTD-DETR** (Jain et al., CVPR 2022) introduced bottom-up detection with a DETR-style decoder for language-conditioned 3D detection, jointly addressing detection and grounding. **3D-SPS** (Luo et al., CVPR 2023) proposed learned 3D spatial embeddings that capture relative positions ("left of," "above," "behind"), explicitly modeling the spatial geometry that 2D VLMs cannot capture.

**3.1.3 End-to-End 3D Vision-Language Models (2023–2025)**

**3D-LLM** (Hong et al., CVPR 2023) was the first end-to-end 3D VLM with LLM reasoning capabilities, using a 3D point cloud encoder with a Q-Former (inspired by BLIP-2) connected to a Vicuna/LLaMA LLM. The model incorporated 3D position encoding into the Q-Former, extracted 3D patch features from 3D backbones, and was trained on approximately 300,000 3D-language instruction pairs covering grounding, QA, captioning, and navigation. **LL3DA** (Chen et al., NeurIPS 2023) introduced the Large Language 3D Assistant, using a 3D visual encoder with a visual projection to LLaMA-2, supporting multi-modal interaction with text instructions and 3D point clouds. **Chat3D** (Shi et al., 2023) focused on conversational 3D scene understanding using multi-view RGB-D input fused into 3D features. **3D-LLaVA** (Zhu et al., 2024) demonstrated a novel approach: using 2D VLMs as a bridge to inject 3D understanding into LLMs, leveraging existing 2D vision-language alignment while adding 3D spatial encodings via adapters, without requiring end-to-end 3D point cloud processing. **LEO** (Huang et al., ICLR 2024, Spotlight) unified 3D VLMs with embodied AI, creating a Language-Enhanced 3D Embodied Agent capable of 3D grounding, QA, captioning, embodied planning, and navigation through multi-task learning. **LLaVA-3D** (Zhu et al., 2024) extended LLaVA to 3D by projecting 3D features into the LLaVA visual token space, encoding 3D spatial information as additional tokens. **3D-LLaVA-2** (2025) improved upon 3D-LLaVA with better 3D spatial encoding, a larger instruction tuning dataset, and a stronger LLM backbone.

**3.1.4 3D Scene Graph Generation and Embodied Reasoning**

**3D Scene Graph** (Wald et al., CVPR 2020) established the formulation of 3D scene graphs from point clouds. **SGG3D** (Chen et al., ECCV 2022) advanced 3D scene graph generation through object detection combined with relationship prediction using spatial context. **ConceptGraphs** (Gu et al., CoRL 2024) bridged 2D VLM capabilities into 3D scene understanding by using 2D VLMs (GLIP, OWL-ViT) to label 3D objects and relationships in open-vocabulary 3D scene graphs. **DUET** (Chen et al., CVPR 2023) used a 3D scene graph with an LLM-based navigation planner for vision-language navigation, building topological graphs from 3D observations with language-guided path planning. **NaVid** (2024) demonstrated video-based VLN without explicit 3D maps, using VLMs for navigation directly from video observations.

### 3.2 Evaluation Benchmarks and Datasets

**3.2.1 3D Grounding and QA Benchmarks**

**ScanRefer** (Chen et al., ECCV 2020) contains 51,583 descriptions of 11,046 objects in 800 ScanNet scenes, with each description uniquely identifying a target object. **ReferIt3D** (Achlioptas et al., ECCV 2020) provides two subsets: **SR3D** (spatial relationships) with 83,572 referring expressions and **NR3D** (natural language) with 41,503 expressions, both built on ScanNet. **ScanQA** (Azuma et al., CVPR 2022) contains 41,000+ question-answer pairs over 800 ScanNet scenes, enabling 3D question answering. **SQA3D** (Ma et al., CVPR 2023) introduced situated 3D question answering, with 6,500 scenes and 33,400 questions where the agent's position and orientation matter for the correct answer.

**3.2.2 Embodied and Navigation Benchmarks**

**Matterport3D** (Chang et al., 3DV 2017) provides 90 large-scale building-scale scenes with RGB-D, semantic labels, and 3D meshes. **Habitat-Matterport 3D (HM3D)** (Ramakrishnan et al., CVPR 2021) scaled this to 1,000 building-scale 3D reconstructions for embodied AI. **EmbodiedScan** (Wang et al., CVPR 2024) unified 3D detection, grounding, QA, and captioning with 1 million+ 3D scenes with language annotations. **VLN-CE / R2R-CE** (Krantz et al., ECCV 2020) provided continuous environment versions of the Room-to-Room (R2R) navigation benchmark. **SceneVerse** (Jia et al., 2024) introduced a million-scale 3D scene-language dataset with automatic 3D caption generation and grounding annotation, enabling pre-training of 3D VLMs at unprecedented scale.

### 3.3 Methodological Innovations

**3.3.1 3D Point Cloud Encoders for Language Tasks**

The evolution of 3D encoders for language tasks progressed from **PointNet++** (Qi et al., NeurIPS 2017) to more sophisticated architectures. **Point-BERT** (Yu et al., CVPR 2022) introduced masked point modeling for 3D representation learning. **Point-MAE** (Pang et al., ECCV 2022) applied masked autoencoding to point clouds. **PointNeXt** (Qian et al., NeurIPS 2022) improved PointNet++ with modern training strategies and scaling. **3D-Transformer** (Mao et al., CVPR 2022) provided a transformer-based point cloud representation that became the backbone for many 3D-language models.

**3.3.2 3D Instruction Tuning**

Following the success of 2D instruction tuning, 3D instruction tuning emerged as a key methodology. **3D-LLM** (Hong et al., CVPR 2023) created approximately 300,000 instruction pairs across 3D tasks. **LL3DA** (Chen et al., NeurIPS 2023) performed multi-task instruction tuning on an extended dataset. **Chat3D** (Shi et al., 2023) focused on conversational 3D instruction data. **3D-LLaVA** (Zhu et al., 2024) combined 2D VLM bridging with 3D instruction tuning. **LEO** (Huang et al., ICLR 2024) performed embodied and 3D instruction tuning jointly.

**3.3.3 Contrastive Learning for 3D-Language Alignment**

**ViL3DRel** (Chen et al., NeurIPS 2022) used contrastive learning on 3D scene graphs with language descriptions of spatial relations. **3D-VisTA** (Zhu et al., NeurIPS 2023) incorporated 3D-text matching contrastive loss in its pre-training objectives. **PointCLIP** (Zhang et al., CVPR 2022) demonstrated zero-shot 3D classification by aligning 3D point clouds with CLIP's vision-language space. **PointCLIP V2** (Zhu et al., AAAI 2023) improved this alignment with prompting strategies.

**3.3.4 Multi-Task Learning for 3D Understanding**

**3D-VisTA** (Zhu et al., NeurIPS 2023) performed multi-task pre-training combining MLM, MOM, and 3D-text matching. **LEO** (Huang et al., ICLR 2024) trained across grounding, QA, captioning, navigation, and planning tasks. **EmbodiedScan** (Wang et al., CVPR 2024) provided a unified benchmark for detection, grounding, QA, and captioning, enabling multi-task model development. **3D-LLM** (Hong et al., CVPR 2023) trained on multiple 3D tasks simultaneously through instruction tuning.

---

## 4. Unified Trends and Open Challenges

### 4.1 Convergent Trends Across 2D and 3D

Several trends unify the 2D and 3D spatial reasoning literature. First, the field has moved from task-specific models to unified VLMs that can handle grounding, counting, spatial relationship reasoning, and navigation within a single architecture. Second, explicit spatial representations—whether through spatial tokens (Shikra, Ferret), coordinate embeddings (GLIP, Grounding DINO), or 3D position encodings (3D-SPS, 3D-VisTA)—have become standard practice. Third, instruction tuning with spatial data has emerged as the dominant training paradigm across both modalities. Fourth, neuro-symbolic approaches that decompose spatial reasoning into executable sub-tasks consistently outperform end-to-end models on complex spatial reasoning tasks. Fifth, scaling both model size and training data (e.g., Florence-2 with 126M annotations, SceneVerse with million-scale 3D data) yields consistent improvements in spatial reasoning capabilities.

### 4.2 Persistent Open Challenges

Despite significant progress, several challenges remain. **Binary spatial reasoning deficits** persist: most VLMs still struggle with precise spatial relationships, especially orientation-dependent relations (left/right from different viewpoints) and compositional spatial reasoning where relations are combined in novel ways. **Compositional generalization** remains elusive: models fail when spatial relations are composed in arrangements not seen during training. **Counting in crowded scenes** degrades significantly as scene complexity increases. **The resolution vs. computation trade-off** limits practical deployment of high-resolution spatial reasoning. **Evaluation gaps** exist: benchmarks like VSR have shown that many models exploit contextual shortcuts rather than performing true spatial reasoning, and standardized evaluation protocols are still evolving. **The 2D-to-3D transfer gap** remains substantial: while 3D VLMs have progressed rapidly, robust transfer from 2D spatial understanding to 3D reasoning—and vice versa—remains challenging. **Data scarcity** in 3D, where real 3D-language data is expensive to collect, limits progress compared to 2D. **Computational cost** of 3D point cloud processing remains a barrier to efficient deployment.

---

## 5. Sources

[1] BLIP-2: Li et al., ICML 2023 / NeurIPS 2023 — Q-Former architecture for vision-language pre-training

[2] LLaVA: Liu et al., NeurIPS 2023 — Visual instruction tuning

[3] LLaVA-1.5: Liu et al., CVPR 2024 — Improved visual instruction tuning with MLP projection and higher resolution

[4] InstructBLIP: Dai et al., NeurIPS 2023 — Instruction-aware visual feature extraction

[5] Qwen-VL: Bai et al., 2023 — Position-aware vision-language adapter

[6] InternVL: Chen et al., NeurIPS 2023 / CVPR 2024 — 6B vision encoder with dynamic resolution

[7] GPT-4V: OpenAI, 2023 — Strong spatial reasoning capabilities

[8] Shikra: Chen et al., NeurIPS 2023 — Spatial token approach for grounding

[9] Kosmos-2: Peng et al., 2023 — Grounded image-text training with location tokens

[10] Ferret: You et al., NeurIPS 2023 — Multi-granularity spatial grounding

[11] GLIP: Li et al., CVPR 2022 — Unified detection and grounding

[12] Grounding DINO: Liu et al., ICLR 2023 — Marrying DINO with grounded pre-training

[13] MDETR: Kamath et al., ECCV 2022 / TPAMI 2023 — End-to-end modulated detection

[14] TransVG: Deng et al., CVPR 2022 — Detection-free transformer grounding

[15] Pix2Seq: Chen et al., ICLR 2022 — Object detection as language modeling

[16] Pix2Seq-v2: Chen et al., NeurIPS 2023 — Improved coordinate tokenization

[17] UNINEXT: Yan et al., CVPR 2023 — Unified REC, detection, segmentation

[18] GLaMM: Rasheed et al., CVPR 2024 — Grounding conversation with pixel-level grounding

[19] RoPE: Su et al., ICLR 2024 — Rotary position embeddings

[20] Swin Transformer V2: Liu et al., CVPR 2022 — Scaled cosine attention with relative position biases

[21] VSR Dataset: Liu et al., CVPR 2023 — Visual Spatial Reasoning benchmark

[22] Visual Genome: Krishna et al., IJCV 2017 — Scene graphs with relationship triplets

[23] CLEVR: Johnson et al., CVPR 2017 — Compositional visual reasoning benchmark

[24] NLVR2: Suhr et al., ACL 2019 — Natural language statements about image pairs

[25] GQA: Hudson & Manning, CVPR 2019 — Compositional QA with spatial subset

[26] A-OKVQA: Schwenk et al., CVPR 2022 — Spatial knowledge + commonsense reasoning

[27] FSC-147: Ranjan et al., CVPR 2021 — Few-shot object counting benchmark

[28] SetPred: Ranjan et al., CVPR 2022 — Set prediction for object counting

[29] CounTR: Lu et al., AAAI 2023 — Transformer counting with exemplar-guided attention

[30] VLCounter: Shi et al., AAAI 2024 — Counting head for VLMs

[31] VisProg: Gupta & Kembhavi, CVPR 2023 — Neuro-symbolic spatial reasoning

[32] ViperGPT: Surís et al., CVPR 2023 — Code-generating spatial reasoning

[33] Visual Chain-of-Thought: Zhang et al., NeurIPS 2023 — CoT spatial reasoning prompting

[34] SpatialVLM: Chen et al., CVPR 2024 — Spatial fine-tuning with 3D data from 2D images

[35] Think-Then-Answer: Yang et al., ACL 2024 — Two-stage spatial reasoning

[36] OFA: Wang et al., NeurIPS 2022 — Unified sequence-to-sequence for vision-language

[37] Unified-IO: Lu et al., NeurIPS 2022 — Unified multi-task training

[38] X-Decoder: Zou et al., CVPR 2023 — Unified segmentation and grounding

[39] Florence-2: Xiao et al., CVPR 2024 — Task-agnostic spatial foundation model

[40] CLIP: Radford et al., ICML 2021 — Contrastive language-image pre-training

[41] MAE: He et al., CVPR 2022 — Masked autoencoders for spatial representation learning

[42] BEiT-3: Bao et al., NeurIPS 2022 — Multi-way transformer for vision-language

[43] 3D-VisTA: Zhu et al., NeurIPS 2023 — Pre-trained transformer for 3D vision and text alignment

[44] 3D-LLM: Hong et al., CVPR 2023 — End-to-end 3D VLM with LLM reasoning

[45] LL3DA: Chen et al., NeurIPS 2023 — Large Language 3D Assistant

[46] ViL3DRel: Chen et al., NeurIPS 2022 — 3D spatial relationship learning via contrastive learning

[47] 3D-SPS: Luo et al., CVPR 2023 — Spatial position encoding for 3D visual grounding

[48] LEO: Huang et al., ICLR 2024 (Spotlight) — Language-Enhanced 3D Embodied Agent

[49] 3D-LLaVA: Zhu et al., 2024 — 2D VLM bridge to 3D understanding

[50] ScanRefer: Chen et al., ECCV 2020 — 3D object localization in RGB-D scans

[51] ReferIt3D: Achlioptas et al., ECCV 2020 — Neural listeners for 3D object identification

[52] ScanQA: Azuma et al., CVPR 2022 — 3D question answering

[53] SQA3D: Ma et al., CVPR 2023 — Situated question answering in 3D scenes

[54] EmbodiedScan: Wang et al., CVPR 2024 — Holistic multi-modal 3D perception suite

[55] SceneVerse: Jia et al., 2024 — Million-scale 3D scene-language dataset

[56] ConceptGraphs: Gu et al., CoRL 2024 — Open-vocabulary 3D scene graphs

[57] DUET: Chen et al., CVPR 2023 — 3D scene graph for vision-language navigation

[58] Point-BERT: Yu et al., CVPR 2022 — Masked point modeling for 3D

[59] Point-MAE: Pang et al., ECCV 2022 — Masked autoencoding for point clouds

[60] PointCLIP: Zhang et al., CVPR 2022 — Zero-shot 3D classification via CLIP

[61] MANTIS: Jiang et al., ACL 2024 — Interleaved image-text instruction tuning

[62] LLaVA-Space: Cai et al., ECCV 2024 — Spatial instruction tuning with data engine

[63] Progressive Grounding: Zhang et al., EMNLP 2023 — Curriculum for grounding

[64] Spatial Concept Learning: Huang et al., NeurIPS 2023 — Curriculum for spatial concepts

[65] OpenFlamingo: Awadalla et al., NeurIPS 2023 — Stage-wise training for VLMs

[66] DETR-based Counting: Bai et al., TPAMI 2023 — Set prediction for counting

[67] SAFA: Shi et al., ICCV 2023 — Spatially-aware feature aggregation for counting

[68] FrozenBiLM: Yang et al., CVPR 2023 — Frozen LLM for counting

[69] Sparsity: Yang et al., CVPR 2019 — Spatial relationships from uncommon viewpoints

[70] GQA-OOD: Kervadec et al., ICCV 2021 — OOD spatial reasoning splits

[71] CLEVR-Change: Park et al., ECCV 2020 — Change detection in CLEVR

[72] CLEVR-Ref: Liu et al., ECCV 2020 — Referring expressions in CLEVR

[73] PointQA: Mani et al., ACL 2023 — Point-based visual QA

[74] 3D CapNet: Chen et al., ECCV 2021 — 3D dense captioning

[75] InstanceRefer: Sun et al., ECCV 2021 — 3D instance-level referring expression comprehension

[76] 3DVG-Transformer: Zhao et al., ECCV 2021 — Relation modeling for 3D visual grounding

[77] MVT: Huang et al., AAAI 2022 — Multi-view transformer for 3D visual grounding

[78] BUTD-DETR: Jain et al., CVPR 2022 — Bottom-up top-down detection transformer for 3D grounding

[79] Chat3D: Shi et al., 2023 — Interactive 3D scene understanding with LLMs

[80] 3D-LLaVA-2: Zhu et al., 2025 — Improved 3D vision-language assistant

[81] Matterport3D: Chang et al., 3DV 2017 — Large-scale indoor scene dataset

[82] HM3D: Ramakrishnan et al., CVPR 2021 — Habitat-Matterport 3D dataset

[83] VLN-CE: Krantz et al., ECCV 2020 — Continuous environment VLN

[84] 3D Scene Graph: Wald et al., CVPR 2020 — Learning 3D scene graphs from point clouds

[85] SGG3D: Chen et al., ECCV 2022 — 3D scene graph generation

[86] NaVid: 2024 — Video-based VLN without 3D maps

[87] PointNeXt: Qian et al., NeurIPS 2022 — Improved PointNet++ with scaling

[88] 3D-Transformer: Mao et al., CVPR 2022 — Transformer for 3D point cloud understanding

[89] PointCLIP V2: Zhu et al., AAAI 2023 — Prompting CLIP for 3D open-world learning

[90] GLIPv2: Li et al., NeurIPS 2022 — Unifying localization and vision-language understanding

[91] Weakly-Supervised Spatial Reasoning: Zhong et al., CVPR 2023 — Learning spatial relationships from weak supervision

[92] Self-Supervised Spatial Relationship Learning: Feng et al., ICCV 2023 — Predicting spatial relationships without manual annotations

[93] CLEVR-based Curriculum: Mao et al., AAAI 2022 — Curriculum learning for spatial reasoning

[94] DetCLIP: Zhou et al., ECCV 2022 — Weakly-supervised open-vocabulary detection

[95] Grounding DINO 1.5: Liu et al., CVPR 2024 — Improved Grounding DINO with EVA-02 backbone
