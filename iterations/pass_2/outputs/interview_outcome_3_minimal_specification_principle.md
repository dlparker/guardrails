# Interview Outcome 3: Minimal Specification Principle

## Context

When discussing validation criteria, the question arose whether the autonomy spectrum fully addresses vague instructions like "do some kind of basic validation," or whether a pattern library is needed. This led to articulating a critical design constraint for the guardrails process.

## Core Principle: Process Overhead Must Not Exceed Work Value

**The guardrails process must keep user investment (writing stories, reviewing results) proportional to cycle size.**

If small exploratory cycles require:
- 30 minutes to write detailed story specification
- 20 minutes for agent to execute
- 15 minutes to review and decide

Then the 45-minute overhead dominates the 20-minute value creation. At that point, the user should just code it themselves.

## Design Goal: Minimum Viable Story Specification

**For Exploring/Pioneering phases especially, stories should be as minimal as possible while still:**
1. Focusing the agent on the actual problem to solve
2. Preventing scope creep toward completeness/production thinking
3. Providing enough context to start

**They should NOT require:**
- Exhaustive detail that's discoverable from code/docs
- Specification of every implementation choice
- Production-level requirements (error handling, edge cases, etc.)
- Pattern libraries or reference documentation for common tasks

## The Tension Being Resolved

There's a fundamental tension:
- **Too vague**: Agent pursues wrong goals, adds unnecessary completeness, wastes time
- **Too detailed**: User spends too much time writing/reviewing, loses productivity advantage

**The guardrails process attempts to resolve this through:**
1. **Story Type Rules**: Focus agent attention on appropriate goals for phase
2. **Autonomy Spectrum**: Give agent permission to figure out details pragmatically
3. **Minimal Specification**: Trust agent to make reasonable choices within constraints

## Validation Criteria as Boundary Condition

Story1.md deliberately uses vague instruction:
> "Do some kind of basic validation of successful load by printing the output of one of the src/ctrack/data_service.py query operations."

**This is a test case for the minimal specification principle:**
- ✓ Points agent to validation need
- ✓ Suggests general approach (query operations)
- ✓ Suggests output method (printing)
- ✗ Doesn't specify which query
- ✗ Doesn't specify exact output format
- ✗ Doesn't specify success criteria

**Expected agent behavior with Story Type Rules + Autonomy Spectrum:**
- Agent reads story, understands it's an Exploring/Study context
- Sees "some kind of validation" as permission to choose pragmatically
- Reviews available DataService query methods
- Picks reasonable option (accounts_count, get_accounts, etc.)
- Displays output in simple format
- Moves on without asking for more detail

**If this doesn't work in practice, we iterate on:**
- Story Type Rules wording
- Autonomy Spectrum guidance
- Role definitions

**We avoid:**
- Adding "validation pattern library" (increases overhead)
- Making stories more prescriptive (increases overhead)
- Creating more templates/checklists (increases overhead)

## Iteration Strategy

Since this is a boundary condition, we should:

1. **Test with minimal specification first**
   - Use Story Type Rules + Autonomy Spectrum
   - See if agents handle vague validation criteria appropriately
   - Measure how often agents ask unnecessary questions

2. **Identify failure patterns**
   - When agents ask for specifics they should figure out
   - When agents make inappropriate choices (production thinking)
   - When agents get stuck on decisions

3. **Adjust guidance, not stories**
   - Refine Story Type Rules to better focus attention
   - Clarify Autonomy Spectrum expectations
   - Improve Role Definitions to reduce questioning

4. **Only add story specification if guidance fails**
   - If agents consistently can't handle validation pragmatically
   - Then consider minimal pattern hints
   - But prefer "see validation patterns doc" over inline specification

## Metrics for Success

**User Time Investment:**
- Writing Exploring-phase story: ~10-15 minutes (not 30+)
- Reviewing agent results: ~5-10 minutes (not 15+)
- Total overhead: <30 minutes for small cycles

**Agent Behavior:**
- Makes pragmatic choices without asking (for high-autonomy phases)
- Stays focused on learning objectives, not production concerns
- Unblocks itself (database resets, run commands, validation choices)

**Cycle Effectiveness:**
- Information revealed per time invested
- Decisions made per cycle
- User feeling "this saved time" not "this created overhead"

## Implications for Guardrails Development

### 1. Default to Less, Add More Only When Proven Necessary

When designing templates, rules, or guidance:
- Start minimal
- Test with real stories/tasks
- Add specificity only where agents consistently fail
- Measure user overhead at each addition

### 2. Guidance Over Specification

Prefer improving:
- Story Type Rules (general principles)
- Autonomy Spectrum (when to decide vs. ask)
- Role Definitions (expected behaviors)

Over adding:
- Story template fields
- Required specification sections
- Pattern libraries
- Checklists

### 3. Optimize for Small Cycles

The process must excel at small, fast exploratory cycles because:
- These are most common in early development
- These provide highest information value
- These are where LLM assistance has most leverage
- Poor overhead ratio kills adoption

If the process only works well for large stories, it's failed.

### 4. User Investment Should Match Phase Importance

- **Exploring**: Minimal story writing, fast cycles, disposable output
- **Pioneering**: Light story writing, establish patterns
- **Settling**: Moderate story writing, working features
- **Fortifying**: Detailed story writing, production quality
- **Re-Founding**: Context-dependent

The process should make early phases very low-overhead.

## Open Questions to Resolve Through Testing

1. **Can Story Type Rules + Autonomy Spectrum eliminate most "how should I validate?" questions?**
   - Test: Present story1.md with rules to fresh agent
   - Measure: Does agent pick reasonable validation without asking?

2. **What percentage of pragmatic decisions should agents make vs. ask about?**
   - Exploring phase: >90% decisions, <10% questions?
   - Fortifying phase: >90% questions, <10% decisions?

3. **When is a pattern library genuinely helpful vs. adding overhead?**
   - Maybe useful for Settling+ phases where consistency matters
   - Probably harmful for Exploring phase where flexibility is key

4. **How do we measure "user time investment" in practice?**
   - Track story writing time
   - Track review time
   - Correlate with user satisfaction/adoption

5. **What's the right level of granularity for tasks?**
   - Story1 has 3 tasks for 3 library options
   - Is this right, or should it be 1 task "evaluate libraries"?
   - Does task granularity affect overhead?

## Validation Criteria Decision (For Now)

**Decision: Rely on autonomy spectrum and Story Type Rules**

Do NOT add:
- Pattern libraries for validation
- Specific validation requirements in stories
- Required validation sections in templates

DO test:
- Whether Story Type Rules prevent over-engineering validation
- Whether agents handle "some kind of validation" appropriately
- Where agents ask unnecessary questions

Revisit if testing shows consistent problems with validation choices.

## Summary

The minimal specification principle is critical to making the guardrails process viable for small cycles. The tension between "too vague" and "too detailed" is real and must be resolved through:

1. **Strong conceptual guidance** (Story Type Rules, Autonomy Spectrum) that shapes agent thinking
2. **Minimal story specification** that trusts agent judgment within constraints
3. **Iterative refinement** based on actual agent behavior, not theoretical completeness
4. **Measuring overhead** and optimizing for small-cycle efficiency

Validation criteria in story1.md is a deliberate test case: Can we be this vague and still get good results? The answer will inform how detailed stories need to be across other dimensions.
