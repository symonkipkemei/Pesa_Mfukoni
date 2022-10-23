#connection
import sqlalchemy as s
from connect import engine
from connect import connection
from connect import metadata
from date_of_transaction import extract_date

from mysql_status import show_status_table
from mysql_account import show_account_table
from mysql_account_type import show_account_type_table
from mysql_purpose_type import show_purpose_type_table
from mysql_purpose import show_purpose_table

def transaction_table(table_name: str, ACCOUNT_ID : int, STATUS_ID: int, MONEY_IN: int, MONEY_OUT:int, PURPOSE_ID:int, DATE_OF_TRANSACTION) -> int:
    """A record of the transaction done from each and every account

    Args:
        table_name (str): transaction
        ACCOUNT_ID (int): primary key for the account table
        STATUS_ID (int): primary key for the status table
        MONEY_IN (int): Money deposited in refernce to status
        MONEY_OUT (int): Money withdrawn in refernce to status
        PURPOSE_ID (int): function of the transaction
        DATE_OF_TRANSACTION (_type_): date the transaction was executed

    Returns:
        int: the transaction id
    """

    # create a table object for result
    selected_table = s.Table(f'{table_name}', metadata, autoload=True, autoload_with=engine)

    # MONEY IN
    if STATUS_ID == 1:
        insert = s.insert(selected_table).values(account_id = ACCOUNT_ID, status_id = STATUS_ID,money_in = MONEY_IN,purpose_id = PURPOSE_ID, date_of_transaction = DATE_OF_TRANSACTION )
        proxy = connection.execute(insert)
        print("Transaction completed")

    # MONEY OUT
    elif STATUS_ID == 2:
        insert = s.insert(selected_table).values(account_id = ACCOUNT_ID, status_id = STATUS_ID,money_out = MONEY_OUT,purpose_id = PURPOSE_ID, date_of_transaction = DATE_OF_TRANSACTION )
        proxy = connection.execute(insert)
        print("Transaction completed")



def showcase_transaction_table(table_name: str,showcasenumber = 10 ) -> int:
    """View transaction ordered by the date it was transacted , select, update and insert the transaction table

    Args:
        table_name (str): name of table
        showcasenumber (int, optional): number of transactions to be displayed. Defaults to 5.

    Returns:
        int: selected transaction id
    """

    try_again = True
    while try_again:
        # table objects created with the following abreviations
        # tt_transaction_table
        # st_status_table
        # at_account_table
        # pt_purpose_table


        # create a table object for result
        tt = s.Table(f'{"transaction"}', metadata, autoload=True, autoload_with=engine)
        st = s.Table(f'{"status"}', metadata, autoload=True, autoload_with=engine)
        at = s.Table(f'{"account"}', metadata, autoload=True, autoload_with=engine)
        pt = s.Table(f'{"purpose"}', metadata, autoload=True, autoload_with=engine)
        

    
        # select entries in the database
        join_statement = tt.join(st,st.columns.status_id == tt.columns.status_id).join(at, at.columns.account_id == tt.columns.account_id).join(pt, pt.columns.purpose_id == tt.columns.purpose_id)
        query = s.select([tt.columns.transaction_id, st.columns.status_description, at.columns.account_name, pt.columns.purpose_description,tt.columns.date_of_transaction,tt.columns.money_in,tt.columns.money_out]).select_from(join_statement).order_by(s.desc(tt.columns.transaction_id)).limit(showcasenumber)
        result_proxy = connection.execute(query)

        # STORING RESULTS PROXY IN A DICT AND DISPLAY ENTRIES
        #_______________________________________________________________________________________
       
        # record the output in a dict ( key and value); id and the name
        output_dict = {}
        list_details =[]
        for result in result_proxy:
            #convert tuple output to one item
            column_0= str(result[0]) #transaction_id
            column_1= str(result[1]) #status_description
            column_2= str(result[2]) #account_name
            column_3= str(result[3]) #purpose_description
            column_4= str(result[4]) #date_of_transaction
            column_5= str(result[5]) #money_in
            column_6= str(result[6]) #money_out

            # table_id (primary key) recorded as the key, followed by list of transaction details
            list_details =f"status:{column_1} ** account:{column_2} ** purpose:{column_3} ** date:{column_4} ** money in:{column_5} ** money out:{column_6} "

            output_dict[column_0]=list_details

        print()
        print(F"{table_name}")
        print("*****************************************************************************************************************************")
        for key, value in output_dict.items():
            print(f"{key}:{value}")
        print("_____________________________________________________________________________________________________________________________")

        # DISPLAY CREATE, DELETE AND INSERT OPTIONS
        #_______________________________________________________________________________________
        # insert option to update if input is missing
        changes = {"u":"update","d":"delete","i":"insert" }

        for key, value in changes.items():
            print(f"<> ({key}):{value} <> ", end="")
    
        print()
        print("*****************************************************************************************************************************")

        user_selection = input("select: ")
    

        # SELECT ENTRY IN DATABASE LOGIC
        #_______________________________________________________________________________________
        if user_selection.isdigit():
            user_selection = int(user_selection)
            if user_selection in output_dict.keys():
                try_again = False
            else:
                print("Integer selected out of range")
                try_again = True

        # UPDATE , DELETE AND INSERT LOGIC
        #_______________________________________________________________________________________
        else:
            if user_selection in changes.keys():
                #UPDATE
                if user_selection == str.lower("u"):
                    print()
                    print("_____________________________")
                    print("Updating a database entry")
                    print("_____________________________")
                    TRANSACTION_ID = int(input("Select transaction id: "))
                    STATUS_ID = show_status_table("status")
                    ACCOUNT_TYPE_ID = show_account_type_table("account_type")
                    ACCOUNT_ID = show_account_table("account", ACCOUNT_TYPE_ID)
                    PURPOSE_TYPE_ID = show_purpose_type_table("purpose_type")
                    PURPOSE_ID = show_purpose_table("purpose",PURPOSE_TYPE_ID)
                    DATE_OF_TRANSACTION = extract_date()
                    if STATUS_ID == 1:
                        MONEY_IN = int(input("New money_in: "))
                        update = s.update(tt).values(status_id=STATUS_ID, account_id=ACCOUNT_ID,purpose_id=PURPOSE_ID,date_of_transaction=DATE_OF_TRANSACTION,money_in=MONEY_IN).where(tt.columns.transaction_id==TRANSACTION_ID)
                        proxy = connection.execute(update)

                    elif STATUS_ID == 2:
                        MONEY_OUT = int(input("New money_out: "))
                        update = s.update(tt).values(status_id=STATUS_ID, account_id=ACCOUNT_ID,purpose_id=PURPOSE_ID,date_of_transaction=DATE_OF_TRANSACTION,money_out=MONEY_OUT).where(tt.columns.transaction_id==TRANSACTION_ID)
                        proxy = connection.execute(update)
                    
                    else:
                        print("I need an update")

                    print("_____________________________")
                    print()

                    try_again = True

            
                #DELETE

                elif user_selection == "d":
                    # delete the entries
                    print()
                    print("_____________________________")
                    print("Deleting a database entry")
                    print("_____________________________")
                    id_selection = int(input("select transaction id: "))
                    print("_____________________________")
                    print()
                
                    delete = query = s.delete(tt).where(tt.columns.transaction_id == id_selection)
                    proxy = connection.execute(delete)
                    try_again = True
                

                # INSERT
                elif user_selection == "i":
                    # insert new entries
                    print("Press 1 below to add funds :)")
                    user_selection == 0
                    try_again = False

                else:
                    print("Input selected is out of range")

    # RETURN ID(PRIMARY KEY) OF SELECTED OPTION
    #_______________________________________________________________________________________   
    return user_selection 


if __name__ == "__main__":
    transaction_id = showcase_transaction_table("transaction",10)
    print(transaction_id)

