import pytest

from algorithms.task_scheduler import Task, critical_path, schedule


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


def test_critical_path():
    tasks = [
        Task("install_deps", 5, []),
        Task("compile", 10, ["install_deps"]),
        Task("test", 8, ["compile"]),
        Task("package", 3, ["compile"]),
        Task("deploy", 2, ["test", "package"]),
    ]
    assert critical_path(tasks) == 25


def test_critical_path_again():
    tasks = [
        Task("A", 10, []),
        Task("B", 1, []),
        Task("C", 1, ["B"]),  # C can start at t=1
        Task("D", 1, ["A", "C"]),  # D starts at t=10, finishes at t=11
    ]
    assert critical_path(tasks) == 11
