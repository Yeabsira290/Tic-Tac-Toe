from tkinter import *
import sys
import random


class main():

    def __init__(self):

        self.player = "X"
        self.computer = "o"
        self.beginner = random.randint(0, 1)
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

        # player moves
        self.pfirstRow = 0
        self.psecondRow = 0
        self.pthirdRow = 0

        self.pfirstColumn = 0
        self.psecondColumn = 0
        self.pthirdColumn = 0

        self.pleftDiagonal = 0
        self.prightDiagonal = 0

        self.totalSelected = 0

        # Button Status
        self.selected_buttons = []

        # initializing
        self.game_display = ""
        self.end_window = ""
        self.b1r1 = ""
        self.b2r1 = ""
        self.b3r1 = ""
        self.b4r2 = ""
        self.b5r2 = ""
        self.b6r2 = ""
        self.b7r3 = ""
        self.b8r3 = ""
        self.b9r3 = ""
        self.game = "playing"

        # Main window
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
        letter_x = Radiobutton(self.menu_window, text="X", font=("Arial Bold", 15), variable=letter, bg="black", fg='gray30',
                        value=1, command=lambda: self.letter_assigner("X")).place(x=70, y=130)

        letter_o = Radiobutton(self.menu_window, text="O", font=("Arial Bold", 15), variable=letter, bg="black", fg='gray30',
                        value=2, command=lambda: self.letter_assigner("O")).place(x=200, y=130)
        play = Button(self.menu_window, text="Start", font=("Arial Light", 10), bg='gray69', width=6,
                      command=self.close).place(
            x=70,
            y=190)
        exit1 = Button(self.menu_window, text="Exit", font=("Arial Light", 10), bg='gray69', width=6,
                       command=self.exit).place(
            x=190,
            y=190)
        self.menu_window.mainloop()

    def game_window(self):

        self.game_display = Tk()
        self.game_display.title("Tic Tac Toe")
        self.game_display.geometry("308x300")
        self.game_display.configure(background="black")

        back_logo = PhotoImage(file='back.png')
        resized_back_logo = back_logo.subsample(4, 4)

        replay_logo = PhotoImage(file='relay.png')
        resized_replay_logo = replay_logo.subsample(4, 4)

        self.b1r1 = Button(self.game_display, font=("Arial Bold", 10), bg='gray69', width=11, height=4,
                           command=lambda: self.clicker("b1r1", "player"))
        self.b1r1.place(x=2, y=45)

        self.b2r1 = Button(self.game_display, font=("Arial Bold", 10), bg='gray69', width=11, height=4,
                           command=lambda: self.clicker("b2r1", "player"))
        self.b2r1.place(x=106, y=45)

        self.b3r1 = Button(self.game_display, font=("Arial Bold", 10), bg='gray69', width=11, height=4,
                           command=lambda: self.clicker("b3r1", "player"))
        self.b3r1.place(x=209, y=45)

        self.b4r2 = Button(self.game_display, font=("Arial Bold", 10), bg='gray69', width=11, height=4,
                           command=lambda: self.clicker("b4r2", "player"))
        self.b4r2.place(x=2, y=125)

        self.b5r2 = Button(self.game_display, font=("Arial Bold", 10), bg='gray69', width=11, height=4,
                           command=lambda: self.clicker("b5r2", "player"))
        self.b5r2.place(x=106, y=125)

        self.b6r2 = Button(self.game_display, font=("Arial Bold", 10), bg='gray69', width=11, height=4,
                           command=lambda: self.clicker("b6r2", "player"))
        self.b6r2.place(x=209, y=125)

        self.b7r3 = Button(self.game_display, font=("Arial Bold", 10), bg='gray69', width=11, height=4,
                           command=lambda: self.clicker("b7r3", "player"))
        self.b7r3.place(x=2, y=205)

        self.b8r3 = Button(self.game_display, font=("Arial Bold", 10), bg='gray69', width=11, height=4,
                           command=lambda: self.clicker("b8r3", "player"))
        self.b8r3.place(x=106, y=205)

        self.b9r3 = Button(self.game_display, font=("Arial Bold", 10), bg='gray69', width=11, height=4,
                           command=lambda: self.clicker("b9r3", "player"))
        self.b9r3.place(x=209, y=205)

        back = Button(self.game_display)
        back.config(image=resized_back_logo, bg='black', compound=LEFT, bd=0, width=30, height=30, command=self.back)
        back.place(x=10, y=5)

        replay = Button(self.game_display)
        replay.config(image=resized_replay_logo, bg='black', compound=LEFT, bd=0, width=30, height=30,
                      command=lambda: self.replay("replay"))
        replay.place(x=260, y=5)

        self.game_display.mainloop()

    def clicker(self, button_name, selector):

        self.player_moves_checker()
        self.computer_moves_checker()

        if self.game == "playing":

            draw_status = self.draw_checker()

            if draw_status == 1:

                self.totalSelected += 1

                if selector == "player" and self.next == 1 or self.beginner == 1:

                    self.beginner = -1

                    if button_name == "b1r1":
                        self.b1r1.configure(text=self.player, bg='gray33', state=DISABLED)
                        self.pfirstRow += 1
                        self.pfirstColumn += 1
                        self.pleftDiagonal += 1
                        self.selected_buttons.append("b1r1")

                    elif button_name == "b2r1":
                        self.b2r1.configure(text=self.player, bg='gray33', state=DISABLED)
                        self.pfirstRow += 1
                        self.psecondColumn += 1
                        self.selected_buttons.append("b2r1")

                    elif button_name == "b3r1":
                        self.b3r1.configure(text=self.player, bg='gray33', state=DISABLED)
                        self.pfirstRow += 1
                        self.pthirdColumn += 1
                        self.prightDiagonal += 1
                        self.selected_buttons.append("b3r1")

                    elif button_name == "b4r2":
                        self.b4r2.configure(text=self.player, bg='gray33', state=DISABLED)
                        self.psecondRow += 1
                        self.pfirstColumn += 1
                        self.selected_buttons.append("b4r2")

                    elif button_name == "b5r2":
                        self.b5r2.configure(text=self.player, bg='gray33', state=DISABLED)
                        self.psecondRow += 1
                        self.psecondColumn += 1
                        self.prightDiagonal += 1
                        self.pleftDiagonal += 1
                        self.selected_buttons.append("b5r2")

                    elif button_name == "b6r2":
                        self.b6r2.configure(text=self.player, bg='gray33', state=DISABLED)
                        self.psecondRow += 1
                        self.pthirdColumn += 1
                        self.selected_buttons.append("b6r2")

                    elif button_name == "b7r3":
                        self.b7r3.configure(text=self.player, bg='gray33', state=DISABLED)
                        self.pthirdRow += 1
                        self.pfirstColumn += 1
                        self.prightDiagonal += 1
                        self.selected_buttons.append("b7r3")

                    elif button_name == "b8r3":
                        self.b8r3.configure(text=self.player, bg='gray33', state=DISABLED)
                        self.pthirdRow += 1
                        self.psecondColumn += 1
                        self.selected_buttons.append("b8r3")

                    elif button_name == "b9r3":
                        self.b9r3.configure(text=self.player, bg='gray33', state=DISABLED)
                        self.pthirdRow += 1
                        self.pthirdColumn += 1
                        self.pleftDiagonal += 1
                        self.selected_buttons.append("b9r3")

                    self.update_next(0)

                    if self.totalSelected < 9:
                        self.computer_control()

                else:

                    if button_name == "b1r1":
                        self.b1r1.configure(text=self.computer, bg='gray33', state=DISABLED)

                        self.cfirstRow += 1
                        self.cfirstColumn += 1
                        self.cleftDiagonal += 1
                        self.selected_buttons.append("b1r1")

                    elif button_name == "b2r1":
                        self.b2r1.configure(text=self.computer, bg='gray33', state=DISABLED)

                        self.cfirstRow += 1
                        self.csecondColumn += 1
                        self.selected_buttons.append("b2r1")

                    elif button_name == "b3r1":
                        self.b3r1.configure(text=self.computer, bg='gray33', state=DISABLED)

                        self.cfirstRow += 1
                        self.cthirdColumn += 1
                        self.crightDiagonal += 1
                        self.selected_buttons.append("b3r1")

                    elif button_name == "b4r2":
                        self.b4r2.configure(text=self.computer, bg='gray33', state=DISABLED)

                        self.csecondRow += 1
                        self.cfirstColumn += 1
                        self.selected_buttons.append("b4r2")

                    elif button_name == "b5r2":
                        self.b5r2.configure(text=self.computer, bg='gray33', state=DISABLED)

                        self.csecondRow += 1
                        self.csecondColumn += 1
                        self.crightDiagonal += 1
                        self.cleftDiagonal += 1
                        self.selected_buttons.append("b5r2")

                    elif button_name == "b6r2":
                        self.b6r2.configure(text=self.computer, bg='gray33', state=DISABLED)

                        self.csecondRow += 1
                        self.cthirdColumn += 1
                        self.selected_buttons.append("b6r2")

                    elif button_name == "b7r3":
                        self.b7r3.configure(text=self.computer, bg='gray33', state=DISABLED)

                        self.cthirdRow += 1
                        self.cfirstColumn += 1
                        self.crightDiagonal += 1
                        self.selected_buttons.append("b7r3")

                    elif button_name == "b8r3":
                        self.b8r3.configure(text=self.computer, bg='gray33', state=DISABLED)

                        self.cthirdRow += 1
                        self.csecondColumn += 1
                        self.selected_buttons.append("b8r3")

                    elif button_name == "b9r3":
                        self.b9r3.configure(text=self.computer, bg='gray33', state=DISABLED)

                        self.cthirdRow += 1
                        self.cthirdColumn += 1
                        self.cleftDiagonal += 1
                        self.selected_buttons.append("b9r3")

                    self.update_next(1)

            else:

                self.end("Draw")

            check = self.draw_checker()
            if check == 0:

                self.computer_moves_checker()
                self.player_moves_checker()

                if self.game == "playing":

                    self.end("draw")

    def computer_control(self):

        button_names = ["b1r1", "b2r1", "b3r1", "b4r2", "b5r2", "b6r2", "b7r3", "b8r3", "b9r3"]
        rand = random.randint(0, 8)

        selected = self.button_status_checker(button_names[rand])

        if selected == 1:

            self.clicker(button_names[rand], "computer")

        else:

            self.computer_control()

    def button_status_checker(self, button_name):

        if button_name in self.selected_buttons:

            return 0

        else:

            return 1

    def end(self, message):

        self.end_window = Tk()

        self.end_window.title("Tic Tac Toe")
        self.end_window.geometry("300x130")
        self.end_window.configure(background="black")

        replay = Button(self.end_window, text="Replay", command=lambda: self.replay("re")).place(x=70, y=70)
        close = Button(self.end_window, text="exit", command=self.exit).place(x=230, y=70)
        message_label = Label(self.end_window, text=message, bg='black', fg='white', font=("Arial Bold", 15)).place(
            x=100, y=20)

    def who_start(self):

        if self.beginner == 0:

            self.computer_control()
            self.beginner = -1

        else:

            self.next = 0

    def exit(self):

        sys.exit()

    def close(self):

        self.menu_window.destroy()
        self.game_window()
        self.who_start()

    def back(self):

        self.game_display.destroy()
        main()

    def update_next(self, next_player):

        self.next = next_player

    def letter_assigner(self, letter):

        if letter == "X":

            self.player = "X"
            self.computer = "O"

        else:

            self.player = "O"
            self.computer = "X"

    def draw_checker(self):

        if self.totalSelected == 9:

            return 0

        else:

            return 1

    def computer_moves_checker(self):

        if self.cfirstRow == 3:
            self.end("Computer win")
            self.color_changer("FR")
            self.game = "End"

        elif self.csecondRow == 3:
            self.end("Computer win")
            self.color_changer("SR")
            self.game = "End"

        elif self.cthirdRow == 3:
            self.end("Computer win")
            self.color_changer("TR")
            self.game = "End"

        elif self.cfirstColumn == 3:
            self.end("Computer win")
            self.color_changer("FC")
            self.game = "End"

        elif self.csecondColumn == 3:
            self.end("Computer win")
            self.color_changer("SC")
            self.game = "End"

        elif self.cthirdColumn == 3:
            self.end("Computer win")
            self.color_changer("TC")
            self.game = "End"

        elif self.cleftDiagonal == 3:
            self.end("Computer win")
            self.color_changer("LD")
            self.game = "End"

        elif self.crightDiagonal == 3:
            self.end("Computer win")
            self.color_changer("RD")
            self.game = "End"

    def player_moves_checker(self):

        if self.pfirstRow == 3:
            self.end("You win")
            self.color_changer("FR")
            self.game = "End"

        elif self.psecondRow == 3:
            self.end("You win")
            self.color_changer("SR")
            self.game = "End"

        elif self.pthirdRow == 3:
            self.end("You win")
            self.color_changer("TR")
            self.game = "End"

        elif self.pfirstColumn == 3:
            self.end("You win")
            self.color_changer("FC")
            self.game = "End"

        elif self.psecondColumn == 3:
            self.end("You win")
            self.color_changer("SC")
            self.game = "End"

        elif self.pthirdColumn == 3:
            self.end("You win")
            self.color_changer("TC")
            self.game = "End"

        elif self.pleftDiagonal == 3:
            self.end("You win")
            self.color_changer("LD")
            self.game = "End"

        elif self.prightDiagonal == 3:
            self.end("You win")
            self.color_changer("RD")
            self.game = "End"

    def color_changer(self, direction):

        if direction == "FR":
            self.b1r1.configure(bg='red')
            self.b2r1.configure(bg='red')
            self.b3r1.configure(bg='red')

        if direction == "SR":
            self.b4r2.configure(bg='red')
            self.b5r2.configure(bg='red')
            self.b6r2.configure(bg='red')

        if direction == "TR":
            self.b7r3.configure(bg='red')
            self.b8r3.configure(bg='red')
            self.b9r3.configure(bg='red')

        if direction == "LD":
            self.b1r1.configure(bg='red')
            self.b5r2.configure(bg='red')
            self.b9r3.configure(bg='red')

        if direction == "RD":
            self.b3r1.configure(bg='red')
            self.b5r2.configure(bg='red')
            self.b7r3.configure(bg='red')

        if direction == "FC":
            self.b1r1.configure(bg='red')
            self.b4r2.configure(bg='red')
            self.b7r3.configure(bg='red')

        if direction == "SC":
            self.b2r1.configure(bg='red')
            self.b5r2.configure(bg='red')
            self.b8r3.configure(bg='red')

        if direction == "TC":
            self.b3r1.configure(bg='red')
            self.b6r2.configure(bg='red')
            self.b9r3.configure(bg='red')

    def replay(self, button):

        if button == "re":
            self.end_window.destroy()

        self.beginner = random.randint(0, 1)

        self.b1r1.config(text='', bg='gray69', state=NORMAL)
        self.b2r1.config(text='', bg='gray69', state=NORMAL)
        self.b3r1.config(text='', bg='gray69', state=NORMAL)
        self.b4r2.config(text='', bg='gray69', state=NORMAL)
        self.b5r2.config(text='', bg='gray69', state=NORMAL)
        self.b6r2.config(text='', bg='gray69', state=NORMAL)
        self.b7r3.config(text='', bg='gray69', state=NORMAL)
        self.b8r3.config(text='', bg='gray69', state=NORMAL)
        self.b9r3.config(text='', bg='gray69', state=NORMAL)

        # Button Status
        self.selected_buttons = []

        # total buttons selected
        self.totalSelected = 0

        # computer moves
        self.cfirstRow = 0
        self.csecondRow = 0
        self.cthirdRow = 0

        self.cfirstColumn = 0
        self.csecondColumn = 0
        self.cthirdColumn = 0

        self.cleftDiagonal = 0
        self.crightDiagonal = 0

        # player moves
        self.pfirstRow = 0
        self.psecondRow = 0
        self.pthirdRow = 0

        self.pfirstColumn = 0
        self.psecondColumn = 0
        self.pthirdColumn = 0

        self.pleftDiagonal = 0
        self.prightDiagonal = 0

        self.game = "playing"

        self.who_start()


main()
