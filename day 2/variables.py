#Day 2: 30 Days of python programming
import math, sys

first_name = 'Simon'
last_name = 'Fragger'
full_name = first_name + ' ' + last_name
country = 'PT'
city = 'Lisbon'
age = 30
year = 2024
is_married = False
is_true, is_light_on = True, True

for var in [first_name, last_name, full_name, country, city, age, year, is_married, is_true, is_light_on]:
    print('Type ', var, ':',type(var))
    
for var in [first_name, last_name]:
    print('Length of', var, ':', len(var))

num_one, num_two = 5, 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
floor_division = num_one // num_two
remainder = num_one % num_two
exp = num_one ** num_two


radius = 30
area_of_circle = math.pi * (num_one ** 2)
circumference_of_circle = 2 * math.pi * float(radius)
print('Area of circle with radius ', radius, ':', area_of_circle)
print('Circumference of circle with radius ', radius, ':', circumference_of_circle)  

input_radius = input('Enter radius: ')
area_of_circle_input = math.pi * (float(input_radius) ** 2)
print('Area of circle with radius ', input_radius, ':', area_of_circle_input)
print()
print('Forms:')
first_name = input('Enter first name: ')
last_name = input('Enter last name: ')
country = input('Enter country: ')
age = input('Enter age: ')
print('First name: ', first_name)   
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)

print(help('keywords'))