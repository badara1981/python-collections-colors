fruit_colors = {
    "apple": "red",
    "berries": "blue"
}

for color in fruit_colors:
    print(f'the color of the {color}is the {fruit_colors.get(color)}')
    print(fruit_colors.keys())

for k in fruit_colors.keys():
    print(k)

    print(fruit_colors.keys())
    print(fruit_colors.values())

    ## copy 

badara1 = {'b': 300, 'a': 400, 'd': [1, 2, 3]}
badara2 = badara1.copy()
badara2['b'] = 30
badara2['c'] = [1, 2, 3, 4]
print("Original dictionary:", badara1)
print("New dictionary:", badara2)

# How to create in Dictionary
#create a dictionary
my_information = {'name': 'Badara', 'age': 28, 'location': 'Berlin'}

print(my_information)

#check data type
print(type(my_information))

#output

#{'name': 'Badara', 'age': 28, 'location': 'Berlin'}
#<class 'dict'>




# how to in del a Dictionary

my_information = {'name': 'Badara', 'age': 28, 'location': 'Berlin'}

del my_information['location']

print(my_information)

#output

#{'name': 'Badara', 'age': 28}

#Let's see an example of creating a dictionary using fromkeys() without setting a value for all the keys:

#create sequence of strings
cities = ('Paris','Berlin', 'Madrid')

#create the dictionary, `my_dictionary`, using the fromkeys() method
my_dictionary = dict.fromkeys(cities)

print(my_dictionary)

#{'Paris': None, 'Berlin': None, 'Madrid': None}

##Enumerate  method 
days_weeks = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAYS", "FRIDAY" ]
for index,  days in enumerate(days_weeks):
    print(f"{days.capitalize()} is the days in  the week  {index} start = 100 ")
