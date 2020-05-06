from tkinter import *
import sys

class main():

    def __init__(self):

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
                        value=1).place(x=70, y=130)
        O = Radiobutton(self.menu_window, text="O", font=("Arial Bold", 15), variable=letter, bg="black", fg='gray30',
                        value=2).place(x=200, y=130)
        play = Button(self.menu_window, text="Start", font=("Arial Light", 10), bg='gray69', width=6, command=self.close).place(
            x=70,
            y=190)
        exit1 = Button(self.menu_window, text="Exit", font=("Arial Light", 10), bg='gray69', width=6, command=self.exit).place(
            x=190,
            y=190)
        self. menu_window.mainloop()

    def main_window(self):

        self.main_window = Tk()
        self.main_window.title("Tic Tac Toe")
        self.main_window.geometry("308x300")
        self.main_window.configure(background="black")

        backLogo = PhotoImage(file='back.png')
        smallback_logo = backLogo.subsample(4, 4)

        reLogo = PhotoImage(file='relay.png')
        smallre_logo = reLogo.subsample(4, 4)



        self.b1r1 = Button(self.main_window, text="", font=("Arial Light", 10), bg='gray69', width=11, height=4).place(x=2, y=45)
        self.b2r1 = Button(self.main_window, text="", font=("Arial Light", 10), bg='gray69', width=11, height=4).place(x=106, y=45)
        self.b3r1 = Button(self.main_window, text="", font=("Arial Light", 10), bg='gray69', width=11, height=4).place(x=209, y=45)
        self.b4r2 = Button(self.main_window, text="", font=("Arial Light", 10), bg='gray69', width=11, height=4).place(x=2, y=125)
        self.b5r2 = Button(self.main_window, text="", font=("Arial Light", 10), bg='gray69', width=11, height=4).place(x=106, y=125)
        self.b6r2 = Button(self.main_window, text="", font=("Arial Light", 10), bg='gray69', width=11, height=4).place(x=209, y=125)
        self.b7r3 = Button(self.main_window, text="", font=("Arial Light", 10), bg='gray69', width=11, height=4).place(x=2, y=205)
        self.b8r3 = Button(self.main_window, text="", font=("Arial Light", 10), bg='gray69', width=11, height=4).place(x=106, y=205)
        self.b9r3 = Button(self.main_window, text="", font=("Arial Light", 10), bg='gray69', width=11, height=4).place(x=209, y=205)

        back = Button(self.main_window)
        back.config(image=smallback_logo,bg='black', compound=LEFT,bd=0,width=30,height=30,command=self.back)
        back.place(x=10,y=5)

        replay = Button(self.main_window)
        replay.config(image=smallre_logo, bg='black', compound=LEFT, bd=0, width=30, height=30,command= lambda : self.end(1))
        replay.place(x=260, y=5)

        self.main_window.mainloop()


    def exit(self):
        sys.exit()

    def close(self):
        self.menu_window.destroy()
        self.main_window()

    def back(self):
        self.main_window.destroy()
        main()

    def replay(self):
        return None

    def end(self,message):

        end_window=Tk()

        end_window.title("Tic Tac Toe")
        end_window.geometry("300x130")
        end_window.configure(background="black")

        re = Button(end_window,text="relpay").place(x=70,y=70)
        exit = Button(end_window, text="exit",command=self.exit).place(x=230, y=70)


        if message==1:

            message_label = Label(end_window,text="You win!!!",bg='black',fg='white',font=("Arial Bold", 15)).place(x=100,y=20)

        else:
            message_label = Label(end_window, text="You Lose!!!", bg='black', fg='white', font=("Arial Bold", 15)).place(
                x=100, y=20)




main()

