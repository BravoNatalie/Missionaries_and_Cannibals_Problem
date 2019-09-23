from MC_Problem import MC_Problem
from State import State

class Graph():

    def __init__(self, problem):
        self.problem = problem
        self.root = problem.initial_state

    def Breadth_first_search(self):  # busca em largura
        openedStates = list()
        closedStates = list()

        openedStates.append(self.root)

        while(len(openedStates) > 0):

            if(openedStates[0].is_final()):
                return True

            children = self.problem.move_rigth_sub(openedStates[0])
            openedStates.extend(children)
            closedStates.append(openedStates.pop(0))
            
        return False

         
        