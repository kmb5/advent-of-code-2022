from __future__ import annotations
from dataclasses import dataclass
from pprint import pprint

TEST_STR = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
"""


@dataclass
class Dir:
    name: str
    parent: Dir
    children: list[Dir | File]
    size: int


@dataclass
class File:
    name: str
    size: int


def main():

    with open("inputs/day7.txt") as f:
        s = f.read()

    commands = parse_commands(TEST_STR)

    dirs = make_dir_structure(commands)

    p1_sol = p1(dirs)
    print(f"Part 1: {p1_sol}")


def parse_commands(s: str) -> list[str]:
    return [x.split("\n") for x in s.split("$ ") if x != ""]


def p1(dirs: dict[str, Dir]):
    total_sum = 0
    for dirname in dirs:
        dir = dirs[dirname]
        size = get_total_size(dir)
        print(dirname, size)
        if size <= 100000:
            total_sum += size

    return total_sum


def get_total_size(obj: Dir | File) -> int:
    if isinstance(obj, File):
        return obj.size
    else:
        return sum(get_total_size(c) for c in obj.children)


def make_dir_structure(commands: list[str]) -> dict[str, Dir]:

    dirs = {"/": Dir("/", None, [])}
    curr_dir = dirs["/"]

    for command in commands[1:]:
        cmd, result = command[0], [c for c in command[1:] if c != ""]

        if cmd.startswith("cd"):
            curr_dir = cd(cmd, curr_dir, dirs)
        elif cmd.startswith("ls"):
            ls(curr_dir, result, dirs)

    return dirs


def cd(cmd, curr_dir: Dir, dirs: dict[str, Dir]) -> Dir:
    name = cmd.split(" ")[1]
    print(name)
    if name != "..":
        return dirs[name]
    if curr_dir.parent is not None:
        return curr_dir.parent
    return dirs["/"]


def ls(curr_dir: Dir, objects: list[str], dirs: dict[str, Dir]):
    for obj in objects:
        size, name = obj.split(" ")
        if size == "dir":
            d = Dir(name, curr_dir, [])
            dirs[name] = d
            curr_dir.children.append(d)
        else:
            f = File(name, int(size))
            curr_dir.children.append(f)


if __name__ == "__main__":
    main()
