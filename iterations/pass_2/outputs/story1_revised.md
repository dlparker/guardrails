# Guardrails Development Process

## Development Process Theory

This process is focused on two things: iteration style and design analysis through experiment.

Robert Pirsig's Metaphysics of Quality (MOQ) describes evolution as a rhythmic alternation between Dynamic Quality (DQ), the unpredictable force of innovation that disrupts and creates new possibilities, and Static Quality (SQ), the latching mechanism that preserves valuable patterns once proven.

This process seeks to emulate this, as it tracks well with the author's experience in producing quality software at relatively high speed.

- DQ Phase: Invest minimally in a small, experimental change to probe the problem or solution space.
- SQ Phase: Immediately test, evaluate, and either latch (retain) the change if it adds value or discard it without cost.

So, these principles should guide the work:

1. Recognize the core of the needed change, and strictly limit the work to that core.
2. At all times, avoid premature insertion of the code features associated with production quality; wait for those to be an explicit goal.
3. When latching in progress, ensure that only the confirmed value is locked down; preserve flexibility for more innovation.

## Process Taxonomies

### Phase Definitions

Each process step, typically a story and its component tasks, will be designated to be part of a "phase", which declares the work to have a completion goal that is a specific level of maturity, such as prototype, alpha quality, production, etc. Any process actor should regulate the level and type of efforts applied to that goal accordingly. Agentic Assistants should be particularly careful not to introduce elements that properly belong to later phases, so as to avoid premature investment in a potentially ephemeral work product.

Note that phase assignment is not usually at the whole project level. There are often sets of components, features, or functionalities that are at different phase levels at the same time.

| **Phase**        | **Typical Story Types**              | **Goal**                                                          |
|------------------|--------------------------------------|-------------------------------------------------------------------|
| **Exploring**    | Study, POC                           | Selection of solution approaches for key features                 |
| **Pioneering**   | Framing, Glueing                     | Only enough code and test to validate the solution approach       |
| **Settling**     | Anchoring, Joining, User             | Enough working code to support development of other features      |
| **Fortifying**   | Compliance, Joining, Anchoring       | Preparing feature for releasable status                           |
| **Re-Founding**  | Compliance, Joining, Anchoring, User | Adding or changing support for new features                       |

### Story Definitions

Stories will be created and maintained in written form and will service as the primary increment of process progress. Almost all stories will be implemented as a series of tasks, unless the story reduces simply to a single task. Proof of Concept stories might be like that.

This list is mostly complete; any additional story type should probably be added to the process definition, not just for the target project.

| **Story Type**  | **Focus**                                                                     |
|-----------------|-------------------------------------------------------------------------------|
| **Study**       | Answering questions about problem space and possible solution options         |
| **POC**         | Enough code to demo key solutions, very short term                            |
| **Framing**     | Establish early component boundaries, mostly short term                       |
| **Glueing**     | Scaffolding integration to support early components                           |
| **Anchoring**   | Improving components to solidify APIs and primary logic to production level   |
| **Joining**     | Improving integrations                                                        |
| **User**        | User interactions                                                             |
| **Compliance**  | Meeting standards for code coverage, documentation, UI style guide            |

### Task Definitions

This list is probably not complete; a given project may need additional types specific to that project.

| **Task Type**     | **Story Type**               | **Description**                                                                          |
|-------------------|------------------------------|------------------------------------------------------------------------------------------|
| **Spike Code**    | Study                        | Code to test ideas about detailed nature of problem or possible solution                 |
| **Spike Report**  | Study                        | Research notes about detailed nature of problem or possible solution                     |
| **POC**           | POC                          | Simple functions and classes allowing temporary tests or demo development                |
| **Component**     | All except Study and POC     | Encapsulating a piece of the solution in a function or class                             |
| **Scaffold**      | POC, Framing, Glueing        | Code to tie components together for preliminary tests and demos                          |
| **Demo Test**     | POC, Framing, Glueing        | Test code designed to aid evaluation and debug of incomplete features                    |
| **Test**          | Anchoring, Joining, Compliance | Test code intended for long term retention, follow "no mocking" rule                   |
| **Covert Test**   | Anchoring, Joining, Compliance | Test code targeted at coverage gaps, follow "mostly no mocking" rule                   |

### Role Definitions

This list is probably not yet complete. Needed additions that emerge might be either process wide or project specific. As this process is developed, it is likely that specific rules and other guidance will be created to instruct agents as to expectations for specific roles. There may be project specific guidance for this too, such as specifying tools or formats for Task definitions or Reports.

| **Role Name**    | **Description**                                                                                      |
|------------------|------------------------------------------------------------------------------------------------------|
| **Clerk**        | Interacts with user to sequence through defined process management steps, calling on other roles     |
| **Analyst**      | Thinks about elements required to complete story, studies code and docs, suggests Task breakdown     |
| **Coder**        | Performs code creation and modification as Task directs                                              |
| **Test Designer**| Analyzes target code (specified in Story or Task) and develops Tasks to build tests (see Test Rules) |
| **Reporter**     | Tracks repo changes, builds Task and Story reports capturing any extra user input and feedback       |

### Autonomy Spectrum

The guardrails process operates on a spectrum from high agent autonomy (in early phases) to high specification detail (in later phases):

```
Exploring → Pioneering → Settling → Fortifying → Re-Founding
   ↑                                                    ↑
High Autonomy                                  High Specification
(figure it out)                                (follow exact specs)
```

This spectrum guides:
- **How much detail stories should provide:** Early phases trust agent discovery; later phases provide explicit specifications
- **When agents should make pragmatic decisions vs. ask questions:** High autonomy = figure it out; high specification = ask when unclear
- **What level of completeness/polish is expected:** Varies by phase (minimal → production quality)
- **How precisely validation criteria must be specified:** Vague is acceptable early; explicit required later

**Phase-Specific Guidance:**

**Exploring/Pioneering (High Autonomy):**
- Agent discovers run commands from project context
- Agent chooses reasonable validation approaches
- Agent resolves obstacles pragmatically
- Agent makes implementation decisions without asking
- Only ask if the learning objective itself is unclear

**Settling (Medium Autonomy):**
- Stories indicate preferred patterns
- Agent has flexibility on implementation details
- Ask about architectural choices affecting other features

**Fortifying (High Specification):**
- Stories provide exact requirements
- Agent follows specifications precisely
- Ask about any ambiguity affecting production behavior

See Story Type Rules for phase-specific behavioral guidance.

### Directives

Directives are reusable focus patterns that specify how agents should approach work. They are more specific than roles but more general than task details.

**Examples:**
- "ensure API methods have type annotations and doc strings"
- "build minimal spike ensuring resource supplies needed info"
- "produce example code for user evaluation of specific solution options"
- "identify existing code related to Story goals"

**Purpose:**
Directives shape agent attention and behavior within the constraints of the story type and phase. They provide specific focus without over-specifying implementation details.

**Directives work in combination with:**
- **Story Type Rules:** Phase-level mindset (what to focus on, what to ignore)
- **Autonomy Spectrum:** Detail level expectations (figure out vs. follow specs)
- **Task-specific instructions:** Concrete what-to-do for individual tasks

**Building a Directives Library:**
Users develop a personal library of directives over time:
- Reuse common focus patterns across stories
- Reduce overhead by selecting from library instead of writing from scratch
- Evolve patterns based on what works in practice

## Story Type Rules

### Study Story Rules

**Autonomy Level: HIGH** - You are expected to figure out implementation details, run commands, validation approaches, and obstacle resolution pragmatically.

**1. Information over Implementation**
The goal is learning, not production code. Write the minimum code necessary to answer the question or reveal information about the problem/solution space.

**2. Vague is Permissive**
Phrases like "probably need to," "some kind of," "might require" are **permissions to handle pragmatically**, not gaps requiring clarification. A journeyman programmer would figure it out - you should too. Don't ask for more specifics unless the learning objective itself is unclear.

Examples:
- "Probably need to remove the database" → Just delete it if you hit issues
- "Some kind of validation" → Pick any reasonable validation approach
- "Might require reset" → Reset if you think it's needed

**3. No Production Thinking**
Unless explicitly stated, ignore these concerns:
- Error handling
- UI polish and styling
- Edge cases
- Performance optimization
- Logging and monitoring
- Comprehensive documentation
- Code reusability
- Test coverage

These belong in later phases (Settling, Fortifying). In Study stories, these are premature investments in potentially throwaway work.

**4. Unblock Yourself**
If you encounter obstacles, resolve them the simplest way possible:
- Database state issues? Delete the database file
- Missing file? Hard-code a path to a test file
- Dependency conflict? Install/update as needed
- API unclear? Try the most obvious approach first

Don't wait for permission or detailed instructions. The cost of fixing a wrong guess is near zero in spike code.

**5. Measure Success by Learning**
Did we answer the question? Did we reveal new information?

NOT:
- Is this code maintainable?
- Is this code testable?
- Is this code complete?
- Would this pass code review?

If the spike code successfully demonstrates the concept or answers the study question, it's successful - even if it's ugly, hard-coded, or incomplete.

**6. Throw-away Mindset**
Assume this code will be discarded or heavily modified. Don't invest in its longevity. Use:
- Hard-coded values instead of configuration
- Print statements instead of logging
- Simple functions instead of classes
- Inline code instead of abstractions

Later phases will make things production-ready. Your job is to learn fast and cheap.

### [Other Story Type Rules - To Be Defined]

Rules for POC, Framing, Glueing, Anchoring, Joining, User, and Compliance story types will be developed through iteration on actual stories.

## Test Rules

1. **No Mocking test rule**
   1. Tests don't just test code, they test intention behind the code
   2. Should use test data and simulated operation flow to setup test conditions, not mocks
   3. Hard to test code should be considered possible target for redesign
   4. No use of mocks unless to capture external services
2. **Mostly No Mocking test rule**
   1. Typically applied to last few percent of missing coverage
   2. Typically only applies to error handling code
   3. Using mocking allowed but only if the cost of applying the No Mocking rule is too high

## Story Type Standard Workflow

Stories always involve actions in the "clerk" and "reporter" role, plus one or more roles as needed per task.

1. **Clerk:** Update story status: `todo` → `doing`, commit change
2. **Analyst:** Create task files in `process_docs/tasks/` (with status: `doing`)
3. **For each task:**
   1. **Coder:** Build minimal spike, commit with message "Spike: [task name]"
   2. **Reporter:** Present results to user for evaluation
   3. **User decides disposition:** save / retire / discard
   4. **Execute git workflow:**
      - **Save:** Keep code (current state)
      - **Retire:** `git tag retired/[descriptive-name] && git reset --hard HEAD~1`
      - **Discard:** `git reset --hard HEAD~1`
   5. **Clerk:** Update task status: `doing` → `done/retired/discarded`, commit change
4. **Reporter:** Generate summary report (optional for small cycles)
5. **Clerk:** Update story status based on user disposition, commit change

### Git Workflow for Experiments

**Saving experiment results:**
- Code remains in working tree
- Task status → `done`

**Retiring experiment results:**
- Tag: `git tag retired/[descriptive-name]`
- Reset: `git reset --hard HEAD~1`
- Task status → `retired`
- Preserved for future reference: `git show retired/[descriptive-name]`
- List retired experiments: `git tag -l 'retired/*'`

**Discarding experiment results:**
- Reset: `git reset --hard HEAD~1`
- Task status → `discarded`
- Removed from working tree, no tag (effectively forgotten)

**Rationale:**
- Git reset physically removes code from working tree (prevents context pollution)
- Tags preserve retired experiments for future reference
- No file movement overhead, git handles bookkeeping

### Subjective Evaluation (Study Stories)

For Study stories, evaluation is **not a checklist comparison**. It's a subjective assessment based on experience-based software design intuition.

**User's evaluation process:**
1. Look at the resulting code
2. Imagine where it might be going
3. Use design intuition to sense direction
4. Decide: shape it toward preferred direction, or cut it off and try something else

**Reporter's role is to facilitate, not evaluate:**
- Present each experiment's code clearly
- Highlight key differences between approaches
- Show what was learned or discovered
- Ask open questions: "What did you observe?" "Which approach feels right?"

**Reporter should NOT:**
- Score options against criteria
- Recommend which option is "best"
- Try to make the evaluation objective

The user's subjective judgment, based on design intuition and experience, is essential and cannot be delegated.

---

# Story-Specific Content

## Common Story Fields

| **Field**          | **Value**                                                                     |
|--------------------|-------------------------------------------------------------------------------|
| **Story ID**       | 1                                                                             |
| **Story Name**     | GnuCash file picker experiment                                                |
| **Status**         | todo                                                                          |
| **Phase**          | exploring                                                                     |
| **Story Type**     | study                                                                         |
| **Directive**      | produce example code for user evaluation of specific solution options         |

## Story Goal

Review UI methods of identifying and loading GnuCash file in the Textual interface.

## Context

The application flow defined in `src/ctrack/flow.py` requires selecting a GnuCash file as the first step. Review `tests/test_flow.py` to understand the relevance of selecting and loading the GnuCash file.

Extend the Textual UI stub found in `scripts/tx_main.py` and `src/ctrack/textual/tx_main.py` to experiment with GnuCash file selection methods.

The underlying DataService mechanism only supports a single GnuCash target file. Trying to load a new one will require re-initializing the database (probably by removing `{data_dir}/ctrack.db` and letting it recreate).

## Options to Try

Experiment with these three file picker approaches:

1. **DirectoryTree** - Built-in Textual widget (doesn't do file picker directly, but should be good base for implementing one)
2. **textual-fspicker** - Third-party library already in dependencies
3. **textual-filedrop** - Third-party library already in dependencies

## Task Sketches

### Task 1.1: DirectoryTree picker

| **Field**           | **Value**                      |
|---------------------|--------------------------------|
| **Parent Story**    | 1 - GnuCash file picker experiment |
| **Task ID**         | 1.1                            |
| **Task Name**       | try DirectoryTree picker       |
| **Task Type**       | spike code                     |

Implement file picker using DirectoryTree. Target the example GnuCash file in `demo_work/` (after running `uv run scripts/prep_work.py`). Validate successful load using DataService query operations.

### Task 1.2: textual-fspicker

| **Field**           | **Value**                      |
|---------------------|--------------------------------|
| **Parent Story**    | 1 - GnuCash file picker experiment |
| **Task ID**         | 1.2                            |
| **Task Name**       | try textual-fspicker           |
| **Task Type**       | spike code                     |

Implement file picker using textual-fspicker library. Target the example GnuCash file in `demo_work/`. Validate successful load using DataService query operations.

### Task 1.3: textual-filedrop

| **Field**           | **Value**                      |
|---------------------|--------------------------------|
| **Parent Story**    | 1 - GnuCash file picker experiment |
| **Task ID**         | 1.3                            |
| **Task Name**       | try textual-filedrop           |
| **Task Type**       | spike code                     |

Implement file picker using textual-filedrop library. Target the example GnuCash file in `demo_work/`. Validate successful load using DataService query operations.

---

## Evaluation Notes

(To be filled in after experiments complete - user's subjective evaluation and rationale)
