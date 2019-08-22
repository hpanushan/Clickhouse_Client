from clickhouse_driver import Client

class ClickhouseClient:

    def __init__(self, ipAddress):
        self.ipAddress = ipAddress

    # Queries for databases
    def createDatabase(self,dbName):
        # Create database in clickhouse server
        client = Client(self.ipAddress)
        query = "CREATE DATABASE {}".format(dbName)
        client.execute(query)
        print("Database is created successfully")

    def showDatabases(self):
        # Return databases in clickhouse server
        client = Client(self.ipAddress)
        query = "SHOW DATABASES;"
        return client.execute(query)

    def dropDatabase(self,dbName):
        # Drop the database
        client = Client(self.ipAddress)
        query = "DROP DATABASE IF EXISTS {};".format(dbName)
        client.execute(query)
        print("Database is dropped successfully")

    # Queries for tables
    def showTables(self,dbName):
        # Return tables in specific database
        client = Client(self.ipAddress)
        query = 'SHOW TABLES FROM {};'.format(dbName)
        return client.execute(query)

    def createTable(self,dbName,tableName):
        # Create a new table in clickhouse server
        client = Client(self.ipAddress)
        query = 'CREATE TABLE {}.{} (user_id String, user_name String, text_id String, text String) ENGINE = Memory'.format(dbName,tableName)
        client.execute(query)
        print("Table is created successfully")

    def insertData(self,dbName,tableName,userID,userName,textID,text):
        # Inserting the data into the table
        client = Client(self.ipAddress)
        query = 'INSERT INTO {}.{} (user_id,user_name,text_id,text) VALUES'.format(dbName,tableName)
        client.execute(query,[{'user_id':userID,'user_name':userName,'text_id':textID,'text':text}])
        print('Record is added successfully')

    def selectData(self,dbName,tableName):
        # Retrive table data
        client = Client(self.ipAddress)
        query = 'SELECT * FROM {}.{};'.format(dbName,tableName)
        return client.execute(query)

    def dropTable(self,dbName,tableName):
        # Drop the table
        client = Client(self.ipAddress)
        query = 'DROP TABLE IF EXISTS {}.{};'.format(dbName,tableName)
        client.execute(query)
        print("Table is dropped successfully")

    def addColumn(self,dbName,tableName,columnName,dataType):
        # Add column to existing table
        client = Client(self.ipAddress)
        query = 'ALTER TABLE {}.{} ADD {} {};'.format(dbName,tableName,columnName,dataType)
        client.execute(query)
        print("Table column is added successfully")

    

