class Seat:
    def __init__(self, free: bool = True) -> None:
        self.free = free 
        self.occupant = ""
    
# assign someone a seat if it's free
    def set_occupant(self, name: str): 
        # if it's free, put new student in the place
        if self.free:
            self.occupant = name
            self.free = False
        # if it's already occupied
        else:
            last_occupant = self.remove_occupant()
            print (f"Bye bye {last_occupant}, they were removed from the seat.")
            self.occupant = name
            
# remove someone from a seat and return the name of the person occupying the seat before
    def remove_occupant(self):
        # remove the person by making the seat free again        
        self.free = True
        # return the name of the last occupant
        return self.occupant 

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