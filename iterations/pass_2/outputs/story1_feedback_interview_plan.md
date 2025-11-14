# Story Definition Feedback - Interview Plan

## Purpose

This document serves as a structured interview plan to discuss feedback on story1.md and develop an action plan for improving the story generation process. The goal is to clarify which aspects of the feedback should be addressed in story templates, which in task templates, and which as general process guidance.

## Analysis Summary

### Overall Assessment: 70% Ready

The story definition (story1.md) provides solid technical context and clear intent, but lacks operational clarity in several critical areas. An experienced agent could build working demonstrations, but would likely need to make assumptions about scope, database management, and success criteria that might not align with intentions.

### What Works Well ✓

1. **Process Framework Context** - Excellent coverage of guardrails philosophy (DQ/SQ, phases, story types), clear taxonomy definitions, well-documented standard workflow steps, and helpful role definitions.

2. **Technical Direction** - Three specific options identified, relevant code files correctly referenced, connection to MainFlow workflow explained, and test file location specified.

3. **Story Structure** - Clear story goal and phase assignment, task sketches provide helpful examples of task definition style, parent-child relationship structure is clear.

### Core Problem Pattern

The story falls into the "planning trap" - assuming the executor knows operational details that seem obvious to the author but aren't explicitly stated. This manifests in three categories:

1. **Critical Gaps** - Missing information that would block execution (database reset, run commands, validation specs)
2. **Significant Ambiguities** - Unclear expectations about scope and approach (experiment isolation, UI integration depth, evaluation criteria)
3. **Minor Issues** - Small inconsistencies that wouldn't block but would help (task numbering, documentation references)

### Confidence Assessment by Role

- **Clerk Role**: 65% - Would struggle with git hash capture timing and database reset
- **Analyst Role**: 80% - Could infer task breakdown but might miss database constraints
- **Coder Role**: 60% - Could build demos but would make assumptions about scope/isolation
- **Reporter Role**: 70% - Could present results but unclear on evaluation dimensions

### What Agent WOULD Understand vs. MIGHT Struggle With

**Would Understand:**
- The guardrails process philosophy and workflow
- Where to make changes (tx_main.py)
- Which libraries to experiment with
- How to validate technically (MainFlow.get_data_needs)
- Test file location (demo_work/test.gnucash)
- Task definition structure from sketches

**Might Struggle With:**
- How to reset database between experiments
- Exact command to run the application
- What validation output to display
- Whether to isolate or integrate experiments
- Level of polish expected for spike code
- What criteria user will evaluate on

## Interview Checklist

### Section 1: Critical Operational Gaps

These items represent missing information that would likely block an agent from executing the story autonomously.

- [ ] **1.1 Database Reset Mechanism**
  - Discuss: Should stories always include explicit database/state reset instructions?
  - Discuss: Is this a story-level concern or should it be in task definitions?
  - Discuss: Should there be a standard pattern/template for "stateful experiment" stories?
  - Decide: Add to story template, task template, or both?

- [ ] **1.2 Application Run Commands**
  - Discuss: Should every story include the exact CLI command to run/test?
  - Discuss: Is this redundant with general project documentation (README, CLAUDE.md)?
  - Discuss: For spike stories specifically, should run commands always be included?
  - Decide: Add to story template, reference external docs, or make context-dependent?

- [ ] **1.3 Validation Success Criteria**
  - Discuss: How specific should validation requirements be in stories vs. tasks?
  - Discuss: Should there be a standard "validation display format" template?
  - Discuss: Is "do some kind of validation" ever acceptable, or should it always be explicit?
  - Decide: Create validation specification template or leave to task definitions?

### Section 2: Scope and Approach Ambiguities

These items represent areas where the story's intent is unclear, leading to potentially divergent implementations.

- [ ] **2.1 Experiment Isolation Strategy**
  - Discuss: Should spike stories specify whether experiments are sequential or parallel?
  - Discuss: Should story define git workflow (commit per task, stash, branches)?
  - Discuss: Is experiment isolation a story concern or a general process rule?
  - Decide: Add to story template, create separate workflow guidance, or both?

- [ ] **2.2 Implementation Scope and Polish Expectations**
  - Discuss: How to communicate "spike code" expectations clearly to agents?
  - Discuss: Should stories specify what NOT to do (no error handling, no styling, etc.)?
  - Discuss: Does the phase (Exploring) already communicate this, or is it too subtle?
  - Decide: Add explicit "out of scope" section to story template?

- [ ] **2.3 Task-Specific Technical Ambiguities**
  - Discuss: How much technical detail should be in story vs. delegated to Coder role?
  - Discuss: Example: "use DirectoryTree" - should story specify "build custom picker" vs. "use as-is"?
  - Discuss: Is this a task definition issue rather than story issue?
  - Decide: Where does story guidance end and task/role autonomy begin?

- [ ] **2.4 User Evaluation Criteria**
  - Discuss: Should stories always specify what user will evaluate on?
  - Discuss: For Study stories specifically, is evaluation rubric required?
  - Discuss: Should this be in story or in Reporter role guidance?
  - Decide: Add evaluation criteria template for Study stories?

### Section 3: Story/Task Boundary Questions

These items relate to what belongs in story definitions vs. task definitions vs. process guidance.

- [ ] **3.1 Task Sketch Completeness**
  - Discuss: How complete should task sketches be in the story?
  - Discuss: Should Analyst role expand task sketches, or are they just examples?
  - Discuss: What's the minimum viable task sketch?
  - Decide: Create task sketch template with required/optional fields?

- [ ] **3.2 Story Metadata and Workflow Integration**
  - Discuss: Review git hash capture workflow - is it clear when to do this?
  - Discuss: Should stories reference the standard workflow steps or assume they're known?
  - Discuss: Are there story-specific workflow variations that need to be stated?
  - Decide: Create workflow reference checklist for story writers?

- [ ] **3.3 Code Context References**
  - Discuss: How much code context should stories provide vs. expecting agent exploration?
  - Discuss: Example: "review tests/test_flow.py" - should story summarize or just reference?
  - Discuss: Should stories list available query methods or let agent discover?
  - Decide: Define when to be explicit vs. when to reference?

### Section 4: Story Generation Process Improvements

These items relate to tooling and templates to prevent recurring issues.

- [ ] **4.1 Story Template Design**
  - Discuss: What sections should every story have?
  - Discuss: Which sections vary by story type (Study, POC, Framing, etc.)?
  - Discuss: How to balance completeness vs. avoiding boilerplate?
  - Decide: Create story template(s) with required and optional sections?

- [ ] **4.2 Story Validation Checklist**
  - Discuss: What checklist should story writers use before marking story ready?
  - Discuss: Should there be different checklists for different story types?
  - Discuss: How to validate a story is "agent-executable in fresh context"?
  - Decide: Create story validation checklist for human story authors?

- [ ] **4.3 Task Definition Standards**
  - Discuss: What makes a complete task definition?
  - Discuss: Review task sketch examples in story1 - which elements are essential?
  - Discuss: How much autonomy should Coder role have vs. following explicit instructions?
  - Decide: Create task definition template with required fields?

- [ ] **4.4 Role Guidance Enhancement**
  - Discuss: Do role definitions need more specific guidance about autonomy vs. following specs?
  - Discuss: Should there be role-specific checklists (e.g., "Clerk: always capture git hash")?
  - Discuss: How do roles interact - when does Analyst hand off to Coder?
  - Decide: Enhance role definitions with behavioral expectations?

### Section 5: Documentation and Reference Materials

These items relate to supporting documentation that stories can reference.

- [ ] **5.1 Project-Specific vs. Story-Specific Information**
  - Discuss: What belongs in CLAUDE.md vs. what should be repeated in stories?
  - Discuss: Can stories reference CLAUDE.md for run commands, or should they duplicate?
  - Discuss: How to handle information that changes (file paths, commands)?
  - Decide: Create story writing guidelines about what to reference vs. duplicate?

- [ ] **5.2 Process Documentation Organization**
  - Discuss: Should there be a "Story Writer's Guide" separate from the process definition?
  - Discuss: Should examples of good/bad stories be maintained?
  - Discuss: How to capture lessons learned from story executions?
  - Decide: Plan documentation structure for mature guardrails process?

- [ ] **5.3 Story Templates by Type**
  - Discuss: Should each story type (Study, POC, Framing, etc.) have its own template?
  - Discuss: What's common across all types vs. type-specific?
  - Discuss: How to avoid template proliferation while maintaining clarity?
  - Decide: Design template strategy (single template with variants vs. multiple templates)?

## Post-Interview Action Plan

After completing the interview, this section will be populated with:

1. **Immediate Actions** - Changes to make to story1.md specifically
2. **Story Template Changes** - What to add/modify in story templates
3. **Task Template Development** - Required fields and structure for task definitions
4. **Process Documentation Updates** - Clarifications needed in process definition
5. **Role Guidance Enhancements** - Additional instructions for Clerk, Analyst, Coder, Reporter roles
6. **Validation Checklists** - Checklists for story writers to use before marking stories ready
7. **Examples and Patterns** - Pattern library to develop (database reset, validation display, etc.)
8. **Open Questions** - Items that need more experimentation before deciding

## Notes Section

(Space for capturing additional thoughts and context during the interview)
