import Constants as c
from State import State
import numpy as np

class MC_Problem:
    def __init__(self, missionaries, cannibais, boat_capacity, max_nodes):
        self.M = missionaries
        self.C = cannibais
        self.B_CAP = boat_capacity
        self.N_MAX = max_nodes
        self.initial_state = State(self.M, self.C, c.B)
        self.final_state = c.FINAL_STATE
        self.all_actions = self.__get_all_actions()
        self.count = 1 

    def __get_all_actions(self):

        standard_actions = { # set of tuples
            (1, 0, 1), # o barco leva um missionário
            (2, 0, 1), # o barco leva dois missionário
            (0, 1, 1), # o barco leva um canibal
            (0, 2, 1), # o barco leva dois canibais
            (1, 1, 1)  # o barco leva um missionário e um canibal
        }
        
        if((self.B_CAP - c.MIN_B_CAP) > 0):
   
            for i in range(c.MIN_B_CAP + 1, self.B_CAP + 1):

                standard_actions.add((i, 0, c.B))
                standard_actions.add((0, i, c.B))

                if(i % 2 == 0):
                    standard_actions.add((i//2, i//2, c.B))
                else:
                    standard_actions.add((i//2 + 1, i//2, c.B))
                    standard_actions.add((i//2, i//2 + 1, c.B))
        
        return standard_actions
                    

    # os métodos de operação abaixo utilizam soma e subtração para gerar os possíveis estados alcançáveis a partir de um estada dado 

    def move(self, state):
        possibles_states = list()
        for s in self.all_actions:
            if state.depth % 2 == 0: 
                result = State(*tuple(np.subtract(state.value, s)))
            else:
                result = State(*tuple(np.add(state.value, s)))
            result.depth = state.depth + 1
            result.path = [state] + state.path
            result.id = self.count
            self.count += 1
            if result.is_valid(self.initial_state):
                possibles_states.append(result)
        return possibles_states
