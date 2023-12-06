from collections import deque


class PuzzleNode:
    def __init__(self, state, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action


def get_blank_position(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def move(state, direction):
    i, j = get_blank_position(state)
    new_state = [row.copy() for row in state]
    if direction == 'up' and i > 0:
        new_state[i][j], new_state[i - 1][j] = new_state[i - 1][j], new_state[i][j]
    elif direction == 'down' and i < 2:
        new_state[i][j], new_state[i + 1][j] = new_state[i + 1][j], new_state[i][j]
    elif direction == 'left' and j > 0:
        new_state[i][j], new_state[i][j - 1] = new_state[i][j - 1], new_state[i][j]
    elif direction == 'right' and j < 2:
        new_state[i][j], new_state[i][j + 1] = new_state[i][j + 1], new_state[i][j]
    return new_state


def is_goal(state):
    return state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def print_solution(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    for t in path[::-1]:
        print('\n'.join([' '.join(map(str, row)) for row in t]))
        print()


def breadth_first_search(initial_state):
    initial_node = PuzzleNode(initial_state)
    queue = deque([initial_node])
    visited = set()

    while queue:
        current_node = queue.popleft()
        if is_goal(current_node.state):
            print_solution(current_node)
            return True

        visited.add(tuple(map(tuple, current_node.state)))

        for action in ['up', 'down', 'left', 'right']:
            new_state = move(current_node.state, action)
            if tuple(map(tuple, new_state)) not in visited:
                new_node = PuzzleNode(new_state, current_node, action)
                queue.append(new_node)

    print("No solution found.")
    return False
