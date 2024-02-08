from table import Table, Seat

class Openspace(Table):
    def __init__(self, number_of_tables: int = 6) -> None:
        self.number_of_tables = number_of_tables
        self.tables = []
        # Create list of tables 
        for _ in range(self.number_of_tables):
            # give names to the tables so we can a room layout 
            self.table_num = f"{_}"
            self.tables.append(Table(table_num = self.table_num))
          
    def organize(self, names: list):        
        # randomly assign people to Seat objects in the different Table objects.
        for name in names:  
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    break

    def display():
        # display the different tables and there occupants in a nice and readable way
        pass
    def store(filename):
        #store the repartition in an excel file
        pass