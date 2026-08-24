# Comprehensive Analysis: Obsidian Plugins for Notion-Like Multi-View Database Functionality

## Executive Summary

No single plugin perfectly replicates all four Notion database views (Table, Kanban, Calendar, and List) on the same dataset with a polished, unified experience. However, several approaches come close, each with distinct trade-offs in stability, feature completeness, and long-term maintainability. The closest single-plugin solutions are the **Obsidian Database Plugin** (by ekmungi) and **Make.md**, while a combination approach using **Dataview** with specialized plugins can work but suffers from a critical data silo problem with Kanban boards. The new **Obsidian Bases** core plugin (beta, Catalyst-only) offers promising native functionality but currently only supports table and card views. This report provides a detailed comparison of all viable options, including considerations for data synchronization, customizability, performance, and future-proofing.

---

## Single-Plugin Approaches

### Obsidian Database Plugin (ekmungi)

**Views:** Table, Kanban, Calendar, Timeline/Gantt (4 views)  
**Status:** Pre-1.0.0, not yet in community plugin registry, installable via BRAT  
**GitHub:** https://github.com/ekmungi/obsidian-database-plugin [15]

This plugin is the closest single-plugin approximation of Notion's database functionality currently available. It allows users to "turn any folder of markdown files into a database," with YAML frontmatter serving as the data layer and the plugin providing four view types [15].

**Key Features:**
- **Table view**: Spreadsheet-like grid with inline editing, sorting, filtering, and search
- **Kanban view**: Drag-and-drop cards grouped by select/multi-select properties
- **Calendar view**: Monthly calendar with events placed by date, drag to reschedule
- **Timeline view**: Horizontal Gantt-style chart with zoom levels, today marker, and color-coded bars
- **Inline editing** for all cell types (text, number, date, select, multi-select, checkbox, relation)
- **Bidirectional relations** with auto-syncing backlinks between databases
- **Recursive subfolder scanning** (opt-in)
- **View management** with Notion-style tabs, persistence across restarts
- **Codeblock embedding** (`database` codeblock) inside any markdown note
- **Template picker** for creating records from templates

**Column types supported:** file, text, number, date, select, multi-select, checkbox, relation, and rollup (read-only computed from relations) [15].

**Strengths:**
- All views draw from the same YAML frontmatter data—changes in any view are reflected everywhere
- Inline editing is available in all views, not just the table
- Bidirectional relations with auto-syncing backlinks mimics Notion's relational database feature
- Three-layer architecture (Data Layer, Database Engine, View Layer) ensures clean separation of concerns
- Preact-based UI is lightweight (~3KB React-compatible framework)

**Weaknesses:**
- **No List view**—only Table, Kanban, Calendar, and Timeline. The Table view can be configured to approximate a list, but not identically
- Pre-1.0.0 software with potential bugs and breaking changes
- Not yet in the Obsidian community plugin registry (requires BRAT for installation)
- External file renames outside Obsidian can break relation backlinks
- Roadmap items (gallery view, CSV import/export, formula columns) are not yet implemented

**Data synchronization:** "All edits write directly to your markdown files' frontmatter. No proprietary database—your notes stay portable" [15]. The DatabaseController acts as a shared data layer used by both tab-based views and codeblock renderers, ensuring consistency across all views.

---

### Make.md

**Views:** Table, List, Board, Cards, Catalog, Gallery, Flow, Calendar (day/week/month)—8+ views  
**Status:** Actively developed, version 1.3.5, scored 70/100 on Obsidian Stats  
**Plugin page:** https://community.obsidian.md/plugins/make-md  
**GitHub:** https://github.com/Make-md/makemd [6]

Make.md is described as an "Organization and Personalization Engine for your notes" that "comes with everything you need to organize, label and personalize your notes inside Obsidian without any additional code or 3rd party dependencies" [6]. It has the most extensive view library of any Obsidian plugin, closely mirroring Notion's feature set.

**Key Features:**
- **Spaces Navigation**: Flexible navigation pane for pinning folders and tags as "spaces" without affecting vault structure
- **Data Views**: Table, list, board, cards, catalog, gallery, flow, and calendar (day, week, month)
- **Properties (Notion-like Databases)**: Supports text, number, boolean, date, option menus, tags, formulas, links, relations, flex, aggregate, object, images, and repeat property types
- **Grouping, Sorting & Filtering**: Includes a "group by" option not commonly found in other apps
- **Formulas**: Formula property with comprehensive function list, formatted similarly to Notion, including column calculations (sum feature)
- **Workspace Customization**: Spaces can be turned into dashboards with customizable covers, stickers, labels, and repositionable elements

**Strengths:**
- Most view types of any plugin (including a native List view, which Projects and the Database Plugin lack)
- Closest feature parity to Notion in terms of property types and formulas
- "I really challenge anyone that is coming from notion but they really want to have an offline solution where they're privacy first... if you use this make.md plugin I think you could pretty much get the same type of stuff that you would use in notion over in Obsidian" [7]
- No additional code or third-party dependencies required

**Weaknesses:**
- **Significant stability issues**: Multiple users report bugs and unresponsiveness. One user stated: "I have been using it this past week and regularly find it buggy and/or unresponsive" [9]. Another noted: "I've sort of stopped using MAKE.md because, like you said, it seems to be more of an inconvenience than a plus" [9]
- "I don't think the plug-in is quite ready yet for heavy use" [9]
- Spaces feature can cause confusion: "Since my first post I've had a case where spaces got confused. The reload spaces feature cured the confusion at the cost of losing all spaces" [9]
- No built-in automation, collaboration, or sharing features (expected for local-first)
- 184 open issues on GitHub (65 closed) indicates ongoing development challenges [6]

**Data synchronization:** All views draw from the same YAML frontmatter and properties system. However, the Spaces feature introduces complexity that can lead to data visibility issues if not carefully managed.

---

### Obsidian Projects (Marcus Olsson) — ARCHIVED

**Views:** Table, Board (Kanban), Calendar, Gallery (4 views)  
**Status:** **Discontinued and archived.** GitHub repository archived by owner on July 18, 2025, now read-only. Plugin removed from community plugin list.  
**GitHub (archived):** https://github.com/obsmd-projects/obsidian-projects [1]

**CRITICAL STATUS:** This plugin is no longer maintained. The developer stated: "I created Obsidian Projects because I wanted to scratch my own itch. Unfortunately, I'm no longer using Obsidian, nor following the development of the plugin eco-system" [1]. The repository has 1.9k stars and 150 forks but is now read-only. It can still be installed via the BRAT plugin but is not recommended for new setups.

**Key Features (when active):**
- **Table view**: Default view with sortable columns
- **Board view**: Kanban-style workflow with status columns
- **Calendar view**: Monthly schedule with checkboxes for published status
- **Gallery view**: Card thumbnails with cover images
- **Framework architecture**: "The real benefit of Projects is that it provides the framework for basically any plugin to be added to it as a view" [2]
- **Separation of concerns**: Separates data input (YAML frontmatter) from output (view)

**Strengths (historical):**
- Clean architectural design that allowed other plugins to add custom views
- Used standard Dataview-format YAML metadata
- Local-first, file-based, no proprietary database
- "The real appeal is the separation, because once they're separated, it adds this modularization to it so that each view becomes like an atomic component" [2]

**Weaknesses:**
- **No List view**—only Table, Board, Calendar, Gallery
- Known bugs: "always opening to the default project, not saving column width changes, and issues with boolean/checkbox recognition if cells are incorrectly edited" [1]
- **Plugin is discontinued**—no further updates, bug fixes, or security patches
- Community response was significant: "Obsidian's plugin architecture is one of its liabilities—when a plugin like Projects is no longer developed after users have built systems around it, trust in the app's reliability is degraded" [1]

**Successor: Projects Plus** (by ParkPavel) is available on GitHub at ParkPavel/obs-projects-plus but is undergoing community testing and has not yet been released to the community plugin registry [1].

---

### Kanban for Professionals

**Views:** Board, Table, **List** (3 views, switchable with one click)  
**Price:** Free core, $5.99 lifetime for Pro  
**Status:** Active, version 1.0.9, 458 downloads, MIT License  
**Plugin page:** https://community.obsidian.md/plugins/kanban-pro-boards [4]

This plugin is a newer alternative that provides Board, Table, and List views of the same cards, switchable with one click. It uses the same `kanban-plugin` board markdown format as the community Kanban plugin, ensuring compatibility with existing boards [4].

**Key Features:**
- **Free features**: Board, Table, and List views, drag-and-drop with undo/redo, inline editing, embed boards in notes via `kanban-plugin` code block, inline metadata parsing (due dates, tags, priorities, Dataview fields)
- **Pro features ($5.99 lifetime)**: Saved Views (named, reusable filters), Dashboard with overdue/due-soon counters and rollups, Recurrence (repeating cards via rrule), Time tracking per card, Calendar (.ics) export, GitHub Issues sync

**Strengths:**
- Three views (Board, Table, List) on the same cards, switchable with one click
- Compatible with existing community Kanban boards—no conversion needed
- "Your boards are stored entirely as local markdown in your vault. Nothing is uploaded, and the plugin works fully offline" [4]
- Affordable one-time Pro price ($5.99 lifetime)

**Weaknesses:**
- **Kanban-centered**—the data model is the Kanban code block format, not general YAML frontmatter. This means data is not easily shared with other plugins that read YAML
- **No Calendar view**—calendar export is available only in Pro, and it exports to .ics (external calendar), not an in-app calendar view
- Limited to cards/boards—not a general-purpose database solution
- Pro features require payment (though core is free)

**Data synchronization:** Reads and writes the same `kanban-plugin` board markdown format. Changes made in any view sync back to the code block. However, data is not stored in YAML frontmatter, limiting integration with other plugins.

---

### Obsidian Planner (SawyerRensel)

**Views:** Calendar, Kanban, Timeline, **Task List** (4 views, integrated)  
**Status:** Not yet in community plugins, 30 stars on GitHub, GPL v3.0  
**GitHub:** https://github.com/SawyerRensel/Planner [25]

"Unified calendar, kanban, timeline, and task list for project and time management in Obsidian" with "Your data stays in plain Markdown files with YAML frontmatter, giving you complete ownership and flexibility" [25].

**Key Features:**
- Four integrated views: Calendar (with six layouts via FullCalendar), Kanban (drag-and-drop with columns, swimlanes, WIP limits), Timeline (powered by Markwhen), and Task List (table view with virtual scrolling)
- Full recurrence support with iCal RRULE compatibility
- Natural language input for creating items
- Drag & drop rescheduling and task movement
- Item hierarchy (parent/child relationships) and dependencies (blocked_by)
- Multiple color-coded calendars, mobile optimization, keyboard navigation

**Strengths:**
- Four integrated views including a Task List (table-style)
- Uses YAML frontmatter as data source
- Full recurrence support and natural language input

**Weaknesses:**
- **Not in community plugin registry**—requires manual installation
- Low adoption (30 stars, 4 forks)
- Early-stage development with limited community testing
- No Table view in the traditional sense—Task List is table-style but task-focused

**Data synchronization:** All views draw from YAML frontmatter in plain Markdown files. Changes in any view update the underlying notes.

---

### DB Folder (RafaelGB) — ARCHIVED

**Views:** Table (only)  
**Status:** **Archived.** Repository archived by owner on July 28, 2025, now read-only.  
**GitHub:** https://github.com/RafaelGB/obsidian-db-folder [11]

**CRITICAL STATUS:** This plugin is no longer maintained. It is included here for completeness but is not recommended for new setups.

When active, DB Folder "allows you to create Notion's like databases in your Obsidian Vault" using "the search engine of the popular Dataview plugin, you can view the content of your notes and edit the fields directly from the table without the need to open the note" [11].

**Key Features (when active):**
- Notion-like database based on folders, links, tags, or Dataview queries
- Seven property types: Text, Number, Select, Tag, Checkbox, Date, Date & Time, Formula
- Filtering and sorting (single or multi-column)
- Group filters with AND/OR relationships
- Grouping into subfolders
- CSV export, embedding in other notes

**Strengths (historical):**
- Strong integration with Dataview's query engine
- Editable table cells with inline editing
- Supported relation and rollup column types

**Weaknesses:**
- **Table only**—no Kanban, Calendar, or List views
- **Archived and unmaintained**—no future updates
- Performance issues: "The performance really starts to get quite bad if you have a lot of files" [13]
- Requires manual refresh to update the database view
- No mobile support
- Known bugs: auto-update problems, CSV import failing silently

**Data synchronization:** Changes made in the database update the notes and vice versa, though the database may need manual refreshing.

---

## Combination Approach: Dataview + Kanban + Calendar Plugins

### How It Works

This approach uses **Dataview** as the query engine and combines it with separate plugins for each view type:

1. **Table view:** ````dataview TABLE ... FROM "folder" WHERE ... ````
2. **List view:** ````dataview LIST ... FROM "folder" WHERE ... ````
3. **Calendar view:** ````dataview CALENDAR ... FROM "folder" ```` (or Full Calendar Remastered for a graphical calendar)
4. **Kanban view:** Either the official Kanban plugin or a Dataview-generated Kanban using `TABLE ... GROUP BY status`

All plugins read from the **same YAML frontmatter** in the same markdown files, making YAML the single source of truth [22].

### Dataview Plugin Details

**Plugin page:** https://community.obsidian.md/plugins/dataview [22]  
**GitHub:** https://github.com/blacksmithgu/obsidian-dataview  
**Status:** Actively maintained (version 0.5.70, Beta, April 2026), 4.8M+ downloads, 9.3k stars [22]

Dataview "treats your Obsidian Vault as a database which you can query from. Provides a JavaScript API and pipeline-based query language for filtering, sorting, and extracting data from Markdown pages" [22]. It offers four query types: LIST, TABLE, TASK, CALENDAR [22].

**Key Features:**
- **DQL (Dataview Query Language)**: Pipeline-based, vaguely SQL-looking expression language
- **DataviewJS**: Full JavaScript API with rendering utilities
- **Inline expressions**: Embed DQL directly in markdown
- **Automatic indexing**: Built-in metadata fields (file.name, file.folder, file.ctime, file.mtime, file.tags, file.inlinks, file.outlinks, etc.)

**Strengths:**
- Most powerful querying capabilities of any Obsidian plugin
- Extensive documentation and community support
- Active maintenance with 138 releases (now maintained by @holroy)
- Works with YAML frontmatter, inline fields, and built-in metadata
- Regular Dataview queries are sandboxed and cannot make negative changes to your vault

**Weaknesses:**
- **Read-only output**—Dataview results are not editable inline. "One thing you cannot query in Dataview: the contents of your notes" [23]
- **Invisible output**—Dataview results are invisible outside Obsidian's renderer. They do not appear in the Graph view, backlinks pane, Obsidian Publish, plain-text search/grep, Git diffs, or AI agents reading raw files [23]
- **Steep learning curve**: "Users with SQL experience may find DQL counterproductive because keywords like WHERE, TASKS, GROUP BY, FROM, and SORT have different meanings than in SQL" [22]
- Requires creating separate code blocks for each view—no unified view management

### The Critical Kanban Data Silos Problem

This is the **fundamental incompatibility** in the combination approach:

- **Dataview** reads from YAML frontmatter and inline fields (`Key:: Value`)
- **Kanban plugin** stores boards in a special `kanban-plugin` code block format within a markdown file
- These are **different data formats**—they cannot query each other's data

As one user noted: "the two plugins didn't share data seamlessly—Fantasy Calendar used YAML front matter, while Kanban stored data as markdown task lists, requiring duplicate data entry" [2]. A tutorial by Justin from Effective Remote Work shows how to build a plain-text Kanban board in Obsidian using the Dataview plugin alone, but the tutorial notes: "You're not going to be able to just drag and drop cards... you have to go into each note and actually change this status item" [17].

**Workarounds for the Kanban data silo:**

1. **Use Dataview GROUP BY** instead of the Kanban plugin—read-only, no drag-and-drop
2. **Use Task List Kanban** (Chris Kerr)—collects tasks from markdown files and syncs changes back to the source files [18]
3. **Use Kanban for Professionals**—has Board, Table, and List views built-in, reads/writes standard Kanban format [4]
4. **Use only YAML-based plugins** (Projects, Database Plugin, Make.md) that all draw from the same frontmatter

### Dataview Serializer Plugin

A notable companion to Dataview is the **Dataview Serializer** (by Sébastien Dubois), which writes query results as real Markdown into notes, making outputs visible to the graph, Publish, grep, git, and AI agents [20]. The author explains: "The idea behind the Dataview Serializer is that when a query is detected by the plugin, it will actually generate a list of results. But if I look at this file on my filesystem, I will find those links. And this is a big difference with normal Dataview queries" [20].

**GitHub:** https://github.com/dsebastien/dataview-serializer

Directives control refresh behavior: `QueryToSerialize` (on save), `QueryToSerializeManual`, `QueryToSerializeOnce`, and `QueryToSerializeOnceAndEject` (runs once, then deletes itself) [20].

---

## Obsidian Bases (Core Plugin) — The Emerging Native Solution

**Status:** Beta for Catalyst members (requires Obsidian 1.9.0 and Catalyst license, $25 one-time fee)  
**Documentation:** https://obsidian.md/help/bases [3]

Obsidian Bases is a new core plugin that "lets you turn any set of notes into a powerful database" [3]. It is built by the Obsidian team and represents the most significant native step toward Notion-like functionality.

**Key Features:**
- **Instant table creation** from entire vault contents (tested with 5,000 notes, loading instantly)
- **Property-based filtering** with clickable UI (no need to write queries)
- **Multiple views** within a single table (e.g., fiction/non-fiction)
- **Embedding bases** into other notes using `![[embed]]` syntax or base code blocks
- **Functions/formulas** for complex queries (Overdue flag, due in days, relative dates, etc.)
- **Column reordering** via drag-and-drop
- **Batch editing** of properties directly within the table view
- **Template Generator**—Generate new notes from a template tied to the current view
- **Card view** with cover images
- **Export to CSV** via view UI

**Current View Types:** Table (editing + summaries), Cards (covers/galleries), List (dashboards/MoCs), Map (requires Maps plugin) [3]

**Performance:** "Bases loads everything instantly—even in vaults with thousands of notes—something that older solutions struggled with" [3]. In direct comparison with DB Folder: "Even without measuring it, we can see that the DB folder file opens much slower and only shows the first 10 entries while the Base file shows the full table" [3].

**Strengths:**
- Built by the Obsidian team—guaranteed long-term support and integration
- "The speed is incredible. It's way faster than dataview or notion... There's 5,000 notes here and it just popped up" [3]
- No coding required—visual editor for creating and editing bases
- "Almost anything you would have previously used a Dataview query for can be converted to a Base view" [3]

**Weaknesses:**
- **Currently only table and card views**—Kanban, Calendar, and List views are on the roadmap but not yet available
- Requires Catalyst license ($25 one-time fee) for early access
- Inline fields are not supported for columns—only properties defined in the frontmatter work
- Embedded images do not get displayed as thumbnails
- Legacy properties "tag", "alias", and "cssclass" are no longer supported (must use "tags", "aliases", "cssclasses")
- This is still a beta version

**Roadmap:** List/card views, grouping, API support for plugins, and Obsidian Publish support [3]. "Adding more view types such as lists and cards is already on the roadmap and knowing the Obsidian team, these will come really soon" [3].

**Data synchronization:** "Notes are the source of truth; Bases is a view layer only" [3]. Each Base starts with EVERY note in the vault, allowing users to whittle it down to the views they want for that specific Base.

---

## Side-by-Side Comparison

### Table: View Coverage by Plugin

| Plugin | Table | Kanban | Calendar | List | Other Views | Status |
|--------|-------|--------|----------|------|-------------|--------|
| Obsidian Database Plugin (ekmungi) | ✅ | ✅ | ✅ | ❌ | Timeline, Gantt | Pre-1.0.0, active |
| Make.md | ✅ | ✅ | ✅ | ✅ | Gallery, Cards, Catalog, Flow | Active, buggy |
| Obsidian Projects (Marcus Olsson) | ✅ | ✅ | ✅ | ❌ | Gallery | **Archived** |
| Kanban for Professionals | ✅ | ✅ | ❌ | ✅ | None | Active, paid Pro |
| Obsidian Planner (SawyerRensel) | ❌ (Task List) | ✅ | ✅ | ✅ | Timeline | Early, pre-release |
| DB Folder (RafaelGB) | ✅ | ❌ | ❌ | ❌ | None | **Archived** |
| Dataview (combination) | ✅ | ✅ (GROUP BY) | ✅ (CALENDAR) | ✅ | TASK | Active, read-only |
| Obsidian Bases (core) | ✅ | ❌ (roadmap) | ❌ (roadmap) | ✅ | Cards, Map | Beta, Catalyst |

### Table: Data Synchronization & Storage

| Plugin | Data Source | Editing | Cross-View Sync | Notes |
|--------|-------------|---------|-----------------|-------|
| Obsidian Database Plugin | YAML frontmatter | Inline in all views | ✅ Bidirectional | "All edits write directly to your markdown files' frontmatter" [15] |
| Make.md | YAML frontmatter + proprietary | Inline editing | ✅ (but buggy) | Spaces feature can cause confusion |
| Obsidian Projects | YAML frontmatter | Inline in all views | ✅ Bidirectional | Architecture allowed view plugins |
| Kanban for Professionals | Kanban code block | Inline in all views | ✅ Within its format | Not YAML-based; limited cross-plugin integration |
| Obsidian Planner | YAML frontmatter | Inline | ✅ Bidirectional | "Your data stays in plain Markdown files" [25] |
| DB Folder | YAML frontmatter | Inline in table | ✅ (manual refresh) | Archived |
| Dataview combination | YAML frontmatter | Read-only in Dataview | ❌ Kanban data silo | Kanban stores data in code blocks, not YAML |
| Obsidian Bases | YAML frontmatter (Properties) | Inline in table | ✅ | "Notes are the source of truth; Bases is a view layer only" [3] |

### Table: Customizability

| Plugin | Property Types | Filters | Sorting | Grouping | Formulas |
|--------|---------------|---------|---------|----------|----------|
| Obsidian Database Plugin | 9 types (text, number, date, select, multi-select, checkbox, relation, rollup, file) | ✅ Search, column filters | ✅ Multi-column | ✅ By property | ✅ Rollup (read-only) |
| Make.md | 15+ types (text, number, boolean, date, option, tags, formulas, links, relations, flex, aggregate, object, images, repeat) | ✅ Advanced | ✅ Multi-column | ✅ "Group by" option | ✅ Comprehensive (Notion-like) |
| Kanban for Professionals | Inline metadata (due, tags, priority, Dataview fields) | ✅ Space-separated tokens | ✅ Manual | ✅ Swimlanes | ❌ |
| Dataview | All YAML + inline fields | ✅ WHERE clause | ✅ SORT | ✅ GROUP BY | ✅ JavaScript (DataviewJS) |
| Obsidian Bases | YAML Properties | ✅ Clickable UI | ✅ Clickable | ❌ (roadmap) | ✅ Functions (Overdue, due in days, etc.) |

### Table: Performance & Stability

| Plugin | Performance | Stability | Known Issues |
|--------|-------------|-----------|--------------|
| Obsidian Database Plugin | Good (Preact-based) | Pre-1.0.0 | External renames break relation backlinks |
| Make.md | Moderate | **Buggy** | "regularly find it buggy and/or unresponsive" [9]; 184 open issues |
| Obsidian Projects | Good | Stable (archived) | Known bugs: column width, boolean recognition |
| Kanban for Professionals | Good | Stable | Limited to Kanban data model |
| Obsidian Planner | Unknown (low adoption) | Pre-release | 30 stars, limited testing |
| DB Folder | Poor with large vaults | Stable (archived) | "performance really starts to get quite bad" [13]; needs manual refresh |
| Dataview | Excellent | Stable | Read-only output; invisible to graph/grep |
| Obsidian Bases | **Excellent** | Beta | "5,000 notes here and it just popped up" [3]; limited view types |

### Table: Learning Curve & Community

| Plugin | Learning Curve | Documentation | Community Support | Update Frequency |
|--------|---------------|---------------|-------------------|------------------|
| Obsidian Database Plugin | Moderate | GitHub README | Limited (pre-registry) | Active (pre-1.0.0) |
| Make.md | Moderate | GitHub, website | Discord community, active forum | Active (1.3.5) |
| Obsidian Projects | Low | Blog post, videos | Large (archived) | **Discontinued** |
| Kanban for Professionals | Low | Plugin page | Limited (458 downloads) | Active |
| Obsidian Planner | Moderate | GitHub README | Very limited (30 stars) | Early stage |
| DB Folder | Moderate | GitHub Pages, videos | Large (archived) | **Discontinued** |
| Dataview | **Steep** | Comprehensive docs | **Largest** (4.8M downloads) | Active (holroy) |
| Obsidian Bases | **Low** | Official help page | Official Obsidian team | Active (core plugin) |

---

## View-by-View Analysis

### Table View

**Best options:** Obsidian Database Plugin (most Notion-like with inline editing), Obsidian Bases (fastest, native, no coding), Dataview (most powerful queries, but read-only)

The Obsidian Database Plugin offers the most complete table view experience with inline editing for all cell types, sorting, filtering, and search. Obsidian Bases is significantly faster and requires no coding, but is currently in beta and only available to Catalyst members. Dataview offers the most powerful querying capabilities but is read-only, meaning users cannot edit data directly in the table.

### Kanban View

**Best options:** Kanban for Professionals (Board + Table + List, one-click switching), Obsidian Database Plugin (drag-and-drop cards grouped by select/multi-select properties), Dataview GROUP BY (read-only, no drag-and-drop)

The Kanban for Professionals plugin offers the most polished Kanban experience with three views switchable by one click. However, it stores data in the Kanban code block format rather than YAML frontmatter, limiting cross-plugin integration. The Obsidian Database Plugin stores Kanban data in YAML frontmatter, ensuring full compatibility with other plugins. The Dataview GROUP BY approach works but is read-only and does not support drag-and-drop.

### Calendar View

**Best options:** Full Calendar Remastered (most feature-complete, Google Calendar sync, CalDAV), Obsidian Database Plugin (monthly calendar with drag-to-reschedule), Obsidian Planner (six calendar layouts via FullCalendar), Dataview CALENDAR (simple date-point visualization)

Full Calendar Remastered is the most comprehensive calendar solution with two-way Google Calendar sync, CalDAV sync, ICS import, and task backlog drag-and-drop [9]. The Obsidian Database Plugin and Obsidian Planner offer built-in calendar views that draw from the same YAML data. Dataview's CALENDAR query type provides a simple point-based calendar visualization but is read-only.

### List View

**Best options:** Make.md (native List view), Kanban for Professionals (List view on same cards), Dataview LIST (most powerful, but read-only), Obsidian Planner (Task List view)

Make.md has a native List view as one of its many view types, though the plugin's stability issues are a concern. Kanban for Professionals offers a List view of the same cards, but is Kanban-centered. Dataview LIST is the most powerful and flexible option but is read-only and invisible to the graph and backlinks. Obsidian Planner offers a Task List view with virtual scrolling.

---

## Can a Single Plugin Achieve All Four Views?

**No single plugin currently achieves all four views (Table, Kanban, Calendar, and List) on the same dataset with a polished, unified experience.**

The closest options are:

1. **Obsidian Database Plugin (ekmungi)** — Has Table, Kanban, Calendar, and Timeline views. **Missing: List view.** The Table view can be configured to approximate a list, but not identically.

2. **Make.md** — Has Table, List, Board (Kanban), Calendar, and many other views. **Theoretically has all four views.** However, stability issues and bugs make it unreliable for production use.

3. **Obsidian Planner (SawyerRensel)** — Has Calendar, Kanban, Timeline, and Task List views. **Missing: True Table view.** The Task List is table-style but task-focused, and the plugin is in early development.

4. **Kanban for Professionals** — Has Board, Table, and List views. **Missing: Calendar view.** Calendar export is available in Pro but exports to .ics (external calendar), not an in-app view.

5. **Combination approach (Dataview + Kanban + Calendar)** — Can achieve all four views on the same YAML data, but **suffers from the Kanban data silo problem** where the Kanban plugin stores data in its own format, not in YAML frontmatter.

---

## Recommendations

### For Users Who Want the Closest Notion Experience in a Single Plugin

**Use the Obsidian Database Plugin (ekmungi)** — It has Table, Kanban, Calendar, and Timeline views on the same YAML frontmatter data. It is pre-1.0.0 but actively developed and offers the most Notion-like feature set of any single plugin. The lack of a List view is the main limitation, but the Table view can be configured to approximate one. Install via BRAT until it reaches the community plugin registry.

### For Users Who Prioritize Stability and Long-Term Support

**Use Obsidian Bases (core plugin)** — Built by the Obsidian team, it offers instant performance, a visual editor, and guaranteed long-term support. The current limitation is that it only supports Table, Card, and List views—Kanban and Calendar views are on the roadmap. For users who need those views immediately, supplement with Dataview for Calendar queries and the Kanban for Professionals plugin for Kanban, accepting the data silo limitation.

### For Users Who Need a List View and Are Willing to Accept Instability

**Use Make.md** — It has the most view types (including a native List view) and closest feature parity to Notion. However, users should be prepared for bugs and potential data issues. Test thoroughly before committing to a large workflow.

### For Users Who Want the Combination Approach

**Use Dataview for Table and List views, Dataview GROUP BY for Kanban (accepting read-only), and Full Calendar Remastered for Calendar.** This approach gives the most powerful querying capabilities and all four views, but requires accepting that Dataview results are read-only and invisible to the graph/backlinks. Use the Dataview Serializer plugin to make query results visible in published notes and Git diffs.

### For Users Who Want to Future-Proof Their Data

**Use standard YAML frontmatter with consistent property names across all notes.** This ensures data works with any plugin—Obsidian Database Plugin, Make.md, Obsidian Bases, or Dataview. The new Obsidian Bases core plugin is worth watching closely: it is built by the Obsidian team, offers fast visual database editing without coding, and has a clear roadmap for adding more view types.

---

## Sources

[1] The Obsidian Projects Plugin: My Secret Weapon for Staying Organized and Focused: https://readmedium.com/the-obsidian-projects-plugin-my-secret-weapon-for-staying-organized-and-focused-0a558e440cd3

[2] Notion-like content calendar in Obsidian // Obsidian Projects plugin (Nicole van der Hoeven): https://www.youtube.com/watch?v=ny8lksaQ5A8

[3] Introduction to Bases - Obsidian Help: https://obsidian.md/help/bases

[4] Kanban for Professionals - Obsidian Plugin: https://community.obsidian.md/plugins/kanban-pro-boards

[5] Obsidian Community Plugins search for "Kanban": https://community.obsidian.md/search?q=Kanban

[6] MAKE.md – Obsidian Plugin · Obsidian Stats: https://www.obsidianstats.com/plugins/make-md

[7] Best Offline Notion Alternative with Obsidian - Make.md Plugin (Antone Heyward, Apr 2025): https://www.youtube.com/watch?v=Ad03iBrgs6Q

[8] Revolutionize Your Obsidian Experience with MAKE.md Plugin (Antone Heyward, Jul 2023): https://www.youtube.com/watch?v=G-TF1yy8R9E

[9] MAKE.md - Help - Obsidian Forum: https://forum.obsidian.md/t/make-md/55662

[10] Obsidian Make.md · Outliner Software forum: https://www.outlinersoftware.com/topics/viewt/10108/0/obsidian-makemd

[11] Obsidian Database Folder - GitHub Pages: https://rafaelgb.github.io/obsidian-db-folder

[12] obsidian-db-folder/docs/docs/index.md at master · RafaelGB/obsidian-db-folder · GitHub: https://github.com/RafaelGB/obsidian-db-folder/blob/master/docs/docs/index.md

[13] My Obsidian Setup (Part 14) — Database Folder Plugin - Medium: https://medium.com/technology-hits/my-obsidian-setup-part-14-database-folder-plugin-932fe2e360ad

[14] obsidian-db-folder/README.md at master · RafaelGB/obsidian-db-folder · GitHub: https://github.com/RafaelGB/obsidian-db-folder/blob/master/README.md

[15] GitHub - ekmungi/obsidian-database-plugin: https://github.com/ekmungi/obsidian-database-plugin

[16] My Obsidian-Based Kanban Writing Workflow (Mike Schmitz, Jul 2021): https://thesweetsetup.com/my-obsidian-based-kanban-writing-workflow

[17] Build a Kanban Board with Obsidian + Dataview Plugin (Justin, Effective Remote Work, May 2021): https://www.youtube.com/watch?v=rGFb6j9KDh4

[18] Task List Kanban – Obsidian Plugin: https://www.obsidianstats.com/plugins/task-list-kanban

[19] "'Kanbanibalization' in Obsidian" by Stowe Boyd, Medium: https://medium.com/workings/kanbanibalization-in-obsidian-9abc6a83c144

[20] Query your notes like a pro with the Dataview and Dataview Serializer plugins (Sébastien Dubois, Apr 2025): https://www.youtube.com/watch?v=j2q6OF5XFUc

[21] Query from lists using dataview - Basement - Obsidian Forum: https://forum.obsidian.md/t/query-from-lists-using-dataview/23881

[22] Dataview - Obsidian Plugin: https://community.obsidian.md/plugins/dataview

[23] Dataview in Obsidian: A Beginner's Guide: https://obsidian.rocks/dataview-in-obsidian-a-beginners-guide

[24] Dataview query to extract a list item and all its sublist items - Help - Obsidian Forum: https://forum.obsidian.md/t/dataview-query-to-extract-a-list-item-and-all-its-sublist-items/78291

[25] GitHub - SawyerRensel/Planner: Unified calendar, kanban, timeline, and task list: https://github.com/SawyerRensel/Planner

[26] Obsidian Project Management Setup That Works on Mobile (TaskForge blog, May 2026): https://taskforge.md/blog/obsidian-project-management

[27] Obsidian vs Notion 2026: 1,400 Plugins vs 100M Users [Tested]: https://tech-insider.org/obsidian-vs-notion-2026

[28] Notion vs Obsidian for Developers: APIs, Plugins, and Why I Use Both: https://dev.to/trackstack/notion-vs-obsidian-for-developers-apis-plugins-and-why-i-use-both-16d0

[29] Obsidian vs. Notion: I Tried Both and Here's How They Differ: https://learn.g2.com/obsidian-vs-notion

[30] I tested Obsidian Bases against Notion with a real project, and one of them fell apart: https://www.xda-developers.com/tested-obsidian-bases-against-notion-with-real-project-one-fell-apart

[31] Moving from Notion to Obsidian - daverupert.com: https://daverupert.com/2025/05/notion-to-obsidian

[32] The Complete Guide to Dataview in Obsidian - Query Everything, Then Make It Last (Sébastien Dubois, Aug 2026): https://www.dsebastien.net/the-complete-guide-to-dataview-in-obsidian

[33] Tech Habits: Obsidian Kanban and Full Calendar Integration - Medium: https://medium.com/@geetduggal/tech-habits-obsidian-kanban-and-full-calendar-integration-a05a7ff2d2f6

[34] Displaying data - Database Folder documentation: https://rafaelgb.github.io/obsidian-db-folder/features/Displaying%20data

[35] MASTER Obsidian's Powerful DATABASE FOLDER Plugin - Step by Step (Sascha D. Kasper, Oct 2023): https://www.youtube.com/watch?v=lIuZAik1jPM

[36] Obsidian Plugin to Allow Notion like database based on folders · GitHub (RafaelGB): https://github.com/RafaelGB/obsidian-db-folder

[37] Real use case for Obsidian: Dataview and Database Folder (Nicole van der Hoeven, Oct 2022): https://www.youtube.com/watch?v=Ak7cuIyQeYw

[38] What are the differences between various database plugins? - Obsidian Forum: https://forum.obsidian.md/t/what-are-the-differences-between-various-database-plugins/39406

[39] Dataview vs Datacore vs Obsidian Bases - Obsidian Rocks: https://obsidian.rocks/dataview-vs-datacore-vs-obsidian-bases

[40] Full Calendar (Remastered) - Obsidian Plugin: https://community.obsidian.md/plugins/full-calendar-remastered

[41] Full Calendar Remastered - Documentation Site: https://obsidian-full-calendar-remastered.github.io/plugin-full-calendar

[42] GitHub - community-archive/obsidian-full-calendar: https://github.com/obsidian-community/obsidian-full-calendar

[43] GitHub - liamcain/obsidian-calendar-plugin: https://github.com/liamcain/obsidian-calendar-plugin

[44] Arcadia Projects - Obsidian Plugin: https://community.obsidian.md/plugins/arcadia-projects
