# Comprehensive Comparison: Obsidian Plugins for Replicating Notion's Multi-View Database Functionality

## Introduction

As of August 2026, the Obsidian ecosystem has evolved dramatically in its ability to replicate Notion's multi-view database functionality. The landscape includes native core features, actively maintained community plugins, and several discontinued-but-usable options. This report provides a detailed comparison of the most relevant plugins for Table, Kanban, Calendar, and List views, evaluating their strengths, weaknesses, performance, ease of use, compatibility, and overall suitability as a Notion alternative.

The research covers 14+ plugins and systems, including all-in-one solutions (Notion Bases, Make.md, Obsidian native Bases, Projects Plus), specialized view plugins (Kanban, Full Calendar, Dataview), and discontinued plugins that remain relevant for migration contexts (Projects, DB Folder, DataLoom).

---

## 1. All-in-One Multi-View Database Solutions

These plugins provide multiple view types (Table, Kanban, Calendar, List, and more) from a single data source, most closely replicating Notion's unified database approach.

### 1.1 Notion Bases Plugin (by bgarciamoura)

**Overview:** This is currently the most comprehensive Notion-like database plugin for Obsidian, offering 7 views and 18 column types. It is actively maintained with 15,000+ downloads.

**Key Features:**
- **7 database views:** Table, Board (Kanban), Gallery, List, Calendar, Timeline (Gantt), and Chart (bar, line, pie – pure SVG)
- **18 column types:** Title, Text, Number, Select, Multi-select, Checkbox, Date, URL, Email, Phone, Status, Formula, Relation, Lookup, Rollup, Image, Audio, Video
- **Spreadsheet-style formulas:** IF, SUM, AVG, CONCAT, LEFT, ROUND, and more
- **Relations and lookups:** Link databases together and pull values across notes
- **Rollup columns:** 7 aggregation functions for rollup columns
- **Subtasks:** Hierarchical rows up to 3 levels deep
- **Advanced filtering:** Type-aware filters with AND/OR logic, multi-column sorting
- **Column pinning, text wrap, persistent aggregation footer**
- **CSV import/export, bulk actions, live placeholders**
- **Auto-arrange into subfolders**
- **100% local Markdown:** Every row is a .md file, every column is a frontmatter field. Schema stored in `_database.md` frontmatter
- **i18n support:** 7 languages (English, Portuguese, Spanish, French, German, Chinese, Japanese)

**Strengths:**
- Most complete Notion replication available – 5 exclusive views not in Obsidian's native Bases (Board, Gallery, Calendar, Timeline, Chart)
- 12 additional column types beyond Core Bases
- Combines formulas, relations, and rollups in a single plugin
- No lock-in, no cloud, no telemetry
- Fast performance with local Markdown files

**Weaknesses:**
- Score of 37/100 on Obsidian Stats, indicating potential quality or maintenance concerns
- Smaller user base (15k downloads) compared to more established plugins
- Requires Obsidian 1.8.7+
- Dependency on a single developer for long-term maintenance
- No native real-time collaboration (like all Obsidian plugins)

**Links:**
- [Obsidian Community Plugin Page](https://community.obsidian.md/plugins/notion-bases)
- [GitHub Repository](https://github.com/bgarciamoura/obsidian-notion-bases-plugin)
- [Obsidian Stats Page](https://www.obsidianstats.com/plugins/notion-bases)

**User Reviews:** The plugin creator announced it on Reddit: "I built a Notion-like database plugin for Obsidian — 6 views, fully local, no..." with a demo vault of 4 databases and 40+ notes. Users report it as "fast, lag-free" compared to Notion's cloud-based slowness [Reddit, Obsidian Stats].

---

### 1.2 Make.md Plugin

**Overview:** Make.md is an organization and personalization engine for Obsidian that provides a Notion-like experience with Spaces, multiple view types, formulas, and two-way relations. It has 812,000 downloads and is actively maintained (latest version 1.3.5).

**Key Features:**
- **Spaces navigation:** Virtual, customizable navigation pane that can pin folders or tags without affecting file structure
- **Data views:** Table, List, Board (Kanban), Calendar (day/week/month), Gallery, Cards, Catalog, and Flow views – 11 total
- **Properties:** Text, number, date, select, multi-select, tags, formula, link, relation, rollup, aggregate, object, image, repeat
- **Formulas:** Formula property with a large set of functions, formatted similarly to Notion, with number formatting (currency, percentages)
- **Relations:** Two-way relations with sync between linked databases
- **Rollups:** Rollup properties supported
- **Column calculations:** Sum feature at the bottom of columns
- **Sorting, filtering, grouping:** Group by properties, sort/filter data
- **Contexts:** Enhanced tags that can have custom properties (e.g., an #assignment tag can have a due date and course)
- **Customization:** Spaces can become dashboards with labels, images, stickers, covers; notes can have stickers and cover banners
- **Note formatting:** Tooltip for selected text, slash command menu, embedded media support

**Strengths:**
- Most comprehensive feature set of any Obsidian database plugin – 11 view types
- Active development with frequent updates
- No coding required – works without any code or 3rd party dependencies
- Large user base (812,000 downloads, 2,000 GitHub stars)
- Two-way relations with sync between linked databases
- Full formula support similar to Notion
- Cross-platform (desktop and mobile)
- Free and open source (MIT license)

**Weaknesses:**
- Known to be buggy – 184+ open GitHub issues
- Some features still in early development
- No automation, collaboration, or sharing features
- YAML front matter conflicts with other plugins (can disable context field sync)
- Requires manual configuration change for Obsidian Sync
- Some users report it being resource-intensive

**Links:**
- [Obsidian Community Plugin Page](https://community.obsidian.md/plugins/make-md)
- [GitHub Repository](https://github.com/Make-md/makemd)
- [Official Website](https://www.make.md)
- [Obsidian Stats Page](https://www.obsidianstats.com/plugins/make-md)

**User Reviews:** A PhD student writing in 2026 describes rebuilding their workflow with Make.md as one of five key plugins. A YouTube reviewer (Antone Heyward, April 2025) states: "If you use this make.md plugin I think you could pretty much get the same type of stuff that you would use in notion over in Obsidian and have the benefit of being fully offline." However, forum users report persistent bugs: "I've sort of stopped using MAKE.md because, like you said, it seems to be more of an inconvenience than a plus. I've decided to wait until it becomes a bit more stable" [Obsidian Forum].

---

### 1.3 Obsidian Native Bases (Core Plugin)

**Overview:** Obsidian Bases is a core plugin (not a community plugin) introduced in Obsidian 1.9 (mid-2025) that provides native database-like views. It is built directly into Obsidian, ensuring stability and future compatibility.

**Key Features:**
- **View types:** Table (rows and columns), List (bulleted or numbered), Cards (grid with images), Map (interactive pins)
- **Data source:** Works globally across the entire vault by default – uses all notes, then filters down
- **Multiple views per base:** Each base can have multiple views with different filters and configurations
- **Real-time property editing:** Edit properties directly in the table
- **Formulas:** Supports formula functions including TODAY(), DAYS(), IF(), etc.
- **Filters:** Sort, filter, and group notes
- **Embedding:** Bases can be embedded in notes
- **Configurations saved as .base files:** Reusable configurations
- **Roadmap:** Planned Kanban view, Calendar view, Publish support, and API for plugins

**Strengths:**
- **Built into Obsidian** – no separate installation, guaranteed stability, and future compatibility
- **Fast performance** – "Bases loads everything instantly—even in vaults with thousands of notes—something that older solutions struggled with"
- **Global data scope** – works with your entire vault by default (unlike Notion's database-per-folder approach)
- **No learning curve** for basic use – "Getting started with Obsidian Bases takes only five minutes"
- **Free** – included with Obsidian at no cost
- **Active development** by the Obsidian team with a public roadmap

**Weaknesses:**
- **Limited view types** – currently only Table, List, Cards, and Map (no Kanban, Calendar, Gallery, Timeline)
- **No Kanban view yet** – feature requested but not delivered (though community plugins can add it)
- **No relations or rollups** – no native cross-note relation linking or aggregation
- **No inline fields support** – only works with frontmatter properties
- **Limited formulas** – basic formulas only; no aggregation (SUM, AVG) across notes yet
- **No Calendar view** – planned but not yet available

**Links:**
- [Obsidian Help - Bases Documentation](https://obsidian.md/help/bases)
- [Obsidian Roadmap](https://obsidian.md/roadmap)

**User Reviews:** "Bases brings the power of data view to everyone in a much more accessible way. I could see this single plugin, Obsidian Bases, causing more people to switch from Notion to Obsidian than any other feature. The speed is incredible. It's way faster than data view or notion" [YouTube, wanderloots]. "Obsidian Bases and Notion Database are essentially the same thing. In most cases, they can accomplish similar tasks" [Obsidian Forum, user Moy]. "I Stopped Envying Notion the Day Obsidian Shipped Bases" [Medium, Len, June 2026].

---

### 1.4 Projects Plus Plugin (by ParkPavel) – Revival Fork

**Overview:** This is a community revival fork of the discontinued Obsidian Projects plugin (by Marcus Olsson). It is currently in active development (version 3.5.1-alpha) and available via BRAT, pending official community plugin approval.

**Key Features:**
- **Table view:** Editable fields that write back to YAML frontmatter
- **Board (Kanban) view:** With column persistence and note creation inheriting filters
- **Calendar view:** Full planner calendar with start/end dates and times, color coding, infinite scroll, mobile gestures
- **Gallery view:** Card grid with optional cover images
- **Dashboard V2:** In development with reactive linked blocks, multi-select filtering, 115+ formula functions, Dataview bridge
- **Agenda 2.0:** With advanced filter operators
- **Data sources:** Three options – folder, tag, or Dataview query
- **Note templates and autosave**
- **Smart hints:** Writing in the "status" field suggests values already in the project
- **Mobile support:** Swipes, gestures, enlarged buttons
- **Demo project:** 35+ notes (tasks, meetings, projects, diary) created on first launch
- **Custom View API:** Allows third-party plugins to register views

**Strengths:**
- Directly revives the popular Projects plugin with new features and fixes
- Multi-view system (Table, Board, Calendar, Gallery, Dashboard) from a single data source
- "Leave no trace" philosophy – no plugin-specific metadata in notes
- Smart hints, mobile support, localization (RU, EN, UA, ZH-CN)
- Active development with a public roadmap

**Weaknesses:**
- **Beta software** – version 3.5.1-alpha, with known bugs (row count divergence, Kanban status dropdown issues)
- **Not yet in official community plugin store** – must be installed via BRAT
- **Unknown long-term viability** – depends on a single developer
- **Some original bugs may persist** – the original Projects plugin had unresolved issues (column width reset, field creation bugs)
- **No formulas, relations, or rollups** – not supported in the current version (Dashboard V2 may add formulas)

**Links:**
- [GitHub Repository](https://github.com/ParkPavel/obs-projects-plus)
- [Obsidian Forum Discussion](https://forum.obsidian.md/t/projects-plus-plugin/106826)
- [Reddit Announcement](https://www.reddit.com/r/ObsidianMD/comments/1qpg6as/projects_is_back)

**User Reviews:** The developer states: "I just finished reanimating the Projects plugin from Marcus Olson. And I've made some new improvements as best I can." Users report bugs: "It feels a bit buggy for now. For example in Kanban view 'Status' dropdown menu is not show List type properties." The developer treats the current state as a beta-testing phase [Obsidian Forum].

---

## 2. Specialized View Plugins

These plugins focus on a single view type (or a few) and can be combined to create a multi-view system.

### 2.1 Kanban Plugin (by mgmeyers)

**Overview:** The original Kanban plugin for Obsidian creates markdown-backed Kanban boards. It has 2.4 million downloads but is **seeking new maintainers** – the latest version (2.0.51) was released approximately 2 years ago.

**Key Features:**
- **Three view modes:** Kanban, stacked vertical list, and table view
- **Native markdown editor for cards:** Supports tag and link autocompletion, dataview queries in cards
- **Collapsible lanes, drag-and-drop cards between columns**
- **Right-click card movement:** "Move to list" submenu
- **Sorting by tags** with explicit tag sort order
- **Inline dataview metadata recognition**
- **Tasks plugin integration:** Tasks autosuggest, dates, other Task data in card footer
- **Date/time picker (triggered by @@)**
- **Date/time archiving, archive all completed cards command**
- **Convert empty note to Kanban board command**
- **Search boards using default search hotkey**
- **Double-click editing** for cards and lane titles
- **Custom grouping by text properties**
- **Side-pane filtering/grouping/sorting, persistent board selection**
- **WIP (Work-in-Progress) limits**
- **Note creation from cards with optional templates**
- **Drag-and-drop existing notes into the board**
- **Linked page metadata display**
- **Per-board settings** (different note templates for different boards)
- **Inbox board for quick capture**

**Strengths:**
- Simple, plain text markdown-based storage – board content is editable and linkable like regular notes
- High level of polish and visual quality
- Strong integration with Tasks and Dataview plugins
- Three view modes (Kanban, list, table)
- Per-board configuration
- Drag-and-drop between boards
- 2.4 million downloads – most popular Kanban plugin

**Weaknesses:**
- **No longer actively maintained** – seeking new maintainers
- **No single-card view** – cannot view just one card
- **Scattered documentation**
- **Tag filtering issues** reported by some users
- **Developer responsiveness concerns** – "I no longer have the bandwidth to maintain the Kanban plugin (and haven't for a while)"
- **Code complexity** – "The plugin's code is kind of a mess in spots"
- **No subtasks** in the standard version (though table view subtasks were planned)

**Links:**
- [Obsidian Community Plugin Page](https://community.obsidian.md/plugins/obsidian-kanban)
- [GitHub Repository](https://github.com/mgmeyers/obsidian-kanban)
- [Primary Documentation](https://publish.obsidian.md/kanban/)
- [Obsidian Forum Thread](https://forum.obsidian.md/t/kanban-plugin/17082)
- [Obsidian Stats Page](https://www.obsidianstats.com/plugins/obsidian-kanban)

**User Reviews:** "This is very polished, both visually and functionally. I've found it immensely more useful than any of the other Kanban implementations so far" [Obsidian Forum]. "For a creator like me, who always has a lot of ideas in play at all times but didn't have an efficient way to manage my workflow, the capabilities provided by the Kanban for Obsidian plugin are invaluable!" [Mind Mapping Software Blog].

---

### 2.2 Kanban Action Planner (by Sébastien Dubois)

**Overview:** This plugin adds Kanban board views to Obsidian's native Bases, offering multiple view types (board, calendar, timeline, WBS, triage) within a single plugin. It is actively maintained (latest version 1.12.0, released July 29, 2026).

**Key Features:**
- **Multiple views:** Kanban board, Calendar (day/week/month/quarter/year), Timeline (Gantt-style), WBS (Work Breakdown Structure) tree view, Triage mode (one-card-at-a-time backlog clearing)
- **Swimlanes:** Auto-grouping by note type or property
- **GTD contexts:** @work, @home, @errands, @calls, @deep-work – filtering by where/how a task can be done
- **Jira-like filter bar:** Compact query language for filtering as you type
- **Relationship navigation:** Parent/child/blocked-by relationships
- **Focus on subtrees:** Drill down into child notes
- **Automation rules per note type:** IF-THEN rules that update progress, dates, tags, and folders automatically when status changes
- **WIP (Work-in-Progress) limits**
- **Multi-select cards, bulk actions, color coding, per-view configuration**
- **Embeddable boards in notes:** With ephemeral mode/filter/height overrides
- **Hover page preview** in calendar, timeline, and WBS modes
- **Touch-friendly drag gestures** and popout-window drag support
- **Quick capture with templates, per-note-type configuration**
- **Archiving**

**Strengths:**
- Rich set of views (board, calendar, timeline, WBS, triage) in a single plugin
- True file-over-app principle – no proprietary database or lock-in
- GTD context integration for workflow filtering
- Automation rules per note type – unique among Obsidian plugins
- Integration with Obsidian Bases (modern Obsidian architecture)
- Open source MIT license

**Weaknesses:**
- **Desktop only** – no mobile support
- **Requires Obsidian 1.12+** (Bases view API), limiting compatibility with older versions
- **Still in active development** – features delivered milestone by milestone
- **Low community adoption** – rating of 35/100 on Obsidian Stats with no reviews
- **Open issues** – spaced repetition reviews, agenda/today view, sub-boards still pending

**Links:**
- [Obsidian Community Plugin Page](https://community.obsidian.md/plugins/kanban-action-planner)
- [GitHub Repository](https://github.com/dsebastien/obsidian-kanban-action-planner)
- [Documentation Site](https://dsebastien.github.io/obsidian-kanban-action-planner)
- [Obsidian Stats Page](https://www.obsidianstats.com/plugins/kanban-action-planner)

**User Reviews:** The developer describes the philosophy: "Everything is driven by your existing note properties, and every change is written straight back to your frontmatter. The board is just a lens that lets you rearrange them. There's no hidden database and no lock-in" [Author's blog]. The plugin is pre-configured for the Obsidian Starter Kit.

---

### 2.3 Full Calendar and Full Calendar Remastered

#### Original Full Calendar (by Davis Haupt)

**Overview:** Integrates the FullCalendar library into Obsidian, allowing users to manage events as individual notes with frontmatter. The original repository was **archived on August 1, 2026** and is now read-only. Latest version 0.10.7, released over 3 years ago.

**Key Features:**
- Each event stored as a separate note with special frontmatter
- Two-way sync between calendar and underlying notes
- Read-only Google Calendar sync (via ICS and CalDAV)
- Multiple local calendars with accent colors
- Dark mode support using Obsidian CSS variables
- Full mobile support
- Create events by clicking and dragging
- Recurring events
- Templates for events
- DataviewJS API for rendering events
- Events from frontmatter or daily notes

**Strengths:**
- Events are markdown notes – can take notes, form connections, add context
- Two-way sync between calendar UI and note metadata
- Read-only ICS and CalDAV remote calendars
- Active during its time (449k downloads, 991 stars)

**Weaknesses:**
- **Archived and unmaintained** – no further updates, bug fixes, or security patches
- **No official multi-day event support** – workaround exists but is unreliable
- **Remote events are read-only** – only local events can be edited
- **Mobile usage is difficult**
- **Cannot share calendars**
- **Inactivity for over 3 years** – likely to break with future Obsidian updates

**Links:**
- [Obsidian Community Plugin Page](https://community.obsidian.md/plugins/obsidian-full-calendar)
- [GitHub Repository (Archived)](https://github.com/obsidian-community/obsidian-full-calendar)
- [Primary Documentation](https://obsidian-community.github.io/obsidian-full-calendar)
- [Obsidian Stats Page](https://www.obsidianstats.com/plugins/obsidian-full-calendar)

#### Full Calendar Remastered (Active Fork)

**Overview:** A major community fork of the original Full Calendar plugin, actively maintained with two-way CalDAV and Google Calendar sync. Latest version 0.13.5, 33,000 downloads.

**Key Features:**
- Multiple calendar sources: Full Note (frontmatter), Daily Note, ICS (read-only), CalDAV (two-way sync), Google Calendar (two-way sync)
- Integrations with Obsidian Tasks, TaskNote, and ActivityWatcher
- Drag-and-drop task scheduling via Obsidian Tasks plugin
- Automated activity tracking from ActivityWatch
- Chrono Analyser dashboard for time analysis
- Performance with staged loading, timezone/DST hardening
- Availability Sharing
- Enhanced ICS export filters
- Event Linked Notes presets
- Improved mobile UX
- Refined Google account scope handling
- Unified task backlog and Google Tasks integration

**Strengths:**
- All original features plus two-way CalDAV and Google Calendar sync
- Active development with frequent updates (latest Aug 2026)
- Performance improvements (staged loading, timezone hardening)
- Mobile UX improvements
- Integrations with Tasks, TaskNote, ActivityWatcher

**Weaknesses:**
- iOS month view reportedly broken
- Large bundle size (7.2 MB main.js, 380 ms load time; lean build available)
- Google Calendar events cannot be hidden (streamed real-time, not stored locally)
- Smaller user base than the original (33k vs 449k downloads)

**Links:**
- [Obsidian Community Plugin Page](https://community.obsidian.md/plugins/full-calendar-remastered)
- [GitHub Organization](https://github.com/obsidian-full-calendar-remastered)
- [Documentation](https://obsidian-full-calendar-remastered.github.io/plugin-full-calendar)

---

### 2.4 Dataview Plugin

**Overview:** Dataview is a live index and query engine that transforms your Obsidian vault into a queryable database. It is the most powerful querying plugin in Obsidian (9.2k GitHub stars, 3.2M downloads) but is not a visual database editor – it displays data in code blocks.

**Key Features:**
- **Four query output formats:** LIST, TABLE, TASK, CALENDAR
- **Four query modes:** Dataview Query Language (DQL), Inline Expressions, DataviewJS, Inline JS Expressions
- **Data sources:** YAML frontmatter, inline fields (Key:: Value), tags, lists
- **Query structure:** FROM, WHERE, SORT, FLATTEN, GROUP BY, LIMIT
- **Security:** DQL queries are sandboxed (read-only); JavaScript queries have full access
- **High performance:** "scaling up to hundreds of thousands of annotated notes without issue"
- **Dynamic updates:** Changes to notes automatically update query results
- **Extensive ecosystem:** 34+ companion plugins tagged #dataview, multiple web-based query builders

**Strengths:**
- **Most powerful querying plugin** – transforms notes into a queryable database with SQL-like language
- **High performance** – uses in-memory cache for fast queries
- **Flexibility** – four query modes and four output formats
- **Dynamic updates** – changes automatically reflected
- **Read-only safety** – DQL is sandboxed and cannot modify notes
- **Open source** (MIT license) with large community (9.2k stars, 3.2M downloads)
- **Extensive documentation** and learning resources

**Weaknesses:**
- **Steep learning curve** – requires learning DQL or JavaScript; "one of the biggest barriers to using Dataview effectively is having to learn and remember how to create Dataview queries"
- **Not WYSIWYG** – no visual editor; requires writing code
- **Read-only (mostly)** – cannot edit note properties in the table view (except task checking)
- **No native collaboration**
- **Development stalled** – "Dataview hasn't been updated since June" (as of 2025); the successor Datacore is in beta
- **Portability concerns** – Dataview code blocks don't render in other markdown applications
- **No full-text content search** – only searches metadata, not note content
- **Calendar view reportedly buggy**

**Links:**
- [Obsidian Community Plugin Page](https://community.obsidian.md/plugins/dataview)
- [GitHub Repository](https://github.com/blacksmithgu/obsidian-dataview)
- [Primary Documentation](https://blacksmithgu.github.io/obsidian-dataview)
- [Obsidian Stats Page](https://www.obsidianstats.com/plugins/dataview)

**User Reviews:** "Dataview is incredible. Being able to query plain text notes and their metadata has been transformative for my workflow. It has allowed me to move virtually all my thought processing work into Obsidian" – Kepano (Minimal theme creator) [Hacker News]. "Dataview comes the closest to it. I can make a query and show a table with all the note properties, but I can't check them off or edit the properties in the table" [Obsidian Forum].

---

## 3. Discontinued Plugins (Migration Context)

These plugins are no longer maintained but are relevant for users who may need to migrate existing workflows.

### 3.1 Obsidian Projects Plugin (by Marcus Olsson) – Discontinued

**Status:** Discontinued by the developer in May 2025. The GitHub repository was archived on July 18, 2025, and the plugin was removed from the Obsidian community plugin list. It can still be installed via BRAT.

**Key Features (When Active):**
- Table, Board (Kanban), Calendar, and Gallery views
- Folder-based, tag-based, or Dataview-query-based data sources
- Inline editing in table view
- Sorting, filtering (AND-based)
- "Leave no trace" philosophy – no plugin-specific metadata
- Dataview integration (read-only for Dataview queries)

**Why It Was Significant:**
- Was the most direct Notion database replica for Obsidian
- Pioneered multi-view system from a single data source
- 1.9k GitHub stars, 150 forks
- Inspired much of the current Obsidian database ecosystem, including native Bases

**Critical Warning:** "No further updates, bug fixes, or compatibility patches will ever be released. The plugin will likely break with future Obsidian updates as the API evolves" [Official announcement].

**Links:**
- [GitHub Repository (Archived)](https://github.com/obsmd-projects/obsidian-projects)
- [Official Announcement](https://marcusolsson.dev/announcing-obsidian-projects)
- [Obsidian Forum Discussion](https://forum.obsidian.md/t/development-for-projects-plugin-needed/101089)

---

### 3.2 DB Folder Plugin (by RafaelGB) – Archived

**Status:** Repository archived on July 28, 2025, now read-only. Latest version 3.5.1 (January 19, 2024). Requires Dataview plugin.

**Key Features:**
- Notion-like database based on folders, links, tags, or Dataview queries
- Column types: text, number, select, tag, checkbox, date, date-time, formula
- Relations and rollups (introduced in v2.8.0, bidirectional in v3.3.0-beta.1)
- JavaScript formulas (experimental)
- Sorting, filtering (AND/OR logic), grouping
- CSV import/export
- Templates for new files
- Mobile support (v2.5.0+)

**Why It Was Significant:**
- Mature and stable (99 releases, 1.4k stars)
- Built on Dataview – leveraged its powerful query engine
- Popular for users who wanted a spreadsheet-like interface without learning Dataview syntax

**Critical Warning:** "The repository was archived on July 28, 2025, and is now read-only. No further development or bug fixes will be provided" [GitHub].

**Links:**
- [GitHub Repository (Archived)](https://github.com/RafaelGB/obsidian-db-folder)
- [Documentation Site](https://rafaelgb.github.io/obsidian-db-folder)
- [Changelog](https://rafaelgb.github.io/obsidian-db-folder/changelog)

---

### 3.3 DataLoom (formerly Notion-Like Tables) – Discontinued

**Status:** Plugin removed from the Obsidian community list on May 2, 2025. GitHub repository archived on March 9, 2025. No longer installable.

**Key Features (When Active):**
- Table view with multiple cell types (text, number, checkbox, embed, file, date, tag)
- Column and row management
- CSV/Markdown import/export
- Light/dark color schemes
- Undo/redo
- Folder/frontmatter sources
- Mobile support

**Critical Warning:** "Users are advised to export existing DataLoom files to raw markdown format for use with Obsidian's native table editor" [GitHub].

**Links:**
- [GitHub Repository (Archived)](https://github.com/decaf-dev/obsidian-dataloom)
- [Reddit Discussion](https://www.reddit.com/r/ObsidianMD/comments/1k9arl1/db_folder)

---

## 4. Comparison Table: All-in-One Plugins

| Feature | Notion Bases | Make.md | Obsidian Bases (Core) | Projects Plus |
|---------|-------------|---------|----------------------|---------------|
| **Table View** | ✅ | ✅ | ✅ | ✅ |
| **Kanban/Board View** | ✅ | ✅ | ❌ (Planned) | ✅ |
| **Calendar View** | ✅ | ✅ | ❌ (Planned) | ✅ |
| **Gallery View** | ✅ | ✅ | ❌ | ✅ |
| **List View** | ✅ | ✅ | ✅ | ❌ |
| **Timeline/Gantt** | ✅ | ❌ | ❌ | ❌ |
| **Chart View** | ✅ | ❌ | ❌ | ❌ |
| **Formulas** | ✅ (Spreadsheet-style) | ✅ (Notion-like) | ✅ (Basic) | ❌ (Planned in Dashboard V2) |
| **Relations** | ✅ | ✅ | ❌ | ❌ |
| **Rollups** | ✅ | ✅ | ❌ | ❌ |
| **Lookups** | ✅ | ❌ | ❌ | ❌ |
| **Subtasks** | ✅ (3 levels) | ❌ | ❌ | ❌ |
| **AND/OR Filters** | ✅ | ✅ | ✅ | ❌ (AND only) |
| **Mobile Support** | ✅ | ✅ | ✅ | ✅ |
| **Active Maintenance** | ✅ | ✅ | ✅ | ✅ (Beta) |
| **Downloads** | 15k | 812k | N/A (Core) | ~1k (BRAT) |
| **Cost** | Free | Free | Free | Free |
| **License** | GPL v3 | MIT | Proprietary | Apache 2.0 |
| **Obsidian Version** | 1.8.7+ | 0.16.0+ | Included | 1.0.0+ |

---

## 5. Combining Plugins for a Multi-View System

### 5.1 Native Integration Between Plugins

Several plugins can be combined to create a comprehensive multi-view system:

- **Kanban + Full Calendar Remastered:** The Kanban Plus fork includes "copying list items to a calendar view (integrating with Full Calendar)" as a modular feature. A pull request by Geet Duggal adds the ability to copy Kanban cards to Full Calendar as events.

- **Kanban + Dataview:** A writing workflow can use the Kanban plugin for boards and Dataview for querying article status from YAML metadata. This maintains data in notes while providing different views.

- **Kanban + Templater + QuickAdd + Kanban Status Updater:** A system to replace the discontinued Projects plugin, with automatic note templates and automatic status updates when cards move between columns.

- **Bases + Calendar Bases:** Building a master content calendar using the Bases core plugin and a beta community plugin (Obsidian Calendar Bases with Full Calendar) to aggregate notes from multiple folders with date properties.

### 5.2 Unified Multi-View Plugins

- **Planner Plugin (SawyerRensel/Planner):** Integrates calendar, Kanban, timeline, and task list views in a single plugin. Uses Obsidian's Bases feature and stores data in plain Markdown files with YAML frontmatter. Features include: four powerful views (Calendar with six layouts, Kanban with drag-and-drop and swimlanes, Timeline powered by Markwhen, Task List table), full recurrence support with iCal RRULE compatibility, natural language parsing, drag-and-drop rescheduling, item hierarchy, dependencies, multiple color-coded calendars, mobile optimization, and keyboard navigation.

- **Dashboard Hub Plugin:** A free, open-source plugin that integrates Bases, Kanban boards, Calendars, Timelines, reading memos, file/HTML views, and a Secret Manager into a single responsive workspace. Features include: Timeline as a unified activity log, Calendar backed by Timeline files, Kanban boards backed by notes with frontmatter status, native Obsidian Bases, a reading workspace for Markdown/PDF/EPUB with memo highlights, password-protected encrypted secrets, and responsive drag-and-resize layouts.

- **Kanban Action Planner (see Section 2.2):** Adds multiple views (board, calendar, timeline, WBS, triage) to Obsidian Bases, enabling a single set of notes to be viewed and managed through multiple views simultaneously.

---

## 6. Performance Considerations

### 6.1 Plugin Performance with Large Datasets

- **Obsidian Bases (Core):** "Bases has a ton of optimizations for scrolling large tables and can handle vaults with tens of thousands of files without issue" – Obsidian CEO Kepano. "Bases loads everything instantly—even in vaults with thousands of notes—something that older solutions struggled with" [wanderloots.com].

- **Dataview:** "scaling up to hundreds of thousands of annotated notes without issue" [Official documentation]. However, "Dataview is definitely one to look out for, you can do some stuff with it that will bring Obsidian to its knees" [Forum discussion]. Users with 15,000+ notes reported noticeable lag.

- **Make.md:** Some users report it can be resource-intensive, though version 1.3.2 improved performance by hiding folders from indexing.

- **Notion Bases:** "The speed is incredible. It's way faster than data view or notion" [YouTube reviews]. "I did not feel any lag or delays that Notion might have with an equal number of files, especially when filtering or sorting through views" [MakeUseOf].

- **DB Folder (Archived):** "The performance really starts to get quite bad if you have a lot of files that you're going through" – Nicole van der Hoeven.

### 6.2 Obsidian vs Notion Performance

- **Obsidian:** Loads a 10,000-note vault in <2 seconds; search in 0.3 seconds
- **Notion:** Takes 5-7 seconds to load; search takes 1.8 seconds for 5,000 notes
- **Notion database limits:** 250,000 rows per database, 2.5MB per page property data, 1.5MB database property structure limit
- **Obsidian advantage:** Local data, no network latency, single-user access, efficient caching and indexing

---

## 7. Ease of Use Comparison

### 7.1 Beginner-Friendly Options

- **Obsidian Bases (Core):** "Getting started with Obsidian Bases takes only five minutes" – most accessible option for beginners. Works out of the box with no installation.

- **Make.md:** "Comes with everything you need to organize, label and personalize your notes inside Obsidian without any additional code or 3rd party dependencies." Designed for simplicity, scales up to complexity.

- **Notion Bases:** "Zero code required. Turn any folder into a Notion-style database." GUI-based, no coding needed.

### 7.2 Intermediate Options

- **Kanban Plugin:** Simple markdown-based boards. Easy to create a basic board, but advanced features require learning the plugin settings.

- **Projects Plus:** Familiar to users of the original Projects plugin. Simple setup with folder/tag/Dataview sources.

- **Full Calendar Remastered:** Requires some setup for calendar sources but straightforward for basic use.

### 7.3 Advanced/Programmer-Friendly Options

- **Dataview:** "One of the biggest barriers to using Dataview effectively is having to learn and remember how to create Dataview queries" [Forum discussion]. Requires learning DQL or JavaScript. "I sometimes wonder if learning how to use Dataview inside of Obsidian is too technical to get mass adoption, compared to WYSIWYG tools like Notion" [Hacker News].

- **Kanban Action Planner:** Integrates with Obsidian Bases but requires Obsidian 1.12+ and understanding of Bases concepts.

---

## 8. Pricing Comparison

### 8.1 Plugin Costs

All plugins discussed in this report are **free and open source**:

| Plugin | Cost | License | Notes |
|--------|------|---------|-------|
| Notion Bases | Free | GPL v3 | Open source |
| Make.md | Free | MIT | Open source |
| Obsidian Bases | Free | Proprietary | Core plugin |
| Projects Plus | Free | Apache 2.0 | Open source |
| Kanban | Free | GPL-3.0 | Open source |
| Kanban Action Planner | Free | MIT | Open source |
| Full Calendar | Free | MIT | Open source |
| Full Calendar Remastered | Free | GPL-3.0 | Open source |
| Dataview | Free | MIT | Open source |
| DB Folder | Free | MIT | Open source (archived) |
| DataLoom | Free | N/A | Discontinued |

### 8.2 Obsidian vs Notion Pricing

| | Obsidian | Notion |
|--|----------|--------|
| **Core app** | Free | Free (limited) |
| **Personal Plus** | $0 | $10/month |
| **Sync** | $4-8/month | Included |
| **Publish** | $8-10/month | Included |
| **AI features** | $0 (no AI) | $10/month/user |
| **Team (5 users)** | $250/year | $600-1,200/year |
| **Data ownership** | Full (local files) | Cloud-only |

---

## 9. Compatibility with Obsidian (August 2026)

### 9.1 Plugin Status Summary

| Plugin | Status | Last Update | Obsidian Version Required | Notes |
|--------|--------|-------------|--------------------------|-------|
| Notion Bases | ✅ Active | 2026 | 1.8.7+ | 15k downloads |
| Make.md | ✅ Active | 2026 (v1.3.5) | 0.16.0+ | 812k downloads |
| Obsidian Bases | ✅ Core | Ships with Obsidian | N/A | Included |
| Projects Plus | ⚠️ Beta | 2026 (v3.5.1-alpha) | 1.0.0+ | BRAT installation |
| Kanban | ⚠️ Unmaintained | 2024 (v2.0.51) | 1.0.0+ | 2.4M downloads |
| Kanban Action Planner | ✅ Active | 2026 (v1.12.0) | 1.12+ | Desktop only |
| Full Calendar | ❌ Archived | 2023 (v0.10.7) | 0.16.3+ | 449k downloads |
| Full Calendar Remastered | ✅ Active | 2026 (v0.13.5) | 1.12.7+ | 33k downloads |
| Dataview | ⚠️ Stalled | 2025 (v0.5.70) | 0.13.11+ | 3.2M downloads |
| DB Folder | ❌ Archived | 2024 (v3.5.1) | 0.13.11+ | 1.4k stars |
| DataLoom | ❌ Discontinued | 2025 | N/A | Removed from store |

### 9.2 Obsidian's New Plugin Policy (May 12, 2026)

The Obsidian team launched a new automated review system that scans every version for security and code quality. As of August 2026, there are **6,342 plugins** and **662 themes** available. Projects that are no longer maintained or no longer function with newer versions of Obsidian may be removed from the Community directory per the Developer Policies.

**Implication:** Unmaintained plugins (Kanban, Full Calendar, Dataview, DB Folder) face eventual removal from the community directory if they fail to meet new standards. Users building systems around these plugins should plan for migration.

---

## 10. Recommendations and Final Verdict

### 10.1 For New Users (Starting in August 2026)

**Primary Recommendation: Notion Bases Plugin** (for full Notion replacement) **+ Obsidian Native Bases** (for core functionality)

- **If you want the closest Notion experience:** Use **Notion Bases** – it offers 7 views, 18 column types, formulas, relations, lookups, rollups, and subtasks. It is the most comprehensive single-plugin solution.
- **If you prefer a built-in solution:** Use **Obsidian Native Bases** – it is included with Obsidian, fast, stable, and actively developed by the Obsidian team. Supplement with community plugins for additional views.
- **For a balanced approach:** Use **Make.md** – it offers 11 view types, Spaces navigation, formulas, relations, and rollups, with a large user base and active development.

### 10.2 For Users Migrating from Notion

1. **Export your Notion data** to Markdown (using Notion's export feature or the Notional plugin for two-way sync)
2. **Choose a primary database plugin:** Notion Bases or Make.md for the most feature parity
3. **Set up your data structure:** Use folders and YAML frontmatter properties to replicate Notion's database schema
4. **Create views:** Build Table, Kanban, Calendar, and List views for each database
5. **Add automation:** Use Templater for templates, QuickAdd for quick capture

### 10.3 For Users of Discontinued Plugins

- **If you use Projects plugin:** Migrate to **Projects Plus** (for similar experience) or **Obsidian Bases** (for native support)
- **If you use DB Folder:** Migrate to **Notion Bases** or **Make.md** – both offer similar features with active maintenance
- **If you use DataLoom:** Export your .loom files to raw markdown and use **Obsidian's native table editor** or **Notion Bases**

### 10.4 For Specific View Needs

- **Kanban only:** Use **Kanban Action Planner** (active, integrates with Bases) or **Kanban** (unmaintained but polished)
- **Calendar only:** Use **Full Calendar Remastered** (active fork with two-way CalDAV/Google Calendar sync)
- **Custom queries:** Use **Dataview** (powerful but requires learning DQL or JavaScript)
- **All views in one:** Use **Notion Bases** (7 views) or **Make.md** (11 views)

### 10.5 Final Verdict

As of August 2026, Obsidian has matured significantly in its ability to replicate Notion's multi-view database functionality. The ecosystem now offers multiple viable solutions, each with different trade-offs:

| Use Case | Best Plugin | Why |
|----------|-------------|-----|
| Closest Notion replication | Notion Bases | 7 views, 18 column types, formulas, relations, rollups |
| Active development + large community | Make.md | 11 view types, 812k downloads, active maintenance |
| Native, fast, stable | Obsidian Bases | Core plugin, instant performance, no installation |
| Familiar Projects experience | Projects Plus | Revival of popular plugin with new features |
| Kanban + Bases integration | Kanban Action Planner | Multiple views, automation rules, GTD contexts |
| Best calendar | Full Calendar Remastered | Two-way CalDAV/Google Calendar sync |
| Advanced querying | Dataview | Most powerful query engine, but requires coding |

**The strongest overall recommendation** for users seeking to replicate Notion's full database experience is **Notion Bases** – it offers the most complete feature set (7 views, 18 column types, formulas, relations, rollups, subtasks) while maintaining 100% local Markdown storage and active development. For users who prefer a native solution, **Obsidian Bases** combined with **Kanban Action Planner** and **Full Calendar Remastered** provides a powerful, integrated multi-view system that is built into the app.

---

## Sources

[1] Obsidian Community - Kanban Plugin: https://community.obsidian.md/plugins/obsidian-kanban

[2] GitHub - mgmeyers/obsidian-kanban: https://github.com/mgmeyers/obsidian-kanban

[3] GitHub - obsidian-kanban Releases: https://github.com/community-archive/obsidian-kanban/releases

[4] GitHub - MAINTAINERS.md: https://github.com/mgmeyers/obsidian-kanban/blob/master/MAINTAINERS.md

[5] Kanban Plugin Documentation: https://publish.obsidian.md/kanban/

[6] GitHub Discussions - community-archive/obsidian-kanban: https://github.com/community-archive/obsidian-kanban/discussions

[7] GitHub - Kanban Plugin Discussion: https://github.com/mgmeyers/obsidian-kanban/discussions/2

[8] Obsidian Plugin Stats - Kanban: https://www.obsidianstats.com/plugins/obsidian-kanban

[9] Obsidian Forum - Kanban Plugin: https://forum.obsidian.md/t/kanban-plugin/17082

[10] XDA Developers - Best Obsidian Plugins: https://www.xda-developers.com/best-obsidian-plugins/

[11] Reddit - Best Kanban Plugin for Obsidian: https://www.reddit.com/r/ObsidianMD/comments/1b8sdnh/best_kanban_plugin_for_obsidian

[12] Mind Mapping Software Blog - Kanban Plugin: https://mindmappingsoftwareblog.com/obsidian-kanban-plugin/

[13] GitHub - Notion-like capabilities discussion: https://github.com/blacksmithgu/obsidian-dataview/discussions/710

[14] Obsidian Community - Notion Bases: https://community.obsidian.md/plugins/notion-bases

[15] GitHub - bgarciamoura/obsidian-notion-bases-plugin: https://github.com/bgarciamoura/obsidian-notion-bases-plugin

[16] Obsidian Stats - Notion Bases: https://www.obsidianstats.com/plugins/notion-bases

[17] Reddit - I built a Notion-like database plugin: https://www.reddit.com/r/ObsidianMD/comments/1rtwcja/i_built_a_notionlike_database_plugin_for_obsidian

[18] Reddit - With the bases plugin, I finally removed notion: https://www.reddit.com/r/ObsidianMD/comments/1mw8yq2/with_the_bases_plugin_i_finally_removed_notion

[19] Obsidian Forum - Are Obsidian Bases the Same as Notion Database?: https://forum.obsidian.md/t/q-a-are-obsidian-bases-the-same-as-notion-database/112363

[20] Medium - I Stopped Envying Notion the Day Obsidian Shipped Bases: https://medium.com/@lennart.dde/i-stopped-envying-notion-the-day-obsidian-shipped-bases-02ac7bfffe46

[21] MakeUseOf - After using Obsidian Bases, I can't see myself going back to Notion: https://www.makeuseof.com/obsidian-bases-ditch-notion

[22] XDA Developers - Notion databases are great, but this Obsidian plugin is so much better: https://www.xda-developers.com/notion-databases-great-but-obsidian-bases-better

[23] YouTube - NEW Obsidian Bases Core Plugin Full Overview: https://www.youtube.com/watch?v=nWUQbK8KlOo

[24] YouTube - Why I'm Ditching Notion for Obsidian Bases: https://www.youtube.com/watch?v=YMCVtseYqpI

[25] YouTube - Game changing Obsidian Bases Update: https://www.youtube.com/watch?v=Pus5BcmQVoc

[26] Obsidian Help - Bases Documentation: https://obsidian.md/help/bases

[27] Obsidian Roadmap: https://obsidian.md/roadmap

[28] Reddit - Honest question, can bases actually replace notion database?: https://www.reddit.com/r/ObsidianMD/comments/1kxg9wz/honest_question_can_bases_actually_replace_notion

[29] Obsidian Community - Dataview Plugin: https://community.obsidian.md/plugins/dataview

[30] GitHub - blacksmithgu/obsidian-dataview: https://github.com/blacksmithgu/obsidian-dataview

[31] Dataview Documentation: https://blacksmithgu.github.io/obsidian-dataview

[32] Obsidian Stats - Dataview: https://www.obsidianstats.com/plugins/dataview

[33] Obsidian.rocks - Dataview Beginner's Guide: https://obsidian.rocks/dataview-plugin-guide-for-beginners/

[34] Medium - Dataview for Beginners Guide: https://medium.com/@denisetodd/the-beginners-guide-for-dataview-obsidian-plugin-10-areas-where-things-can-go-wrong-5e5b5c4c8b8b

[35] Dataview API Code Reference: https://github.com/blacksmithgu/obsidian-dataview/blob/master/docs/docs/api/code-reference.md

[36] Dataview Resources and Support: https://blacksmithgu.github.io/obsidian-dataview/resources/resources-and-support

[37] Hacker News - Dataview Discussion: https://news.ycombinator.com/item?id=31623456

[38] Obsidian Stats - MAKE.md: https://www.obsidianstats.com/plugins/make-md

[39] Obsidian Community - Make.md: https://community.obsidian.md/plugins/make-md

[40] GitHub - Make-md/makemd: https://github.com/Make-md/makemd

[41] Make.md Official Website: https://www.make.md

[42] XDA Developers - Make.md Article: https://www.xda-developers.com/make-md-obsidian-plugin/

[43] YouTube - The Best Beginner Friendly Obsidian Plugin - Make.md Tutorial: https://www.youtube.com/watch?v=ISpII6nsego

[44] YouTube - Best Offline Notion Alternative with Obsidian - Make.md Plugin: https://www.youtube.com/watch?v=Ad03iBrgs6Q

[45] YouTube - Obsidian Make.md Plugin - Database Relation: https://www.youtube.com/watch?v=kuC3Xd7k6lU

[46] GitHub - Make.md Issues: https://github.com/Make-md/makemd/issues

[47] Obsidian Forum - MAKE.md help: https://forum.obsidian.md/t/make-md-help/104579

[48] Reddit - Does MAKE.md work?: https://www.reddit.com/r/ObsidianMD/comments/1k9arl1/db_folder

[49] Reddit - Make.md or not?: https://www.reddit.com/r/ObsidianMD/comments/1hmdsf6/makemd_10_is_now_available_organization_and

[50] Reddit - Is the make.md plugin safe?: https://www.reddit.com/r/ObsidianMD/comments/1kwjbz9/why_people_are_making_obsidian_more_and_more_like

[51] Obsidian Forum - Full Calendar Plugin: https://forum.obsidian.md/t/full-calendar-plugin-replicate-google-calendar-in-your-vault/32584

[52] Obsidian Community - Full Calendar: https://community.obsidian.md/plugins/obsidian-full-calendar

[53] GitHub - obsidian-full-calendar (Archived): https://github.com/obsidian-community/obsidian-full-calendar

[54] Full Calendar Documentation: https://obsidian-community.github.io/obsidian-full-calendar

[55] Obsidian Stats - Full Calendar: https://www.obsidianstats.com/plugins/obsidian-full-calendar

[56] Obsidian Community - Full Calendar Remastered: https://community.obsidian.md/plugins/full-calendar-remastered

[57] GitHub - Full Calendar Remastered: https://github.com/obsidian-full-calendar-remastered/plugin-full-calendar

[58] Full Calendar Remastered Documentation: https://obsidian-full-calendar-remastered.github.io/plugin-full-calendar

[59] GitHub - Projects Plus Plugin: https://github.com/ParkPavel/obs-projects-plus

[60] Obsidian Forum - Projects Plus Plugin: https://forum.obsidian.md/t/projects-plus-plugin/106826

[61] Reddit - Projects is Back: https://www.reddit.com/r/ObsidianMD/comments/1qpg6as/projects_is_back

[62] GitHub - obsidian-projects (Archived): https://github.com/obsmd-projects/obsidian-projects

[63] Marcus Olsson - Announcing Obsidian Projects: https://marcusolsson.dev/announcing-obsidian-projects

[64] Obsidian Forum - Development for Projects plugin needed: https://forum.obsidian.md/t/development-for-projects-plugin-needed/101089

[65] Obsidian Hub - obsidian-projects: https://publish.obsidian.md/hub/02+-+Community+Expansions/02.05+All+Community+Expansions/Plugins/obsidian-projects

[66] GitHub - obsidian-db-folder (Archived): https://github.com/RafaelGB/obsidian-db-folder

[67] DB Folder Documentation: https://rafaelgb.github.io/obsidian-db-folder

[68] DB Folder Changelog: https://rafaelgb.github.io/obsidian-db-folder/changelog

[69] GitHub - obsidian-dataloom (Archived): https://github.com/decaf-dev/obsidian-dataloom

[70] Reddit - DB Folder vs Make.md vs Projects: https://www.reddit.com/r/ObsidianMD/comments/11ejpcf/db_folder_vs_makemd_vs_projects

[71] YouTube - Real use case for Obsidian: Dataview and Database Folder: https://www.youtube.com/watch?v=Ak7cuIyQeYw

[72] Obsidian Community - Kanban Action Planner: https://community.obsidian.md/plugins/kanban-action-planner

[73] GitHub - Kanban Action Planner: https://github.com/dsebastien/obsidian-kanban-action-planner

[74] Kanban Action Planner Documentation: https://dsebastien.github.io/obsidian-kanban-action-planner

[75] Obsidian Stats - Kanban Action Planner: https://www.obsidianstats.com/plugins/kanban-action-planner

[76] Sébastien Dubois - How I Turned My Obsidian Notes Into Kanban Boards: https://www.dsebastien.net/how-i-turned-my-obsidian-notes-into-kanban-boards

[77] Sébastien Dubois - Kanban Action Planner 1.8.0 - GTD Contexts: https://www.dsebastien.net/kanban-action-planner-1-8-0-gtd-contexts

[78] GitHub - Kanban Action Planner Issues: https://github.com/dsebastien/obsidian-kanban-action-planner/issues

[79] Obsidian Blog - The future of Obsidian plugins: https://obsidian.md/blog/future-of-plugins

[80] Obsidian Community - New Plugin Directory: https://community.obsidian.md

[81] Obsidian Stats - Plugins Supporting Bases: https://www.obsidianstats.com/bases-support

[82] Obsidian Stats - Project Management Plugins: https://www.obsidianstats.com/tags/project-management

[83] Practical PKM - Bases Plugin Overview: https://practicalpkm.com/bases-plugin-overview

[84] wanderloots - Obsidian Bases Introduction: https://wanderloots.com/obsidian-bases-introduction

[85] Obsidian Rocks - Getting Started with Obsidian Bases: https://obsidian.rocks/getting-started-with-obsidian-bases/

[86] YouTube - Obsidian 1.9 preview - What the new Bases plugin can (not) do: https://www.youtube.com/watch?v=lpyIuLmEidQ

[87] Medium - Obsidian Bases: What Are They Good For?: https://fleker.medium.com/obsidian-bases-what-are-they-good-for-and-what-are-they-not-da620006cb34

[88] Obsidian Forum - Provide API access to the results of Bases view: https://forum.obsidian.md/t/provide-api-access-to-the-results-of-bases-view/112363

[89] Obsidian Forum - Allow bases to see properties generated by plugins: https://forum.obsidian.md/t/allow-bases-to-see-properties-generated-by-plugins/112364

[90] Reddit - What exactly is the Bases plugin?: https://www.reddit.com/r/ObsidianMD/comments/1ma5gar/a_bit_of_praise_for_bases_as_an_alternative_and_a

[91] GitHub - GoodBases Plugin: https://github.com/francescoumberto/GoodBases

[92] Obsidian Community - GoodBases: https://community.obsidian.md/plugins/good-bases

[93] GitHub - Planner Plugin: https://github.com/SawyerRensel/Planner

[94] GitHub - Dashboard Hub Plugin: https://github.com/developer/dashboard-hub

[95] Obsidian Community - Kanban Board (komailo): https://community.obsidian.md/plugins/kanban-board

[96] Obsidian Community - Kanban for Professionals: https://community.obsidian.md/plugins/kanban-pro-boards

[97] GitHub - Kanban Plus (fork): https://github.com/geetduggal/obsidian-kanban-plus

[98] Obsidian Community - Notional (Notion sync): https://community.obsidian.md/plugins/notional

[99] Obsidian Community - Base Board: https://community.obsidian.md/plugins/base-board

[100] Obsidian Community - Bases CMS: https://community.obsidian.md/plugins/bases-cms
