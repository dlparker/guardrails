# Applying Metaphysics of Quality to Agentic Coding: The Guardrails Framework

## Chapter 3: Operationalizing Constraints by Phase

### Introduction to Phase-Specific Constraints

Chapter 2 established the Guardrails taxonomies and workflows. This chapter operationalizes those constraints through **phase-specific behavioral rules** that guide agentic assistants across the development lifecycle. Each phase represents a distinct maturity level with corresponding autonomy expectations, constraint intensity, and behavioral directives.

The **Autonomy Spectrum** (introduced in Chapter 2) provides the foundational principle:

```
Exploring → Pioneering → Settling → Fortifying → Re-Founding
   ↑                                                    ↑
High Autonomy                                  High Specification
(figure it out)                                (follow exact specs)
```

This spectrum determines:
- **Agent decision-making authority**: From pragmatic problem-solving to strict specification adherence
- **Constraint granularity**: From high-level principles to detailed requirements
- **Validation expectations**: From subjective evaluation to objective criteria
- **Code quality investment**: From throwaway spikes to production polish

Phase-specific rules translate these principles into actionable guidance, ensuring agents align with the user's DQ/SQ rhythm while preventing the scope creep and context pollution identified in Chapter 1.

### The Autonomy Spectrum in Detail

| **Autonomy Level** | **Phase**       | **Agent Mindset**                          | **User Involvement**                  | **Constraint Style**                  |
|-------------------|----------------|-------------------------------------------|--------------------------------------|--------------------------------------|
| **High**          | Exploring      | "Figure it out pragmatically"             | Sets direction, evaluates results     | Principles + "throw-away" directives  |
| **High-Medium**   | Pioneering     | "Make reasonable choices, validate approach" | Approves key decisions, tests viability | Story-focused constraints            |
| **Medium**        | Settling       | "Follow preferred patterns, ask about architecture" | Specifies integration points      | Pattern guidance + architectural rules |
| **Low-Medium**    | Fortifying     | "Implement exact specifications"          | Provides detailed requirements        | Detailed specs + compliance rules     |
| **Low**           | Re-Founding    | "Precise implementation, no deviations"   | Complete specifications               | Exact requirements + regression protection |

## Universal Constraints (Apply to ALL Phases)

These **Rule 0** constraints apply universally, regardless of phase:

| **Rule** | **Statement** | **Purpose** | **Examples** |
|---------|--------------|-------------|-------------|
| **Rule 0** | **Complete, Then Stop** | Deliver exactly what was requested | "Future CLI tool" → ignore<br>"JSON later" → ignore |
| **Rule 1** | **Context ≠ Requirements** | Background = understanding only | User rationale ≠ action items |
| **Rule 2** | **No Implicit Scope Expansion** | Don't infer additional requirements | "Might be useful for X" ≠ implement X |

### Rule 0: Complete, Then Stop (MANDATORY)

**Core Principle**: 
> "A skilled human developer would understand that this is background... LLM based coding assistants will keep dragging it back in"

**Implementation**:
```markdown
REQUEST: [Exact deliverable - 1-2 sentences]
CONTEXT: [Background for understanding ONLY]

DELIVER: Exactly the REQUEST above
IGNORE: Future plans, rationale, possibilities mentioned in CONTEXT

### Phase-Specific Behavioral Rules

#### Exploring Phase: Maximum Autonomy, Minimum Investment

**Primary Story Types**: Study, POC  
**Autonomy Level**: HIGH  
**Guiding Principle**: "Learn fast, invest minimally, discard freely"

**Core Rules**:

1. **Information Over Implementation**
   - Goal is learning, not production code
   - Write minimum code necessary to answer questions or reveal solution characteristics
   - **Agent Directive**: "Produce just enough code to demonstrate the concept or answer the study question"

2. **Vague is Permissive**
   - Phrases like "probably need to," "some kind of," "might require" are **permissions to handle pragmatically**
   - **Agent Directive**: "A journeyman programmer would figure it out - you should too"
   - Don't ask for clarification unless the learning objective itself is unclear

   | **Vague Phrase**            | **Agent Action**                          |
   |-----------------------------|------------------------------------------|
   | "Probably need to remove DB" | Delete database if it blocks progress    |
   | "Some kind of validation"   | Pick any reasonable validation approach  |
   | "Might require reset"       | Reset if you think it's needed           |

3. **No Production Thinking**
   - **Strictly ignore** (unless explicitly requested):
     | **Category**             | **Examples**                          |
     |--------------------------|---------------------------------------|
     | Error handling           | try/except blocks, validation         |
     | UI polish                | Styling, animations, responsive design |
     | Edge cases               | Rare scenarios, boundary conditions   |
     | Performance              | Optimization, caching                 |
     | Logging/monitoring       | Log statements, metrics               |
     | Documentation            | Docstrings, comments                 |
     | Reusability              | Abstractions, design patterns         |
     | Test coverage            | Unit tests, integration tests         |

4. **Unblock Yourself**
   - **Agent Directive**: "Resolve obstacles with simplest possible approach"
   | **Obstacle**             | **Pragmatic Solution**                     |
   |--------------------------|-------------------------------------------|
   | Database state issues    | Delete database file                      |
   | Missing files            | Hard-code test data paths                 |
   | Dependency conflicts     | Install/update as needed                  |
   | Unclear APIs             | Try most obvious approach first           |

5. **Measure Success by Learning**
   | **Success Criteria**      | **NOT Success Criteria**                  |
   |--------------------------|------------------------------------------|
   | ✓ Answered the question  | ✗ Maintainable code                      |
   | ✓ Revealed new info      | ✗ Testable code                          |
   | ✓ Demonstrated concept   | ✗ Complete implementation                |
   |                          | ✗ Would pass code review                 |

6. **Throw-Away Mindset**
   - **Agent Directive**: "Assume this code will be discarded or heavily modified"
   | **Use This**             | **Avoid This**                           |
   |--------------------------|------------------------------------------|
   | Hard-coded values        | Configuration files                      |
   | Print statements         | Logging frameworks                       |
   | Simple functions         | Classes and abstractions                 |
   | Inline code              | Modular architecture                     |

**Exploring Phase Example Directives**:
- "Produce example code for user evaluation of specific solution options"
- "Build minimal spike ensuring resource supplies needed info"
- "Identify existing code related to Story goals"

#### Pioneering Phase: Validate Solution Approaches

**Primary Story Types**: Framing, Glueing  
**Autonomy Level**: High-Medium  
**Guiding Principle**: "Validate that the solution approach works"

**Key Behavioral Shifts from Exploring**:
1. **Slightly Higher Investment**: Code should demonstrate viability, not just learning
2. **Basic Integration**: Components should work together minimally
3. **Early API Definition**: Establish rough boundaries and interfaces

**Core Rules**:
1. **Focus on Validation**: Primary goal is proving the approach works end-to-end
2. **Minimal but Functional**: Code should run and demonstrate core value
3. **Preserve for Next Phase**: Successful work becomes foundation for Settling phase
4. **Still Avoid Production Polish**: No error handling, logging, or comprehensive testing

**Agent Directives**:
- "Create minimal working integration demonstrating solution viability"
- "Establish basic component boundaries and interfaces"
- "Build scaffolding to validate solution approach"

#### Settling Phase: Build Stable Foundations

**Primary Story Types**: Anchoring, Joining, User  
**Autonomy Level**: Medium  
**Guiding Principle**: "Create stable foundation supporting further development"

**Key Behavioral Shifts**:
1. **API Solidification**: Define stable interfaces for dependent components
2. **Basic Error Handling**: Handle expected failure modes
3. **Integration Testing**: Ensure components work together reliably
4. **Architectural Alignment**: Consider impact on other features

**Core Rules**:
1. **Stable APIs**: Changes require explicit justification
2. **Primary Logic**: Implement core business logic to production quality
3. **Basic Testing**: Tests for main happy paths (No Mocking rule applies)
4. **Architectural Questions**: Ask user about choices affecting other features

**Agent Directives**:
- "Solidify APIs and primary logic for production use"
- "Improve integrations to reliable working state"
- "Implement user interactions with stable interfaces"

#### Fortifying Phase: Production Readiness

**Primary Story Types**: Compliance, Joining, Anchoring  
**Autonomy Level**: Low-Medium  
**Guiding Principle**: "Prepare for release"

**Key Behavioral Shifts**:
1. **Comprehensive Testing**: Full test coverage (Mostly No Mocking)
2. **Production Quality**: Error handling, logging, documentation
3. **Performance**: Basic optimization where needed
4. **Compliance**: Standards for security, accessibility, style

**Core Rules**:
1. **Exact Specifications**: Follow requirements precisely
2. **Comprehensive Coverage**: Tests for all scenarios
3. **Production Features**: Full error handling, monitoring, documentation
4. **Ask for Clarification**: Any ambiguity affecting production behavior

**Agent Directives**:
- "Implement comprehensive test coverage following test rules"
- "Add production-quality error handling and logging"
- "Ensure compliance with coding standards and style guides"

#### Re-Founding Phase: Extension and Evolution

**Primary Story Types**: Compliance, Joining, Anchoring, User  
**Autonomy Level**: Low  
**Guiding Principle**: "Extend or modify while preserving existing quality"

**Key Behavioral Shifts**:
1. **Regression Protection**: Full testing of existing functionality
2. **Backward Compatibility**: Preserve existing interfaces where possible
3. **Incremental Enhancement**: Add features without disrupting stability
4. **Explicit Specifications**: Complete requirements provided

**Core Rules**:
1. **No Breaking Changes**: Unless explicitly authorized
2. **Comprehensive Regression**: Test existing functionality
3. **Precise Implementation**: Follow exact specifications
4. **Documentation Updates**: Keep docs current

**Agent Directives**:
- "Add new features while preserving existing functionality"
- "Modify support for new requirements with full regression testing"
- "Extend capabilities following exact specifications"

### Phase Transition Guidelines

| **From Phase** | **To Phase**   | **Key Changes**                                    | **Agent Focus**                          |
|---------------|---------------|----------------------------------------------------|------------------------------------------|
| Exploring     | Pioneering    | Learning → Validation                              | Make it work end-to-end                  |
| Pioneering    | Settling      | Validation → Stability                             | Solidify APIs, reliable integration      |
| Settling      | Fortifying    | Foundation → Production                            | Comprehensive testing, polish             |
| Fortifying    | Re-Founding   | Release → Evolution                                | Preserve quality while extending         |

### Directive Library by Phase

| **Phase**      | **Example Directives**                                                                 |
|---------------|----------------------------------------------------------------------------------------|
| **Exploring** | "Produce example code for user evaluation", "Build minimal spike", "Identify related code" |
| **Pioneering**| "Create minimal working integration", "Establish component boundaries", "Validate approach" |
| **Settling**  | "Solidify APIs", "Improve integrations reliably", "Implement stable user interactions" |
| **Fortifying**| "Add comprehensive tests", "Implement production error handling", "Ensure compliance" |
| **Re-Founding**| "Add features with regression testing", "Extend following exact specs", "Preserve APIs" |

### Preventing Backsliding: Constraint Enforcement Patterns

1. **Phase Declaration in Every Story/Task**:
   ```markdown
   | **Phase**     | **Exploring** |
   |--------------|--------------|
   | **Autonomy** | High         |
   | **Focus**    | Learning     |
   ```

2. **Repeated Phase Reminders**:
   - Every agent prompt includes: "You are operating in [PHASE] phase with [AUTONOMY] autonomy"
   - Story Type Rules explicitly referenced

3. **Constraint Checklists**:
   | **Phase**     | **Must Avoid**                          |
   |--------------|----------------------------------------|
   | Exploring    | Production features, comprehensive tests |
   | Pioneering   | Full error handling, documentation      |
   | Settling     | Incomplete APIs, unreliable integration |

4. **Git Commit Message Standards**:
   ```
   [Story-1]: GnuCash File Selection: [Task-1.1]: Spike Code: DirectoryTree picker (Exploring)
   ```

### Measuring Constraint Effectiveness

| **Metric**                  | **Target**              | **Early Phases** | **Later Phases** |
|-----------------------------|------------------------|-----------------|-----------------|
| Lines of code per task      | < 100 LOC              | ✓              | ✗               |
| Time to review per task     | < 5 minutes            | ✓              | ✗               |
| Unwanted features introduced| 0%                     | ✓              | ✓               |
| Context reset frequency     | < 1 per story          | ✓              | ✓               |
| User approval rate          | > 90% first pass       | ✓              | ✓               |

### Integration with Story Workflow

Phase constraints integrate directly into the Chapter 2 workflow:

1. **Story Creation**: User specifies phase → determines applicable rules
2. **Task Breakdown**: Analyst applies phase-appropriate autonomy level
3. **Execution**: Coder follows phase-specific directives
4. **Evaluation**: Reporter presents results with phase context
5. **Disposition**: User evaluates against phase success criteria

**Example Story Header**:
```markdown
| **Phase**     | **Exploring** |
| **Story Type**| Study        |
| **Autonomy**  | High         |
| **Directives**| "produce example code for user evaluation" |
```

This chapter provides the operational blueprint for constraint application. Chapter 4 will examine complete story and task lifecycles, demonstrating how these phase-specific rules manifest in practice through the full DQ/SQ workflow.
