import mysql.connector as mdb

mydb = mdb.connect(
  host="localhost",
  user="root",
  passwd="123456789",
  database="tictactoe"
)

def player1Update(p1_result,p1_name):
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

def main():
	p1_result = 0
	p2_result = 2
	p1_name = "Hrishikesh"
	p2_name = "Arindam"

	player1Update(p1_result,p1_name)
	player2Update(p2_result,p2_name)

if __name__ == "__main__":
	main()




