TEST_INPUT = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".splitlines()


def main():

    head = [0, 0]
    tail = [0, 0]

    with open("inputs/day9.txt") as f:
        inp = f.read().splitlines()

    for row in TEST_INPUT:
        direction, n = row.split(" ")
        for _ in range(int(n)):
            # display([head, tail], 10, 10)
            print(head)
            move_head(direction, head)
            move_tail(direction, tail, head)


def absdiff(head, tail):
    return abs(head[0] - tail[0]), abs(head[1] - tail[1])


def diff(head, tail):
    return (head[0] - tail[0]), (head[1] - tail[1])


def move_head(direction, knot):
    if direction == "L":
        knot[0] -= 1
    elif direction == "R":
        knot[0] += 1
    elif direction == "U":
        knot[1] += 1
    elif direction == "D":
        knot[1] -= 1
    else:
        raise ValueError("Invalid direction")


def display(knots, x=6, y=5):
    lst = [["." for _ in range(x)] for _ in range(y)]

    h_x, h_y = knots[0]
    t_x, t_y = knots[1]

    lst[h_y][h_x] = "H"
    lst[t_y][t_x] = "T"

    for row in lst:
        print("".join(row))


def move_tail(direction, knot, head):
    ad_x, ad_y = absdiff(head, knot)
    d_x, d_y = diff(head, knot)
    if ad_x < 2 and ad_y < 2:
        pass
    elif ad_x == 0 or ad_y == 0:
        move_head(direction, knot)
    elif d_x == 2:
        knot[0] -= 1
        knot[1] += 1
    elif d_x == -2:
        knot[0] -= 1
        knot[1] += 1
    elif d_y == 2:
        knot[0] += 1
        knot[1] += 1
    elif d_y == -2:
        knot[0] -= 1
        knot[1] -= 1


if __name__ == "__main__":
    main()
