class Seat:
    """    
    Class creates seat object that contain attributes:
    Atrib:
    self.occupant (str): Stores a name () of someone sitting or "NULL" if the seat is empty.
    self.free (bool):  True if no one is sitting in the object, False if the seat is free.      
    """
   
    def __init__(self, free: bool = True) -> None:   
        self.occupant = "NULL"
        self.free = free         

    def __str__(self) -> str:
        """ 
        Method returns name of the person occupying seat or "NULL" if it's free.
        """
        return f"{self.occupant}"
    
    def set_occupant(self, name: str) -> None: 
        """
        Method assigns a name to a seat and changes it to occupied.
        Args:
            name (str): name of a person who is seating.
        """        
        self.occupant = name
        self.free = False        

    def remove_occupant(self) -> str:
        """
        Method removes person from a seat. Seats it as a free seat and with "NULL" ocuppant.
        Returns:
            previous_occupant (str): name of the person who was removed from the seat.
        """      
        self.free = True   
        previous_occupant = self.occupant  
        self.occupant = "NULL"
        return previous_occupant

class Table(Seat):
    """    
    Class creates table object that contain attributes:
    Atrib:
    self.table_num (str): Numerical name for a table, starting from 1.
    self.capacity (int):  Number of seats available in the table.
    self.seats (list): Stores all seats objects available at the table.      
      
    """
    def __init__(self, table_num: str, capacity: int) -> None:
        self.table_num = table_num
        self.capacity = capacity 
        self.seats = [Seat() for _ in range(self.capacity)] 

    def __str__(self) -> str:
        """ 
        Method returns numerical name of the table.
        """
        return f"{self.table_num}"  

    def has_free_spot(self) -> bool:
        """
        Method assess if the table has seats that are still not occupied.
        Returns:
            bool: True if there is at least one seat available. False if all seats are occupied.
        """
        for s in self.seats:
            if s.free:
                return True
        return False
    
    def assign_seat(self, name) -> None:
        """
        Method searches table for an available seat. If it finds one, seats this person on it.
        Args:
            name (str): name of a person who is trying to seat        
        """        
        for s in self.seats:
            if s.free:
                s.set_occupant(name)
                break

    def left_capacity(self) -> int:
        """
        Method counts the number of free seats in a table.
        Returns:
            count (int): seats available for seating.
        """
        count = 0             
        if self.has_free_spot():
            for s in self.seats:
                if s.free:
                    count += 1
        return count