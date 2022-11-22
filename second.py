def double_power(current_powers: list) -> list:
    res = []
    for numb in current_powers:
        numb *= 2
        res.append(numb)
    return res
print(double_power([34, 40, 27]))
