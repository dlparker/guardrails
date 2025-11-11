# guardrails

A process framework and toolset for constraint-driven AI-assisted software development.

## Project Vision

Guardrails provides structured guidance for AI coding agents through explicit constraints and context-efficient artifacts, enabling autonomous work while preventing over-engineering and maintaining focus on defined goals.

## Core Philosophy

Traditional AI coding assistance often struggles with:
- Over-engineering solutions beyond stated requirements
- Inefficient use of context windows
- Lack of structured workflows for different development phases
- Difficulty maintaining focus on specific, bounded tasks

Guardrails addresses these challenges through:
- **Explicit constraint frameworks** that define what to do AND what NOT to do
- **Context-efficient story templates** that embed just enough guidance without bloating prompts
- **Phase-aware workflows** that adapt behavior to project maturity (Exploring → Pioneering → Settling)
- **Disposable-first thinking** in early phases to encourage rapid experimentation

## Key Concepts

### Development Phases
- **Exploring**: Learning through disposable spikes, minimal complexity, no error handling
- **Pioneering**: Building first implementations, accepting technical debt for learning
- **Settling/Fortifying**: Hardening code, production quality, comprehensive testing

### Story Types
- **Study**: Compare multiple approaches through minimal experiments
- **Pathfinder**: Build prototypes to validate technical decisions
- **Forming**: Implement features with phase-appropriate quality
- **User**: Deliver end-user functionality
- **Compliance**: Address technical debt, security, standards

### Actor Roles
- **coder**: Writes, reviews, and refactors code
- **planner**: Breaks work into tasks, estimates effort
- **code_reviewer**: Analyzes code for quality, patterns, issues
- **test_developer**: Creates and maintains tests
- **reporter**: Synthesizes information, generates summaries

### Directives (Under Development)
Fine-grained activity constraints within roles:
- "Scope integration points, estimate change size (DO NOT implement)"
- "Build minimal spike, capture observations (disposable code)"
- "Implement [feature], run tests, commit"
- "Review for [concern], propose refactoring"

## Process Artifacts

### Story Files
Programmatically generated documents combining:
- Generic elements (phase constraints, story-type workflows)
- Specific requirements (options to evaluate, expected artifacts, definition of done)

### Task Files
11-item metadata structure including:
- Role and directive assignments
- Git hash audit trail (start/end states)
- Save/discard decisions from lead developer
- Links to related tasks and superseding alternatives

### Session Transcripts
AI coding sessions captured as markdown, committed as first-class artifacts for:
- Retrospective analysis via git diff
- Context for synthesis and reporting
- Cross-project learning and process refinement

### Inspection Reports
Structured reviews identifying issues, root causes, and resolutions, inspired by software design document inspection processes.

## Design Principles

### Context Window Efficiency
Stories balance two constraints:
1. **Self-contained**: Include enough guidance for autonomous agent work
2. **Non-redundant**: Reference stable taxonomies rather than duplicating definitions

### Constraint-Driven Development
Explicit "what NOT to do" constraints prevent common AI agent failure modes:
- Adding error handling in exploratory spikes
- Refactoring while implementing new features
- Building production-quality code during learning phases

### Audit Trail Over Rollback
Git hashes capture repository state at task boundaries, enabling:
- `git diff {start} {end}` to see exactly what an experiment produced
- Retrospective analysis without polluting git history
- Reporter role synthesis from actual changes, not descriptions

### Dogfooding
The process is being developed using itself - directive library, story generators, and process tools will emerge from Study and Pathfinder stories in this repository.

## Tools (Planned/In Development)

### Directive Library
Search/create/browse tool for activity directives:
- Prevents semantic drift (inconsistent phrasings of same intent)
- Grows organically as patterns emerge
- Maintains consistency without rigid taxonomies

### Story Generator
Programmatic composition of story files from:
- Generic templates (phase constraints, workflows)
- Story-type-specific patterns
- User-provided specifics (options, artifacts, goals)

### Session Capture
Tool for recording Claude Code sessions as markdown (currently in use for this project's development).

## Current State

**Phase**: Exploring

This repository is in active zero-to-one development. Current contents:
- Foundational concept definitions (`ai_docs/background/`)
- Process definitions and workflows (`ai_docs/process_definition.md`)
- First iteration artifacts (`iterations/first/`)
- Inspection reports documenting design decisions

The process is being validated through real usage on the `ctrack` project (credit card transaction import tool), with learnings feeding back to improve guardrails itself.

## Meta-Process Architecture

```
guardrails repo
  ├─ Process definitions (foundations, story templates)
  ├─ Tools (directive library, story generator)
  └─ Session transcripts (committed as artifacts)
       └─ Synthesized into process improvements
            └─ Applied to ctrack development work
                 └─ Generates new sessions
                      └─ Improves guardrails
```

This feedback loop ensures the process evolves through actual use, not theoretical design.

## Contributing

As this is in early exploration phase, the process itself is the primary deliverable. Contributions will be considered once the core framework stabilizes.

## License

TBD

