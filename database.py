import mysql.connector

# Global cursor and database connection
cursor = None
db = None

def connect_to_database(username, password):
    global cursor, db
    db = mysql.connector.connect(
        host="localhost",
        user=username,
        password=password,
        database="server"
    )
    cursor = db.cursor()
    print("Connected to database successfully!")

def create_table(name, values):
    query = f"CREATE TABLE IF NOT EXISTS `{name}` ({values})"
    cursor.execute(query)
    db.commit()
    print(f"Table '{name}' created successfully!")

def insert_table(tableName, names, values):
    query = f"INSERT INTO `{tableName}` ({names}) VALUES ({','.join(['%s'] * len(values))})"
    cursor.execute(query, values)
    db.commit()
    print(f"Inserted into '{tableName}' successfully!")

def read_value(tableName, column, condition, condition_values):
    query = f"SELECT {column} FROM `{tableName}` WHERE {condition} = %s LIMIT 1"
    cursor.execute(query, (condition_values,))
    result = cursor.fetchone()
    if result:
        print(result[0])
    else:
        print("No matching record found.")
    return result[0]
def delete_from_table(tableName, condition, condition_values):
    query = f"DELETE FROM `{tableName}` WHERE {condition} = %s"
    cursor.execute(query, (condition_values,))
    db.commit()
    print(f"Deleted rows from '{tableName}' where {condition}")