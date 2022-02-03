from pesa_date import *
from funds import *
from wealth_motivation import *
from purpose import *


def main():
    "control the flow of different elements"

    print("************PESA MFUKONI***********")
    print("1) Add funds\n"
          "2) View Net income")

    user_selection = int(input("choice: "))

    if user_selection == 1:
        current_date = extract_date()
        last_no = net_income_extract()
        purpose = pesa_purpose()
        fund_size, fund_type, net_fund_size = amount(last_no)

        print(current_date)
        print(purpose)
        print(fund_size)
        print(fund_type)
        print(net_fund_size)


    elif user_selection == 2:
        print("To be updated")

    else:
        print("Wrong input")


main()
