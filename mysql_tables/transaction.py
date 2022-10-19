#connection
import sqlalchemy as s
from connect import engine
from connect import connection
from connect import metadata


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

    insert = s.insert(selected_table).values(account_id = ACCOUNT_ID, status_id = STATUS_ID,money_in = MONEY_IN,money_out = MONEY_OUT,purpose_id = PURPOSE_ID, date_of_transaction = DATE_OF_TRANSACTION )
    proxy = connection.execute(insert)
    print("Transaction completed")

    # RETURN ID(PRIMARY KEY) OF SELECTED OPTION
    #_______________________________________________________________________________________   
    return 0


if __name__ == "__main__":
    pass
