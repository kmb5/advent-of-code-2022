import string


def p1():

    points = {letter: i + 1 for i, letter in enumerate(string.ascii_letters)}

    with open("inputs/day3.txt") as f:
        str = f.read().splitlines()

    sum = 0
    for line in str:
        firstpart, secondpart = line[: len(line) // 2], line[len(line) // 2 :]
        in_both = set(l for l in firstpart if l in secondpart)
        for l in in_both:
            sum += points[l]

    print(sum)


def p2():

    points = {letter: i + 1 for i, letter in enumerate(string.ascii_letters)}

    with open("inputs/day3.txt") as f:
        str = f.read().splitlines()

    sum = 0
    for l1i in range(0, len(str), 3):
        l1 = str[l1i]
        l2 = str[l1i + 1]
        l3 = str[l1i + 2]
        intrs = set.intersection(set(l1), set(l2), set(l3))

        for i in intrs:
            sum += points[i]

    print(sum)


if __name__ == "__main__":
    p1()
    p2()
