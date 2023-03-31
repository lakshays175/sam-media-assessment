from enum import Enum

class SQLQuries(Enum):
    """Contains the SQL queries that is executed in the database

    Args:
        Enum (string): contains queries
    """
    SELECT_USER = "SELECT distinct USER_ID, SERVICE, OS_NAME, unsubscription_date FROM USERS"
    SELECT_TRANSACTIONS = "SELECT distinct USER_ID, STATUS FROM TRANSACTIONS WHERE STATUS IS NOT NULL"

