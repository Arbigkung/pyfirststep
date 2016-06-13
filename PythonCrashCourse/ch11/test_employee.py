import unittest
from Employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self): 
        self.name = 'Pawat'
        self.last = 'Biggy'
        self.a_salary = 5000
        self.custom = 7000
        self.my_employee = Employee(self.name, self.last, self.a_salary)

    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(10000, self.my_employee.annual_salary)
    
    def test_give_custom_raise(self):
        self.my_employee.give_raise(adds=self.custom)
        self.assertEqual(12000, self.my_employee.annual_salary)
        

unittest.main()
