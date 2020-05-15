from tkinter import *
import sys
import random


class main():

    def __init__(self):

        self.player = "X"
        self.computer = "o"
        self.turn = random.randint(0, 1)
        self.next = ''

        # computer moves
        self.cfirstRow = 0
        self.csecondRow = 0
        self.cthirdRow = 0

        self.cfirstColumn = 0
        self.csecondColumn = 0
        self.cthirdColumn = 0

        self.cleftDiagonal = 0
        self.crightDiagonal = 0

        #player moves
        self.pfirstRow = 0
        self.psecondRow = 0
        self.pthirdRow = 0

        self.pfirstColumn = 0
        self.psecondColumn = 0
        self.pthirdColumn = 0

        self.pleftDiagonal = 0
        self.prightDiagonal = 0

        self.totalSelected = 0

        self.menu_window = Tk()
        self.menu_window.title("Tic Tac Toe")
        self.menu_window.geometry("300x300")
        self.menu_window.configure(background="black")

        # menu
        title = Label(self.menu_window, text="TIC TAC TOE", font=("Arial Bold", 25, "bold italic"), bg="black",
                      fg="white").place(
            x=50, y=30)
        choose = Label(self.menu_window, text="Choose your letter", font=("Arial Light", 15), bg="black",
                       fg="white").place(
            x=70,
            y=100)

        letter = IntVar()
        letter.set(1)
        X = Radiobutton(self.menu_window, text="X", font=("Arial Bold", 15), variable=letter, bg="black", fg='gray30',
                        value=1, command=lambda: self.letterAss("X")).place(x=70, y=130)
        O = Radiobutton(self.menu_window, text="O", font=("Arial Bold", 15), variable=letter, bg="black", fg='gray30',
                        value=2, command=lambda: self.letterAss("O")).place(x=200, y=130)
        play = Button(self.menu_window, text="Start", font=("Arial Light", 10), bg='gray69', width=6,
                      command=self.close).place(
            x=70,
            y=190)
        exit1 = Button(self.menu_window, text="Exit", font=("Arial Light", 10), bg='gray69', width=6,
                       command=self.exit).place(
            x=190,
            y=190)
        self.menu_window.mainloop()

    def main_windowf(self):

        self.main_window = Tk()
        self.main_window.title("Tic Tac Toe")
        self.main_window.geometry("308x300")
        self.main_window.configure(background="black")

        backLogo = PhotoImage(file='back.png')
        smallback_logo = backLogo.subsample(4, 4)

        reLogo = PhotoImage(file='relay.png')
        smallre_logo = reLogo.subsample(4, 4)

        self.b1r1 = Button(self.main_window, font=("Arial Bold", 10), bg='gray69', width=11, height=4,
                           command=lambda: self.display("b1r1"))
        self.b1r1.place(x=2, y=45)

        self.b2r1 = Button(self.main_window, font=("Arial Bold", 10), bg='gray69', width=11, height=4,
                           command=lambda: self.display("b2r1"))
        self.b2r1.place(x=106, y=45)

        self.b3r1 = Button(self.main_window, font=("Arial Bold", 10), bg='gray69', width=11, height=4,
                           command=lambda: self.display("b3r1"))
        self.b3r1.place(x=209, y=45)

        self.b4r2 = Button(self.main_window, font=("Arial Bold", 10), bg='gray69', width=11, height=4,
                           command=lambda: self.display("b4r2"))
        self.b4r2.place(x=2, y=125)

        self.b5r2 = Button(self.main_window, font=("Arial Bold", 10), bg='gray69', width=11, height=4,
                           command=lambda: self.display("b5r2"))
        self.b5r2.place(x=106, y=125)

        self.b6r2 = Button(self.main_window, font=("Arial Bold", 10), bg='gray69', width=11, height=4,
                           command=lambda: self.display("b6r2"))
        self.b6r2.place(x=209, y=125)

        self.b7r3 = Button(self.main_window, font=("Arial Bold", 10), bg='gray69', width=11, height=4,
                           command=lambda: self.display("b7r3"))
        self.b7r3.place(x=2, y=205)

        self.b8r3 = Button(self.main_window, font=("Arial Bold", 10), bg='gray69', width=11, height=4,
                           command=lambda: self.display("b8r3"))
        self.b8r3.place(x=106, y=205)

        self.b9r3 = Button(self.main_window, font=("Arial Bold", 10), bg='gray69', width=11, height=4,
                           command=lambda: self.display("b9r3"))
        self.b9r3.place(x=209, y=205)

        back = Button(self.main_window)
        back.config(image=smallback_logo, bg='black', compound=LEFT, bd=0, width=30, height=30, command=self.back)
        back.place(x=10, y=5)

        replay = Button(self.main_window)
        replay.config(image=smallre_logo, bg='black', compound=LEFT, bd=0, width=30, height=30,
                      command=lambda: self.replay("replay"))
        replay.place(x=260, y=5)

        self.main_window.mainloop()


    def display(self, buttonName):

        self.checkDraw()
        self.Pcheckwin()
        self.Ccheckwin()

        if self.next == 1 or self.turn == 1:

            self.turn = -1

            if buttonName == "b1r1":
                self.b1r1.configure(text=self.player, bg='gray33', state=DISABLED)

                self.pfirstRow += 1
                self.pfirstColumn += 1
                self.pleftDiagonal += 1

            elif buttonName == "b2r1":
                self.b2r1.configure(text=self.player, bg='gray33', state=DISABLED)

                self.pfirstRow += 1
                self.psecondColumn += 1

            elif buttonName == "b3r1":
                self.b3r1.configure(text=self.player, bg='gray33', state=DISABLED)

                self.pfirstRow += 1
                self.pthirdColumn += 1
                self.prightDiagonal += 1

            elif buttonName == "b4r2":
                self.b4r2.configure(text=self.player, bg='gray33', state=DISABLED)

                self.psecondRow += 1
                self.pfirstColumn += 1

            elif buttonName == "b5r2":
                self.b5r2.configure(text=self.player, bg='gray33', state=DISABLED)

                self.psecondRow += 1
                self.psecondColumn += 1
                self.prightDiagonal += 1
                self.pleftDiagonal += 1

            elif buttonName == "b6r2":
                self.b6r2.configure(text=self.player, bg='gray33', state=DISABLED)

                self.psecondRow += 1
                self.pthirdColumn += 1

            elif buttonName == "b7r3":
                self.b7r3.configure(text=self.player, bg='gray33', state=DISABLED)

                self.pthirdRow += 1
                self.pfirstColumn += 1
                self.prightDiagonal += 10

            elif buttonName == "b8r3":
                self.b8r3.configure(text=self.player, bg='gray33', state=DISABLED)

                self.pthirdRow += 1
                self.psecondColumn += 1

            elif buttonName == "b9r3":
                self.b9r3.configure(text=self.player, bg='gray33', state=DISABLED)

                self.pthirdRow += 1
                self.pthirdColumn += 1
                self.pleftDiagonal += 1

            self.totalSelected += 1

            self.updateNext(0)
            self.computerControl()

        else:
            print("No")

    def displayCom(self, bname):

        self.checkDraw()
        self.Pcheckwin()
        self.Ccheckwin()

        if bname == "b1r1":
            self.b1r1.configure(text=self.computer, bg='gray33', state=DISABLED)

            self.cfirstRow+=1
            self.cfirstColumn+=1
            self.cleftDiagonal+=1

        elif bname == "b2r1":
            self.b2r1.configure(text=self.computer, bg='gray33', state=DISABLED)

            self.cfirstRow += 1
            self.csecondColumn += 1

        elif bname == "b3r1":
            self.b3r1.configure(text=self.computer, bg='gray33', state=DISABLED)

            self.cfirstRow += 1
            self.cthirdColumn += 1
            self.crightDiagonal += 1

        elif bname == "b4r2":
            self.b4r2.configure(text=self.computer, bg='gray33', state=DISABLED)

            self.csecondRow += 1
            self.cfirstColumn += 1

        elif bname == "b5r2":
            self.b5r2.configure(text=self.computer, bg='gray33', state=DISABLED)

            self.csecondRow += 1
            self.csecondColumn += 1
            self.crightDiagonal+=1
            self.cleftDiagonal+=1

        elif bname == "b6r2":
            self.b6r2.configure(text=self.computer, bg='gray33', state=DISABLED)

            self.csecondRow += 1
            self.cthirdColumn += 1

        elif bname == "b7r3":
            self.b7r3.configure(text=self.computer, bg='gray33', state=DISABLED)

            self.cthirdRow += 1
            self.cfirstColumn += 1
            self.crightDiagonal += 10

        elif bname == "b8r3":
            self.b8r3.configure(text=self.computer, bg='gray33', state=DISABLED)

            self.cthirdRow += 1
            self.csecondColumn += 1

        elif bname == "b9r3":
            self.b9r3.configure(text=self.computer, bg='gray33', state=DISABLED)

            self.cthirdRow += 1
            self.cthirdColumn += 1
            self.cleftDiagonal += 1

        self.totalSelected += 1

    def end(self, message):

        self.end_window = Tk()

        self.end_window.title("Tic Tac Toe")
        self.end_window.geometry("300x130")
        self.end_window.configure(background="black")

        re = Button(self.end_window, text="Replay", command=lambda: self.replay("re")).place(x=70, y=70)
        exit = Button(self.end_window, text="exit", command=self.exit).place(x=230, y=70)
        message_label = Label(self.end_window, text=message, bg='black', fg='white', font=("Arial Bold", 15)).place(
            x=100, y=20)

    def whoStart(self):

        print(self.turn)

        if self.turn == 0:

            self.computerControl()
            self.turn = -1

        else:

            self.next = 0

    def computerControl(self):

        buttonNames = ["b1r1", "b2r1", "b3r1", "b4r2", "b5r2", "b6r2", "b7r3", "b8r3", "b9r3"]
        rand = random.randint(0, 8)
        self.displayCom(buttonNames[rand])
        self.updateNext(1)

    def exit(self):

        sys.exit()

    def close(self):

        self.menu_window.destroy()
        self.main_windowf()
        self.whoStart()

    def back(self):

        self.main_window.destroy()
        main()

    def updateNext(self, next):

        self.next = next

    def letterAss(self, letter):

        if letter == "X":

            self.player = "X"
            self.computer = "O"

        else:

            self.player = "O"
            self.computer = "X"


    def checkDraw(self):

        if self.totalSelected == 9:
            self.end("Draw")

    def Ccheckwin(self):

        if self.cfirstRow==3:
            self.end("Computer win")
            self.winColor("FR")

        elif self.csecondRow==3:
            self.end("Computer win")
            self.winColor("FR")

        elif self.cthirdRow==3:
            self.end("Computer win")
            self.winColor("FR")

        elif self.cfirstColumn==3:
            self.end("Computer win")
            self.winColor("FR")

        elif self.csecondColumn==3:
            self.end("Computer win")
            self.winColor("FR")

        elif self.cthirdColumn==3:
            self.end("Computer win")
            self.winColor("FR")

        elif self.cleftDiagonal==3:
            self.end("Computer win")
            self.winColor("FR")

        elif self.crightDiagonal==3:
            self.end("Computer win")
            self.winColor("FR")

    def Pcheckwin(self):

        if self.pfirstRow==3:
            self.end("You win")
            self.winColor("FR")

        elif self.psecondRow==3:
            self.end("You win")
            self.winColor("FR")

        elif self.pthirdRow==3:
            self.end("You win")
            self.winColor("FR")

        elif self.pfirstColumn==3:
            self.end("You win")
            self.winColor("FR")

        elif self.psecondColumn==3:
            self.end("You win")
            self.winColor("FR")

        elif self.pthirdColumn==3:
            self.end("You win")
            self.winColor("FR")

        elif self.pleftDiagonal==3:
            self.end("You win")
            self.winColor("FR")

        elif self.prightDiagonal==3:
            self.end("You win")
            self.winColor("FR")

    def winColor(self,direction):

        if direction=="FR":
            self.b1r1.configure(bg='red')
            self.b2r1.configure(bg='red')
            self.b3r1.configure(bg='red')

        if direction=="SR":
            self.b4r2.configure(bg='red')
            self.b5r2.configure(bg='red')
            self.b6r2.configure(bg='red')

        if direction=="TR":
            self.b7r3.configure(bg='red')
            self.b8r3.configure(bg='red')
            self.b9r3.configure(bg='red')

        if direction=="LD":
            self.b3r1.configure(bg='red')
            self.b5r2.configure(bg='red')
            self.b7r3.configure(bg='red')

        if direction=="RD":
            self.b1r1.configure(bg='red')
            self.b5r2.configure(bg='red')
            self.b9r3.configure(bg='red')

        if direction=="FC":
            self.b1r1.configure(bg='red')
            self.b4r2.configure(bg='red')
            self.b7r3.configure(bg='red')

        if direction=="SC":
            self.b2r1.configure(bg='red')
            self.b5r2.configure(bg='red')
            self.b8r3.configure(bg='red')

        if direction=="TC":
            self.b3r1.configure(bg='red')
            self.b6r2.configure(bg='red')
            self.b9r3.configure(bg='red')

    def replay(self, button):

        if button == "re":
            self.end_window.destroy()

        self.b1r1.config(text='', bg='gray69', state=NORMAL)
        self.b2r1.config(text='', bg='gray69', state=NORMAL)
        self.b3r1.config(text='', bg='gray69', state=NORMAL)
        self.b4r2.config(text='', bg='gray69', state=NORMAL)
        self.b5r2.config(text='', bg='gray69', state=NORMAL)
        self.b6r2.config(text='', bg='gray69', state=NORMAL)
        self.b7r3.config(text='', bg='gray69', state=NORMAL)
        self.b8r3.config(text='', bg='gray69', state=NORMAL)
        self.b9r3.config(text='', bg='gray69', state=NORMAL)

        self.totalSelected = 0

        #computer
        self.cfirstRow = 0
        self.csecondRow = 0
        self.cthirdRow = 0

        self.cfirstColumn = 0
        self.csecondColumn = 0
        self.cthirdColumn = 0

        self.cleftDiagonal = 0
        self.crightDiagonal = 0

        #player
        self.pfirstRow = 0
        self.psecondRow = 0
        self.pthirdRow = 0

        self.pfirstColumn = 0
        self.psecondColumn = 0
        self.pthirdColumn = 0

        self.pleftDiagonal = 0
        self.prightDiagonal = 0

        self.turn = random.randint(0, 1)

        self.whoStart()

main()
