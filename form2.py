#!C:/Users/Piyush S. Patel/AppData/Local/Programs/Python/Python37-32/python.exe -u
print("Content-Type: text/html")    
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
f_room = form.getvalue('ROOM_NO')
f_roomtype = form.getvalue('TYPE')
f_amenities = form.getvalue('AMENITIES')
f_price = form.getvalue('PRICE')
#print("Name of the user is:",name)

import pymysql;
# Open connection to the database

db = pymysql.connect("localhost","root","mysqlpass9","PROJECT" );
# Start a cursor object using cursor() method
cursor = db.cursor()

# Execute a SQL query using execute() method.
sql = "INSERT INTO ROOM (ROOM_NO, TYPE, AMENITIES, PRICE)VALUES (%s,%s,%s,%s);"
cursor.execute(sql,(f_room,f_roomtype,f_amenities,f_price))
db.commit()

print("<p> Data Added Sucessfully</p>")

# Fetch all the rows using fetchall() method.

cursor.execute("SELECT * FROM ROOM");
#cursor.execute("SELECT * FROM CLIENT WHERE CLIENT_ID = (SELECT MAX(CLIENT_ID) FROM CLIENT)");

data = cursor.fetchall()

db.close()
# Fetch all the rows using fetchall() method.
