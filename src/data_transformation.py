import pandas as pd
from db_operation import DBOperation
from sqlqueries import SQLQuries


class DataTransformation(DBOperation):
    def __init__(self, hostname, database, user, password):
        """ 
        Constructor to get the connection details of connection

        Args:
            hostname (string): host name of the sever
            database (string): database name
            user (string): username
            password (string): passwrord
        """
        super().__init__(hostname, database, user, password)

    def get_data_from_db(self, sql_query):
        """Method get the data in the datafame from the database

        Args:
            sql_query (string): Query that is run on the database

        """
        conn = self.db_connection()
        df = pd.read_sql(sql=sql_query, con=conn)
        return df

    def cleanse_data(self):
        """cleanse the data by joining users and transactions
        """
        df_users = self. get_data_from_db(SQLQuries.SELECT_USER.value)

        df_transactions = self. get_data_from_db(
            SQLQuries.SELECT_TRANSACTIONS.value)

        df_merged = pd.merge(
            df_users, df_transactions, on='user_id', how='inner')
        return df_merged

    def trasform_data_service(self):
        """Method gives the Count of users per service
        """
        df_merge = self.cleanse_data()

        df_grouped = df_merge.groupby(['service']).aggregate({
            'user_id': 'count'
        }
        )
        return df_grouped

    def trasform_data_os(self):
        """Method gives the Count of users per OS
        """
        df_merge = self.cleanse_data()
        df_grouped = df_merge.groupby(['os_name']).aggregate({
            'user_id': 'count'
        }
        )
        return df_grouped

    def trasform_data_status(self):
        """Method to count the users pe status

        """
        df_merge = self.cleanse_data()
        df_grouped = df_merge.groupby(['status']).aggregate({
            'user_id': 'count'
        }
        )

        return df_grouped
