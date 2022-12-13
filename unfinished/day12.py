from typing import Iterator, TypeVar
from collections import deque
import heapq
from string import ascii_lowercase

TEST_INPUT = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi"""


GridLocation = tuple[int, int]
T = TypeVar("T")
Location = TypeVar("Location")


class SquareGrid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.weights: dict[GridLocation, int] = {}
        self.grid: list[list] = []

    def possible_move(self, coord: GridLocation, self_coord: GridLocation) -> bool:
        (x, y) = coord
        (s_x, s_y) = self_coord

        try:
            orig_idx = ascii_lowercase.index(self.grid[s_y][s_x])
            new_idx = ascii_lowercase.index(self.grid[y][x])
            print(orig_idx, new_idx)
            if new_idx - orig_idx <= 1:
                return True
            return False
        except IndexError:
            return False

    def neighbors(self, coord: GridLocation) -> Iterator[GridLocation]:
        (x, y) = coord

        neighbors = [(x + 1, y), (x - 1, y), (x, y - 1), (x, y + 1)]  # E W N S
        results = filter(
            lambda neighbor: self.possible_move(neighbor, coord), neighbors
        )
        return results

    def cost(self, from_node: GridLocation, to_node: GridLocation) -> int:
        return self.weights.get(to_node, 1)


class PriorityQueue:
    def __init__(self):
        self.elements: list[tuple[int, T]] = []

    def empty(self) -> bool:
        return not self.elements

    def put(self, item: T, priority: int):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


def prepare_input(inp):

    grid = SquareGrid(len(inp[0]), len(inp))
    weights = {}
    start = None
    end = None

    for j, row in enumerate(inp):
        grid_row = []
        for i, char in enumerate(row):
            if char == "S":
                start = (i, j)
                grid_row.append("a")
            elif char == "E":
                end = (i, j)
                grid_row.append("a")
            else:
                weights[(i, j)] = 1  # ascii_lowercase.index(char)
                grid_row.append(char)
        grid.grid.append(grid_row)

    grid.weights = weights

    return grid, start, end


def draw_tile(graph, id, style):
    r = " . "
    if "number" in style and id in style["number"]:
        r = " %-2d" % style["number"][id]
    if "point_to" in style and style["point_to"].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style["point_to"][id]
        if x2 == x1 + 1:
            r = " > "
        if x2 == x1 - 1:
            r = " < "
        if y2 == y1 + 1:
            r = " v "
        if y2 == y1 - 1:
            r = " ^ "
    if "path" in style and id in style["path"]:
        r = " @ "
    if "start" in style and id == style["start"]:
        r = " A "
    if "goal" in style and id == style["goal"]:
        r = " Z "
    return r


def draw_grid(graph, **style):
    print("___" * graph.width)
    for y in range(graph.height):
        for x in range(graph.width):
            print("%s" % draw_tile(graph, (x, y), style), end="")
        print()
    print("~~~" * graph.width)


def dijkstra_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from: dict = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while not frontier.empty():
        current = frontier.get()

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost
                frontier.put(next, priority)
                came_from[next] = current

    return came_from, cost_so_far


def reconstruct_path(
    came_from: dict[Location, Location], start: Location, goal: Location
) -> list[Location]:

    current: Location = goal
    path: list[Location] = []
    if goal not in came_from:  # no path was found
        return []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start)  # optional
    path.reverse()  # optional
    return path


def main():

    grid, start, end = prepare_input(TEST_INPUT.splitlines())

    came_from, cost_so_far = dijkstra_search(grid, start, end)
    print(len(reconstruct_path(came_from, start=start, goal=end)))
    return
    draw_grid(grid, point_to=came_from, start=start, goal=end)
    print()
    draw_grid(grid, path=reconstruct_path(came_from, start=start, goal=end))


if __name__ == "__main__":
    main()
