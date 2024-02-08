class Seat:
    def __init__(self, free: bool, occupant: str) -> None:
        self.free = free 
        self.occupant = occupant
    
    # assign someone a seat if it's free
    def set_occupant(name): 
        pass
    # remove someone from a seat and return the name of the person occupying the seat before
    def remove_occupant():
        pass

class Table:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        #list of Seat objects (size = capacity)        
        self.seats = [] # To do

    def has_free_spot():
        # returns a boolean (True if a spot is available)
        pass
    def assign_seat(name):
        # places someone at the table
        pass
    def left_capacity():
        # returns an integer
        pass