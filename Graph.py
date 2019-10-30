from MC_Problem import MC_Problem
from State import State
import pygraphviz as PG
from operator import itemgetter


class Graph():

    def __init__(self, problem):
        self.problem = problem
        self.root = problem.initial_state

    # Calcula o custo para a busca ordenada
    def calculate_cost_ordered_search(self, state, parent_state):
        state.cost += 1

    def calculate_heuristic_cost_search(self, state, parent_state):
        state.cost = state.m

    def calculate_a_star_cost(self, state, parent_state):
        state.cost = (parent_state.cost - parent_state.m) + state.m + 1

    # Executa a busca usando a abordagens diversas de calculos de custo
    def perform_search(self, calculate_cost_function=None):
        closed_states = list()

        tree = PG.AGraph(directed=True, strict=True)

        states = [self.root]

        while len(states) > 0:

            current_state = states.pop()

            if current_state in closed_states or current_state in current_state.path:
                continue

            tree.add_node(current_state.id, label=str(current_state.value))

            if len(current_state.path) > 0:
                tree.add_edge(current_state.path[0].id, current_state.id)

            if current_state.is_final():
                return current_state, tree

            children = self.problem.move(current_state, calculate_cost_function)

            states += children
            closed_states.append(current_state)

            if calculate_cost_function:
                states.sort()

        return None, tree

    # busca em largura
    def breadth_first_search(self, prune=False):
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

    # Busca backtracking
    def backtracking_search(self):
        return self.perform_search()

    # Busca ordenada
    def ordered_search(self):
        return self.perform_search(self.calculate_cost_ordered_search)

    # Busca Heuristica
    def heuristic_search(self):
        return self.perform_search(self.calculate_heuristic_cost_search)

    # Busca A*
    def a_star_search(self):
        return self.perform_search(self.calculate_a_star_cost)
