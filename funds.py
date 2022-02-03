def amount(net_income):
    "edit the net income based on the amount and type of funds the user enters"
    fund_size = int(input("insert amount:"))
    net_fund_size = int(net_income)

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


def net_income_extract():
    "Extract the current status of net income from the csv file"
    import csv
    with open("net_income.csv", "r") as f:
        for row in f:
            iterable = csv.reader(f)
            dd_iterable = list(iterable)
            for item in dd_iterable:
                last_no = int(item[0])
        return last_no


income = net_income_extract()
amount(income)
