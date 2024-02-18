#Write Examples code for concatenation
#String Concatenation
str1 = "Hello"
str2 = "World"
result_string = str1 + " " + str2

print(result_string)

#List Concatenation
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result_list = list1 + list2

print(result_list)

name = "John"
age = 25
result_sentence = "My name is " + name + " and I am " + str(age) + " years old."

print(result_sentence)

initial_list = [1, 2, 3]
new_element = 4
result_list = initial_list + [new_element]

print(result_list)



#Write one Examples for each formatting techniques
#String Formatting
name = "Alice"
age = 30
formatted_string = "My name is %s and I am %d years old." % (name, age)

print(formatted_string)

name = "Bob"
age = 25
formatted_string = f"My name is {name} and I am {age} years old."

print(formatted_string)


name = "Charlie"
age = 22
formatted_string = "My name is {} and I am {} years old.".format(name, age)

print(formatted_string)



#Go Through Reference site and apply various options into formatting techniques

amount = 123.456
formatted_amount = "%.2f" % amount  # Two decimal places
print(formatted_amount)

value = 42.5678
formatted_value = "{:^10.2f}".format(value)  # Center-aligned, two decimal places
print(formatted_value)



#Write example for each arithmetic operators
#Addition
a = 10
b = 5
result = a + b
print(result)

#Subtraction
a = 10
b = 5
result = a - b
print(result)

#Multiplication
a = 10
b = 5
result = a * b
print(result)

#Division
a = 10
b = 5
result = a / b
print(result)

#Floor Division (//)
a = 10
b = 3
result = a // b
print(result)

#Modulus (%)
a = 10
b = 3
result = a % b
print(result)

#Exponentiation (**)
a = 2
b = 3
result = a ** b
print(result)



#Write Example for assignment operators (except: = & +=)
#Subtraction Assignment (-=)
a = 10
b = 5
a -= b
print(a)

#Multiplication Assignment (*=)
a = 3
b = 4
a *= b
print(a)

#Division Assignment (/=)
a = 15
b = 3
a /= b
print(a)

#Floor Division Assignment (//=)
a = 17
b = 3
a //= b
print(a)

#Modulus Assignment (%=)
a = 20
b = 7
a %= b
print(a)

#Exponentiation Assignment (=)
a = 2
b = 3
a **= b
print(a)




