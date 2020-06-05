import os
import pymysql

# Get username from Cloud9
username = os.getenv('C9_User')

connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')
try:
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        cursor.execute("Update Friends set age = 22 where name = 'Bob';")
        connection.commit()
finally:
    connection.close()
