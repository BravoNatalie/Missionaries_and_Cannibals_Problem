from MC_Problem import MC_Problem
from State import State
import pygraphviz as PG


class Graph():

    def __init__(self, problem):
        self.problem = problem
        self.root = problem.initial_state

    def breadth_first_search(self, prune=False):  # busca em largura
        opened_states = list()
        closed_states = list()

        i = 0
        tree = PG.AGraph(directed=True, strict=True)

        opened_states.append(self.root)

        while len(opened_states) > 0:

            if prune:
                if opened_states[0] in closed_states:
                    opened_states.pop(0)
                    continue

            if opened_states[0] in opened_states[0].path:
                opened_states.pop(0)
                continue

            tree.add_node(opened_states[0].id, label=str(opened_states[0].value))

            if len(opened_states[0].path) > 0:
                tree.add_edge(opened_states[0].path[0].id, opened_states[0].id)

            if opened_states[0].is_final():
                return opened_states[0], tree

            children = self.problem.move(opened_states[0])

            opened_states.extend(children)
            closed_states.append(opened_states.pop(0))

        return None, tree
