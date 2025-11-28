# Applying Metaphysics of Quality to Agentic Coding: The Guardrails Framework

## Chapter 2: The Guardrails Process Specification

### Introduction to the Guardrails Process
This chapter provides a detailed specification of the Guardrails process, drawing directly from the evolving documentation in the guardrails repository (https://github.com/dlparker/guardrails). The process is designed to apply a specific development style to agentic-assisted coding, countering the default "vibe coding" mode of large language models (LLMs). In vibe coding, users request high-level results, and the LLM infers and implements comprehensive designs, often producing excessive code volume.

Guardrails shifts this paradigm toward small, constrained iterations. A primary motivation is enabling the user to deeply comprehend the agent's work product, avoiding the overwhelm of reviewing complex outputs. LLMs tend to expand scope beyond requests, introducing premature structure and features into unproven code. This leads to two key issues: (1) user exhaustion from voluminous reviews, and (2) context pollution with agent-inserted goals, necessitating resets that risk losing valuable context.

To mitigate these, Guardrails guides agents through user-created Stories—self-contained units defining desired outcomes and constraints to curb scope creep. Agents then propose Tasks as small work units, which the user approves or iterates upon before execution. This structure promotes rapid experimentation, explicit constraints, and clean context boundaries, aligning with the Metaphysics of Quality (MOQ) principles introduced in Chapter 1.

The process is currently in an "Exploring" phase of its own development, dogfooding itself on real projects like ctrack (a GnuCash transaction import tool). Artifacts such as session transcripts and inspection reports are committed to the repository for retrospective analysis and refinement.

### Development Process Theory
The Guardrails process centers on two intertwined elements: iteration style and design analysis through low-cost experimentation.

Robert Pirsig's Metaphysics of Quality (MOQ) frames evolution as a rhythmic alternation between Dynamic Quality (DQ)—the unpredictable force of innovation that disrupts and opens new possibilities—and Static Quality (SQ)—the latching mechanism that preserves proven patterns for stability.

This process emulates that rhythm, mirroring the author's experience in delivering high-quality software at speed:
- **DQ Phase**: Invest minimally in a small, experimental change to probe the problem or solution space.
- **SQ Phase**: Immediately test, evaluate, and either latch (retain) the change if it adds value or discard it at near-zero cost.

Guiding principles include:
1. Recognize the core of the needed change and strictly limit work to that core.
2. Avoid premature insertion of production-quality features (e.g., error handling, logging) unless explicitly targeted.
3. When latching progress, lock down only confirmed value, preserving flexibility for future innovation.

These principles ensure iterations remain lightweight, focused, and reversible, fostering a mental model of the solution space without premature commitment.

### Process Taxonomies
Guardrails relies on interconnected taxonomies to enforce constraints dynamically. These define phases, stories, tasks, roles, and directives, ensuring agents operate within bounded scopes tailored to the development maturity level.

#### Phase Definitions
Each process step—typically a Story and its Tasks—is assigned to a phase, declaring a maturity goal (e.g., prototype, production). Actors (especially agents) must calibrate efforts accordingly, avoiding elements from later phases to prevent investment in ephemeral work. Phases are not project-wide; components or features often progress concurrently at different levels.

| **Phase**      | **Typical Story Types** | **Goal**                                              |
|----------------|-------------------------|-------------------------------------------------------|
| **Exploring**  | Study, POC              | Selection of solution approaches for key features     |
| **Pioneering** | Framing, Glueing        | Only enough code and test to validate solution approach |
| **Settling**   | Anchoring, Joining, User| Enough working code to support development of other features |
| **Fortifying** | Compliance, Joining, Anchoring | Preparing feature for releasable status              |
| **Re-Founding**| Compliance, Joining, Anchoring, User | Adding or changing support for new features          |

#### Story Definitions
Stories are written, maintained documents serving as primary increments of progress. Most decompose into series of Tasks, though simple ones (e.g., Proof of Concept) may be single-Task. The taxonomy is mostly complete; new types should integrate into the core definition.

| **Story Type** | **Focus**                                                                 |
|----------------|---------------------------------------------------------------------------|
| **Study**      | Answering questions about problem space and possible solution options     |
| **POC**        | Enough code to demo key solutions, very short term                        |
| **Framing**    | Establish early component boundaries, mostly short term                   |
| **Glueing**    | Scaffolding integration to support early components                       |
| **Anchoring**  | Improving components to solidify APIs and primary logic to production level|
| **Joining**    | Improving integrations                                                    |
| **User**       | User interactions                                                         |
| **Compliance** | Meeting standards for code coverage, documentation, UI style guide        |

#### Task Definitions
Tasks represent granular work units. This taxonomy is extensible for project-specific needs.

| **Task Type**    | **Story Type**               | **Description**                                                                          |
|------------------|------------------------------|------------------------------------------------------------------------------------------|
| **Spike Code**   | Study                        | Code to test ideas about detailed nature of problem or possible solution                 |
| **Spike Report** | Study                        | Research notes about detailed nature of problem or possible solution                     |
| **POC**          | POC                          | Simple functions and classes allowing temporary tests or demo development                |
| **Component**    | All except Study and POC     | Encapsulating a piece of the solution in a function or class                             |
| **Scaffold**     | POC, Framing, Glueing        | Code to tie components together for preliminary tests and demos                          |
| **Demo Test**    | POC, Framing, Glueing        | Test code designed to aid evaluation and debug of incomplete features                    |
| **Test**         | Anchoring, Joining, Compliance | Test code intended for long-term retention; follow "No Mocking" rule                     |
| **Covert Test**  | Anchoring, Joining, Compliance | Test code targeted at coverage gaps; follow "Mostly No Mocking" rule                     |

#### Role Definitions
Roles guide agent behaviors; the list is evolving, with project-specific guidance possible (e.g., tools for Task reports). Future refinements may include role-specific rules.

| **Role Name**    | **Description**                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------|
| **Clerk**        | Interacts with user to sequence through defined process management steps, calling on other roles     |
| **Analyst**      | Thinks about elements required to complete story, studies code and docs, suggests Task breakdown     |
| **Coder**        | Performs code creation and modification as Task directs                                              |
| **Test Designer**| Analyzes target code (specified in Story or Task) and develops Tasks to build tests (see Test Rules) |
| **Reporter**     | Tracks repo changes, builds Task and Story reports capturing any extra user input and feedback       |

#### Directives
Directives are reusable, focused instructions refining role guidance for Stories or Tasks—more specific than roles but general enough for reuse.

Examples:
- "Build minimal spike ensuring resource supplies needed info"
- "Let user evaluate UI component selection"
- "Identify existing code related to Story goals"
- "Scope code changes for Story and breakdown into proposed Tasks for new and changed code separately"

Directives shape agent focus within phase and story constraints, building toward a personal library for efficiency.

### Test Rules
Tests in Guardrails emphasize intention and realism over isolation, aligning with low-mock philosophies to encourage redesign of hard-to-test code.

1. **No Mocking Rule**:
   - Tests validate not just code but the intention behind it.
   - Use test data and simulated flows for setup, not mocks.
   - Hard-to-test code signals a redesign opportunity.
   - Mocks permitted only for external services.

2. **Mostly No Mocking Rule**:
   - Applies to final coverage gaps (last few percent).
   - Typically for error handling.
   - Mocking allowed if "No Mocking" cost is disproportionately high.

### Story Standard Workflow
Stories engage the Clerk and Reporter roles universally, plus others as needed. The workflow ensures auditability via Git hashes, enabling precise retrospectives (e.g., `git diff {start_hash} {end_hash}`) without rollbacks.

1. **Clerk**: Capture current Git hash.
2. **Analyst**: Create task files in `process_docs/tasks/todo/` (see Task Definition Outline).
3. **For each Task**:
   - **Clerk**: Record starting Git hash in task file; move to `process_docs/tasks/doing`.
   - **Coder**: Build minimal spike (commit as "[Story ID]: [Story Name]: [Task ID]: [Task Type]: [Task Name]").
   - **Clerk**: Record ending Git hash in task file.
   - **Reporter**: Present results to user for save/discard/retire decisions:
     - **Discard**: Remove results; move task to `process_docs/tasks/discarded`.
     - **Retire**: Move results to a notes file (named from story); commit; move task to `process_docs/tasks/discarded`.
     - **Save**: Move task to `process_docs/tasks/done`.
4. **Reporter**: Generate summary report analyzing experiments and decisions.
5. **Reporter**: Collect story disposition from user (save/discard/retire).
6. **Clerk**: Move story file to `process_docs/stories/done|retired|discarded`.

Tasks are broken down *before* execution, with user approval required—iterating proposals until alignment.

### Task Definition Outline
Task breakdown analyzes the story and codebase to keep scopes small, per the workflow above. Stories precede Task execution; user approval (or revision cycles) is mandatory.

**Available Resources**:
- Full access to project files and documentation.
- Agent explores codebase for details.
- CLAUDE.md (or equivalent) provides structure and commands.

**Expected Task Definition Format**:
- Brief table with metadata (e.g., Parent Story, Task ID, Name, Type).
- 1-2 sentence focus description.
- No detailed step-by-step instructions.
- No comprehensive validation criteria—deduce from Task nature or seek user feedback for revision.

**Task File Organization**:
- Individual files in `process_docs/tasks/todo/`.
- Naming: `task_1_1.md`, etc.
- Temporary file-based; future: CLI tools over database.

**Execution Model**:
- Obey process, Story, and Task guidance.
- Tasks are independent units (especially in Study Stories).
- Separate commits per Task.
- User evaluates post-execution; next Task starts fresh (revert via Git if needed).

This specification forms the operational core of Guardrails, enabling constrained, iterative agentic coding. Subsequent chapters will expand on phase-specific applications and lifecycle management.

