# Solent Computer Repairs

print("***********************")
print("Solent Computer Repairs")
print("***********************")

customers = []


def booking():
    print("Please enter Customer details!")
    customer_name = input("Customer name: ")
    item = input("Item: ")
    fault_description = input("Fault description: ")

    customer_list = [customer_name, item, fault_description]
    customers.append(customer_list)

    print(customers)
    return customers


def search_booking():
    customer = str(input("Which customer would you like to search for: ?"))
    if customer in customers:
        print(customer)


def show_menu():
    print("[1] Book item")
    print("[2] search for a specific item by the customer")
    print("[3] display all items booked for repair, sorted by customer name")
    print("[4] search for an item by customer name")
    print("[5] delete a specific item")
    print("[6] answer enquiries")
    print("[7] exit")

    return option


loop = True

while loop:

    option = input("\nWhat would you like to do: ?")

    if option == '1':
        print("\noption 1 has been selected")
        booking()
        print("\nWould you like to book another?:")

    elif option == '2':
        print("\noption 2 has been selected")
        search_booking()

    elif option == '3':
        print("\noption 3 has been selected")

    elif option == '4':
        print("\noption 4 has been selected")

    elif option == '5':
        print("\noption 5 has been selected")

        print("\nEnter id to delete a booking")
        input1 = input()
        for i in customers[:]:
            if i[3] == input1: 2
            customers.remove(i)
            print(customers[:])

    elif option == '6':
        print("\noption 6 has been selected")
        queue = ['My computer is running slow – what can I do about it?',
                 'Which web browser would you recommend, and why?',
                 'Can you recommend the PC build for gamer?',
                 'Why there is no audio output?']

        # Removing elements from the queue
        print("\nEnquiries answered")
        print(queue.pop(0))
        print(queue.pop(0))
        print(queue.pop(0))
        print(queue.pop(0))

        print("\nAll enquiries answered")
        print(queue)

    elif option == '7':
        print("\noption 7 has been selected. Good bye!")
        loop = False  # This will make the while loop to end as not value of loop is set to False
    else:
        print("\nWrong option selected! Please choose a valid option!")


def run():
    show_menu()


run()
