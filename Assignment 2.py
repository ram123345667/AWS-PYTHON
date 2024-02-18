#Refer capitalize function in shared program files, replicate .upper() and .lower() functions
def capitalize_custom(string):
    
    if len(string) > 0:
        return string[0].upper() + string[1:]
    else:
        return string

def upper_custom(string):
   
    return string.upper()

def lower_custom(string):
   
    return string.lower()


original_string = "hello world"
capitalized_string = capitalize_custom(original_string)
uppercased_string = upper_custom(original_string)
lowercased_string = lower_custom(original_string)

print("Original:", original_string)
print("Capitalize:", capitalized_string)
print("Upper:", uppercased_string)
print("Lower:", lowercased_string)


#Create a odd sequence from given sequence [1,2,34,65,1,2,65,66,44,33,22,87,123412,09,78,76]
original_sequence = [1, 2, 34, 65, 1, 2, 65, 66, 44, 33, 22, 87, 123412, 9, 78, 76]

odd_sequence = [num for num in original_sequence if num % 2 != 0]

print("Original Sequence:", original_sequence)
print("Odd Sequence:", odd_sequence)



#{‘apple’: 10, ‘mango’: 20, ‘pineapple’: 25, ‘orange’: 30, ‘strawberry’: 50, ‘jackfruit’: 10}
Generate a comprehension fruits which has more than 20
original_dict = {'apple': 10, 'mango': 20, 'pineapple': 25, 'orange': 30, 'strawberry': 50, 'jackfruit': 10}


fruits = {key: value for key, value in original_dict.items() if value > 20}

print("Original Dictionary:", original_dict)
print("Fruits with more than 20:", fruits)

