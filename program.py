
from mysql_account_type import account_type_table
from mysql_account import account_table
from mysql_purpose import purpose_table
from mysql_purpose_type import purpose_type_table
from mysql_status import status_table
from mysql_transaction import showcase_transaction_table, transaction_table
from date_of_transaction import extract_date

import wealth_motivation as pw

def add_funds():
    """control flow for adding a transaction
    """
    
    account_type_id = account_type_table("account_type")

    account_id = account_table("account",account_type_id)

    status_id = status_table("status")

    purpose_type_id = purpose_type_table("purpose_type")

    purpose_id = purpose_table("purpose", purpose_type_id)   

    print("\namount transacted")
    print("***************************************************")
    transaction_amount = float(input("insert:"))
    print("***************************************************")
    print("transaction recorded\n")

    date_of_transaction = extract_date()

    transaction_table("transaction", account_id, status_id, transaction_amount, purpose_id,date_of_transaction)

    showcase_transaction_table("transaction",5)

def main():
    "control the flow of different elements"
    correct = True
    while correct:
        print("\n************PESA MFUKONI***********")
        print("1) ADD FUNDS\n"
              "2) VIEW MONEY OUT\n"
              "3) VIEW MONEY IN\n"
              "4) THE NET WORTH CURVE\n"
              "5) EXIT")
        print("************************************")

        user_selection = int(input("select: "))

        if user_selection == 1:
            add_funds()
        
 
        elif user_selection == 2:
            print("design in progress, It will be available soon")
            pass

        elif user_selection == 3:
            print("design in progress, It will be available soon")
            pass

        elif user_selection == 4:
            print("design in progress, It will be available soon")
            pass
    
        elif user_selection == 5:
            quote = pw.motivation()
            print(quote)
            print("Thank you")
            correct = False

        else:
            print("Wrong input")


if __name__ == "__main__":
    main()


