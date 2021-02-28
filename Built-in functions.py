# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 16:59:25 2021

@author: irisa
"""

"""
Task 1
Write a program that asks the user to enter comma-separated digits. 
Write data management exceptions. 
Using Python built-in functions output to the screen: 
    sum of digits entered, maximum and minimum values, 
    values which index is between 2 and 4, 
    number of numbers entered, 
    values greater than 10, 
    list in ascending and descending order, 
    and "inverted "list entered.
"""

"""
values = input("Input some comma seprated numbers : ")

digit_list = values.split(",")

lst = []
try:  
    for i in digit_list:
         lst.append(float(i))
    print("The sum of the digits enetered: ", sum(lst))
    print("The max number of the digits enetered: ", max(lst))
    print("The min number of the digits enetered: ", min(lst))
    print("Values which index is between 2 and 4 on the list: ", lst[2:4])
    print("Number of numbers entered: ", len(lst))
    
    print("Values greater than 10 on the list:")
    greater_than_ten = filter(lambda x: x > 10, lst)
    greater_than_ten = list(greater_than_ten)
    
    if(greater_than_ten):
        print(greater_than_ten)
    else:
        print("No values in the list greater than 10")
         
    print("List in ascending order: ", sorted(lst))
    print("List in descending order: ", sorted(lst, reverse=True))

except ValueError:
    print("This is not a number")
    
"""    

"""
Task 2
Sort the list by item length in ascending and descending order.
sort_me = ["Kaunas", "Vilnius", "Alytus", "Klaipeda", "Varena", "Druskininkai", "Klaipeda"]
"""
"""
def Sorting(sort_me): 
    lst = sorted(sort_me, key=len) 
    return lst 
      
# Driver code 
sort_me = ["Kaunas", "Vilnius", "Alytus", "Klaipeda", "Varena", "Druskininkai", "Klaipeda"]
print(Sorting(sort_me)) 
"""

"""
Task 3
Perform list element transformation: 
    1. by using formula: x = x * (x - 10), 
    2. square each element.
 my_list = [12, 45, 23, 56, -546, 34]
"""

"""
def calculate_formula(x):
    
    return x * (x-10)

def calculate_square(n):
    return n * n


my_list = [12, 45, 23, 56, -546, 34]

result = map(calculate_formula, my_list)
print(list(result))

result = map(calculate_square, my_list)
print(list(result))

"""


"""
Task 4
Sort the dictionary according to the second item in the value list in 
ascending and descending order.

 sort_me = { 
     "a": [7, 1, 9], 
     "b": [8, -4, 3],
     "c": [9, 10, 151],
     "d": [-3, 9, 11]
 }
"""
"""
sort_me = {
    "a": [7, 1, 9], 
    "b": [8, -4, 3],
    "c": [9, 10, 151],
    "d": [-3, 9, 11]}

#by adding another [1] in x: x[1][1] we go to the second value
print("Dictionary sorted by ascending order: ")
a = sorted(sort_me.items(), key=lambda x: x[1][1])
print(a)

print("Dictionary sorted by descending order: ")
a = sorted(sort_me.items(), key=lambda x: x[1][1], reverse=True)
print(a)
"""




















