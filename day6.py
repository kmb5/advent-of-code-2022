TEST_STR = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
from collections import Counter


def main():
    with open("inputs/day6.txt") as f:
        txt = f.read()

    print(f"Part 1: {first_n_distinct_chars(txt, 4)}")
    print(f"Part 2: {first_n_distinct_chars(txt, 14)}")


def first_n_distinct_chars(strng: str, n: int):
    "Return position where first n distinct characters are found"
    for i in range(n, len(strng)):
        chars = strng[i - n : i]

        if len(Counter(chars)) == n:
            return i


if __name__ == "__main__":
    main()
