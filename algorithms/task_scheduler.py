from collections import defaultdict, deque
from dataclasses import dataclass


@dataclass
class Task:
    name: str
    duration: int
    dependencies: list[str]  # names of tasks that must run first

    def __hash__(self) -> int:
        return hash(self.name)


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


def critical_path(tasks: list[Task]) -> int:
    """
    Return the minimum time to complete all tasks given unlimited parallelism.
    """
    by_id = {t.name: t for t in tasks}
    dependencies: dict[Task, set[Task]] = defaultdict(set)

    # the next set of tasks this can lead to
    dependants: dict[Task, set[Task]] = defaultdict(set)

    for t in tasks:
        dependencies[t] = {by_id[pred] for pred in t.dependencies}
        for pred in t.dependencies:
            dependants[by_id[pred]].add(t)

    # contains tasks with no unresolved dependencies
    ready: deque[Task] = deque([t for t in tasks if not dependencies[t]])

    # earliest time this task can finish
    earliest_finish: dict[Task, int] = {}

    while ready:
        t = ready.popleft()

        # earliest time it can finish = max finish time of all dependent tasks + this duration
        dependant_tasks = (by_id[pred] for pred in t.dependencies)
        earliest_finish[t] = (
            max((earliest_finish[tt] for tt in dependant_tasks), default=0) + t.duration
        )

        for succ in dependants[t]:
            dependencies[succ].remove(t)
            if not dependencies[succ]:
                ready.append(succ)

    if len(earliest_finish) < len(tasks):
        raise ValueError("cycle detected")

    return max(earliest_finish.values(), default=0)
