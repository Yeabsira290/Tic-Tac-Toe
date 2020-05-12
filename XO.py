from tkinter import *
import sys
import random

class main():

    def __init__(self):

        self.player="X"
        self.computer="o"
        self.turn=random.randint(0,1)
        self.next=''

        self.menu_window = Tk()
        self.menu_window.title("Tic Tac Toe")
        self.menu_window.geometry("300x300")
        self.menu_window.configure(background="black")



        # menu
        title = Label(self.menu_window, text="TIC TAC TOE", font=("Arial Bold", 25, "bold italic"), bg="black",
                      fg="white").place(
            x=50, y=30)
        choose = Label(self.menu_window, text="Choose your letter", font=("Arial Light", 15), bg="black", fg="white").place(
            x=70,
            y=100)

        letter = IntVar()
        letter.set(1)
        X = Radiobutton(self.menu_window, text="X", font=("Arial Bold", 15), variable=letter, bg="black", fg='gray30',
                        value=1, command= lambda : self.letterAss("X")).place(x=70, y=130)
        O = Radiobutton(self.menu_window, text="O", font=("Arial Bold", 15), variable=letter, bg="black", fg='gray30',
                        value=2, command= lambda : self.letterAss("O")).place(x=200, y=130)
        play = Button(self.menu_window, text="Start", font=("Arial Light", 10), bg='gray69', width=6, command=self.close).place(
            x=70,
            y=190)
        exit1 = Button(self.menu_window, text="Exit", font=("Arial Light", 10), bg='gray69', width=6, command=self.exit).place(
            x=190,
            y=190)
        self. menu_window.mainloop()

    def main_windowf(self):

        self.main_window = Tk()
        self.main_window.title("Tic Tac Toe")
        self.main_window.geometry("308x300")
        self.main_window.configure(background="black")

        backLogo = PhotoImage(file='back.png')
        smallback_logo = backLogo.subsample(4, 4)

        reLogo = PhotoImage(file='relay.png')
        smallre_logo = reLogo.subsample(4, 4)

        self.b1r1 = Button(self.main_window, font=("Arial Bold", 10), bg='gray69', width=11, height=4,command=  lambda : self.display("b1r1"))
        self.b1r1.place(x=2, y=45)

        self.b2r1 = Button(self.main_window, font=("Arial Bold", 10), bg='gray69', width=11, height=4,command=  lambda : self.display("b2r1"))
        self.b2r1.place(x=106, y=45)

        self.b3r1 = Button(self.main_window, font=("Arial Bold", 10), bg='gray69', width=11, height=4,command=  lambda : self.display("b3r1"))
        self.b3r1.place(x=209, y=45)

        self.b4r2 = Button(self.main_window, font=("Arial Bold", 10), bg='gray69', width=11, height=4,command=  lambda : self.display("b4r2"))
        self.b4r2.place(x=2, y=125)

        self.b5r2 = Button(self.main_window, font=("Arial Bold", 10), bg='gray69', width=11, height=4,command=  lambda : self.display("b5r2"))
        self.b5r2.place(x=106, y=125)

        self.b6r2 = Button(self.main_window, font=("Arial Bold", 10), bg='gray69', width=11, height=4,command=  lambda : self.display("b6r2"))
        self.b6r2.place(x=209, y=125)

        self.b7r3 = Button(self.main_window, font=("Arial Bold", 10), bg='gray69', width=11, height=4,command=  lambda : self.display("b7r3"))
        self.b7r3.place(x=2, y=205)

        self.b8r3 = Button(self.main_window, font=("Arial Bold", 10), bg='gray69', width=11, height=4,command=  lambda : self.display("b8r3"))
        self.b8r3.place(x=106, y=205)

        self.b9r3 = Button(self.main_window, font=("Arial Bold", 10), bg='gray69', width=11, height=4,command=  lambda : self.display("b9r3"))
        self.b9r3.place(x=209, y=205)

        back = Button(self.main_window)
        back.config(image=smallback_logo,bg='black', compound=LEFT,bd=0,width=30,height=30,command= self.back)
        back.place(x=10,y=5)

        replay = Button(self.main_window)
        replay.config(image=smallre_logo, bg='black', compound=LEFT, bd=0, width=30, height=30,command= lambda : self.replay("replay"))
        replay.place(x=260, y=5)

        self.main_window.mainloop()

    def whoStart(self):

        if self.turn==0:

            self.computerControl()
            self.turn=-1
            self.next=1

        else:

            self.next=0

    def computerControl(self):

        print("Computer")
        buttonNames=["b1r1","b2r1","b3r1","b4r2","b5r2","b6r2","b7r3","b8r3","b9r3"]
        rand=random.randint(0,8)
        self.displayCom(buttonNames[rand])
        self.updateNext(1)

    def letterAss(self,letter):

        if letter=="X":

            self.player="X"
            self.computer="O"

        else:

            self.player="O"
            self.computer="X"

    def exit(self):
        sys.exit()

    def close(self):
        self.whoStart()
        self.menu_window.destroy()
        self.main_windowf()

    def back(self):
        self.main_window.destroy()
        main()

    def replay(self,buttonn):

        if buttonn=="re":
            self.end_window.destroy()

        self.b1r1.config(text='',bg='gray69',state=NORMAL)
        self.b2r1.config(text='', bg='gray69', state=NORMAL)
        self.b3r1.config(text='', bg='gray69', state=NORMAL)
        self.b4r2.config(text='', bg='gray69', state=NORMAL)
        self.b5r2.config(text='', bg='gray69', state=NORMAL)
        self.b6r2.config(text='', bg='gray69', state=NORMAL)
        self.b7r3.config(text='', bg='gray69', state=NORMAL)
        self.b8r3.config(text='', bg='gray69', state=NORMAL)
        self.b9r3.config(text='', bg='gray69', state=NORMAL)



    def end(self,message):

        self.end_window=Tk()

        self.end_window.title("Tic Tac Toe")
        self.end_window.geometry("300x130")
        self.end_window.configure(background="black")

        re = Button(self.end_window,text="relpay",command= lambda : self.replay("re")).place(x=70,y=70)
        exit = Button(self.end_window, text="exit",command=self.exit).place(x=230, y=70)


        if message==1:

            message_label = Label(self.end_window,text="You win!!!",bg='black',fg='white',font=("Arial Bold", 15)).place(x=100,y=20)

        else:
            message_label = Label(self.end_window, text="You Lose!!!", bg='black', fg='white', font=("Arial Bold", 15)).place(
                x=100, y=20)

    def updateNext(self,next):

        self.next=next


    def display(self, bname):

        if self.next == 1 or self.turn==1:

            self.turn=-1

            if bname=="b1r1":
                self.b1r1.configure(text=self.player, bg='gray33', state=DISABLED)

            elif bname == "b2r1":
                self.b2r1.configure(text=self.player, bg='gray33', state=DISABLED)

            elif bname == "b3r1":
                self.b3r1.configure(text=self.player, bg='gray33', state=DISABLED)

            elif bname == "b4r2":
                self.b4r2.configure(text=self.player, bg='gray33', state=DISABLED)

            elif bname == "b5r2":
                self.b5r2.configure(text=self.player, bg='gray33', state=DISABLED)

            elif bname == "b6r2":
                self.b6r2.configure(text=self.player, bg='gray33', state=DISABLED)

            elif bname == "b7r3":
                self.b7r3.configure(text=self.player, bg='gray33', state=DISABLED)

            elif bname == "b8r3":
                self.b8r3.configure(text=self.player, bg='gray33', state=DISABLED)

            elif bname == "b9r3":
                self.b9r3.configure(text=self.player, bg='gray33', state=DISABLED)

            self.updateNext(0)
            self.computerControl()

        else:
            print("No")

    def displayCom(self, bname):

            if bname=="b1r1":
                self.b1r1.configure(text=self.computer, bg='gray33', state=DISABLED)

            elif bname == "b2r1":
                self.b2r1.configure(text=self.computer, bg='gray33', state=DISABLED)

            elif bname == "b3r1":
                self.b3r1.configure(text=self.computer, bg='gray33', state=DISABLED)

            elif bname == "b4r2":
                self.b4r2.configure(text=self.computer, bg='gray33', state=DISABLED)

            elif bname == "b5r2":
                self.b5r2.configure(text=self.computer, bg='gray33', state=DISABLED)

            elif bname == "b6r2":
                self.b6r2.configure(text=self.computer, bg='gray33', state=DISABLED)

            elif bname == "b7r3":
                self.b7r3.configure(text=self.computer, bg='gray33', state=DISABLED)

            elif bname == "b8r3":
                self.b8r3.configure(text=self.computer, bg='gray33', state=DISABLED)

            elif bname == "b9r3":
                self.b9r3.configure(text=self.computer, bg='gray33', state=DISABLED)


main()

