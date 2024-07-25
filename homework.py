from helper import clear


service_tickets = {
    1: {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    2: {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def next_id(): # return an ID I can use to make a new service ticket
    last_id = 0
    for id in service_tickets.keys():
        if id > last_id:
            last_id = id
    return last_id + 1

def new_ticket(): # function for creating a new ticket
    new_id = next_id()
    while True:
        customer = input("Please enter the customer name: \n")
        issue = input("Please state the issue: \n")
        print(f"Customer: {customer}, Issue: {issue}")
        correct = input("Is this information correct? (y/n)").lower()
        if correct == 'y': # create a new ticket
            service_tickets[new_id] = {'Customer': customer, 'Issue': issue, 'Status': 'open'}
            break
        else:
            clear()
            continue

def main():
    while True:
        ans = input('''
SERVICE TICKET MANAGER
Enter the corresponding number for the action you'd like to take:
    1 - Open a new service ticket.
    2 - Update a service ticket.
    3 - Display all service tickets.
    4 - Quit
''')
        if ans == '1':
            clear()
            new_ticket()
        elif ans == '2':
            pass # function to update a ticket
        elif ans == '3':
            print(service_tickets) # function to display all tickets
        elif ans == '4':
            print("Thanks for making service tickets and stuff like that. Have a great day!")
            break
        else:
            print("Enter the right number fool!")

main()