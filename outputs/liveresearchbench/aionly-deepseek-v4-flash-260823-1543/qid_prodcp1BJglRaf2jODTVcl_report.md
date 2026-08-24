# Comparison of Video Conferencing and Collaboration Platforms: Zoom, Microsoft Teams, and Google Meet (August 2026)

## Scope and Data Availability

This report compares video conferencing and collaboration platforms across eight dimensions: video quality, meeting capacity, security, ease of setup/UI, integrations, collaboration features, mobile app functionality, and pricing.

The research findings provided detailed, cited data for **Zoom**, **Microsoft Teams**, and **Google Meet**. No research data was returned for **Cisco Webex**, **Slack Huddles**, **Discord**, or **Adobe Connect**. Per the brief's instruction to note unavailable data explicitly rather than make assumptions, those four platforms are not covered in this report.

Where pricing is concerned, the rates below were verified against official vendor pricing pages where available (Microsoft and Google) and reputable 2026 pricing analyses for Zoom. All prices are in USD for the US market as of August 2026.

---

## Summary Comparison Table

| Dimension | Zoom (Business Plan) | Microsoft Teams (M365 Business Basic) | Google Meet (Workspace Business Starter) |
|---|---|---|---|
| **Max video resolution** | 720p default; 1080p on Business/Enterprise (requires enablement); no 4K for meetings | Up to 1080p @ 30fps for meetings and screen sharing; no 4K | 1080p sending (web since June 2024; ChromeOS hardware since June 2026); up to 4K claimed on iOS app |
| **Meeting capacity** | 300 participants | 300 participants | 100 participants |
| **Meeting duration** | 30 hours | 30 hours | 24 hours |
| **Encryption in transit** | AES-256 GCM (enhanced encryption), TLS 1.2; SRTP for media | TLS 1.2+ with AES-256, SRTP for media; DTLS for E2EE | DTLS/SRTP (IETF standards), TLS; AES-256 at rest |
| **E2EE availability** | Yes — all users can enable; post-quantum E2EE available | 1:1 calls (must be enabled); meetings require Teams Premium | Not available for business accounts; only legacy Duo/personal-account calls |
| **SSO / SAML / 2FA** | SSO/SAML on Business; 2FA/MFA supported | Microsoft Entra ID, SSO, MFA, Conditional Access | Google SSO, 2FA/MFA |
| **Key access controls** | Waiting Room, meeting lock, authentication profiles, host permissions | Lobby, meeting roles, sensitivity labels, watermarks (Premium) | Quick Access (lobby), host controls, up to 25 co-hosts |
| **Setup & UX** | Easy install; mixed reviews of new Zoom Workplace UI | Steep learning curve; deep Microsoft 365 integration | Browser-based, no install; clean, minimal UI |
| **Integration ecosystem** | ~3,000 apps in Zoom App Marketplace | 600+ apps in Teams App Store; deep M365 integration | Native Google Workspace; limited CRM; FigJam/Lucidspark/Miro whiteboards |
| **Whiteboard** | Zoom Whiteboard (unlimited on Business) | Microsoft Whiteboard (native) | Jamboard discontinued (Dec 31, 2024); replaced by FigJam/Lucidspark/Miro |
| **Breakout rooms** | Up to 50 rooms | Yes (meetings under 300 attendees) | Up to 100 rooms (Business Standard and higher) |
| **Mobile app** | Strong parity; screen sharing, host controls | Screen sharing available; no give-control on mobile | Full screen sharing; host controls; breakout room participation |
| **Pricing (US, entry paid business tier)** | **$18.33/user/mo** (annual) or **$21.99/user/mo** (monthly) | **$7.00/user/mo** (annual, effective July 1, 2026) or **$8.40** (monthly) | **$7.00/user/mo** (annual) or **$8.40** (flexible/monthly) |

---

## 1. Video Quality Specifications

### Zoom

Zoom's HD video support is tier-dependent. Per Zoom's official support documentation, standard HD (720p) video is available on Pro and higher plans, while **Full HD (1080p) is limited to Business and Enterprise accounts** (or Pro with Zoom Events/Webinars Plus licenses) and must be enabled by Zoom Support [1]. 1080p also requires an i7 Quad Core (physical core) CPU or higher, the desktop app, and virtual backgrounds must be disabled [1]. A Zoom Community thread confirmed that 720p is the default on Business and that 1080p requires separate enablement [2].

**Zoom does not support 4K for video conferencing meetings.** The Video SDK documentation explains that the client dynamically adjusts resolution based on layout: Speaker View uses 720p (or 1080p if enabled), Gallery View 3×3 uses 360p, 5×5 uses 180p, and 7×7 uses 90p [3].

Bandwidth requirements per official Zoom docs: 720p needs 1.2 Mbps up/down for 1:1 calls and 2.6/1.8 Mbps for group calls; 1080p needs 3.0 Mbps minimum for receiving and 3.8 Mbps for sending [1].

Performance optimization features include noise suppression (with high mode for loud environments), original sound for musicians, touch-up appearance, low-light adjustment, portrait lighting, and autoframing [4][5]. The March 2026 release notes added AI Avatars in meetings, voice translator (beta), and AI-generated virtual background enhancements; the July 2026 release introduced Enhanced Media with high bitrate screen sharing up to 12 Mbps and 60fps content sharing [6]. Recorded video resolution ranges from 360p to 1080p depending on camera HD settings, participant count, and gallery view size [7].

### Microsoft Teams

Microsoft Teams supports **up to 1080p video resolution at up to 30fps** for both video and content where bandwidth is not limited [8][9]. Microsoft states Teams is "always conservative on bandwidth utilization and can deliver HD video quality in under 1.2Mbps" [9][10]. Screen sharing also caps at 1080p; users have requested 4K support, but Microsoft has not enabled it [11].

For **Teams Events** (town halls), 1080p video is available for large-audience events at up to 30fps, requiring approximately 4 Mbps per stream; the platform adaptively downshifts to 720p or 540p if network conditions require it [12].

Official bandwidth guidance: for 1:1 video, minimum 150/150 kbit/s, recommended 1,500/1,500, best 4,000/4,000; for meetings, minimum 150/200, recommended 2,500/4,000, best 4,000/4,000 [10].

AI-powered optimization includes echo cancellation, de-reverberation, full-duplex audio interruptibility, background noise suppression (three levels: Auto, Low, High), real-time screen optimization, AI-based video optimization under bandwidth constraints, and brightness/focus filters [13][14]. Copilot features in 2026 include the Facilitator Agent (AI note-taker), Interpreter (real-time bidirectional translation), and Audio/Video Recap (podcast-style and video-clip meeting summaries) [15].

### Google Meet

Google launched support for **sending full HD 1080p video in Meet on the web in June 2024**, and extended it to ChromeOS-based Meet room hardware on June 10, 2026 [16]. Meet automatically uses 1080p when needed (large screens, pinned video, recordings) and adjusts quality downward under network constraints; there is no admin or user toggle [16]. The Google Meet iOS App Store listing claims support for "up to 4K video quality (bandwidth permitting)" [17].

Bandwidth: Meet requires ~3.8 Mbps upload / 3.2 Mbps download for 1080p, comparable to Zoom's 3.8/3.0 Mbps [18]. Meet uses adaptive streaming and automatic lighting adjustment [16][18].

AI audio/video enhancements include AI-powered noise cancellation (available on free and paid tiers), Studio Sound (AI-enhanced audio for Bluetooth headsets and dial-ins), Studio Look & Lighting (AI-improved visuals), AI-generated backgrounds, and watermarking [19][20]. Gemini in Meet adds "Take notes for me" (automatic structured notes saved to Google Docs), real-time transcription in 8+ languages, and translated captions in 60+ languages [21][22][23].

---

## 2. Meeting Capacity Limits

### Zoom (Business Plan)

The Zoom Business plan supports **300 participants**, consistent across multiple 2026 pricing analyses [24][25][26][27]. Meeting duration is up to **30 hours** on paid licensed plans, per Zoom's official time-limit documentation [28]. The **Large Meeting add-on** can expand capacity: 500 participants ($50/month), 1,000 ($149/month), 3,000 ($990/month), or 5,000 ($2,490/month) [26][27].

### Microsoft Teams (Microsoft 365 Business Basic)

Microsoft 365 Business Basic supports **300 interactive participants** in online meetings and video calls, per official Microsoft documentation [29][30][31]. Meetings, webinars, and town halls have a **30-hour time limit** [31][32]. Webinars on Business Basic/Standard are capped at 300 participants; upgrading to E3/E5 or enabling view-only mode is required for larger audiences [33][34]. For context, Enterprise plans (E3/E5, A3/A5) support 1,000 interactive participants plus up to 10,000 view-only attendees [31][32].

### Google Meet (Workspace Business Starter)

The Google Workspace Business Starter plan supports **100 participants** per meeting. Business Standard supports 150, Business Plus 500, and Enterprise up to 1,000 [35][36][37]. **The limit is determined by the host's plan**, not attendees' plans [37].

All paid Google Workspace plans allow group meetings up to **24 hours**; free accounts are limited to 60-minute group calls (1:1 calls can last 24 hours) [36][38]. Enterprise editions additionally support livestreaming to audiences of up to 100,000 viewers [35].

---

## 3. Core Security Features

### Zoom

**Encryption:** Default Zoom meetings use **256-bit AES-GCM encryption** for media in transit, with keys generated and managed by Zoom's servers [39]. Zoom's encryption whitepaper confirms E2EE uses the same AES-256-GCM algorithm but with keys generated on participants' devices [40]. Zoom 5.0 (April 2020) upgraded encryption from ECB to GCM mode [41]. Zoom Chat is encrypted in transit with TLS 1.2 + AES-256 [42]; Zoom Phone uses SIP over TLS 1.2 with AES-256 and SRTP [43].

**E2EE:** Available to all users (free and paid). Hosts must enable it in the web portal; all participants must use the desktop/mobile app or Zoom Rooms. E2EE disables cloud recording, live transcription, breakout rooms, polling, and AI features [44][45]. **Post-quantum E2EE** (PQ E2EE) is automatically used when all participants run version 6.0.10+ (desktop/mobile) or 6.1.0+ (Zoom Rooms) [44]. Advanced Chat Encryption (ACE) provides device-generated keys for chat [46].

**Authentication:** The Business plan includes **SSO/SAML** and managed domains [27][47]. 2FA/MFA is supported, and authentication profiles allow hosts to restrict meetings to signed-in users, specific domains, or external SSO [48][49].

**Access controls:** Waiting Room, meeting lock, host permissions (mute, remove, restrict screen sharing), "suspend participant activities," watermarks, and role-based access control (RBAC) [48][49][50]. Compliance certifications include SOC 2 Type II, HIPAA (with BAA), GDPR, and FedRAMP [51].

### Microsoft Teams

**Encryption:** All Teams data in transit is encrypted with **TLS 1.2 or later using AES-256**; media streams use **SRTP** [52][53]. Data at rest is encrypted with BitLocker and per-file Azure/SharePoint/OneDrive encryption; organizations can bring their own keys via Microsoft Purview Customer Key [52][53]. The security guide confirms media encryption keys are negotiated via TLS 1.2 + AES-256 (GCM mode) [54].

**E2EE:** Available for **1:1 calls** (disabled by default; both parties must enable it). For **meetings**, E2EE requires a **Teams Premium** license. E2EE covers audio, video, and video-based screen sharing only — not chat, files, or presence [55][56]. E2EE uses DTLS for peer-to-peer media and GKMP for meeting key negotiation over TLS 1.3 [55].

**Authentication:** Teams uses **Microsoft Entra ID (Azure AD)** with Modern Authentication (OAuth 2.0), supporting MFA, SSO, and Conditional Access [54][57].

**Access controls:** Lobby admission rules, meeting roles, anonymous/external/guest access policies, sensitivity labels, watermarks, and screen-capture prevention (Teams Premium) [54][32]. Admin settings include numeric-only meeting passcodes (May 2026) and explicit consent policies for recording 1:1 calls (Feb 2026) [58]. Certifications: ISO 27001, ISO 27018, SOC 1, SOC 2, HIPAA BAA, GDPR [57].

### Google Meet

**Encryption:** All Meet data is encrypted **in transit by default** using IETF standards (**DTLS and SRTP**) and **at rest** [59][60]. Google Cloud's default encryption documentation specifies **AES-256** for data at rest, with AES-GCM (256-bit) as the preferred symmetric cipher [61]. In-transit encryption uses TLS (BoringSSL, FIPS 140-3 validated), ALTS, and post-quantum ML-KEM key derivation [62].

**E2EE:** **Not available for business accounts.** Google Meet business meetings use cloud encryption by default. E2EE ("additional encryption") is only available for calls between personal Google accounts (legacy Duo features); business and EDU accounts always use cloud encryption [59][63]. Client-side encryption is available for Workspace Enterprise Plus and Education Standard, letting organizations manage their own keys [63].

**Authentication:** Google Workspace supports 2FA/MFA and unified SSO via Google Cloud Identity; advanced DLP, endpoint management, and audit logging require Business Plus or Enterprise [64][65].

**Access controls:** Quick Access (the waiting-room/lobby equivalent) allows hosts to require participants to "Ask to Join"; host controls include muting all, locking chat/present/video/audio, removing participants, and ending the call [66]. Up to **25 co-hosts** can be added on eligible Workspace editions [67]. HIPAA compliance is available with Business Plus/Enterprise plus a signed BAA [65][68].

---

## 4. Ease of Setup and User Interface Design

### Zoom

Zoom requires downloading the desktop app (or using the web app); account creation is free. The 2026 "Zoom Workplace" app adds a left-sidebar toolbar and a right-sidebar settings panel [4][5].

UX assessments are mixed. A positive UX review (Appcues) praised Zoom's "3-click journey to value" and strong visual hierarchy, but criticized low-contrast buttons and the easy-to-miss End Meeting button [69]. A TidBITS forum thread documented user frustration with Zoom Workplace's feature bloat and poor Apple Calendar integration, with one user calling it "a disaster" compared to the elegant simplicity of earlier versions [70]. The SaaS CRM Review gives Zoom a UX score of 8/10, noting resource intensity (400–800MB RAM) and pricing complexity as downsides [51].

### Microsoft Teams

Teams is part of the Microsoft 365 ecosystem; installation is straightforward for M365 subscribers. The "New Teams" client (GA October 2023) delivers "up to two times faster app performance" and 50% lower memory usage [57].

The learning curve is steeper than Zoom's. A detailed UX review identified multiple issues: inconsistent padding, confusing back-arrow navigation, redundant settings icons, and an overlay panel with no close button [71]. Users report slow synchronization and notification overload [72]. However, the deep integration with Outlook, SharePoint, and OneDrive is a major strength — creating a team automatically provisions a SharePoint site, an Outlook group, and a workspace [73]. The 2026 masterclass tutorial spans 8 modules, reflecting the platform's breadth [73].

### Google Meet

Google Meet is **browser-based with no software downloads** required, offering full feature parity across Chrome, Safari, Firefox, and Edge [74][75]. Sign-up requires a Google account (personal Gmail or Workspace business email). Meetings are scheduled via Google Calendar with a single click, and joining is link/code/calendar based.

The UI is clean and minimal, integrating deeply with Gmail, Calendar, and Drive. Analysts consistently describe Meet as winning on "integration and simplicity" while Zoom wins on customization and AI features [18][75]. For organizations already on Google Workspace, the learning curve is minimal.

---

## 5. Integration Capabilities

### Zoom

The **Zoom App Marketplace lists nearly 3,000 ready-to-use apps and integrations** (over 3,100 per a June 2026 analysis, with ~1 in 5 new listings being AI-powered) [76][77].

Key integrations include:
- **Calendar/Email:** Google Calendar, Microsoft Outlook (add-in), Zoom Mail & Calendar, Zoom Scheduler ($4.99/user/mo)
- **CRM:** Salesforce (most mature), HubSpot, Pipedrive, Dynamics 365
- **Document suites:** Google Drive, OneDrive/SharePoint, Dropbox, Box
- **Project management:** Asana, Jira, Trello, Monday.com, ServiceNow
- **Team communication:** Slack (/zoom command), Microsoft Teams tab, Gmail add-on
- **Automation:** Zapier (7,000+ apps), Make, Zoom Workflow Automation, Zoom AI Studio [77][78]

AI Companion is included at no additional cost on paid Zoom Workplace plans [51].

### Microsoft Teams

Teams is the hub of the Microsoft 365 ecosystem: files live in SharePoint, calendars sync with Outlook, and Word/Excel/PowerPoint support real-time co-authoring without leaving the app [73][79]. The Teams App Store contains **over 600 apps** [80].

Key integrations:
- **CRM:** Microsoft Dynamics 365 (native), Zoho Desk, Salesforce (via Woobot), CRM as a Service by TeamsWork
- **Project management:** Teamwork.com, Wrike, Asana, Monday.com, ClickUp, Trello, Zoho Projects, Smartsheet, Microsoft Project, Jira Cloud
- **Native tools:** Microsoft Planner, To Do, Approvals, Shifts, Power Automate, Loop, Viva Engage [81][82][83]

Microsoft's new **Project Manager Agent in Teams** uses AI to create plans, assign tasks, and track progress in chat [81].

### Google Meet

Google Meet has **deep native integration with Google Workspace**: Calendar, Gmail, Docs, Slides, Drive, Chat, and Spaces [84][85]. Gemini in Meet writes notes to Google Docs and surfaces them in Gmail [22].

However, CRM integration is limited — **no native Salesforce, HubSpot, or Pipedrive sync** [22]. Project management also requires third-party tools or add-ons [86]. Google has partnered with **FigJam, Lucidspark, and Miro** for whiteboarding, integrated across Meet, Drive, and Calendar [87][88].

---

## 6. Collaboration Features

### Zoom

- **Screen sharing:** Full desktop, application windows, portions of screen, video/audio, second camera; multiple participants can share simultaneously; annotation tools; slide control for presenters [89][90].
- **Whiteboard:** Zoom Whiteboard supports drawing, sticky notes, templates, PDF/image upload, version history, and download as PNG/PDF. Business plans include unlimited whiteboards [91].
- **Breakout rooms:** Up to **50 separate rooms** with full video, audio, chat, whiteboards, and screen sharing; automatic/manual assignment, participant choice, pre-assignment via CSV, broadcast messaging, and "Ask for Help" [92][93]. Each breakout room has its own E2EE key [44].
- **Other tools:** Polls/quizzes, reactions/emojis, immersive view, focus mode, watermarks, AI Companion meeting summaries, and voice translator (GA July 2026) [5][6][94].

### Microsoft Teams

- **Screen sharing:** Share entire screen or window; **Give control / Request control** for interactive collaboration; **Slide control** for up to 20 people to navigate PowerPoint slides; PowerPoint Live presenter mode; Share audio and Optimize for video [95].
- **Whiteboard:** Microsoft Whiteboard is native to Teams with infinite canvas, real-time co-editing, sticky notes, templates, and persistent boards [83]. Unlimited whiteboards for all users [96].
- **Breakout rooms:** Available for meetings under 300 attendees; bulk participant assignment via CSV added June 17, 2026; live captions work in breakout rooms [97][32][58].
- **Together Mode was deprecated for all Teams clients as of June 18, 2026** [98].
- **Other tools:** Live captions in 30+ languages, language interpretation, Copilot (Facilitator Agent, Interpreter, Audio/Video Recap), collaborative notes, branded reactions, and real-time text [15][58][32].

### Google Meet

- **Screen sharing:** Share a tab, window, or entire screen; up to **10 simultaneous presentations**; "Also share tab audio" for tab sharing; some editions can present from a camera [99][100].
- **Whiteboard:** **Jamboard was discontinued on December 31, 2024** (Jamboard devices reached end of life October 1, 2024). Google replaced it with partner integrations: **FigJam, Lucidspark, and Miro**, which can be launched directly within a Meet call [87][88][101].
- **Breakout rooms:** Available on Business Standard and higher; up to **100 breakout rooms**; hosts can pre-assign rooms in Google Calendar, shuffle participants, set timers, and broadcast to rooms. Participants can join from mobile and dial-in [102][103].
- **Other tools:** Live captions in 60+ languages, translated captions, polls, Q&A, hand raising, co-hosts (up to 25), Gemini "Take notes for me" (with a Decisions tracker as of April 2026) [23][67][21].

---

## 7. Mobile App Functionality

### Zoom

Zoom's mobile app (iOS/Android) offers strong feature parity: start/join/schedule meetings, screen sharing, host controls, virtual backgrounds, touch-up appearance, portrait lighting, closed captions, whiteboard access, and AI features [4][104].

- **Android screen sharing:** Photos, documents (PDF/images), Box, Dropbox, Google Drive, OneDrive, website URLs, bookmarks, and whiteboard. Requires Android 5.0+ (official docs specify Android 10.0+ for screen sharing). Device audio is NOT shared during Android screen sharing [90][105].
- **iOS screen sharing:** Screen (iOS 11+), photos, iCloud Drive, Box, Google Drive, OneDrive, website URLs, whiteboard (iPad only). Annotation is not available when sharing the entire screen on iOS [90][105].
- **Host controls on mobile:** Include AI features, chat, participants, share, record, captions, polls, virtual backgrounds, livestream to YouTube (host only), and "Transfer to room" [94]. Hosts can toggle participant screen sharing from mobile [89].

The June 2026 release notes added push notifications for last-minute schedule changes, meeting summary prompts, caption speaker names, and AI-generated virtual background enhancements on mobile [6].

### Microsoft Teams

Teams is available on iOS and Android (iOS 18.0+ / last two major iOS versions; last four major Android versions) [57][106].

- **Screen sharing on mobile:** Available — share PowerPoint, photos, video, screen, or Whiteboard [95].
- **Known limitations:** **Transfer control / Give control is NOT available on mobile** — it's desktop-only [107]. **iOS devices cannot take control of a shared screen** during a meeting; iPad users can only share via the whiteboard feature [108]. Slide control is not supported on mobile [95].
- **Mobile-specific features:** Multi-line calling on Teams Mobile (Aug 2026), Queues app (June 2026), Teams Phone Mobile (SIM-enabled business numbers, call uplift to Teams) [58][109].

### Google Meet

The Google Meet iOS app is rated **4.8/5 stars from 2.3 million ratings**; the Android app is 4.4/5 from 11.5 million reviews [17][75].

- **Screen sharing on mobile:** Mobile shares the entire screen. Android: More → Share screen → Start Sharing; iOS: three-dot menu → Share screen → Start broadcast. Notifications may be visible — Do Not Disturb is recommended [100][99].
- **Host controls on mobile:** Available, including participant management and safety settings [21].
- **Breakout rooms on mobile:** Participants can join breakout rooms and use "Ask for help" / "Return to main call" from updated mobile Meet/Gmail apps; hosts must start breakout rooms from a computer [102].
- **iOS video quality:** Up to 4K (bandwidth permitting) [17]. Gemini "Take notes for me" works on desktop, Android, iPhone, and iPad; "Summary so far" is desktop-only [21].

---

## 8. Pricing (US Market, August 2026)

### Zoom — Business Plan

The Zoom Business plan is priced at **$18.33 per user per month billed annually** ($219.96/year) or **$21.99 per user per month billed monthly** [24][25][26][27]. License range is 1–250 licenses [27][51]. Annual billing saves roughly 16–21% versus monthly [25][51].

What's included: everything in Pro (30-hour meetings, 10GB cloud recording, AI Companion, polling, streaming, Zoom Mail/Calendar) plus 300 attendees, admin portal, SSO, managed domains/company branding, unlimited whiteboards, Zoom Scheduler, and DLP APIs [25][26][27].

Relevant add-ons: Large Meeting (500/$50/mo, 1,000/$149/mo, 3,000/$990/mo, 5,000/$2,490/mo) [26]; Zoom Whiteboard $2.08/user/mo (Plus $5.83) [26]; Zoom Scheduler $4.99/user/mo [26]; Zoom Phone from $10/user/mo [25].

*Note: Zoom pricing figures come from 2026 third-party pricing analyses; the official Zoom pricing page was not among the research sources for this report.*

### Microsoft Teams — Microsoft 365 Business Basic

Microsoft 365 Business Basic is officially priced at **$7.00 per user per month paid yearly** (annual subscription with auto-renewal) [110][111]. This price took effect **July 1, 2026**, up from $6.00 (a 16% increase) [112][113][114]. Monthly billing is approximately **$8.40 per user/month** [115][116].

What's included: web and mobile versions of Word, Excel, PowerPoint, OneNote, Outlook (no desktop apps), Exchange email with custom domain, Teams, OneDrive (1TB/user), SharePoint, Forms/Planner/To Do, Copilot Chat (basic), MFA, SSO, and a 99% uptime guarantee [110][111][116]. Business Basic does **not** include desktop Office apps, Intune, or Defender for Business [110].

For context: Business Standard is $14.00/user/mo (annual) and Business Premium is $22.00/user/mo (annual) as of July 1, 2026 [111][112][113].

### Google Meet — Workspace Business Starter

Google Workspace Business Starter is officially priced at **$7.00 per user per month with annual billing** (1-year commitment, save 16%) or **$8.40 per user per month with flexible/monthly billing** [35][117][118].

What's included: Gmail, 30GB pooled storage per user, Google Meet (up to 100 participants), Calendar, Docs, Chat, AppSheet Core, custom business email, admin controls, and 24/7 support [35][37]. Gemini in Gmail only (basic AI) is included; **full Gemini AI, meeting recording, breakout rooms, noise cancellation, and "Take notes for me" require Business Standard or higher** [21][37][119].

For context: Business Standard is $14.00/user/mo (annual) or $16.80 (flexible); Business Plus is $22.00/user/mo (annual) or $26.40 (flexible) [37][117].

---

## 9. Key Takeaways

- **Capacity:** Zoom Business and Teams (M365 Business Basic) both support 300 participants; Google Meet's entry business plan (Business Starter) caps at 100, with 150 on Standard and 500 on Plus.
- **Video quality:** All three platforms support up to 1080p. Zoom restricts 1080p to Business/Enterprise and requires enablement; Teams and Meet apply it more broadly. None supports 4K for standard meetings (though Meet's iOS listing claims up to 4K bandwidth-permitting).
- **Security:** All three offer AES-256-class encryption in transit and SSO/2FA. Zoom and Teams offer user-facing E2EE (Zoom for all meetings, Teams for 1:1 calls and Premium meetings); Google Meet does not offer E2EE for business accounts.
- **Pricing:** Teams (M365 Business Basic) and Google Meet (Business Starter) are both $7.00/user/mo annually; Zoom Business is substantially more expensive at $18.33/user/mo annually.
- **Ecosystem:** Zoom has the largest app marketplace (~3,000 apps), Teams wins on Microsoft 365 integration depth, and Meet wins on simplicity and native Google Workspace integration.

---

## Sources

[1] Zoom Support — Enabling HD video for Zoom Meetings: https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0066166

[2] Zoom Community — Low video resolution in Zoom meetings: https://community.zoom.com/meetings-2/low-video-resolution-in-zoom-meetings-79209

[3] Zoom Developer Blog — Video Resolution with the Video SDK: https://developers.zoom.us/blog/video-resolution-with-the-video-sdk

[4] YouTube (The Zoom Playground) — How to Use Zoom | Beginner's Guide 2026 Update: https://www.youtube.com/watch?v=pXBLAy8Iqss

[5] YouTube (Patricia Regier) — How to Use Zoom in 2026 | Full Meeting Tutorial & New Features: https://www.youtube.com/watch?v=iGaWVPjMpF4

[6] Zoom Support — Release notes for Zoom Meetings (KB0080363): https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0080363

[7] Zoom Support — Resolution of recorded video (KB0066421): https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0066421

[8] Microsoft Learn — Limits and specifications for Microsoft Teams: https://learn.microsoft.com/en-us/microsoftteams/limits-specifications-teams

[9] Microsoft Q&A — Is there a way to make Teams screen-share or webcam to be good in quality?: https://learn.microsoft.com/en-us/answers/questions/4458408/is-there-a-way-to-make-teams-screen-share-or-webca

[10] Microsoft Learn — Prepare your organization's network for Teams: https://learn.microsoft.com/en-us/microsoftteams/prepare-network

[11] Microsoft Community Hub — Increase video quality for screen sharing: https://techcommunity.microsoft.com/discussions/microsoftteams/increase-video-quality-for-screen-sharing-/3048694

[12] Microsoft Learn — Enable 1080p video resolution for Teams events: https://learn.microsoft.com/en-us/microsoftteams/enable-1080p-video-resolution

[13] Microsoft 365 Blog — How Microsoft Teams uses AI and machine learning to improve calls and meetings: https://www.microsoft.com/en-us/microsoft-365/blog/2022/06/13/how-microsoft-teams-uses-ai-and-machine-learning-to-improve-calls-and-meetings

[14] Microsoft Support — Reduce background noise in Microsoft Teams meetings: https://support.microsoft.com/en-us/teams/meetings/reduce-background-noise-in-microsoft-teams-meetings

[15] YouTube (Mike Tholfsen) — How to Use Copilot in Microsoft Teams Meetings | 5 Powerful Features (2026): https://www.youtube.com/watch?v=l0nh1sYtY5A

[16] Google Workspace Updates — Google Meet now supports sending 1080p HD video from ChromeOS meeting room hardware: https://workspaceupdates.googleblog.com/2026/06/google-meet-now-supports-sending-1080p-HD-video-from-ChromeOS-meeting-room-hardware.html

[17] Apple App Store — Google Meet: https://apps.apple.com/us/app/google-meet/id1096918571

[18] Teleprompter.com — Google Meet vs Zoom: Best Video Meeting App in 2026: https://www.teleprompter.com/blog/google-meet-vs-zoom

[19] Google Workspace — AI for Meetings & Video Conferencing: https://workspace.google.com/resources/ai-for-meetings

[20] Coolpo — How to Improve Video Quality on Google Meet or Zoom?: https://coolpo.io/post/how-to-improve-video-quality-on-google-meet-or-zoom

[21] MeetGeek — Google Meet AI Note Taker: How to Turn On Gemini Notes: https://meetgeek.ai/blog/google-meet-ai

[22] SummarizeMeeting — Google Meet AI Review 2026: Gemini-Powered Notes & Transcription: https://summarizemeeting.com/en/app-reviews/google-meet

[23] Google Blog — Gemini can handle note-taking during Google Meet calls: https://blog.google/products-and-platforms/products/workspace/take-notes-for-me

[24] Secumeet — Zoom Pricing Guide 2026: Plans, Costs, and How to Choose: https://secumeet.com/reviews/zoom-pricing

[25] MeetGeek — Zoom Pricing 2026: Every Plan, Add-On and Real Cost: https://meetgeek.ai/blog/zoom-price-plans

[26] Pumble — Zoom Pricing Guide 2026: Plans, Cost & Value: https://pumble.com/zoom-pricing

[27] TrustRadius — Solved: Zoom Pricing Breakdown for 2026: https://solutions.trustradius.com/buyer-blog/zoom-pricing-breakdown

[28] Zoom Support — Understanding time limits for Zoom Meetings (KB0067966): https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0067966

[29] Microsoft Q&A — Teams attendance limit: https://learn.microsoft.com/en-us/answers/questions/5828670/teams-attendance-limit

[30] Microsoft Learn — Meetings and events feature and capacity comparison: https://learn.microsoft.com/en-us/microsoftteams/meetings-events-feature-comparison

[31] VirtoSoftware — Microsoft Teams Limits: The Complete Specification Guide 2025: https://blog.virtosoftware.com/microsoft-teams-limitations

[32] Microsoft Learn — Meetings and events feature and capacity comparison (updated Aug 7, 2026): https://learn.microsoft.com/en-us/microsoftteams/meetings-events-feature-comparison

[33] Microsoft Q&A — Teams Webinar participant limit, 300 vs 1000 people: https://learn.microsoft.com/en-us/answers/questions/566229/teams-webinar-participant-limit-300-vs-1000-people

[34] Microsoft Q&A — Registration Capacity for Teams Webinar - Business Basic License: https://learn.microsoft.com/en-us/answers/questions/4438498/registration-capacity-for-teams-webinar-business-b

[35] Google Workspace — Compare Flexible Pricing Plan Options: https://workspace.google.com/pricing

[36] UseCarly — Google Meet Participant Limits by Plan (2026): https://www.usecarly.com/blog/google-meet-participant-limit

[37] Google Workspace Help — Business editions: https://knowledge.workspace.google.com/admin/getting-started/editions/business-editions

[38] Convo — Google Meet Time Limit & How to Get Past It (2026): https://www.itsconvo.com/guides/google-meet-time-limit

[39] Tactiq — Is Google Meet Encrypted? Full Guide (2025): https://tactiq.io/learn/is-google-meet-encrypted

[40] Zoom — Encryption Whitepaper (PDF): https://media.zoom.com/download/assets/zoom-encryption-whitepaper.pdf/bc3e8eb2e9ef11ed991baa083779b9cc

[41] Zoom Blog — Zoom Hits Milestone on 90-Day Security Plan, Releases Zoom 5.0: https://www.zoom.com/en/blog/zoom-hits-milestone-on-90-day-security-plan-releases-zoom-5-0

[42] LinkedIn (Rob Grealis) — Zoom Encryption Options: Enhanced vs End-to-End: https://www.linkedin.com/posts/rgrealis_zoom-encryption-in-2025-what-it-really-means-activity-7401425519323275264--tH-

[43] Zoom Support — Encryption for Zoom Phone (KB0069186): https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0069186

[44] Zoom Support — Using end-to-end encryption (E2EE) in Zoom meetings (KB0065408): https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065408

[45] Zoom Blog — Zoom Rolling Out End-to-End Encryption Offering: https://www.zoom.com/en/blog/zoom-rolling-out-end-to-end-encryption-offering

[46] Zoom Support — Setting up advanced chat encryption (KB0065662): https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065662

[47] tldv — Zoom Pricing in 2026: Every Plan, Hidden Cost, and Whether It's Actually Worth It: https://tldv.io/blog/zoom-pricing

[48] Zoom Support — Configuring authentication settings and profiles (KB0061263): https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0061263

[49] SMCCCD ITS — About Zoom Security: https://its.smccd.edu/zoom-security

[50] Valence Security — Essential Guide to Zoom Security: https://www.valencesecurity.com/saas-security-terms/essential-guide-to-zoom-security-safeguarding-your-virtual-meetings

[51] SaaS CRM Review — Zoom Workplace Review 2026: Features, Pricing, Pros & Cons: https://saascrmreview.com/zoom-workplace-review

[52] Microsoft Learn — Encryption in Microsoft Teams: https://learn.microsoft.com/en-us/microsoftteams/teams-encryption

[53] Microsoft Community Hub — Encryption in Microsoft Teams: June 2025: https://techcommunity.microsoft.com/blog/microsoftteamsblog/encryption-in-microsoft-teams-june-2025/4442913

[54] Microsoft Learn — Security guide for Microsoft Teams overview: https://learn.microsoft.com/en-us/microsoftteams/teams-security-guide

[55] Microsoft Learn — End-to-end encryption for Microsoft Teams: https://learn.microsoft.com/en-us/microsoftteams/teams-end-to-end-encryption

[56] InvGate ITDB — Microsoft Teams | Specs, reviews and EoL info: https://invgate.com/itdb/microsoft-teams

[57] InvGate ITDB — Microsoft Teams (specs and system requirements): https://invgate.com/itdb/microsoft-teams

[58] Microsoft Learn — Release notes for Microsoft Teams: https://learn.microsoft.com/en-us/officeupdates/teams-admin

[59] Google Meet Help — Learn about call and meeting encryption in Google Meet: https://support.google.com/meet/answer/12387251?hl=en

[60] Google Blog — Connect confidently with Google Meet security features: https://blog.google/products-and-platforms/products/education/connect-confidently-google-meet-security-features

[61] Google Cloud — Default encryption at rest: https://docs.cloud.google.com/docs/security/encryption/default-encryption

[62] Google Cloud — Encryption in transit for Google Cloud: https://docs.cloud.google.com/docs/security/encryption-in-transit

[63] Google Meet Help — Learn about call and meeting encryption (ZA): https://support.google.com/meet/answer/12387251?hl=en-ZA&ref_topic=14074547

[64] Mailbird — Google Workspace Pricing Changes 2026: Small Business Guide: https://www.getmailbird.com/google-workspace-pricing-small-business-guide

[65] Fortinet — Is Google Meet HIPAA Compliant?: https://www.fortinet.com/resources/articles/is-google-meet-hipaa-compliant

[66] YouTube (Chris Batcher, Crux Learning) — Understanding Security settings in Google Meet: https://www.youtube.com/watch?v=2b3liYvyOTw

[67] Google Meet Community — Co-Hosting: https://support.google.com/meet/thread/333694060/co-hosting?hl=en

[68] Lark — Google Workspace Pricing 2026: Plans, Costs, Hidden Fees: https://www.larksuite.com/en_us/blog/google-workspace-pricing

[69] Appcues (goodux) — A UX review of Zoom's video call experience: https://goodux.appcues.com/blog/zoom-video-call-ux-review

[70] TidBITS Talk — How bad is Zoom Workplace?: https://talk.tidbits.com/t/how-bad-is-zoom-workplace/29115

[71] Medium (Vishnu Moulish) — UX Review #1 of Microsoft Teams: https://moulishvishnu.medium.com/ux-review-1-of-microsoft-teams-a67244ffe74e

[72] Fibery — Microsoft Teams Reviews, Pros & Cons (2026): https://fibery.io/openion/microsoft-teams-76/user-experience-concerns-with-messaging-and-ui-interactions-218649

[73] YouTube (Teacher's Tech) — Getting Started with Microsoft Teams 2026 | Full Tutorial: https://www.youtube.com/watch?v=DnxEyXXl2gE

[74] CheckThat.ai — Google Meet Pricing 2026: Plans, Costs & Real Comparisons: https://checkthat.ai/brands/google-meet/pricing

[75] Lovable — Google Meet vs Zoom 2026: Pricing, Features & Recommendations: https://lovable.dev/guides/google-meet-vs-zoom-which-video-platform-fits-your-team

[76] Zoom — Zoom Apps and Integrations: https://www.zoom.com/en/zoom-apps

[77] Telsys — Best Zoom Integrations 2026: Top Apps for Workflow: https://telsysinc.com/blogs/zoom-integrations-apps-workflow

[78] Zoom Blog — We Now Have More Than 1,000 Apps on the Zoom App Marketplace: https://www.zoom.com/en/blog/we-now-have-more-than-1000-apps-on-the-zoom-app-marketplace

[79] Sherweb — Microsoft Teams mobile app overview: https://www.sherweb.com/blog/microsoft-ecosystem/office-365/microsoft-teams-mobile-app-overview

[80] Mio — Best 46 Microsoft Teams Integrations You Need To Try: https://www.m.io/blog/microsoft-teams-integrations

[81] Teamwork.com — Best Microsoft Teams Project Management Apps (2026): https://www.teamwork.com/blog/microsoft-teams-project-management-apps

[82] ClickUp — Best Project Management Tools that Integrate with Microsoft Teams: https://clickup.com/blog/project-management-tools-that-integrate-with-microsoft-teams

[83] TeamsWork — 10 Best Microsoft Teams Productivity Apps in 2026: https://www.teamswork.app/post/what-productivity-tools-for-microsoft-teams-in-2025

[84] Google Workspace — AI for Meetings & Video Conferencing (integrations): https://workspace.google.com/resources/ai-for-meetings

[85] tldv — How to Take Notes with Gemini on Google Meet: https://tldv.io/blog/gemini-google-meet

[86] Lark — Google Workspace Pricing 2026 (integration notes): https://www.larksuite.com/en_us/blog/google-workspace-pricing

[87] Google Workspace Updates — The next phase of digital whiteboarding for Google Workspace: https://workspaceupdates.googleblog.com/2023/09/the-next-phase-of-digital-whiteboarding-for-google-workspace.html

[88] Google Workspace Blog — Announcing the next phase of digital whiteboarding for Google Workspace: https://workspace.google.com/blog/product-announcements/next-phase-digital-whiteboarding

[89] Zoom Support — Allowing or preventing your meeting participants from screen sharing (KB0058641): https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0058641

[90] Zoom Support — Sharing your screen or desktop on Zoom (KB0060596): https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0060596

[91] SkillPath — The New Zoom Whiteboard: https://skillpath.com/blog/the-new-zoom-whiteboard

[92] Zoom — Breakout Rooms: Create Focused Discussions: https://www.zoom.com/en/products/virtual-meetings/features/breakout-rooms

[93] Vibe — Get Started With Zoom Breakout Rooms for Team Collaboration: https://vibe.us/blog/zoom-breakout-rooms

[94] Zoom Support — Using host and co-host controls in a meeting (KB0065164): https://support.zoom.com/hc/en/article?id=zm_kb&sysparm_article=KB0065164

[95] Microsoft Support — Present content in Microsoft Teams meetings: https://support.microsoft.com/en-us/teams/meetings/present-content-in-microsoft-teams-meetings

[96] GetVoIP — We Compared Zoom vs. Microsoft Teams: 2026 Comparison: https://getvoip.com/blog/zoom-vs-microsoft-teams

[97] Microsoft Q&A — Does MS Teams have captions in break out rooms: https://learn.microsoft.com/en-us/answers/questions/2106501/does-ms-teams-have-captions-in-break-out-rooms

[98] Microsoft Learn — Release notes for Microsoft Teams Rooms: https://learn.microsoft.com/en-us/microsoftteams/rooms/rooms-release-note

[99] Google Meet Help — Present during a video meeting (Android): https://support.google.com/meet/answer/9308856?hl=en&co=GENIE.Platform%3DAndroid

[100] MeetGeek — How to Share Screen on Google Meet on Any Device: https://meetgeek.ai/blog/how-to-share-screen-on-google-meet

[101] Google — Jamboard device end of life information: https://edu.google.com/products/jamboard

[102] Google Workspace Individual Help — Use breakout rooms in Google Meet: https://support.google.com/google-workspace-individual/answer/10099500?hl=en

[103] Google Meet Community — How to assign Google Meet Breakout Rooms in Google Calendar before your meeting starts: https://support.google.com/meet/community-video/205450315/how-to-assign-google-meet-breakout-rooms-in-google-calendar-before-your-meeting-starts?hl=en

[104] YouTube (The Zoom Playground) — Beginner's Guide to Zoom on Mobile (2025): https://www.youtube.com/watch?v=I_a5BPaDDuI

[105] LAPU Course Help — Screen Sharing in Zoom: https://coursehelp.lapu.edu/course-support/conferencing/screen-sharing

[106] NHSmail Support — How to use Microsoft Teams on your mobile (Android and iOS): https://support.nhs.net/knowledge-base/how-to-use-microsoft-teams-on-your-mobile-android-and-ios

[107] Microsoft Q&A — Is it possible to transfer control while screen sharing on a mobile device?: https://learn.microsoft.com/en-us/answers/questions/4443504/is-it-possible-to-transfer-control-while-screen-sh

[108] Microsoft Q&A — How to take control of a shared screen from Teams on iOS: https://learn.microsoft.com/en-us/answers/questions/4440363/how-to-take-control-of-a-shared-screen-from-teams

[109] Microsoft Support — Getting started with Microsoft Teams Phone Mobile: https://support.microsoft.com/en-us/teams/calls-devices/getting-started-with-microsoft-teams-phone-mobile

[110] Microsoft — Microsoft 365 Business Plans and Pricing: https://www.microsoft.com/en-us/microsoft-365/business/microsoft-365-plans-and-pricing

[111] Microsoft Licensing — Microsoft 365 Pricing and Packaging Updates: https://www.microsoft.com/en-us/licensing/news/2026-m365-packaging-pricing-updates

[112] SWK Technologies — Microsoft 365 Price Increases Will Take Effect July 2026: https://www.swktech.com/microsoft-365-price-increases-will-take-effect-july-2026

[113] iFeeltech — Microsoft 365 Price Increase 2026: Business Plan Guide: https://ifeeltech.com/blog/microsoft-365-business-plan-comparison-copilot-2026

[114] Kosh Solutions — Microsoft 365 Prices Are Going Up July 1st 2026: https://www.koshsolutions.com/post/microsoft-365-prices-are-going-up-july-1st-here-s-what-new-mexico-businesses-need-to-know

[115] LazyAdmin — Microsoft 365 Business Plans Compared: https://lazyadmin.nl/office-365/microsoft-365-business-plans

[116] Katy Computer Systems — Microsoft 365 for Small Business: Which Plan Do You Actually Need?: https://katycomputer.com/microsoft-office/microsoft-365-for-small-business-which-plan-do-you-actually-need

[117] Google Workspace Help — Flexible Plan: https://knowledge.workspace.google.com/admin/billing/flexible-plan

[118] EmailVendorSelection — Google Workspace Pricing (2026): How much does it really cost?: https://www.emailvendorselection.com/google-workspace-pricing

[119] Leads Monky — Google Workspace Business Starter USA Price 2026: https://leadsmonky.com/google-workspace-business-starter-usa-price-2026
