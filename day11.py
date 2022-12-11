import numpy as np

from inputs import day11_test, day11

"""
The key to this is a modular arithmetic concept.
First, you need to multiply all the monkeys' mod values together.
Let's call this M. Some say find the LCM but they're small enough you can get away with just the product.
Now, after every operation you do to an item worry level, after doing the computation,
mod that value with M. If you're adding, add then take that result and mod with M.
If you're multiplying, multiply and then mod with M. This will keep your worry values small.
Everything else is the same. We are exploiting the property that for all integers k: (a mod km) mod m = a mod m
"""


def main():

    monkeys = day11.monkeys
    monkey_ops = day11.monkey_ops
    monkey_tests = day11.monkey_tests
    M = day11.M

    rounds = 10000
    items_inspected = {i: 0 for i in monkeys.keys()}

    for _ in range(rounds):
        for monkey, monkey_items in monkeys.items():
            if len(monkey_items) > 0:
                items = np.mod(monkey_ops[monkey](monkey_items), M)
                throw_to = monkey_tests[monkey](items)
                items_inspected[monkey] += items.size
                for item_idx, new_monkey_idx in enumerate(throw_to):

                    monkeys[new_monkey_idx] = np.append(
                        monkeys[new_monkey_idx], items[item_idx]
                    )

            monkeys[monkey] = []

    max_1, max_2 = sorted(items_inspected.values(), reverse=True)[:2]
    print(max_1 * max_2)


if __name__ == "__main__":
    main()
