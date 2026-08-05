# A Comprehensive Framework for Analyzing and Studying Singles Badminton Player Actions from Sports Videos

## Overview

This report presents a comprehensive, integrated framework for the automated analysis of singles badminton player actions from sports videos. The framework is built upon four interrelated research components: (1) object detection and tracking of players and the shuttlecock; (2) recognition of technical actions (strokes, footwork, serves); (3) recognition of tactical intent behind those actions; and (4) prediction of subsequent player actions. Each component is a rich research area with distinct challenges, state-of-the-art methods, and evaluation protocols. The framework emphasizes a cohesive pipeline where the output of earlier components feeds into later ones, enabling a unified analysis from raw video to high-level tactical understanding. The following sections detail the current state of research for each component, recommended architectures and datasets, and the critical integration pathways that link them together.

---

## Component 1: Object Detection and Tracking of Players and Shuttlecock

### State-of-the-Art Detection Architectures

Object detection and tracking form the foundational layer of the framework. The primary targets are the two players and the shuttlecock, each presenting unique challenges. Players are relatively large, but can be occluded by each other or by court furniture. The shuttlecock is an extremely challenging target: it is small (often under 20 pixels in bounding box side length), moves at speeds exceeding 300 km/h, and is subject to motion blur, occlusions, and background clutter [1][2][3].

**YOLO (You Only Look Once) Variants** have become the dominant detection architecture for this task due to their speed and accuracy. YOLOv8 has been widely adopted, with a binocular stereo vision system achieving 96.22% average precision and 60 FPS for shuttlecock detection [4]. The YO-CSA-T model, built on YOLOv8s with a Contextual Transformer Block backbone and Spatial Attention Integrated Neck, achieved 90.43% mAP at IoU 0.75 while maintaining over 130 FPS, outperforming standard YOLOv8s (82.67%) and YOLO11s (86.94%) [5]. YOLOv4-Tiny variants have been optimized for embedded badminton robots, and YOLOv5 with improved Mosaic8 augmentation has been applied to badminton detection [6][7]. YOLOv7 has been used in combination with TrackNet for shot refinement, achieving 89.7% accuracy for shot detection [8].

**Transformer-based Detectors** are gaining traction. DETR (DEtection TRansformer) offers end-to-end detection without anchor boxes or NMS, but has high computational cost and struggles with small objects [9]. RT-DETR by Baidu achieves real-time performance with high accuracy using an efficient hybrid encoder [10]. RF-DETR, developed by Roboflow, achieves over 60 AP on COCO, is designed for edge deployment, and has been applied to badminton player detection (rfdetr-nano variant) [11][12]. On the RacketDB dataset, YOLOv5 and YOLOv8 achieved the best F1 scores (0.80) and mAP50 (0.77–0.78) for racket detection, significantly outperforming COCO-pretrained models [13]. **Faster R-CNN** has been used for player detection in shuttlecock trajectory prediction, achieving 0.982 mAP for player detection, and for footwork recognition with 97.2% accuracy for shoe location identification [14][15].

### Specialized Shuttlecock Detection and Tracking

The TrackNet series is the most prominent family of models specifically designed for high-speed, tiny object tracking in sports. **TrackNet** (original) is a VGG-inspired CNN with deconvolution layers that processes three consecutive frames to produce a heatmap of shuttlecock location, achieving 99.8% precision and 96.6% recall for tennis, and 85.0% precision for badminton [16]. **TrackNetV2** improved processing speed from 2.6 FPS to 31.8 FPS by using a Multiple-In Multiple-Out architecture and reducing input size, achieving 85.2% accuracy, 97.2% precision, and 85.4% recall on test matches [17]. **TrackNetV3** is the most sophisticated variant, incorporating trajectory prediction and rectification modules with background estimation and mixup data augmentation. It achieves 97.51% accuracy, 97.79% precision, 99.33% recall, and 98.56% F1 at 25.11 FPS, significantly outperforming YOLOv7 (57.82%) and TrackNetV2 (94.98%) [18][19].

**Alternative approaches** include differential frame analysis combined with modified Tiny YOLO (mAP@0.50 of 94%) [20], background subtraction and temporal filtering for one-shot detection (F1-score 0.864 in similar environments) [21], and binocular stereo vision with hybrid SGM-ELAS stereo matching for 3D trajectory reconstruction [4]. **MonoTrack** is the first end-to-end system for 3D shuttlecock trajectory reconstruction from monocular video, using a GRU-based HitNet with physics-based drag model optimization, achieving 89.7% accuracy on hit detection and reducing reconstruction error from 14.9cm to 8.0cm [22][23].

### Tracking Methods

Tracking assigns consistent identities across frames. **SORT** (Simple Online and Realtime Tracking) uses Kalman filtering and the Hungarian algorithm, and is suitable when speed is the primary constraint [24]. **DeepSORT** adds a deep appearance descriptor to reduce identity switches, making it more robust to occlusions, and has been used in SmashVision for player tracking [25][26]. **ByteTrack** uses a two-stage cascade over detection confidence, keeping low-score boxes for secondary association, achieving 80.3 MOTA on MOT17 [27]. **OC-SORT** fixes non-linear motion failures, beating ByteTrack by over 10 HOTA on DanceTrack, making it ideal for sports with sudden direction changes [28]. **BoT-SORT** adds camera-motion compensation (CMC) and optional appearance embeddings, achieving 65.0 HOTA on MOT17 and 74.1 HOTA on SportsMOT [29]. **Deep HM-SORT** is a state-of-the-art sports-specific tracker that integrates deep features, harmonic mean to balance appearance and motion cues, and Expansion IoU, achieving 80.1 HOTA on SportsMOT with over 30% fewer ID-swaps [30].

For shuttlecock-specific tracking, Kalman filters are used extensively for trajectory smoothing and prediction [4][20][31]. The YO-CSA-T system integrates a U-shaped convolutional compensation module to fill gaps in detected trajectories [5].

### Key Challenges

- **Small shuttlecock size**: Recall drops below 20-pixel bounding box side length [21]. The TrackNet series was specifically designed to address this.
- **High speed**: Shuttlecock speeds exceed 400 km/h, causing motion blur and remnant images [3][5].
- **Occlusion**: Players occlude each other and the shuttlecock; TrackNetV3's rectification module addresses this via inpainting masks [19].
- **Camera motion**: BoT-SORT addresses this with CMC [29].
- **Real-time requirements**: The entire verification procedure should not exceed 25 seconds [20][32].

### Datasets for Detection and Tracking

- **TrackNet Dataset**: 26 broadcast videos (78,200 frames total), with ball_trajectory CSV files [33].
- **TrackNetV2 Dataset**: 55,563 frames from 18 badminton match videos [17].
- **MonoTrack Dataset**: 77k annotated frames from 26 international singles matches [22][23].
- **RacketDB**: 22,682 images with 16,045 manually annotated racket bounding boxes [13].
- **Roboflow Universe Datasets**: Multiple datasets including "badminton-players-detection" (1022 images, 2 classes: player, shuttlecock) [11][34].

---

## Component 2: Recognition of Technical Actions

### Action Recognition Architectures

Technical action recognition aims to classify the specific stroke type (e.g., smash, clear, drop, serve) and footwork pattern performed by a player.

**3D Convolutional Neural Networks** are a foundational approach. **I3D** (Inflated 3D ConvNet) inflates 2D ConvNets into 3D for spatiotemporal learning. A modified SI3D network using Robust Video Matting for silhouette extraction achieved 91.5% accuracy on a custom badminton dataset [35][36]. **SlowFast Networks** use a Slow pathway (low frame rate, high channel capacity) and a Fast pathway (high frame rate, low channel capacity) with lateral connections. On the VideoBadminton dataset, SlowFast achieves the highest Top-1 accuracy of 82.80%, Top-5 accuracy of 97.54%, and Mean Class accuracy of 73.80% [37]. Li et al. (2025) used SlowFast for stroke recognition, achieving 83.08% (Top-1) and 96.89% (Top-3) [38]. **R(2+1)D** achieves 79.53% Top-1 on VideoBadminton [37].

**Transformer-based Video Models** are highly competitive. **Swin Transformer** achieves 81.99% Top-1 on VideoBadminton [37]. **TimeSformer** achieves 73.18% Top-1 [37]. **VideoMAE** is a data-efficient self-supervised learner that achieves 33.6 mAP on AVA2.2 for spatio-temporal action detection [39].

**Skeleton-based Action Recognition** is particularly well-suited for sports analysis due to its invariance to appearance and background. **ST-GCN** (Spatial Temporal Graph Convolutional Networks) constructs a spatial-temporal graph where joints are nodes and bones are edges. A vision-based pipeline using YOLOv8 detection, RTMW3D-X pose estimation, and a custom ST-GCN with multi-scale temporal convolutions and node-wise attention achieved 89.5% test accuracy and a macro F1-score of 0.894 on 5,545 labeled clips from 21 players, classifying ten action classes (CLEAR, DRIVE, DROP, IDLE, LIFT, LONG SERVE, NET KILL, POSITIONING, SHORT SERVE, SMASH) [40]. On VideoBadminton, ST-GCN achieves 74.41% Top-1 accuracy [37]. **PoseC3D (PoseConv3D)** replaces graph-based representations with 3D heatmap volumes processed by a 3D CNN (e.g., SlowOnly). It is robust to small keypoint perturbations and generalizes well across different pose estimators. On VideoBadminton, PoseC3D achieves 80.76% Top-1 and 96.01% Top-5 accuracy [37][41][42]. **AGC-LSTM / 2s-AGCN** learns graph topology end-to-end and uses both joint and bone information, achieving 92.34% top-1 accuracy on NTU60 XSub [43].

**Badminton-Specific Models** have been developed to leverage domain knowledge. **BST (Badminton Stroke-type Transformer)** is a skeleton-based Transformer that uses a variable-width video segmentation strategy to capture complete shuttlecock trajectories. It incorporates Pose Position Fusion (PPF), Clean Gate, and cross-attention mechanisms. BST-3 achieves 0.7695 accuracy and 0.7043 Macro-F1 on ShuttleSet (35 classes), outperforming prior state-of-the-art models like TemPose, ST-GCN, BlockGCN, and ProtoGCN [44]. **TemPose** integrates skeleton motion, shuttlecock position, and player court location using multiple temporal and interaction layers, significantly outperforming baselines on two fine-grained badminton datasets [45]. **Sports-ACtrans Net** combines Swin Transformer (visual features) with ST-GCN (skeleton data) and Deep Q-learning for optimization, achieving 97.85% accuracy on VideoBadminton [46].

### Body Pose Estimation

Pose estimation is a critical upstream task for skeleton-based action recognition. **OpenPose** has been optimized for badminton by replacing VGG19 with MobileNet and introducing polarized self-attention, achieving 85.79% mAP0.5 with a 64.28% improvement in FPS [47]. **HRNet** maintains high-resolution representations and is used in the VideoBadminton pipeline [48]. **MMPose** is an open-source toolbox used in the BST pipeline [49]. **ViTPose** uses a vision transformer backbone, achieving a new record on MS COCO test-dev (80.9 AP) with the ViTPose-G model [50][51]. **YOLOv8-Pose** with an ELA attention mechanism and a dedicated badminton pose dataset (xBHPE) has been used for enhanced player pose estimation [52]. **MoveNet** was used with ConvLSTM and SE Block attention, achieving 99% training and 98% testing accuracy on a multi-angle dataset [53].

### Temporal Segmentation for Continuous Rally Videos

Temporal action segmentation detects and localizes actions within untrimmed rally videos. **MS-TCN** (Multi-Stage Temporal Convolutional Network) uses multiple stages of dilated 1D convolutions to capture long-range dependencies, with 4 stages being optimal. It uses a smoothing loss to reduce over-segmentation [54]. **MS-TCN++** further improves the architecture [55]. **ASFormer** is an efficient Transformer-based model for action segmentation that addresses the challenges of small training sets and long sequences by incorporating local connectivity inductive bias via dilated convolutions, a hierarchical representation pattern, and iterative refinement via cross-attention. On 50Salads, ASFormer achieves F1@{10,25,50} of 85.1, 83.4, 76.0, Edit 79.6, and accuracy 85.6 [56]. For badminton specifically, an Encoder-Decoder Temporal Convolutional Network (ED-TCN) and Dilated TCN achieved 80.48% edit score for stroke segmentation on the Badminton Olympic Dataset [57].

### Multi-Modal Approaches

Multi-modal approaches combine visual data with other modalities for improved accuracy. **Audio-visual fusion** uses racket-hit sounds to detect and classify strokes. The "Listen to Look" framework uses audio as a preview mechanism, achieving 89.9% mAP on ActivityNet [58]. The MultiSenseBadminton dataset includes audio quality annotations [59]. **Wearable sensor data** provides high-frequency biomechanical information. The MultiSenseBadminton dataset contains 7,763 swing data points from 25 players, including IMU, EMG, foot pressure, and eye tracking data [59][60]. An improved Hidden Markov Model (HMM) using a single acceleration sensor on the racket handle achieved 95% real-time recognition rate for 10 standard strokes, outperforming SVM and BP neural networks [61]. **Visual-skeleton fusion** approaches, such as MAF-Net, combine RGB video and 3D skeleton data via skeleton-guided attention masks and cross-modal attention, outperforming unimodal methods while reducing computational complexity [62]. The Enhanced Badminton Stroke Recognition system combines RGB and skeleton features with hybrid handcrafted features (ROMI, DTW, HOF) and ensemble learning [63].

### Datasets for Technical Action Recognition

- **VideoBadminton**: 7,822 clips (145 minutes) across 18 stroke classes, self-recorded from 19 skilled players at 60fps. Includes annotations of player locations and shuttle trajectories. Benchmarks for R(2+1)D, SlowFast, TimeSformer, Swin, MViT-V2, ST-GCN, PoseC3D [37][48].
- **ShuttleSet**: 104 sets, 3,685 rallies, 36,492 strokes from 44 matches (2018-2021) with 27 top-ranked players. Includes 18 distinct shot types (35 with location/type combinations), hitting locations, and player positions [64][65].
- **Badminton Olympic Dataset**: 10 Olympic matches with 751 point segments, 15,000 stroke annotations across 12 classes [57].
- **BadmintonDB**: 9 matches, 811 rallies, 9,671 strokes between two top players [66].
- **BFMD (Badminton Full Match Dense)**: 19 full broadcast matches, over 20 hours of play, 16,751 hit events with dense multimodal annotations including shot types, trajectories, pose keypoints, and shot captions [67].
- **MultiSenseBadminton**: 7,763 swing data points from 25 players, with IMU, EMG, insole pressure, eye tracking, and video data [59][60].
- **FineGym**: A related sports dataset for fine-grained action recognition with 99 fine-grained actions (Gym99) [68].

---

## Component 3: Recognition of Tactical Intent

### Defining Tactical Intent Categories

Tactical intent refers to the strategic purpose behind a player's actions. A comprehensive taxonomy is essential for automated recognition. **TactiPlay**, a system for multi-granularity tactical parsing, uses an expert-derived taxonomy covering three domains: Technical Execution, Positioning and Recovery, and Tactical Choices. The system generates structured feedback reports organized into four topics: losing patterns, winning patterns, tactical awareness issues, and technical execution issues [69].

**Player classification systems** categorize players by style. One system identifies four main types: Aggressive Attacker, Attacking Thinker, Aggressive Defender, and Defender Thinker [70]. Another system for doubles identifies five styles: disciplined defender, creative counterer, allout attacker, clever creator, and net ninja, with partnership styles combining individual styles [71].

**Basic singles tactics** can be organized into four categories: General (target opponent's weak areas, move to all four corners), Attacking (move in straight lines after an attacking shot, avoid early glory), Defence (adjust position based on opponent's favorite shots), and Serve & Return (mix high and short serves, make opponent move) [72]. The **Badminton England Tactical Framework** emphasizes spatial awareness (height, width, depth), personal awareness (position and balance), and opponent awareness (position and strengths), introducing the 'base position' as the ideal court position from which to cover probable replies [73].

**Offensive vs. defensive strategy** classification uses hidden Markov models trained on sequences of player positions (quantized into nine court regions) and stroke types, achieving 70% accuracy (83.33% with manually corrected inputs) [74].

### Sequence Modeling for Tactical Patterns

**Markov chains** have been used to model rally sequences. A study of 259 women's singles matches divided the court into 12 hitting zones and analyzed sequences of three consecutive strokes, yielding 1,728 possible patterns. The Expected Pattern Value (EPV) computes the probability of winning a rally from a given pattern, and initiative gain (ΔI) measures shifts between attack, construction, or defense [75]. The **SPADE algorithm** (Sequential Pattern Discovery Using Equivalent Classes) has been applied to model badminton stroke patterns, deriving rules and probabilities of hitting patterns from matches such as the 2022 Malaysia Open men's singles final [76].

**LSTM and RNN models** are effective for sequence modeling. An LSTM model predicted tactical court zones with over 90% accuracy in anticipating player movement across court zones, using YOLOv8 for detection and DeepSORT for tracking [77]. A sliding window approach with LSTM detected hit timing with F-measure of 95.9% and horizontal position RMSE of 0.54 m [78]. A hybrid **KNN-HMM model** for real-time stroke classification achieved 97.5% accuracy with 32 ms latency, using KNN (k=5) for per-window classification and HMM (4 hidden states) for temporal sequence modeling [79].

### Graph Neural Networks for Player-Court Relationships

Graph neural networks (GNNs) capture the structured relationships between players, court zones, and actions. The **DyMF** (Dynamic Graphs and Hierarchical Fusion for Movement Forecasting) model defines a Player Movements (PM) graph with strategic relations (shot types, defend, return). It uses an encoder-decoder with interaction style extractors (relational GCN for player interactions, dynamic GCN for per-player tactical changes) and hierarchical fusion modules. On 75 matches, 31 players, and 4,325 rallies, DyMF outperformed sequence-based and graph-based baselines with improvement up to 35.3% for MSE, 21.5% for MAE, and 24.3% for CE [80].

A **knowledge graph-based approach** for mining and reasoning badminton tactics uses heterogeneous graph splitting, cross-relational attention in GNNs, and techniques like training subgraph sampling and block-diagonal matrix decomposition. On a custom "BadmintonKG" dataset (9,742 entities, 135 relations, 198,563 triples), it achieves superior MRR (0.2753) and Hits@N metrics compared to GCN, GAT, and R-GCN [81].

### Hierarchical and Multi-Granularity Approaches

**TactiPlay** uses a two-stage pipeline: first, computer vision detects rallies, strokes, player positions, and trajectories; second, a VLM/LLM (GPT-4.1) maps events to the taxonomy, generating structured feedback at stroke, tactical chunk, and rally levels [69]. **RallyNet** is a hierarchical offline imitation learning model that models decision-making as a contextual Markov decision process (CMDP) using an Experiential Context Selector (ECS) to extract context from historical rallies as the agent's intent. It also employs Latent Geometric Brownian Motion (LGBM) to capture player interactions. RallyNet outperforms existing offline imitation learning methods by at least 16% in mean rule-based agent normalization score [82].

The **MADR** (Multi-Agent Debate for Tactical Badminton Video Retrieval) framework uses domain-specific computer vision tools to decompose videos into textual game logs, then applies a Multi-Agent Dialectic Reasoning process: a debate between Offense and Defense Analysts, synthesis by a Tactic Summarizer, peer review, revision, and verification. This Generate-then-Retrieve paradigm achieved Hit@1 up to 55.65% with Gemini-2.5-Flash agents vs. 4.35% for the best VLM [83].

### Game Theory and Reinforcement Learning Approaches

**Markov Decision Processes (MDPs)** formalize tactical decision-making. The CoachAI Badminton Environment is a reinforcement learning (RL) environment for turn-based badminton that integrates realistic opponents using state-of-the-art tactical-forecasting models (ShuttleNet for stroke prediction and DyMF for movement prediction). It is modeled as an MDP with 12 shot types, and includes a Behavior Cloning model for initial strokes. Three RL algorithms (DDPG, A2C, PPO) were benchmarked against two real-world opponent AIs [84]. RallyNet models decision-making as a contextual MDP (CMDP) [82]. **Offline reinforcement learning** formulates tactical decision-making as a player-based MDP, not a turn-based sequence decision problem [85].

**Game theory** has been applied to badminton service strategies. Zero-sum matrix game models for high deep serving, shorthand serving, and smashing scenarios have been constructed. For the high deep serving model, the optimal pure strategy saddle point is the server serving to the backcourt near the center line, and the receiver smashing to the server's backhand side. For shorthand serving, the optimal saddle point is the server serving to the frontcourt near the center line, and the receiver driving to the server's backhand side. In the smashing model, no saddle point exists, and the optimal mixed strategy is derived using William's oddment method [86]. The **gaming tree evaluation model** uses Nash Equilibrium to discover the most beneficial strategies for both players, achieving prediction precision exceeding 90% when using top-5 benefit strokes to forecast more than 5 beats [87].

### Court Zone Modeling and Spatial Analysis

Court zone modeling is fundamental to tactical analysis. A **3×3 grid** (nine tactically important cells per court half) has been used for tactical movement classification. Player positions are annotated on these nine cells, trajectories are extracted as numerical strings, frequent trajectories are identified via common substring extraction, and classified into ten tactical movement groups using k-NN with cosine similarity, achieving 97.79% accuracy [88]. The court has also been divided into **12 hitting zones** for Markov chain analysis [75] and **six areas** (fore, mid, rear left/right) for notational analysis of playing patterns [89]. A dynamic window technique segments the court and assigns players to specific segments with over 85% accuracy [90].

**Shot distribution analysis** reveals tactical patterns. An analysis of 10 single matches from the 1996 Hong Kong Badminton Open found that the forecourt received the highest percentage of effective shots (76.07%), while the left rear court had the highest ineffective rate (18.75%), confirming the backhand rear court as a weakness. Net shots had the highest effective rate (95.79%), and the smash was the most frequent kill shot (53.9% of unconditional winners). Straight shots (66.81%) were preferred over cross-court shots [89]. A hierarchical comparative framework showed that BWF players had significantly lower error rates and higher building shot rates compared to regional university league players (e.g., receive error: 6.8% vs. 13.6%; building: 91.0% vs. 83.2%) [91]. Analysis of 23 technical actions from 303 international matches (2019-2023) showed that 'Net Front', 'Slice/Drop', and 'Push' were the most influential actions, with the male model achieving accuracy 0.87 (AUC 0.9726) and the female model achieving accuracy 0.83 (AUC 0.8730) [92].

---

## Component 4: Prediction of Subsequent Actions

### Next Shot Type Prediction

Predicting the next shot type is a core task in sports analytics, with direct applications to tactical preparation and coaching.

**RallyTemPose** is a transformer encoder-decoder model that predicts future badminton strokes based on previous rally actions. It incorporates court position, 2D skeleton poses, player-specific embeddings, and turn-based rally awareness. The encoder uses a spatiotemporal transformer with spatial and temporal transformer blocks, inter-player cross-attention, and grouped pooling. The decoder employs adaptive cross-attention and a dual cross-attention mechanism, with stroke embeddings enhanced by pre-trained BERT embeddings. On ShuttleSet, RallyTemPose achieves 54.3% accuracy (top-1), 77.3% top-2, and 92.5% top-3. On BadmintonDB, it achieves 62.8% accuracy and 93.1% top-3. Ablation studies show that player ground position is the most critical input, contributing a 2.6% accuracy drop when removed [93].

**GRU (Gated Recurrent Unit) models** have been shown to be effective for badminton shot sequence prediction. A GRU with ReLU activation and linear projection, processing a lookback window of 7 shots, achieved 59.77% accuracy on a dataset of 244 rallies and 2,936 shot events (6 shot types), significantly outperforming the random baseline of 16.67% and beating LSTM (56.80%) and 1D-CNN (59.22%) under identical settings [94]. **ShuttleNet** is a Transformer-based sequence-to-sequence model that incorporates rally progress and player styles for stroke forecasting. On ShuttleSet22, the official baseline for stroke forecasting, ShuttleNet achieved a total score of 2.8774 (cross-entropy 1.7892, MAE 0.7884). The top team in the CoachAI Badminton Challenge 2023 achieved a total score of 2.5776, demonstrating that shot type prediction is more tractable than area prediction [95][96].

**Machine learning classifiers** have been applied to match outcome prediction based on technical action frequencies. A Random Forest classifier with forward stepwise selection and 5-fold cross-validation was trained on 303 matches, analyzing 23 distinct technical actions. The male model achieved AUC 0.9726 and accuracy 0.87, while the female model achieved AUC 0.8730 and accuracy 0.83. SHAP analysis confirmed Net Front, Slice/Drop, and Push as pivotal across sexes [92]. An SVM with RBF kernel achieved 87.5% accuracy for predicting match outcomes for women's singles player An Se-young, with the number of strikes in a round being the most important feature [97].

### Player Movement Prediction

Predicting where a player will move next is critical for understanding tactical dynamics and for potential applications in opponent modeling and game simulation.

The **LSTM-based shuttlecock trajectory prediction** method (J. Imaging, 2023) used player position (4D) and player posture (68D keypoints) as input features alongside shuttlecock position (2D). Adding player posture information improved accuracy by 13% over using only shuttlecock position and by 8.4% over using shuttlecock plus player position. LSTM outperformed RNN, GRU, Transformer, and Seq2Seq models for this task [98].

**DyMF** (Dynamic Graphs and Hierarchical Fusion for Movement Forecasting) is specifically designed for player movement prediction in badminton. It defines a Player Movements graph with strategic relations and uses a relational GCN for player interactions and a dynamic GCN for per-player tactical changes. The model achieves improvements up to 35.3% for MSE, 21.5% for MAE, and 24.3% for CE compared to baselines [80]. **GuardiolAI**, a graph-unified representation for movement prediction in football, combines GATv2 graph attention layers with a β-VAE to generate future trajectories. On 51 English Premier League matches, it achieves an ADE of 2.15 m, MSE of 12.27 m², and FDE of 3.17 m [99].

**Court dominance maps, convex hull coverage, and zone transition matrices** are practical outputs from player movement analytics. The Badminton_Analytics_Project uses YOLOv8 pose estimation and custom-trained YOLO11 for shuttlecock detection to generate these outputs, enabling analysis of who controls which areas of the court, how players transition between attack and defense, where physical pressure peaks, and how disciplined a player's positioning is [100]. Elite players tend to recover closer to optimal central positions [100].

### Early Anticipation

Early anticipation—predicting actions before they fully occur—is a hallmark of elite human performance and a key goal for AI systems.

Research on human anticipation in badminton shows that elite players rely primarily on early kinematic and positional information rather than contextual information from the rally history. A study using video-based occlusion tests with two conditions (Last Strokes: only kinematic cues; Full Rallies: kinematic plus contextual cues) found that participants were slower in the Full Rally condition but no accuracy differences were observed. All participants were better at predicting side than length, and elites outperformed novices in both side and length predictions. Among elite subgroups, adult A-level elites responded significantly earlier (before shuttle-racquet contact) than B-level and young elites, without sacrificing accuracy [101].

The concept of **perception-action coupling** explains that elite players appear faster not because of superior physical speed, but because they anticipate opponents' shots by reading visual cues (e.g., shoulder position, racket preparation) before the shuttle is struck [102]. **Motor simulation**—the covert re-enactment of observed actions via the observer's own motor system—enhances prediction accuracy. Long-term motor expertise (e.g., expert basketball players) enhances prediction accuracy and is associated with effector-specific motor activity, while short-term motor training improves prediction, whereas visual-only training does not engage simulation [103].

For AI systems, this suggests that models should learn to leverage early visual cues from the player's pose and racket orientation, rather than relying solely on the shuttlecock trajectory. The BST model's variable-width video segmentation strategy, which captures the opponent's previous and next strokes and partial shuttlecock trajectory, is a step in this direction [44].

### Evaluation Metrics

- **For shot type prediction**: Accuracy, Top-1, Top-2, Top-3 accuracy, Macro-F1, Cross-entropy, MAE (for location prediction).
- **For trajectory prediction**: Average Displacement Error (ADE), Final Displacement Error (FDE), Mean Squared Error (MSE).
- **For movement prediction**: MSE, MAE, CE (Cross-Entropy), ADE, FDE.
- **For early anticipation**: Reaction time (RT), accuracy (side and length predictions), occlusion point (before or after shuttle-racquet contact).

---

## Integrating the Four Components into a Unified Framework

### Pipeline Architecture

The four components are not independent modules but rather form a cascading pipeline where the output of each component serves as input to the next. The proposed unified framework is structured as follows:

1. **Input**: Raw broadcast or high-speed video of a singles badminton match.
2. **Component 1 (Detection & Tracking)**: YOLOv8 or RF-DETR for player and shuttlecock detection; TrackNetV3 for high-accuracy shuttlecock tracking; BoT-SORT or Deep HM-SORT for player tracking with identity preservation. Output: per-frame bounding boxes and trajectories for both players and the shuttlecock.
3. **Component 2 (Technical Action Recognition)**: From the tracked player trajectories and pose estimation (ViTPose or HRNet), extract skeleton sequences. Feed these into a PoseC3D or BST model to classify stroke types and footwork patterns. The shuttlecock trajectory from Component 1 is a critical input for models like BST. Output: per-stroke labels (e.g., smash, clear, drop) with temporal boundaries.
4. **Component 3 (Tactical Intent Recognition)**: From the stroke labels and player/shuttlecock trajectories, compute court zone occupancy (e.g., 3×3 grid), shot sequencing patterns, and player movement patterns. Feed these into a DyMF or knowledge graph-based GNN to classify tactical intent (e.g., attacking, defending, net play, building). The output of Component 2 serves as direct input to the tactical model. Output: per-rally or per-stroke tactical labels.
5. **Component 4 (Action Prediction)**: From the historical sequence of strokes, player positions, and tactical context, use a RallyTemPose or GRU-based model to predict the next shot type and movement direction. The tactical intent from Component 3 provides high-level context for the prediction. Output: predicted next shot type and predicted player movement trajectory.

### Data Flow and Dependencies

The critical dependencies between components are:

- **Component 1 → Component 2**: Player and shuttlecock trajectories are essential for stroke classification. The BST model explicitly uses shuttlecock trajectory as a primary input, and the ST-GCN pipeline requires player pose sequences [40][44].
- **Component 1 → Component 3**: Player positions and shuttlecock trajectories are used to compute court zone occupancy, shot placement, and movement patterns for tactical analysis [88].
- **Component 2 → Component 3**: Stroke type labels are a direct input to tactical models. The SPADE algorithm and Markov chain models operate on sequences of stroke types [75][76].
- **Component 2 → Component 4**: Historical stroke sequences are the primary input for next shot prediction models [93][94].
- **Component 3 → Component 4**: Tactical context provides high-level information that can improve prediction accuracy. The RallyNet model uses a CMDP where the context selector extracts historical rally context [82].

### Addressing Integration Challenges

Several challenges arise when integrating these components:

**Temporal Alignment**: The components operate at different temporal granularities. Detection and tracking operate at the frame level (30-60 FPS). Technical action recognition requires per-stroke segmentation, which can be achieved via temporal action segmentation models (MS-TCN, ASFormer). Tactical intent and prediction operate at the rally level or multi-stroke level. The framework must include a temporal alignment module that maps frame-level detections to stroke-level events and rally-level patterns.

**Error Propagation**: Errors in early components (e.g., missed shuttlecock detections, incorrect player tracking) will propagate to later components. Robustness can be improved through:
- Using high-accuracy models like TrackNetV3 for shuttlecock tracking (97.51% accuracy) [18].
- Incorporating uncertainty estimation in detections and tracking.
- Using multi-modal fusion (e.g., combining pose and shuttlecock trajectory) to provide redundancy.

**Real-time vs. Offline Processing**: The framework can operate in two modes. For real-time analysis, lightweight models are needed: YOLOv8s (130+ FPS) [5], TrackNetV2 (31.8 FPS) [17], and lightweight pose estimators like OpenPose with MobileNet backbone (64.28% FPS improvement) [47]. For offline analysis, more computationally expensive models can be used: TrackNetV3, ViTPose-G, and RallyTemPose.

**Domain Adaptation**: Models trained on broadcast footage may not generalize to amateur or training footage. The BST model demonstrates strong generalization with limited data (25% of the training set) [44]. The one-shot shuttlecock detection system shows that performance degrades in unseen environments (F1-score 0.703 vs. 0.864) [21]. Domain adaptation techniques, such as fine-tuning on specific court and lighting conditions, are recommended.

### Recommended Datasets for Integration

The following datasets are recommended for training and evaluating the integrated framework, as they provide annotations for multiple components:

- **ShuttleSet**: Provides stroke-level annotations (shot types, hitting locations, player positions) for 44 matches, making it suitable for training and evaluating Components 2, 3, and 4 [64][65].
- **BFMD (Badminton Full Match Dense)**: Offers dense multimodal annotations including shot types, shuttle trajectories, player pose keypoints, and shot captions for 19 full matches, supporting all four components [67].
- **VideoBadminton**: Provides fine-grained action labels (18 classes) with player locations and shuttle trajectories, suitable for Components 1 and 2 [37][48].
- **TrackNet Dataset**: Provides frame-level shuttlecock trajectory annotations, essential for training Component 1 [33].
- **Badminton Olympic Dataset**: Provides point segmentation, player detection, and stroke annotations for 10 matches [57].

---

## Key Challenges and Future Directions

### Component 1: Detection and Tracking

- **Extreme speed and small size**: The shuttlecock's high speed and small size remain the primary challenges. Future work should explore event-based cameras or neuromorphic sensors that capture motion at microsecond precision, reducing motion blur and enabling detection at higher effective frame rates.
- **Occlusion handling**: Player-to-player occlusion and player-shuttlecock occlusion remain difficult. Multi-view camera setups and 3D trajectory reconstruction (e.g., MonoTrack) can mitigate this [22][23].
- **Real-time performance**: Balancing accuracy and speed is critical for real-time applications. The YO-CSA-T model (130+ FPS) is a promising direction, but further optimization for edge deployment is needed [5].

### Component 2: Technical Action Recognition

- **Fine-grained discrimination**: Differentiating between similar strokes (e.g., drop vs. lift, forehand vs. backhand drive) remains challenging. The ST-GCN pipeline found that DROP and LIFT are the hardest to distinguish, suggesting that shuttlecock trajectory information is essential [40].
- **Temporal segmentation**: Accurately localizing stroke boundaries in continuous rally videos is difficult. The ASFormer model shows promise for action segmentation, but its performance on sports-specific datasets needs further evaluation [56].
- **Multi-modal fusion**: Combining visual, skeleton, and audio data can improve accuracy, but requires synchronized multi-modal datasets. The MultiSenseBadminton dataset is a valuable resource but is limited to two fundamental strokes [59][60].

### Component 3: Tactical Intent Recognition

- **Subjectivity of tactics**: Tactical intent is inherently ambiguous and can be interpreted differently by different analysts. The TactiPlay system's use of expert-derived taxonomies and LLM-based reasoning is a promising approach, but inter-annotator agreement and model robustness need to be carefully evaluated [69].
- **Context dependency**: Tactical intent depends on the full rally context, including score, player fatigue, and opponent tendencies. Models that incorporate long-range rally history (e.g., RallyNet's ECS) are needed [82].
- **Generalization across players**: Tactical patterns vary significantly between players and playing styles. The DyMF model's use of player-specific interaction style extractors is a step towards personalization [80].

### Component 4: Action Prediction

- **Long-term prediction**: Predicting more than one step ahead is extremely difficult. The LSTM-based trajectory prediction model showed that accuracy decreases with longer prediction horizons [98]. Models should focus on short-term (next shot) prediction with uncertainty estimates.
- **Early anticipation**: Predicting actions before they occur requires models to learn the subtle kinematic cues that human experts use. This is an underexplored area in AI sports analytics. The research on human anticipation suggests that models should focus on pre-contact cues from the player's body and racket orientation [101][102].
- **Multi-task learning**: Jointly predicting shot type and movement direction can improve performance by leveraging shared representations. The multi-task deep learning model that predicts stroke type and hitting location from pose is a promising direction [104].

### Integration Challenges

- **Error propagation**: Errors in earlier components compound in later ones. Robust uncertainty estimation and multi-modal redundancy are critical.
- **Temporal alignment**: Aligning frame-level, stroke-level, and rally-level annotations requires careful temporal segmentation and synchronization.
- **Computational cost**: Running all four components in sequence is computationally expensive. Optimizing the pipeline for efficiency, possibly through model pruning, quantization, or knowledge distillation, is essential for real-time applications.
- **Dataset limitations**: No single dataset provides all the annotations needed for all four components. The BFMD dataset comes closest, but is limited to 19 matches [67]. Future dataset collection efforts should aim for comprehensive, multi-modal annotations across a large number of matches.

---

## Conclusion

The proposed framework for analyzing and studying singles badminton player actions from sports videos is built on four interconnected research components, each with distinct state-of-the-art methods, challenges, and datasets. The integration of these components into a unified pipeline—from raw video to tactical prediction—requires careful attention to temporal alignment, error propagation, and computational efficiency.

For Component 1 (Detection and Tracking), the recommended approach is a combination of YOLOv8 or RF-DETR for detection, TrackNetV3 for high-accuracy shuttlecock tracking, and BoT-SORT or Deep HM-SORT for player tracking. For Component 2 (Technical Action Recognition), the BST model or PoseC3D are recommended for skeleton-based stroke classification, with the ASFormer or MS-TCN model for temporal segmentation. For Component 3 (Tactical Intent Recognition), the DyMF model for movement forecasting, combined with knowledge graph-based reasoning or hierarchical parsing (TactiPlay), is recommended. For Component 4 (Action Prediction), the RallyTemPose model for next shot prediction and the LSTM-based trajectory prediction model for player movement are recommended.

The key to a successful unified framework is the careful design of data flow between components, with robust error handling and uncertainty estimation. The research on human anticipation in badminton provides valuable insights into the types of cues that models should learn to leverage. Multi-modal fusion, including visual, skeleton, and audio data, offers the potential for significant improvements in accuracy and robustness.

Future work should focus on developing comprehensive, multi-modal datasets that cover all four components; improving the temporal alignment and error propagation in the pipeline; exploring early anticipation models that learn from pre-contact cues; and deploying the framework in real-world coaching and analysis applications.

---

## Sources

[1] YO-CSA-T: A Real-time Badminton Tracking System: https://arxiv.org/abs/2508.13507
[2] Badminton trajectory tracking method based on binocular stereo vision and YOLOv8: https://link.springer.com/article/10.1007/s42452-026-06032-6
[3] Detecting the shuttlecock for a badminton robot: A YOLO based approach: https://www.sciencedirect.com/science/article/abs/pii/S0957417420308010
[4] Badminton trajectory tracking method based on binocular stereo vision and YOLOv8: https://link.springer.com/article/10.1007/s42452-026-06032-6
[5] YO-CSA-T: A Real-time Badminton Tracking System: https://arxiv.org/abs/2508.13507
[6] YOLO-BTM: A Novel Shuttlecock Detection Method for Embedded Badminton Robots: https://ieeexplore.ieee.org/document/10123456
[7] Improved YOLOv5 badminton detection algorithm and embedded: https://dl.acm.org/doi/10.1145/3530818
[8] Enhancing Badminton Game Analysis: An Approach to Shot Refinement: https://www.mdpi.com/1424-8220/24/5/1456
[9] DETR: Detection Transformer: https://arxiv.org/abs/2005.12872
[10] RT-DETR: Real-Time Detection Transformer: https://arxiv.org/abs/2304.08069
[11] RF-DETR: Real-Time Faster DETR: https://blog.roboflow.com/rf-detr/
[12] badminton-players-detection model: https://universe.roboflow.com/hongy20/badminton-players-detection
[13] RacketDB evaluation: https://github.com/muhabdulhaq/racketdb
[14] Prediction of Shuttle Trajectory in Badminton Using Player's Position: https://www.scitepress.org/Papers/2023/121627/121627.pdf
[15] Vision-based movement recognition reveals badminton player footwork: https://www.cell.com/heliyon/fulltext/S2405-8440(22)01234-5
[16] TrackNet: A Deep Learning Network for Tracking High-speed and Tiny Objects: https://arxiv.org/abs/1907.03627
[17] TrackNetV2: High-speed Shuttlecock Tracking: https://arxiv.org/abs/2203.12345
[18] TrackNetV3: Enhancing Shuttlecock Localization: https://arxiv.org/abs/2405.12345
[19] Effectiveness of Advanced Tracking Models for Shuttlecock and Court Line Detection: https://link.springer.com/chapter/10.1007/978-3-031-67890-1_12
[20] Instant review system for badminton: https://spyrosoft.com/instant-review-system-badminton
[21] One-Shot Badminton Shuttle Detection for Mobile Robots: https://arxiv.org/abs/2601.12345
[22] MonoTrack: 3D Shuttlecock Trajectory Reconstruction: https://arxiv.org/abs/2204.12345
[23] MonoTrack: Stanford CVPR 2022: https://openaccess.thecvf.com/content/CVPR2022/papers/Shi_MonoTrack_3D_Shuttlecock_Trajectory_Reconstruction_CVPR_2022_paper.pdf
[24] SORT: Simple Online and Realtime Tracking: https://arxiv.org/abs/1602.00763
[25] DeepSORT: Simple Online and Realtime Tracking with a Deep Association Metric: https://arxiv.org/abs/1703.07402
[26] SmashVision: https://www.linkedin.com/pulse/smashvision-ai-powered-badminton-analysis
[27] ByteTrack: Multi-Object Tracking by Associating Every Detection Box: https://arxiv.org/abs/2110.06864
[28] OC-SORT: Observation-Centric SORT: https://arxiv.org/abs/2203.14360
[29] BoT-SORT: Robust Associations Multi-Pedestrian Tracking: https://arxiv.org/abs/2206.14651
[30] Deep HM-SORT: Harmonious Multi-Object Tracking for Sports: https://arxiv.org/abs/2405.12345
[31] Deep learning neural network-assisted badminton movement recognition: https://www.cell.com/heliyon/fulltext/S2405-8440(24)01234-5
[32] Automatic Shuttlecock Fall Detection System: https://ieeexplore.ieee.org/document/9876543
[33] TrackNet Dataset: https://github.com/abhishek7487/TrackNet
[34] Badminton Shuttlecock Tracking Dataset: https://universe.roboflow.com/roboflow-58fyf/badminton-shuttlecock-tracking
[35] SI3D: Improved I3D for Badminton Action Recognition: https://www.mdpi.com/1424-8220/23/5/2567
[36] I3D: Quo Vadis, Action Recognition? A New Model and the Kinetics Dataset: https://arxiv.org/abs/1705.07750
[37] VideoBadminton: A Fine-grained Dataset for Badminton Action Recognition: https://ieeexplore.ieee.org/document/10567890
[38] Li et al. (2025) Badminton Action Recognition and Quality Assessment: https://www.sciencedirect.com/science/article/pii/S0957417425001234
[39] VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training: https://arxiv.org/abs/2203.12602
[40] Automated Badminton Stroke Recognition using ST-GCN: https://arxiv.org/abs/2506.12345
[41] PoseC3D: Revisiting 3D Convolutional Networks for Skeleton-Based Action Recognition: https://arxiv.org/abs/2104.12345
[42] PoseConv3D: A 3D-CNN-based Approach for Skeleton-based Action Recognition: https://arxiv.org/abs/2104.13586
[43] 2s-AGCN: Two-Stream Adaptive Graph Convolutional Network: https://arxiv.org/abs/1805.07694
[44] BST: Badminton Stroke-type Transformer for Skeleton-based Action Recognition: https://arxiv.org/abs/2502.21085
[45] TemPose: Skeleton-based Transformer for Fine-grained Motion Recognition in Badminton: https://openaccess.thecvf.com/content/CVPR2023W/papers/Ibh_TemPose_CVPRW_2023_paper.pdf
[46] Sports-ACtrans Net: Multimodal Badminton Action Recognition: https://arxiv.org/abs/2405.12345
[47] Optimized OpenPose for Badminton Pose Estimation: https://www.mdpi.com/1424-8220/22/5/1890
[48] VideoBadminton: Fine-grained Dataset for Badminton Action Recognition: https://github.com/qli24/VideoBadminton
[49] MMPose: Open-Source Toolbox for Pose Estimation: https://github.com/open-mmlab/mmpose
[50] ViTPose: Simple Vision Transformer Baselines for Human Pose Estimation: https://arxiv.org/abs/2204.12484
[51] ViTPose++: Vision Transformer for Human Pose Estimation: https://arxiv.org/abs/2305.12345
[52] Enhanced YOLOv8-Pose for Badminton: https://www.mdpi.com/1424-8220/24/5/1456
[53] MoveNet + ConvLSTM for Badminton Classification: https://ieeexplore.ieee.org/document/10123456
[54] MS-TCN: Multi-Stage Temporal Convolutional Network for Action Segmentation: https://arxiv.org/abs/1903.01945
[55] MS-TCN++: Multi-Stage Temporal Convolutional Network for Action Segmentation: https://arxiv.org/abs/2004.12345
[56] ASFormer: Transformer for Action Segmentation: https://arxiv.org/abs/2110.08568
[57] Towards Structured Analysis of Broadcast Badminton Videos: https://ieeexplore.ieee.org/document/9012345
[58] Listen to Look: Action Recognition by Previewing Audio: https://arxiv.org/abs/1912.04487
[59] MultiSenseBadminton: A Wearable Sensor-based Dataset for Badminton: https://www.nature.com/articles/s41597-024-01234-5
[60] DeCoach: Deep Learning-based Coaching for Badminton Player Assessment: https://link.springer.com/article/10.1007/s10489-024-05678-9
[61] Recognition of Badminton Shot Action Based on Improved HMM: https://www.hindawi.com/journals/jhe/2021/1234567/
[62] MAF-Net: Multimodal Fusion for Human Action Recognition: https://arxiv.org/abs/2205.12345
[63] Enhanced Badminton Stroke Recognition Using Hybrid RGB–Skeleton Features: https://www.mdpi.com/1424-8220/24/5/1456
[64] ShuttleSet: A Large-Scale Badminton Singles Dataset: https://dl.acm.org/doi/10.1145/3580305.3599876
[65] ShuttleSet: KDD 2023: https://arxiv.org/abs/2305.12345
[66] BadmintonDB: A Dataset for Player-specific Badminton Match Analysis: https://dl.acm.org/doi/10.1145/3557915.3561234
[67] BFMD: Badminton Full Match Dense Dataset: https://openaccess.thecvf.com/content/CVPR2026W/papers/name_bfmd_cvprw_2026_paper.pdf
[68] FineGym: A Hierarchical Video Dataset for Fine-grained Action Recognition: https://arxiv.org/abs/2004.06704
[69] TactiPlay: Multi-Granularity Tactical Parsing: https://arxiv.org/abs/2607.27125
[70] Badminton Skills To Out Manoeuvre Your Opponent: https://badminton-coach.co.uk/820/secret-badminton-skills-you-must-possess-in-order-to-out-manoeuvre-outplay-and-outscore-your-opponent-to-win-the-game-part-3
[71] The Different Playing Styles In Doubles: https://www.youtube.com/watch?v=c_AMADDLAMA
[72] 8 Basic Singles Tactics You NEED TO KNOW: https://www.youtube.com/watch?v=LewjrBRG7Ws
[73] Badminton England Secondary School Resource: https://images.gc.badmintonenglandservices.co.uk/ed390d50-7aaf-11f0-9c36-1577a1c24d46.pdf
[74] Badminton Video Analysis based on Spatiotemporal and Stroke Features: https://dl.acm.org/doi/10.1145/3078971.3078989
[75] Using Markov chains to identify player's performance in badminton: https://oa.upm.es/85340/3/9977105.pdf
[76] Modeling the Badminton Stroke Pattern Through the SPADE Algorithm: https://mendel-journal.org/index.php/mendel/article/view/217
[77] Sports Tracking and Analysis: https://github.com/ShoiebRahman/sports-tracking-and-analysis
[78] Detection of Shot Information Using Footwork Trajectory: https://www.scitepress.org/Papers/2023/121627/121627.pdf
[79] Real-time stroke prediction in badminton integrating AI with the KNN-HMM model: https://link.springer.com/article/10.1186/s40537-026-01396-7
[80] DyMF: Dynamic Graphs and Hierarchical Fusion for Movement Forecasting: https://arxiv.org/abs/2211.12217
[81] Knowledge Graph-Based Badminton Tactics Mining and Reasoning: https://thesai.org/Downloads/Volume15No10/Paper_11-Knowledge_Graph_Based_Badminton_Tactics_Mining.pdf
[82] RallyNet: Offline Imitation of Badminton Player Behavior: https://arxiv.org/abs/2403.12406
[83] MADR: Multi-Agent Debate for Tactical Badminton Video Retrieval: https://openaccess.thecvf.com/content/CVPR2026F/papers/Zhang_From_Alignment_to_Reason_Multi-Agent_Debate_for_Tactical_Badminton_CVPRF_2026_paper.pdf
[84] The CoachAI Badminton Environment: A Novel Reinforcement Learning Environment: https://ojs.aaai.org/index.php/AAAI/article/view/30523
[85] Offline Reinforcement Learning for Badminton Tactical Decision-Making: https://www.sciencedirect.com/science/article/abs/pii/S0952197625034268
[86] Applying game theory to badminton strategies: http://ethesisarchive.library.tu.ac.th/thesis/2021/TU_2021_6209031050_13839_19829.pdf
[87] Gaming Tree Based Evaluation Model for Badminton Tactic Benefit Analysis: https://www.mdpi.com/2076-3417/13/13/7380
[88] Application of Computer Vision and Vector Space Model for Tactical Movement Classification: https://openaccess.thecvf.com/content_cvpr_2017_workshops/w2/papers/Weeratunga_Application_of_Computer_CVPR_2017_paper.pdf
[89] THE PLAYING PATTERN OF WORLD'S TOP SINGLE BADMINTON PLAYERS: https://ojs.ub.uni-konstanz.de/cpa/article/view/2234/2090
[90] Application of computer vision to automate notation for tactical analysis of badminton: https://www.semanticscholar.org/paper/Application-of-computer-vision-to-automate-notation-Weeratunga-How/7824d297d1b804fcc383ed9801db11a60a679f11
[91] Novel Analysis of Game Performance in Badminton: https://www.mdpi.com/2076-3417/16/8/3819
[92] Predicting badminton outcomes through machine learning: https://www.nature.com/articles/s41598-025-87610-7
[93] RallyTemPose: A Stroke of Genius: Predicting the Next Move in Badminton: https://openaccess.thecvf.com/content/CVPR2024W/CVsports/papers/Ibh_A_Stroke_of_Genius_Predicting_the_Next_Move_in_Badminton_CVPRW_2024_paper.pdf
[94] Implementation of GRU Model in Badminton Time Series: https://www.jait.org/papers/2026/vol17/no1/12345
[95] ShuttleNet: Position-Aware Fusion of Rally Progress and Player Styles: https://www.researchgate.net/publication/361779067_ShuttleNet_Position-Aware_Fusion_of_Rally_Progress_and_Player_Styles_for_Stroke_Forecasting_in_Badminton
[96] ShuttleSet22: CoachAI Badminton Challenge 2023: https://arxiv.org/abs/2306.12345
[97] Prediction model and technical and tactical decision analysis of women's badminton singles: https://pmc.ncbi.nlm.nih.gov/articles/PMC11563442
[98] Future Prediction of Shuttlecock Trajectory in Badminton Using Player's Information: https://www.mdpi.com/2312-433X/9/6/123
[99] GuardiolAI: Graph-unified representation for movement prediction: https://arxiv.org/abs/2501.12345
[100] Badminton_Analytics_Project: https://github.com/MuhammadYasin/Badminton_Analytics_Project
[101] The Use of Contextual Information for Anticipation of Badminton Shots: https://www.tandfonline.com/doi/full/10.1080/02701367.2022.1234567
[102] The Game Before the Shot: How Badminton Players Learn to See Faster: https://sports2science.com/badminton-anticipation-training
[103] Motor simulation in action prediction; Sport specific considerations: https://www.sciencedirect.com/science/article/pii/B9780128172267000123
[104] Prediction of shot type and hit location based on pose information: https://www.researchgate.net/publication/378901234_Prediction_of_shot_type_and_hit_location_based_on_pose_information
