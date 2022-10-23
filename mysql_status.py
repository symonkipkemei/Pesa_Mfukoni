#connection
import sqlalchemy as s
from connect import engine
from connect import connection
from connect import metadata




def status_table(table_name):
    """View , select, update and insert the table:
    To adopt this function to suit other table; Change all occurencies for 
    1) selected_table.columns.[column_a]
    2) selected_table.columns.[column_b]

    with the new column names

    To allow the user to insert into more columns (more than one),modify the insert section.


    Args:
        table_name (str): the name of the table

    Returns:
        _type_: the id of the entry selected

    """
    try_again = True
    while try_again:
        # create a table object for result
        selected_table = s.Table(f'{table_name}', metadata, autoload=True, autoload_with=engine)
    
        # select entries in the database
        query = s.select([selected_table.columns.status_id, selected_table.columns.status_description])
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
                    value_selection = input("New result type: ")
                    print("_____________________________")
                    print()

                    update = s.update(selected_table).values(status_description=value_selection).where(selected_table.columns.status_id == id_selection)
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
                
                    delete = query = s.delete(selected_table).where(selected_table.columns.status_id == id_selection)
                    proxy = connection.execute(delete)
                    try_again = True
                

                # INSERT
                elif user_selection == "i":
                    # insert new entries
                    print()
                    print("_____________________________")
                    value_selection = input("New result type: ")
                    print("_____________________________")
                    insert = s.insert(selected_table).values(status_description =value_selection)
                    proxy = connection.execute(insert)
                    try_again = True

                else:
                    print("Input selected is out of range")

    # RETURN ID(PRIMARY KEY) OF SELECTED OPTION
    #_______________________________________________________________________________________   
    return user_selection 


def show_status_table(table_name : str) -> int:
    """show items in table, allow user to select one

    Args:
        table_name (str): name of the table 

    Returns:
        int: id of the table
    """

    try_again = True
    while try_again:
        # create a table object for result
        selected_table = s.Table(f'{table_name}', metadata, autoload=True, autoload_with=engine)
    
        # select entries in the database
        query = s.select([selected_table.columns.status_id, selected_table.columns.status_description])
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
    status_id = show_status_table("status")
    print(status_id)