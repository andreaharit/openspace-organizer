class Seat:
    def __init__(self, name, free: bool = True) -> None:
        self.name = name
        self.free = free 
        self.occupant = ""
    
# assign someone a seat if it's free
    def set_occupant(self, name: str): 
        if self.free:
            self.occupant = name
            self.free = False        

# remove someone from a seat and return the name of the person occupying the seat before
    def remove_occupant(self):   
        self.free = True
        return self.occupant 


class Table(Seat):
    def __init__(self, name, capacity: int = 4) -> None:
        self.name = name
        self.capacity = capacity

        # List of Seat objects (size = capacity)        
        self.seats = [] 
        for _ in range(self.capacity):
            # Give names to the chairs to build a visual layout
            seat_name = f"{self.name}.{_}"
            self.seats.append(Seat(seat_name))

    # Returns a boolean (True if a spot is available on the table)
    def has_free_spot(self) -> bool:
        for s in self.seats:
            if s.free:
                return True
        return False
    # Place someone at the table in a free spot
    def assign_seat(self, name):        
        for s in self.seats:
            if s.free:
                s.set_occupant(name)                               
                break
    # Return number of free seats at the table
    def left_capacity(self) ->int :
        count = 0
        if self.has_free_spot():
            for s in self.seats:
                if s.free:
                    count += 1
        return count