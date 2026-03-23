# ------------------------------------------------------------------------------------------------- #
# Title: Assignment08 - Main.py
# # Description: Demonstrates how to use properties in a class
# ChangeLog: (Who, When, What)
# DallenT,3.25.2026,Converted dictionary rows to student class objects.
# DallenT,3.25.2026,Added properties and private attributes
# DallenT,3.25.2026,Moved classes into a modules
# DallenT,3.25.2026,Moved classes into separate modules
# ------------------------------------------------------------------------------------------------- #

import processing_classes as proc
import presentation_classes as pres
from data_classes import Employee

# Constants -------------------------------------------- #
FILE_NAME: str = 'EmployeeRatings.json'
MENU: str = '''
    ---- Employee Ratings ------------------------------
      Select from the following menu:
        1. Show current employee rating data.
        2. Enter new employee rating data.
        3. Save data to a file.
        4. Exit the program.
    --------------------------------------------------
    '''
# Variables -------------------------------------------- #
employees: list = []  # a table of employee data
menu_choice = ''

# Beginning of the main body of this script
employees = proc.FileProcessor.read_employee_data_from_file(file_name=FILE_NAME,
                                                            employee_data=employees,
                                                            employee_type=Employee)  # Note this is the class name (ignore the warning)
# Repeat the following tasks
while True:
    pres.IO.output_menu(menu=MENU)
    menu_choice = pres.IO.input_menu_choice()

    if menu_choice == "1":  # Display current data
        try:
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "2":  # Get new data (and display the change)
        try:
            employees = pres.IO.input_employee_data(employee_data=employees,
                                                    employee_type=Employee)  # Note this is the class name (ignore the warning)
            pres.IO.output_employee_data(employee_data=employees)
        except Exception as e:
            pres.IO.output_error_messages(e)
        continue

    elif menu_choice == "3":  # Save data in a file
        try:
            proc.FileProcessor.write_employee_data_to_file(file_name=FILE_NAME, employee_data=employees)
            print(f"Data was saved to the {FILE_NAME} file.")
        except Exception as e:
            pres.IO.output_error_messages("Error saving data.", e)
        continue

    elif menu_choice == "4":  # End the program
        print("Goodbye!")
        break  # out of the while loop
