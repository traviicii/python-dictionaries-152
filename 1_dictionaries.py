# Python Dictionaries

# what are dictionaries?

# Mutable data type : We can add, mutate, and remove data from them
# collection of key-value pairs: like a labled drawer - each drawer has its own contents

# keys
#-- must be unique
#-- typically keys are string, but they can be any IMMUTABLE data type (strings, numbers, tuples)

# values : can be any data type

# big benefit is that dictionaries are flexible and can change over time

# We can use keys to access the data contained in its value

# Empty dictionary
# empty_list = []
empty_dictionary = {}

#populated dictionary

student_grades = {
    "Alice" : 85, 
    "Bob" : 92, 
    "Charlie" : 78
    }


# Accessing elements within a dictionary

# we access values in a dictionary by specifying the key in square brackets
print(student_grades["Alice"])

alice_grade = student_grades["Alice"]
print(alice_grade)

# KeyErrors can occur when trying to access a dictionary at a key that doesn't exist
# david_grade = student_grades["David"]

# can also access dictionaries with .get()

# syntax for .get(<key>, <default return if the key we're looking for isn't found>)

david_grade = student_grades.get("David", "Not found")
print(david_grade)

# using the .get() method prevents us from encountering a KeyError