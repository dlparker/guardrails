# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Guardrails is a process framework for constraint-driven AI-assisted software development. This is a zero-to-one project in the **Exploring** phase, focused on developing structured guidance for AI coding agents through explicit constraints and context-efficient artifacts.

**Critical Context**: This repository contains process definitions and tools, not a traditional software project. Most files are markdown documents defining workflows, phases, roles, and story templates. The primary "output" is documentation and tooling that will be used by AI agents working in *other* repositories.

## Core Architecture

### Document Structure

The repository is organized around **composable process artifacts**:

**`background/`** - Foundational concepts
- `foundations_concept_summary.md` - Five-phase development model (Exploring → Pioneering → Settling → Fortifying → Re-Founding)
- `foundations_concept.md` - Detailed discussion of the frontier analogy
- `process_definition.md` - Story types, actor roles, and process overview

**`partials/`** - Reusable template components for programmatic story generation
- `phases/` - Phase-specific constraints (e.g., exploring.md)
- `roles/` - Actor role definitions (e.g., coder.md)
- `modes/` - Activity mode descriptions (e.g., code_scoping.md, coding.md)

**`manual/`** - Hand-crafted story definitions and examples
- `stories/` - Example stories like gnucash_file_selection_study.md

**`iterations/`** - Experimental iterations with session transcripts
- `first/` - Initial trial containing claude conversation log and inspection report

**`tools/`** - Utilities
- `org2md.py` - Converts org-mode files to markdown using pandoc

### Key Process Concepts

**Development Phases** determine quality expectations:
- **Exploring**: Disposable spikes, minimal complexity, no error handling
- **Pioneering**: First implementations, accept technical debt
- **Settling**: Add structure, tests, configuration
- **Fortifying**: Production quality, comprehensive testing
- **Re-Founding**: Versioned APIs, documentation, packaging

**Story Types** define the goal:
- **Study**: Compare approaches through minimal experiments, produce reports
- **Pathfinder**: Prototype components and integrations
- **Forming**: Convert prototypes to permanent implementations
- **User**: Deliver end-user functionality
- **Compliance**: Address technical debt, standards, documentation

**Actor Roles** define who does the work:
- **coder**: Writes code respecting phase constraints
- **planner**: Breaks down goals into tasks
- **code_reviewer**: Reviews for compliance with phase standards
- **test_developer**: Creates tests from story-level perspective
- **reporter**: Records process execution, compiles reports

**Modes/Directives** (evolving concept) define how roles approach tasks:
- Code Scoping: Find minimums and limits to define precise tasks
- Coding: Implement defined tasks
- Reviewing: Assess code for specific concerns
- Refactoring: Improve structure while maintaining behavior

### Story Template Architecture

Stories are **programmatically generated** from:
1. **Generic elements** - Phase constraints, story-type workflows (from `partials/`)
2. **Specific requirements** - Options to evaluate, expected artifacts, definition of done

Example structure from `manual/stories/gnucash_file_selection_study.md`:
```
# Story Definition
# Generic
## Phase 'Exploring'
[Phase-specific constraints: disposable output, minimal complexity, no error handling]

## Story Type 'Study'
[Workflow: create tasks → execute experiments → lead reviews → generate report]

# Specific
## Story Name: [Specific goal]
[Task breakdown, options to try, expected artifacts]
```

### Task Metadata Structure

Tasks include 11 metadata items:
1. Story name and definition file path
2. Task name
3. Description of how task applies to story goals
4. Expected artifacts description
5. Role (references process_definition.md §Actor Roles)
6. Mode/Directive (evolving - may become free-form directive)
7. Phase
8. Git hash at task start
9. Git hash at task completion
10. Save/discard decision from lead developer
11. Optional reference to superseding task

**Git hashes enable audit trail**: Use `git diff {start_hash} {end_hash}` to see exactly what an experiment produced.

## Development Commands

### Converting Org-Mode Files to Markdown

```bash
python tools/org2md.py
```

Converts all `.org` files in `partials/modes/`, `partials/phases/`, `partials/roles/`, and `manual/stories/` to markdown using pandoc.

## Design Principles

### Constraint-Driven Development

The process explicitly states both what to do AND what NOT to do. Example constraints from Exploring phase:
- "Treat output as likely disposable"
- "Absolutely avoid adding error handling, retries, optional API elements, etc. unless specified"

This prevents common AI agent failure modes like over-engineering and scope creep.

### Context Window Efficiency

Story templates balance two goals:
1. **Self-contained**: Include enough guidance for autonomous agent work
2. **Non-redundant**: Reference stable taxonomies rather than duplicating

Generated stories embed just enough guidance without bloating prompts or requiring large reference documents in context.

### Audit Trail Over Rollback

Git hashes capture repository state at task boundaries for retrospective analysis, not rollback. The reporter role can synthesize findings from actual diffs, not just descriptions.

### Session Transcripts as Artifacts

AI coding sessions are captured as markdown and committed as first-class artifacts. See `iterations/first/claude-conversation-2025-11-09-3a9c2598.md` for example. These enable:
- Retrospective analysis of design decisions
- Context for synthesis and reporting
- Process refinement based on actual usage

### Inspection Reports

Structured reviews documenting issues, root causes, and resolutions. See `iterations/first/process_docs/inspection_report_1.md` for format. Inspired by software design document inspection processes.

## Current State and Active Work

**Phase**: Exploring (the process is being developed using itself)

**Key Open Questions** (from inspection_report_1.md):
1. Mode vs. Directive: Should task constraint be taxonomy (Mode) or free-form with library support (Directive)?
2. Workflow sections: Need to add canonical workflow steps to each story type template
3. Directive library: Plan to build search/create/browse tool for maintaining consistent directives

**Validation Strategy**: Process is being tested on the `ctrack` project (credit card transaction import tool). Learnings feed back to improve guardrails.

**Next Planned Tools**:
- Directive library (search/create/browse)
- Story generator (compose stories from partials + specifics)
- Enhanced session capture tooling

## Working with This Repository

### When Adding New Phases/Roles/Modes

1. Create markdown file in appropriate `partials/` subdirectory
2. Keep descriptions concise - these will be embedded in generated stories
3. Focus on constraints and expectations, not generic advice

### When Creating Story Templates

1. Study existing examples in `manual/stories/`
2. Include both Generic (reusable) and Specific (story-unique) sections
3. Embed phase constraints and story-type workflows
4. Specify expected artifacts and definition of done in Specific section

### When Writing Inspection Reports

Use the format from `iterations/first/process_docs/inspection_report_1.md`:
- Issue ID with severity/category
- Description, root cause, discussion outcome
- Proposed resolution with status and priority
- Summary of actions required section

### Session Transcript Commits

When committing session transcripts:
- Place in `iterations/` with descriptive subdirectory
- Include related artifacts (inspection reports, generated stories)
- Transcript serves as audit trail for design decisions

## Important Notes

- This is meta-process work: building a process to guide AI agents in building software
- The process is self-referential: it will be developed using itself ("dogfooding")
- Most work involves document refinement, not traditional coding
- The goal is context efficiency: maximum constraint with minimum token usage
- Fast iteration cycles are valued: the lead developer prefers multiple small changes over large batches
- The ctrack project serves as the test bed for validating this process
