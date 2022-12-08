TEST_INPUT = """30373
25512
65332
33549
35390"""


def main() -> None:
    with open("inputs/day8.txt") as f:
        inp = f.read()

    trees = [[int(i) for i in line] for line in inp.splitlines()]

    num_visible = 0
    scenic_scores = []
    for y, row in enumerate(trees):
        for x, tree in enumerate(row):
            score_r = []
            score_l = []
            score_d = []
            score_u = []
            r = look_right(tree, x, y, trees, score_r)
            l = look_left(tree, x, y, trees, score_l)
            d = look_down(tree, x, y, trees, score_d)
            u = look_up(tree, x, y, trees, score_u)
            if any([r, l, d, u]):
                num_visible += 1
            scenic_scores.append(
                sum(score_r) * sum(score_l) * sum(score_u) * sum(score_d)
            )

    print("Part 1: ", num_visible)
    print("Part 2: ", max(scenic_scores))


def look_right(
    target: int, x: int, y: int, trees: list[list[int]], score: list[int]
) -> bool:
    """Check if target tree is bigger than all trees on the right
    Also append 1 to the score for every tree that is smaller + one for last seen tree"""
    try:
        if trees[y][x + 1] >= target:
            score.append(1)
            return False
        else:
            score.append(1)
            return look_right(target, x + 1, y, trees, score)
    except IndexError:
        return True


def look_left(
    target: int, x: int, y: int, trees: list[list[int]], score: list[int]
) -> bool:
    """Check if target tree is bigger than all trees on the left
    Also append 1 to the score for every tree that is smaller + one for last seen tree"""
    if x <= 0:
        return True
    if trees[y][x - 1] >= target:
        score.append(1)
        return False
    score.append(1)
    return look_left(target, x - 1, y, trees, score)


def look_down(
    target: int, x: int, y: int, trees: list[list[int]], score: list[int]
) -> bool:
    """Check if target tree is bigger than all trees downwards
    Also append 1 to the score for every tree that is smaller + one for last seen tree"""
    try:
        if trees[y + 1][x] >= target:
            score.append(1)
            return False
        else:
            score.append(1)
            return look_down(target, x, y + 1, trees, score)
    except IndexError:
        return True


def look_up(
    target: int, x: int, y: int, trees: list[list[int]], score: list[int]
) -> bool:
    """Check if target tree is bigger than all trees upwards
    Also append 1 to the score for every tree that is smaller + one for last seen tree"""
    if y <= 0:
        return True
    if trees[y - 1][x] >= target:
        score.append(1)
        return False
    score.append(1)
    return look_up(target, x, y - 1, trees, score)


if __name__ == "__main__":
    main()
