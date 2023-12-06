from copy import deepcopy


def print_puzzle(state):
    for row in state:
        print(row)
    print()


def h(state, goal_state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != goal_state[i][j]:
                count += 1
    return count


def get_neighbors(state):
    neighbors = []
    zero_i, zero_j = None, None

    # Encontrar a posição do zero no estado atual
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                zero_i, zero_j = i, j

    # Mover para cima
    if zero_i > 0:
        neighbor = deepcopy(state)
        neighbor[zero_i][zero_j], neighbor[zero_i - 1][zero_j] = neighbor[zero_i - 1][zero_j], neighbor[zero_i][zero_j]
        neighbors.append(neighbor)

    # Mover para baixo
    if zero_i < 2:
        neighbor = deepcopy(state)
        neighbor[zero_i][zero_j], neighbor[zero_i + 1][zero_j] = neighbor[zero_i + 1][zero_j], neighbor[zero_i][zero_j]
        neighbors.append(neighbor)

    # Mover para a esquerda
    if zero_j > 0:
        neighbor = deepcopy(state)
        neighbor[zero_i][zero_j], neighbor[zero_i][zero_j - 1] = neighbor[zero_i][zero_j - 1], neighbor[zero_i][zero_j]
        neighbors.append(neighbor)

    # Mover para a direita
    if zero_j < 2:
        neighbor = deepcopy(state)
        neighbor[zero_i][zero_j], neighbor[zero_i][zero_j + 1] = neighbor[zero_i][zero_j + 1], neighbor[zero_i][zero_j]
        neighbors.append(neighbor)

    return neighbors


def hill_climbing(start_state, goal_state):
    current_state = start_state

    while True:
        print_puzzle(current_state)

        # Verificar se atingimos o objetivo
        if current_state == goal_state:
            break

        # Obter estados vizinhos
        neighbors = get_neighbors(current_state)

        # Avaliar vizinhos
        neighbor_evaluations = [h(neighbor, goal_state) for neighbor in neighbors]

        # Escolher o vizinho com a menor avaliação
        best_neighbor = neighbors[neighbor_evaluations.index(min(neighbor_evaluations))]

        # Se a melhor avaliação for maior ou igual à avaliação atual, paramos
        if h(best_neighbor, goal_state) >= h(current_state, goal_state):
            print("Não é possível melhorar mais.")
            break

        # Atualizar o estado atual
        current_state = best_neighbor