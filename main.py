import random
import copy
import os, sys
import time
from depth_search import depth_first_search
from breadth_search import breadth_first_search
from hill_climbing import hill_climbing
from best_search import best_first_search
from best_cost import best_cost_search
from best_path import best_path_search


def main():
    final_state = [
                    [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 0]
                ]


    def check_possibility_of_solution(state): # verifica a paridade do estado, caso for par, então há solução
        arr_state = []
        parity = 0
        for arr in state:
            for n in arr:
                if n != 0:
                    arr_state.append(n)

        for i in range(0, 8):
            for j in range(i + 1, 8):
                if arr_state[i] > arr_state[j]:
                    parity += 1

        if parity % 2 == 0:
            return True
        else:
            return False


    def shuffle_numbers():
        numbers = []

        while True:
            initial_state = [
                    [0, 0, 0],
                    [0, 0, 0],
                    [0, 0, 0]
                ]

            while len(numbers) != 8: 
                for m in range(0, 3):
                    for n in range(0, 3):
                        drawn_number = random.randrange(1, 9)
                        if drawn_number not in numbers and initial_state[m][n] == 0:
                            initial_state[m][n] = drawn_number
                            numbers.append(drawn_number)
            if check_possibility_of_solution(initial_state) and initial_state != final_state:
                return initial_state

        return 0


    def print_state(state):
        for row in state:
            print(row)


    # comandos:
    while True:
        os.system("clear")
        initial_state = shuffle_numbers()
        print("O estado inicial do seu 8 Puzzle game é: ")
        print_state(initial_state)
        print("\nPara que a IA comece a resolver o puzzle, pressione 'Enter'...")
        print("\nCaso deseja fechar o programa aperte 'Ctrl + c'")
        input()


        #Busca em profundidade:
        os.system("clear")
        input("Aperte 'Enter' para a Busca em profundidade: ")

        begin = time.time()
        depth_first_search(initial_state)
        exec_time = time.time() - begin
        print(f"A busca em profundidade levou {exec_time} segundos para resolver este puzzle")
        input()


        #Busca em largura
        os.system("clear")
        input("Aperte 'Enter' para a Busca em largura: ")
       
        begin = time.time()
        breadth_first_search(initial_state)
        exec_time = time.time() - begin
        print(f"A busca em largura levou {exec_time} segundos para resolver este puzzle")
        input()


        #Busca em Hill-Climbing
        os.system("clear")
        input("Aperte 'Enter' para a Busca em Hill-Climbing: ")
       
        begin = time.time()
        hill_climbing(initial_state, final_state)
        exec_time = time.time() - begin
        print(f"A busca em Hill-Climbing levou {exec_time} segundos para resolver este puzzle")
        input()


        #Busca em Best-search
        os.system("clear")
        input("Aperte 'Enter' para a Busca em Best-Search: ")
       
        begin = time.time()
        best_first_search(initial_state)
        exec_time = time.time() - begin
        print(f"A busca em Best-Search levou {exec_time} segundos para resolver este puzzle")
        input()


        #Busca em Best-Cost:
        os.system("clear")
        input("Aperte 'Enter' para a Busca em Best-Cost: ")       
        begin = time.time()
        best_cost_search(initial_state)
        exec_time = time.time() - begin
        print(f"A busca em Best-Cost levou {exec_time} segundos para resolver este puzzle")
        input()


        #Busca em Best-Path:
        os.system("clear")
        input("Aperte 'Enter' para a Busca em Best-Path: ")
       
        begin = time.time()
        best_path_search(initial_state, final_state)
        exec_time = time.time() - begin
        print(f"A busca em Best-Path levou {exec_time} segundos para resolver este puzzle")
        input()


        input()


if __name__ == "__main__":
    main()