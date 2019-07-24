from clickhouse_driver import Client

def showDatabases():
    # Return databases in clickhouse server
    client = Client('10.0.0.22')
    query = "SHOW DATABASES;"
    return client.execute(query)

def dropDatabase():
    # Drop the database
    client = Client('10.0.0.22')
    query = "DROP DATABASE system;"
    client.execute(query)
    print("Database is dropped successfully")

def showTables():
    # Return tables in clickhouse server
    client = Client('10.0.0.22')
    query = "SHOW TABLES;"
    return client.execute(query)

def createTable(tableName):
    # Create a new table in clickhouse server
    client = Client('10.0.0.22')
    query = 'CREATE TABLE {} (user_id String, user_name String, tweet_id String, text String) ENGINE = Memory'.format(tableName)
    client.execute(query)
    print("Table is created successfully")

def insertData(tableName,userID,userName,tweetID,text):
    # Inserting the data into the table
    client = Client('10.0.0.22')
    query = 'INSERT INTO {} (user_id,user_name,tweet_id,text) VALUES'.format(tableName)
    client.execute(query,[{'user_id':userID,'user_name':userName,'tweet_id':tweetID,'text':text}])
    print('Record is added successfully')

def selectData(tableName):
    # Retrive table data
    client = Client('10.0.0.22')
    query = 'SELECT * FROM {};'.format(tableName)
    return client.execute(query)

def dropTable(tableName):
    # Drop the table
    client = Client('10.0.0.22')
    query = 'DROP TABLE IF EXISTS {};'.format(tableName)
    client.execute(query)
    print("Table is dropped successfully")

###################################################




