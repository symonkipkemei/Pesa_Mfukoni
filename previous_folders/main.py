from pesa_date import *
from pesa_functions.funds import *
from pesa_functions.wealth_motivation import *
from pesa_functions.purpose import *
from pesa_functions.store_csv import *
from pesa_analysis.data_analysis import *

def main():
    "control the flow of different elements"
    correct = True
    while correct:
        print("\n************PESA MFUKONI***********")
        print("1) Add funds\n"
              "2) View Net income\n"
              "3) Adjust Purpose option\n"
              "4) Quit")

        user_selection = int(input("choice: "))

        if user_selection == 1:
            current_date = extract_date()
            type_of_fund = fund_types()
            purpose = pesa_purpose(type_of_fund)
            previous_net_fund = net_fund_extract()
            fund_size, net_fund_size = new_net_fund_size(type_of_fund, previous_net_fund)
            store_data_csv(current_date, type_of_fund, fund_size, purpose, net_fund_size)

            print(current_date)
            print(type_of_fund)
            print(purpose)
            print(fund_size)
            print(net_fund_size)

        elif user_selection == 2:
            print("\n")
            month = select_month()
            compound_fund_uses(month)


        elif user_selection == 3:
            print("1) Expenditure\n"
                  "2) Income\n")
            select = int(input("your choice:"))

            if select == 1:
                add_pesa_purpose_expenditure()
            elif select == 2:
                add_pesa_purpose_income()

        elif user_selection == 4:
            quote = motivation()
            print(quote)
            print("Thank you")
            correct = False

        else:
            print("Wrong input")


main()


#war continues as from tomorrow