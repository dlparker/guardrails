# Guardrails Process - Action Plan

## Executive Summary

This action plan consolidates insights from the story1.md review interview into concrete next steps for developing the guardrails process framework. Six key outcomes emerged that fundamentally shape how the process should work:

1. **Story Type Rules** - Phase-specific guidance that focuses agent attention appropriately
2. **Autonomy Spectrum** - Detail level varies by phase (high autonomy early, high specification later)
3. **Minimal Specification Principle** - Process overhead must remain proportional to cycle size
4. **Subjective Evaluation** - Early-phase evaluation requires human design intuition, not criteria checklists
5. **Lightweight Workflow** - Git-native code management + status fields instead of heavy file movement
6. **Directives Library** - Reusable focus patterns that shape agent behavior

These outcomes work together to address the core tension: **How to guide AI agents toward the right level of investment without adding overhead that kills productivity?**

## Core Principles Discovered

### 1. The Completeness Problem
LLM coding assistants have a strong inclination toward completeness and production thinking. The guardrails process must actively counteract this in exploratory phases through:
- Story Type Rules that give explicit permission to be minimal
- Autonomy Spectrum that clarifies when to figure things out vs. ask
- Minimal Specification that trusts agent judgment within constraints

### 2. The Overhead Constraint
For small exploratory cycles, if story writing + review takes longer than the coding work, the process has failed. Every addition to the process must be justified by value creation, not theoretical completeness.

### 3. The Context Pollution Problem
Discarded experiments leak back into agent thinking even when explicitly told to ignore them. Solution: Physically remove code from working tree using git reset, preserve with tags when needed.

### 4. The Tacit Knowledge Problem
Design rationale and "why we chose this" thinking is almost always lost. Future enhancement: Voice transcription to capture subjective evaluation reasoning.

## Immediate Actions (Priority 1)

These are ready to implement now and provide immediate value.

### 1. Update Process Definition Document

**File:** `guardrails/docs/process_definition.md` (or similar)

**Add these sections:**

#### A. Autonomy Spectrum Section (after Phase Definitions)
```markdown
## Autonomy Spectrum

The guardrails process operates on a spectrum from high agent autonomy (in early phases)
to high specification detail (in later phases):

Exploring → Pioneering → Settling → Fortifying → Re-Founding
   ↑                                                    ↑
High Autonomy                                  High Specification
(figure it out)                                (follow exact specs)

This spectrum guides:
- How much detail stories should provide
- When agents should make pragmatic decisions vs. ask questions
- What level of completeness/polish is expected
- How precisely validation criteria must be specified

See Story Type Rules for phase-specific guidance on appropriate autonomy levels.
```

**Reference:** `interview_outcome_2_autonomy_spectrum.md`

#### B. Story Type Rules Section (after Test Rules)
```markdown
## Story Type Rules

### Study Story Rules

**Autonomy Level: HIGH** - You are expected to figure out implementation details,
run commands, validation approaches, and obstacle resolution pragmatically.

1. **Information over Implementation**: The goal is learning, not production code.
   Write the minimum code necessary to answer the question.

2. **Vague is Permissive**: Phrases like "probably need to," "some kind of," "might require"
   are permissions to handle pragmatically, not gaps requiring clarification.
   A journeyman programmer would figure it out - you should too.

3. **No Production Thinking**: Unless explicitly stated, ignore error handling, UI polish,
   edge cases, performance, logging, documentation. These belong in later phases.

4. **Unblock Yourself**: If you encounter obstacles (database state, missing files,
   dependency conflicts), resolve them the simplest way possible. Delete files,
   hard-code paths, use temporary scaffolding - whatever gets you to the learning
   objective fastest.

5. **Measure Success by Learning**: Did we answer the question? Did we reveal new
   information? Not: Is this code maintainable/testable/complete?

6. **Throw-away Mindset**: Assume this code will be discarded or heavily modified.
   Don't invest in its longevity.

### [Other Story Type Rules - To Be Defined Through Iteration]

POC, Framing, Glueing, Anchoring, Joining, User, Compliance story types each need
their own rule sets. These will be developed through practical application and iteration.

**Pattern for developing rules:**
- Define the phase's investment level
- Give pragmatic permissions
- Focus attention on what matters
- Define success criteria
- Set boundaries on what doesn't belong
```

**Reference:** `interview_outcome_1_story_type_rules.md`

#### C. Directives Section (after Story Definitions)
```markdown
## Directives

Directives are reusable focus patterns that specify how agents should approach work.
They are more specific than roles but more general than task details.

**Examples:**
- "ensure API methods have type annotations and doc strings"
- "build minimal spike ensuring resource supplies needed info"
- "identify existing code related to Story goals"
- "produce example code for user evaluation of specific solution options"

Users build a personal library of directives over time. The story generator tool
provides directive selection from the library.

**Directives work in combination with:**
- Story Type Rules (phase-level mindset)
- Autonomy Spectrum (detail level expectations)
- Task-specific instructions (concrete what-to-do)
```

**Reference:** `interview_outcome_6_directives_library.md`

#### D. Update Story Type Standard Workflow Section
Replace file-movement workflow with status-field + git workflow:

```markdown
# Story Type Standard Workflow

Stories always involve actions in the "clerk" and "reporter" role, plus one or more
roles as needed per task.

1. Clerk: Update story status: todo → doing, commit
2. Analyst: Create task files in process_docs/tasks/ (with status: doing)
3. For each task:
   1. Coder: Build minimal spike, commit with message "Spike: [task name]"
   2. Reporter: Present results to user for evaluation
   3. User decides disposition: save / retire / discard
   4. Execute git workflow:
      - Save: Keep code (current state)
      - Retire: `git tag retired/[name] && git reset --hard HEAD~1`
      - Discard: `git reset --hard HEAD~1`
   5. Clerk: Update task status: doing → done/retired/discarded, commit
4. Reporter: Generate summary report (optional for small cycles)
5. Clerk: Update story status based on user disposition, commit

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

**Reference:** `interview_outcome_5_lightweight_workflow.md`

### 2. Create Story Template with Status Field

**File:** `guardrails/templates/story_template.md`

```markdown
**Story ID:** [number]
**Story Name:** [descriptive name]
**Status:** todo  <!-- todo | doing | done | discarded | retired -->
**Phase:** [exploring | pioneering | settling | fortifying | re-founding]
**Story Type:** [study | poc | framing | glueing | anchoring | joining | user | compliance]
**Directive:** [Select from library or enter custom focus instruction]

**Story Goal:** [One sentence describing what this story aims to achieve]

## Context

[Background information, problem being solved, relevant code/features]

## Approach

[High-level approach or options to explore]

## Expected Results

[What should result from this story - code, decision, knowledge, etc.]

---

## Task Sketches (if applicable)

### Task [story_id].[task_number]: [task name]

**Task Type:** [spike code | spike report | poc | component | scaffold | demo test | test | covert test]

[Brief description of what this task entails]

---

## Evaluation Notes

[To be filled in after experiments complete - user's subjective evaluation and rationale]
```

**Notes:**
- Common Story Fields section will evolve through iteration
- Don't over-specify required fields - keep it minimal
- Template serves as guide, not rigid requirement

**Reference:** `interview_outcome_5_lightweight_workflow.md`

### 3. Create Task Template

**File:** `guardrails/templates/task_template.md`

```markdown
**Task ID:** [story_id].[task_number]
**Task Name:** [descriptive name]
**Parent Story:** [story_id] - [story_name]
**Status:** doing  <!-- doing | done | discarded | retired -->
**Task Type:** [spike code | spike report | poc | component | scaffold | demo test | test | covert test]
**Directive:** [Inherited from story or override]

## Description

[What needs to be done]

## Result

[Link to commit, or git tag if retired]

## Notes

[Any observations, issues encountered, decisions made]
```

**Reference:** `interview_outcome_5_lightweight_workflow.md`

## Near-Term Actions (Priority 2)

These require some implementation work but provide high value.

### 4. Build Story Generator Tool (Q&A + JSON Schema)

**Purpose:** Minimize user overhead for story creation through guided Q&A process.

**Core Features:**

1. **Question Flow:**
   - Story type selection (determines subsequent questions via autonomy spectrum)
   - Phase selection
   - Story goal (free text)
   - Context (optional, free text)
   - Directive selection (from library + custom)
   - Approach/options (for Study stories)
   - Expected results

2. **Directives Library:**
   - SQLite database or JSON file storage
   - CRUD operations: list, add, edit, delete
   - Search/filter by category
   - Usage tracking (count, last used)
   - Quick-add during story creation

3. **Output:**
   - Generated markdown file following story template
   - Auto-populated with user answers
   - Status field defaults to "todo"
   - Ready to commit to process_docs/stories/

4. **Technology Options:**
   - CLI tool with prompts (quick to build)
   - Web UI with NiceGUI (matches your existing tooling)
   - TUI with Textual (lightweight alternative)

**Implementation Steps:**

A. Define JSON schema for Q&A flow
```json
{
  "story_types": {
    "study": {
      "autonomy_level": "high",
      "required_fields": ["story_type", "phase", "story_goal", "directive"],
      "optional_fields": ["context", "approach", "task_sketches"],
      "questions": [...]
    },
    // ... other types
  }
}
```

B. Build directives library manager
- Simple CRUD CLI or minimal UI
- JSON storage initially, migrate to SQLite if needed
- Export/import functionality

C. Build story generator
- Interactive Q&A flow
- Directive selection from library
- Template rendering
- File output to process_docs/stories/

D. Test with real stories
- Generate story1.md equivalent using tool
- Measure time investment vs. manual writing
- Iterate on questions and flow

**Reference:** `interview_outcome_6_directives_library.md`

### 5. Document Minimal Specification Principle

**File:** `guardrails/docs/design_principles.md`

Create a design principles document that captures:

**Core Principle:**
Process overhead must remain proportional to cycle size. For small exploratory cycles,
story writing + review must not exceed coding time.

**Implications:**
- Default to less specification, add more only when proven necessary
- Prefer improving guidance (Story Type Rules) over adding specification requirements
- Optimize for small cycles - if process only works for large stories, it's failed
- Measure user time investment and keep it minimal
- Iterate based on actual agent behavior, not theoretical completeness

**Metrics for Success:**
- Writing Exploring-phase story: ~10-15 minutes (not 30+)
- Reviewing agent results: ~5-10 minutes (not 15+)
- Total overhead: <30 minutes for small cycles

**Testing Strategy:**
- Test with minimal specification first (Story Type Rules + Autonomy Spectrum)
- Identify failure patterns (when agents ask unnecessarily, make wrong choices)
- Adjust guidance, not stories
- Only add story specification if guidance fails

**Reference:** `interview_outcome_3_minimal_specification_principle.md`

### 6. Develop Remaining Story Type Rules

Through iteration on actual stories, develop rule sets for:

- **POC Story Rules** (sketch provided in outcome doc)
- **Framing Story Rules**
- **Glueing Story Rules**
- **Anchoring Story Rules** (sketch provided in outcome doc)
- **Joining Story Rules**
- **User Story Rules**
- **Compliance Story Rules**

**Process for developing:**
1. Write story without type-specific rules (use only general guidance)
2. Observe where agent struggles or makes wrong choices
3. Draft rules that would have prevented the issue
4. Test rules on next similar story
5. Refine based on results

**Pattern to follow (from Study Story Rules):**
- Define autonomy level
- Give pragmatic permissions
- Focus attention on what matters
- Define success criteria
- Set boundaries on what doesn't belong

**Reference:** `interview_outcome_1_story_type_rules.md`

## Medium-Term Actions (Priority 3)

These are enhancements that provide value but aren't immediately critical.

### 7. Build Simple Process Management Database

Once story generation is working and process is stabilizing:

**Features:**
- Stories and tasks as database models
- Status tracking and transitions
- Git integration (store commit hashes, tags)
- Query capabilities (show all "doing" stories, show retired experiments)
- Report generation

**Technology:**
- SQLite database (lightweight, no server)
- Python CLI or minimal UI
- Integration with story generator tool

**Migration:**
- Status fields in markdown → DB columns
- Existing markdown files → import script
- Preserve markdown as "source of truth" initially
- Eventually DB becomes source of truth

**Reference:** `interview_outcome_5_lightweight_workflow.md`

### 8. Create Story Examples Repository

Build a collection of example stories that demonstrate:

**Good Examples:**
- Study story with appropriate vagueness (like story1.md + fixes)
- POC story showing different focus
- Anchoring story showing production requirements
- How directives shape agent behavior
- Appropriate autonomy level by phase

**Bad Examples (Learning Opportunities):**
- Study story that over-specifies (production thinking)
- Anchoring story that under-specifies (too vague for production)
- Stories that violate minimal specification principle
- Stories that lack clear directive

**Format:**
- Markdown files in `guardrails/examples/`
- Annotated with commentary on what makes them good/bad
- Referenced in documentation
- Used for testing story generator tool

## Long-Term Enhancements (Priority 4)

These are valuable but can wait until the core process is proven.

### 9. Voice Transcription for Design Rationale Capture

**Vision:** Capture user's subjective evaluation thinking during experiment review.

**Features:**
- Voice recording during evaluation session
- Real-time transcription
- Attachment to story/task files
- Indexed for future search
- Preserves design rationale that would otherwise be lost

**Benefits:**
- Future developers understand "why we chose this"
- Can review thinking when revisiting decisions
- Builds institutional/project memory
- Captures tacit knowledge in explicit form

**Implementation:**
- Integration with story management tool
- Voice-to-text service (OpenAI Whisper, cloud services, etc.)
- Storage format: markdown sections in story files
- Query interface: "Why did we choose approach X?"

**Reference:** `interview_outcome_4_subjective_evaluation.md`

### 10. Agent Behavior Testing Framework

Build automated testing for agent behavior:

**Purpose:** Validate that Story Type Rules + Autonomy Spectrum produce expected behavior

**Tests:**
- Present story with vague validation criteria → Does agent choose pragmatically?
- Present Study story → Does agent avoid production thinking?
- Present Anchoring story → Does agent add proper error handling?
- Present high-autonomy phase → Does agent figure out run commands?

**Implementation:**
- Test harness that presents stories to agents
- Captures agent questions and implementation choices
- Compares against expected behavior
- Regression testing when process definition changes

**Value:**
- Validates process changes don't break existing stories
- Quantifies agent behavior improvement
- Identifies gaps in guidance

## Testing & Validation Strategy

### Phase 1: Manual Validation (Now)
- Update story1.md with principles from interview outcomes
- Present to fresh agent session
- Observe: Does agent behave as expected?
- Document: Where does agent struggle or make wrong choices?
- Iterate: Refine Story Type Rules and guidance

### Phase 2: Real Story Testing (Near-Term)
- Use story generator to create 3-5 new stories
- Execute stories with agents following updated process
- Measure: User time investment, agent behavior quality, cycle efficiency
- Adjust: Templates, rules, directives as needed

### Phase 3: Process Refinement (Medium-Term)
- Develop remaining Story Type Rules based on experience
- Build directives library with proven patterns
- Identify common failure modes and address systematically
- Document patterns and anti-patterns

### Phase 4: Tool Validation (Long-Term)
- Automated testing of agent behavior
- Metrics collection on process efficiency
- User feedback and iteration
- Process stabilization for broader use

## Success Metrics

### User Experience Metrics
- **Story writing time:** <15 minutes for Exploring phase (measured)
- **Review time:** <10 minutes for small cycles (measured)
- **User satisfaction:** "This saved time" vs. "This created overhead" (survey)

### Agent Behavior Metrics
- **Pragmatic decisions:** >90% in high-autonomy phases (observation)
- **Appropriate questions:** Only when learning objective unclear (count)
- **Production thinking:** Rare in Exploring phase (code review)
- **Completeness:** Appropriate for phase (code review)

### Process Effectiveness Metrics
- **Information per cycle:** Decisions enabled by experiments (count)
- **Cycle efficiency:** Value created vs. overhead invested (qualitative)
- **Knowledge preservation:** Design rationale captured (count)

### Code Quality Metrics (Phase-Appropriate)
- **Exploring:** Does code answer the question?
- **Settling:** Does code work for intended use cases?
- **Fortifying:** Does code meet production standards?

## Open Questions for Iteration

These questions will be answered through practical application:

1. **Task Granularity:** What's the right level of task breakdown? Should story1's 3 tasks be 1 task "evaluate libraries"?

2. **Directive Scope:** Should directives be at story level, task level, or both? Can tasks override story directive?

3. **Template Variations:** Does each story type need its own template, or one template with conditional sections?

4. **Evaluation Criteria:** Are there any story types where objective evaluation criteria ARE appropriate?

5. **Workflow Variations:** Do different story types need different workflows, or is the standard workflow sufficient?

6. **Pattern Libraries:** At what point do pattern libraries (validation patterns, etc.) become helpful vs. overhead?

7. **Sharing Directives:** Should users be able to share directive libraries across projects or with community?

## Migration Path for Existing Work

For the ctrack project currently using process:

### Immediate
1. Update story1.md with:
   - Status field (set to "doing")
   - Reference to Study Story Rules
   - Note about autonomy level (high)
   - Keep existing directive

2. Don't move task/story files to directories
   - Add status fields to task sketches
   - Keep in current locations

### When Ready
3. Test updated story1.md with fresh agent
   - Observe behavior changes
   - Document what works better
   - Note remaining issues

4. Use story generator for next story
   - Compare time investment
   - Evaluate output quality
   - Refine tool based on experience

### Future
5. Migrate to process DB when built
   - Import existing stories/tasks
   - Continue using git workflow
   - Add voice transcription when available

## Summary

The interview revealed that the guardrails process must walk a careful line:

**Too vague:** Agents pursue wrong goals, add unnecessary completeness, waste time
**Too detailed:** User overhead kills productivity advantage

**The solution is a layered approach:**

1. **Story Type Rules** shape agent mindset for the phase
2. **Autonomy Spectrum** clarifies when to decide vs. ask
3. **Directives** provide specific focus without over-specifying
4. **Minimal Specification** trusts agent judgment within constraints
5. **Lightweight Workflow** minimizes bookkeeping overhead
6. **Subjective Evaluation** preserves human judgment where it matters

These principles work together to guide agents toward appropriate investment levels without the overhead that would make the process impractical for small cycles.

**Next concrete step:** Update the process definition document with Priority 1 actions, then build the story generator tool.

---

## Reference Documents

Detailed analysis and rationale for each outcome:

1. `interview_outcome_1_story_type_rules.md` - Study Story Rules and pattern for other types
2. `interview_outcome_2_autonomy_spectrum.md` - Phase-based detail level guidance
3. `interview_outcome_3_minimal_specification_principle.md` - Overhead constraint and iteration strategy
4. `interview_outcome_4_subjective_evaluation.md` - Design intuition and rationale capture
5. `interview_outcome_5_lightweight_workflow.md` - Git-native + status field approach
6. `interview_outcome_6_directives_library.md` - Reusable focus patterns

**Interview source:** `story1_feedback_interview_plan.md`
