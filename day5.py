from collections import defaultdict
import re
import os
from time import sleep


def parse_input(inp: str) -> tuple:
    """Parse input to a separate variable for crates and instructions

    crates: dict[list]
        column index as key and list of crates as value (topmost crate at the end of the list)
    instructions: list[str]
        a list of each instruction as a string
    """
    crates, instructions = inp.split("\n\n")

    instructions = instructions.splitlines()
    crates_dct = defaultdict(list)

    for row in crates.splitlines()[:-1]:
        # -1 because we don't need last row (which has the column numbers)

        # split to sublists of 4 characters
        # because its either 4 empty spaces or eg. [A] (3 characters + space at end)
        spl = [row[i : i + 4] for i in range(0, len(row), 4)]

        for i, elem in enumerate(spl):
            cleaned = elem.replace(" ", "").replace("[", "").replace("]", "")
            if cleaned:
                crates_dct[i + 1].insert(0, cleaned)

    return crates_dct, instructions


def handle_instruction(
    instruction: str, crates: dict[list], reverse: bool
) -> dict[list]:
    """Handle a single instruction by modifying crates in place
    If reverse is True, crates will be moved in bulk, otherwise one by one"""

    # remove anything except digits and convert to int
    n, frm, to = [int(x) for x in re.findall(r"\b\d+\b", instruction)]

    # move n elements from the end
    moved = crates[frm][-1 : -(n + 1) : -1]

    # remaining is everything until the n-th element counted from the end of the list
    remaining = crates[frm][:-n]
    crates[frm] = remaining

    if reverse:
        crates[to].extend(reversed(moved))
    else:
        crates[to].extend(moved)


def assemble_message(crates: dict[list]) -> str:
    """Assemble a message by taking the topmost crate's letter for each column"""
    msg = ""
    for i in range(len(crates)):
        msg += crates[i + 1][-1]

    return msg


def p1(inp: str) -> str:
    crates, instructions = parse_input(inp)

    for instruction in instructions:
        os.system("clear")
        visualise_crates(crates)
        sleep(0.03)
        handle_instruction(instruction=instruction, crates=crates, reverse=False)

    os.system("clear")
    visualise_crates(crates)
    return assemble_message(crates)


def p2(inp: str) -> str:
    crates, instructions = parse_input(inp)

    for instruction in instructions:
        handle_instruction(instruction=instruction, crates=crates, reverse=True)

    return assemble_message(crates)


def visualise_crates(crates: dict[list]):

    crates = dict(crates)
    # print(crates)

    for i in range(0, 11):
        for j in range(0, 11):
            try:
                if 11 - i < 0:
                    raise IndexError
                chr = f"[{crates[j][11 - i]}]"
            except (KeyError, IndexError):
                chr = "   "
            print(chr, end=" ")
        print()

    print(" " + ("   ".join([str(i) for i in range(0, 10)])))


def main() -> None:

    with open("inputs/day5.txt") as f:
        inp = f.read()

    print(f"Part 1: {p1(inp)}")
    # print(f"Part 2: {p2(inp)}")


if __name__ == "__main__":
    main()
