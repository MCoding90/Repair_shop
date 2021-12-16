

def search_repair_book():
    print(f"Please specify what data you are entering, if you wish to display all or go back to main menu: \n"
          f"[1] A customer name. \n"
          f"[2] An item type. \n"
          f"[3] A description. (Not Recommended) \n" 
          f"[4] An ID number. \n"
          f"[5] Display all items booked for repair. \n" 
          f"[6] Go back to the main menu. "
          f"Please enter your selection: ")
    srb_input1 = int(input())

    if srb_input1 == range(1, 4):
        print(f"Please enter the data: ")
        srb_input2 = str(input())
        for i in repair_book:
            if i[(srb_input1-1)] == srb_input2.strip():
                print(i)
    elif srb_input1 == 5:
        for i in repair_book:
            print(i)
    elif srb_input1 == 6:
        main_menu()
    else:
        print("Please enter a valid input. \n"
              "Function Reloading... \n")
        search_repair_book()