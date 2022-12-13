from __future__ import annotations
from dataclasses import dataclass
from os import system
from time import sleep

TEST_INPUT = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

TEST_INPUT_2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


def diff(head: Knot, tail: Knot):
    return head.x - tail.x, head.y - tail.y


@dataclass
class Knot:
    x: int
    y: int

    def move_1(self, direction: str) -> tuple(str, tuple(int, int)):
        prev_pos = self.x, self.y

        if direction == "L":
            self.x -= 1
        elif direction == "R":
            self.x += 1
        elif direction == "U":
            self.y -= 1
        elif direction == "D":
            self.y += 1
        else:
            raise ValueError("Invalid direction")
        return (direction, prev_pos)

    def move_tail(self, head: Knot, head_dir: str, head_prev_pos):
        d = diff(head, self)
        if d[0] in range(-1, 2) and d[1] in range(-1, 2):
            # adjacent, don't move
            pass
        elif head.x == self.x or head.y == self.y:
            # in same row
            self.move_1(head_dir)
        else:
            # diagonal => move to prev pos of head
            self.x, self.y = head_prev_pos


def show(head: Knot, tail: Knot, x: int = 6, y: int = 5, sleep_s: int = 0):
    for _y in range(y):
        for _x in range(x):
            if tail.x == _x and tail.y == _y:
                print("T", end="")
            elif head.x == _x and head.y == _y:
                print("H", end="")
            else:
                print(".", end="")
        print()
    sleep(sleep_s)


def main():

    with open("inputs/day9.txt") as f:
        inp = f.read()

    p1_sol = p1(TEST_INPUT)
    print(f"Part 1: {p1_sol}")
    print(p2(TEST_INPUT))


def show(knots: list[Knot], x: int = 6, y: int = 5, sleep_s: int = 0):
    for _y in range(y):
        for _x in range(x):
            to_show = []
            for i, knot in enumerate(knots):
                if knot.x == _x and knot.y == _y:
                    to_show.append(i)

            if to_show[-1] == 0:
                print("T", end="")
            elif to_show[-1] == 1:
                print("H", end="")
            elif len(to_show) > 0:
                print(str(to_show[-1]), end="")
            else:
                print(".", end="")
        print()
    sleep(sleep_s)


def p1(inp, visualise: bool = False) -> int:

    # arbitrary starting position
    head = Knot(0, 4)
    tail = Knot(0, 4)

    all_visited = {(tail.x, tail.y): True}

    for move in inp.splitlines():
        direction, n = move.split(" ")
        for _ in range(int(n)):
            head_dir, head_prev_pos = head.move_1(direction)
            tail.move_tail(head, head_dir, head_prev_pos)
            if not all_visited.get((tail.x, tail.y)):
                all_visited[(tail.x, tail.y)] = True

            if visualise:
                # system("clear")
                show(head, tail, 6, 5)

    return len(all_visited)


def p2(inp: str) -> int:

    knots = [Knot(0, 0) for _ in range(10)]

    all_visited = {(knots[0].x, knots[0].y): True}

    for move in inp.splitlines():
        direction, n = move.split(" ")
        for _ in range(int(n)):
            head = knots[-1]
            tail = knots[-2]
            head_dir, head_prev_pos = head.move_1(direction)
            tail.move_tail(head, head_dir, head_prev_pos)

            if not all_visited.get((knots[0].x, knots[0].y)):
                all_visited[(knots[0].x, knots[0].y)] = True

            for i in range(8, -1, -1):
                head = knots[i]
                tail = knots[i - 1]

                head_dir, head_prev_pos = head.move_1(direction)
                tail.move_tail(head, head_dir, head_prev_pos)

                if not all_visited.get((knots[0].x, knots[0].y)):
                    all_visited[(knots[0].x, knots[0].y)] = True

                show_all(knots)

    return len(all_visited)


def show_all(knots, x: int = 6, y: int = 5, sleep_s: int = 0) -> None:

    for i, knot in enumerate(knots):
        if i == 0:
            k = "T"
        elif i == len(knots) - 1:
            k = "H"
        else:
            k = str(i)

        for _y in range(y):
            for _x in range(x):
                if knot.x == _x and knot.y == _y:
                    print(k, end="")
                else:
                    print(".", end="")
            print()
    sleep(sleep_s)


if __name__ == "__main__":
    main()
