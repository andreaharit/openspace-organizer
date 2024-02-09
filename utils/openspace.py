from .table import Table
import random
import csv

class Openspace(Table):
    """_summary_

    Args:
        Table (class): Generates tables in a room.
        :number_of_tables (int): number of tables available in the Openspace. Default is 6.
        :capacity_tables (int): number of seats available in each table. Default is 4.
    Atr:
        :self.number_of tables (int): assigned to argument number_of_tables. 
        :self.capacity_tables (int): assigned to argument capacity_tables.
        self.tables (list): stores tables objects of the OpenSpace.
        """
    def __init__(self, number_of_tables: int, capacity_tables: int) -> None:
        self.number_of_tables = number_of_tables
        self.capacity_tables = capacity_tables
        # Create list of tables 
        self.tables = [Table(table_num = str(_+1), capacity = self.capacity_tables) for _ in range(self.number_of_tables)]        
          
    def organize(self, names: list) -> None: 
        """ 
        Method distributes randomly names in a list into seats in each table. Checks if a person was not left
        seating alone in the last table. If it person is alone, removes a person from the first table, first seat
        and puts them in the last table too.
        Args:
            :names (list): list of people's names that will be seated.        
        """       
        # Randomizing order of names 
        random.shuffle(names)
        # Assigning names to tables and its seats
        for name in names:  
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    break
        # Checking if there is a person alone at the last table. If yes, reassign someone to be together.    
        self.not_seat_alone()

    def room_layout (self) -> list:
        """       
        It is an auxiliary method that makes writing the seat layout CSV file easier.
        Creates a nested list with organized information about who is seating in which table.
        Ex: [["1", "Joana"], ["2", "Carl"], ["2","Bruno"]]. Joana is at table 1, Carl at 2, Bruno at 2.
        Returns:
            : layout (list): nested list where elements are [table name, name person sitting on it]
        """
        layout = []        
        for table in self.tables:
            for seat in table.seats:
                # initialize/reset temporary sublist for each pair table/name
                location_person = []
                # populates sublist with info
                location_person.append(table.table_num)
                location_person.append(seat.occupant)
                # puts into main list of the OpenSpace layout
                layout.append(location_person)
        return layout
    
    def display(self) -> None:
        """
        Method prints current layout: 
        Name of person seating at which table. And how many empty seats are in total in the OpenSpace.
        """            
        for table in self.tables:
            empty_seat = 0
            for seat in table.seats:
                if not seat.free:
                    print(f"{seat.occupant} is seating at table number {table.table_num}.")
                else: 
                    empty_seat += 1                    
            if empty_seat > 0:
                print(f"Table {table.table_num} has {empty_seat} empty seats.")

    def display_occupation(self) -> None:
        """
        Method prints if all tables in the OpenSpace are full or how many seats are still available.
        """
        empty_total = 0
        for table in self.tables:
            empty_total += table.left_capacity()
        if empty_total == 0:
            print ("All tables are full.")
        else:
            print (f"We still have {empty_total} empty seats")

    def not_seat_alone(self):
        """
        Method checks last table to see if there is a person seating alone. 
        If yes, gets the first person in the first table and add to the last one.        
        """
        # Initializes tables to be checked/changed
        last_table = self.tables[-1]
        first_table = self.tables[0]
        # Calculates if last table has only one person seating
        if last_table.left_capacity() == (self.capacity_tables - 1):
            # Removes first person person on the first table and adds them to last table
            person_moved = first_table.seats[0].remove_occupant()
            last_table.assign_seat(person_moved)

    def store (self, filename = "seat_layout.csv") -> None:  
        """
        Method stores currently seatting layout into a CSV file.        
        """
        # Creates header      
        header = ["Table", "Occupant"]
        # Writing file
        with open(filename ,'w') as output:
            writer = csv.writer(output)
            writer.writerow(header)
            writer.writerows(self.room_layout())
        output.close()