
## Overview

This development process combines some elements of well known processes such as scrum and common tools such as kanban 
but with modifications and extensions that are tuned to allow a senior developer to guide AI coding agents to produce
work according to a specific model that does not precisely match existing models.

The motivation for building this is the common problem that agentic coding processes just plain do too much, and if
the driver (human user of the tools) does not work very hard at instructing the agent to do exactly this and not any 
of that, then much of the code produced is not only not useful, but it is actually harmful. It is harmful for two reasons.
First, the volume of code produced makes it onerous to inspect in detail, costing so much time that it is often quicker 
to write it yourself. Second, it is often hard to get the LLM to discard any undesirable elements of the new code or 
unlearn the wrong lesson learned from the last prompt without dicarding the whole context.

After a number of unsatisfactory experiments in reducing this agrivating waste of my time and money, I reached the 
conclusion that, for me at least, the problem with the common approach is not granular enough and the iterations
cover too much change. I am a fast coder, and I use very small iterations over very little change, commonly completing
several edit/run cycles per minute. My mind works best in this mode, and I tend to get overwhelmed by the volume
of agentic output and lose effectiveness in the oversight role.

This process is therefore focused on guiding agentic workers primarily with constraints in order to reduce
the scope of each pass of the prompt/response cycle.


## Constraints

There is a conceptual framework (see the foundations\_concept\_summary.md file) that helps humans remember
the terms used to label the concepts. 


agentic tool does. 



## Controlling Context

I assert that the best results an agentic coding assistant can deliver are achieved more through context management
than prompt design. Promt design impacts context, of course, but the context is greater than the prompt.

These methods

## Scrum and not Scrum

Scrum practice is focused on the interactions of teams of humans, so much of it is not relevant to individuals
with agentic assistance. Most of what this process borrows from Scrum is:

1. The way activities are tuned to be performed by certain roles
2. The artifacts that are used to coordinate the activities of the roles
3. The iterative approach to pursuing objectives.

## Kanban plus

A kanban like method is used for tracking stories and tasks, with a couple of extensions:

1. Stories and Tasks can be "retired", meaning that some work was completed but a change of direction rendered the Story or Task irrelevant. The value of this is realized only when writing retrospective reports, informing readers of dead ends, wild goose chases, things that turned out to be too expensive, etc. 
2. Stories and Tasks can be "discarded", meaning that some new understanding has revealed that this activity is not actually desirable. This preserves knowledge of the dead branches of thinking about the project so future planning can avoid repeating the error.

## Extended Story flavors

|  **Story Type Name** | **Focus** | **Typical task types** |
|-------|----------------|----------------|
| **Study** |  Answering questions about problem space and possible solution options | Spikes |
| **Pathfinder** |  Protoyping components and their interactions | fast, cheap component experiements, simple hardwire integrations |
| **Forming** |  Converting protoype components into preliminary permanent forms and integrations | data and process component design, code and test |
| **User** | User interactions | ui component design, code and test |
| **Compliance** | Meeting standards for code coverage, documentation, UI style guide, support for configuration, monitoring, error reporting, etc. | Almost any type |

---


## Actor Roles

|  **Role Name** | **Focus** |
|-------|----------------|----------------|
| **coder** |  Writes code and simple tests |
| **planner** |  Breaks down higher level goals into lower ones, e.g. creating tasks to complete a story |
| **code_reviewer** | Reviews changes for compliance with the standards and constraints of the current phase |
| **test_developer** | Plans and builds tests that approach the tasks from a top (story) down perspective rather than a code centric perspective as used in TDD.
| **reporter** | Records information about process execution, human feedback and compiles reports |

---







