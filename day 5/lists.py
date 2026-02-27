import sys, math

'''
There are four collection data types in Python :

    - List: is a collection which is ordered and changeable(modifiable). Allows duplicate members.
    - Tuple: is a collection which is ordered and unchangeable or unmodifiable(immutable). Allows duplicate members.
    - Set: is a collection which is unordered, un-indexed and unmodifiable, but we can add new items to the set. Duplicate members are not allowed.
    - Dictionary: is a collection which is unordered, changeable(modifiable) and indexed. No duplicate members.
'''

'''
    Exercice 1
'''

empty_list = []
list_of_items = ['item1', 'item2', 'item3', 'item4', 'item5']

for list in [empty_list, list_of_items]:
    print(f'{list} is of type {type(list)} and has length {len(list)}')

first_item = list_of_items[0]
middle_item = list_of_items[math.floor(len(list_of_items) / 2)]
last_item = list_of_items[-1]

mixed_data_types = ['Simon', 18, 181, {'Single', 'Narnia'}]
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

for item in it_companies:
    print(item)

print(f'The number of companies in the list is {len(it_companies)}')

print(f'The first company is {it_companies[0]}')
print(f'The middle company is {it_companies[math.floor(len(it_companies) / 2)]}')
print(f'The last company is {it_companies[-1]}')

it_companies[0] = 'Meta'
print(it_companies)

it_companies.append('Twitter')
print(it_companies)

it_companies.insert(3, 'LinkedIn')
print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies)

it_companies = '#; '.join(it_companies)
print(it_companies)

print('Facebook' in it_companies)

it_companies = it_companies.split('#; ') #Split the string back into a list in order to move and sort the items
print(it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

it_companies_without_first_three = it_companies[3:]
print(it_companies_without_first_three)

it_companies_without_last_three = it_companies[:-3]
print(it_companies_without_last_three)

it_companies.clear() # to remove all items from the list, we can use clear() method instead of remove() method
print(it_companies)

del it_companies # to delete the list completely, we can use del keyword instead of clear() method
try:
    print(it_companies)
except NameError:
    print('The list it_companies has been deleted and is no longer defined.')
    
