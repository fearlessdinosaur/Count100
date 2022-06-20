def countFromXToY(min_number, max_number):
    numbers = ""
    for x in range(min_number, max_number + 1):
        val = ""
        if x % 3 == 0:
            val = val + "Three"
        if x % 5 == 0:
            val = val + "Five"
        if val == "":
            val = x
        numbers = numbers + str(val) + " "
    return numbers


if __name__ == '__main__':
    result = countFromXToY(1, 100)
    print(result)
