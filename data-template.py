
from telnetlib import PRAGMA_HEARTBEAT
from time import pthread_getcpuclockid
from unicodedata import digit
import sqlalchemy as s
import os
from pprint import pprint

password = os.environ["PW_MYSQL_ROOT"]
database_name = "pesamfukoni"
#connection
engine = s.create_engine(f"mysql+pymysql://root:{password}@localhost/{database_name}")
connection = engine.connect()
metadata = s.MetaData()


def result_table():
 
    try_again = True
    while try_again:
        # create a table object for result
        result_table = s.Table('result', metadata, autoload=True, autoload_with=engine)
    
        # select entries in the database
        result_query = s.select([result_table.columns.result_id, result_table.columns.result_type])
        result_proxy = connection.execute(result_query)

        # record the output in a dict
        result_dict = {}
        for result in result_proxy:
            #convert tuple output to one item
            result_id = result[0]
            result_type= result[1]

            result_dict[result_id]=str.upper(result_type)

        # insert option to update if input is missing
        changes = {"u":"update","d":"delete","i":"insert" }


        # display the entries to the user
        print()
        print("result")
        print("***************************************************")
        for key, value in result_dict.items():
            print(f"{key}:{value}")
        print("___________________________________________________")
        for key, value in changes.items():
            print(f"<> ({key}):{value} <> ", end="")
    
        print()
        print("***************************************************")

        user_selection = input("select: ")
    

        #user selects the inputs in database
        if user_selection.isdigit():
            user_selection = int(user_selection)

            if user_selection in result_dict.keys():
                result = result_dict[user_selection]
                try_again = False
            else:
                print("Integer selected out of range")
                try_again = True

        # users selects crud options (update, delete, insert)
        else:
            if user_selection in changes.keys():
                if user_selection == str.lower("u"):
                    # updates the entries
                    print()
                    print("_____________________________")
                    print("Updating a database entry")
                    print("_____________________________")
                    id_selection = int(input("Select result id: "))
                    value_selection = input("New result type: ")
                    print("_____________________________")
                    print()

                    result_update = s.update(result_table).values(result_type=value_selection).where(result_table.columns.result_id == id_selection)
                    result_update_proxy = connection.execute(result_update)

                elif user_selection == "d":
                    # delete the entries
                    print()
                    print("_____________________________")
                    print("Deleting a database entry")
                    print("_____________________________")
                    id_selection = int(input("Select result id: "))
                    print("_____________________________")
                    print()
                
                    result_delete = query = s.delete(result_table).where(result_table.columns.result_id == id_selection)
                    result_delete_proxy = connection.execute(result_delete)
                
                elif user_selection == "i":
                    # insert new entries
                    print()
                    print("_____________________________")
                    value_selection = input("New result type: ")
                    print("_____________________________")
                    result_insert = s.insert(result_table).values(result_type =value_selection)
                    result_insert_proxy = connection.execute(result_insert)

                else:
                    print("Input selected is out of range")
        
    
    return result



        


# DISPLAY result
    def retrieve_result():
        """Read the result from the result table,
         select one option and return it to the user.
         If option is missing allow user to update.

        Returns:
            result(str): selected result
        """    
    
ans = result_table()



def purpose_type_table():
    table_type = "'purpose_type'"
    try_again = True
    while try_again:
        # create a table object for result
        table = s.Table(table_type, metadata, autoload=True, autoload_with=engine)
    
        # select entries in the database
        query = s.select([table.columns.purpose_id, table.columns.purpose_type_description])
        results_proxy = connection.execute(query)

        # record the output in a dict
        result_dict = {}
        for result in results_proxy:
            #convert tuple output to one item
            result_id = result[0]
            result_type= result[1]

            result_dict[result_id]=str.upper(result_type)

        # insert option to update if input is missing
        changes = {"u":"update","d":"delete","i":"insert" }


        # display the entries to the user
        print()
        print(f"{table_type} table")
        print("***************************************************")
        for key, value in result_dict.items():
            print(f"{key}:{value}")
        print("___________________________________________________")
        for key, value in changes.items():
            print(f"<> ({key}):{value} <> ", end="")
    
        print()
        print("***************************************************")

        user_selection = input("select: ")
    

        #user selects the inputs in database
        if user_selection.isdigit():
            user_selection = int(user_selection)

            if user_selection in result_dict.keys():
                result = result_dict[user_selection]
                try_again = False
            else:
                print("Integer selected out of range")
                try_again = True

        # users selects crud options (update, delete, insert)
        else:
            if user_selection in changes.keys():
                if user_selection == str.lower("u"):
                    # updates the entries
                    print()
                    print("_____________________________")
                    print("Updating a database entry")
                    print("_____________________________")
                    id_selection = int(input("Select result id: "))
                    value_selection = input("New result type: ")
                    print("_____________________________")
                    print()

                    result_update = s.update(result_table).values(result_type=value_selection).where(result_table.columns.result_id == id_selection)
                    result_update_proxy = connection.execute(result_update)

                elif user_selection == "d":
                    # delete the entries
                    print()
                    print("_____________________________")
                    print("Deleting a database entry")
                    print("_____________________________")
                    id_selection = int(input("Select result id: "))
                    print("_____________________________")
                    print()
                
                    result_delete = query = s.delete(result_table).where(result_table.columns.result_id == id_selection)
                    result_delete_proxy = connection.execute(result_delete)
                
                elif user_selection == "i":
                    # insert new entries
                    print()
                    print("_____________________________")
                    value_selection = input("New result type: ")
                    print("_____________________________")
                    result_insert = s.insert(result_table).values(result_type =value_selection)
                    result_insert_proxy = connection.execute(result_insert)

                else:
                    print("Input selected is out of range")
