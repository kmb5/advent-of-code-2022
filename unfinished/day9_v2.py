from __future__ import annotations
from dataclasses import dataclass
from time import sleep
from os import system

TEST_INPUT = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

TEST_2 = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""


@dataclass
class Knot:
    x: int
    y: int

    def diff(self, k: Knot):
        return abs(self.x - k.x), abs(self.y - k.y)

    def __str__(self):
        return f"{self.x},{self.y}"


def move_knot(knot: Knot, direction: str) -> tuple:
    prev_pos = (knot.x, knot.y)
    if direction == "L":
        knot.x -= 1
    elif direction == "R":
        knot.x += 1
    elif direction == "U":
        knot.y -= 1
    elif direction == "D":
        knot.y += 1
    else:
        raise ValueError("Invalid direction")

    return prev_pos


def move_tail(knot: Knot, head: Knot, head_prev_pos: tuple):
    prev_pos = (knot.x, knot.y)
    diff = knot.diff(head)
    if diff[0] <= 1 and diff[1] <= 1:
        # adjacent, don't move
        pass
    else:
        knot.x, knot.y = head_prev_pos

    return prev_pos


def p1():
    head = Knot(0, 0)
    tail = Knot(0, 0)

    all_visited = set(str(tail))
    show([head, tail])

    with open("inputs/day9.txt") as f:
        inp = f.read()

    for move in inp.splitlines():
        direction, n = move.split(" ")
        for _ in range(int(n)):
            head_prev_pos = move_knot(head, direction)
            move_tail(tail, head, head_prev_pos)

            if not all_visited.get((tail.x, tail.y)):
                all_visited[((tail.x, tail.y))] = True

            show([tail, head], 10, 10, sleep_s=0.2)
            system("clear")

    print(len(all_visited))


def p2():

    knots = [Knot(0, 0) for _ in range(10)]

    all_visited = set(str(knots[-1]))

    for move in TEST_2.splitlines():
        direction, n = move.split(" ")  # U, 2
        for _ in range(int(n)):
            head = knots[0]
            head_prev_pos = move_knot(head, direction)
            for i in range(1, 10):
                tail = knots[i]
                head_prev_pos = move_tail(tail, head, head_prev_pos)
                head = knots[i]
                print()
                # print()
                all_visited.add(str(knots[-1]))

            # show(knots, 50, 50, sleep_s=0.2)
            # system("clear")

    print(len(all_visited))


def show(knots: list[Knot], x: int = 6, y: int = 5, sleep_s: int = 0):
    for _y in range(y, -1, -1):
        for _x in range(x):
            to_show = []
            for i, knot in enumerate(knots):
                if knot.x == _x and knot.y == _y:
                    to_show.append(i)

            if not to_show:
                print(".", end="")
            elif to_show[-1] == 0:
                print("T", end="")
            elif to_show[-1] == len(knots) - 1:
                print("H", end="")
            else:
                print(str(to_show[0]), end="")
        print()
    sleep(sleep_s)


p2()
