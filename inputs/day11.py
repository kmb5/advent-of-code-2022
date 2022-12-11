import numpy as np

M = 9699690

monkeys = {
    0: np.array([59, 74, 65, 86]),
    1: np.array([62, 84, 72, 91, 68, 78, 51]),
    2: np.array([78, 84, 96]),
    3: np.array([97, 86]),
    4: np.array([50]),
    5: np.array([73, 65, 69, 65, 51]),
    6: np.array([69, 82, 97, 93, 82, 84, 58, 63]),
    7: np.array([81, 78, 82, 76, 79, 80]),
}

monkey_ops = {
    0: lambda x: (x * 19),
    1: lambda x: (x + 1),
    2: lambda x: (x + 8),
    3: lambda x: (x * x),
    4: lambda x: (x + 6),
    5: lambda x: (x * 17),
    6: lambda x: (x + 5),
    7: lambda x: (x + 3),
}

monkey_tests = {
    0: lambda x: np.piecewise(x, [x % 7 == 0, x % 7 != 0], [6, 2]),
    1: lambda x: np.piecewise(x, [x % 2 == 0, x % 2 != 0], [2, 0]),
    2: lambda x: np.piecewise(x, [x % 19 == 0, x % 19 != 0], [6, 5]),
    3: lambda x: np.piecewise(x, [x % 3 == 0, x % 3 != 0], [1, 0]),
    4: lambda x: np.piecewise(x, [x % 13 == 0, x % 13 != 0], [3, 1]),
    5: lambda x: np.piecewise(x, [x % 11 == 0, x % 11 != 0], [4, 7]),
    6: lambda x: np.piecewise(x, [x % 5 == 0, x % 5 != 0], [5, 7]),
    7: lambda x: np.piecewise(x, [x % 17 == 0, x % 17 != 0], [3, 4]),
}
