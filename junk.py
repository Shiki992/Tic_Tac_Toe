import mysql.connector as mdb



	



def find(inpu):
	mydb = mdb.connect(
	host="localhost",
	user="root",
	passwd="123456789",
	database="tictactoe")
	mycursor2 = mydb.cursor()
	mycursor2.execute("select count(Name) from players where Name = '"+inpu+"'")
	result = mycursor2.fetchone()[0]
	print(result)
	return result
  


def insertDB(inpu):
	mydb = mdb.connect(
	host="localhost",
	user="root",
	passwd="123456789",
	database="tictactoe")
	mysql_insert="INSERT INTO players(pid,Name,Gamesplayed,Gameswon,Gameslost,Gamesdrawn) VALUES(6,'"+inpu+"',10,4,3,3)"
	cursor=mydb.cursor()
	cursor.execute(mysql_insert)
	mydb.commit()
	print("Record inserted succesfully into the players Table")






