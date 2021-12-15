# Solent Computer Repairs

print("***********************")
print("Solent Computer Repairs")
print("***********************")


def show_menu():
    print("[1] Book item")
    print("[2] search for a specific item by the customer")
    print("[3] display all items booked for repair, sorted by customer name")
    print("[4] search for an item by customer name")
    print("[5] delete a specific item")
    print("[6] answer enquiries")
    print("[7] exit")


loop = True

while loop:
    customers = []

    show_menu()
    option = input("What would you like to do: ?")

    if option == '1':
        print("option 1 has been selected")

        print("Please enter Customer details!")
        customer_name = input("Customer name: ")
        item = input("Item: ")
        fault_description = input("Fault description: ")

        customers.append(customer_name)
        customers.append(item)
        customers.append(fault_description)

        print(customers)

    elif option == '2':
        print("option 2 has been selected")


    elif option == '3':
        print("option 3 has been selected")

    elif option == '4':
        print("option 4 has been selected")

    elif option == '5':
        print("option 5 has been selected")

    elif option == '6':
        print("option 5 has been selected")

    elif option == '7':
        print("option 7 has been selected")
        loop = False  # This will make the while loop to end as not value of loop is set to False
    else:
        print("Wrong option selected! Please choose a valid option!")