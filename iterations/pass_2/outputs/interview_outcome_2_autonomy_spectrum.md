# Interview Outcome 2: Autonomy Spectrum Across Phases

## Context

When discussing whether stories should include explicit run commands, the question arose: Should Study stories trust agent autonomy to figure it out, or should they provide explicit commands? This led to a broader insight about how phases map to a spectrum of autonomy vs. specification.

## Core Principle: Phase-Based Autonomy Spectrum

```
Exploring → Pioneering → Settling → Fortifying → Re-Founding
   ↑                                                    ↑
High Autonomy                                  High Specification
(figure it out)                                (follow exact specs)
```

### Rationale

**Early Phases (Exploring, Pioneering)**
- Problem/solution space is unclear
- Need flexibility to discover and adapt
- Learning and exploration are the primary goals
- Decisions are temporary and will likely change
- Speed and cheapness of cycles matter most

**Later Phases (Settling, Fortifying, Re-Founding)**
- Key decisions have been made and should be preserved
- Need consistency and precision
- Production quality and stability are the goals
- Implementation patterns should be followed
- Correctness and completeness matter most

## Application to Story Specifications

This autonomy spectrum should guide how much detail stories provide across multiple dimensions:

### 1. Run Commands and Testing

**Exploring Phase (Study stories):**
- No need to specify run commands
- Agent discovers from CLAUDE.md, project structure, scripts/
- Agent figures out how to validate results pragmatically

**Pioneering Phase (POC, Framing stories):**
- Include run commands if non-standard or multiple options exist
- Otherwise, agent autonomy is appropriate

**Settling Phase (Anchoring, Joining stories):**
- Include specific run commands if they have important flags
- Specify test commands to ensure consistency

**Fortifying Phase (Compliance stories):**
- Exact commands required
- Specific test suites, coverage requirements, CI/CD integration specified
- No ambiguity about how to validate success

### 2. Error Handling

**Exploring/Pioneering:**
- Agent decides if error handling is needed
- Usually skip unless it blocks the learning objective

**Settling:**
- Story indicates which error cases need handling
- Agent has latitude on implementation approach

**Fortifying:**
- Comprehensive error handling required
- Specific error messages, logging, recovery patterns specified

### 3. Implementation Detail

**Exploring/Pioneering:**
- Stories provide goals and constraints
- Agent chooses implementation approach
- Multiple valid solutions acceptable

**Settling:**
- Stories indicate preferred patterns or architectures
- Agent follows established conventions
- Solutions should align with existing code

**Fortifying:**
- Stories specify exact implementation requirements
- Agent follows detailed specifications
- Consistency with production code required

### 4. Asking Questions

**Exploring/Pioneering:**
- Agent should make pragmatic decisions rather than ask
- Only ask if the learning objective itself is unclear
- "Figure it out like a journeyman programmer would"

**Settling:**
- Ask about architectural choices that affect other features
- Make pragmatic decisions on implementation details

**Fortifying:**
- Ask about any ambiguity that could affect production behavior
- Verify assumptions about requirements and edge cases

### 5. Validation and Success Criteria

**Exploring/Pioneering:**
- Vague criteria ("some kind of validation") are permissive
- Agent chooses reasonable validation approach
- Success = learning objective achieved

**Settling:**
- Clear criteria but some implementation flexibility
- Success = feature works for intended use cases

**Fortifying:**
- Explicit, measurable criteria
- Success = all requirements met, all tests pass

## Implementation in Guardrails Process

### 1. Add Autonomy Spectrum to Process Definition

Add a new section in the process definition (perhaps before or after Phase Definitions):

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

### 2. Integrate into Story Type Rules

Each Story Type Rule set should reference where that story type falls on the autonomy spectrum.

**Example for Study Stories:**
```markdown
## Study Story Rules

**Autonomy Level: HIGH** - You are expected to figure out implementation details,
run commands, validation approaches, and obstacle resolution pragmatically.

[... existing 6 rules ...]
```

**Example for Compliance Stories:**
```markdown
## Compliance Story Rules

**Specification Level: HIGH** - Follow exact requirements, ask about ambiguities,
validate against explicit criteria.

[... rules to be defined ...]
```

### 3. Story Template Updates

Story templates should include a field indicating autonomy level:

```markdown
**Phase:** [exploring/pioneering/settling/fortifying/re-founding]
**Autonomy Level:** [high/medium/low] (determined by phase)
**Agent Guidance:** [See {Story Type} Rules for appropriate autonomy expectations]
```

### 4. Role Definition Updates

Role definitions should reference the autonomy spectrum to guide behavior:

**Analyst Role:**
- In high-autonomy phases: Create minimal task breakdowns, leave implementation details to Coder
- In high-specification phases: Create detailed task definitions with specific requirements

**Coder Role:**
- In high-autonomy phases: Make pragmatic implementation choices, unblock yourself
- In high-specification phases: Follow specifications precisely, ask about ambiguities

**Clerk Role:**
- In high-autonomy phases: Trust agents to handle workflow details
- In high-specification phases: Ensure precise adherence to workflow steps

## Examples of Autonomy Spectrum in Practice

### Example 1: Database Reset

**Exploring Phase (Study story):**
- Story: "Probably need to remove database and re-initialize"
- Agent interpretation: "I'll delete ctrack.db if I hit issues" ✓

**Fortifying Phase (Compliance story):**
- Story: "Database reset functionality must handle these cases: [list], with error messages: [list], and fallback to: [behavior]"
- Agent interpretation: "I need to implement exactly as specified" ✓

### Example 2: Run Command

**Exploring Phase (Study story):**
- Story: [no run command provided]
- Agent: Discovers from CLAUDE.md or scripts/ ✓

**Fortifying Phase (Compliance story):**
- Story: "Run with: `uv run pytest --cov=ctrack --cov-report=html --cov-fail-under=80`"
- Agent: Uses exact command ✓

### Example 3: Validation

**Exploring Phase (Study story):**
- Story: "Do some kind of basic validation of successful load"
- Agent: Picks `accounts_count() > 0` or prints first account ✓

**Fortifying Phase (Compliance story):**
- Story: "Validation must check: account count matches expected, all required fields populated, no orphaned records, foreign keys valid"
- Agent: Implements all specified checks ✓

## Benefits of This Principle

1. **Reduces Specification Burden**: Early-phase stories don't need exhaustive detail
2. **Encourages Appropriate Behavior**: Agents know when to be autonomous vs. precise
3. **Matches Human Development Patterns**: Mimics how human developers work (explore freely, then lock down)
4. **Prevents Premature Optimization**: Agents won't over-engineer early-phase work
5. **Ensures Production Quality**: Late-phase work gets necessary rigor and precision
6. **Coherent Mental Model**: Single principle guides multiple dimensions of behavior

## Next Steps for Guardrails Project

1. **Add Autonomy Spectrum section to process definition** (before or after Phase Definitions)

2. **Update Story Type Rules** to include autonomy level indicator

3. **Update Role Definitions** to reference autonomy spectrum for behavioral guidance

4. **Create Story Templates** with autonomy level field based on phase

5. **Develop Examples** showing same feature at different phases with appropriate autonomy levels

6. **Test with Agents** to validate that autonomy spectrum guidance produces expected behavior

7. **Document Mapping**: Create clear mapping from Phase → Autonomy Level → Expected Agent Behavior
   - Exploring: High autonomy - figure it out, make pragmatic choices
   - Pioneering: High autonomy - but establish patterns for later phases
   - Settling: Medium autonomy - follow established patterns, flexibility on details
   - Fortifying: Low autonomy - precise specifications, ask about ambiguities
   - Re-Founding: Context-dependent - depends on what's being changed
