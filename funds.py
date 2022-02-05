def new_net_fund_size(previous_net_fund_size):
    "edit the previous net_fund_size based on the new fund size and type of funds the user enters"
    fund_size = int(input("insert amount:"))
    net_fund_size = int(previous_net_fund_size)

    fund_type_dict = {"e": "EXPENDITURE", "i": "INCOME"}

    print("Expenditure(e) or Income(i) ")
    user_selection = input("insert option (e/i):")

    if user_selection == "e":
        net_fund_size -= fund_size

    elif user_selection == "i":
        net_fund_size += fund_size
    else:
        print("wrong input")

    data = str(net_fund_size) + "\n"

    with open("net_income.csv", "a") as f:
        f.write(data)
    print(f"The net income is {net_fund_size} ")

    fund_type = fund_type_dict[user_selection]

    data = (fund_size, fund_type, net_fund_size)
    return data


def net_fund_extract():
    "Extract the current status of net fund size from the csv file"

    last_nest_fund = 0
    try:
        import csv
        with open("Kiplelgo_funds_record.csv", "r") as f:
            iterable = csv.reader(f)
            dd_iterable = list(iterable)
            for item in dd_iterable:
                last_nest_fund = int(item[4])

    except FileNotFoundError:
        file = open("net_income.csv", "w")
        file.close()

    return last_nest_fund


def fund_type():
    "Establish the type of funds being recorded by the user"
    print("Expenditure(e) or Income(i) ")
    user_selection = input("insert option (e/i):")
    fund_type_dict = {"e": "EXPENDITURE", "i": "INCOME"}

    fund_type = fund_type_dict[user_selection]






