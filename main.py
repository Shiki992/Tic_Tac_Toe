import tkinter as tk
from tkinter import messagebox
from tkthread import tk, TkThread
import re
import threading
import junk
import win
import leader
r1=[1,2,3]
r2=[4,5,6]
r3=[7,8,9]
c1=[1,4,7]
c2=[2,5,8]
c3=[3,6,9]
d1=[1,5,9]
d2=[3,5,7]


flag=0
bclick=True
'''def btnClick(buttons):
    global bclick,flag
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        print(buttons)
        flag+= 1


    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        #checkForWin()
        flag += 1
    else:
        tk.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")'''

class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
    def show(self):
        self.lift()

class Page1(Page):
   win=False
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
       global X
       global O
       X=[]
       O=[]
       def btnClick(buttons):
            global bclick,flag
            if buttons["text"] == " " and bclick == True:
                buttons["text"] = "X"
                bclick = False
                print(buttons)
                s=str(buttons)
                g=s.split(".!")
                s=g[3].split("n")
                if s[1]=='':
                    s[1]=1
                e=int(s[1])
                X.append(e)
                X.sort()
                flag+= 1
                print("X: ", X)
                t1=threading.Thread(target=chkforwin, args=([X]))
                t1.start()
                t1.join()
                if win==True:
                    messagebox.showinfo("Tic-Tac-Toe","We have a winner!!!!")



            elif buttons["text"] == " " and bclick == False:
                buttons["text"] = "O"
                bclick = True
                s=str(buttons)
                g=s.split(".!")
                s=g[3].split("n")
                if s[1]=='':
                    s[1]=1
                e=int(s[1])
                O.append(e)
                O.sort()
                flag += 1
                print("O: ", O)
                t2=threading.Thread(target=chkforwin, args=([O]))
                t2.start()
                t2.join()
            else:
                messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")
       def reset():
            button1["text"] = " "
            bclick = False
            #print(buttons)
            button2["text"] = " "
            bclick = False
            #print(buttons)
            button3["text"] = " "
            bclick = False
            #print(buttons)
            button4["text"] = " "
            bclick = False
            #print(buttons)
            button5["text"] = " "
            bclick = False
            #print(buttons)
            button6["text"] = " "
            bclick = False
            #print(buttons)
            button7["text"] = " "
            bclick = False
            #print(buttons)
            button8["text"] = " "
            bclick = False
            #print(buttons)
            button9["text"] = " "
            bclick = False
            #print(buttons)

       def chkforwin(d=[],*args):
            count=0
            for i in range(len(r1)):
                if r1[i] in d:
                    print("r1")
                    count=count+1
                    if count==3:
                        messagebox.showinfo("Tic-Tac-Toe","we have a winner!")
                        reset()
                        d=[]                    
                        
                        print("Somebody won!!!")
       
            count=0
            for i in range(len(r2)):
                if r2[i] in d:
                    print("r2")
                    count=count+1
                    if count==3:
                        messagebox.showinfo("Tic-Tac-Toe","We have a winner!!!!")
                        reset()
                        d=[]
                        
            count=0
            for i in range(len(r3)):
                if r3[i] in d:
                    print("r3")
                    count=count+1
                    if count==3:
                        messagebox.showinfo("Tic-Tac-Toe","We have a winner!!!!")
                        reset()
                        d=[]                        
                        
            count=0
            for i in range(len(c1)):
                if c1[i] in d:
                    print("c1")
                    count=count+1
                    if count==3:
                        messagebox.showinfo("Tic-Tac-Toe","We have a winner!!!!")
                        reset()
                        d=[]                        
                        
            count=0
            for i in range(len(c2)):
                if c2[i] in d:
                    print("c2")
                    count=count+1
                    if count==3:
                        messagebox.showinfo("Tic-Tac-Toe","We have a winner!!!!")
                        reset()
                        d=[]                        
                        
            count=0
            for i in range(len(c3)):
                if c3[i] in d:
                    print("c3")
                    count=count+1
                    if count==3:
                        messagebox.showinfo("Tic-Tac-Toe","We have a winner!!!!")
                        reset()
                        d=[]                        
                        
            count=0
            for i in range(len(d1)):
                if d1[i] in d:
                    print("d1")
                    count=count+1
                    if count==3:
                        messagebox.showinfo("Tic-Tac-Toe","We have a winner!!!!")
                        reset()
                        d=[]                        
                        
            count=0
            for i in range(len(d2)):
                if d2[i] in d:
                    print("d2")
                    count=count+1
                    if count==3:
                        messagebox.showinfo("Tic-Tac-Toe","We have a winner!!!!")
                        reset()
                        d=[]                        
                        
            

       



class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        global p1n,p2n
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
        p1n=text1.get()
        print(p1n)
        l2=tk.Label(txtFrame,text="Player 2 name:")
        l2.grid(column=75,row=75)
        text2=tk.Entry(txtFrame,width=20)
        text2.grid(column=150,row=75)
        p2n=text2.get()
        print(p2n)
        def plift():
            p1n=text1.get()
            if p1n==" ":
                messagebox.showinfo("please enter a name")
            p2n=text2.get()
            if p2n==" ":
                messagebox.showinfo("please enter a name")
            p1.lift
        b1 = tk.Button(buttonframe, text="Submit and Play",fg="white",bg="black", command= p1.lift)
      
        b1.pack(side="bottom")
        frame = tk.Frame(self)
        frame.pack(side="bottom",fill="x", expand=False)

        #bt=tk.Button(frame, text="RESET",fg="white",bg="red", command=lambda : p1.destroy)
       # bt.pack(side="bottom")



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tic Tac Toe")
    photo =tk.PhotoImage(file = "/home/hrishikesh//Desktop/IIITDM/OS/Tic-Tac-Toe/Tic_Tac_Toe/ttt.png")
    root.iconphoto(False,photo)
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("400x500")
    root.mainloop()