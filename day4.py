def p1():

    with open("inputs/day4.txt") as f:
        txt = f.read().splitlines()

    sum = 0
    for pair in txt:
        p1, p2 = pair.split(",")
        p1 = [int(x) for x in p1.split("-")]
        p2 = [int(x) for x in p2.split("-")]

        if (p1[0] >= p2[0] and p1[1] <= p2[1]) or ((p1[0] <= p2[0] and p1[1] >= p2[1])):
            # count if one is fully within range of the other
            sum += 1

    print(sum)


def p2():

    with open("inputs/day4.txt") as f:
        txt = f.read().splitlines()

    overlaps = 0
    for pair in txt:
        p1, p2 = pair.split(",")
        p1 = [int(x) for x in p1.split("-")]
        p2 = [int(x) for x in p2.split("-")]

        if [x for x in range(p1[0], p1[1] + 1) if x in range(p2[0], p2[1] + 1)]:
            # count if at least 1 element is overlapping
            overlaps += 1

    print(overlaps)


if __name__ == "__main__":
    p1()
    p2()
