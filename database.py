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
    query = f"CREATE TABLE IF NOT EXIST`{name}` ({values})"
    cursor.execute(query)
    db.commit()
    print(f"Table '{name}' created successfully!")

def insert_table(tableName, names, values):
    query = f"INSERT INTO `{tableName}` ({names}) VALUES ({','.join(['%s'] * len(values))})"
    cursor.execute(query, values)
    db.commit()
    print(f"Inserted into '{tableName}' successfully!")

def read_values(tableName, columns, condition, condition_values):
    query = f"SELECT {columns} FROM `{tableName}` WHERE {condition}"
    cursor.execute(query, condition_values)
    results = cursor.fetchall()
    for row in results:
        print(row)
    return results

def read_value(tableName, columns, condition, condition_values):
    query = f"SELECT {columns} FROM `{tableName}` WHERE {condition} LIMIT 1"
    cursor.execute(query, condition_values)
    result = cursor.fetchone()
    if result:
        print(result)
    else:
        print("No matching record found.")
    return result
def delete_from_table(tableName, condition, condition_values):
    query = f"DELETE FROM `{tableName}` WHERE {condition}"
    cursor.execute(query, condition_values)
    db.commit()
    print(f"Deleted rows from '{tableName}' where {condition}")