import pytest

from algorithms.task_scheduler import Task, schedule


def test_scheduling():
    tasks = [
        Task("install_deps", 5, []),
        Task("compile", 10, ["install_deps"]),
        Task("test", 8, ["compile"]),
        Task("package", 3, ["compile"]),
        Task("deploy", 2, ["test", "package"]),
    ]

    valid = ["install_deps", "compile", "test", "package", "deploy"]
    also_valid = ["install_deps", "compile", "package", "test", "deploy"]
    assert (schedule(tasks) == valid) or (schedule(tasks) == also_valid)


def test_cycle():
    tasks = [Task("a", 0, ["b"]), Task("b", 0, ["a"])]
    with pytest.raises(ValueError):
        schedule(tasks)
