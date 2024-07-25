from helper import d

# Nesting dictionaries and lists

# lists inside of dictionaries

pet_names = {
    "Dog" : ['Toast', 'Oreo', 'Punkin', 'Pinky', 'Dogue', 'Rover', 'Rex', 'Pluto', 'Fido', 'Trouble'],
    'Cat' : ['Mittens', 'Ziggy', 'Hot Pocket', 'Miso', 'CatKeisha', 'Randolf', 'Snowball', 'Smokey'],
    'Hamster' : ['Hamtarro', 'Lightening', 'Nugget', 'Cheddar', 'Hammie', 'Turbo'],
    'Lizzard' : 'Lizzy'
}

pet_names['Lizzard'] = ['Lizzy', 'Izzy']
# print(pet_names)
miso_index = pet_names['Cat'].index("Miso") # finding the index of "Miso"
print(miso_index)
print(pet_names['Cat'][3]) # we can chain keys and indecies together, similar to nested lists

d()

for pet, names in pet_names.items():
    print(f"\nCommon {pet} names: ")
    if isinstance(names, list):
        for name in names:
            print(name)
    else:
        print(names)

d()

# Dictionaries inside of lists

books = [
    {'Title': 'Diary of a Wimpy Kid', 'Author': "Jeff Kiney", 'Genre': 'YAF'},
    {'Title': 'Rich Dad Poor Dad', 'Author': 'Robert Kiwaske', "Genre": 'Self Help'},
    {'Title': 'Dune', 'Author': 'Frank Herbert', 'Genre': 'Science Ficiton'}
]

# We can chain indecies and keys after one another
print(books[0]['Author'])

for book in books:
    # print(book)
    print(f"{book['Title']} is written by {book['Author']}")

d()

# user database as a dictionary with many different data types inside
user = {
    'dk@email.com' : {'username': 'dylank', 'password': '12345', 'likes': ['dogs', 'tacos']},
    'tp@email.com' : {'username': 'traviicii', 'password': '67890', 'likes': ['key lime pie', 'long walks on the beach']},
    'toast@email.com': {'username': 'toaster-struddle', 'password': 'iamadawg', 'likes': ['treats', 'walks to the park']}
}

print(user['tp@email.com']['likes'][0])


# Creating a login function using the user "database" dictionary above.
def login(user_dict):
    while True:
        try:
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            user = user_dict[email]
            if password != user['password']:
                raise ValueError
        except Exception as e:
            print(e)
            print("Invalid email or password")
        else:
            print(f"Welcome back {user['username']}")
            break

login(user)