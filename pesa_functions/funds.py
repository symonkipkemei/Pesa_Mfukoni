def new_net_fund_size(type_of_fund, previous_net_fund_size):
    "edit the previous net_fund_size based on the new fund size and type of funds the user enters"
    fund_size = int(input("insert amount:"))
    net_fund_size = int(previous_net_fund_size)

    if type_of_fund == "EXPENDITURE":
        net_fund_size -= fund_size

    elif type_of_fund == "INCOME":
        net_fund_size += fund_size
    else:
        print("wrong input")

    print(f"The net income is {net_fund_size} ")
    data = (fund_size, net_fund_size)
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
        file = open("Kiplelgo_funds_record.csv", "w")
        file.close()

    return last_nest_fund


def fund_types():
    "Establish the type of funds being recorded by the user"
    print("Expenditure(e) or Income(i) ")
    user_selection = str.lower(input("insert option (e/i):"))
    fund_type_dict = {"e": "EXPENDITURE", "i": "INCOME"}

    type_of_fund = fund_type_dict[user_selection]

    return type_of_fund
