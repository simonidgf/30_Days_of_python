'''
Exercise 2: Basic Sintax!
'''
import sys
# Ex. 1, 1)
print(sys.version)
print()

# Ex. 1, 2)
print(3+4)
print(3-4)
print(3*4)
print(3%4)
print(3/4)
print(3**4)
print(3//4)
print()

# Ex. 1, 3)
print('Simon')
print('Fragger')
print('PT')
print('I am enjoying 30 days of Coding')
print()

# Ex. 1, 4)
print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type('Simon'))
print(type('Fragger'))
print(type('PT'))
print()

'''
Exercise 3: Final Level day 1
'''
# Ex. 3, 1)
integer = 10
floating_point = 9.8
complex_number = 4 - 4j
string = 'Simon'
boolean = True
list_ = ['Asabeneh', 'Python', 'Finland']
tuple_ = ('Asabeneh', 'Python', 'Finland')
dictionary = {'first_name': 'Simon', 'last_name': 'Fragger', 'country': 'PT', 'age': 30, 'is_married': False}
set_ = {'Asabeneh', 'Python', 'Finland'}

'''
 Using a for loop, print the type of each of the following variables: 
 integer, floating_point, complex_number, string, boolean, list_, tuple_, dictionary, set_
'''
for iterate in [integer, floating_point, complex_number, string, boolean, list_, tuple_, dictionary, set_]:
    print(type(iterate)) 
    
# Ex. 3, 1)
'''
Find an Euclidean distance between (2, 3) and (10, 8)
'''
import math
starting_point = (2,3)
ending_point = (10,8)
euclidean_distance = math.hypot(ending_point[0] - starting_point[0], ending_point[1] - starting_point[1])
print(euclidean_distance)
    