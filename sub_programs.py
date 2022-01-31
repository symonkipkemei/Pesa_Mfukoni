def add_pesa_purpose():
    """Highlight all possible uses of money that the user can handpick at any
    particular time. The purpose should be referenced by an index to make it easier to pick the correct option,
    minimise on errors and save time. The user can also add new purpose."""

    pesa_dict = {}
    correct = True
    while correct:
        print("Adjust Pesa_dictionary\n"
              "1) Insert new purpose\n"
              "2) quit")
        select = int(input("insert option: "))
        data = ''

        if select == 1:
            index = int(input("insert_index:"))
            purpose = str.upper(input("insert the use of money:"))
            data = str(index) + "," + str(purpose) + "\n"
            with open("pesa_purpose.csv", "a") as f:
                f.write(data)

        elif select == 2:
            for x in data:
                print(x)
            correct = False

        else:
            print("Wrong input, Try again")


add_pesa_purpose()


def pesa_purpose():
    """ The following function reads the pesa purpose csv and converts into a dictionary.
    It then display the dictionary for the user to select which purpose wants to be recorded"""

    pesa_dict = {}



