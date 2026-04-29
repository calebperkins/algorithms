def pretty_print(dividend: int, divisor: int) -> str:
    """
    Prints dividend/divisor as a decimal. Puts the repeating part in paranthesis.
    """
    assert divisor != 0

    tokened_dividend = [int(d) for d in str(dividend)]
    integral_part: list[str] = []
    q = 0
    r = 0

    for digit in tokened_dividend:
        r = r * 10 + digit
        q, r = divmod(r, divisor)
        # avoid printing a leading zero
        if q == 0 and r > 0:
            continue
        integral_part.append(str(q))

    # no decimals, print a whole number
    if (q, r) == (0, 0):
        return "".join(integral_part)

    # if the answer is less than 1, include a leading zero
    if not integral_part:
        integral_part.append("0")

    fractional_part = []

    seen: list[tuple[int, int]] = []

    while True:
        r = r * 10
        q, r = divmod(r, divisor)

        if (q, r) == (0, 0):
            break

        if (q, r) in seen:
            # place the opening bracket before the location of (q, r)
            period_starts = seen.index((q, r))
            fractional_part.insert(period_starts, "(")
            fractional_part.append(")")
            break

        seen.append((q, r))
        fractional_part.append(str(q))

    return "".join(integral_part + ["."] + fractional_part)
