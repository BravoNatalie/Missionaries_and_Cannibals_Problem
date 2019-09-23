import sys
import MC_Problem as mc
from Graph import Graph
from State import State

def main():
    #sys.stdin = open("input.txt", "r") # seria interessante ler os parâmetros de arquivo de entrada
    m = 3
    c = 3
    b = 2
    n_max = 10000 # nº máximo de execuções
            
    problem = mc.MC_Problem(m, c, b, n_max)

    g = Graph(problem)

    g.Breadth_first_search()

if __name__ == '__main__':
	main()