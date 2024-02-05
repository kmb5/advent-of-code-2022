TEST_INPUT = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]"""


def main():

    with open("inputs/day13.txt") as f:
        inp = f.read().split("\n\n")

    print(f"Part 1 : {part1(inp)}")


def part1(inp: list) -> int:

    right_indices = []

    for i, lines in enumerate(inp):
        left, right = lines.split("\n")
        left = eval(left)
        right = eval(right)
        if compare_multiple(left, right):
            right_indices.append(i + 1)

    return sum(right_indices)


def compare_multiple(left: list, right: list):
    rng = max(len(left), len(right))

    for i in range(rng):
        try:
            l = left[i]
        except IndexError:
            return True

        try:
            r = right[i]
        except IndexError:
            return False

        comp = compare(l, r)
        if comp is not None:
            return comp

    return None


def compare(left: list | int, right: list | int) -> bool | None:

    t_l = type(left)
    t_r = type(right)
    if t_l == t_r == int:
        return left < right
    elif t_l == t_r == list:
        for 
    elif t_l == int:
        return compare_lists([left], right)
    elif t_r == int:
        return compare_lists(left, [right])


def _compare(l, r):
    if type(l) == list and type(r) == list:
        


def compare_ints(left: int, right: int) -> bool | None:
    try:
        if left == right:
            return None
        return left < right
    except Exception:
        print(left, right)


def compare_lists(left: list[int], right: list[int]) -> bool | None:
    rng = max(len(left), len(right))
    for i in range(rng):
        try:
            l = left[i]
        except IndexError:
            return True

        try:
            r = right[i]
        except IndexError:
            return False

        comp = compare_ints(l, r)
        if comp is not None:
            return comp

    return None


if __name__ == "__main__":
    main()
