
from mysql_tables.account_type import account_type_table
from mysql_tables.account import account_table
from mysql_tables.purpose import purpose_table
from mysql_tables.purpose_type import purpose_type_table
from mysql_tables.status import status_table
from mysql_tables.transaction import transaction_table
from pesa_date import extract_date

import previous_folders.pesa_functions.wealth_motivation as pw

def add_funds():
    """control flow for adding a transaction
    """

    account_type_id = account_type_table("account_type")

    account_id = account_table("account",account_type_id)

    status_id = status_table("status")

    if status_id == 1:
        money_in = int(input("insert amount:"))
        money_out = 0
        print("money input recorded")

    elif status_id == 2:
        money_out = int(input("insert amount:"))
        money_in = 0
        print("money output recorded")
    
    purpose_type_id = purpose_type_table("purpose_type")

    purpose_id = purpose_table("purpose", purpose_type_id)

    date_of_transaction = extract_date()

    transaction_table("transaction", account_id, status_id,money_in, money_out, purpose_id,date_of_transaction)



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
            add_funds()
        
 
        elif user_selection == 2:
            print("design in progress, It will be available soon")
            pass

        elif user_selection == 3:
            print("design in progress, It will be available soon")
            pass


        elif user_selection == 4:
            quote = pw.motivation()
            print(quote)
            print("Thank you")
            correct = False

 
        else:
            print("Wrong input")



if __name__ == "__main__":
    main()