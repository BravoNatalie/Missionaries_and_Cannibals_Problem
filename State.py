import Constants as c
import MC_Problem as mc


class State:
    def __init__(self, missionaries, cannibals, boat):
        self.value = (missionaries, cannibals, boat)
        self.m = missionaries
        self.c = cannibals
        self.b = boat
        self.depth = 0
        self.path = []
        self.id = 0
        self.cost = 0

    def __str__(self):
        return "%s -> Depth: %d" % (self.value, self.depth)

    def __eq__(self, obj):
        return isinstance(obj, State) and self.value == obj.value

    def __lt__(self, state):
        if self.cost == state.cost:
            if self.id < state.id:
                return self
            return state
        if self.id < state.id:
            return self

    def is_final(self):
        return self.value == c.FINAL_STATE.value

    def is_valid(self, initial_state):

        # mais canibais que missionários no lado de origem
        if self.c > self.m != 0:
            return False

        # mais de um barco ou barco negativo
        elif self.b > 1 or self.b < 0:
            return False

        # missionários e canibais negativos
        elif self.c < 0 or self.m < 0:
            return False

        # nº de missionários e canibais maior que o máximo do problema
        elif self.c > initial_state.c or self.m > initial_state.m:
            return False

        else:
            return True
