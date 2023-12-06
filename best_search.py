from queue import PriorityQueue


def print_puzzle(state):
    for row in state:
        print(row)
    print()


def manhattan_distance(state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    distance = 0

    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_position = divmod(value - 1, 3)
                distance += abs(i - goal_position[0]) + abs(j - goal_position[1])

    return distance


def is_goal_state(state):
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    return state == goal_state


def get_neighbors(state):
    neighbors = []
    zero_i, zero_j = None, None

    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zero_i, zero_j = i, j

    possible_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    for move in possible_moves:
        new_i, new_j = zero_i + move[0], zero_j + move[1]

        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row.copy() for row in state]
            new_state[zero_i][zero_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[zero_i][zero_j]
            neighbors.append(new_state)

    return neighbors


def best_first_search(initial_state):
    frontier = PriorityQueue()
    visited = set()

    frontier.put((manhattan_distance(initial_state), initial_state))

    while not frontier.empty():
        _, current_state = frontier.get()

        print_puzzle(current_state)

        if is_goal_state(current_state):
            return current_state

        visited.add(tuple(map(tuple, current_state)))

        for neighbor in get_neighbors(current_state):
            if tuple(map(tuple, neighbor)) not in visited:
                priority = manhattan_distance(neighbor)
                frontier.put((priority, neighbor))

    return None
