import Constants as c
import MC_Problem as mc

class State():
    def __init__(self, missionaries, cannibals, boat):
        self.value = (missionaries, cannibals, boat)
        self.m = missionaries
        self.c = cannibals
        self.b = boat
        self.depth = 0
        self.path = [] 
        self.id = 0
        
    def __str__(self):
        return ("%s -> Depth: %d" % (self.value, self.depth))
    def __eq__(self, obj):
        return isinstance(obj, State) and self.value == obj.value
        
    def is_final(self):
        return self.value == c.FINAL_STATE.value
    
    def is_valid(self, initial_state):
        if(self.c > self.m and self.m != 0): # mais canibais que missionários no lado de origem
            return False
        elif(self.b > 1 or self.b < 0): # mais de um barco ou barco negativo
            return False
        elif(self.c < 0  or self.m < 0): # missionários e canibais negativos
            return False
        elif(self.c > initial_state.c or self.m > initial_state.m): # nº de missionários e canibais maior que o máximo do problema
            return False
        else:
            return True