from dataclasses import dataclass

TEST_INPUT = """noop
addx 3
addx -5"""


@dataclass
class Cpu:
    x: int = 1
    cycle: int = 0
    signal_strength: int = 0

    def addx(self, x: int) -> None:
        self._cycle()
        self._cycle()
        self.x += x

    def noop(self) -> None:
        self._cycle()

    def _cycle(self):
        self.cycle += 1
        if self.cycle in range(20, 221, 40):
            self.signal_strength += self.cycle * self.x


def main():

    with open("inputs/day10.txt") as f:
        inp = f.read().splitlines()

    print(f"Part 1: {p1(inp)}")


def p1(inp: list[str]) -> int:

    cpu = Cpu()

    for line in inp:
        if line.startswith("addx"):
            cpu.addx(int(line.split(" ")[-1]))
        elif line.startswith("noop"):
            cpu.noop()
        else:
            raise ValueError("Wrong instruction")

    return cpu.signal_strength


if __name__ == "__main__":
    main()
