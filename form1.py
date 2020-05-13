#!C:/Users/Piyush S. Patel/AppData/Local/Programs/Python/Python37-32/python.exe -u
print("Content-Type: text/html")    
print()

import cgi,cgitb
cgitb.enable() #for debugging
form = cgi.FieldStorage()
f_id = form.getvalue('CLIENT_ID')
print(f_id);
f_name = form.getvalue('NAME')
print(f_name);
f_ssn = form.getvalue('SSN')
print(f_ssn);
f_phone = form.getvalue('PHONE_NO')
print(f_phone);
f_age = form.getvalue('AGE')
print(f_age);
f_pref = form.getvalue('ROOM_PREF')
print(f_pref);
#print("Name of the user is:",name)

import pymysql;
# Open connection to the database

db = pymysql.connect("localhost","root","mysqlpass9","PROJECT" );
# Start a cursor object using cursor() method
cursor = db.cursor()

# Execute a SQL query using execute() method.
sql = "INSERT INTO CLIENT (CLIENT_ID, NAME, SSN, PHONE_NO, AGE, ROOM_PREF)VALUES (%s,%s,%s,%s,%s,%s);"
cursor.execute(sql,(f_id,f_name,f_ssn,f_phone,f_age,f_pref))
db.commit()

print("<p> Data Added Sucessfully</p>")

# Fetch all the rows using fetchall() method.

cursor.execute("SELECT * FROM CLIENT");
cursor.execute("SELECT * FROM CLIENT WHERE CLIENT_ID = (SELECT MAX(CLIENT_ID) FROM CLIENT)");

data = cursor.fetchall()

db.close()
# Fetch all the rows using fetchall() method.
