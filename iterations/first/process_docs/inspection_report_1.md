# Inspection Report: Study Story Template Design
## Process Documentation Review Session

**Document Under Review:** `process_docs/stories/todo/gnucash_file_selection_study.md`
**Review Date:** 2025-11-09
**Participants:**
- Author: dparker (Lead Developer)
- Reviewer: Claude (AI Code Assistant)
- Recorder: Claude

**Related Documents:**
- `ai_docs/background/foundations_concept_summary.md`
- `ai_docs/process_definition.md`

**Review Objective:** Evaluate clarity and completeness of Study story template for guiding AI agents with minimal context window usage.

---

## Executive Summary

The Study story template demonstrates strong architectural design for constraint-driven agentic development. The Phase constraints are clear and actionable. The main areas requiring refinement are: (1) story-type-specific workflows, (2) the Mode/Directive field definition, and (3) task metadata field explanations. Discussion revealed that many perceived gaps are intentional design choices supporting a programmatic generation strategy and context efficiency goals.

**Overall Assessment:** Template is 80% ready for use. Remaining work involves adding workflow sections and resolving the Mode vs. Directive design decision.

---

## Issues Identified

### ISSUE-01: Role and Mode Fields Undefined
**Severity:** Major
**Category:** Missing Definition

**Description:**
Task metadata items #5 (Role) and #6 (Mode) are required fields but not defined in the story document. Reviewer initially could not determine valid values.

**Root Cause:**
Design intent is for definitions to exist in separate reference file (`process_definition.md`) to support context efficiency goals. Story template must balance self-contained guidance vs. avoiding redundancy with reference docs.

**Discussion Outcome:**
- Role definitions exist in `process_definition.md` §Actor Roles
- Mode may evolve into "Directive" (free-form field with library support)
- Author plans directive library tool (search/create/browse) to maintain consistency without rigid taxonomy

**Proposed Resolution:**
1. Add minimal reference in task metadata section: "For Role definitions, see process_definition.md §Actor Roles"
2. Replace "Mode" with "Directive" in template
3. Add directive guidance: "Free-form field stating what to produce, what NOT to do, expected scope. Search directive library for consistency."

**Status:** OPEN - Awaiting author decision on Mode vs. Directive
**Priority:** HIGH - Blocks task file creation

---

### ISSUE-02: Missing Story-Type-Specific Workflow
**Severity:** Major
**Category:** Missing Content

**Description:**
Story template does not include canonical workflow steps for executing a Study story. Reviewer had to infer sequence: create tasks → execute → review → report.

**Root Cause:**
Template currently focuses on phase constraints (Exploring) and story type description but lacks procedural guidance. Author confirmed different story types likely need different workflows.

**Proposed Resolution:**
Add "Study Story Workflow" section to generic template:
```
## Study Story Workflow
1. Capture current git hash
2. Create task files in process_docs/tasks/pending/ (one per option to evaluate)
3. For each task:
   a. Record starting git hash in task file
   b. Build minimal spike
   c. Record ending git hash in task file
4. Present results to lead developer for save/discard decisions
5. Generate summary report analyzing experiments and decisions

The git hashes enable retrospective analysis. Reporter role can examine
exactly what was changed via `git diff {start_hash} {end_hash}`.
```

**Status:** OPEN - Author confirmed this should be added
**Priority:** HIGH - Critical for agent autonomy

---

### ISSUE-03: Task Metadata Fields Need Inline Explanation
**Severity:** Minor
**Category:** Clarity

**Description:**
11-item task metadata list includes fields whose purpose is not immediately clear:
- Item #10: "placeholder for save/discard decision" - when/how is this populated?
- Item #11: "optional placeholder for name of different task if results chosen in preference" - workflow unclear

**Root Cause:**
Template assumes familiarity with the overall process workflow. Context-efficient design means not repeating process_definition.md content, but critical fields need brief clarification.

**Proposed Resolution:**
Add 1-sentence explanations for ambiguous items:
```
10. Save/discard decision (populated by lead developer after task completion)
11. Optional: If results discarded in favor of another task, reference that task name
```

**Status:** OPEN
**Priority:** MEDIUM - Improves usability but agents can ask for clarification

---

### ISSUE-04: Git Hash Workflow Timing Unclear
**Severity:** Minor
**Category:** Procedural Ambiguity

**Description:**
When exactly should git hashes be recorded? Before writing task file? After? Should each task have its own commit?

**Root Cause:**
Git hashes serve as audit trail for retrospective analysis, not rollback mechanism. This purpose was clarified during discussion but not explicit in template.

**Discussion Outcome:**
Author explained: "I want to be able to run experiments and then go back and review the report and find in those reports just exactly what was done in the experiment in code and process docs."

**Proposed Resolution:**
Add to workflow section (see ISSUE-02 resolution):
```
The git hashes enable retrospective analysis. Reporter role can examine
exactly what was changed via `git diff {start_hash} {end_hash}`.
```

**Status:** RESOLVED via ISSUE-02 workflow addition
**Priority:** N/A - superseded

---

### ISSUE-05: Expected Artifacts Definition Vague
**Severity:** Minor
**Category:** Specification Gap

**Description:**
Story says "A description of the expected artifacts" should be in task files, but doesn't specify what artifacts are expected for file picker experiments (code? screenshots? written analysis?).

**Root Cause:**
This is intentionally story-specific content to be provided by generator, not generic template content.

**Discussion Outcome:**
Author clarified that story generation will be programmatic, with generic elements (like Phase constraints) plus specifics (like expected artifacts list). The current story file already contains specifics section; this would be populated by generator.

**Proposed Resolution:**
No template change needed. Expected artifacts should be in "Specific" section of generated stories. Current story could add:
```
Expected artifacts per task:
- Runnable spike demonstrating the file picker approach
- Brief notes on observations (ease of use, limitations, fit with DataService)
```

**Status:** RESOLVED - Working as designed
**Priority:** N/A - No action needed for template

---

### ISSUE-06: Task Creation Timing Ambiguous
**Severity:** Minor
**Category:** Procedural Ambiguity

**Description:**
Should all task files be created upfront, or create one → execute → create next? Phrasing "first artifact that will be produced" suggests upfront but not definitive.

**Root Cause:**
Workflow sequence not explicit (see ISSUE-02).

**Proposed Resolution:**
Workflow section (ISSUE-02) clarifies: "Create task files... (one per option)" at step 2, before execution begins at step 3.

**Status:** RESOLVED via ISSUE-02
**Priority:** N/A - superseded

---

### ISSUE-07: Workspace Organization Not Specified
**Severity:** Minor
**Category:** Missing Guidance

**Description:**
Where should experimental code live? In `src/ctrack/textual/`? Separate experiment directory? `demo_work/`?

**Root Cause:**
Generic template should provide workspace convention to maintain repository organization.

**Proposed Resolution:**
Add to generic Study template:
```
## Workspace Convention
Place experimental code in: process_docs/experiments/{story-slug}/{task-name}/

This keeps exploratory spikes separate from production source tree.
```

**Status:** OPEN
**Priority:** LOW - Agents can ask or infer, but convention helps consistency

---

### ISSUE-08: "Definition of Done" Missing
**Severity:** Minor
**Category:** Specification Gap

**Description:**
What makes this story "complete"? After all 3 approaches tried? After lead picks one? After report written?

**Root Cause:**
This is story-specific, should be in the "Specific" section of generated story (not generic template).

**Proposed Resolution:**
Current story should add to "Specific" section:
```
**Definition of Done:**
- All 3 file picker approaches have been implemented as minimal spikes
- Lead developer has reviewed results and made save/discard decisions
- Summary report generated documenting findings and rationale
```

Generic template can note: "Each story should include Definition of Done in Specific section."

**Status:** OPEN - Story-specific, not template issue
**Priority:** LOW - Helpful but not blocking

---

### ISSUE-09: Save/Discard Decision Process Unclear
**Severity:** Minor
**Category:** Process Gap

**Description:**
Item #10 references "save/discard decision" but doesn't explain: when does this happen? How is it recorded? What does "save" mean practically (keep code? just note it?)?

**Root Cause:**
Process interaction between agent and lead developer not fully specified in document. This may be part of larger process definition, not Study-story-specific.

**Discussion Outcome:**
Author's session capture tool and git audit trail suggest this is part of retrospective review process. Study stories produce ephemeral spikes; "save" likely means "use as reference implementation for future Forming stories."

**Proposed Resolution:**
Generic Study template should clarify:
```
After task completion, lead developer reviews results and records decision:
- SAVE: This approach/spike is reference for future implementation
- DISCARD: Approach rejected, document rationale in task file
- SUPERSEDED: Different task's approach preferred, reference that task
```

**Status:** OPEN
**Priority:** MEDIUM - Important for process closure

---

### ISSUE-10: Mode/Directive Taxonomy Decision
**Severity:** Major
**Category:** Design Decision Required

**Description:**
"Mode" field exists in task metadata but no taxonomy defined. Discussion revealed Mode was conceived to capture micro-rhythms of coding (Code Scoping, Coding, Reviewing, Refactoring) but may be over-engineered.

**Root Cause:**
Author is in "Exploring" phase on process design itself. Mode was intuitive but not fully validated. Tension between rigid taxonomy (easy to bootstrap) vs. free-form (flexible but leads to inconsistency).

**Discussion Outcome:**
Author considering "Directive" as free-form field with library support as alternative:
- Directive: "Scope integration points, estimate change size (DO NOT implement)"
- Directive library tool with search/create/browse prevents drift
- Allows evolution without taxonomy maintenance burden

**Proposed Resolution:**
Author decision required:

**Option A: Keep Mode, define taxonomy**
- Define modes for each role (coder, planner, reporter, etc.)
- Add to process_definition.md
- More structured, but maintenance burden

**Option B: Replace with Directive field**
- Free-form field with suggested patterns
- Build directive library tool (separate Study story)
- More flexible, grows organically

Author leaning toward Option B based on discussion.

**Status:** OPEN - AUTHOR DECISION REQUIRED
**Priority:** HIGH - Blocks task file template finalization

---

### ISSUE-11: Context Efficiency Strategy Needs Documentation
**Severity:** Observation
**Category:** Meta-Process

**Description:**
Discussion revealed sophisticated design intent: stories must be self-contained to avoid requiring large reference docs in context, but also avoid bloat. This balancing act is not documented anywhere.

**Root Cause:**
This is a design principle guiding the entire process but not explicitly stated in any reviewed document.

**Proposed Resolution:**
Consider adding to `process_definition.md` or creating `design_principles.md`:
```
## Context Window Efficiency

Story templates balance two constraints:
1. Self-contained: Include enough guidance for agents to work autonomously
2. Non-redundant: Reference external taxonomies rather than duplicating

Generated stories should:
- Embed phase-specific constraints (varies by phase)
- Embed story-type-specific workflow (varies by type)
- Reference stable taxonomies (roles, phases) by name only
- Include story-specific details (options, expected artifacts, definition of done)
```

**Status:** OPEN - Enhancement for future iteration
**Priority:** LOW - Process works without this, but documenting rationale helps future maintainers

---

### ISSUE-12: Dogfooding Opportunity
**Severity:** Observation
**Category:** Process Validation

**Description:**
Author is designing a process for constraint-driven agentic coding and could use that process to build itself (e.g., directive library as Study/Pathfinder stories).

**Root Cause:**
N/A - This is an opportunity, not a defect.

**Discussion Outcome:**
Author enthusiastically endorsed: "Love your last suggestion. I will do that after I go through this whole conversation..."

**Proposed Resolution:**
After resolving open issues from this inspection, create stories for:
- Study: Directive library design (evaluate storage formats, search approaches)
- Pathfinder: Directive library CLI prototype
- Study: Story generator design

This validates process on non-trivial work and generates real task file examples.

**Status:** ACCEPTED - Author will do after addressing this inspection
**Priority:** N/A - Future work

---

## Summary of Actions Required

### Author Decisions Needed (Blocking)
1. **ISSUE-10:** Choose Mode vs. Directive approach
2. **ISSUE-01:** Approve directive field guidance wording

### Template Content Additions (High Priority)
3. **ISSUE-02:** Add Study Story Workflow section
4. **ISSUE-09:** Clarify save/discard decision process

### Template Content Additions (Medium Priority)
5. **ISSUE-03:** Add inline explanations for task metadata fields
6. **ISSUE-07:** Add workspace convention guidance

### Story-Specific Content (For current story)
7. **ISSUE-05:** Add expected artifacts list to Specific section
8. **ISSUE-08:** Add Definition of Done to Specific section

### Future Enhancements (Low Priority)
9. **ISSUE-11:** Document context efficiency strategy in process_definition.md
10. **ISSUE-12:** Use process to build directive library (dogfooding)

---

## Reviewer Notes

The author's systems thinking is impressive. The meta-stack of using session transcripts as artifacts, committing them for synthesis, and cross-pollinating between ctrack and guardrails repos shows sophisticated engineering practice.

The constraint-driven approach is well-suited to preventing agentic over-engineering. The explicit phase guidance ("disposable," "no error handling") directly addresses common LLM failure modes.

The open questions about Mode vs. Directive reflect appropriate "Exploring" phase thinking - preferring to validate concepts before committing to structure. The directive library idea elegantly solves the taxonomy rigidity problem.

Key insight from discussion: This is not just a process for building software, it's a process for **building processes**. The self-referential nature requires careful bootstrapping, which author is handling thoughtfully.

---

**End of Inspection Report**
