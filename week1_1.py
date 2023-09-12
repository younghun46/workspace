# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 22:16:36 2023

@author: Younghun
"""

class Employee:
    def __init__(self, my_name, my_age):
        self.name = my_name  #self.ane is instance variable
        self.age = my_age
    def display_details(self):
        return f"{self.name} is {self.age} years old"
        
        
emp1 = Employee("James", 25)
#print(emp1.display_details())

emp2 = Employee("BOB", 20)
#print(emp2.display_details())


empl_list = [emp1,emp2]
for i in empl_list:
    print(i.display_details())


class Contract_Employee(Employee):
    def __init__(self, my_name, my_age):
        super().__init__(my_name, my_age)
        
emp3 = Contract_Employee("John",22)
print(emp3.display_details())
