# ------------------------------------------------------------------------------------------------- #
# Title: processing_classes.py
# Description: Logic for processing Employee data via JSON files
# ChangeLog: (Who, When, What)
# DallenT, 3.25.2026, Created processing classes Script
# ------------------------------------------------------------------------------------------------- #
import json

class FileProcessor:
    """
    A collection of processing layer functions that work with Json files
    """

    @staticmethod
    def read_employee_data_from_file(file_name: str, employee_data: list, employee_type: object):
        """ This function reads data from a json file and loads it into a list of dictionary rows

        ChangeLog: (Who, When, What)
        DallenT,3.25.2026,Created function

        :param file_name: string data with name of file to read from
        :param employee_data: list of dictionary rows to be filled with file data
        :param employee_type: a reference to the Employee class
        :return: list
        """
        try:
            with open(file_name, "r") as file:
                list_of_dictionary_data = json.load(file)
                for employee in list_of_dictionary_data:
                    employee_object = employee_type()
                    employee_object.first_name = employee["FirstName"]
                    employee_object.last_name = employee["LastName"]
                    employee_object.review_date = employee["ReviewDate"]
                    employee_object.review_rating = employee["ReviewRating"]
                    employee_data.append(employee_object)
        except FileNotFoundError:
            pass  # Allow program to start even if file doesn't exist yet
        except Exception as e:
            raise e
        return employee_data

    @staticmethod
    def write_employee_data_to_file(file_name: str, employee_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        DallenT,3.25.2026,Created function

        :param file_name: string data with name of file to write to
        :param employee_data: list of dictionary rows to be writen to the file

        :return: None
        """
        try:
            list_of_dictionary_data: list = []
            for employee in employee_data:
                # Create a dictionary from the object properties
                employee_json: dict = {
                    "FirstName": employee.first_name,
                    "LastName": employee.last_name,
                    "ReviewDate": employee.review_date,
                    "ReviewRating": employee.review_rating
                }
                list_of_dictionary_data.append(employee_json)

            with open(file_name, "w") as file:
                json.dump(list_of_dictionary_data, file, indent=2)
        except Exception as e:
            raise e