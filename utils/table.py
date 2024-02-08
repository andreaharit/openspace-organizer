class Seat:
    def __init__(self, seat_num: str, free: bool = True) -> None:
        self.seat_num = seat_num
        self.free = free 
        self.occupant = ""
    
    def set_occupant(self, name: str): 
        if self.free:
            self.occupant = name
            self.free = False        

    def remove_occupant(self):
        self.free = True
        # return previous occupant
        return self.occupant 

class Table(Seat):
    def __init__(self, table_num: str, capacity: int = 4) -> None:
        self.table_num = table_num
        self.capacity = capacity 
        self.seats = [] 
        for _ in range(self.capacity):
            # Gives each seat a numeric name to create a layout and helps debuggin
            seat_num = f"{_}"
            self.seats.append(Seat(seat_num = seat_num))

    def has_free_spot(self) -> bool:
        for s in self.seats:
            if s.free:
                return True
        return False
    
    def assign_seat(self, name):        
        for s in self.seats:
            if s.free:
                s.set_occupant(name)
                break

    def left_capacity(self):
        count = 0
        if self.has_free_spot():
            for s in self.seats:
                if s.free:
                    count += 1
        return count