## Purpose

To achieve **extreme speed in producing useful code**, a primary skill is **good balance** between:

* getting something done *fast enough* to move the project forward as soon as possible, and  
* building something *so good* that there is never any need to rewrite it.

It is possible to use a conceptual model to help **think and communicate clearly** about what constitutes the **“right” balance** for a particular part of a particular project at a particular time — and the variables along each of those dimensions that help identify what is “right”. This 
can help a developer take the most useful intentional stance for the current need.

The **conceptual framework** framework described here analogizes the way Westerners established their presence in North America to the 
process of developing concrete software results in the landscape of possible solutions. The phases are:

> **exploring → pioneering → settling → fortifying → re-founding**

Each phase is named with a **gerund** so that we can speak naturally about the *current stance* of development: 
> “We are **fortifying** the matcher subsystem.”

For more discussion, see foundation_concept.md

## Phase Definitions

| **Phase** | **Frontier Image** | **Software Stance** | **Ship-able code** |
|-------|----------------|----------------|------|
| **Exploring** | Scout mapping rivers & passes | Study Stories, Throw-away spikes, REPL experiments, “what if?” scripts | None |
| **Pioneering** | Lone family clearing a homestead | Minimal focused, partial, components on simplified data | None |
| **Settling** | Cluster of families + shared barn/mill | Enough internal API structure to rough out end to end, persistence, integration tests | probably not |
| **Fortifying** | Fort for defense, stores and other services, docks and rail stations | Well structured internal APIs, coherent readable code, configuration support, logging, error management, functionally complete   | Yes |
| **Re-Founding** | City infrastructure such as water, police, roads, major services | Extensions for flexibility, upgrade APIs and documentation for external integrations, upgrades to handle versioning of external formats and APIs, publishing | Yes |

---

## Story Definitions

|  **Story Type Name** | **Focus** | **Typical task types** |
|-------|----------------|----------------|
| **Study** |  Answering questions about problem space and possible solution options | Spikes |
| **POC** | enough code to demo key solutions, very short term | POC functions, classes | 
| **Framing** | Establish early component boundaries, mostly short term | Simple functions and classes, very basic tests |
 |
| **Glueing** | Scaffoling interagration to support early components | lots of hardcoding, much of it in temporary tests |
| **Anchoring** | Improving components to solidify APIs and primary logic to production level | Survivable APIs, well factored classes, data definitions, heavy testing through integration tests |
| **Joining** | Improving integrations | Integration layer components, Heavy testing with zero or minimal mocking, Early docs, especially docstrings |
| **User** | User interactions | ui component design, code and test |
| **Compliance** | Meeting standards for code coverage, documentation, UI style guide, support for configuration, monitoring, error reporting, etc. | Almost any type |

---

## Example: Credit-Card → GnuCash Automation Tool

### Exploring
* Wrote quick scripts to export CSV → spreadsheet.
* Experimented with bookkeeping tools; discovered **piecash**.
* Spiked pattern-matching on transaction descriptions.

### Pioneering
* Built four tiny components (account export, matcher rules, transaction import, file rewrite) that worked end-to-end on a toy file with 2 accounts and 2 transactions.

### Settling
* Replaced hard-coding with configuration.
* Introduced dataclasses, SQLAlchemy models, pytest integration tests.
* Created a catalog of coordinated CSV test sets.

### Fortifying
* Switched UI from LibreOffice Calc → **NiceGUI** single-page app.
* Added programmatic GnuCash import via piecash.
* Implemented validation, rollback, health checks, CI matrix.

### Re-Founding
* Extracted a **Flow sequencer** that orchestrates the wizard UI.
* Published internal contracts, versioned API, documentation.
* Packaged as a reusable PyPI module.

For more a more detailed discussion, see foundations_concept.md

---
