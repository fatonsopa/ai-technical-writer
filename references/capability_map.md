# Capability Map (CM)

A capability map splits an initiative into capabilities that can be specified and shipped separately, and shows which ones depend on others. Write one when a broad initiative mixes several outcomes and a specification author needs to choose what to specify first. A single capability needs no map; specify it directly.

## Principles

- Name capabilities by what users can do, not by screens, services or code modules. A capability can span several surfaces, and one surface can serve several capabilities.
- Give each capability a stable ID and a one-line responsibility. Child specifications cite that ID, so keep it when the map changes.
- Record a dependency only when one capability can't deliver its outcome without another, and say why. Shared code or a convenient order isn't a dependency.
- Derive the build order from the dependencies. Capabilities with no unmet dependency can start in parallel; say so.
- If dependencies form a cycle, name the capabilities in it and hold their order until the cycle is resolved, for example by splitting a capability or changing a dependency.

## Structure

Start with the initiative and its source, then list the capabilities, their dependencies with reasons and the resulting build order. Note open questions. Each child specification cites the capability ID it implements.

## Template

```md
# [Initiative] capability map

## Initiative
[Outcome and the brief, product document or request it comes from.]

## Capabilities
| ID | Capability | Responsibility |
| --- | --- | --- |
| [CAP-1] | [What users can do] | [What it owns and excludes] |

## Dependencies
| Capability | Depends on | Reason |
| --- | --- | --- |
| [CAP-3] | [CAP-2] | [Why it can't deliver without it] |

## Build order
[What can start now, in parallel, and what waits for what. Any cycle and the order it holds.]

## Open questions
- [Undecided boundary or dependency, and who decides.]
```

## Completed example

Read the [Capability Map (CM) example for Websites Review](../examples/capability_map.md). It shows two independent starting capabilities and one that depends on another.

## Quality check

Can a specification author pick one capability, see what it owns and know whether it can start now? Check that every dependency has a reason, the order follows from the dependencies and no capability is named after a screen or service.

## Sources

- [Martin Fowler: Capability-oriented boundaries](https://martinfowler.com/articles/break-monolith-into-microservices.html)
