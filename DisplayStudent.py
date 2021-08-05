import mysql.connector
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='school',
                                         user='root',
                                         password='12345')

    sql_select_Query = "select * from student"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        #print("Id = ", row[0], )
        #print("Name = ", row[1])
        #print("City  = ", row[2])
       # print("Country  = ", row[3], "\n")
        print(row[0], '\t', row[1], '\t\t', row[2], '\t', row[3])

except mysql.connector.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")