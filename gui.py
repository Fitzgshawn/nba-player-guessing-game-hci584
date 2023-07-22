from tkinter import *
from tkinter.font import BOLD 
#from tkinter import ttk
from tkinter.messagebox import askokcancel
import random
import csv

play_another_round = False

class App(Tk):  # derives your class from TK, so you can run it's inherited mainloop()
    def __init__(self):

        super().__init__()  # run init of your super class, i.e. TK

        # configure the root window
        self.title('NBA guessing game')
        #self.geometry('300x500')

        # Row 0
        # text area used as "terminal" for showing text
        self.text_area = Text(self, height=20, width=70,wrap=WORD, font=('Helvetica', 14, "bold"), spacing3=10)
        self.text_area.grid(row=0, column=0, columnspan=3) # 3 columns wide
        self.text_area.insert(INSERT, "Welcome to the game! Get 5 chances to guess an NBA player from the 2022-2023 season\n") # INSERT refers to the cursor position, which is at the start
        # Make a 3 column grid for: question text (label), text input (answer) and a button that triggers the evaluation

        # Row 1

        # label
        self.question = Label(self, text="Player's name is: ")      
        self.question.grid(row=1, column=0, sticky="e") # stick to east

        # text entry field for the answers
        self.answer_str = StringVar()
        self.answer = Entry(self, width=15, textvariable=self.answer_str) 
        self.answer.bind("<Return>", self.eval_answer)  # callback when Enter/Return is pressed inside entry field
        self.answer.grid(row=1, column=1, sticky="ew") # stretch between label and button

        # GO! button to trigger the player's answer (same as hitting Return)
        self.go = Button(self, text=" Submit!", command=self.eval_answer)
        self.go.grid(row=1, column=2, sticky="w") # sticky="w" make stick to west

        # get data and shuffle
        csv_file = "nba_player_list.csv"
        with open("data/" + csv_file, "r") as f:   
            reader = csv.reader(f)
            rows = list(reader)
            row = random.choice(rows)

        self.random_player = row[1]
        self.ppg = row[30]
        self.rpg = row[22]
        self.apg = row[23]
        self.age = row[5]
        self.team = row[4]

        # define hints
        self.hint_list = [[self.ppg, "points per game"],
                          [self.rpg, "rebounds per game"], 
                          [self.apg, "assists per game"],
                          [self.age, "years old"],
                          [self.team, ""]]

        self.question_number = 0 # 0 to len(hint_list)
        self.show_question() # kick of game with first question.
        # showing the next questions will be triggered in eval_answer


    def show_question(self):
        '''show current question'''

        # grab the 2 parts for the current question
        question_value = self.hint_list[self.question_number][0]
        question_text = self.hint_list[self.question_number][1]

        if self.question_number <= 2:
            self.text_area.insert(INSERT, f"This player averages {question_value} {question_text}. Who is it?\n")
        
        if self.question_number is 3:
                self.text_area.insert(INSERT, f"This player is {question_value} {question_text}. Who is it?\n")
        
        if self.question_number is 4:
            self.text_area.insert(INSERT, f"This player plays for {question_value}. Who is it?\n")
    


    def eval_answer(self, event_data=None):

        # get value of text field
        player = self.answer_str.get()
        if player == self.random_player:
            self.text_area.insert(INSERT, f"Correct, player is {player}!\n\n")
            self.text_area.insert(INSERT, "Play another round?")

            if askokcancel("Play another Round?") == True:
                pass
                # new round:
                # clear text area
                # reset counter
                # get new data
            else:
                pass
                # quit app

        else:
            self.text_area.insert(INSERT, f"{player} is incorrect!\n")

            # Show next hint or fail game
            self.question_number += 1

            if self.question_number >= len(self.hint_list):
                self.text_area.insert(INSERT, f"You are out of hints, the correct player is {self.random_player}!\n\n")
                self.text_area.insert(INSERT, "Play another round?")

                if askokcancel("Play another Round?") == True:
                    pass
                    # new round:
                    # clear text area
                    # reset counter
                    # get new data
                else:
                    pass
                    # quit app

            else:
                self.show_question()


if __name__ == "__main__":
  app = App()
  app.mainloop()
