# Solent Computer Repairs

print("***********************")
print("Solent Computer Repairs")
print("***********************")

customers = [["John", "notebook", "screen"], ["William", "processor", "high usage"],
             ["Catherine", 'monitor', 'no output'], ["Bridget", 'mouse', 'wireless connection'],
             ["Jim", 'gpu', 'directx'], ["Maciej", 'phone', 'screen']]


def booking():
    print("\nPlease enter Customer details!")
    customer_name = input("Customer name: ")
    item = input("Item: ")
    fault_description = input("Fault description: ")

    customer_list = [customer_name, item, fault_description,]
    customers.append(customer_list)

    print(customers)
    return customers


def search_booking():
    customer = str(input("Which customer would you like to search for: ?"))
    if customer in customers[0]:
        print(customer)
        return customers


def insertion_sort():
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
    if len(customers) <= 1:
        return customers
    # Find the middle point and divide it
    middle = len(customers) // 2
    left_list = customers[:middle]
    right_list = customers[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))


# Merge the sorted halves

def merge(left_half, right_half):
    listm = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0][1] < right_half[0][1]:
            listm.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            listm.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        listm = listm + right_half
    else:
        listm = listm + left_half
    return listm


def delete_repair():
    items = input("Enter the item you want to delete: ")
    print(customers)
    for data in customers:
        if items == customers[0][1]:
            customers.remove(data)
            print("This repair has been recorded")
        else:
            print("This item is not in the list")
        return customers


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
        insertion_sort()

    elif option == '4':
        print("\noption 4 has been selected")
        print(merge_sort(customers))

    elif option == '5':
        print("\noption 5 has been selected")
        delete_repair()

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
