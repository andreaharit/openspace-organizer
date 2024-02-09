from utils.openspace import Openspace
import random
import csv

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
    # Initializing list to store names
    people = []
    # Reads CSV files with names and assign to list
    with open("new_colleagues copy.csv", "r") as f:
        for line in f:
            line = line.strip()
            people.append(line)
    f.close()

    # Default parameters
    num_t = 6
    num_s = 4
    
    print("Currently layout is 6 tables with 4 seats each.")

    # Asks user if they wish to change default settings   
    while True:
        try: 
            print ("Do you wish to change the layout?")
            answer = input("Please use 1 for Yes or anything else of No: ")
            answer.strip().lower()
            if answer == "1":
                while True:
                    num_t = int(input("Insert number of tables: "))
                    num_s = int(input("Insert number of seats per table: "))
                    break
            break
        except ValueError:
            print ("Input not supported, please try again")
            pass
    
    
    # Creates an Openspace
    room = Openspace(number_of_tables = num_t, capacity_tables = num_s)
    # Populates the seats with people
    print ("Assigning people to seats...")
    room.organize(people)
    # Display current occupation
    print ("Current OpenSpace occupation: ", end="")
    room.display_occupation()
    # Writes CSV with final layout
    print ("Outputting table and seating distribution on file.")
    room.store()

if __name__ == "__main__":
    main()