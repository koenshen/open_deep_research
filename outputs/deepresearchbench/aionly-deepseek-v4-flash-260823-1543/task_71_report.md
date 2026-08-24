# AIGC in K-12 Education: A Comprehensive Global Research Report on Practical Applications, Frameworks, and Implementation

## Executive Summary

This report synthesizes research on the practical application of AIGC (AI-Generated Content) in primary and secondary school classrooms worldwide, drawing on peer-reviewed studies, government reports, and documented school-level case studies from North America, Europe, Asia, and Australia/Oceania. The evidence base reveals a field in rapid transition: student AI usage in the US jumped from 66% to 92% in a single year, with 83% of K-12 teachers now using generative AI tools, and the global AI-in-education market valued at $7.05B in 2025 projected to reach $136.79B by 2035 [1][2]. Yet the causal evidence on learning outcomes remains thin—of 800+ academic papers on AI in K-12 education, only 20 meet standards for strong causal inference, and none are high-quality causal studies of student-facing AI tools in US K-12 classrooms [3].

The report organizes AIGC applications into five core categories: (1) intelligent tutoring and personalized learning, (2) teacher productivity and lesson planning, (3) assessment generation and automated feedback, (4) subject-specific content generation, and (5) AI literacy and ethics education. Across these categories, the report presents detailed case studies including Newark Public Schools' Khanmigo rollout, Iowa's statewide Amira reading tutor, the UK's Oak National Academy Aila and EEF ChatGPT trial, Finland's Generation AI programme, China's Squirrel AI and iFLYTEK deployments, Singapore's Student Learning Space, India's Mindspark and Smart Paper, Japan's MEXT pilot schools, and South Korea's AI digital textbook experiment. The report concludes with implementation guidance, teacher training requirements, infrastructure considerations, future trends including agentic AI, and actionable recommendations for educators, administrators, and policymakers.

---

## 1. The Evidence Base: What Research Actually Shows

### 1.1 Adoption Statistics and Market Context

Adoption of AIGC in K-12 settings has accelerated dramatically. During the 2024-25 school year, 85% of teachers and 86% of students used AI (student use jumped 26% year-over-year), with 69% of teachers reporting AI tools have improved their teaching methods [1]. A 2025 Walton Family Foundation and Gallup study found 60% of teachers used AI at least occasionally, with weekly users saving about 6 hours per week—equivalent to six full weeks per school year [4]. Teachers using AI weekly save an average of 5.9 hours per week [5]. In a nationally representative 2025 RAND survey, 54% of middle and high school students reported using AI for school, and 53% of English language arts, math, and science teachers reported using AI in instructional tasks [3][6].

The global picture shows similar momentum. In Europe, over 80% of teenagers already use AI regularly for learning, and a 2025 Flash Eurobarometer found 63% of respondents agreed everyone will need to be AI-literate by 2030 [7]. Eurostat data reveals that in 2025, nearly 1 in 3 people in the EU used generative AI, with the highest education-sector adoption rates in Sweden (21%), Malta (20.2%), and Denmark (17.9%), compared to lower rates in Germany (6%), Poland (4.6%), and Romania (3.4%) [8]. In the Asia-Pacific region—the fastest-growing market at 48% CAGR—China, Singapore, Japan, South Korea, and India have all implemented national AI-in-education strategies [1][9].

### 1.2 What the Causal Evidence Shows

The Stanford AI Hub Research Repository contained over 1,100 academic papers on AI and K-12 education as of late 2025, yet only 20 high-quality causal studies rigorously examine how AI tools affect students or educators, with none conducted in US K-12 schools on student-facing AI tools [3][10]. The research that does exist yields several critical insights:

- **Performance during use ≠ learning.** A study of high school math students found that those using a general-purpose chatbot performed worse on a subsequent closed-book exam than students who practiced with no AI support, despite having higher practice performance. The OECD's Digital Education Outlook 2026 similarly found that students with access to general-purpose AI chatbots produced higher-quality outputs than peers, but this advantage disappeared and sometimes reversed in exams when access was removed [3][11][12].

- **Design matters more than technology.** Systems that prompt students to explain reasoning and engage actively tend to support learning, while systems that generate complete answers reduce cognitive work and learning. Tutoring-style AI with hints and guided reasoning shows more promise than general-purpose chatbots [3][11].

- **Teacher-facing tools show early promise.** The EEF's randomized controlled trial in England found teachers using ChatGPT saved approximately 25 minutes per week (a 31% reduction) in lesson planning time without reducing resource quality [6][13]. Stanford's Tutor CoPilot RCT showed AI-assisted tutors improved student math mastery by 4 percentage points, with gains of 9 points for lower-rated tutors [14][15].

- **Well-designed AI tutors can outperform traditional instruction.** A peer-reviewed RCT published in *Scientific Reports* (June 2025) found an AI tutor outperformed traditional in-class learning with an effect size between 0.73 and 1.3 standard deviations [1]. A June 2025 Harvard study found students using a well-designed AI tutor (PS2 Pal) learned more than twice as much in less time compared to active-learning classrooms—succeeding due to pedagogical guardrails, not the underlying technology [16].

- **A 2026 systematic review** of 45 studies (2020–2024) in *Research and Practice in Technology Enhanced Learning* found GenAI tools significantly improve students' academic performance, cognitive abilities, and learning motivation, while also noting challenges including erroneous content generation, student dependence, and privacy infringement [17]. A separate systematic review of 30 papers found mathematics was the most common subject studied (5 papers), ChatGPT was used in 21 of 30 papers, and 90% emphasized the need for teacher professional development [18].

---

## 2. An Overall Framework for AIGC in K-12 Education

### 2.1 A Taxonomy of Application Approaches

Synthesizing the case study evidence, AIGC applications in K-12 classrooms can be organized into five core categories, each with distinct characteristics, benefits, and challenges:

| Category | Primary Users | Representative Tools | Key Benefits | Key Challenges |
|---|---|---|---|---|
| **1. Intelligent Tutoring & Personalized Learning** | Students (K-12) | Khanmigo, Amira, Squirrel AI, SLS Adaptive Learning System | Individualized pacing, 24/7 availability, immediate feedback, scalability | Over-reliance risk, uneven engagement, limited causal evidence |
| **2. Teacher Productivity & Lesson Planning** | Teachers | Aila, MagicSchool AI, ChatGPT, Eduaide | 20-40% workload reduction, faster planning, higher-quality differentiation | Output verification needed, quality varies by subject, prompt skill required |
| **3. Assessment Generation & Automated Feedback** | Teachers & Students | Smart Paper, Gradescope, ShortAnsFA, AI graders | 10x faster feedback, objective scoring at scale, misconception detection | Bias risks, over-reliance on detectors, feedback quality concerns |
| **4. Subject-Specific Content Generation** | Teachers & Students | DALL-E, Midjourney, Suno, ERNIE Bot, custom chatbots | Creativity support, multimodal expression, engagement, accessible entry points | Copyright/attribution, quality control, age-appropriateness |
| **5. AI Literacy & Ethics Education** | Students (all grades) | Generation AI tools, DigiHavel, Teachable Machine, Day of AI | Critical thinking, democratic resilience, responsible use, future readiness | Curriculum crowding, teacher readiness, rapid technological change |

### 2.2 Guiding Frameworks for Classification and Implementation

Several established frameworks help organize AIGC applications:

- **UNESCO AI Competency Framework for Students** outlines 12 competencies across four dimensions (Human-centred mindset, Ethics of AI, AI techniques and applications, AI system design) spanning three progression levels: Understanding, Applying, and Creating with AI [19][20]. The companion **UNESCO AI Competency Framework for Teachers** defines 15 competencies across five dimensions (Human-centred mindset, Ethics of AI, AI foundations and applications, AI pedagogy, AI for professional learning) organized into Acquire, Deepen, and Create levels [19][21].

- **The OECD Digital Education Outlook 2026** introduces three modes of human-AI collaboration: *Replacement* (AI performs tasks traditionally requiring instructional judgment), *Complementarity* (AI handles repetitive tasks while teachers retain final decisions), and *Augmentation* (AI actively re-stimulates and extends teachers' professional judgment) [12][22].

- **The AI4K12 "Five Big Ideas"** — Perception, Representation & Reasoning, Learning, Natural Interaction, and Societal Impact — provide a K-12 curriculum taxonomy with grade-band progression charts (K-2, 3-5, 6-8, 9-12) developed by the AAAI and CSTA [23][24].

- **The SAMR model** (Substitution, Augmentation, Modification, Redefinition) is increasingly applied to AI integration. Louisiana's four-tier approach (AI-Empowered, Enhanced, Assisted, Prohibited) is explicitly aligned with SAMR, and Delaware uses SAMR with version tracking for AI integration [25].

- **The AI-TPACK framework** extends the classic TPACK model with AI-specific knowledge components (AI-TK, AI-TCK, AI-TPK, AI-TPACK, and AI Ethics). Empirical studies of 401 Turkish teachers found AI-TPACK competencies below average (mean 3.33 on a 7-point scale), with digital proficiency as a significant predictor [26]. A 14-week AI-focused pedagogical course for 84 preservice science teachers produced statistically significant improvements across all AI-TPACK dimensions with a large effect size (z = -6.900, p < .001, r = 0.76) [27].

- **The SREB Four-Pillar Framework** (April 2025) provides practical guidance: (1) Use AI to develop more cognitively demanding tasks, (2) Use AI to streamline teacher administrative work, (3) Use AI to support personalized learning, and (4) Develop students as ethical and proficient AI users [28].

---

## 3. Category 1: Intelligent Tutoring and Personalized Learning

### 3.1 Khanmigo (Khan Academy) — United States

Khanmigo, Khan Academy's AI-powered tutoring platform built on GPT-4, represents the most widely documented AIGC tutoring deployment. Developed in just seven months (November 2022 to March 2023), it was designed as a Socratic tutor that guides students through questioning rather than providing direct answers [29][30]. Adoption grew from 68,000 users in 2023-24 to more than 700,000 students in the 2024-25 school year—described by Chief Learning Officer Kristen DiCerbo as "the biggest one-year jump" in ed tech adoption she's seen in 20 years—expanding from 45 to over 380 district partners [29][30][31]. Projections exceed one million students in 2025-26 [29].

**Newark Public Schools case study (New Jersey):** Newark was among the first districts to pilot Khanmigo, launching at First Avenue School in 2023-24 for grades 5-8, supporting math, reading, and writing instruction [32]. The district expanded to 14 North Ward schools in 2024-25, eventually reaching 66 schools and approximately 29,000 students [32][33]. Students using Khanmigo during the pilot showed math score improvements—First Avenue School had the second-highest math proficiency rate among North Ward schools in spring 2024 state tests, and district math proficiency rose from 15% to 17.7% [32]. A three-year longitudinal efficacy study of ~8,000 students in grades 3-8 found students who became Yearly Proficient Learners (learning 60+ additional skills) achieved an average of +6 points on the NJSLA, versus the state average of +2—three times the state average math score increase [33].

Bill Gates, who visited First Avenue School in May 2024, documented teachers' creative uses: an eighth-grade algebra teacher used Khanmigo to create problem sets incorporating Newark boxer Shakur Stevenson's workout routines, while a third-grade teacher changed AI-drafted story problems from a generic fruit stand to Pokémon cards and Roblox themes, noting "Khanmigo gives me the blueprint, but I have to give the delivery" [34]. Teachers used AI dashboards to track individual student progress, saving significant time. However, Gates also acknowledged limitations: students noted Khanmigo struggled to pronounce Hispanic names, had only a male voice option, and required multiple attempts to get desired results [34].

**Evidence and challenges:** Khan Academy has not yet conducted a randomized control trial of Khanmigo due to cost and complexity [31]. Robbie Torney of Common Sense Media notes there is little to no evidence that generative AI-powered tutors improve student outcomes, despite research backing human tutoring [31]. Early issues included errors in basic math problem-solving (since fixed) and the tool offering too much help during assessments, prompting changes to align with a "Socratic tutor" approach [33]. DiCerbo expressed disappointment that some teachers primarily use the AI to generate multiple-choice questions rather than deeper engagement activities, and noted the biggest challenge is achieving meaningful student engagement—many students respond with "I don't know" or don't put forth sufficient cognitive effort [30].

### 3.2 Amira AI Reading Tutor — Iowa, United States

In August 2024, the Iowa Department of Education invested $3 million in Amira (EPS Learning), an AI-powered reading tutor using voice recognition to follow children reading aloud and offer corrective feedback through a digital avatar. The program issued 200,000 licenses to 246 schools, with an estimated 105,000 elementary students gaining access [35]. In the first year, Iowa students read approximately 960,000 stories and logged nearly 4 million minutes of reading. Students typically use Amira 20-30 minutes per week, and teachers can review recorded sessions to modify instruction [35].

For the 2025-26 school year, Iowa expanded access with $400,000 in licenses for MTSS Tier II and Tier III students, English Learner access, and an additional $2.5 million from Governor Kim Reynolds to expand to Tier I students statewide [35]. The tool has an Evidence for ESSA rating of Moderate, based on two studies of 15,602 students with an average effect size of +0.15. A student-randomized trial with 178 struggling readers in grades 1-4 found Amira users scored significantly higher on the Woodcock Reading Mastery Test (effect size +0.64) [35].

Amira differs from general-purpose AI like ChatGPT—it operates as a closed, secure system that never accesses the open internet, fully compliant with COPPA, FERPA, and CIPA, and does not generate its own responses to students [35]. Winterset Elementary School third-grade teacher Abby Bean noted the tool "provides accountability during independent reading, immediate corrective feedback, diagnostic information, and progress monitoring reports" [35].

### 3.3 Squirrel AI — China

Squirrel AI (Squirrel Ai Learning), founded in Shanghai in 2014, is China's flagship AI adaptive learning system, recognized as a TIME100 Most Influential Companies for 2026 [36]. Its Intelligent Adaptive Learning System (IALS) pioneered nanoscale knowledge decomposition: junior high school mathematics (300 knowledge components) is dissolved into 30,000 fine-grained knowledge components connected in a graph structure [36][37]. The system's MCM model (Modes of Thinking, Capacity, and Methods) analyzes attention spans, study patterns, and knowledge point blindness [37].

Documented outcomes include a success story in Qingtai County, a poverty-stricken county (average yearly income $1,025), where student mastery rates increased from 56% to 89% in one month, with rural children's achievement exceeding county averages and some surpassing average students in Wuhan [37]. The company reports serving over 24 million registered students across 2,000+ self-study centers, with its LAM (Large Adaptive Model) launched January 2024 improving question accuracy rates from 78% to 93% [36][38]. A 2018 research paper evaluated the system on English and math learning in Chinese middle schools, finding "students achieved better performance than both traditional classroom instruction by expert teachers and another adaptive learning platform" [39]. Squirrel AI has research partnerships with Harvard University, Carnegie Mellon, SRI, and Stanford, with first US centers opening in California and New York [38].

### 3.4 Singapore's Student Learning Space (SLS) AI Features

Singapore's national SLS platform—available to every teacher and student from primary through pre-university levels—has integrated eight AI-enabled features: the Adaptive Learning System (ALS) for personalized pathways in Mathematics and Geography; Authoring Copilot (ACP) for AI-driven lesson planning; Annotated Feedback Assistant (AFA); Data Assistant (DAT) for student data analysis; Learning Assistant (LEA), a student-facing dialogic agent that "helps students learn by asking guiding questions" and "takes on different roles to encourage students to think in different ways"; Feedback Assistant Mathematics (FA-Math) offering step-by-step hints; Short Answer Feedback Assistant (SAFA); and Speech Evaluation Tool (SET) for pronunciation feedback in English and Mother Tongue Languages [40][41]. Singapore's Ministry of Education emphasizes that "students must continue to have opportunities to struggle productively, experience failure and work with others," and has introduced a progressive age-tiered policy: P1-P3 pupils do not directly use AI, P4-P6 use AI in structured ways under teacher supervision, and secondary students get progressively wider exposure [42][43]. All teachers must complete compulsory AI literacy modules by end of 2027 [44].

### 3.5 Mindspark — India

The Mindspark randomized controlled trial in Delhi (conducted by Muralidharan, Singh, and Ganimian) provides some of the strongest causal evidence for AI-assisted personalized learning in low-resource settings. Among 619 students from low-income neighborhoods in five public middle schools, lottery winners scored 0.37σ higher in math and 0.23σ higher in Hindi over a 4.5-month period, with instrumental variable estimates showing that 90 days of attendance would raise math and Hindi scores by 0.6σ and 0.39σ respectively [45][46]. The program cost just INR 200 (USD 3) per month, was cost-effective even at small scale, and delivered the largest gains for academically weaker students [45]. The study's context is stark: over 50% of Grade 5 students in India cannot read at second-grade level, and the average Grade 6 student was 2.5 grade levels behind in math, growing to 4.5 by Grade 9 [45].

### 3.6 Lessons Across Tutoring Systems

Across all tutoring systems, the evidence converges on several design principles: (1) Socratic guidance that prompts students to explain reasoning outperforms systems that generate complete answers; (2) pedagogical guardrails matter more than underlying model capability; (3) dosage and sustained engagement are the biggest implementation challenges—Khan Academy's 2024 efficacy report found only ~9% of students met the recommended 18+ hours/year dosage, though those who did saw ~20% greater-than-expected MAP Growth gains [3][47]; and (4) human encouragement and teacher integration are essential—a 2016 UC Berkeley RCT found that without parental encouragement, student usage plummeted and short-term gains vanished within a week [47].

---

## 4. Category 2: Teacher Productivity and Lesson Planning

### 4.1 Oak National Academy Aila — United Kingdom

The UK government invested £2 million in Oak National Academy in October 2023 to develop AI-powered tools for teachers in England, resulting in Aila, a free AI lesson-planning assistant launched in 2024 [48][49]. Aila operates through a four-step process: teachers tell Aila what lesson to plan (e.g., "KS2 geography - features of a volcano"), follow an iterative process where Aila can add case studies, adjust keyword difficulty, and generate starter/exit quizzes, learning cycles, practice tasks, and model answers, then download editable lesson plans, slides, worksheets, and quizzes [49]. Teachers remain in control throughout, and the tool is underpinned by Oak's research-informed curriculum principles with built-in quality checks for grammar, Americanisms, and coherence [49].

Teacher testimonials report saving 3-4 hours per week. One teacher at The Charter School Bermondsey reported: "Instead of spending hours searching for and compiling information, I can now prepare comprehensive lessons in a fraction of the time—saving me four hours a week" [49]. The Education Endowment Foundation is currently recruiting 450 Key Stage 2 teachers from 86 primary schools for an independent randomized controlled trial of Aila, with results expected in autumn 2026 [50]. John Roberts, Interim CEO at Oak, notes: "We only save teachers time if what it produces is reliable, safe and high-quality" [50].

### 4.2 EEF ChatGPT Trial — United Kingdom

The Education Endowment Foundation conducted a rigorous randomized controlled trial involving 259 teachers of Year 7 and/or Year 8 science from 68 state-funded secondary schools in England. Teachers used ChatGPT (supported by an online guide) for approximately 10 weeks during the 2024 summer term [6][13][51]. Key findings:

- Teachers in the ChatGPT group saved approximately 25 minutes per week on average (56.2 minutes vs. 81.5 minutes for the comparison group)—a 31% reduction in lesson planning time [6][13].
- There was no difference in the quality of resources produced, based on blind review by a panel of five science teachers [6][13].
- Three-quarters of the ChatGPT group reported a positive impact on their teaching, and 78% said they would continue using ChatGPT for lesson preparation [6][13].
- The proportion of ChatGPT teachers who felt they spent "too much time" on lesson preparation dropped from 49% to 26% during the trial [6][13].
- Common uses included generating ideas for teaching and quizzes, tailoring lessons for different classes, and adapting existing resources for cover lessons [6].

Limitations noted included privacy concerns, limitations in image generation, and the need for all outputs to be checked for accuracy due to potential hallucination [6].

### 4.3 MagicSchool AI — United States and Global

MagicSchool AI is a teacher productivity suite with 80+ tools and 5M+ educator users across 173 countries and 48 languages [52]. Its 2025 Wrapped report shows total AI generations rising by 87%, with the most-used teacher tools being: (1) Text Rewriter, (2) Multiple Choice Quiz and Assessment, (3) Worksheet Generator, (4) Writing Feedback, and (5) Lesson Plan Generator. For students, the top tools were Custom Chatbot (acting as a tutor), Writing Feedback, Character Chatbot, Quiz Me, and Study Bot [52].

A Technology Review published in *Education Sciences* (July 2025) evaluated MagicSchool AI's five special-education functions: Text Leveler, Text Scaffolder, Assignment Scaffolder, Exemplar & Non-Examples, and Sentence Starters. The review found the tool valuable for teachers creating inclusive lessons, particularly for non-core subject teachers lacking special education support, but noted it falls short of providing direct, actionable activities ready for classroom implementation and cannot offer detailed feedback on teachers' lesson plans [53]. Context: 40% of special education teachers leave the field within five years, and 7.5 million US students (15% of enrollment) required IEPs during 2022-23 [54][55].

### 4.4 Tutor CoPilot — Stanford University / FEV Tutor

Tutor CoPilot is a Human-AI system that models expert thinking to assist tutors in real time during chat-based tutoring sessions, leveraging the Bridge method which extracts latent expert reasoning from experienced educators through think-aloud protocols [14][15]. In a randomized controlled trial involving 874 full-time tutors and 1,787 K-12 students (grades 3-8, 80% Hispanic, 67% economically disadvantaged) from Title I schools, students of tutors with access to Tutor CoPilot were 4 percentage points more likely to pass exit tickets (62%→66%, p<0.01) [14][15]. Among tutors who actually used the tool, students were 14 p.p. more likely to pass. Lower-rated tutors saw the greatest benefit—9 p.p. improvement in student mastery (56%→65%) [14][15].

Analysis of over 350,000 messages showed Tutor CoPilot promotes effective pedagogy, increasing the use of probing questions and reducing generic praise. Treatment tutors were approximately 2 standard deviations more likely to use high-quality strategies like "prompting student to explain" and "asking questions to guide thinking," and less likely to "give away the answer" [14][15]. The cost is only $20 per tutor annually—far cheaper than traditional professional development programs costing $3,300+ per teacher annually [14]. The World Bank replicated positive effects in Nigerian secondary English classes, with the AI assistant delivering 0.31 standard deviation growth within six weeks (equated to almost two years of schooling) [56].

---

## 5. Category 3: Assessment Generation and Automated Feedback

### 5.1 Smart Paper AI — India

Smart Paper, developed in Jodhpur, India, demonstrates the potential of AIGC for assessment at scale. In a proof of concept in Jodhpur District, more than 10,000 handwritten exams from 2,500 students were graded by the platform for 300 teachers across 55 government schools [57]. The AI not only scores but analyzes student reasoning—when 1,000 students solve the same algebra equation incorrectly, the large language model clusters answers, identifies common misconceptions, and generates targeted lesson plans. "You're reading the thoughts of students at scale. That's never been possible before," said co-founder Nirmal Patel [57]. The platform is currently used across 65,000 middle schools for multiple-choice grading, with earlier prototypes digitizing multiple-choice worksheets using computer vision that works on low-end phones, collecting data on 5 million students over three years [57].

### 5.2 AI-Assisted Grading and Feedback Systems

- **iFLYTEK SPARK AI Grader P30** (China) integrates scanning, automated grading, and printing, supporting objective and subjective questions including essays, performing step-by-step evaluation and generating learning reports [58].
- **Singapore's Short Answer Feedback Assistant (SAFA)** provides fast, personalized feedback for free-response questions, with teachers vetting AI-generated feedback before it reaches students. The **Speech Evaluation Tool (SET)** provides instant automated feedback on pronunciation and reading fluency [40][41].
- **Gradescope** reportedly reduces grading time by up to 80%, evaluating handwritten math, coding, and essays [59].
- **Better Speech's Streamline platform** reduced IEP preparation time by 90% (from 3 hours to 10 minutes). Teachers using AI to draft IEP goals scored 9.1-10 on a 10-point quality scale vs. 5.5-9.2 without AI. By 2024-25, 57% of special education teachers used AI for IEPs or 504 plans (up from 39%) [54][55].
- AI assessment tools provide feedback 10x faster than traditional methods, and AI-powered personalized learning increases engagement by up to 60% and learning efficiency by 57% [1].

### 5.3 Evidence and Cautions on Automated Feedback

The evidence on automated feedback quality is mixed but promising. The Tutor CoPilot study demonstrated that AI-generated feedback guidance improved tutor questioning strategies [14]. However, research also cautions that AI detectors are unreliable—one analysis found only 1% of instructors completely trust AI detection software, which disproportionately flags neurodivergent and second-language students' work [60]. Massachusetts explicitly recommends against AI detection tools, favoring trust-based, transparency-focused approaches to academic integrity [25]. The CITE Journal study of 310 AI-generated lesson plans (2,230 learning activities) for Massachusetts eighth-grade civics found only 10% of activities promoted higher-order thinking (analyze, evaluate, create), with 45% coded at the "remember" level—a cautionary finding for those using AI to generate assessments [61].

---

## 6. Category 4: Subject-Specific Content Generation

### 6.1 Language Arts and Writing

AVID Open Access identifies AI-assisted writing and revision as one of the seven most effective student-facing strategies, with tools like MagicSchool, School AI, and Enlighten AI providing automated feedback [62]. Students using guided AI tutors scored dramatically higher on practice problems without harming performance on real tests [3][62]. However, studies of college-level writing show complex patterns: a Boston University study found that in 18.6% of prompts, students asked ChatGPT to write for them, with students using ChatGPT to generate 8.2% of the writing they submitted [63]. English as a foreign language (EFL) students integrated less AI-generated text into their papers than non-EFLs [63].

In secondary settings, a Malaysian study of 40 Form 4 students using "Bard G" (a guided learning aid for Google Gemini) found students could complete essay writing tasks within half an hour (compared to about an hour before), reported increased confidence, and could teach others to use Gemini—though problems included lack of facilities, poor internet connection, and insufficient guidance [64]. APA Monitor guidance for reducing problematic reliance includes breaking large writing assignments into smaller scaffolded chunks, reducing page length, providing face-to-face feedback, and using group/multimedia assignments that require student-produced elements [60]. Teachers are also teaching students to critique AI outputs and use AI as a "questioning partner" rather than an answer generator [60].

### 6.2 Mathematics

Mathematics has the largest share of causal impact studies in K-12 AI research [10]. Key findings include:

- A University of Pennsylvania study found unguided AI access harmed learning outcomes in high school mathematics [16].
- A study of high school math students found those using a general-purpose chatbot performed worse on a subsequent closed-book exam than students who practiced with no AI support [3][11].
- Khanmigo's algebra focus in Newark produced measurable gains for Yearly Proficient Learners [33].
- Singapore's FA-Math offers step-by-step hints with suggested marks, including randomized question generation with geometry and graphs [41].
- Squirrel AI's nanoscale knowledge decomposition of junior high math into 30,000 components enables precise diagnosis and remediation [36][37].
- A University of Toronto RCT (10,979 students) found only grades 3-6 students who used Khan Academy ~35 min/week saw math gains (0.12-0.17 SD), with usage dropping sharply without teacher/parental encouragement [47].

### 6.3 Science

The University of Gothenburg study "Generative AI as a lab partner: A case study" (published in *Physical Review Physics Education Research*, August 2025) examined how high school students use ChatGPT during a physics laboratory session on acoustic levitation. The study found that although generative AI can handle some relevant questions during lab work, "the teacher still plays a crucial role in identifying students' needs and capabilities for understanding the potential and limitations of generative AI," and students need support and training to efficiently utilize the tools [65]. A Beijing high school English reading case study (published in *Frontiers in Education*, May 2025) integrated Midjourney for AIGC visuals, ERNIE Bot for mind maps, and multiple generative AIs for group discussions, finding statistically significant improvements in language proficiency (6.5 to 8.0, +1.5), classroom engagement (+1.7), teamwork (+1.2), and learning motivation (+1.5) [66].

### 6.4 Social Studies and Civics

DigiHavel (Czech Republic) is a civic education chatbot inspired by Václav Havel that teaches democracy and citizenship while also teaching students to verify information and detect AI hallucinations. The deliberately caricatured design reminds users it's a simulation, and it includes accessibility features like text-to-speech and English support for Ukrainian refugee students [67][68]. Interactive role-playing via AI chatbots (e.g., speaking with historical figures through Khanmigo and MagicSchool) is identified as one of the seven most effective student-facing strategies [62].

However, the CITE Journal study of AI-generated civics lesson plans found that 90% of activities were coded at lower-order thinking levels, and AI-generated plans rarely introduced diverse perspectives—only 144 of 2,230 activities received a Banks' code for multicultural content. Gemini declined to generate plans for 7 standards (including elections and political protests) due to election-related restrictions [61].

### 6.5 Arts: Visual Art and Music

AI art tools including Midjourney, DALL-E, Microsoft Copilot, Canva AI, Adobe Firefly, and Stable Diffusion are being incorporated into K-12 classrooms. Edutopia guidance emphasizes that AI art vocabulary is essential (there's a big difference between asking for "guitar music" vs. "Spanish guitar in the style of Govi"), human supervision is required, and bias awareness is critical [69]. Midjourney is NOT recommended for K-12 schools because it uses public Discord servers, while DALL-E is considered suitable for high school and above [69][70].

The AI music-generation tool Suno converts text into fully realized songs in under a minute. Classroom applications include elementary math students collectively writing lyrics describing types of triangles (creating a mnemonic song) and English language arts students turning poetry into songs to deepen understanding of mood and tone. The software is intended for users 13 and up [71]. SchoolAI's guide notes AI art tools democratize visual expression, citing Lehigh University research on higher engagement with Midjourney and the Ecole des Beaux-Arts "Artique" AI tutor in France [70]. An analysis of 101,953 AI-generated songs found English most prevalent (71.39% on Udio, 46.75% on Suno), with worship songs forming the largest individual cluster [72]. Ethical considerations around copyright and attribution are paramount, with the National Art Education Association recommending use of public domain or Creative Commons-licensed imagery [70].

---

## 7. Category 5: AI Literacy and Ethics Education

### 7.1 Finland's Generation AI Programme

Finland's Generation AI research programme—funded by the Strategic Research Council and delivered by the Universities of Eastern Finland, Helsinki, and Oulu with Code School Finland—was named Europe's best AI literacy initiative for education at EMINENT 2025 [73]. The programme develops research-based tools that allow pupils to build classifiers or their own language models, examine social media algorithms, and investigate algorithmic bias without needing programming skills. Key tools include the Generation AI Teachable Machine, Social Media Machine, Breaking Machine, and Small Language Machine—all running locally in browsers with full GDPR compliance and no data transfer outside the classroom [73]. The tools have been used more than 200,000 times in over 50 countries and have won multiple international awards [73].

Principal investigator Professor Matti Tedre explained: "We want to help children and young people understand how AI systems work and how they affect, for example, what they see online, how they are profiled and the ways in which decisions concerning them are made" [73]. Finland's approach is grounded in its status as Europe's most media-literate country, with media literacy part of the national curriculum from primary through secondary school. Education Minister Anders Adlercreutz emphasizes AI literacy as a central democratic skill, particularly given Russian hybrid pressure and disinformation campaigns—high school students even set up troll farms to understand how easily people are swayed [74]. The Finnish National Agency for Education published "Artificial intelligence in education – legislation and recommendations" in 2025, covering AI bias, the AI Act, data protection, copyright, assessment, and sustainable development [75].

### 7.2 UAE's Mandatory AI Curriculum

In May 2025, the UAE Cabinet approved making AI a mandatory subject across all government schools, from kindergarten through Grade 12, making it "among the first nations worldwide to integrate AI into schools" [76][77]. The curriculum is integrated into the existing Computing, Creative Design, and Innovation subject without requiring additional teaching hours, with 1,000+ teachers trained nationwide and 1 million students engaged annually [78]. The curriculum structure is age-appropriate: kindergarten students learn AI via stories and play (comparing machines and humans), grades 5-8 design and evaluate AI systems (bias and algorithms, ethics), and secondary students focus on prompt engineering, real-world AI scenarios, and career preparation [79]. Minister Sarah Al Amiri emphasized: "We studied the advent of technology across the last few decades and we saw that if we don't react appropriately... So we wanted to make sure that today students are aware of the downfalls of using AI or their limitations, the ethical considerations, the biases that are built into those systems" [80]. TALIS 2024 data shows about 75% of UAE teachers use AI tools—far above the global average of 33%, matched only by Singapore [80]. The UAE's 2026 MOE manual bans generative AI for students under 13 or below Year 7, with older students permitted to use AI only under teacher supervision [81].

### 7.3 China's National AI Education Mandate

Starting September 2025, AI education became mandatory in all Chinese primary and secondary schools, with students from age 6 receiving at least 8 hours of AI education per year [82]. The curriculum is centralized and standardized, covering concepts, machine learning, robotics, and practical AI applications [82]. In February 2024, China's Ministry of Education selected 184 primary and secondary schools as AI education pilot bases [83]. The May 2025 Guidelines for AI Education divide the curriculum by level: primary (imagination and basic cognition), junior high (technical principles), and senior high (systematic thinking and innovation) [84]. In April 2026, China launched a national "AI+Education Action Plan" issued by the Ministry of Education alongside four other ministries, mandating AI integration from kindergarten through lifelong learning with a goal of deep AI-education integration by 2030 [85][86]. By 2035, China aims to make AI integral to textbooks, exams, and classrooms at all levels [87].

### 7.4 AI Literacy Frameworks and Programs

- **The AILit Framework** (European Commission/OECD, approved by the PISA Governing Board April 2026) defines AI literacy as "the technical knowledge, durable skills and future-ready attitudes required to thrive in a world influenced by AI" and organizes 22 competences into four domains: Engaging with AI, Creating with AI, Managing AI, and Designing AI. AI literacy will be assessed for the first time on the PISA 2029 Media & AI Literacy assessment [7][88].
- **aiEDU's AI Readiness Framework** was cited by 87 organizations and 13 state education agencies; its curriculum reached 2 million students across 175 countries in 2025 [89][90].
- **Day of AI Australia/Aotearoa** reached 340,000+ students since 2022 with country-specific programs. In New Zealand, 92% of students in a pilot were already using AI, but understanding rose from 20% to 64% after the pilot [91][92].
- **The CSTA/AI4K12 "AI Learning Priorities"** (2025) found eight out of ten CS teachers believe learning about and using AI should be part of foundational CS education [24].

---

## 8. Regional Policy Landscapes

### 8.1 United States

The US policy landscape is fragmented. The April 2025 Executive Order established a White House Task Force on AI Education, and the US Department of Education issued guidance on July 22, 2025 via a Dear Colleague Letter outlining how federal grant funds may be used for AI-based instructional materials, AI-enhanced tutoring, and AI for college/career pathway navigation [6][93]. As of October 28, 2025, 34 states (plus Puerto Rico) have official guidance or policy on AI use in K-12 schools [25]. Notable state approaches include Georgia's "Traffic Light" system, Louisiana's four-tier integration approach, New Mexico's M.A.Z.E. framework with a five-level AI Assessment Scale, and Massachusetts' explicit guidance against AI detection tools [25]. A 2026 FutureEd tracker documented 77 AI education bills across 27 states, with ten enacted [94]. However, the US has zero binding federal AI curriculum standards, and only 5% of superintendents have formal AI policies in place [2][95].

### 8.2 European Union

The EU AI Act entered into force August 2024 and becomes fully applicable in August 2026, with many education AI applications expected to fall under its "high-risk" category [96]. The JRC exploratory study (2025) examined GenAI use among early adopters across Ireland, Finland, Germany, Luxembourg, and Spain, finding that educators and students saw GenAI as a tool to enhance learning but raised concerns about academic integrity, bias, and over-reliance [97]. The European Commission and OECD jointly developed the AILit Framework, and European Schoolnet's EMINENT 2025 report covering 23 education systems revealed fragmented approaches and uneven readiness [7][98]. National policies vary widely: Germany's Kultusministerkonferenz adopted a "Recommendation for action" covering five key topics including examination culture and teacher professionalization [96]; France's AI in Education Framework (June 2025) prohibits student use of generative AI before 4th grade and requires teacher authorization for any use [99]; Spain pairs €1.5B strategy funding with a national AI language model (ALIA) and a Guide on AI Use in Education [100].

### 8.3 Asia

Asia shows the most centralized and aggressive policy adoption. China mandates AI education nationwide with 184 pilot schools and a national action plan [82][85][86]. Singapore integrates AI through its EdTech Masterplan 2030 and SLS, with the "Four Learns" framework (Learn about AI, Learn to use AI, Learn with AI, Learn beyond AI) [42][101]. Japan's MEXT issued guidelines in July 2023 (updated December 2024) emphasizing caution, human judgment, and appropriate use, with 52 designated "testbed" schools [102][103]. South Korea's AI digital textbook initiative—launched March 2025 for grades 3, 4, 7, and 10—was stripped of mandatory status within four months after teacher and parent opposition, with adoption rates dropping from 37% to 19% between semesters and an estimated $545 million in stranded publisher investment [104][105][106]. India plans to implement AI curriculum from Grade 3 beginning 2026-27, building on CBSE's AI elective for classes IX-XII [107][108].

### 8.4 Australia and New Zealand

Australia's national *Australian Framework for Generative AI in Schools* (endorsed December 2023, reviewed June 2025) outlines principles including privacy and security, equity, and human oversight [109]. South Australia's EdChat trial (an education-specific chatbot providing hints rather than answers) expanded to 16 public high schools [110][111]. New South Wales deployed NSWEduChat to 50 schools, restricted to the state syllabus; at Plumpton High, year 11 students use it to draft essays on Shakespeare, and the chatbot refuses to write essays for students, instead prompting deeper thinking—with reported improvements from 800 to 1,000-1,500 words in 40 minutes [112]. New Zealand's Ministry of Education guidance (updated May 2026) emphasizes that "human teachers must remain central in students' education," prohibits GenAI in NCEA external assessment, and provides case studies from Aotea College and Hobsonville Point Secondary School [113]. A NZCER survey of primary schools found 79% of teacher respondents used generative AI at least monthly, but only 8% of schools had a teacher-use AI policy and only 39% of teachers felt adequately supported [114][115].

---

## 9. Practical Implementation Methods

### 9.1 Step-by-Step Guidance for Schools and Districts

Based on the TeachAI toolkit, the ILO Group framework, and documented district experiences, implementation follows a consistent pattern [3][116]:

**Phase 1: Governance and Policy (Months 1-3)**
- Establish a district-wide AI steering committee (administrators, teachers, parents, students, legal counsel)
- Audit existing technology infrastructure, vendor contracts, and data privacy practices
- Develop a principles-based AI policy (avoid overly complex policies that are difficult to refine as technology evolves)
- Conduct caregiver engagement early—"Families are going to turn to their child's classroom teacher and school principal when they have questions"

**Phase 2: Training and Pilot (Months 3-9)**
- Provide foundational AI literacy training to all staff (addressing fear and confusion first, before practical applications)
- Pilot AI tools at specific grade levels with volunteer teachers
- Pair AI tools with high-quality instructional materials
- Establish feedback loops and evaluation criteria with measurable outcomes
- Teach students how to ask good questions of AI tutors—Michigan Virtual's pilot found "my students struggled to ask Khanmigo the correct question. They didn't know what they didn't know" [117]

**Phase 3: Evaluation and Scaling (Months 9-18)**
- Evaluate pilot outcomes against measurable goals (time saved, learning gains, engagement)
- Develop an approved-tools list with vendor accountability requirements (SOC 2 compliance, CIPA/COPPA/FERPA adherence, usage reporting)
- Scale successful tools with clear use policies and ongoing professional development
- Review policies at least annually [3][116][118]

The ExcelinEd model AI Pilot Program Act provides a legislative template requiring eligible platforms to be SOC 2 compliant, certified by a recognized edtech rating organization, and to generate district-level usage reports with parent/student access to AI interaction records [118].

### 9.2 Teacher Training Requirements

The evidence on teacher training is clear: it is the single most important implementation factor, and current provision is inadequate.

- **Current state**: Only 48% of US districts had provided AI training to teachers by fall 2024 (up from 23% in fall 2023), with a stark poverty-based gap—67% of low-poverty districts had trained teachers vs. 39% of high-poverty districts [119]. 96% of teachers report receiving no professional development on AI [2]. A 2024 TALIS survey shows only one in three teachers uses AI, and three of four report lacking knowledge to teach with AI [7].
- **Training models**: The ISTE+ASCD "AI Deep Dive for Educators" is a 15-hour self-paced course [120]. ISTE's AI Explorations program has served over 2,000 educators with free Hands-On AI Projects guides in English, Spanish, and Arabic [121]. RAND's research recommends training that starts with trust-building and AI fundamentals, includes hands-on low-stakes learning and peer structures, and addresses teacher fear first—13 of 14 district leaders interviewed encountered teachers with negative views, and virtually all training was optional [119].
- **Content**: UNESCO's AI Competency Framework for Teachers defines the 15 competencies teachers need across human-centred mindset, AI ethics, AI foundations, AI pedagogy, and AI professional learning [21]. The SREB framework provides an "Artificial Intelligence Literacy for Educators" appendix covering skills and aptitudes for teachers and leaders [28].
- **Time investment**: A 14-week AI-focused pedagogical course significantly improved preservice teachers' AI-TPACK with large effect sizes [27]. A systematic review of 43 empirical studies on teacher PD for AI integration found that technical training alone is insufficient—successful integration requires a combination of pedagogical knowledge, positive attitudes, organizational support, and continuous training, with strong convergence on collaborative practices including Professional Learning Communities [122].

### 9.3 Infrastructure Considerations

CoSN's 2025 State of EdTech District Leadership Report found only 16% of K-12 schools were fully ready for AI, with 61% having dirty or siloed data not operationalizable by AI [123][124]. Key infrastructure requirements include:

- **Bandwidth**: No major AI-specific bandwidth crises yet, but "however much bandwidth you have today, you will need 200 percent more in five years." Networks must handle "microbursts" when all students log on simultaneously [125].
- **Devices**: Low-cost devices like Chromebooks with 2-4 GB of RAM provide poor AI user experiences; districts may need "more girthy hardware" if AI workloads shift to local devices [125].
- **Funding**: The federal E-rate program covers broadband subsidies but not AI operational costs; districts increasingly pay "per-token costs" to providers like AWS or Microsoft Azure, and many districts face "bankruptcy-level conditions" [125].
- **Cybersecurity**: 61% of districts rely on general funds for cybersecurity with no dedicated funding; phishing is the top threat (27% high risk), followed by data breaches and ransomware (13% each) [123].
- **Global equity**: As of 2025, over 2 billion people remained offline, with internet use ranging from over 90% in high-income countries to just 23% in low-income countries. Visits to ChatGPT per internet user are 50 times greater in high-income countries than in low-income countries [126][127]. The World Bank recommends "small AI" approaches—nimble, targeted tools that support teachers without requiring large-scale infrastructure [127].

### 9.4 Academic Integrity and Responsible Use Policies

The research converges on several principles for academic integrity in the age of AIGC:

- **Shift from policing to process**: Massachusetts explicitly recommends against AI detection tools, favoring trust-based, transparency-focused approaches. TeachAI's sample guidance states: "Teachers will not use technologies that purport to identify the use of generative AI to detect cheating and plagiarism, as their accuracy is questionable" [25][128].
- **Require disclosure and citation**: AI use must be disclosed and cited (MLA, APA, Chicago style references provided), and AI cannot be named as a coauthor [60][128].
- **Redesign assessment**: Break large writing assignments into smaller scaffolded chunks, require oral explanations, use process-based and authentic assessments, and focus on "What role did AI play in your process?" rather than "Did you use AI?" [60][129]. Saskatoon Public Schools' adaptation of the AI Assessment Scale placed visual icons on assignments so students see at a glance which AI uses are appropriate, shifting conversations from detecting AI use toward purpose and process [129].
- **Age-appropriate restrictions**: The UAE bans generative AI for students under 13 [81]; Singapore restricts AI use for P1-P3 pupils [43]; ChatGPT requires age 13+ with parental permission for under 18 [113].

---

## 10. Risks, Challenges, and Limitations

### 10.1 Learning and Cognitive Risks

- **Over-reliance and cognitive offloading**: Over 30% of students risk becoming overly dependent on AI tools [16]. An MIT study found users relying on generative AI "may unintentionally hinder deep cognitive processing, retention, and authentic engagement with written material," with brain activity not recovering even when users later relied only on their own minds [130][131].
- **The "yes-bot" problem**: Students blindly accept AI answers or are unable to appropriately select when to use AI—observed in Japan's MEXT pilot results [103]. 49.9% of Japanese girls use AI for consultation or conversations (vs. 23.0% of boys), and around 20% rely entirely on AI for answers [132].
- **Skill erosion**: Over 70% of teachers express concern about skill erosion [2]. A study of 535 Japanese university students found about 36% submitted AI-translated text "as-is" for foreign language assignments [131].

### 10.2 Equity and Access

- Only 11% of US districts rigorously evaluate AI tools for privacy compliance [16].
- Students in low-income and rural areas are least likely to have schools that allow AI integration; 24.7% of working-age population in Global North uses generative AI vs. 14.1% in Global South [1].
- AI adoption remains below 15% in most African and Latin American systems [133].
- Algorithmic bias is documented: a Wisconsin early warning system was wrong nearly 75% of the time in identifying potential dropouts and disproportionately misidentified Black and Hispanic students [134].
- A ChinaTalk analysis notes Chinese households spend an average of 17.1% of annual income on education (vs. 1-2% in US/Japan), raising concerns that wealthy urban students already enjoy AI-guided learning tools, potentially widening rather than narrowing gaps [135].

### 10.3 Teacher and System Challenges

- 68%+ of urban teachers have received no AI training [16]; 45% of educators and 52% of students still lack AI training [89].
- Only 5% of superintendents have formal AI policies in place [95].
- South Korea's AI digital textbook failure demonstrates the risks of top-down implementation without teacher buy-in—a teacher survey found 98.5% of 2,626 respondents considered training insufficient, and a lawsuit was filed by the Korean Teachers and Education Workers Union [105][106].
- The #1 failure pattern: institutions adopt AI tools without intentional design, which can harm learning outcomes rather than improve them [16].

### 10.4 Privacy and Safety

- Only 11% of US districts follow rigorous evaluation measures for AI privacy compliance [16].
- AI-generated deepfakes targeting students have emerged in Australia [133].
- China's classroom surveillance practices—including brain-wave sensing headbands that measure concentration levels sent in real time to teachers and parents—raise significant ethical concerns [136].

---

## 11. Future Trends

### 11.1 Agentic AI

Agentic AI—autonomous AI systems that can plan, make decisions, and take actions across multiple systems—represents the next major shift. Gartner projects 40% of enterprise applications will embed task-specific AI agents by the end of 2026 (up from less than 5% in 2025), and 86% of organizations plan to increase investment, though only 6% trust it [137]. In education, AI agents can cut instructor preparation and grading time by up to 30% and save teachers 8-10 hours per week [137]. UPCEA's analysis predicts 2026 will be the year institutions move "from scattered pilots to governed, agentic workflows," including 24/7 digital concierges, Socratic tutors for every learner, and predictive intervention using LMS behavioral data [138]. Microsoft is embedding Copilot into LMS environments starting Spring 2026 [137]. However, guardrails are essential: instruction-level policies, content filtering, data access controls for FERPA/GDPR/EU AI Act compliance, human-in-the-loop requirements, and fail-safes with rollback to "recommend only" mode [137].

### 11.2 Multimodal AI

Multimodal AI—processing text, images, voice, video, and gestures simultaneously—is expanding classroom possibilities. Applications include science lab assistance (92% accuracy in one study), art critique (8x more iterations), and language learning (2.3x faster fluency gains). Voice-first learning shows 71% retention vs. 58% for text-only [139]. By 2026, 62% of platforms are expected to support voice-first interfaces [139].

### 11.3 Assessment Transformation

The 2026 EDUCAUSE Horizon Report documents a shift "toward authentic, process-based demonstrations of learning" as AI complicates traditional assessments [140]. Some faculty are "moving away from traditional AI-completable assignments toward those emphasizing process, reflection, oral explanation, authentic projects, and critical evaluation of AI outputs" [141]. Google's AI-generated customizable textbooks and AI-powered textbooks are identified as emerging signals [140].

### 11.4 AI Literacy as Core Competency

AI literacy is expected to become a core competency embedded across disciplines by end of 2026 [16]. The PISA 2029 assessment will measure AI literacy globally [94]. China's 2030 goals include an "AI education system covering all stages of schooling" and "a long-term mechanism for AI literacy among all citizens" [86]. Finland's approach—treating AI literacy as a democratic skill—is being adopted as a model across Europe [73][74].

### 11.5 Small AI and Global South Innovation

The World Bank highlights "small AI" approaches—nimble, targeted tools that work in low-resource settings. Examples include uLesson in Nigeria (working offline via SD cards), Kenyan Sign Language translation tools, and RobotsMali producing 180+ culturally relevant children's books in Bambara within a year [127][142]. These offer a "steppingstone toward more advanced AI-enabled transformation by building capacity, trust, and responsible data use" [127].

---

## 12. Actionable Recommendations

### 12.1 For Classroom Teachers

1. **Focus on the problem, not the technology.** Ask whether AI helps solve a specific instructional problem; start slowly and gather local evidence about what works. "Don't let FOMO drive your decisions" [30].
2. **Use AI as a planning partner, not a replacement.** Teachers using ChatGPT saved 31% in planning time while maintaining quality [6]. Use AI for lesson hooks, differentiation, and routine tasks, but maintain your professional judgment and verify all outputs [6][13].
3. **Teach students how to use AI and how not to use it.** Set clear expectations about intended purpose from the start of the year. Michigan Virtual's pilot found students "didn't know what they didn't know"—explicit instruction in questioning AI is essential [117].
4. **Design assessments that reveal thinking.** Use process-based assignments, oral explanations, and scaffolded chunks. Ask "What role did AI play in your process?" rather than policing AI use [60][129].
5. **Never input personally identifiable information** into general-purpose AI tools, and avoid AI detectors as a policing tool—they are unreliable and disproportionately flag neurodivergent and second-language students [60][128].
6. **Invest in your own AI literacy.** Free/low-cost options include ISTE+ASCD's AI Deep Dive ($186-249 for 15 hours), Google's free Educator Series, and ISTE's free Hands-On AI Projects guides [120][121][142].

### 12.2 For School Administrators

1. **Pilot before scaling.** Pair AI tools with high-quality instructional materials, pilot at specific grade levels, gather evidence, and adopt clear AI use policies before districtwide rollout [31].
2. **Establish governance early.** Form a district-wide AI steering committee; develop a principles-based policy (avoid complex policies that are difficult to refine as technology evolves); engage families proactively [3].
3. **Invest in professional learning first.** Address teacher fear and confusion before practical applications; use hands-on, low-stakes learning and peer structures; prioritize training for high-poverty schools where only 39% of teachers have received AI training vs. 67% in low-poverty districts [119].
4. **Plan infrastructure strategically.** Account for wireless "microbursts," device RAM, cloud per-token costs, and cybersecurity. Only 16% of schools are fully ready for AI [123][125].
5. **Budget explicitly for AI.** Include hardware, software, licensing, infrastructure, training, legal guidance, and compliance; conduct ROI analysis [3].
6. **Require vendor accountability.** Select platforms that are SOC 2 compliant, adhere to CIPA/COPPA/FERPA, and generate district-level usage reports with parent/student access to interaction records [118].

### 12.3 For Policymakers

1. **Adopt UNESCO's AI competency frameworks** as international references for national frameworks, teacher training programs, and assessment parameters [19][20][21].
2. **Mandate human-centred regulation.** The EU AI Act and UNESCO guidance provide models: mandate data privacy protection, set age limits for independent GenAI conversations, and require validation of educational AI systems [143][144].
3. **Close the equity gap.** Address the poverty-based AI training gap and the global digital divide (ChatGPT visits per internet user are 50x higher in high-income countries). Invest in foundational digital skills and connectivity; support "small AI" approaches for low-resource settings [119][126][127].
4. **Fund rigorous research.** Support randomized controlled trials and longitudinal studies of AI tutors—currently almost entirely lacking. Explore under-researched contexts: early childhood, special needs, rural settings, and Africa/Middle East/South America [10][18].
5. **Learn from South Korea's reversal.** Top-down AI textbook mandates without teacher buy-in and adequate training fail. South Korea's adoption dropped from 37% to 19% in one semester after teachers reported 98.5% insufficient training [104][105][106].
6. **Prepare for PISA 2029.** AI literacy will be assessed internationally for the first time; embed AI literacy in curricula now [94].
7. **Follow the OECD's guidance**: "GenAI can be a powerful ally for education, but only when guided by pedagogy, policy and a strong commitment to human-centred learning." How GenAI is designed and used matters more than whether it is used at all [12][22].

---

## Sources

[1] 25 AI in Education Statistics to Guide Your Learning Strategy in 2026 (Engageli): https://www.engageli.com/blog/ai-in-education-statistics

[2] How AI Is Reshaping K-12 & Higher Education in the USA 2026 (Third Rock Techkno): https://www.thirdrocktechkno.com/blog/how-ai-is-reshaping-the-future-of-k-12-and-higher-education-in-the-usa

[3] Artificial Intelligence in K–12 Schools (Live Handbook of Education Policy Research): https://livehandbook.org/k-12-education/miscellaneous/k-12-education/school-resources/artificial-intelligence-in-k%E2%80%9312-schools

[4] Six Weeks a Year: How AI Gives Teachers Time Back (Walton Family Foundation / Gallup, June 25, 2025): https://nextgeninsights.waltonfamilyfoundation.org/resources/how-ai-gives-teachers-time-back

[5] 25 AI in Education Statistics (Engageli): https://www.engageli.com/blog/ai-in-education-statistics

[6] Teachers' use of ChatGPT in lesson preparation can save time (Impact Journal, Chartered College of Teaching): https://my.chartered.college/impact_article/teachers-use-of-chatgpt-in-lesson-preparation-can-save-time

[7] Empowering Learners for the Age of AI: An AI Literacy Framework (OECD/European Commission): https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/06/empowering-learners-for-the-age-of-ai_2f8315e7/65cd27d4-en.pdf

[8] AI in the classroom — but not equally across Europe (eudebates.tv): https://www.facebook.com/eudebates.tv/posts/-ai-in-the-classroom-but-not-equally-across-europein-2025-nearly-1-in-3-people-i/1741194766853091

[9] AI in K-12 Education: Global Policies, Outcomes, and Actionable Best Practices (FifthRow): https://www.fifthrow.com/blog/ai-in-k-12-education-global-policies-outcomes-and-actionable-best-practices

[10] Understanding the Evidence Base on AI in K-12 Education (Stanford SCALE): https://scale.stanford.edu/research-in-action/understanding-evidence-base-ai-k12-education

[11] How is ChatGPT impacting schools, really? (Stanford News): https://news.stanford.edu/stories/2025/07/chatgpt-open-ai-impact-schools-education-learning-data-research

[12] OECD Digital Education Outlook 2026: https://digital-skills-jobs.europa.eu/en/latest/news/oecd-digital-education-outlook-2026-how-generative-ai-can-support-learning-when-used

[13] ChatGPT in lesson preparation - Teacher Choices trial (EEF): https://educationendowmentfoundation.org.uk/projects-and-evaluation/projects/choices-in-edtech-using-generative-ai-chatgpt-for-ks3-science-lesson-preparation-2024-teacher-choices-trial

[14] Tutor CoPilot: A Human-AI Approach for Scaling Real-Time Expertise (Stanford EdWorkingPaper No. 24-1054): https://edworkingpapers.com/sites/default/files/ai24-1054.pdf

[15] Tutor CoPilot: A Human-AI Approach for Scaling Real-Time Expertise (NSSA, Stanford): https://nssa.stanford.edu/studies/tutor-copilot-human-ai-approach-scaling-real-time-expertise

[16] AI in Education: The Ultimate Guide for K-12 District Leaders (Panorama Education): https://www.panoramaed.com/blog/ai-in-education-the-ultimate-guide

[17] Generative artificial intelligence in K-12 education: A systematic review (RPTEL, Vol. 21, 2026): https://rptel.apsce.net/index.php/RPTEL/article/view/2026-21034

[18] Generative AI use in K-12 education: a systematic review (Frontiers in Education, Sept 23, 2025): https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2025.1647573/full

[19] UNESCO AI competency framework for students: https://www.unesco.org/en/articles/ai-competency-framework-students

[20] Digital competencies for teachers and school students in Member States (UNESCO G77+China): https://www.unesco.org/en/digital-education/g77-competencies

[21] UNESCO AI competency framework for teachers: https://www.unesco.org/en/articles/ai-competency-framework-teachers

[22] Summary of OECD Digital Education Outlook 2026 (CIDDL): https://ciddl.org/summary-of-oecd-digital-education-outlook-2026

[23] AI4K12 – Sparking Curiosity in AI: https://ai4k12.org

[24] AI Learning Priorities for All K-12 Students (CSTA & AI4K12, 2025): https://csteachers.org/ai-priorities

[25] State AI Guidance for K12 Schools (AI for Education): https://www.aiforeducation.io/ai-resources/state-ai-guidance

[26] Exploring the relationship between teachers' competencies in AI-TPACK and digital proficiency (Hava & Babayiğit, Springer, 2024): https://link.springer.com/article/10.1007/s10639-024-12939-x

[27] Fostering preservice science teachers' AI-TPACK competence (Antonio, JOTSE, Vol 15 No 3, 2025): https://www.jotse.org/index.php/jotse/article/view/3693/1013

[28] Guidance for the Use of AI in the K-12 Classroom (SREB, April 2025): https://www.sreb.org/sites/main/files/file-attachments/2025_ai_in_k-12classroom_guidance.pdf?1744905120=

[29] Khan Academy rolls out AI-powered teaching tools as school districts scale up adoption (Global Society): https://www.globalsociety.earth/post/khan-academy-rolls-out-ai-powered-teaching-tools-as-school-districts-scale-up-adoption

[30] Can an AI-Powered Tutor Produce Meaningful Results? (Education Week / AEI): https://www.aei.org/commentary/can-an-ai-powered-tutor-produce-meaningful-results

[31] 3 questions for K-12 leaders to consider amid the AI tutoring boom (K-12 Dive): https://www.k12dive.com/news/3-questions-for-k-12-leaders-to-consider-amid-the-ai-tutoring-boom/757314

[32] Newark Public Schools plans next rollout of Khanmigo AI tutoring tool (Chalkbeat): https://www.chalkbeat.org/newark/2024/11/15/newark-receives-25k-gates-foundation-grant-to-expand-khanmigo-ai-tutor-chatbot

[33] Newark Public Schools partners with Khan Academy to boost math proficiency (Khan Academy): https://www.khanacademy.org/schools/case-studies/newark-public-schools

[34] This Newark school is already using AI (Bill Gates, Gates Notes): https://www.gatesnotes.com/home/home-page-topic/reader/my-trip-to-the-frontier-of-ai-education

[35] Growing strong literacy skills with Amira (Iowa Department of Education): https://educate.iowa.gov/headline-story/2025-11-04/growing-strong-literacy-skills-amira

[36] Squirrel AI Learning (Official site): https://squirrelai.com

[37] Squirrel AI Learning (HundrED): https://hundred.org/en/innovations/squirrel-ai-learning

[38] Squirrel Ai Learning - AI Adaptive Learning (LinkedIn company page): https://www.linkedin.com/company/squirrelai

[39] Performance Comparison of an AI-Based Adaptive Learning System in China (Cui, Xue, Thai, 2018): https://www.semanticscholar.org/paper/Performance-Comparison-of-an-AI-Based-Adaptive-in-Cui-Xue/14df8fba9313e71c813e3e42825c8922e1e3697a

[40] AI in Education: Transforming Singapore's education system with Student Learning Space (GovTech, Jan 2025): https://www.tech.gov.sg/technews/ai-in-education-transforming-singapore-education-system-with-student-learning-space

[41] AI-enabled Features in SLS (Singapore MOE, updated Aug 4, 2026): https://www.moe.gov.sg/education-in-sg/educational-technology-journey/edtech-masterplan/artificial-intelligence-in-education/ai-enabled-features-sls

[42] Artificial intelligence in education - Singapore (MOE): https://www.moe.gov.sg/education-in-sg/educational-technology-journey/edtech-masterplan/artificial-intelligence-in-education

[43] How MOE Is Using AI for Students in 2026 (SGSchoolKaki, Aug 12, 2026): https://sgschoolkaki.com/blog/ai-in-singapore-schools-moe-students-2026

[44] New MOE plan requires primary, secondary & JC teachers to complete compulsory AI module (MustShareNews): https://mustsharenews.com/moe-teachers-compulsory-ai-modules

[45] Disrupting Education? Experimental Evidence on Technology-Aided Instruction in India (Ganimian, Muralidharan, Singh): https://alejandroganimian.com/files/20190216_Disrupting_education.pdf

[46] Study: AI-Assisted Tutoring Boosts Students' Math Skills (The 74): https://www.the74million.org/article/study-ai-assisted-tutoring-boosts-students-math-skills

[47] AI tutors won't transform education, study finds (LinkedIn - Jamie Martin): https://www.linkedin.com/posts/jamie-martin-a14bb61b_research-on-khan-academy-makes-it-extremely-activity-7361444402449317888-1aRf

[48] New support for teachers powered by Artificial Intelligence (GOV.UK): https://www.gov.uk/government/news/new-support-for-teachers-powered-by-artificial-intelligence

[49] Introducing Aila, our AI-powered lesson assistant (Oak National Academy): https://www.thenational.academy/blog/introducing-aila-for-ai-lesson-planning

[50] Oak Academy asks teachers to trial AI-powered lesson planning tool (EdTech Innovation Hub): https://www.edtechinnovationhub.com/news/oak-asks-teachers-to-trial-ai-powered-lesson-planning-tool

[51] EEF Report Shows ChatGPT Can Cut Lesson Planning Time By 30% (TeachingTimes): https://www.teachingtimes.com/eef-report-shows-teachers-using-chatgpt-can-cut-lesson-planning-time-by-over-30-per-cent

[52] Most Used AI Tools in Classrooms | MagicSchool Wrapped 2025: https://www.magicschool.ai/blog-posts/most-used-classroom-ai-tools-2025

[53] Technology Review of Magic School AI (MDPI Education Sciences): https://www.mdpi.com/2227-7102/15/8/963

[54] AI in Education: The Ultimate Guide (Panorama Education): https://www.panoramaed.com/blog/ai-in-education-the-ultimate-guide

[55] Impact Report 2025: AI readiness in action (aiEDU): https://www.aiedu.org/impact-report-2025-ai-readiness-framework

[56] How AI can improve tutor effectiveness (SCALE Initiative, Stanford): https://scale.stanford.edu/news/how-ai-can-improve-tutor-effectiveness

[57] How Smart Paper Is Transforming Handwritten Assessments at Scale (Tools Competition): https://tools-competition.org/smart-paper-ai-handwritten-assessments-scale-india

[58] iFLYTEK Showcases AI-Driven Innovation at CICBE 2025: https://www.iflytek.com/en/news-events/news/297.html

[59] AI in Education: Use Cases and Real Examples (Third Rock Techkno, 2026): https://www.thirdrocktechkno.com/blog/ai-in-education-top-use-cases-and-real-examples

[60] Teaching academic writing in the age of AI (APA Monitor on Psychology): https://www.apa.org/monitor/2026/04-05/academic-writing-ai-higher-education

[61] Civic Education in the Age of AI (CITE Journal): https://citejournal.org/volume-25/issue-3-25/social-studies/civic-education-in-the-age-of-ai-should-we-trust-ai-generated-lesson-plans

[62] Generative AI Applications for the K–12 Classroom (AVID Open Access): https://avidopenaccess.org/resource/463-generative-ai-applications-for-the-k-12-classroom

[63] Generative AI use in college writing classes (Journal of Writing Research): https://www.jowr.org/jowr/article/view/1762/1030

[64] Teaching Secondary School Essay Writing Using Generative AI (IJRISS): https://rsisinternational.org/journals/ijriss/articles/teaching-secondary-school-essay-writing-using-generative-ai

[65] Generative AI as a lab partner: A case study (Physical Review Physics Education Research): https://link.aps.org/doi/10.1103/ggy1-3kjk

[66] Deep learning based AI-driven teaching models in Chinese high school English class (Frontiers in Education, May 2025): https://www.frontiersin.org/journals/education/articles/10.3389/feduc.2025.1591393/full

[67] "Fun" and "different" – Václav Havel AI aims to help Czech schoolchildren (Radio Prague International): https://english.radio.cz/fun-and-different-vaclav-havel-ai-aims-help-czech-schoolchildren-learn-about-8769577

[68] The AI experiences in education that stand out in Europe (ProFuturo): https://profuturo.education/en/observatory/innovative-solutions/las-experiencias-de-ia-educativa-que-destacan-en-europa

[69] Generative AI Art in School (Edutopia): https://www.edutopia.org/article/generative-ai-art-school

[70] A guide to creating AI-powered art in the classroom (SchoolAI): https://schoolai.com/blog/guide-ai-powered-art-creation-classroom

[71] AI Tool Demo: Making Music With Suno (Edutopia): https://www.edutopia.org/video/ai-tool-demo-music-generation-with-suno

[72] Data-Driven Analysis of Text-Conditioned AI-Generated Music (TISMIR): https://transactions.ismir.net/en/articles/10.5334/tismir.273

[73] Europe's best AI literacy initiative for education comes from Finland (University of Helsinki): https://www.helsinki.fi/en/news/artificial-intelligence/europes-best-ai-literacy-initiative-education-comes-finland

[74] Finland strengthens digital defences with AI and media literacy from young (CNA interview with Minister Anders Adlercreutz): https://www.youtube.com/watch?v=_yI-S9QHJ2o

[75] Artificial intelligence in education – legislation and recommendations (Finnish National Agency for Education): https://www.oph.fi/en/artificial-intelligence-education-legislation-and-recommendations

[76] AI goes to school in the United Arab Emirates (UNESCO Courier): https://courier.unesco.org/en/articles/ai-goes-school-united-arab-emirates

[77] UAE introduces AI as core subject in schools (LinkedIn - Dan Murphy/CNBC): https://www.linkedin.com/posts/danmurphynews_the-uae-just-made-a-huge-shift-in-how-future-activity-7325387838873653248-Cse7

[78] UAE Mandates AI Curriculum in Public Schools (LinkedIn - Mahmood Abdulla): https://www.linkedin.com/posts/mahmood-abdulla-400694244_artificial-intelligence-becomes-a-core-curriculum-activity-7364230211606843392-OLi1

[79] Mind the Innovation Gap: A Roadmap for U.S. Schools After the UAE's AI Surge (Stefan Bauschard): https://stefanbauschard.substack.com/p/mind-the-innovation-gap-a-roadmap

[80] UAE Minister Sarah Al Amiri interview (CNBC/LinkedIn): https://www.linkedin.com/posts/danmurphynews_the-uae-just-made-a-huge-shift-in-how-future-activity-7325387838873653248-Cse7

[81] The UAE Ministry of Education's 2026 manual on Safe and Responsible Use of AI (The UAE Times): https://www.facebook.com/theuaetimes/posts/the-uae-ministry-of-educations-2026-manual-on-safe-and-responsible-use-of-artifi/1343076814527184

[82] US and China's AI education strategies compared (LinkedIn - Alex Wang): https://www.linkedin.com/posts/alexwang2911_ai-education-technology-activity-7321613839978950657-vVcw

[83] China releases list of 184 AI education bases in schools (Gov.cn, Feb 2024): https://english.www.gov.cn/news/202402/23/content_WS65d85f47c6d0868f4e8e44a7.html

[84] AI in education (CHINA POLICY Substack): https://chinapolicy.substack.com/p/ai-in-education

[85] What Is China's AI+Education Action Plan? A Breakdown (David PBL Ross): https://davidpblross.substack.com/p/what-is-chinas-aieducation-action

[86] "AI + Education" Action Plan (CSET Georgetown, July 2026): https://cset.georgetown.edu/publication/china-ai-plus-education-action-plan

[87] China is embracing AI in education. How are principals coping? (UNESCO World Education Blog, Sept 2025): https://world-education-blog.org/2025/09/04/china-is-embracing-ai-in-education-how-are-principals-coping

[88] EMINENT 2025 (European Schoolnet): http://www.eun.org/eminent-2025

[89] Impact Report 2025: AI readiness in action (aiEDU): https://www.aiedu.org/impact-report-2025-ai-readiness-framework

[90] Day of AI | Australian and New Zealand Students Receive Free Curriculum-Aligned AI Literacy: https://dayofai.org/news/australian-and-new-zealand-students-receive-free-curriculum-aligned-ai-literacy-through-tailored-local-programs

[91] Day of AI Aotearoa New Zealand: https://dayofai.org/news/australian-and-new-zealand-students-receive-free-curriculum-aligned-ai-literacy-through-tailored-local-programs

[92] Generative artificial intelligence in Aotearoa New Zealand primary schools—Teacher and student survey findings (NZCER): https://www.nzcer.org.nz/research/publications/generative-artificial-intelligence-aotearoa-new-zealand-primary-schools

[93] U.S. Department of Education Issues Guidance on Artificial Intelligence Use in Schools: http://www.ed.gov/about/news/press-release/us-department-of-education-issues-guidance-artificial-intelligence-use-schools-proposes-additional-supplemental-priority

[94] Legislative Tracker: 2026 State AI in Education Bills (FutureEd, updated July 13, 2026): https://www.future-ed.org/legislative-tracker-2026-state-ai-in-education-bills

[95] 2025 State of AI + CS Education Report (Code.org): https://advocacy.code.org/stateofcs

[96] Germany AI in Education (International Trade Administration): https://www.trade.gov/market-intelligence/germany-ai-education

[97] Generative Artificial Intelligence in Secondary Education (JRC exploratory study): https://euagenda.eu/publications/download/675730

[98] EMINENT 2025 (European Schoolnet): http://www.eun.org/eminent-2025

[99] Back to school in 2025: teaching and learning in the age of AI (Labo Société Numérique): https://labo.societenumerique.gouv.fr/en/articles/dossier-rentree-scolaire-2025-enseigner-et-apprendre-a-lheure-des-ia-et-de-lencadrement-des-usages-numeriques

[100] The Use of AI by Undergraduate Students of Social Education in Spain and Portugal (MDPI Education Sciences): https://www.mdpi.com/2227-7102/15/3/390

[101] AI in Higher Education: Hype or Hope? (Straits Times Education Forum 2026): https://www.youtube.com/watch?v=Zy7ucMmtDmg&vl=en

[102] MEXT Publishes Guidelines on Using Generative AI in Schools (EN-ICHI, Feb 2025): https://ippjapan.org/en_ichi/en/archives/774

[103] Ethical, Legal, and Social Issues in the Use of Generative AI (J-STAGE): https://www.jstage.jst.go.jp/article/itel/5/1/5_5.1.Inv.p002/_pdf/-char/ja

[104] When AI Textbooks Flopped in South Korea — And What the World Can Learn From It (PHI Learning, Nov 2025): https://www.phindia.com/blogs/2025/11/15/when-ai-textbooks-flopped-in-south-korea-and-what-the-world-can-learn-from-it

[105] AI-powered textbooks fail to make the grade in South Korea (Rest of World, 2025): https://restofworld.org/2025/south-korea-ai-textbook

[106] AI Education: South Korea slows down on AI education (Friedrich Naumann Foundation): https://www.freiheit.org/north-and-south-korea/south-korea-slows-down-ai-education

[107] India to introduce AI curriculum in all schools by 2026 (CoinGeek): https://coingeek.com/india-to-introduce-ai-curriculum-in-all-schools-by-2026

[108] AI in Education (PIB India, March 3, 2026): https://www.pib.gov.in/PressReleasePage.aspx?PRID=2234853&reg=3&lang=1

[109] Australian Framework for Generative Artificial Intelligence (AI) in Schools (Australian Government): https://www.education.gov.au/schooling/resources/australian-framework-generative-artificial-intelligence-ai-schools

[110] High school students are using a ChatGPT-style app in an Australia-first trial (The Conversation): https://theconversation.com/high-school-students-are-using-a-chatgpt-style-app-in-an-australia-first-trial-209215

[111] South Australian high schools to embrace new AI tool in two-year trial (Dailymotion): https://www.dailymotion.com/video/x9qlr4k

[112] How AI is being used in our schools (ABC News 7.30, Aug 2025): https://www.youtube.com/watch?v=5nM1faDNcro

[113] Generative AI (New Zealand Ministry of Education, updated 22 May 2026): https://www.education.govt.nz/school/digital-technology/generative-ai

[114] Generative AI in Aotearoa primary schools - Teacher and student use (NZCER webinar): https://www.youtube.com/watch?v=SV4RHj6Or-w

[115] Generative artificial intelligence in Aotearoa New Zealand primary schools (NZCER): https://www.nzcer.org.nz/research/publications/generative-artificial-intelligence-aotearoa-new-zealand-primary-schools

[116] Framework for Implementing Artificial Intelligence (AI) in K-12 Education v1.0 (ILO Group): https://www.ilogroup.com/wp-content/uploads/2024/03/Framework-for-Implementing-Artificial-Intelligence-AI-in-K-12-Education_v1.0.pdf

[117] Have You Considered AI in Your Classroom? A Khanmigo Pilot Story (Michigan Virtual): https://michiganvirtual.org/blog/have-you-considered-ai-in-your-classroom-a-khanmigo-pilot-story

[118] Artificial Intelligence (AI) Pilot Program Act model policy (ExcelinEd, 2025): https://excelined.org/wp-content/uploads/2025/04/2025-AI-Pilot-Program-Model-Policy.pdf

[119] More Districts Are Training Teachers on Artificial Intelligence (RAND, April 8, 2025): https://www.rand.org/pubs/research_reports/RRA956-31.html

[120] ISTE | AI Deep Dive for Educators: https://iste.org/courses/ai-deep-dive-for-educators

[121] ISTE's AI Explorations: https://sites.google.com/docs.iste.org/isteaiandstemnetwork/home

[122] A Systematic Review of Generative AI in K–12: Mapping Goals, Activities, Roles, and Outcomes via the 3P Model (MDPI Systems, 2025): https://www.mdpi.com/2079-8954/13/10/840

[123] CoSN Releases 2025 State of EdTech District Leadership Report (May 6, 2025): https://www.cosn.org/cosn-news/cosn-releases-2025-state-of-edtech-district-leadership-report

[124] CoSN's 2025 State of EdTech Leadership Annual Report Webinar Recording: https://www.cosn.org/tools-and-resources/resource/cosns-2025-state-of-edtech-leadership-annual-report-webinar-recording

[125] What Kind of Infrastructure Will K-12 Schools Need for AI? (GovTech, May 11, 2026): https://www.govtech.com/education/k-12/what-kind-of-infrastructure-will-k-12-schools-need-for-ai

[126] Inequalities in Use of and Exposure to Artificial Intelligence (World Bank Atlas of Global Development 2026): https://data360.worldbank.org/en/atlas/artificial-intelligence

[127] Digital and AI (World Bank): https://www.worldbank.org/ext/en/topic/digital-and-ai

[128] Sample Guidance | AI Guidance for Schools Toolkit (TeachAI): https://www.teachai.org/toolkit-guidance

[129] Case Study: Saskatoon Public Schools and AI Assessment (Leon Furze, April 2026): https://leonfurze.com/2026/04/27/case-study-saskatoon-public-schools-and-ai-assessment

[130] Potential risks of generative artificial intelligence (ScienceDirect): https://www.sciencedirect.com/science/article/pii/S2666920X26000226

[131] Japan schools flooded with machine-generated work as research shows AI saps thinking skills (The Mainichi, July 31, 2026): https://mainichi.jp/english/articles/20260731/p2a/00m/0na/010000c

[132] Survey Finds Many Japanese Teens Using Generative AI (Nippon.com): https://www.nippon.com/en/japan-data/h02692

[133] AI in K-12 Education: Global Policies, Outcomes, and Actionable Best Practices (FifthRow, April 2026): https://www.fifthrow.com/blog/ai-in-k-12-education-global-policies-outcomes-and-actionable-best-practices

[134] AI in K–12 Education (2022–2025): A Comprehensive Landscape Scan: https://weelookang.blogspot.com/2025/07/ai-in-k12-education-20222025.html

[135] China's AI Education Experiment (ChinaTalk - Lily Ottinger): https://www.chinatalk.media/p/chinas-ai-education-experiment

[136] How China Is Using Artificial Intelligence in Classrooms (WSJ, Oct 2019): https://www.youtube.com/watch?v=JMLsHI8aV0g

[137] Agentic AI in Education: Use Cases, 2026 Trends, Playbook (8allocate): https://8allocate.com/blog/agentic-ai-in-education-use-cases-trends-and-implementation-playbook

[138] The Rise of the Agentic AI University in 2026 (UPCEA / Ray Schroeder, Jan 8, 2026): https://upcea.edu/the-rise-of-the-agentic-ai-university-in-2026

[139] AI in Education 2026: 7 Trends Reshaping Teaching (X-Pilot, March 5, 2026): https://www.x-pilot.ai/blog/future-ai-education-2026-trends-report

[140] 2026 EDUCAUSE Horizon Report | Teaching and Learning Edition: https://library.educause.edu/resources/2026/5/2026-educause-horizon-report-teaching-and-learning-edition

[141] EDUCAUSE Horizon Report Finds AI Reshaping Trust, Future of Learning (GovTech, June 2, 2026): https://www.govtech.com/education/higher-ed/educause-horizon-report-finds-ai-reshaping-trust-future-of-learning

[142] Bridging the AI divide in high school STEM education in developing countries (Discover Education, April 2026): https://link.springer.com/article/10.1007/s44217-026-01437-6

[143] Guidance for generative AI in education and research (UNESCO, Sept 2023): https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research

[144] Guidance for generative AI in education and research (UNESCO UNESDOC): https://unesdoc.unesco.org/ark:/48223/pf0000386693.locale=en
