from dataclasses import dataclass, field
from os import system
from time import sleep

TEST_INPUT = """noop
addx 3
addx -5"""

CRT_WIDTH = 40
CRT_HEIGHT = 6


def _gen_lst():
    return [["." for _ in range(CRT_WIDTH)] for _ in range(CRT_HEIGHT)]


@dataclass
class Cpu:
    x: int = 1
    cycle: int = 0
    signal_strength: int = 0
    screen: list[int] = field(default_factory=_gen_lst)

    def addx(self, x: int) -> None:
        self._cycle()
        self._cycle()
        self.x += x

    def noop(self) -> None:
        self._cycle()

    def _cycle(self):
        self.draw_pixel()
        self.cycle += 1
        if self.cycle in range(20, 221, 40):
            self.signal_strength += self.cycle * self.x

    def draw_pixel(self):
        col = self.cycle // 40
        row = self.cycle - col * 40

        pixel = "."
        if self.x in (row - 1, row, row + 1):
            pixel = "#"

        self.screen[col][row] = pixel

    def display(self):
        for row in self.screen:
            print(("").join(row))

    def execute_instruction(self, instruction: str) -> None:
        if instruction.startswith("addx"):
            self.addx(int(instruction.split(" ")[-1]))
        elif instruction.startswith("noop"):
            self.noop()
        else:
            raise ValueError("Wrong instruction")

    def execute_instructions(
        self, instructions: list[str], display: bool = False, sleep_s: int = 0
    ) -> None:
        for instruction in instructions:
            self.execute_instruction(instruction)

            if display:
                self.display()
                sleep(sleep_s)
                system("clear")


def main():

    with open("inputs/day10.txt") as f:
        inp = f.read().splitlines()

    print(f"Part 1: {p1(inp)}")
    p2(inp)


def p2(inp: list[str]) -> None:
    cpu = Cpu()
    cpu.execute_instructions(inp, display=True, sleep_s=0.1)
    cpu.display()


def p1(inp: list[str]) -> int:

    cpu = Cpu()

    cpu.execute_instructions(inp)

    return cpu.signal_strength


if __name__ == "__main__":
    main()
