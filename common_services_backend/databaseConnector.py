# Python code that connects to database for user services (e.g. login, register)
import mysql.connector
from mysql.connector import Error

# Try/except block to validate connection
try:

    connection = mysql.connector.connect(user='developer', password='Team11_developer', host='localhost',
                                         database='team11_demand')
    # connects to DB
    if connection.is_connected():
        database_info = connection.get_server_info()
        print("NOW CONNECTED TO MYSQL SERVER v", database_info)
        myCursor = connection.cursor()
        myCursor.execute("select database(); ")
        record = myCursor.fetchone()
        print("You're connected to database", record)

        # Write into DB
        try:
            sql = "INSERT INTO TaasUser (email, firstName, lastName, DOB, userName, password) VALUES (%s,%s,%s,%s," \
                  "%s,%s) "
            val = ('myEmail@gmail.com', 'Sarah', 'Jones', '1983-07-01', 'sarahJJ', 'secure12')

            myCursor.execute(sql, val)
            connection.commit()
            print(myCursor.rowcount, "was inserted")

        except Error as e:
            print("Error", e)

        # reading from DB
        select_user_information = "SELECT * FROM TaasUser"
        with connection.cursor() as cursor:
            cursor.execute(select_user_information)
            result = cursor.fetchall()
            for row in result:
                print("Here's the data: ", row)

        myCursor.close()
        connection.close()
        print("MySQL connection is closed")

except Error as e:
    print("Error while connecting to MYSQL", e)
