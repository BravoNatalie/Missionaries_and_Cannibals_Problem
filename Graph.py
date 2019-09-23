from MC_Problem import MC_Problem
from State import State

class Graph():

    def __init__(self, problem):
        self.problem = problem
        self.root = problem.initial_state

    def Breadth_first_search(self):  # busca em largura
        openedStates = list()
        closedStates = list()
        level = 0

        openedStates.append(self.root)

        while(len(openedStates) > 0):

            children = self.problem.move_rigth_sub(openedStates[0])
            openedStates.extend(children)
            level +=1
            closedStates.append(openedStates.pop(0))

            for s in openedStates:
                if(s.is_final):
                    return True

        