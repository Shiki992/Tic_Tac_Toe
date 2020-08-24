                                TIC TAC TOE

By CED17I001, CED17I009, CED17I045
OS Concepts used: Threading and GUI(Tkinter) Thread non interrupts.
Other Concepts used: DBMS to check the leaderboard.
No. of Threads used: increases after every turn. At the last possible state, there are at least 9 running threads to check who won.
How to run the code: in main.py under if __name__ == "__main__":
change photo =tk.PhotoImage(file = "/home/hrishikesh//Desktop/IIITDM/OS/Tic-Tac-Toe/Tic_Tac_Toe/ttt.png")
to photo =tk.PhotoImage(file = "Folder_containing _this_file/Tic_Tac_Toe/ttt.png")
and run the code.
Enter details of Player 1 and 2 and click Submit and play to play the game.
While playing the game, if it hangs, do ^C(Keyboard interrupts) and you'll see the code continuing as normal to the finished state. You can only play the game once, after which you'll have to restart the program after safely closing it and ending the program by clicking the x on the top right corner.

NOTE: IF YOU DO A KEYBOARD INTERRUPT TO COMPLETELY EXIT THE GAME, THE GAME WILL NOT WORK PROPERLY THE NEXT TIME YOU WANT TO PLAY.

Happy Tic Tac Toe-ing!!!

