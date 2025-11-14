# Meta-Project Relationship: ctrack ↔ guardrails

## Overview

This ctrack project serves a **dual purpose**:

1. **Primary Purpose:** Credit card transaction import tool for GnuCash
2. **Secondary Purpose:** Testbed for developing the "guardrails" process framework

The guardrails project is a separate repository focused on building a constraint-driven process framework for guiding AI coding agents. This ctrack project is being used to develop, test, and refine that process before generalizing it.

## Why This Relationship Exists

The lead developer is using ctrack as a **real-world proving ground** for process design because:

1. **Actual complexity** - ctrack has real technical challenges (UI framework selection, state machine workflow, GnuCash integration)
2. **Active development** - The project is in active use, providing genuine tasks to test against
3. **Low stakes** - Personal project, so process experiments don't risk production systems
4. **Dogfooding** - Using the process to build the process validates it works in practice

## How It Works

### Development Flow

```
┌─────────────────────────────────────────────────────┐
│  ctrack repo (this project)                         │
│                                                      │
│  1. Process artifacts created here:                 │
│     - Story definitions (process_docs/stories/)     │
│     - Task files (process_docs/tasks/)              │
│     - Enhancement tools (scripts/process_tools/)    │
│     - Inspection reports (process_docs/*)           │
│                                                      │
│  2. Session transcripts captured and committed      │
│     - Discussions about process design              │
│     - Tool design conversations                     │
│     - Process refinement sessions                   │
│                                                      │
│  3. Process tested on real ctrack work              │
│     - Study stories (e.g., file picker evaluation)  │
│     - Pathfinder stories (UI prototyping)           │
│     - Forming stories (production implementation)   │
│                                                      │
└─────────────────────────────────────────────────────┘
                        │
                        │ Lessons learned, refined artifacts
                        ▼
┌─────────────────────────────────────────────────────┐
│  guardrails repo (separate project)                 │
│                                                      │
│  - Generalized process definitions                  │
│  - Story/task generators                            │
│  - Process tools (directive library, etc.)          │
│  - Documentation and examples                       │
│  - May become distributable package/MCP server      │
│                                                      │
└─────────────────────────────────────────────────────┘
```

### Artifact Migration

Process artifacts developed in ctrack are **copied/adapted** to guardrails once validated:

- Story templates → Generalized for any project
- Tool prototypes → Productized with proper CLI/API
- Process documentation → Formalized and extended
- Session transcripts → Mined for insights and examples

## What This Means for AI Sessions

### When Working on ctrack Tasks

If you see references to:
- Process stories (in `process_docs/stories/`)
- Task definitions following specific templates
- Tools for generating stories or tasks
- Enhancement workflows with JSON interchange

**These are process development artifacts**, not ctrack application code.

### If Confused About Project Scope

Ask: "Is this work for the ctrack application itself, or for the process framework development?"

The answer will clarify which mental model to use.

## Key Insight

This is **process development using the process itself** (dogfooding). When you see process-related work in this ctrack repo, you're witnessing the zero-to-one stage of guardrails development. The fact that it's working on a real project (ctrack) validates the process design.

## Future State

Eventually:
1. guardrails becomes a standalone project with published tools
2. ctrack uses guardrails as a dependency/framework
3. This meta-relationship dissolves (normal user-of-framework relationship)
4. New projects can adopt guardrails without this dual-purpose confusion

But for now, **ctrack is the laboratory where guardrails is being invented.**
