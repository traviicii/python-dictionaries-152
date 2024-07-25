# Lecture Notes: Python Dictionaries
## #1 What are Dictionaries?
- Mutable Datatype: You can add, mutate, and remove data from them.
- Key-Value Pairs: Like labeled jars, each key has a corresponding value.
- Organized Storage: An intuitive way to store data.
- Key-Value Pairs
- Keys:
    - Must be unique.
    - Note: If you use a duplicate key, the last assigned value will be kept.
    - Typically strings, but can be other **immutable** data types (e.g., numbers, tuples).
- Values:
    - Can be any data type.
- Flexible and can change over time.
- Associating Keys → Values: 
    - Use the key to access the value.

### Creating Python Dictionaries
#### Empty Dictionary:

```python
# Creates an empty dictionary ready to be populated.
student_grades = {}
```

#### Populated Dictionary:

```python
# Creates a dictionary with three key-value pairs.
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
```

### Accessing Elements
#### Using Keys:

```python
# Access values by specifying its key in square brackets.
alice_grade = student_grades["Alice"]
print(alice_grade)  # Output: 85
```

#### KeyError Example:

```python
#If the key doesn’t exist, a KeyError will be raised.
david_grade = student_grades["David"]
# This will raise a KeyError because "David" is not a key in student_grades
```

#### Using `.get()` to Avoid KeyErrors:

```python
# .get(<key>, <value returned if key doesn't exist>) returns the value if the key exists, otherwise it returns a default value.
david_grade = student_grades.get("David", "Not found")
print(david_grade)  # Output: Not found
```

## #2 Adding and Updating Elements
#### Adding a New Key-Value Pair:

```python
student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Add a new key-value pair to the dictionary.
student_grades["David"] = 88
print(student_grades)  # Output: {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 88}
```

#### Updating an Existing Key:

```python
student_grades["Alice"] = 90
print(student_grades)  # Output: {'Alice': 90, 'Bob': 92, 'Charlie': 78, 'David': 88}
Note: Updates the value associated with an existing key.
```

#### Using .update():

```python
# Merges another dictionary into the existing dictionary, updating keys as needed.
student_grades.update({"Eve": 95})
print(student_grades)  # Output: {'Alice': 90, 'Bob': 92, 'Charlie': 78, 'David': 88, 'Eve': 95}
```

#### Further examples for adding and updating
```python
kitchen = {
    'drawer': 'silver ware', 
    "pantry": 'snacks', 
    'cabinet': 'plates',
    'drawer': 'socks'
    }
#-- add a key-value pair

#dictionary[new_key] = new_value
kitchen['fridge'] = 'cold stuff'
print(kitchen)

kitchen['freezer'] = 'frozen stuff'
print(kitchen)

#-- updating the value of a key

#dictionary[existing_key] = new_value
kitchen['cabinet'] = 'plates and bowls'
print(kitchen)


#-- incrementing values

stock = {'oranges': 10, 'apples': 2, 'pears':20}

#need to restock on apples need 10 more
stock['apples'] += 10
print(stock)

#-- decrementing values

#no one is buying my pears and they're rotting need to throw out 5
stock['pears'] -= 5
print(stock)

#---- .update({key, value}) : merges one dictionary into another, 
#updating any common keys to the new_values

car = {"year" : 1968, 'Make': 'Ford', 'Model': 'Mustang'}

car.update({"color": 'green'}) #adding kvps with .update()
print(car)

car.update({'color': 'black'}) #updating kvps with .update()
print(car)

car.update({'wheels': 4, 'engine': 'v8', 'year': 2024}) #adding and updating multiple things with .update()
print(car)
```

## #3 Removing from Dictionary
#### Using `.pop()`:

```python
# Removes the specified key and returns its value. If the key doesn’t exist, returns a default value.
bob_grade = student_grades.pop("Bob", "Not found")
print(bob_grade)  # Output: 92
print(student_grades)  # Output: {'Alice': 90, 'Charlie': 78, 'David': 88, 'Eve': 95}
```

#### Using .popitem():

```python
# Removes and returns the last key-value pair as a tuple.
last_item = student_grades.popitem()
print(last_item)  # Output: ('Eve', 95)
print(student_grades)  # Output: {'Alice': 90, 'Charlie': 78, 'David': 88}
```

#### Using del:

```python
# Deletes the key-value pair from the dictionary.
del student_grades["Charlie"]
print(student_grades)  # Output: {'Alice': 90, 'David': 88}
```

#### Using .clear():

```python
# Removes all key-value pairs from the dictionary, leaving it empty.
student_grades.clear()
print(student_grades)  # Output: {}
```

## #4 Iterating Over Dictionaries

#### Using .items():

```python
student_grades = {"Alice": 90, "Bob": 92, "Charlie": 78}

items = student_grades.items() # returns each key-value pair as a tuple
print(items)

# Iterates over key-value pairs
for student, grade in student_grades.items():
    print(f"{student}: {grade}")
# Output:
# Alice: 90
# Bob: 92
# Charlie: 78
```

#### Using .keys():

```python
# Iterates over the keys in the dictionary.
for student in student_grades.keys():
    print(student)
# Output:
# Alice
# Bob
# Charlie
```

#### Using .values():

```python
# Iterates over the values in the dictionary.
for grade in student_grades.values():
    print(grade)
# Output:
# 90
# 92
# 78
```

#### Further Examples for Iterating/Looping

```python
chips = {
"Cheeto": "Flamin Hot", 
"Dorito": "Cool Ranch", 
"Takis":'Fuego', 
"Miss Vickies": "Spicy Dill Pickle"
}

#looping keys of a dictionary
#---- .keys() : be explicit

print("Major Chip Brands")
print("-----------------")
for key in chips.keys():
    print('Key', key)
    print('Value', chips[key])


#looping over values of a dictionary
#----- .values()

print("\nFlavors")
print("--------------")
for value in chips.values():
    print(value)


#looping over both keys and value at the same time

print('\nMy favorite flavor per chip')
print("--------------")
for key, value in chips.items():
    print(f'My favorit {key} flavor is {value}!')
```

## #5 Nesting with Dictionaries


#### Lists Inside Dictionaries:

```python
#lists inside Dictionaries

pet_names ={
    'Dogs': ['Oreo', 'Bailey', 'Fido', 'Punkin', 'Baby', 'Trouble'],
    'Cats': ['Mittens', 'CatKeisha', 'Snowball', 'Cookie', 'Smokey'],
    'Hamster': ['Cheddars', 'Hamtarro', 'Lightning', 'Turbo', 'Hammie'],
    'Lizards': 'Lizzy'
}

#we can chain keys and indices one after another
print(pet_names['Cats'][3])

for pet, names in pet_names.items():
    print(f'\nCommon {pet} names:')
    if isinstance(names, list):
        for name in names:
            print(name)
    else:
        print(names)

# Useful for storing multiple values under a single key.
student_subjects = {
    "Alice": ["Math", "Science", "History"],
    "Bob": ["English", "Art", "Music"]
}
```

#### Dictionaries Inside Lists:

```python
books = [
    {'Title': 'Diary of a Wimpy Kid', 'Author': 'Jeff Kiney', 'Genre': 'YAF'},
    {'Title': 'Rich Dad Poor Dad', 'Author': 'Robert Kiwaske', 'Genre': 'Self Help'},
    {'Title': 'Dune', 'Author': 'Frank Herbert', 'Genre': 'Science Fiction'}
]

#we can chain keys and indices one after another
print(books[0]['Author'])

for book in books:
    print(f'{book["Title"]} is written by {book["Author"]}')

# Another example
# Useful for storing multiple dictionaries in a list.
library = [
    {"title": "1984", "author": "George Orwell"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee"}
]
```

#### Dictionaries Inside Dictionaries:

```python
user = {
    'dk@email.com': {'username': 'dylank' , 'password': '12345', 'likes': ['tacos', 'dogs']},
    'tp@email.com': {'username': 'travisp', 'password': '67890', 'likes': ['key lime pie', 'walks on the beach']},
    'ck@catmail.com': {'username': 'catkeisha', 'password':'password', 'likes': ['treats', 'walks on the beach']}
}

print(user['tp@email.com']['likes'][0])


def login(user_dict):

    while True:
        try:
            email = input('email: ')
            password = input('password: ')
            user = user_dict[email]
            if password != user['password']:
                raise ValueError
        except:
            print('invalid email or password')
        else:
            print(f'Welcome back {user["username"]}')
            break


login(user)


# Useful for organizing related data in a hierarchical structure.
company = {
    "employees": {
        "John": {"age": 30, "department": "HR"},
        "Jane": {"age": 25, "department": "IT"}
    },
    "departments": {
        "HR": {"head": "John", "budget": 50000},
        "IT": {"head": "Jane", "budget": 100000}
    }
}
```

Assign Module 2 Mini-Project