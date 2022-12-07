from __future__ import annotations
from dataclasses import dataclass

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


@dataclass
class File:
    name: str
    size: int


def main():

    with open("inputs/day7.txt") as f:
        s = f.read()

    commands = parse_commands(s)
    all_dirs = make_dir_structure(commands)

    print(f"Part 1: {p1(all_dirs)}")
    print(f"Part 2: {p2(all_dirs)}")


def parse_commands(s: str) -> list[str]:
    return [x.split("\n") for x in s.split("$ ") if x != ""]


def p1(dirs: list[Dir]):
    total_size = 0
    for dir in dirs:
        size = get_total_size(dir)
        if size <= 100000:
            total_size += size

    return total_size


def p2(dirs: list[Dir]):
    available_size = 70000000 - get_total_size(dirs[0])
    min_req_size = 30000000 - available_size
    all_applicable = []
    for dir in dirs:
        size = get_total_size(dir)
        if size >= min_req_size:
            all_applicable.append(size)
    return min(all_applicable)


def get_total_size(obj: Dir | File) -> int:
    if isinstance(obj, File):
        return obj.size
    else:
        return sum(get_total_size(c) for c in obj.children)


def make_dir_structure(commands: list[str]) -> list[Dir]:

    curr_dir = Dir("/", None, [])
    all_dirs = [curr_dir]

    for command in commands[1:]:
        cmd, result = command[0], [c for c in command[1:] if c != ""]

        if cmd.startswith("cd"):
            curr_dir = cd(cmd, curr_dir) or all_dirs[0]
        elif cmd.startswith("ls"):
            ls(curr_dir, result, all_dirs)

    return all_dirs


def cd(cmd, curr_dir: Dir) -> Dir:
    name = cmd.split(" ")[1]
    if name != "..":
        return _find_d(curr_dir.children, name)
    if curr_dir.parent is not None:
        return curr_dir.parent
    return None


def _find_d(lst: list[Dir], name: str) -> Dir:
    for d in lst:
        if d.name == name:
            return d


def ls(curr_dir: Dir, objects: list[str], all_dirs: list[Dir]):
    for obj in objects:
        size, name = obj.split(" ")
        if size == "dir":
            d = Dir(name, curr_dir, [])
            all_dirs.append(d)
            curr_dir.children.append(d)
        else:
            f = File(name, int(size))
            curr_dir.children.append(f)


if __name__ == "__main__":
    main()
