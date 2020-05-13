#!C:/Users/Piyush S. Patel/AppData/Local/Programs/Python/Python37-32/python.exe -u
print("Content-Type: text/html")    
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
f_room = form.getvalue('ROOM_NO')



import pymysql;
# Open connection to the database

db = pymysql.connect("localhost","root","mysqlpass9","PROJECT" );
# Start a cursor object using cursor() method
cursor = db.cursor()

# Execute a SQL query using execute() method.
cursor.execute("select * from RESERVATIONS where room_no=(%s)",f_room);
data = cursor.fetchall()
print("RESERVATIONS",data)

# Fetch all the rows using fetchall() method.
