import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='school',
                                         user='root',
                                         password='12345')
    cursor = connection.cursor()
    print("Teacher table before deleting a row")
    sql_select_query = """select * from teacher where id = 1001"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    # Delete a record
    sql_Delete_query = """Delete from teacher where id = 1001"""
    cursor.execute(sql_Delete_query)
    connection.commit()
    print('number of rows deleted', cursor.rowcount)

    # Verify using select query (optional)
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    if len(records) == 0:
        print("Record Deleted successfully ")

except mysql.connector.Error as error:
    print("Failed to delete record from table: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")