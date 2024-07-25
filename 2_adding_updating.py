# Adding and Updating elements in a dictionary

student_grades = {
    "Alice" : 85, 
    "Bob" : 92, 
    "Charlie" : 78
    }

# adding a new key-value pair
student_grades['David'] = 88
student_grades["Josh"] = 98

print(student_grades)

# Updating existing data within a dictionary
student_grades["Alice"] = 90 # altering the data at the key "Alice" to now = 90
student_grades["Alice"] += 5 # we're just adding 5 to the number already stored in the value at the key of "Alice"
print(student_grades)

# using the .update() method
# Merges another dictionary into the existing dictionary, updates keys if necessary
student_grades.update({"Eve": 95, "Walter": 78, "Charlie": 85, "Alice": 100})

print(student_grades)