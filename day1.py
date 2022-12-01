TEST_STR = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""


def prepare_lst(str: str) -> list[list[int]]:
    """Convert str to a list of lists by creating new lists for every double newline"""
    return [[int(i) for i in part.split("\n")] for part in str.split("\n\n")]


def part1(lst: list) -> int:
    """Return the max sum of the sublists in lst"""
    return max(sum(el) for el in lst)


def part2(lst: list) -> int:
    """Return the total sum of the sum of the three largest sublists"""
    largest_three = sorted((sum(el) for el in lst))[-3:]
    return sum(largest_three)


def main():

    with open("inputs/day1.txt") as f:
        str = f.read()[:-2]  # trim ending newline

    prepared_list = prepare_lst(str)

    part1_sol = part1(prepared_list)
    print(f"Part 1: {part1_sol}")

    part2_sol = part2(prepared_list)
    print(f"Part 2: {part2_sol}")


if __name__ == "__main__":
    main()
