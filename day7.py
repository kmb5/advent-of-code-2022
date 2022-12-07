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
    """Representation of a directory with
    an optional parent and a list of directories
    or files as children"""

    name: str
    parent: Dir | None
    children: list[Dir | File]


@dataclass
class File:
    """Representation of a file with a given size"""

    name: str
    size: int


def main():

    with open("inputs/day7.txt") as f:
        s = f.read()

    commands = parse_commands(s)
    all_dirs = make_dir_structure(commands)

    print(f"Part 1: {p1(all_dirs)}")
    print(f"Part 2: {p2(all_dirs)}")


def parse_commands(s: str) -> list[list[str]]:
    """Parse commands from input and return a list which contains commands.
    Each sublist is a command with the first element as the command itself and arguments afterwards"""
    return [x.split("\n") for x in s.split("$ ") if x != ""]


def p1(dirs: list[Dir]) -> int:
    """Solve part 1 by calculating the sum of
    total directory sizes that are <= 100000"""
    total_size = 0
    for dir in dirs:
        size = get_total_size(dir)
        if size <= 100000:
            total_size += size

    return total_size


def p2(dirs: list[Dir]) -> int:
    """Solve part 2 by getting the minimum space that needs to be cleared if
    the total space on the disk is 70000000 and we need to have 30000000 available"""
    available_size = 70000000 - get_total_size(dirs[0])
    min_req_size = 30000000 - available_size
    all_applicable = []
    for dir in dirs:
        size = get_total_size(dir)
        if size >= min_req_size:
            all_applicable.append(size)
    return min(all_applicable)


def get_total_size(obj: Dir | File) -> int:
    """Recursively get total size of a given object
    by going into each child in case of directories"""
    if isinstance(obj, File):
        return obj.size
    else:
        return sum(get_total_size(c) for c in obj.children)


def make_dir_structure(commands: list[str]) -> list[Dir]:
    """Create a list of all directories based on the input commands
    and make all connections between them"""

    curr_dir = Dir("/", None, [])  # always start with root dir
    all_dirs = [curr_dir]

    for command in commands[1:]:  # skip root dir command
        cmd, result = command[0], [c for c in command[1:] if c != ""]

        if cmd.startswith("cd"):
            # if cd returns none (= no parent dir), parent dir is root
            curr_dir = cd(cmd, curr_dir) or all_dirs[0]
        elif cmd.startswith("ls"):
            ls(curr_dir, result, all_dirs)

    return all_dirs


def cd(cmd: str, curr_dir: Dir) -> Dir | None:
    """Execute a cd command by traversing up or down the directory structure

    Returns None if we are trying to find the parent of the root directory"""
    name = cmd.split(" ")[1]
    if name != "..":
        # = going down (because only 2 cases are .. or {dirname})
        return _find_d(curr_dir.children, name)
    if curr_dir.parent is not None:
        # = going up
        return curr_dir.parent
    # no parent => we are in root
    return None


def _find_d(lst: list[Dir], name: str) -> Dir | None:
    """Helper function to find a given directory by its name"""
    for d in lst:
        if d.name == name:
            return d


def ls(curr_dir: Dir, objects: list[str], all_dirs: list[Dir]):
    """Go through list of objects and add them as directories or files to all_dirs.
    Also add children/parent relations"""
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
