import mysql.connector as mdb

mydb = mdb.connect(
  host="localhost",
  user="root",
  passwd="123456789",
  database="tictactoe"
)

mycursor2 = mydb.cursor()
mycursor2.execute("select * from players")

for tb in mycursor2:
   print(tb)
