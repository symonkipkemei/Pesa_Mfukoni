from pesa_date import *
from funds import *
from wealth_motivation import *
from purpose import *
from store_csv import *


def main():
    "control the flow of different elements"

    print("************PESA MFUKONI***********")
    print("1) Add funds\n"
          "2) View Net income")

    user_selection = int(input("choice: "))

    if user_selection == 1:
        current_date = extract_date()
        purpose = pesa_purpose()
        previous_net_fund = net_fund_extract()
        fund_size, fund_type, net_fund_size = new_net_fund_size(previous_net_fund)
        store_data_csv(current_date, fund_type, fund_size, purpose, net_fund_size)

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
