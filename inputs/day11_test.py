import numpy as np

M = 96577

monkeys = {
    0: np.array([79, 98]),
    1: np.array([54, 65, 75, 74]),
    2: np.array([79, 60, 97]),
    3: np.array([74]),
}

monkey_ops = {
    0: lambda x: (x * 19),
    1: lambda x: (x + 6),
    2: lambda x: (x * x),
    3: lambda x: (x + 3),
}

monkey_tests = {
    0: lambda x: np.piecewise(x, [np.mod(x, 23) == 0, np.mod(x, 23) != 0], [2, 3]),
    1: lambda x: np.piecewise(x, [np.mod(x, 19) == 0, np.mod(x, 19) != 0], [2, 0]),
    2: lambda x: np.piecewise(x, [np.mod(x, 13) == 0, np.mod(x, 13) != 0], [1, 3]),
    3: lambda x: np.piecewise(x, [np.mod(x, 17) == 0, np.mod(x, 17) != 0], [0, 1]),
}
