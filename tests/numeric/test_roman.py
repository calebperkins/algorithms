from algorithms.numeric.roman import to_roman


def test_numerals():
    assert "I" == to_roman(1)
    assert "VIII" == to_roman(8)
    assert "IV" == to_roman(4)
    assert "VII" == to_roman(7)
    assert "XV" == to_roman(15)
    assert "MMXIV" == to_roman(2014)
    assert "MCMLIV" == to_roman(1954)
