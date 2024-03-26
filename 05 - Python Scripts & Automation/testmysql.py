# This program requires the python module mysql-connector-python to be installed.
# Install it using the below command
# pip3 install mysql-connector-python

import mysql.connector

# connect to database
connection = mysql.connector.connect(user='root',host='127.0.0.1',database='sales')

# create cursor

cursor = connection.cursor()

connection.close

