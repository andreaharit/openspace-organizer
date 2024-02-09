import sys
from utils.openspace import Openspace
from utils.file_utils import source_file, num_tables, num_seats

def get_people() -> list: 
    """
    Function gets a filename type CSV from file_utils, reads it and loads the names in the file into a list.
    Raises:
        FileNotFoundError: In case the file is not readable, not a CSV, or typed wrong in the file_utils.
        Closes the program if Error is raised.
    Returns:
        people (list): list where each element was a name in the source file provided in file_utils.
    """    
    try:
        source = source_file
        # Checks if it's a csv
        if not source.endswith("csv"):
            raise FileNotFoundError
        else:
            # Initializes list to store names    
            people = []
            # Reads CSV files with names and assign to list
            with open(source, "r") as f:
                for line in f:
                    line = line.strip()
                    people.append(line)
            f.close()            
    except FileNotFoundError:
        print("Error in loading the file. Please check its name in file_utils.")
        sys.exit()
    return people

def get_numb_table_seat(num_tables: int, num_seats: int) -> int:
    """
    Function gets number of tables and number of seats per table from file_utils.
    It checks if its an acceptable value otherwise it closes the program.

    Args:
        num_tables (int): number of tables in the OpenSpace.
        num_seats (int): number of seats in each table.

    Raises:
        ValueError: In case tables or seat numbers provided are 0 or negative.
        TypeError: In case tables or seat numbers provided are not a number.

    Returns:
        num_t (int): number of tables.
        num_s (int): number of seats.

    """
    while True:
        try:
            # Checks if value is a number
            if isinstance(num_tables, int) and isinstance(num_seats, int):
                # Checks if at least one table and one chair exists
                if num_tables > 0 and num_seats > 0:       
                    num_t = num_tables
                    num_s = num_seats
                    return num_t, num_s
                else:
                    raise ValueError
            else: 
                raise TypeError
        # Exits programs in case values are not up to specification
        except TypeError:
            print("Please check if number of tables or seats is an integer at file_utils.")
            sys.exit()
        except ValueError:
            print("Please check if number of tables or seats is bigger than 0.")
            sys.exit()

def main():
    """
    Main function. 
    Opens a CSV with the names of people to be seated.
    Asks if whishes to change defatult number of tables and seats.
    Assigns randomly people to seats while not lefting someone alone at the table.
    Displays current occupation (how many seats are still available or full ocuppancy).
    Outputs file with final layout in CVS format where:
        colum1 = Table number and 
        colum2 = Name person seating at the table.

    """

    print("Welcome to OpenSpace. Let's start!") 
    people = get_people()
    n_table, n_seat = get_numb_table_seat(num_tables, num_seats)
    
    # Creates an Openspace
    room = Openspace(number_of_tables = n_table, capacity_tables = n_seat)

    # Populates the seats with people
    print ("Assigning people to seats...")
    room.organize(people)    
    # Writes CSV with final layout
    print ("Outputting table and seating distribution on file.")
    room.store()
    # Displays who is where seating
    while True:
        answer = str(input("Do you wish us to display who is seating where? Type 1 for yes: ")).lower().strip()
        if answer == "1":
            room.display()
            break
        else:
            break
    print ("Done =) Please check out the exported file.")
     
            
    


if __name__ == "__main__":
    main()