# openspace-organizer

## Description
OpenOrganizer is python program that randomly assigns people to seats on tables.

By importing a user provided CSV file with people's names, then asking user for number of tables and seats. And finally exports the distribuition via a CSV file where:

* Column 1 = Table number.
* Column 2 = Name of a person seating at that table.

As a default feature, the program makes sure no one is sitting alone.

## Installation
The program uses default python libraries.
To use it:
1. Clone the repository.
2. Add a CSV file with the names of the people to be seated in the same folder as main.
3. Run the program from the terminal.

## Usage
The program asks the following inputs from the user:
* Name of file to be read (Ex: "new_colleagues.csv").
* If the user wishes to change default number of tables and seats. If yes:
   * It asks for a number of tables.
   * It asks for the number of seats per table.
   
The program then assigns people to a table, displays the current occupancy and exports the layout to a new file: seat_layout.csv on the main folder.