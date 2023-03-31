import psycopg2


class DBOperation:
    
    CONN = None
    # Establish a connection to the database
    
    def __init__(self, hostname, database, user, password):
        self.hostname = hostname
        self.database = database
        self.user = user
        self.password = password

    def db_connection(self):
        """Connet to the database

        Returns:
            connection: connecting string
        """
        if DBOperation.CONN is None:
            DBOperation.CONN = psycopg2.connect(host=self.hostname,database=self.database,user=self.user,password=self.password) 
        return  DBOperation.CONN
    
    def db_connection_close(self): 
        """Close the connection
        """
        if DBOperation.CONN is not None: 
            DBOperation.CONN.close()
