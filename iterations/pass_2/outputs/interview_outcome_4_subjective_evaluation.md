# Interview Outcome 4: Subjective Evaluation and Design Rationale Capture

## Context

When discussing whether Study stories should specify evaluation criteria (like "ease of implementation," "user experience," etc.), it became clear that this misunderstands the nature of evaluation in exploratory phases.

## Core Insight: Evaluation is Subjective and Experiential

For Study stories (and sometimes Framing, Glueing stories), evaluation is **not a checklist comparison**. It's a subjective assessment based on:

- **Experience-based software design intuition**
- **Looking at the code and imagining where it might be going**
- **Sensing which path has more potential or "rightness"**
- **Feeling which approach aligns with project direction**

This kind of evaluation:
- Cannot be pre-specified in criteria
- Emerges from direct experience with the code
- Draws on tacit knowledge and pattern recognition
- Is more about "Quality" (in Pirsig's sense) than measurable metrics

## What This Means for Story Definitions

### Study Stories Should NOT:
- ❌ Specify evaluation criteria upfront
- ❌ Require measurable comparison dimensions
- ❌ Prescribe what makes one option "better"
- ❌ Create evaluation rubrics or scorecards

### Study Stories SHOULD:
- ✓ State the question being explored
- ✓ Identify options to try
- ✓ Leave evaluation to user's subjective judgment
- ✓ Trust user's design intuition to sense the right path

### User's Role in Study Stories:
The user evaluates by:
1. Looking at the resulting code
2. Imagining where it might be going
3. Using design intuition to sense direction
4. Deciding: shape it toward preferred direction, or cut it off and try something else

**This is inherently a human, subjective role that cannot be delegated to the agent.**

## Reporter Role Implications

The Reporter role's job is **not to evaluate**, but to **present experiments in a way that facilitates user's subjective evaluation**.

**Reporter should:**
- Present each experiment's code clearly
- Highlight key differences between approaches
- Show what was learned or discovered
- Ask open questions: "What did you observe?" "Which approach feels right?"

**Reporter should NOT:**
- Score options against criteria
- Recommend which option is "best"
- Try to make the evaluation objective
- Replace user judgment with metrics

The Reporter **facilitates** subjective evaluation, doesn't **perform** objective evaluation.

## The Lost Knowledge Problem

### Current State
Design rationale and decision-making thinking is **almost always lost**:
- "Why did we choose approach A over B?"
- "What did we learn from this experiment?"
- "What mistake did we already try and reject?"
- "What intuition guided this architectural decision?"

This lost knowledge leads to:
- Future developers repeating mistakes already made
- Revisiting decisions without context
- Unable to understand "why" behind current state
- Loss of accumulated wisdom

### Future Vision: Capturing Design Rationale

**Guardrails process enhancement goal:**
Add voice-to-text transcription capability to capture user's thinking during evaluation.

**During experiment evaluation, user speaks thoughts:**
- "This approach feels cleaner because..."
- "I'm concerned this will become problematic when we add..."
- "The way this handles X reminds me of the Y problem we had..."
- "I'm choosing this even though it's more code because..."

**System captures and attaches to story:**
- Transcribed rationale
- Links to relevant experiments/tasks
- Timestamped with decision point
- Searchable for future reference

**Benefits:**
- Preserves design thinking that would otherwise be lost
- Future developers can understand "why"
- Can review thinking when revisiting decisions
- Builds institutional/project memory
- Captures tacit knowledge in explicit form (as much as possible)

## Implementation in Guardrails Process

### Immediate: Study Story Template

**Do NOT include "Evaluation Criteria" section in Study story template.**

Instead, include:
```markdown
**Expected User Role:**
After experiments are complete, user will evaluate results based on design intuition
and experience to decide which approach (if any) to pursue further.
```

### Near-Term: Reporter Role Guidance

Update Reporter role definition:

```markdown
**Reporter Role:**
...
For Study stories: Present experiments clearly to facilitate user's subjective
evaluation. Do not attempt to score or rank options. Ask open questions to prompt
user reflection. Capture user's rationale if provided.
```

### Long-Term: Voice Transcription Feature

**Future enhancement to guardrails tooling:**

1. **Evaluation Session Mode**
   - User enters evaluation session after experiments complete
   - Voice recording starts
   - User reviews code and speaks thinking aloud
   - System transcribes in real-time

2. **Rationale Attachment**
   - Transcription attached to story file
   - Links to specific experiments/tasks referenced
   - Indexed for future search

3. **Rationale Query**
   - Later developers can search: "Why did we choose textual-fspicker?"
   - System returns story + evaluation rationale
   - Context preserved across time

4. **Format Options**
   - Voice notes (audio preserved)
   - Transcribed text
   - Structured by decision point
   - Tagged by story/task/component

## Story Type Variations

This subjective evaluation pattern applies differently across story types:

**Study, Framing, Glueing:**
- High subjectivity
- Design intuition primary
- User evaluation essential
- Rationale capture valuable

**POC:**
- Moderate subjectivity
- "Does it demonstrate viability?" is more objective
- Still benefits from rationale capture

**Anchoring, Joining, Compliance:**
- Lower subjectivity
- More objective criteria (tests pass, standards met)
- Rationale less critical but still useful

The autonomy spectrum correlates with subjectivity:
- High autonomy phases → High subjective evaluation
- Low autonomy phases → More objective evaluation

## Examples

### Example 1: File Picker Evaluation (Story1)

**NOT this (objective criteria):**
```
Evaluation Results:
- DirectoryTree: 45 LOC, 3 clicks to select, Rating: 7/10
- textual-fspicker: 12 LOC, 2 clicks to select, Rating: 8/10
- textual-filedrop: 8 LOC, 1 click to select, Rating: 9/10
Recommendation: Choose textual-filedrop ✓
```

**But this (facilitating subjective evaluation):**
```
Experiment Results:

DirectoryTree approach: [show code]
Key observations: Requires building custom picker, flexible but more code

textual-fspicker approach: [show code]
Key observations: Purpose-built library, straightforward integration

textual-filedrop approach: [show code]
Key observations: Drag-and-drop interaction, minimal code

What did you observe? Which approach feels right for this project?
```

**User's subjective evaluation (captured):**
[Voice note]
"Looking at these... the DirectoryTree is too much code for something that should be simple. The textual-filedrop is intriguing but drag-and-drop feels wrong for selecting a GnuCash file - that's more of a 'I know where it is, let me browse to it' interaction. The textual-fspicker hits the sweet spot - purpose-built for this use case, integrates cleanly, the code looks straightforward. I'm going with that one. If we have problems with it later, DirectoryTree is a fallback."

### Example 2: Architecture Decision (Hypothetical Framing Story)

**Reporter presents:**
```
Experiment: Tried three approaches to state management:
1. Global singleton: [show code]
2. Context passing: [show code]
3. Event bus: [show code]

All three work for current use case. What's your read on which direction this should go?
```

**User's subjective evaluation (captured):**
[Voice note]
"The singleton is tempting because it's simple right now, but I've been burned by globals before when testing gets complex. The context passing is cleanest architecturally but it's going to get verbose as we add more features. The event bus... that's interesting. It's more code up front but I can see how it would handle the async operations we'll need for GnuCash file operations. Yeah, let's go with the event bus. It's investing in the direction this needs to go."

## Key Distinction

**Objective evaluation:** Can be delegated, measured, automated
**Subjective evaluation:** Requires human judgment, experience, intuition

The guardrails process must:
- Recognize which type of evaluation is appropriate for each story type
- Not force objectivity onto inherently subjective decisions
- Support (not replace) human judgment
- Capture (not lose) the subjective rationale

## Summary

Study stories (and similar exploratory work) require **subjective evaluation based on design intuition**. This cannot be pre-specified as evaluation criteria, and should not be made artificially objective. The user's role is to look at results and sense which path forward has Quality. The Reporter facilitates this by presenting clearly, not by scoring or ranking.

Future enhancement: Capture this subjective thinking through voice transcription so design rationale isn't lost to future developers.

**Decision for story templates: Do NOT include evaluation criteria sections for Study stories.**
