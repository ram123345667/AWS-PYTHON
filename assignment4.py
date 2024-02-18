#String Manipulation

name = "some name"

upper_name = name.upper()

lower_name = name.lower()

capitalized_name = name.capitalize()

modified_name = name.replace('e', 'E')

print("Original Name:", name)
print("Uppercase:", upper_name)
print("Lowercase:", lower_name)
print("Capitalized:", capitalized_name)
print("Modified (Replace):", modified_name)

#List Manipulation
L = [1, 2, 3]

L.extend([5, 6, 7])

del L[4]

print("Original List:", L)

# Dictionary Manipulation
d = {'mango': 10, 'banana': 0, 'apple': 15, 'orange': 0, 'pineapple': 20}

d = {fruit: quantity for fruit, quantity in d.items() if quantity > 0}

d['mango'] = 15
d['pineapple'] -= 5

removed_item = d.pop('banana', None)

print("Updated Dictionary:", d)
print("Removed Item:", removed_item)

#Set Manipulation
s = {1, 2, 3, 4, 5}

s.discard(3)

s.remove(5)

print("Updated Set:", s)
