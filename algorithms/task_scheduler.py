from collections import defaultdict, deque
from dataclasses import dataclass


@dataclass
class Task:
    name: str
    duration: int
    dependencies: list[str]  # names of tasks that must run first


def schedule(tasks: list[Task]) -> list[str]:
    """
    Return task names in a valid execution order.
    Raise ValueError if a cyclic dependency exists.
    """
    dependencies = defaultdict(set)
    dependants = defaultdict(set)
    for t in tasks:
        dependencies[t.name] = set(t.dependencies)
        for tt in t.dependencies:
            dependants[tt].add(t.name)

    # contains tasks with no dependencies
    ready: deque[str] = deque()

    for t in tasks:
        if not dependencies[t.name]:
            ready.append(t.name)

    output = []
    while ready:
        t = ready.popleft()

        output.append(t)

        for succ in dependants[t]:
            dependencies[succ].remove(t)
            if not dependencies[succ]:
                ready.append(succ)

    if len(output) < len(tasks):
        raise ValueError("cycle detected")

    return output
