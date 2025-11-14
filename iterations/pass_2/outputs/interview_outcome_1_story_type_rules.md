# Interview Outcome 1: Story Type-Specific Rules

## Context

During review of story1.md, the agent interpreted vague guidance like "probably by removing it and re-initializing the database" as a gap requiring explicit instructions, including UI handling concerns. This revealed a fundamental misunderstanding: the agent was applying production/completeness thinking to an "exploring" phase "study" story where the goal is fast, cheap learning cycles.

## Core Insight

The "exploring" phase and "study" story type are **intentional stances against LLM inclination toward completeness**. Phrases like "probably need to," "some kind of," "might require" should be interpreted as **permissions to handle pragmatically**, not gaps requiring clarification. A journeyman human programmer would interpret these as "figure it out however needed to complete the learning objective."

## Solution: Story Type-Specific Rules

Following the pattern of "Test Rules" in the process definition, create rule sets for each story type that define the appropriate mindset, level of investment, and focus.

---

## Study Story Rules

### 1. Information over Implementation
**The goal is learning, not production code.** Write the minimum code necessary to answer the question or reveal information about the problem/solution space. If you can answer with 20 lines instead of 200, do that.

### 2. Vague is Permissive
**Phrases like "probably need to," "some kind of," "might require" are permissions to handle pragmatically**, not gaps requiring clarification.

Examples:
- "Probably need to remove the database" → Just delete it if you hit issues
- "Some kind of validation" → Pick any reasonable validation approach
- "Might require reset" → Reset if you think it's needed

A journeyman programmer would figure it out - you should too. Don't ask for more specifics unless the question itself is unclear.

### 3. No Production Thinking
**Unless explicitly stated, ignore these concerns:**
- Error handling
- UI polish and styling
- Edge cases
- Performance optimization
- Logging and monitoring
- Comprehensive documentation
- Code reusability
- Test coverage

These belong in later phases (Settling, Fortifying). In Study stories, these are **premature investments** in potentially throwaway work.

### 4. Unblock Yourself
**If you encounter obstacles, resolve them the simplest way possible:**
- Database state issues? Delete the database file
- Missing file? Hard-code a path to a test file
- Dependency conflict? Install/update as needed
- API unclear? Try the most obvious approach first

Don't wait for permission or detailed instructions. The cost of fixing a wrong guess is near zero in spike code.

### 5. Measure Success by Learning
**Did we answer the question? Did we reveal new information?**

NOT:
- Is this code maintainable?
- Is this code testable?
- Is this code complete?
- Would this pass code review?

If the spike code successfully demonstrates the concept or answers the study question, it's successful - even if it's ugly, hard-coded, or incomplete.

### 6. Throw-away Mindset
**Assume this code will be discarded or heavily modified.** Don't invest in its longevity. Use:
- Hard-coded values instead of configuration
- Print statements instead of logging
- Simple functions instead of classes
- Inline code instead of abstractions

Later phases will make things production-ready. Your job is to learn fast and cheap.

---

## Implementation in Guardrails Process

### Location
Add to process definition document after "Test Rules" section, around line 109.

### Structure
```markdown
## Story Type Rules

### Study Story Rules
[6 rules as defined above]

### POC Story Rules
[To be defined - likely similar to Study but with slightly more structure]

### Framing Story Rules
[To be defined - establishing component boundaries]

### Glueing Story Rules
[To be defined - scaffolding integration]

### Anchoring Story Rules
[To be defined - solidifying to production level]

### Joining Story Rules
[To be defined - improving integrations]

### User Story Rules
[To be defined - user interaction focus]

### Compliance Story Rules
[To be defined - meeting standards]
```

### Template Impact
Story templates should reference the appropriate Story Type Rules:
- Include story type in story metadata
- Add reminder text: "See [Story Type] Rules in process definition for guidance on appropriate level of investment and focus."

---

## Expected Behavioral Change

### Before (Without Rules)
Agent sees "probably need to remove database":
- Interprets as incomplete specification
- Asks: Should stories always include database reset instructions?
- Asks: Should there be UI for this?
- Asks: Should this be in story or task definition?
- Considers production concerns (error handling, user feedback)

### After (With Rules)
Agent sees "probably need to remove database":
- Interprets as pragmatic permission
- Action: Hits database constraint → deletes ctrack.db → continues
- If deletion doesn't work → tries other simple approach
- No questions asked unless the learning objective itself is unclear
- No consideration of production concerns

---

## Next Steps for Guardrails Project

1. **Define rules for remaining story types** (POC, Framing, Glueing, Anchoring, Joining, User, Compliance)
   - Each should specify appropriate investment level
   - Each should define what to focus on vs. ignore
   - Each should give permission to be pragmatic

2. **Add Story Type Rules section to process definition** (after Test Rules)

3. **Update story templates** to reference Story Type Rules explicitly

4. **Create examples** of good Study stories that demonstrate these principles

5. **Test with agents** - Present story1.md with Study Story Rules included, validate behavioral change

---

## Design Principles for Other Story Type Rules

Based on the Study Story Rules pattern, rules for other types should:

1. **Define the phase's investment level** - What level of completeness/polish is appropriate?
2. **Give pragmatic permissions** - What can be done "quick and dirty" vs. needs care?
3. **Focus attention** - What matters most for this story type?
4. **Define success criteria** - How do we know this story succeeded?
5. **Set boundaries** - What explicitly doesn't belong in this phase?

### Sketch: POC Story Rules (for reference)
1. **Demo over Design** - Goal is to demonstrate viability, not create architecture
2. **Happy Path Only** - Focus on the main flow, ignore error cases
3. **Scaffold Freely** - Temporary glue code is expected and appropriate
4. **Show, Don't Tell** - Code that can be run/demoed > documentation
5. **Expect Disposal** - POC code is typically replaced, not refactored

### Sketch: Anchoring Story Rules (contrast)
1. **Production Quality** - Error handling, edge cases, and polish are now required
2. **API Stability** - Interfaces should be carefully designed for longevity
3. **Test Coverage** - Follow "No Mocking" rule, aim for comprehensive tests
4. **Documentation Required** - APIs, complex logic, and usage patterns must be documented
5. **Refactor, Don't Patch** - If design issues emerge, fix them now before they're locked in
