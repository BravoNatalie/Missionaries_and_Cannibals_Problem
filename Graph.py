from MC_Problem import MC_Problem
from State import State
import pygraphviz as PG

class Graph():

    def __init__(self, problem):
        self.problem = problem
        self.root = problem.initial_state

    def Breadth_first_search(self, prune = False):  # busca em largura
        openedStates = list()
        closedStates = list()

        i = 0
        tree = PG.AGraph(directed=True, strict=True)

        openedStates.append(self.root)

        while(len(openedStates) > 0):
            
            if(prune):
                if openedStates[0] in closedStates:
                 openedStates.pop(0)
                 continue

            if openedStates[0] in openedStates[0].path:
                 openedStates.pop(0)
                 continue

            tree.add_node(openedStates[0].id, label=str(openedStates[0].value))

            if(len(openedStates[0].path) > 0):
                tree.add_edge(openedStates[0].path[0].id, openedStates[0].id)

            if(openedStates[0].is_final()):
                return openedStates[0], tree

            children = self.problem.move(openedStates[0])
            
            openedStates.extend(children)
            closedStates.append(openedStates.pop(0))
            
        return None, tree

         
        