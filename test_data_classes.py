# ------------------------------------------------------------------------------------------------- #
# Title: Test Data Classes Module
# # Description: A collection of tests for the data classes module
# ChangeLog: (Who, When, What)
# DallenT,3.25.2026,Created Script
# ------------------------------------------------------------------------------------------------- #

import unittest
from data_classes import Employee

class TestEmployee(unittest.TestCase):
    def test_employee_init(self):
        emp = Employee("John", "Doe", "1900-01-01", 5)
        self.assertEqual(emp.first_name, "John")
        self.assertEqual(emp.last_name, "Doe")
        self.assertEqual(emp.review_rating, 5)

    def test_employee_invalid_name(self):
        with self.assertRaises(ValueError):
            Employee("123", "Doe")
        with self.assertRaises(ValueError):
            Employee("John", "123")

    def test_employee_str(self):
        employee = Employee("John", "Doe")
        self.assertEqual(str(employee), "John,Doe,1900-01-01,5")

if __name__ == '__main__':
    unittest.main()