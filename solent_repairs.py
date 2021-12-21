# Solent Computer Repairs

print("***********************")
print("Solent Computer Repairs")
print("***********************")

customers = []


def booking():
    print("\nPlease enter Customer details!")
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


def insertion_sort(customers):
    global i
    for index in range(1, len(customers)):
        value = customers[index]
        i = index - 1
        while i >= 0:
            if value < customers[i]:
                customers[i + 1] = customers[i]
                customers[i] = value
                i = i - 1
            else:
                break
    print(customers)


def merge_sort(customers):
    global i
    size = len(customers)
    if len(customers) > 1:
        mid = size // 2
        left = customers[:mid]
        right = customers[mid:]  # Recursive call on each half
        merge_sort(left)
        merge_sort(right)
        # variables for traversing the left and right half
        i = 0
        j = 0
        # variable for the main list
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                # The value from the left half has been used
                customers[k] = left[i]  # Move the iterator forward
                i += 1
            else:
                customers[k] = right[j]
                j += 1
                k += 1
        # For all the remaining values
        while i < len(left):
            customers[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            customers[k] = right[j]
            j += 1
            k += 1


def enquiries():
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


def show_menu():
    print("[1] Book item")
    print("[2] search for a specific item by the customer")
    print("[3] display all items booked for repair, sorted by customer name")
    print("[4] search for an item by customer name")
    print("[5] delete a specific item")
    print("[6] answer enquiries")
    print("[7] exit")

    return input("\nWhat would you like to do: ?")


loop = True

while loop:

    option = show_menu()

    if option == '1':
        print("\noption 1 has been selected")
        booking()
        print("\nWould you like to book another?:")

    elif option == '2':
        print("\noption 2 has been selected")
        search_booking()

    elif option == '3':
        print("\noption 3 has been selected")
        insertion_sort(customers)

    elif option == '4':
        print("\noption 4 has been selected")
        merge_sort(customers)

    elif option == '5':
        print("\noption 5 has been selected")

        print("\nEnter id to delete a booking")
        item = input()
        for i in customers[:]:
            if i[2] == item:
                customers.remove(i)
                print(customers[:])

    elif option == '6':
        print("\noption 6 has been selected")
        enquiries()

    elif option == '7':
        print("\noption 7 has been selected. Good bye!")
        loop = False  # This will make the while loop to end as not value of loop is set to False
    else:
        print("\nWrong option selected! Please choose a valid option!")


def run():
    show_menu()


run()
