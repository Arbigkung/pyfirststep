class Employee(object):
    def __init__(self, first, last, a_salary):
        self.fist_name = first        
        self.last_name = last
        self.annual_salary = a_salary
    
    def give_raise(self, adds=5000):
        self.annual_salary += adds
