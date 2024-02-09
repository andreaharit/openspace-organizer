import sys
import json


def load_json(file: str):
    """
    Loads json with settings into variables.

    Args:
        file (str): json file to be loaded.

    Returns:
        num_t (int): number of tables.
        num_s (int): number of seats.
        source_file (str): file with people's name.
    """
    f = open('utils/setting_op.json')
    data = json.load(f)
    num_t = data["num_tables"]
    num_s = data["num_seats"]
    source_file = data["source_file"]
    return num_t, num_s, source_file
     

def get_people(source_file: str = "new_colleagues.csv") -> list: 
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
        if not source.endswith(".csv"):
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

def check_numb_table_seat(number: int) -> bool:
    """
    Function gets number of tables or number of seats per table.
    It checks if its an acceptable value otherwise it closes the program.

    Args:
        num (int): number to be checked.

    Raises:
        ValueError: In case tables or seat numbers provided are 0 or negative.
        TypeError: In case tables or seat numbers provided are not a number.

    Returns:
        True : if num is in acceptable format.

    """
    try:    
        # checks if it's an int
        if isinstance(number, int):
            # Checks if at least one table/one chair exists
            if number > 0:  
                return True
            else:
                raise ValueError
        else: 
            raise TypeError
    # Exits programs in case values are not up to specification
    except TypeError:
        print("Please check if number of tables or seats is an integer.")
        sys.exit()
    except ValueError:
        print("Please check if number of tables or seats is bigger than 0.")
        sys.exit()
        
def ask_display() -> bool: 
    """
    Function asks user if they want to display on terminal seat arrangements.
    Returns:
        bool: True if user wants to see, False if not.
    """
    while True:
            answer = str(input("Do you wish us to display who is seating where? Type y for yes: ")).lower().strip()
            if answer == "y":
                return True
            else:
                return False