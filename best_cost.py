import heapq


class PuzzleNode:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


def is_goal(state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return state == goal_state


def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def generate_successors(node):
    successors = []
    i, j = get_blank_position(node.state)

    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for move in moves:
        ni, nj = i + move[0], j + move[1]

        if 0 <= ni < 3 and 0 <= nj < 3:
            new_state = [row.copy() for row in node.state]
            new_state[i][j], new_state[ni][nj] = new_state[ni][nj], new_state[i][j]

            action = f"Move {node.state[ni][nj]} to ({i}, {j})"
            cost = node.cost + 1

            successors.append(PuzzleNode(new_state, node, action, cost))

    return successors


def print_solution(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    for t in path[::-1]:
        print('\n'.join([' '.join(map(str, row)) for row in t]))
        print()


def best_cost_search(initial_state):
    initial_node = PuzzleNode(initial_state)
    frontier = [initial_node]
    explored = set()

    while frontier:
        node = heapq.heappop(frontier)

        if is_goal(node.state):
            #print("Solution found:")
            print_solution(node)
            return

        explored.add(tuple(map(tuple, node.state)))

        successors = generate_successors(node)

        for successor in successors:
            if tuple(map(tuple, successor.state)) not in explored:
                heapq.heappush(frontier, successor)
                explored.add(tuple(map(tuple, successor.state)))