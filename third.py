def checkio(number):
    number = str(number)
    res = 1
    for x in number:
        if x == '0':
          x = 1
        res *= int(x)

    return res

print(checkio(20670))
