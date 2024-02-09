# openspace-organizer

## Description
OpenOrganizer is python program that randomly assigns people to seats on tables.

The program reads user provided settings from an file_utils. Where:
* source_file is the name of the csv file with people's name
* num_tables is the number of tables available at the OpenSpace.
* num seats is the number of seats that each table has.

And exports the distribuition via a CSV file where:

* Column 1 = Table number.
* Column 2 = Name of a person seating at that table.

As a default feature, the program makes sure no one is sitting alone.

## Installation
The program uses default python libraries.
To use it:
1. Clone the repository.
2. Add a CSV file with the names of the people to be seated in the same folder as main.

## Usage
1. User might edit file_utils to provide the parameters for:
   1. Name of the CSV file to be read, with people's name, that was put on main.
   2. Number of available tables.
   3. Number of available seats per table.
2. Run program via terminal. Where the program will greet you, assign people to a table and displays the current occupancy.
3. The program will then output the layout to a new file: seat_layout.csv on the main folder.