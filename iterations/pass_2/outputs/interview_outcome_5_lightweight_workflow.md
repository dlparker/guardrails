# Interview Outcome 5: Lightweight Workflow for Process Tracking

## Context

The original story1.md workflow involved moving files between directories (`tasks/todo/`, `tasks/doing/`, `tasks/done/`, `tasks/discarded/`) and recording git hashes in task files. This raised the question: Is this bookkeeping overhead appropriate given the minimal specification principle?

## Problems Being Solved

### 1. Context Pollution
**Problem:** Hard to get LLMs to stop including previously discarded code/docs in new analysis, even when explicitly told to ignore it.

**Strategy:** Physically remove discarded code and process docs so they can't leak back into agent context.

### 2. Preserving Ideas for Later
**Problem:** Some experiments aren't right for now but might be useful in different contexts later.

**Strategy:** Keep the code accessible but separated from active work ("retiring" vs. "discarding").

## Solution: Git-Based Code Management + Status Field Tracking

### For Experiment Code (Addressing Context Pollution)

Use git-native workflow instead of file movement:

**Each task produces a spike:**
1. Coder commits the spike: `git commit -m "Spike: try DirectoryTree picker"`
2. User evaluates the code
3. Disposition decision:

**Save (keep in working tree):**
```bash
# Code stays, it's the current state
# Story/task status updated to "done"
```

**Retire (preserve but remove from working tree):**
```bash
git tag retired/directorytree-picker
git reset --hard HEAD~1
# Code removed from working tree (no context pollution)
# Tag preserves access: git show retired/directorytree-picker
# Story/task status updated to "retired"
```

**Discard (remove from working tree):**
```bash
git reset --hard HEAD~1
# Code removed from working tree (no context pollution)
# Still in git history but not tagged (effectively forgotten)
# Story/task status updated to "discarded"
```

**Benefits:**
- Solves context pollution: reset removes code from working tree
- Solves idea preservation: tags make retired experiments findable
- No separate tracking mechanism needed
- Git handles all the bookkeeping
- Can review retired idea anytime: `git show retired/directorytree-picker`
- List retired experiments: `git tag -l 'retired/*'`

### For Story/Task Tracking (Addressing Workflow Overhead)

Use **status fields in markdown files** instead of moving files between directories.

**Directory Structure (simplified):**
```
process_docs/
├── stories/
│   ├── story1.md
│   ├── story2.md
│   └── ...
├── tasks/
│   ├── task1_1.md
│   ├── task1_2.md
│   └── ...
└── archive/  (optional, for completed/retired items)
```

**Status Field in Each File:**
```markdown
**Story ID:** 1
**Story Name:** GnuCash finder experiment
**Status:** doing  <!-- values: todo | doing | done | discarded | retired -->
**Phase:** exploring
**Story Type:** study
```

**Workflow Transitions:**

**Starting a story:**
- Update: `Status: todo` → `Status: doing`
- Commit: `git commit -m "Story 1: Started GnuCash finder experiment"`

**Completing a story:**
- Update: `Status: doing` → `Status: done`
- Commit: `git commit -m "Story 1: Completed"`

**Retiring a story:**
- Update: `Status: doing` → `Status: retired`
- Optionally move to archive: `git mv process_docs/stories/story1.md process_docs/archive/`
- Commit: `git commit -m "Story 1: Retired - preserved for future reference"`

**Discarding a story:**
- Update: `Status: doing` → `Status: discarded`
- Optionally move to archive or delete
- Commit: `git commit -m "Story 1: Discarded"`

**Benefits:**
- No directory structure overhead
- All stories visible in one place
- Status queryable: `grep "Status: doing" process_docs/stories/*.md`
- Git history shows status transitions
- Clean migration to database: Status field → DB column
- Minimal overhead for small cycles

## Clerk Role Workflow (Simplified)

**For Study stories with multiple tasks:**

1. **Story Start**
   - Update story status: `todo` → `doing`
   - Commit status change

2. **For each task:**
   - Create task file in `process_docs/tasks/` with status `doing`
   - Coder builds spike
   - Coder commits spike code: `git commit -m "Spike: [task name]"`
   - Reporter presents results to user
   - User decides: save / retire / discard
   - Execute git commands (keep, tag+reset, or reset)
   - Update task status in task file: `doing` → `done/retired/discarded`
   - Commit task status change

3. **Story Completion**
   - Reporter generates summary (optional for quick cycles)
   - User decides story disposition
   - Update story status: `doing` → `done/retired/discarded`
   - Commit story status change

**For very small cycles:** Some steps can be combined or skipped to minimize overhead.

## Rationale Capture (Future Enhancement)

Story files can accumulate evaluation notes:

```markdown
## Evaluation Notes

### Task 1: DirectoryTree picker
**Status:** retired
**Git Tag:** retired/directorytree-picker
**Rationale:**
Too much code for something that should be simple. Requires building
custom picker from base widget. Not worth the effort for this use case.

### Task 2: textual-fspicker
**Status:** saved
**Rationale:**
Purpose-built library, straightforward integration. Hits the sweet spot -
dedicated file picker functionality without over-engineering. Going with this.

### Task 3: textual-filedrop
**Status:** discarded
**Rationale:**
Drag-and-drop feels wrong for GnuCash file selection. Users know where
the file is and want to browse to it. This is solving the wrong UX problem.
```

With future voice transcription tooling, these notes get auto-populated.

## Future State: Database Tool

The current markdown + status field approach is **intentionally temporary** scaffolding.

**Planned evolution:**
1. **Now (Exploring phase):** Markdown files with status fields
2. **Near-term:** Story generator tool with Q&A + JSON schema
3. **Medium-term:** Lightweight DB for managing process flow
   - Stories become DB models
   - Tasks become DB models
   - Status transitions tracked in DB
   - Git integration for code dispositions
   - Reports generated from DB state

**Migration path:** Status field → DB column is trivial.

The markdown approach minimizes overhead during exploration while establishing structure for future tooling.

## Implementation in Guardrails Process

### 1. Update Story Type Standard Workflow Section

Replace file-movement workflow with status-field workflow:

```markdown
# Story Type Standard Workflow

Stories always involve actions in the "clerk" and "reporter" role, plus one
or more roles as needed per task.

1. Clerk: Update story status: todo → doing, commit
2. Analyst: Create task files in process_docs/tasks/ (with status: doing)
3. For each task:
   1. Coder: Build minimal spike, commit with message "Spike: [task name]"
   2. Reporter: Present results to user for save/discard/retire decisions
      - If save: Keep code, update task status to done
      - If retire: Tag and reset code, update task status to retired
      - If discard: Reset code, update task status to discarded
   3. Clerk: Commit task status change
4. Reporter: Generate summary report (optional for small cycles)
5. Clerk: Update story status based on user disposition, commit
```

### 2. Story Template Updates

Add status field to all story templates:

```markdown
**Story ID:** [number]
**Story Name:** [name]
**Status:** todo  <!-- todo | doing | done | discarded | retired -->
**Phase:** [exploring | pioneering | settling | fortifying | re-founding]
**Story Type:** [study | poc | framing | glueing | anchoring | joining | user | compliance]
```

### 3. Task Template (Create)

Define minimal task template:

```markdown
**Task ID:** [story_id].[task_number]
**Task Name:** [name]
**Parent Story:** [story_id] - [story_name]
**Status:** doing  <!-- doing | done | discarded | retired -->
**Task Type:** [spike code | spike report | poc | component | scaffold | demo test | test | covert test]

## Description
[What needs to be done]

## Result
[Link to commit, or git tag if retired]

## Notes
[Any observations, issues encountered, decisions made]
```

### 4. Git Workflow Documentation

Add to process definition:

```markdown
## Git Workflow for Experiments

**Saving experiment results:**
- Code remains in working tree
- Task status → done

**Retiring experiment results:**
- Tag: `git tag retired/[descriptive-name]`
- Reset: `git reset --hard HEAD~1`
- Task status → retired
- Preserved for future reference: `git show retired/[descriptive-name]`

**Discarding experiment results:**
- Reset: `git reset --hard HEAD~1`
- Task status → discarded
- Removed from working tree, no tag (effectively forgotten)
```

## Benefits Summary

**Addresses context pollution:**
- ✓ Git reset physically removes code from working tree
- ✓ Agent can't reference what's not there

**Preserves useful ideas:**
- ✓ Git tags make retired experiments findable
- ✓ Can review anytime: `git show retired/name`

**Minimizes overhead:**
- ✓ No directory structure complexity
- ✓ No file movement between directories
- ✓ Status field updates are fast
- ✓ Git handles bookkeeping

**Migration-friendly:**
- ✓ Status field → DB column is trivial
- ✓ Markdown structure maps to DB models
- ✓ Git workflow remains unchanged

**Scales with cycle size:**
- Small cycles: Minimal status updates
- Large cycles: Can add more tracking if needed
- Always proportional to value

## Next Steps for Guardrails Project

1. **Update process definition** with status-field workflow
2. **Create story template** with status field
3. **Create task template** with status field
4. **Document git workflow** for code dispositions
5. **Test with real stories** to validate overhead is manageable
6. **Build story generator tool** (Q&A + JSON schema)
7. **Eventually build DB tool** when process stabilizes
