import sys
import MC_Problem as MC
from Graph import Graph
from State import State


def main():
    # sys.stdin = open("input.txt", "r") # seria interessante ler os parâmetros de arquivo de entrada
    m = 3
    c = 3
    b = 2
    n_max = 10000  # nº máximo de execuções

    problem = MC.MC_Problem(m, c, b, n_max)

    g = Graph(problem)

    state, tree = g.backtracking_search()
    tree.layout(prog='dot')
    tree.draw('images/graph_backtrack.png')

    g = Graph(problem)

    state, tree = g.breadth_first_search()
    tree.layout(prog='dot')
    tree.draw('images/graph_breadth.png')

    state, tree = g.ordered_search()
    tree.layout(prog='dot')
    tree.draw('images/graph_ordered_search.png')

    state, tree = g.heuristic_search()
    tree.layout(prog='dot')
    tree.draw('images/graph_heuristic_search.png')

    state, tree = g.a_star_search()
    tree.layout(prog='dot')
    tree.draw('images/graph_a_star_search.png')





if __name__ == '__main__':
    main()
