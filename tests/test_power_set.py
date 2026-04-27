from algorithms.power_set import power_set


def test_power_set():
    s = [1, 2, 3]
    ps = list(power_set(s))
    assert ps == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
