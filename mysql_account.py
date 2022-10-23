#connection
import sqlalchemy as s
from connect import engine
from connect import connection
from connect import metadata
from mysql_account_type import account_type_table



def account_table(table_name: str, ACCOUNT_TYPE_ID : int) -> int:

    """View , select, update and insert the table:
    To adopt this function to suit other table; Change all occurencies for 
    1) selected_table.columns.[column_a]
    2) selected_table.columns.[column_b]

    with the new column names

    To allow the user to insert into more columns (more than one),modify the insert section.


    Args:
        table_name (str): the name of the table
        ACCOUNT_TYPE_ID(int): the id for the account_type table.

    Returns:
        user_selection(int): the id of the entry selected

    """

    try_again = True
    while try_again:
        # create a table object for result
        selected_table = s.Table(f'{table_name}', metadata, autoload=True, autoload_with=engine)
        account_type_table = s.Table('account_type', metadata, autoload=True, autoload_with=engine)
    
        # select entries in the database
        join_statement = selected_table.join(account_type_table,selected_table.columns.account_type_id == account_type_table.columns.account_type_id)
        query = s.select([selected_table.columns.account_id, selected_table.columns.account_name]).select_from(join_statement).where(account_type_table.columns.account_type_id == ACCOUNT_TYPE_ID)
        result_proxy = connection.execute(query)

        # STORING RESULTS PROXY IN A DICT
        #_______________________________________________________________________________________
       
        # record the output in a dict ( key and value); id and the name
        output_dict = {}
        for result in result_proxy:
            #convert tuple output to one item
            column_a = result[0]
            column_b= result[1]

            # table_id (primary key) recorded as the key, followed by identifier name

            output_dict[column_a]=str.upper(column_b)

        # insert option to update if input is missing
        changes = {"u":"update","d":"delete","i":"insert" }


        # DISPLAY ENTRIES IN DATABASE
        #_______________________________________________________________________________________
        print()
        print(F"{table_name}")
        print("***************************************************")
        for key, value in output_dict.items():
            print(f"{key}:{value}")
        print("___________________________________________________")

        # DISPLAY CREATE, DELETE AND INSERT OPTIONS
        #_______________________________________________________________________________________
        for key, value in changes.items():
            print(f"<> ({key}):{value} <> ", end="")
    
        print()
        print("***************************************************")

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
                    id_selection = int(input("Select result id: "))
                    ACCOUNT_NAME= input("insert account_name: ")
                    ACCOUNT_NO= input("Insert account_no: ")
                    ACCOUNT_HOST= input("Insert account_host: ")
                    ACCOUNT_DESCRIPTION= input("Insert account_description: ")
                    print("_____________________________")
                    print()

                    update = s.update(selected_table).values(account_name = ACCOUNT_NAME, account_type_id = ACCOUNT_TYPE_ID,account_no = ACCOUNT_NO, account_host = ACCOUNT_HOST,account_description=ACCOUNT_DESCRIPTION).where(selected_table.columns.account_id == id_selection)
                    proxy = connection.execute(update)
                    try_again = True

            
                #DELETE

                elif user_selection == "d":
                    # delete the entries
                    print()
                    print("_____________________________")
                    print("Deleting a database entry")
                    print("_____________________________")
                    id_selection = int(input("Select result id: "))
                    print("_____________________________")
                    print()
                
                    delete = query = s.delete(selected_table).where(selected_table.columns.account_id == id_selection)
                    proxy = connection.execute(delete)
                    try_again = True
                

                # INSERT
                elif user_selection == "i":
                    # insert new entries
                    print()
                    print("_____________________________")
                    ACCOUNT_NAME= input("insert account_name: ")
                    ACCOUNT_NO= input("Insert account_no: ")
                    ACCOUNT_HOST= input("Insert account_host: ")
                    ACCOUNT_DESCRIPTION= input("Insert account_description: ")

                    print("_____________________________")
                    insert = s.insert(selected_table).values(account_name = ACCOUNT_NAME, account_type_id = ACCOUNT_TYPE_ID,account_no = ACCOUNT_NO, account_host = ACCOUNT_HOST,account_description=ACCOUNT_DESCRIPTION )
                    proxy = connection.execute(insert)
                    try_again = True

                else:
                    print("Input selected is out of range")

    # RETURN ID(PRIMARY KEY) OF SELECTED OPTION
    #_______________________________________________________________________________________   
    return user_selection 


def show_account_table(table_name : str, ACCOUNT_TYPE_ID :int) -> int:
    """show items in table, allow user to select one

    Args:
        table_name (str): name of the table 
        account_type_id(int): name of account type id

    Returns:
        int: id of the table
    """

    try_again = True
    while try_again:
        # create a table object for result
        selected_table = s.Table(f'{table_name}', metadata, autoload=True, autoload_with=engine)
        account_type_table = s.Table(f'{"account_type"}', metadata, autoload=True, autoload_with=engine)
    
        # select entries in the database
        join_statement = selected_table.join(account_type_table,selected_table.columns.account_type_id == account_type_table.columns.account_type_id)
        query = s.select([selected_table.columns.account_id, selected_table.columns.account_name]).select_from(join_statement).where(account_type_table.columns.account_type_id == ACCOUNT_TYPE_ID)
        result_proxy = connection.execute(query)

        # STORING RESULTS PROXY IN A DICT
        #_______________________________________________________________________________________
       
        # record the output in a dict ( key and value); id and the name
        output_dict = {}
        for result in result_proxy:
            #convert tuple output to one item
            column_a = result[0]
            column_b= result[1]

            # table_id (primary key) recorded as the key, followed by identifier name

            output_dict[column_a]=str.upper(column_b)

        # insert option to update if input is missing
        changes = {"u":"update","d":"delete","i":"insert" }


        # DISPLAY ENTRIES IN DATABASE
        #_______________________________________________________________________________________
        print()
        print(F"{table_name}")
        print("***************************************************")
        for key, value in output_dict.items():
            print(f"{key}:{value}")
        print("___________________________________________________")

        # SELECT ENTRY IN DATABASE LOGIC
        #_______________________________________________________________________________________
        user_selection = input("select: ")
        if user_selection.isdigit():
            user_selection = int(user_selection)
            if user_selection in output_dict.keys():
                try_again = False
            else:
                print("Integer selected out of range")
                try_again = True
        else:
            print("Wrong input")
    return user_selection





if __name__ == "__main__":
    account_type_id = 1
    account_id = show_account_table("account")
    print(account_id)
