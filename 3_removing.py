from helper import d

# Removing key-value pairs from a dictionary

student_grades = {
    "Alice" : 85, 
    "Bob" : 92, 
    "Charlie" : 78
    }

# using .pop() : removes the specified key and return its value. If the key doesn't exist it will return a default value that we specify
# bob_grade = student_grades.pop("Bob", "Not found")
# print(bob_grade)
# print(student_grades)

d()

# Using .popitem() removes and returns the last key-value pair as a tuple
# last_item = student_grades.popitem()
# print(last_item)
print(student_grades)

d()

# using del
# delete the key-value pair from the dictionary, with no return value
del student_grades["Charlie"]
print(student_grades)

# Using .clear() : Removes all key-value pairs from the dictionary, leaving it empty
student_grades.clear()
print(student_grades)