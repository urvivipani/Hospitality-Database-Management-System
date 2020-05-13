#!C:/Users/Piyush S. Patel/AppData/Local/Programs/Python/Python37-32/python.exe -u
print("Content-Type: text/html")    
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
f_id = form.getvalue('CLIENT_ID')
f_room = form.getvalue('ROOM_NO')
f_checkin = form.getvalue('CHECK_IN')
f_checkout = form.getvalue('CHECK_OUT')
#print("Name of the user is:",name)

import pymysql;
# Open connection to the database

db = pymysql.connect("localhost","root","mysqlpass9","PROJECT" );
# Start a cursor object using cursor() method
cursor = db.cursor()

# Execute a SQL query using execute() method.
sql = "INSERT INTO RESERVATIONS (CLIENT_ID, ROOM_NO, CHECK_IN, CHECK_OUT)VALUES (%s,%s,%s,%s);"
cursor.execute(sql,(f_id,f_room,f_checkin,f_checkout))
db.commit()

print("<p> Data Added Sucessfully</p>")

# Fetch all the rows using fetchall() method.

cursor.execute("SELECT * FROM RESERVATIONS");
#cursor.execute("SELECT * FROM CLIENT WHERE CLIENT_ID = (SELECT MAX(CLIENT_ID) FROM CLIENT)");

data = cursor.fetchall()

db.close()
# Fetch all the rows using fetchall() method.
