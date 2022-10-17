
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



try_again = True
while try_again:
    # create a table object for status
    status_table = s.Table('status', metadata, autoload=True, autoload_with=engine)
    
    # select entries in the database
    status_query = s.select([status_table.columns.status_id, status_table.columns.status_type])
    status_proxy = connection.execute(status_query)

    # record the output in a dict
    status_dict = {}
    for status in status_proxy:
        #convert tuple output to one item
        status_id = status[0]
        status_type= status[1]

        status_dict[status_id]=str.upper(status_type)

    # insert option to update if input is missing
    changes = {"u":"update","d":"delete","i":"insert" }


    # display the entries to the user
    print()
    print("STATUS")
    print("***************************************************")
    for key, value in status_dict.items():
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

        if user_selection in status_dict.keys():
            result = status_dict[user_selection]
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
                id_selection = int(input("Select status id: "))
                value_selection = input("New status type: ")
                print("_____________________________")
                print()

                status_update = s.update(status_table).values(status_type=value_selection).where(status_table.columns.status_id == id_selection)
                status_update_proxy = connection.execute(status_update)

            elif user_selection == "d":
                # delete the entries
                print()
                print("_____________________________")
                print("Deleting a database entry")
                print("_____________________________")
                id_selection = int(input("Select status id: "))
                print("_____________________________")
                print()
                
                status_delete = query = s.delete(status_table).where(status_table.columns.status_id == id_selection)
                status_delete_proxy = connection.execute(status_delete)
                

            elif user_selection == "i":
                # insert new entries
                print()
                print("_____________________________")
                value_selection = input("New status type: ")
                print("_____________________________")
                status_insert = s.insert(status_table).values(status_type =value_selection)
                status_insert_proxy = connection.execute(status_insert)

            else:
                print("Input selected is out of range")


print(result)
        

    













# DISPLAY STATUS
def retrieve_status():
    """Read the status from the status table,
     select one option and return it to the user.
     If option is missing allow user to update.

    Returns:
        result(str): selected status
    """
    