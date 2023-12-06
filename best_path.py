from queue import PriorityQueue


def print_puzzle(state):
    for row in state:
        print(row)


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def generate_neighbors(state):
    i, j = find_blank(state)
    neighbors = []

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for move in moves:
        x, y = move
        new_i, new_j = i + x, j + y

        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row.copy() for row in state]
            new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
            neighbors.append(new_state)

    return neighbors


def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                target_i, target_j = divmod(state[i][j] - 1, 3)
                distance += abs(i - target_i) + abs(j - target_j)
    return distance


def best_path_search(initial_state, goal_state):
    priority_queue = PriorityQueue()
    priority_queue.put((manhattan_distance(initial_state), initial_state))

    visited = set()

    while not priority_queue.empty():
        current_state = priority_queue.get()[1]
        print_puzzle(current_state)
        print("\n")

        if current_state == goal_state:
            return current_state

        visited.add(tuple(map(tuple, current_state)))

        for neighbor in generate_neighbors(current_state):
            if tuple(map(tuple, neighbor)) not in visited:
                priority_queue.put((manhattan_distance(neighbor), neighbor))

    return None