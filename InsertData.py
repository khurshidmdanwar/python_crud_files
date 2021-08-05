import mysql.connector
def insert_varibles_into_table(Id, Name, age):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='school',
                                             user='root',
                                             password='12345')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO teacher (Id, Name, age) 
                                VALUES (%s, %s, %s) """
        record = (Id, Name, age)
        cursor.execute(mySql_insert_query, record)
        connection.commit()
        print("Record inserted successfully into Teacher table")
    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
insert_varibles_into_table(1001, 'Sohail', 40)
insert_varibles_into_table(1002, 'Mohan', 41)
insert_varibles_into_table(1003, 'Virat', 45)
insert_varibles_into_table(1004, 'Rohan', 47)