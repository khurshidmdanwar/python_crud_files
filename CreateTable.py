import mysql.connector
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='school',
                                         user='root',
                                         password='12345')

    mySql_Create_Table_Query = """CREATE TABLE teacher ( 
                             Id int(11) NOT NULL,
                             Name varchar(25) NOT NULL,
                             age int(3) NOT NULL,                             
                             PRIMARY KEY (Id)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Teacher Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")