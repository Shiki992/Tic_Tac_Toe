import tkinter as tk
from PIL import Image
flag=0
bclick=True
def btnClick(buttons):
    global bclick,flag
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        #playerb = p2.get() + " Wins!"
        #pa = p1.get() + " Wins!"
        #checkForWin()
        flag+= 1


    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        #checkForWin()
        flag += 1
    else:
        tk.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

'''def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)'''

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       button1 = tk.Button(self, text=" ", font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button1))
       button1.grid(row=3, column=0)
       button2 = tk.Button(self, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button2))
       button2.grid(row=3, column=1)
       button3 = tk.Button(self, text=' ',font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button3))
       button3.grid(row=3, column=2)
       button4 = tk.Button(self, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button4))
       button4.grid(row=4, column=0)
       button5 = tk.Button(self, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button5))
       button5.grid(row=4, column=1)
       button6 = tk.Button(self, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button6))
       button6.grid(row=4, column=2)
       button7 = tk.Button(self, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button7))
       button7.grid(row=5, column=0)
       button8 = tk.Button(self, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button8))
       button8.grid(row=5, column=1)
       button9 = tk.Button(self, text=' ', font='Times 20 bold', bg='gray', fg='white', height=4, width=8, command=lambda: btnClick(button9))
       button9.grid(row=5, column=2)
       



class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        
        p1 = Page1(self)

        txtFrame = tk.Frame(self)
        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        txtFrame.pack(side="top", fill="x", expand=False)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        l1=tk.Label(txtFrame,text="Player 1 name:")
        l1.grid(column=75,row=0)
        text1=tk.Entry(txtFrame,width=20)
        text1.grid(column=150,row=0)
        l2=tk.Label(txtFrame,text="Player 2 name:")
        l2.grid(column=75,row=75)
        text2=tk.Entry(txtFrame,width=20)
        text2.grid(column=150,row=75)
        b1 = tk.Button(buttonframe, text="Submit and Play",fg="white",bg="black", command=p1.lift)
      
        b1.pack(side="bottom")
        main1=Page1(self)
        frame = tk.Frame(self)
        frame.pack(side="bottom",fill="x", expand=False)
        bt=tk.Button(frame, text="RESET",fg="white",bg="red", command=main1.lift)
        bt.pack(side="bottom")



if __name__ == "__main__":
    root = tk.Tk()
    photo =tk.PhotoImage(file = "/home/hrishikesh/Desktop/OS/Tic-Tac-Toe/ttt.png")
    root.iconphoto(False, photo)
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("800x800")
    root.mainloop()