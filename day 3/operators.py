import sys

age = 0
height = 0.0
store = 1j

base = input('Enter base: ')
height = input('Enter height: ')
area = 0.5 * float(base) * float(height)
print('Area of triangle is: ', area)

a_side = input('Enter side a: ')
b_side = input('Enter side b: ')
c_side = input('Enter side c: ')
triangle_perimeter = float(a_side) + float(b_side) + float(c_side)
print('The perimeter of the triangle is: ', triangle_perimeter)

rectangle_width = input('Enter width: ')
rectangle_length = input('Enter length: ')
rectangle_area = float(rectangle_width) * float(rectangle_length)
rectangle_perimeter = 2 * (float(rectangle_width) + float(rectangle_length))
print('Area of rectangle is: ', rectangle_area)
print('Perimeter of rectangle is: ', rectangle_perimeter)

circle_radius = input('Enter radius: ')
circle_area = 3.14 * float(circle_radius) ** 2
circle_circumference = 2 * 3.14 * float(circle_radius)
print('Area of circle is: ', circle_area)
print('Circumference of circle is: ', circle_circumference)

'''
8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
10.Compare the slopes in tasks 8 and 9.
'''
slope = 2
x_intercept = 1  # x-intercept is where y=0, so 0 = 2x -2 => x = 1
y_intercept = -2  # y-intercept is where x=0, so y = 2(0) -2 => y = -2

print('Slope:', slope)
print('X-intercept:', x_intercept)
print('Y-intercept:', y_intercept)


point1 = (2, 2)
point2 = (6, 10)

slope_9 = (point2[1] - point1[1]) / (point2[0] - point1[0])
euclidean_distance = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
print('Slope between points (2, 2) and (6, 10):', slope_9)
print('Euclidean distance between points (2, 2) and (6, 10):', euclidean_distance)


if slope == slope_9:
    print('The slopes are equal.')  
else:
    print('The slopes are not equal.')
    
'''
11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
'''
x_values = [-3, -2, -1, 0, 1, 2, 3]

for x in x_values:
    y = x ** 2 + 6 * x + 9
    print(f'For x = {x}, y = {y}')
    if y == 0:
        print(f'y is 0 at x = {x}')
    
'''
12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.
13. Use and operator to check if 'on' is found in both 'python' and 'dragon'
'''
word_python = 'python'
word_dragon = 'dragon'
length_python = len(word_python)
length_dragon = len(word_dragon)
print('Length of "python":', length_python)
print('Length of "dragon":', length_dragon)
if length_python == length_dragon:
    print('The lengths of "python" and "dragon" are equal.')
elif length_python > length_dragon:
    print('The length of "python" is greater than "dragon".')
else:
    print('The length of "dragon" is greater than "python".')

if 'on' in word_python and 'on' in word_dragon:
    print('"on" is found in both "python" and "dragon".')
else:
    print('"on" is not found in both "python" and "dragon".')
    
'''
14. "I hope this course is not full of jargon." Use in operator to check if jargon is in the sentence.
'''
sentense = 'I hope this course is not full of jargon.'
if 'jargon' in sentense:
    print('Word "Jargon" is in the sentense: ', sentense)
else:
    print('Word "Jargon" is not in the sentense: ', sentense)


'''
15. There is no 'on' in both dragon and python
'''
print('Is "on" not in both "dragon" and "python"?', 'on' not in word_python and 'on' not in word_dragon)


'''
16. Find the length of the text python and convert the value to float and convert it to string
'''
length_word_python = len(word_python)
length_as_float = float(length_word_python)
print('Length of "python" as float:', length_as_float)
length_as_string = str(length_as_float)
print('Length of "python" as string:', length_as_string)

'''
17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
19. Check if type of '10' is equal to type of 10
20. Check if int('9.8') is equal to 10
21. Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
'''

#Task 17
number = int(input('Enter a number: '))
if number % 2 == 0:
    print(f'{number} is an even number.')
else:
    print(f'{number} is an odd number.')

#Task 18
floor_division = 7 // 3
int_value = int(2.7)
print('Is floor division of 7 by 3 equal to int converted value of 2.7?', floor_division == int_value)

#Task 19
print('Is type of "10" equal to type of 10?', type('10') == type(10))

#Task 20
print('Is int("9.8") equal to 10?', int(float('9.8')) == 10)

#Task 21
hours = float(input('Enter hours worked: '))
rate_per_hour = float(input('Enter rate per hour: '))
pay = hours * rate_per_hour
print('Pay of the person is: ', pay)
