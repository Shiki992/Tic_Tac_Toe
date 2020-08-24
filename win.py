import mysql.connector as mdb


def player1Update(p1_result,p1_name):
	mydb = mdb.connect(
	host="localhost",
	user="root",
	passwd="123456789",
	database="tictactoe"
	)

	mycursor2 = mydb.cursor()

	if p1_result == 0:
		mysql_update = "UPDATE players set Gameslost = Gameslost + 1 where Name = '" + p1_name + "'"
		cursor=mydb.cursor()
		cursor.execute(mysql_update)
		mydb.commit()
		mysql_update = "UPDATE players set Gamesplayed=Gamesplayed+1 where Name = '"+p1_name +"'"
		cursor=mydb.cursor()
		cursor.execute(mysql_update)
		mydb.commit()
		print("Record updated succesfully into the players Table")

	if p1_result == 1:
	   
		mysql_update = "UPDATE players set Gamesdrawn = Gamesdrawn + 1 where Name = '" + p1_name + "'"
		cursor=mydb.cursor()
		cursor.execute(mysql_update)
		mydb.commit()
		mysql_update = "UPDATE players set Gamesplayed=Gamesplayed+1 where Name = '"+p1_name +"'"
		cursor=mydb.cursor()
		cursor.execute(mysql_update)
		mydb.commit()
		print("Record updated succesfully into the players Table")

	if p1_result == 2:
		mysql_update = "UPDATE players set Gameswon = Gameswon + 1 where Name = '" + p1_name + "'"
		cursor=mydb.cursor()
		cursor.execute(mysql_update)
		mydb.commit()
		mysql_update = "UPDATE players set Gamesplayed=Gamesplayed+1 where Name = '"+p1_name +"'"
		cursor=mydb.cursor()
		cursor.execute(mysql_update)
		mydb.commit()
		print("Record updated succesfully into the players Table")



def player2Update(p2_result,p2_name):
	mydb = mdb.connect(
	host="localhost",
	user="root",
	passwd="123456789",
	database="tictactoe"
	)

	mycursor2 = mydb.cursor()

	if p2_result == 0:
		mysql_update = "UPDATE players set Gameslost = Gameslost + 1 where Name = '" + p2_name + "'"
		cursor=mydb.cursor()
		cursor.execute(mysql_update)
		mydb.commit()
		mysql_update = "UPDATE players set Gamesplayed=Gamesplayed+1 where Name = '"+p2_name +"'"
		cursor=mydb.cursor()
		cursor.execute(mysql_update)
		mydb.commit()
		print("Record updated succesfully into the players Table")

	if p2_result == 1:
	   
		mysql_update = "UPDATE players set Gamesdrawn = Gamesdrawn + 1 where Name = '" + p2_name + "'"
		cursor=mydb.cursor()
		cursor.execute(mysql_update)
		mydb.commit()
		mysql_update = "UPDATE players set Gamesplayed=Gamesplayed+1 where Name = '"+p2_name +"'"
		cursor=mydb.cursor()
		cursor.execute(mysql_update)
		mydb.commit()
		print("Record updated succesfully into the players Table")

	if p2_result == 2:
		mysql_update = "UPDATE players set Gameswon = Gameswon + 1 where Name = '" + p2_name + "'"
		cursor=mydb.cursor()
		cursor.execute(mysql_update)
		mydb.commit()
		mysql_update = "UPDATE players set Gamesplayed=Gamesplayed+1 where Name = '"+p2_name +"'"
		cursor=mydb.cursor()
		cursor.execute(mysql_update)
		mydb.commit()
		print("Record updated succesfully into the players Table")





