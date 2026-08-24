# Comprehensive Research Report: Analysis and Study of Singles Badminton Player Actions Using Sports Videos

## Introduction

This report synthesizes state-of-the-art research across four interconnected components for analyzing singles badminton player actions from sports videos: (1) object detection and tracking, (2) technical action recognition, (3) tactical intent recognition, and (4) subsequent-action prediction. For each component, the report covers influential methods published in reputable venues (2020–2026), public datasets and benchmarks, key challenges specific to singles badminton, and recommended approaches for implementation. The research draws on foundational work in computer vision, action recognition, sequence modeling, and sports analytics, with particular emphasis on the ShuttleSet/CoachAI ecosystem that has become the de facto standard substrate for badminton analytics research.

---

## Component 1: Object Detection and Tracking within Badminton Videos

### 1.1 Player Detection

**YOLO-family detectors** are the dominant practical choice for real-time badminton player detection. Cheng & Kim (2023) demonstrated that YOLOv5 improves performance when trained on generalized video data, particularly when judges or other non-player figures appear in the background [1]. A more sophisticated pipeline by He & Zhang (2024) combined an improved Tiny YOLOv2 (with added convolutional layers, residual connections, and a revised loss incorporating trajectory information) with an Unscented Kalman Filter for shuttlecock position prediction, achieving 91.40% average tracking accuracy, 87.68% F1, and an IoU of 0.922 on ~1,000 stereo-vision frames [2]. Wu et al. (2025) proposed an enhanced YOLOv8-Pose architecture integrating the Efficient Local Attention (ELA) mechanism, evaluated on the xBHPE dataset of 4,000 Kinect-captured samples with a 21-keypoint skeleton model; the ELA-enhanced lightweight variant consistently outperformed baselines on MSE, OKS, and PCK metrics [3]. For multi-class detection, a Roboflow model combining "player" and "shuttlecock" classes across broadcast and ground-level views (1,022 images at 1920×1080) demonstrates the feasibility of unified detection [4].

**Faster R-CNN** remains a strong baseline. Rahmad et al. (2019) showed that Faster R-CNN detects players reliably when fed a generalized dataset [5]. A Heliyon 2022 study used Faster R-CNN with a VGG16 backbone to detect players' shoes in 2D, then converted to 3D world coordinates via homography and binocular positioning, achieving mAP 0.982 and 74.7% final positioning accuracy — a compelling approach for footwork analysis [6].

**Transformer-based detectors** are emerging for crowded/occluded scenes. DETR (2020) treats detection as direct set prediction with learned object queries, eliminating anchors and NMS; Deformable DETR (ICLR 2021) improves small-object performance and converges 10× faster via sparse attention over key sampling points [7][8]. Real-time variants such as RT-DETR now rival YOLO speed-accuracy trade-offs (RT-DETR-R50 achieves 53.1% AP at 108 FPS vs. YOLOv8-L's 52.9% AP at 71 FPS) [7].

### 1.2 Multi-Object Tracking

The tracking-by-detection paradigm dominates. The four-stage pipeline (detection → Kalman motion prediction → cost-matrix association via Hungarian algorithm → track lifecycle management) is standard, with the maxim that "detector quality dominates everything downstream" [9].

Key algorithms benchmarked on sports data:

- **DeepSORT** (2017): Introduced deep appearance embeddings (cosine distance); now considered a historical reference [9].
- **ByteTrack** (ECCV 2022): Associates every detection box, including low-confidence ones, via a two-stage cascade. Achieves MOT17 HOTA 63.1, runs ~2× faster than DeepSORT, and ships in Ultralytics YOLO as the `bytetrack.yaml` default. It is "the 2026 throughput default" [9][10].
- **OC-SORT** (CVPR 2023): Fixes Kalman drift after occlusion via observation-centric re-update (ORU). Best for non-linear motion (DanceTrack, gymnastics, sports with direction changes); MOT17 HOTA 63.2 [9][11].
- **BoT-SORT** (2022): Adds camera-motion compensation (CMC) and Re-ID embeddings; MOT17 HOTA 65.0 — the default tracker in Ultralytics since 2024. Recommended when the camera moves [9].
- **C-BIoU**: Buffered geometric matching without CMC; leads SoccerNet-tracking with HOTA 85.7 [12].
- **Deep HM-SORT** (arXiv 2406.12081): Sports-specific tracker combining feature-embedding and IoU costs via the harmonic mean (skewing toward the lower distance measurement — advantageous when players wear identical uniforms), and retaining all tracklets indefinitely for re-identification after leaving/re-entering the frame. Achieves 80.1 HOTA on SportsMOT and 85.4 HOTA on SoccerNet Tracking Challenge 2023 [13].

Tracker selection guidance: use BoT-SORT for moving cameras, OC-SORT for non-linear motion, ByteTrack for dense scenes and throughput, and BoT-SORT-ReID for long-occlusion identity persistence [9]. Tuning `track_buffer` and `match_thresh` on deployment data is critical; MOT17 defaults should not be left untouched [9].

### 1.3 Shuttlecock Detection and Trajectory Tracking

Shuttlecock tracking is the most challenging sub-problem: shuttlecocks reach top speeds of 493 km/h (the fastest ball type in sports), appear as small circles or triangles depending on camera angle, suffer severe motion blur, and blend with white court lines and backgrounds [14][15].

**TrackNet family** — the dominant approach:

- **TrackNet** (2019): VGG16 backbone with deconvolution layers; processes consecutive images to handle blur, afterimage, and short-term occlusion [16].
- **TrackNetV2** (ICPAI 2020): Improved speed from 2.6 to 31.8 FPS via a Multiple-In Multiple-Out (MIMO) design, real-valued 2D heatmaps, and weighted cross-entropy loss. Trained on 55,563 frames from 18 matches; achieves 96.3% training accuracy and 85.2% on unseen matches [17][18].
- **TrackNetV3** (ACM MM 2023): Adds trajectory prediction and rectification modules, using an estimated background as auxiliary data, mixup augmentation, repair masks, and inpainting for occlusion. Achieves 97.51% accuracy, 99.33% recall, and 98.56% F1 on the Shuttlecock Trajectory Dataset test split — best overall among YOLOv7, TrackNetV2, and TrackNetV3 [19].
- **TrackNetV4** (2025): Fuses high-level visual features with learnable motion attention maps [17].

**MonoTrack** (CVPRW 2022) is the first complete end-to-end system for 3D shuttle trajectory extraction from monocular badminton videos. It integrates court detection (Hough lines + bipartite graph partition), shuttle detection (modified U-Net), a two-layer GRU HitNet for hit-event detection fusing court/pose/shuttle cues with dynamic programming, and per-shot 3D trajectory optimization using drag dynamics and camera reprojection. Synthetic 3D error reaches 8.0 cm with full priors; HitNet F1 improves from 0.815 (shuttle-only) to 0.946 with all cues [20][21].

**Hybrid real-time systems**: Spyrosoft's instant review system and Kopania et al.'s BWF-verified system (Sensors 2022) combine fast differential-frame detection with modified Tiny YOLO fallback, adaptive pixel-wise flicker compensation, Kalman filtering, and blob analysis. The Warsaw system processed two cameras at up to 200 FPS (800×600) on commodity hardware, achieving 94% shuttlecock visibility detection and 81% of visible shuttlecocks correctly tracked within 12 pixels — comparable to Hawk-Eye in accuracy but easier to install [14][15]. For egocentric/robot views, Tuna & Hutter (2026) fine-tuned YOLOv8 on a 20,510-frame egocentric dataset, achieving F1 0.86 in similar environments and 0.70 in unseen environments, with performance degrading when the shuttlecock is smaller than ~20 pixels [22].

**Event cameras** offer a radical alternative: Wang et al. (2026) fused event optical flow (iniVation DAVIS346), high-speed RGB (240 fps), and IMU (500 Hz) via an Extended Kalman Filter to reconstruct smash trajectories with MAE 8.34 mm at 82 FPS — a 42.3% error reduction over traditional optical flow [23].

### 1.4 Court Line Detection and Homography

Court detection approaches fall into three families:

1. **Classical Hough-based methods**: Thresholding white pixels + Hough transform + homography. Reliable on clean broadcast courts but slow (up to 15 s/image) and unstable across court types and amateur venues [24][25].

2. **Deep keypoint detection**: TennisCourtDetector (272-star GitHub) uses a TrackNet-like heatmap network detecting 14 court keypoints (+1 center point), with classical CV postprocessing (keypoint refinement via white-pixel line intersection, homography reconstruction of shifted keypoints). Precision reaches 0.963 with full postprocessing on 8,841 tennis images [26]. ML6's study found MobileNetv3Small the best backbone (~100 FPS) and that predicting only 4 outer keypoints yields results similar to 16 [27].

3. **Semantic segmentation + homography**: Jouini et al. combine DeepLabV3Plus (ResNet-50 encoder) with erosion/dilation postprocessing, linear/PCA regression for line fitting, and RANSAC+DLT homography, achieving badminton IoU 0.781 (vs. 0.727 for KaliCalib) with 0.404 s latency [28]. **CourtKeyNet** (Machine Learning with Applications, 2026) is the first domain-specific badminton court detector, introducing octave feature extraction, polar transform attention, hybrid heatmap+regression keypoint localization, and a geometric consistency loss; it outperforms general-purpose keypoint detectors on KLA@0.05 across varying lighting [29]. For amateur courts, shadow removal (MTMT + ShadowFormer), YOLO net detection, and dominant-color pixel filtering improve robustness substantially [30].

### 1.5 Public Datasets and Benchmarks

| Dataset | Content | Size | Source |
|---|---|---|---|
| Shuttlecock Trajectory Dataset | 26 broadcast singles videos (23 pro + 3 amateur), frame-level shuttlecock coordinates | 78,200 frames, 1280×720@30fps | [31] |
| SportsMOT (ICCV 2023) | Basketball, volleyball, football; fast motion, similar appearances | 240 videos, 720p@25fps | [32][33] |
| TeamTrack (2024) | Soccer, basketball, handball; drone + fisheye views | 155.5 min, 4.37M boxes, 4K–8K | [34] |
| MOT17 / MOT20 | Pedestrian tracking (up to 246 pedestrians/frame) | 7 / 8 sequences | [35] |
| DanceTrack | Dancers, uniform appearance, diverse motion | ~100 videos | [9] |
| TennisCourtDetector dataset | Tennis court keypoints | 8,841 images | [26] |
| xBHPE | Badminton pose, 21-keypoint skeleton, 4 camera angles | 4,000 images | [3] |
| Badminton Player Tracking (Roboflow) | Single-class player detection | 1,033 images | [4] |

### 1.6 Evaluation Metrics

- **HOTA** (√(DetA × AssA)): The field's ranking metric for MOT — "if you read only one number from a tracker comparison, read HOTA" [9][12].
- **MOTA / MOTP / IDF1**: CLEAR metrics; MOTA underweights identity switches, IDF1 overcorrects [9].
- **mAP@50 / Precision / Recall**: For detection models (e.g., 98.3% mAP@50 for player tracking) [4].
- **Distance-based metrics**: True Positive if Euclidean distance between predicted and ground-truth center within τ=25 pixels (for small-object detection) [22]; positioning error of 5 pixels spec for ball detection [24].
- **ADE / FDE**: Average/Final Displacement Error in pixels for trajectory prediction [36].
- **KLA@0.05, IoU**: Keypoint localization accuracy and court detection IoU [26][29].

### 1.7 Key Challenges Specific to Singles Badminton

1. **Small, fast, blurred shuttlecock**: 493 km/h top speed; 2–12 pixel diameters in broadcast video; motion blur and afterimages [14][15][37].
2. **Occlusion**: Player-player occlusion, shuttlecock occlusion, and full occlusion (the most difficult attribute in sports MOT) [33][37].
3. **Camera viewpoint variability**: Broadcast (elevated, TV-style) vs. fixed courtside vs. ground-level mobile views; amateur venues with low angles, scuffed courts, and shadows [4][22][30].
4. **Similar player appearances**: Identical uniforms make appearance-based Re-ID unreliable; sports Re-ID feature spaces are "somewhat fused" [13][33].
5. **Court line occlusion**: Players and shadows obscure court lines; illumination varies [28][30].

### 1.8 Recommended Approaches and Research Directions

- **Pipeline**: YOLOv8/YOLOv8-Pose (with attention mechanisms like ELA) for real-time player detection and pose [3]; ByteTrack or BoT-SORT for tracking depending on camera motion [9]; TrackNetV3 for shuttlecock detection [19]; deep keypoint or segmentation-based court detection [26][28][29].
- **Fusion**: Combine trajectory-based hit detection with swing-action detection via a Shot Refinement Algorithm — Hsu et al. improved shot detection from 58.8% (TrackNet alone) to 89.7% accuracy by fusing TrackNet trajectories with YOLOv7 swing detection across five error scenarios [37].
- **Physics-constrained 3D reconstruction** (MonoTrack-style) integrates court, pose, shuttle, and hit-event cues with drag dynamics for 3D trajectories [20][21].
- **Event cameras and multi-camera setups** are promising for high-speed swing reconstruction and robust 3D tracking [23][38].
- **Detector quality is paramount**: "a weak detector cannot be saved by a clever association step" [9].

---

## Component 2: Recognition of Technical Actions Performed by Singles Players

### 2.1 State-of-the-Art Methods

**Skeleton-based action recognition is the leading paradigm for fine-grained badminton stroke classification.** The VideoBadminton benchmark (arXiv 2403.12385; IEEE BigData 2024) provides the most direct evidence: on 18 BWF-aligned stroke classes from 7,822 self-recorded clips, skeleton-based methods outperformed all video-based methods — ST-GCN achieved 60.70% Top-1 and PoseC3D 59.98%, versus Swin 53.53%, TimeSformer 45.45%, R(2+1)D 40.84%, and SlowFast 12.28% [39][40].

**BST (Badminton Stroke-type Transformer)** (arXiv 2502.21085; CVPR 2026 CVsports) is the current state of the art. Its key innovation is the **Cross Transformer Layer with Multi-Head Cross Attention**, where K/V derive from the shuttlecock trajectory latent and Q from player pose/position latents — based on the argument that "deceptive player movements never misrepresent the actual stroke in the trajectory." Combined with a variable-width clipping strategy that captures complete shuttlecock trajectories in three stages (incoming, outgoing, opponent response), BST-3 achieves 77.10% accuracy and 70.42% Macro-F1 on ShuttleSet (35 categories), outperforming ST-GCN (72.8%), BlockGCN (71.5%), SkateFormer (71.2%), and ProtoGCN (72.3%). On TenniSet (6 classes) it reaches 99.23% accuracy; on BadmintonDB (18 classes) 65.17%. Notably, 2D poses outperform 3D poses (MotionBERT-derived) due to HPE model bias toward general human poses [41][42].

**TemPose-TF-ASF** (arXiv 2605.02558) extends the TemPose skeleton-based framework with bidirectional adjacent-stroke context fusion. A Two-Stage Contextual Refinement strategy avoids ground-truth future annotations: stage one generates preliminary predictions, stage two uses them as estimated adjacent-stroke context. Results: 85.4% accuracy and 76.1% Macro-F1 on ShuttleSet, improving the TemPose-TF baseline (83.5%/74.2%). The ASF module is backbone-agnostic, improving BlockGCN, SkateFormer, and BST-CG-AP consistently [43].

**MMAction2 skeleton model zoo** provides strong baselines: ST-GCN (NTU60 92.34% four-stream), STGCN++ (92.77%), PoseC3D (93.6% NTU60; 93.5% FineGym), and 2s-AGCN (92.34%). PoseC3D is notable for robustness to pose-estimation noise and cross-dataset generalization [44]. FineGym's findings are directly transferable: sparse sampling (3 frames) is insufficient for fine-grained recognition; motion features (optical flow) contribute more than appearance at fine granularities; temporal dynamics modeling (TRN/TSM) is crucial; and Kinetics pre-training is not always beneficial for fine-grained actions [45].

**Hybrid and alternative approaches**:

- **Weighted ensemble with pose features** (Asriani et al., 2024): SVM + LR + AdaBoost with 3D distances to right hip and Fast Dynamic Time Warping temporal features achieved 95.38% accuracy on badminton action recognition [46].
- **QCNN** (Scientific Reports 2025): Quantum convolutional kernels with arm angle as the most significant feature; F1 0.860 for backhand intercept [47].
- **Shot refinement via fusion** (Hsu et al., Sensors 2024): DensePose ankle projection + TrackNet + YOLOv7 swing detection with a five-case Shot Refinement Algorithm achieved 89.7% accuracy/91.3% recall on 69 BWF matches, 1,582 rallies; shot-type classification accuracy 72.1% at the strictest threshold [37].
- **Wearable IMU-based recognition** (Scientific Reports 2025): 1D-CNN on two wrist/racket IMUs achieved 97.16% for six stroke types and 86.07% for fifteen shot trajectories — relevant for ground-truth generation and multimodal fusion [48].
- **Table tennis transfer**: Kulkarni et al. (CVPRW 2021) achieved 99.37% validation accuracy on 11 table tennis strokes using HRNet 2D pose + TCN with only four joints (wrist, elbow, two shoulders), Savitzky-Golay filtering, and 100 standard time steps — strong evidence that minimal pose features suffice for racket sports [49]. Fujihara et al. (Sensors 2025) showed that decomposing strokes into two labels (posture + spin/velocity) improves table tennis test accuracy by up to 18.1%, and 3D joint coordinates outperform raw video [50].

### 2.2 Public Datasets and Benchmarks

| Dataset | Content | Size | Notes |
|---|---|---|---|
| VideoBadminton | 18 BWF-aligned stroke classes, self-recorded | 7,822 clips, 145 min, 19 players | Skeleton methods win; IEEE BigData 2024 [39][40] |
| ShuttleSet (KDD 2023) | Stroke-level singles, 18 shot types | 44 matches, 3,685 rallies, 36,492 strokes | De facto benchmark; 27 players [51] |
| ShuttleSet22 | Stroke-level singles 2022 | 35 players, 58 matches, 33,612 strokes | IJCAI 2024 demo [52] |
| BadmintonDB | Momota vs. Ginting singles | 9 matches, 811 rallies, 9,671 strokes | MMSports '22 [53] |
| CoachAI Challenge Track 1 | Broadcast BWF videos + 13 annotation fields | Rally-based, HitFrame ±2 frames | IJCAI 2023 [54] |
| TTStroke-21 | Table tennis, 20 stroke classes + rejection | 120×120×100 spatio-temporal samples | Transferable [55] |
| FineGym | Gymnastics, 530 element categories | 32,697 sub-action instances | Transferable fine-grained insights [45] |
| MultiSenseBadminton | IMU/EMG/insole + camera | 23 hours, 25 players, 7,763 swings | Wearable ground truth [56] |
| Mendeley frame-level badminton | 884 recordings, frame-level | Multiple viewing angles | [57] |

### 2.3 Evaluation Approaches

- **Top-1/Top-5 accuracy and Mean Class Accuracy**: VideoBadminton benchmark protocol [39].
- **Confusion matrices for similar strokes**: Essential for distinguishing smash vs. wrist smash, lift vs. net tumble [41][48].
- **Macro-F1 and Acc-2**: BST and TemPose-TF-ASF report Macro-F1 and binary accuracy for stroke categories [41][43].
- **Rally-based scoring with strict HitFrame tolerance (±2 frames)**: CoachAI Challenge protocol [54].
- **Per-class accuracy and global accuracy**: MediaEval TTStroke-21 protocol [55].
- **Temporal action localization (mAP@tIoU)**: FineGym reports sub-action mAP@tIoU of 9.6 vs. action-level 49.4 — localization is far harder than classification [45].

### 2.4 Key Challenges Specific to Singles Badminton

1. **Fine-grained distinctions between visually similar strokes**: Smash vs. wrist smash, defensive return drive (worst recall in BST), lift vs. net tumble [41][51].
2. **Extreme shuttlecock speed**: Smash actions exceed 100 m/s with durations of tens of milliseconds, causing motion blur [23].
3. **Short stroke duration and boundary ambiguity**: TTStroke-21 annotators required 25% overlap due to difficulty determining boundaries during fast exchanges [55].
4. **Pose estimation reliability**: Skeleton methods depend on accurate pose extraction; 3D pose lifting is unreliable for badminton-specific poses in ShuttleSet; Kinetics pre-training can hurt fine-grained performance [41][45][51].
5. **Class imbalance**: Rare categories (defensive return lob, driven flight, rush) and heavy-tailed element distributions [45][51].

### 2.5 Recommended Approaches

- **Use skeleton-based models (ST-GCN, PoseC3D, or transformer variants like BST) over raw video models** for fine-grained stroke classification [39][41].
- **Incorporate shuttlecock trajectory as a primary input** via cross-attention (BST's design), since trajectory encodes the true stroke outcome [41].
- **Model bidirectional adjacent-stroke context** (TemPose-TF-ASF) to exploit rally structure without ground-truth future annotations [43].
- **Preprocess pose keypoints with Savitzky-Golay filtering** (improved table tennis accuracy 97.74% → 99.37%) [49].
- **Use multi-label decomposition** (posture + spin/velocity labels) for fine-grained strokes [50].
- **Fine-tune on player-specific data**: left-handed player generalization improved from 38% to 99.22% after 2-epoch fine-tuning in table tennis [49].
- **Consider variable-width clipping around hit frames** (including opponent context strokes) rather than fixed-width clips [41].

---

## Component 3: Recognition of Tactical Intent Behind Singles Players' Actions

### 3.1 State-of-the-Art Methods

**ShuttleNet** (AAAI-22) is the foundational work on stroke forecasting and implicitly on tactical modeling. It formulates stroke forecasting as sequence prediction over alternating player strokes, addressing three challenges: mixed sequences, multiple outputs (shot type + area coordinates), and player dependence. The architecture has three components: a Transformer-based Rally Extractor with multi-head type-area-attention, a Transformer-based Player Extractor splitting the sequence by player, and a Position-Aware Gated Fusion Network combining rally and player contexts via information weights and learnable position weights. On 75 matches / 43,191 strokes, ShuttleNet outperformed all baselines (Seq2Seq, CF-LSTM, TF, dNRI, DMA-Nets) by at least 12.0% in CE and 3.4% in MSE [58][59]. The design principle — separate rally and player contexts, then fuse — is directly relevant to intent recognition because tactical intent depends on both the rally situation and player-specific style.

**BLSR** (ICDM-21; extended in ACM TIST 2022) addresses "How is the stroke?" — inferring shot influence via long short-term dependencies. Treating shots as words and rallies as sentences, it uses location embeddings, enhanced shot-type embeddings with temporal score learning, two per-player 1-D CNNs for local shot patterns, and a bidirectional GRU with attention. The attention mechanism provides interpretability on which shots matter most for rally outcome. Results: AUC 0.8966 and Brier 0.1329 on 15,742 shots from 1,409 rallies of 19 international men's singles matches [60][61]. This is the most direct prior work on *valuing* the tactical intent of individual strokes.

**DyMF** (AAAI-23) formalizes movement forecasting and introduces the Player Movements (PM) graph, transforming rallies into graphs with 12 strategic relation types (10 shot types + "defend" + "return" edges). The encoder-decoder architecture uses Relational GCN + Dynamic GCN (with LSTM-generated weights) for interaction styles and hierarchical fusion (player-player parallel co-attention; player-rally fusion). DyMF outperforms all baselines by up to 35.3% (MSE), 21.5% (MAE), and 24.3% (CE). A case study demonstrated that changing a player's defensive position alters the opponent's returned shot — direct evidence that positional intent shapes opponent behavior [62][63].

**RallyTemPose** (CVPRW 2024) is the first skeleton-based transformer for next-stroke prediction, with direct tactical implications. The encoder (Spatial Transformer + Grouped Pooling + Temporal Transformer with inter-player cross-attention and intra-player self-attention) produces latent variables for stroke and each player; the decoder uses adaptive cross-attention with BERT-embedded stroke descriptors. Ablations show player ground position is the most critical input (removing it drops performance 2.6%); removing keypoints drops accuracy to 48.3%. t-SNE analysis of latent variables reveals clear stroke-type groupings and partial player groupings; cosine similarity of player embeddings reveals playstyle differences (e.g., male vs. female players show lower similarity). Critically, average prediction accuracy varies by over 20% between best- and worst-predicted players, "potentially indicating how well players mask their strokes" — a direct quantitative handle on deception [64][65].

**Statistical and game-theoretic approaches**:

- **Gaming tree with Nash Equilibrium** (Applied Sciences 2023): Analyzed 29 Lin Dan vs. Lee Chong Wei matches (2006–2018) by constructing gaming trees over stroke techniques and 3×3 court zones. Found Lin's best choice was hitting to the backcourt while Lee's best strategy was controlling the forecourt; win/loss predictions matched actual results, and strategy diversity dropped in later career periods [66].
- **PLOS ONE 2024** (An Se-young): SVM with RBF kernel achieved 87.5% accuracy predicting scoring/losing outcomes from features including number of strikes, scoring/losing locations, and techniques in the last three strokes. PCA+K-means confirmed learnable intrinsic structure. Key finding: 60% of An's organized backcourt shots achieved points through lifts or high clears — an attack-via-defense tactical signature [67].
- **Scientific Reports 2025**: Random Forest on 23 technical action frequencies from 303 Super750+ matches achieved AUC 0.9726 (men, top-5 features: Net Front, Slice/Drop, Flat High, High, Push) and 0.8730 (women, top-22 features). SHAP analysis validated feature importance; higher Net Front frequency by the serving side correlated with increased win probability [68].
- **Tennis transfer — Wei & Lucey** (TKDE 2016): The seminal work on forecasting next shot location in tennis from Hawk-Eye spatiotemporal data, discovering unique player styles and predicting within-point events [69].
- **Tennis decision vs. execution decomposition** (Seidl et al., Tennis Australia): Four neural networks (xDW/xDR/xEW/xER) value decisions at the moment the ball leaves the racket and execution at the bounce, using 107,000 hits / 98,000 bounces from the 2020 Australian Open. This disentangles *what the player intended* from *how well they executed* — directly relevant to intent inference [70].
- **Tennis transformer** (Advanced Electromagnetics 2026): Six-layer Transformer encoder with multi-task learning on Match Charting Project shot sequences achieved Macro-F1 0.935 for tactical classification and AUC@5 0.923 for early round-outcome assessment [71].
- **Tennis GNN for intransitive dominance** (arXiv 2510.20454): MagNet with magnetic Laplacian on temporal directed graphs of match outcomes; graph structure carries most predictive signal (removing it raises Brier from 0.2142 to 0.2492) [72].

**Hidden Markov Models**: KNN-HMM (Journal of Big Data 2026) combines a KNN stroke classifier with an HMM (3–5 hidden states, Gaussian emissions, Baum-Welch training, Viterbi decoding) for real-time stroke prediction, achieving 94.6% internal / 93.4% external accuracy with 32 ms latency [73]. HMMs are the classic approach to modeling latent competitive states (momentum, tactical regimes) with interpretable transition matrices [74][75].

**Table tennis transfer**: A transformer-based dual encoder-decoder (MJSSM 2026) forecasting stroke type and landing zone from the "Intellectual Tactical System" database achieved top-1 accuracies of 57.2% (type) and 42.8% (zone), with top-5 of 98.2% and 91.8% [76].

### 3.2 Public Datasets and Benchmarks for Tactical Analysis

- **ShuttleSet** (KDD 2023): The largest public stroke-level badminton singles dataset — 44 broadcast matches (2018–2021), 104 sets, 3,685 rallies, 36,492 strokes, 27 top-ranked players. Four annotation categories per stroke: rally (scores, winner, lose reason), temporal (hitting time/frame), spatial (player positions, shuttle contact location, grid location, above/below net), and hitting (stroke status, backhand, around-head, shot type). Court coordinates via homography. Quality control: temporal MAE 0.24 frames, spatial MAE 0.18 (shuttle) / 0.86 (player). Native benchmarks: stroke influence (ShuttleScorer AUC 0.8371), stroke forecasting (ShuttleNet CE 2.4125), movement forecasting (DyMF CE 2.3146) [51][77][78]. Limitations: singles only, no fixed train/test split, no continuous shuttle trajectories, unreliable 3D pose lifting, class imbalance [51].
- **ShuttleSet22** (IJCAI 2024): Extends to 2022 matches — 35 players, 58 matches, 3,992 rallies, 33,612 strokes with official train/validation/test splits [52].
- **BadmintonDB** (MMSports '22): 9 matches, 811 rallies, 9,671 strokes between Momota and Ginting; used by RallyTemPose and others [53].
- **Tennis Match Charting Project**: Crowdsourced shot-by-shot data — 18,113 matches, 2.82M points, 10.67M shots as of 2025 [79][80].
- **Hawk-Eye data**: Proprietary ball trajectory + player feet movement data, accurate to ~2.6–3.6 mm, used in Wei & Lucey and Seidl et al. Not publicly available [81].
- **CoachAI Projects repository**: Official implementations of ShuttleNet, DyMF, Shot Influence, ShuttleSet, CoachAI Environment, and challenge code (MIT license) [82].

### 3.3 Key Challenges Specific to Singles Badminton

1. **Ambiguity of intent from visual evidence alone**: Badminton stroke forecasting is complicated by inherent unpredictability of player decisions, influenced by physical state, psychological condition, and tactical approach [64].
2. **Deception**: Deceptive shots use two-part motion — preparation identical to the expected shot, then a last-moment change. A shuttlecock takes 0.6 s to cross the court on a drive and 0.3 s on a full-power smash; deception adds 0.1–0.2 s to opponent reaction time. Experts respond by waiting longer for deceptive movements [83][84][85]. Since early visual cues are deliberately misleading, intent cannot be read from kinematics alone; the model must account for the opponent's belief state and game context.
3. **Multi-modal fusion is necessary but complex**: RallyTemPose showed player ground position is the single most critical input; Nokihara et al. showed posture + position + trajectory fusion improves shuttle trajectory prediction ADE by ~13% over shuttle-only [36][64].
4. **Scoreboard masking**: A player can win the same number of points yet lose the match; the scoreboard masks decision vs. execution quality, motivating shot-level valuation [70].
5. **Data availability asymmetry**: Hawk-Eye-quality spatiotemporal data is proprietary; public datasets are either crowdsourced categorical (Match Charting Project) or broadcast-derived with limited spatial precision (ShuttleSet) [51][79].
6. **Limited annotated tactical labels**: ShuttleSet required six trained expert annotators; RallyTemPose authors explicitly call for synthetic data "for a field with sparse quality annotated datasets" [51][64].

### 3.4 Recommended Approaches

- **Model rally context and player style separately, then fuse** (ShuttleNet's PGFN design) [58].
- **Use attention-based sequence models for interpretable shot influence** (BLSR's attention over per-player CNN patterns) [60].
- **Explicitly model player-player interactions as graphs** (DyMF's PM graph with defend/return edges; relational + dynamic GCNs) [62].
- **Fuse skeleton poses, court positions, player embeddings, and shuttlecock trajectories** (RallyTemPose-style) [64].
- **Decompose decision from execution** (Seidl et al.'s xDW/xDR/xEW/xER framework) to separate tactical intent from skill [70].
- **Incorporate game-situation context** (score, fatigue, serve direction counts, prior shot patterns): tennis serve-direction prediction showed cumulative serve direction counts and fatigue (run index) are the most important features, providing indirect evidence of mixed-strategy play [86].
- **Use HMM/regime-switching models for latent tactical states** (momentum, attack/defense phases) with interpretable transitions [73][74].
- **Leverage the CoachAI Badminton Environment** (AAAI-24): an RL environment integrating ShuttleNet + DyMF + Behavior Cloning as realistic opponents within an MDP/OpenAI Gym framework, enabling strategy evaluation — e.g., a PPO agent shifted its movement distribution after serves and achieved a 60% win-rate increase [87][88].

---

## Component 4: Prediction of Singles Players' Subsequent Actions

### 4.1 State-of-the-Art Methods

**Next-shot prediction (stroke forecasting)** is the core task, formalized by ShuttleNet (AAAI-22) as: given an observed sequence of strokes (shot type + area coordinates), predict the next strokes' types and landing coordinates. On ShuttleSet, ShuttleNet achieves CE 2.4125, MSE 1.8121, MAE 1.3582 at τ=8 observed strokes [58][59]. The **CoachAI Badminton Challenge at IJCAI 2023** (Track 2) made this task concrete: given τ=4 observed strokes, predict future strokes; evaluation uses cross-entropy for shot type and MAE for area coordinates, with 6 predicted sequences per rally. The winning team (Intro_to_AI_team8) achieved total 2.5776 (CE 1.7892, MAE 0.7884) vs. the ShuttleNet baseline 2.8774; 11 of 16 teams beat the baseline. Most improvements came in shot-type prediction (2.1777 → 1.7892); area-coordinate prediction barely improved (0.6997 → 0.6797), highlighting the difficulty of jointly predicting type and location [52][89].

**RallyTemPose** (CVPRW 2024) predicts the next stroke from skeleton poses, court positions, and player-specific embeddings using a transformer encoder-decoder with adaptive cross-attention. Results: 54.3% top-1 / 77.3% top-2 / 92.5% top-3 accuracy on ShuttleSet; 62.8% / 83.5% / 93.1% on BadmintonDB. The 20%+ variation in per-player prediction accuracy suggests measurable stroke-masking (deception) [64][65].

**Movement forecasting** — DyMF (AAAI-23) predicts both players' future locations and shot types, outperforming all baselines by up to 35.3% (MSE), 21.5% (MAE), and 24.3% (CE). Its graph formulation (PM graph with 12 strategic relation types) captures movement purposes and dynamic tactics [62][63].

**Shuttlecock trajectory prediction** — Nokihara et al. (J. Imaging 2023; VISAPP 2023) was the first work on future shuttlecock trajectory prediction during rallies. Fusing shuttlecock position (2D), player positions (4D), and player postures (68D) into a 6D feature vector fed to a 3-layer LSTM improved ADE by ~13% over shuttle-only methods and ~8.4% over shuttle+position. The LSTM outperformed RNN (+9.8% ADE), GRU (+5.0%), Transformer (+20%), and Seq2Seq (+12%). Best configuration: 4 input frames / 12 output frames with 50% left-right flip + 50-pixel translation augmentation, achieving ADE 0.04908 and FDE 0.08391. Notably, accuracy improves with more input frames and fewer prediction frames (12-in/4-out: ADE 0.02054) [36][90].

**Early action prediction and anticipation** — In tennis, Wei & Lucey (TKDE 2016) predicted next shot location from Hawk-Eye spatiotemporal data, discovering unique player styles [69]. Serve-direction prediction with Match Charting Project data achieved ~49% (men) / ~44% (women) accuracy on six serve directions, with cumulative serve-direction counts and server fatigue as the most important features — indirect evidence of mixed-strategy play [86]. In badminton, the KNN-HMM (Journal of Big Data 2026) achieved 94.6% accuracy with 32 ms latency for real-time stroke classification, demonstrating practical streaming prediction [73].

**RL for strategic play** — The CoachAI Badminton Environment (AAAI-24) provides an MDP/OpenAI Gym framework with realistic opponents (ShuttleNet + DyMF + Behavior Cloning), enabling agents to learn shot selection strategies. A PPO agent achieved a 60% win-rate increase by shifting its movement distribution after serves [87][88].

### 4.2 Datasets and Benchmarks

- **ShuttleSet / ShuttleSet22**: The primary benchmark for stroke forecasting and movement forecasting (see Component 3.2) [51][52].
- **CoachAI Challenge IJCAI 2023 Track 2**: Standardized evaluation protocol with CE + MAE metrics and 6-sequence sampling [52][89].
- **BadmintonDB**: Used by RallyTemPose for cross-dataset evaluation [53].
- **Shuttlecock Trajectory Dataset**: 26 training + 3 test matches for trajectory prediction [31].
- **Tennis Match Charting Project**: 10.67M shots for transferable next-shot prediction [79][80].

### 4.3 Key Challenges

1. **Joint prediction of shot type and location**: The CoachAI Challenge showed that integrating type and area prediction is the hardest part — most teams were inferior to baseline on MAE [52][89].
2. **Inherent unpredictability**: Badminton stroke decisions are influenced by physical state, psychological condition, and tactical approach, making probabilistic forecasting fundamentally hard [64].
3. **Deception and stroke-masking**: Players deliberately delay revealing intent; per-player prediction accuracy varies by over 20%, and models struggle with deceptive players [64][83].
4. **Temporal sensitivity**: HitFrame must be within 2 frames in the CoachAI protocol; shuttlecock trajectories change suddenly at hit-back and floor-touch moments [36][54].
5. **Sparse quality annotations**: Limited annotated rally data; authors call for synthetic data generation [64].

### 4.4 Recommended Approaches

- **Transformer-based sequence models with separated player/rally contexts** (ShuttleNet architecture) as the backbone for stroke forecasting [58].
- **Graph-based movement modeling** (DyMF) for predicting player positions, since positional intent constrains opponent responses [62].
- **Skeleton + position + trajectory multimodal fusion** (RallyTemPose, Nokihara et al.) [36][64].
- **Bidirectional adjacent-stroke context** (TemPose-TF-ASF's TSCR strategy) to leverage future strokes without ground-truth leakage at inference [43].
- **Probabilistic outputs**: Model area coordinates as bivariate Gaussian distributions (ShuttleNet/DyMF approach) to capture uncertainty [58][62].
- **Reinforcement learning environments** (CoachAI Environment) for evaluating and training predictive/strategic agents [87].
- **Deception-aware modeling**: Explicitly represent temporal kinematics up to contact, model the opponent's belief state, and incorporate game-situation context (score, fatigue, prior patterns) [83][86].

---

## Cross-Component Integration and Overall Recommendations

The four components form a natural pipeline: (1) detect and track players, shuttlecock, and court → (2) recognize the technical stroke executed → (3) infer the tactical intent behind it → (4) predict the next action. The research reveals several cross-cutting principles:

1. **A unified pipeline is achievable but requires careful fusion**. MonoTrack demonstrates end-to-end integration of court, pose, shuttle, and hit-event cues; Hsu et al.'s Shot Refinement Algorithm shows how trajectory-based and action-based detections correct each other's errors [20][37]. The BST model shows that shuttlecock trajectory should be a primary input for stroke classification, not an auxiliary cue [41].

2. **ShuttleSet is the common substrate**. The KDD 2023 dataset has enabled otherwise disconnected research threads — forecasting (ShuttleNet), recognition (BST), movement prediction (DyMF), and report generation — to operate on shared data with comparable metrics [51]. Its limitations (no continuous trajectories, no fixed splits, singles-only) should be addressed by future dataset work.

3. **Skeleton-based representations outperform raw video for fine-grained badminton analysis** across all benchmarks, but 2D poses from sport-appropriate HPE models are preferable to 3D lifting [39][41][49].

4. **Context is everything for intent and prediction**. Player ground position is the single most critical input for next-stroke prediction; rally context, player style, score, and fatigue all shape tactical decisions [64][86]. Models should separate rally and player contexts and fuse them with position-aware gating (ShuttleNet's design) [58].

5. **Evaluation should be multi-metric and decompositional**. HOTA for tracking, Top-1/Macro-F1 for classification, CE+MAE for forecasting, ADE/FDE for trajectories, and AUC/Brier for outcome prediction. Decision vs. execution decomposition (Seidl et al.) should be adopted for intent analysis [70].

6. **Practical recommendations by component**:
   - **Detection/tracking**: YOLOv8-Pose + ByteTrack/BoT-SORT + TrackNetV3 + deep keypoint court detection [3][9][19][26].
   - **Technical recognition**: BST-style cross-attention transformer with 2D pose + shuttlecock trajectory [41]; add bidirectional stroke context [43].
   - **Tactical intent**: BLSR-style interpretable shot influence + DyMF-style graph interaction modeling + game-situation features [60][62][86].
   - **Next-action prediction**: ShuttleNet-style transformer forecasting with bivariate Gaussian outputs, extended with RallyTemPose-style multimodal encoder [58][64].

---

## Sources

[1] AI-powered Badminton Video Detection (Cheng & Kim, 2023): https://www.semanticscholar.org/paper/AI-powered-Badminton-Video-Detection%3A-Enhancing-and-Cheng-Kim/08aadf8b7360dc1d7bf0ed3f4b7ff708dae90066

[2] Deep learning neural network-assisted badminton movement recognition (He & Zhang, Heliyon 2024): https://pmc.ncbi.nlm.nih.gov/articles/PMC11620146

[3] Enhanced Pose Estimation for Badminton Players (Wu et al., Sensors 2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12298368

[4] badminton-players-detection (Roboflow): https://universe.roboflow.com/hongy20/badminton-players-detection-gwgb1

[5] Badminton player detection using faster region CNN (Rahmad et al., 2019): https://www.semanticscholar.org/paper/Badminton-player-detection-using-faster-region-Rahmad-Sufri/2c577fbb6a33a9a82fafe8302b78e932fef855ea

[6] Vision-based movement recognition reveals badminton footwork (Heliyon 2022): https://shura.shu.ac.uk/30683/1/PIIS2405844022013779.pdf

[7] Introduction to DETR (Detection Transformers): https://www.lightly.ai/blog/detr

[8] Deformable DETR (arXiv 2010.04159): https://arxiv.org/abs/2010.04159

[9] Multi-Object Tracking — DeepSORT, ByteTrack, OC-SORT, BoT-SORT (Fora Soft): https://www.forasoft.com/learn/ai-for-video-engineering/articles-ai/multi-object-tracking-deepsort-bytetrack-ocsort

[10] Introduction to BYTETrack: https://datature.com/blog/introduction-to-bytetrack-multi-object-tracking-by-associating-every-detection-box

[11] OC-SORT GitHub (CVPR 2023): https://github.com/noahcao/OC_SORT

[12] SORT vs ByteTrack vs OC-SORT vs BoT-SORT vs C-BIoU (Roboflow Trackers): https://trackers.roboflow.com/latest/trackers/comparison

[13] Deep HM-SORT (arXiv 2406.12081): https://arxiv.org/html/2406.12081v1

[14] Instant Review System for Badminton (Spyrosoft): https://spyro-soft.com/blog/artificial-intelligence-machine-learning/instant-review-system-for-badminton-computer-vision-use-case

[15] Automatic Shuttlecock Fall Detection System (Kopania et al., Sensors 2022): https://pmc.ncbi.nlm.nih.gov/articles/PMC9655598

[16] Enhancing Badminton Game Analysis (Hsu et al., Sensors 2024): https://www.mdpi.com/1424-8220/24/13/4372

[17] TrackNetV2 (Semantic Scholar): https://www.semanticscholar.org/paper/TrackNetV2%3A-Efficient-Shuttlecock-Tracking-Network-Sun-Lin/223c287d516284fec9bd9792ca2805aa0f551fc9

[18] TrackNetV2 (HyperAI): https://hyper.ai/en/papers/tracknetv2-efficient-shuttlecock-tracking

[19] TrackNetV3 (GitHub): https://github.com/qaz812345/TrackNetV3

[20] MonoTrack (arXiv 2204.01899): https://arxiv.org/abs/2204.01899

[21] MonoTrack (GitHub): https://github.com/jhwang7628/monotrack

[22] One-Shot Badminton Shuttle Detection for Mobile Robots (Tuna & Hutter, 2026): https://www.alphaxiv.org/abs/2603.06691

[23] Fine reconstruction of badminton swing dynamic trajectory assisted by event camera (Scientific Reports 2026): https://www.nature.com/articles/s41598-026-46443-8

[24] Tennis Analysis Using Deep Learning (Medium): https://medium.com/@kosolapov.aetp/tennis-analysis-using-deep-learning-and-machine-learning-a5a74db7e2ee

[25] Improving Tennis Court Line Detection with ML (ML6): https://www.ml6.eu/en/blog/improving-tennis-court-line-detection-with-machine-learning

[26] TennisCourtDetector (GitHub): https://github.com/yastrebksv/TennisCourtDetector

[27] Improving Tennis Court Line Detection with ML (ML6, full): https://www.ml6.eu/en/blog/improving-tennis-court-line-detection-with-machine-learning

[28] A Deep Learning-Based Framework for Racket Sports Court Registration (Jouini et al.): https://openreview.net/pdf/01b2e7445170ebd4328ed615e1196d4ce6b880ef.pdf

[29] CourtKeyNet (Machine Learning with Applications 2026): https://www.sciencedirect.com/science/article/pii/S2666827026000496

[30] Accurate Tennis Court Line Detection on Amateur Recorded Matches (arXiv 2404.06977): https://arxiv.org/pdf/2404.06977

[31] Shuttlecock Trajectory Dataset (HackMD): https://hackmd.io/@TUIK/rJkRW54cU

[32] SportsMOT Challenge (DeeperAction@ECCV 2022): https://deeperaction.github.io/tracks/sportsmot.html

[33] SportsMOT Presentation (YouTube): https://www.youtube.com/watch?v=IpjsXa8_akM

[34] TeamTrack (GitHub): https://github.com/AtomScott/TeamTrack

[35] MOT20 Benchmark: https://www.scribd.com/document/535775898/MOT20

[36] Future Prediction of Shuttlecock Trajectory in Badminton Using Player's Information (Nokihara et al., J. Imaging 2023): https://www.mdpi.com/2313-433X/9/5/99

[37] Enhancing Badminton Game Analysis: Shot Refinement (Sensors 2024, PMC): https://pmc.ncbi.nlm.nih.gov/articles/PMC11244353

[38] Tracking Players in a Badminton Court by Two Cameras (arXiv 2308.04872): https://arxiv.org/abs/2308.04872

[39] Benchmarking Badminton Action Recognition with a New Fine-Grained Dataset (VideoBadminton, arXiv 2403.12385): https://arxiv.org/html/2403.12385v2

[40] VideoBadminton: A Video Dataset for Badminton Action Recognition (IEEE BigData 2024): https://www.computer.org/csdl/proceedings-article/bigdata/2024/10825009/23yl5g758wo

[41] BST: Badminton Stroke-type Transformer (arXiv 2502.21085): https://arxiv.org/html/2502.21085v2

[42] BST: Badminton Stroke-type Transformer (CVPR 2026 CVsports): https://openaccess.thecvf.com/content/CVPR2026W/CVsports/papers/Chang_BST_Badminton_Stroke-type_Transformer_for_Skeleton-based_Action_Recognition_in_Racket_CVPRW_2026_paper.pdf

[43] TemPose-TF-ASF: Two-Stage Bidirectional Stroke Context Fusion (arXiv 2605.02558): https://arxiv.org/html/2605.02558v3

[44] Skeleton-based Action Recognition Models (MMAction2): https://mmaction2.readthedocs.io/en/dev-1.x/model_zoo/skeleton.html

[45] FineGym: A Hierarchical Video Dataset for Fine-Grained Action Understanding (official page): https://sdolivia.github.io/FineGym

[46] Improving Badminton Action Recognition Using Spatio-Temporal Analysis and a Weighted Ensemble Learning Model (Asriani et al., 2024): https://www.sciencedirect.com/org/science/article/pii/S1546221824008191

[47] The analysis of motion recognition model for badminton player (QCNN, Scientific Reports 2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12125242

[48] Wearable sensing for badminton stroke recognition with one-dimensional CNN (Scientific Reports 2025): https://www.nature.com/articles/s41598-025-25158-2

[49] Table Tennis Stroke Recognition Using Two-Dimensional Human Pose Estimation (Kulkarni et al., CVPRW 2021): https://openaccess.thecvf.com/content/CVPR2021W/CVSports/papers/Kulkarni_Table_Tennis_Stroke_Recognition_Using_Two-Dimensional_Human_Pose_Estimation_CVPRW_2021_paper.pdf

[50] Stroke Classification in Table Tennis as a Multi-Label Classification Task (Fujihara et al., Sensors 2025): https://www.mdpi.com/1424-8220/25/3/834

[51] ShuttleSet: A Human-Annotated Stroke-Level Singles Dataset for Badminton Tactical Analysis (arXiv 2306.04948): https://arxiv.org/abs/2306.04948

[52] ShuttleSet22: Benchmarking Stroke Forecasting with Stroke-Level Badminton Dataset (arXiv 2306.15664): https://arxiv.org/html/2306.15664v1

[53] BadmintonDB (MMSports '22): https://researchportal.hw.ac.uk/en/publications/badmintondb-a-badminton-dataset-for-player-specific-match-analysi

[54] CoachAI Badminton Challenge 2023 — Track 1: https://sites.google.com/view/coachai-challenge-2023/tasks/track1

[55] Classification of Strokes in Table Tennis for MediaEval 2020 (TTStroke-21): https://ceur-ws.org/Vol-2882/paper2.pdf

[56] MultiSenseBadminton (Scientific Data 2024): https://techxplore.com/news/2024-05-biomechanical-dataset-badminton-analysis.html

[57] A Video-Based Frame-Level Dataset of Badminton Player Movements (Mendeley): https://data.mendeley.com/datasets/3sp4xntp34

[58] ShuttleNet (AAAI-22 paper PDF): https://ojs.aaai.org/index.php/AAAI/article/view/20341/20100

[59] ShuttleNet GitHub: https://github.com/wywyWang/ShuttleNet

[60] Exploring the Long Short-Term Dependencies to Infer Shot Influence in Badminton Matches (BLSR, arXiv 2109.06431): https://arxiv.org/abs/2109.06431

[61] How Is the Stroke? Inferring Shot Influence in Badminton Matches via Long Short-term Dependencies (ACM TIST 2022): https://dl.acm.org/doi/abs/10.1145/3551391

[62] Where Will Players Move Next? Dynamic Graphs and Hierarchical Fusion for Movement Forecasting in Badminton (DyMF, AAAI-23): https://ojs.aaai.org/index.php/AAAI/article/view/25855

[63] DyMF (arXiv HTML): https://arxiv.org/html/2211.12217v2

[64] A Stroke of Genius: Predicting the Next Move in Badminton (RallyTemPose, CVPRW 2024): https://openaccess.thecvf.com/content/CVPR2024W/CVsports/papers/Ibh_A_Stroke_of_Genius_Predicting_the_Next_Move_in_Badminton_CVPRW_2024_paper.pdf

[65] RallyTemPose (IEEE Xplore): https://ieeexplore.ieee.org/document/10677986

[66] Gaming Tree Based Evaluation Model for Badminton Tactic Benefit Analysis and Prediction (Applied Sciences 2023): https://www.mdpi.com/2076-3417/13/13/7380

[67] Prediction model and technical and tactical decision analysis of women's badminton singles based on machine learning (PLOS ONE 2024): https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0312801

[68] Predicting badminton outcomes through machine learning and technical action frequencies (Scientific Reports 2025): https://www.nature.com/articles/s41598-025-87610-7

[69] Forecasting the Next Shot Location in Tennis Using Fine-Grained Spatiotemporal Tracking Data (Wei & Lucey, TKDE 2016): https://www.semanticscholar.org/paper/Forecasting-the-Next-Shot-Location-in-Tennis-Using-Wei-Lucey/1296f1dc09d8e90c42b588fd83adff39c149a1dd

[70] Valuing Decision Making and Shot Execution in Tennis (Seidl, Reid & Robertson): https://cdn.prod.website-files.com/68d6be744d7efccc2207f571/68d6be744d7efccc2208066d_RobertSeidl-TennisRally-RPpaper.pdf

[71] Identification and Prediction of Tennis Players' Technical and Tactical Behaviors Based on Transformer Model (Advanced Electromagnetics 2026): https://www.aemjournal.org/index.php/AEM/article/view/3582

[72] Capturing Intransitive Dominance in Tennis Forecasting: A Graph Neural Network Approach (arXiv 2510.20454): https://arxiv.org/html/2510.20454v2

[73] Real-time stroke prediction in badminton integrating AI with the KNN-HMM model (Journal of Big Data 2026): https://link.springer.com/article/10.1186/s40537-026-01396-7

[74] Predictive Momentum Modeling through Hidden Markov Competitive State Transitions (IJSA 2026): https://iaeme.com/Home/article_id/IJSA_07_01_001

[75] Hidden Markov model (Wikipedia): https://en.wikipedia.org/wiki/Hidden_Markov_model

[76] A New Table Tennis Match Stroke Forecasting Method Using Transformer-Based Deep Neural Networks (MJSSM 2026): https://www.mjssm.me?sekcija=article&artid=311

[77] ShuttleSet: Badminton Stroke-Level Analytics (EmergentMind): https://www.emergentmind.com/topics/shuttleset

[78] KDD 2023 — ShuttleSet Presentation (YouTube): https://www.youtube.com/watch?v=8q9lcNRjrHg

[79] Tennis Match Charting Project (GitHub): https://github.com/JeffSackmann/tennis_MatchChartingProject

[80] Tennis Abstract: Match Charting Project Metadata: https://www.tennisabstract.com/charting/meta.html

[81] Hawk-Eye (Wikipedia): https://en.wikipedia.org/wiki/Hawk-Eye

[82] CoachAI-Projects GitHub repository: https://github.com/wywywang/coachai-projects

[83] Badminton Feint: The Deceptive Shots of the Pros (BadmintonPeak): https://badmintonpeak.com/en/blog/feinte-badminton-deception

[84] Expert Players Accurately Detect an Opponent's Movement Intent Through Sound Alone (Camponogara et al., 2017): https://www.apa.org/pubs/journals/features/xhp-xhp0000316.pdf

[85] How to Trick Your Opponent: A Review Article on Deceptive Actions (Frontiers in Psychology 2017): https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2017.00917/full

[86] Predicting Tennis Serve Directions with Machine Learning (arXiv 2602.22527): https://arxiv.org/html/2602.22527

[87] The CoachAI Badminton Environment (AAAI-24): https://ojs.aaai.org/index.php/AAAI/article/view/30584/32746

[88] A Novel Reinforcement Learning Environment with Realistic Opponents (AAAI-24 Student Abstract): https://ojs.aaai.org/index.php/AAAI/article/view/30523/32673

[89] Team Intro to AI team8 at CoachAI Badminton Challenge 2023: Advanced ShuttleNet for Shot Predictions (arXiv 2307.13715): https://arxiv.org/abs/2307.13715

[90] Prediction of Shuttle Trajectory in Badminton Using Player's Position (VISAPP 2023): https://www.scitepress.org/PublishedPapers/2023/117858/117858.pdf
