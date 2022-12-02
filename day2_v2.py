TEST_INP = """A Y
B X
C Z""".splitlines()


def play_round(computer: int, player: int) -> int:
    """Play a round and return the score obtained from the round"""

    # player gets extra points based on what he plays
    # regardless of the game outcome
    player_point = player + 1

    if (computer + 1) % 3 == player:
        # player won
        return player_point + 6
    elif computer == player:
        # draw
        return player_point + 3
    else:
        # computer won
        return player_point


def numericise(play: str) -> int:
    """Convert the letter played to a number representation"""

    nums = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}
    return nums[play]


def part1(inp):

    total_score = 0
    for round in inp:
        # transform hands to a number
        computer, player = round.split(" ")
        total_score += play_round(numericise(computer), numericise(player))

    return total_score


def part2(inp):

    raise Exception("Part 2 does not work :(")

    total_score = 0
    for round in inp:
        computer, strategy = round.split(" ")
        if strategy == "Y":
            # draw, we play computer 2x because we will anyway transform to numbers
            total_score += play_round(numericise(computer), numericise(computer))
        elif strategy == "X":
            # lose
            # A Y
            # B X --> X    1 0
            pass

        elif strategy == "Z":
            # win
            pass

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
