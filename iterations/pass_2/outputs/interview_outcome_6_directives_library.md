# Interview Outcome 6: Directives as Reusable Focus Patterns

## Context

Story1.md includes a "directive" field but doesn't explain its purpose. This field is critical to the story generation process and warrants explicit definition.

## What is a Directive?

A **directive** is a clarifying instruction that specifies a "subrole," "action mode," or "skill focus" for the agent. It shapes how the agent approaches the work.

**Directives are:**
- More specific than roles (Coder, Analyst, etc.)
- More general than task-specific instructions
- Reusable across different stories and tasks
- Buildable into a personal library over time
- User-specific patterns that match their workflow

## Examples of Directives

### For Code Quality
- "ensure API methods have type annotations and doc strings"
- "add comprehensive error handling with user-friendly messages"
- "follow existing code style patterns in the module"

### For Testing
- "add test details to approach 100% coverage by supplying arguments that don't validate"
- "focus on integration test scenarios, not unit test isolation"
- "ensure tests follow the 'no mocking' rule"

### For Exploration
- "produce example code for user evaluation of specific solution options"
- "build minimal spike ensuring resource supplies needed info"
- "let user evaluate UI component selection"

### For Analysis
- "identify existing code related to Story goals"
- "scope code changes for Story and breakdown into proposed Tasks for new and changed code separately"
- "analyze performance characteristics and report bottlenecks"

### For Design
- "establish component boundaries without implementing full logic"
- "design API surface for future extensibility"
- "minimize dependencies on external libraries"

### For Documentation
- "generate API documentation from code structure"
- "update README with new feature usage examples"
- "document design rationale in architecture decision records"

## How Directives Work

### In Story Context

A story's directive applies to all work within that story:

```markdown
**Story ID:** 1
**Story Name:** GnuCash finder experiment
**Directive:** produce example code for user evaluation of specific solution options
```

This tells agents: "Your goal is not production code. Your goal is code that helps the user make a decision."

### In Task Context

A task's directive can override or augment the story directive:

```markdown
**Task ID:** 1.1
**Task Name:** try DirectoryTree picker
**Directive:** build minimal spike ensuring resource supplies needed info
```

This further narrows focus: "Don't worry about completeness, just prove the concept."

### Directive + Story Type Rules + Autonomy Spectrum

These three work together:

**Story Type Rules** = General mindset for the phase (Study: focus on learning, no production thinking)

**Autonomy Spectrum** = How much detail to expect vs. figure out (Exploring: high autonomy)

**Directive** = Specific focus for this particular work ("ensure API has type annotations")

Example combination for an Anchoring story:
- **Phase:** Settling
- **Story Type:** Anchoring
- **Autonomy Spectrum:** Medium (follow patterns, flexibility on details)
- **Story Type Rules:** Production Quality, API Stability, Test Coverage, Documentation Required
- **Directive:** "ensure API methods have type annotations and doc strings"

The agent understands:
1. This is production-quality work (Story Type Rules)
2. Follow established patterns but have flexibility on implementation (Autonomy Spectrum)
3. Specifically focus on type annotations and doc strings (Directive)

## Directives Library

### Building the Library

Users build a personal library of directives over time:

1. **First project:** User writes directives from scratch in stories
2. **As patterns emerge:** User adds useful directives to library
3. **Later projects:** User selects from library instead of writing
4. **Refinement:** User edits directives based on what works

**Library structure (future tool):**
```json
{
  "directives": [
    {
      "id": "api-types-docs",
      "category": "code-quality",
      "text": "ensure API methods have type annotations and doc strings",
      "applicable_roles": ["Coder"],
      "applicable_story_types": ["Anchoring", "Joining"]
    },
    {
      "id": "minimal-spike",
      "category": "exploration",
      "text": "build minimal spike ensuring resource supplies needed info",
      "applicable_roles": ["Coder"],
      "applicable_story_types": ["Study", "POC"]
    },
    // ... more directives
  ]
}
```

### Categories (Suggested)

- **Exploration:** Directives for Study, POC stories
- **Code Quality:** Type hints, documentation, style
- **Testing:** Coverage, mocking rules, test types
- **Design:** Architecture, API design, boundaries
- **Analysis:** Research, scoping, impact assessment
- **Performance:** Optimization, profiling, benchmarking
- **Documentation:** User docs, API docs, rationale
- **Integration:** Connecting components, scaffolding

### Q&A Tool Integration

When generating a story, the Q&A tool:

1. **Asks for directive:**
   - "What specific focus should guide this work?"

2. **Shows library options:**
   - Filtered by story type and phase if helpful
   - Searchable/filterable
   - Shows recently used directives first

3. **Allows custom entry:**
   - User can type new directive
   - Tool suggests: "Add to library for future use?"

4. **Saves to library:**
   - User can categorize
   - User can mark as frequently used
   - Tool learns user patterns over time

### Example Q&A Flow

```
Q: What story type is this?
A: Study

Q: What specific focus should guide this work? [Select from library or enter custom]
   Recent:
   - produce example code for user evaluation of specific solution options
   - build minimal spike ensuring resource supplies needed info

   Library (Study stories):
   - identify existing code related to Story goals
   - compare solution approaches on key dimensions
   - validate technical feasibility of approach

   [Custom: ____________________]

A: [User selects] "produce example code for user evaluation of specific solution options"

[Story generated with this directive]
```

## Benefits of Directives Library

### 1. Reduces User Overhead
- Don't rewrite the same focus instructions
- Select from dropdown instead of typing
- Faster story generation

### 2. Consistency Across Stories
- Same directive = same agent behavior
- Easier to predict results
- Patterns become established

### 3. Evolves with User
- Library grows with experience
- Captures what works for this user
- Personalizes the process

### 4. Communicates Intent Clearly
- Explicit focus rather than implicit
- Agents understand what to prioritize
- Reduces need for clarification

### 5. Separates Concerns
- Story Type Rules = phase-level guidance
- Directives = work-specific focus
- Task details = concrete what-to-do

## Implementation in Story Generator Tool

### Data Model

**Directives table:**
```sql
CREATE TABLE directives (
  id INTEGER PRIMARY KEY,
  text TEXT NOT NULL,
  category TEXT,
  applicable_roles TEXT,  -- JSON array
  applicable_story_types TEXT,  -- JSON array
  usage_count INTEGER DEFAULT 0,
  last_used TIMESTAMP,
  created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

**Story-directive relationship:**
```sql
CREATE TABLE stories (
  id INTEGER PRIMARY KEY,
  name TEXT,
  directive_id INTEGER REFERENCES directives(id),
  -- or just store directive text directly --
  directive_text TEXT,
  -- ... other fields
);
```

### UI Features

**Directive Selection:**
- Autocomplete search
- Category filters
- Sort by: recent, frequent, alphabetical
- Preview: show example stories that used this directive
- Quick-add: "None of these fit? Add new directive"

**Directive Management:**
- List all directives
- Edit/delete directives
- Merge similar directives
- Export/import library (share between projects)

**Usage Tracking:**
- Count how often each directive is used
- Show last used date
- Suggest frequently used directives first

### Minimal Implementation (V1)

For the first version of the story generator:

1. **Simple text field:** "Directive: [free text]"
2. **Optional dropdown:** Load from simple JSON file
3. **Save feature:** "Add this directive to library?" checkbox
4. **Basic persistence:** Append to JSON file

Later versions can add:
- Database storage
- Categorization
- Search/filter
- Usage analytics
- Sharing between projects

## Process Definition Updates

### Add Directives Section

Add after "Story Definitions" section:

```markdown
## Directives

Directives are reusable focus patterns that specify how agents should approach work.
They are more specific than roles but more general than task details.

Examples:
- "ensure API methods have type annotations and doc strings"
- "build minimal spike ensuring resource supplies needed info"
- "identify existing code related to Story goals"

Users build a personal library of directives over time. The story generator tool
provides directive selection from the library.

Directives work in combination with:
- Story Type Rules (phase-level mindset)
- Autonomy Spectrum (detail level expectations)
- Task-specific instructions (concrete what-to-do)

See examples in the Directives Library [link to reference doc or tool].
```

### Update Story Template

Story template should include directive field with explanation:

```markdown
**Directive:** [Select from library or enter custom focus instruction]

Examples:
- For Study stories: "produce example code for user evaluation of specific solution options"
- For Anchoring stories: "ensure API methods have type annotations and doc strings"
- For Testing tasks: "add test details to approach 100% coverage by supplying arguments that don't validate"
```

## Open Questions for Iteration

1. **Granularity:** Should directives be at story level, task level, or both?
   - Story1 has story-level directive, but examples show task-level potential
   - Maybe story directive is default, tasks can override?

2. **Required vs. Optional:** Is directive always required, or only for certain story types?
   - Study stories might always need directive to focus exploration
   - Compliance stories might not need it (requirements are the focus)?

3. **Multiple Directives:** Can a story have multiple directives?
   - "ensure type annotations" AND "add comprehensive error handling"
   - Or should that be two separate tasks/stories?

4. **Directive Composition:** Can directives reference other directives?
   - "follow production code standards" = type annotations + error handling + docs
   - Or keep them atomic?

5. **Sharing Directives:** Should users be able to share directive libraries?
   - Export/import between projects
   - Community directive library?
   - Per-project vs. per-user vs. shared?

These questions will be answered through iteration on the story generator tool and actual usage.

## Summary

Directives are reusable focus patterns that shape how agents approach work. They fill the gap between general role guidance and specific task instructions. Building a personal directives library reduces user overhead, increases consistency, and captures patterns that work for each user.

The story generator tool should support directive selection from a library, with the ability to add new directives as they emerge from practice.

**Decision for story generator tool: Implement directive library with lookup/add feature.**
