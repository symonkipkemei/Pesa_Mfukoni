def add_pesa_purpose():
    """Highlight all possible uses of money that the user can handpick at any
    particular time. The purpose should be referenced by an index to make it easier to pick the correct option,
    minimise on errors and save time. The user can also add new purpose."""

    global user_purpose, user_index
    import csv

    pesa_dict = {}
    correct = True
    while correct:
        print("\n*************\n"
              "Add purpose(y/n)")
        select = str.lower(input("your choice:"))

        with open("pesa_purpose.csv", "r") as f:
            iterable = csv.reader(f)
            dd_iterable = list(iterable)
            index_list = []
            purpose_list = []
            for item in dd_iterable:
                index_list.append(item[0])
                purpose_list.append(item[1])

        if select == str.lower("y"):
            # check if index is already used
            try_again_index = True
            while try_again_index:
                user_index = str(input("\ninsert index:"))
                if user_index in index_list:
                    print(f"{user_index} already used, try another.")
                elif not user_index.isdigit():
                    print(f"{user_index} is not a digit, try again.")
                else:
                    print(f"{user_index} recorded")
                    try_again_index = False

            # check if purpose already used
            try_again_purpose = True
            while try_again_purpose:
                user_purpose = str.upper(input("insert new purpose:"))
                if user_purpose in purpose_list:
                    print(f"{user_purpose} already used, try again.")
                else:
                    print(f"{user_purpose} recorded")
                    try_again_purpose = False

            # store data
            data = str(user_index) + "," + str(user_purpose) + "\n"
            with open("pesa_purpose.csv", "a") as f:
                f.write(data)

        elif select == str.lower("n"):
            correct = False

        else:
            print("Wrong input, Try again")


def pesa_purpose():
    """ The following function reads the pesa purpose csv and converts into a dictionary.
    It then display the dictionary for the user to select which purpose wants to be recorded"""

    import csv
    global purpose

    pesa_dict = {}

    with open("pesa_purpose.csv", "r") as f:
        iterable = csv.reader(f)
        list_iterable = list(iterable)
        for x in list_iterable:
            print(f"{x[0]}. {x[1]}")
            pesa_dict[int(x[0])] = x[1]

    user_selection = int(input("Insert option above: "))

    for x in pesa_dict:
        if user_selection == x:
            purpose = pesa_dict[x]

    return purpose

