from utils.openspace import Openspace
from utils.file_utils import load_json, get_people, check_numb_table_seat, ask_display


def main():
    """
    Main function. 
    Opens a CSV with the names of people to be sitted.
    Asks if whishes to change defatult number of tables and seats.
    Assigns randomly people to seats while not lefting someone alone at the table.
    Displays current occupation (how many seats are still available or full ocuppancy).
    Outputs file with final layout in CVS format where:
        colum1 = Table number and 
        colum2 = Name person seating at the table.

    """

    
    # Gets variables from json
    n_table, n_seat, source_file = load_json("utils/setting_op.json") 
    people = get_people(source_file)
    # Checks if variables are according to specification
    check_numb_table_seat(n_table)
    check_numb_table_seat(n_seat)

    print("Welcome to OpenSpace. Let's start!")

    # Creates an Openspace
    room = Openspace(number_of_tables = n_table, capacity_tables = n_seat)

    # Populates the seats with people
    print ("Assigning people to seats...")
    room.organize(people) 

    # Writes excel with final layout
    print ("Outputting table and sting distribution on file.")
    room.store()

    # Displays who is sitting where if user wants
    if ask_display():
        room.display()     
    
    print ("Done =) Please check out the exported file.")

if __name__ == "__main__":
    main()
