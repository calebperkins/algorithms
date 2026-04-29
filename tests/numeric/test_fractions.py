from algorithms.numeric.fractions import pretty_print


def test_pretty_print_whole_numbers():
    assert pretty_print(100, 2) == "50"


def test_pretty_print_nonperiodic_fractions():
    assert pretty_print(1, 4) == "0.25"
    assert pretty_print(1, 8) == "0.125"


def test_pretty_print_periodic_fractions():
    assert pretty_print(1, 3) == "0.(3)"
    assert pretty_print(3227, 555) == "5.8(144)"
