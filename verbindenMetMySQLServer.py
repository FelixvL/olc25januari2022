import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",  #port erbij indien mac
  port=3306,
  user="root",
  password="root",  # bij windows is password ""
  database="abc"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM recept")  # vul je eigen record in

myresult = mycursor.fetchall()

for x in myresult:
  print(x[5])

# gaan = input("vul naam in")
# sql = "INSERT INTO telefoon (merk, prijs) VALUES (%s, %s)"
# val = (gaan, 21)
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")
