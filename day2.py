TEST_INP = """A Y
B X
C Z""".splitlines()

RULES = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3,
}

TRANSFORMATIONS = {
    "A X": "A Z",
    "A Y": "A X",
    "A Z": "A Y",
    "B X": "B X",
    "B Y": "B Y",
    "B Z": "B Z",
    "C X": "C Y",
    "C Y": "C Z",
    "C Z": "C X",
}


def part1(inp):

    total_score = 0
    for round in inp:
        total_score += RULES[round]

    return total_score


def part2(inp):

    total_score = 0

    for round in inp:
        total_score += RULES[TRANSFORMATIONS[round]]

    return total_score


def main():

    with open("inputs/day2.txt") as f:
        inp = f.read().splitlines()

    part1_sol = part1(inp)
    print(f"Part 1: {part1_sol}")

    part2_sol = part2(inp)
    print(f"Part 2: {part2_sol}")


if __name__ == "__main__":
    main()
