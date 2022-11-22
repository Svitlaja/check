
def checkio(number):
    number = str(number)
    i = 1
    for x in number:
        x *= int(number[i])
        i = i + 1
        if i == len(number) + 1:
            break

        return x

print(checkio(17))
