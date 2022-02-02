def amount(net_income):
    "edit the net income based on the amount and type of funds the user enters"
    user_input = int(input("insert amount:"))
    income = int(net_income)

    print("Expenditure(e) or Income(i) ")
    user_selection = input("insert option (e/i):")

    if user_selection == "e":
        income -= user_input

    elif user_selection == "i":
        income += user_input
    else:
        print("wrong input")

    data = str(income) + "\n"

    with open("net_income.csv", "a") as f:
        f.write(data)
    print(f"The net income is {income} ")


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
