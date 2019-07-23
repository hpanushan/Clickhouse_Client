from clickhouse_driver import Client

client = Client('10.0.0.22')

query = "SHOW DATABASES"

print(client.execute(query))

