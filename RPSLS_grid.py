from tkinter import *
import random
from tkinter.ttk import *


screen_w = 400
screen_h = 300
label_w = 300



# def get_center(w):
#     return screen_w / 2 - w / 2



class Game:
    def __init__(self):
        self.root = Tk()
        # self.root.geometry(f"{screen_w}x{screen_h}")
        self.root.title("Rock,Paper,Scissors,Lizard,Spock")
        self.wins = IntVar()
        self.losses = IntVar()
        self.result_txt = StringVar()
        self.loss_amount = 0
        self.win_amount = 0
        self.winning_score = 2
        self.root.resizable(False,False)
        # self.rock_photo = ImageTk.PhotoImage(file="Rock_1.png")

    
    def rps(self):
        self.computer = random.choice(["rock","paper","scissors","lizard","spock"])
        print(self.computer)
        # if self.win_amount < self.winning_score and self.loss_amount < self.winning_score:
        if self.player == self.computer:
            self.result_txt.set("Tasuri!")

        elif self.player == "rock":
            if self.computer == "paper":
                self.loss_amount += 1
                self.losses.set(self.loss_amount)
                self.result_txt.set(f"You lost, {self.computer} covers {self.player}!")

            elif self.computer == "scissors":
                self.win_amount += 1
                self.wins.set(self.win_amount)
                self.result_txt.set(f"You won, {self.player} crushes {self.computer}!")

            elif self.computer == "lizard":
                self.win_amount += 1
                self.result_txt.set(f"You won, {self.player} crushes {self.computer}")
            
            else:
                self.loss_amount += 1
                self.losses.set(self.loss_amount)
                self.result_txt.set(f"You lost, {self.computer} vaporizes {self.player}")


        elif self.player == "paper":
            if self.computer == "scissors":
                self.loss_amount += 1
                self.losses.set(self.loss_amount)
                self.result_txt.set(f"You lost, {self.computer} cuts {self.player}!")

            elif self.computer == "rock":
                self.win_amount += 1
                self.wins.set(self.win_amount)
                self.result_txt.set(f"You won, {self.player} covers {self.computer}!")

            elif self.computer == "spock":
                self.win_amount += 1
                self.wins.set(self.win_amount)
                self.result_txt.set(f"You won, {self.player} disproves {self.computer}")
            
            else:
                self.loss_amount += 1
                self.losses.set(self.loss_amount)
                self.result_txt.set(f"You lost, {self.computer} eats {self.player}")
        
        elif self.player == "scissors":
            if self.computer == "paper":
                self.win_amount += 1
                self.wins.set(self.win_amount)
                self.result_txt.set(f"You won, {self.player} cuts {self.computer}")

            elif self.computer == "lizard":
                self.win_amount += 1
                self.wins.set(self.win_amount)
                self.result_txt.set(f"You won, {self.player} decapitates {self.computer}")

            elif self.computer == "rock":
                self.loss_amount += 1
                self.losses.set(self.loss_amount)
                self.result_txt.set(f"You lost, {self.computer} crushes {self.player}")
            
            else:
                self.loss_amount += 1
                self.losses.set(self.loss_amount)
                self.result_txt.set(f"You lost, {self.computer} smashes {self.player}")

        elif self.player == "lizard":
            if self.computer == "spock":
                self.win_amount += 1
                self.wins.set(self.win_amount)
                self.result_txt.set(f"You won, {self.player} poisons {self.computer}")

            elif self.computer == "paper":
                self.win_amount += 1
                self.wins.set(self.win_amount)
                self.result_txt.set(f"You won, {self.player} eats {self.computer}")

            elif self.computer == "rock":
                self.loss_amount += 1
                self.losses.set(self.loss_amount)
                self.result_txt.set(f"You lost, {self.computer} crushes {self.player}")
            
            else:
                self.loss_amount += 1
                self.losses.set(self.loss_amount)
                self.result_txt.set(f"You lost, {self.computer} decapitates {self.player}")

        elif self.player == "spock":
            if self.computer == "scissors":
                self.win_amount += 1
                self.wins.set(self.win_amount)
                self.result_txt.set(f"You won, {self.player} smashes {self.computer}")

            elif self.computer == "rock":
                self.win_amount += 1
                self.wins.set(self.win_amount)
                self.result_txt.set(f"You won, {self.player} vaporizes {self.computer}")

            elif self.computer == "lizard":
                self.loss_amount += 1
                self.losses.set(self.loss_amount)
                self.result_txt.set(f"You lost, {self.computer} poisons {self.player}")
            
            else:
                self.loss_amount += 1
                self.losses.set(self.loss_amount)
                self.result_txt.set(f"You lost, {self.computer} disproves {self.player}")

        # else:
        #     if self.win_amount > self.loss_amount:
        #         self.result_txt.set("Player Won!")
        
        #     else:
        #         self.result_txt.set("Computer Won!")
                
        


    def player_pick(self,pick):
        self.player = pick
        print(pick)
        self.rps()
    
    # def reset_game(self):
    #     self.wins.set(0)
    #     self.losses.set(0)
    #     self.result_txt.set("")
    #     self.rps()


    def widgets(self):
        #Importing all the pictures
        self.rock_photo = PhotoImage(file = "Rock_1.png")
        self.paper_photo = PhotoImage(file = "Paper_1.png")
        self.scissors_photo = PhotoImage(file = "Scissor_1.png")
        self.lizard_photo = PhotoImage(file = "Lizard_1.png")
        self.spock_photo = PhotoImage(file = "Spock_1.png")

        #resize all the pictures
        self.fit_rock = self.rock_photo.subsample(4,4)
        self.fit_paper = self.paper_photo.subsample(4,4)
        self.fit_scissors = self.scissors_photo.subsample(4,4)
        self.fit_lizard = self.lizard_photo.subsample(4,4)
        self.fit_spock = self.spock_photo.subsample(4,4)

        self.player_score = Label(self.root, textvariable=self.wins,font = ('arial', 18))
        self.result = Label(self.root, textvariable=self.result_txt,font = ('arial', 16))
        self.button_rock = Button(self.root, text = "Rock",image = self.fit_rock, command = lambda: self.player_pick("rock"),width="6")
        self.button_paper = Button(self.root, text = "Paper",image =self.fit_paper, command = lambda: self.player_pick("paper"),width="6")
        self.button_scissors = Button(self.root, text = "Scissors",image = self.fit_scissors, command = lambda: self.player_pick("scissors"), width="6")
        self.button_lizard = Button(self.root, text = "Lizard",image = self.fit_lizard, command = lambda: self.player_pick("lizard"), width="6")
        self.button_spock = Button(self.root, text = "Spock",image = self.fit_spock, command = lambda: self.player_pick("spock"),width="6")


        self.cpu_score = Label(self.root, textvariable=self.losses, font = ('arial', 18))
        self.cpu_score.grid(row=6, column = 3, rowspan = 2, padx = 10, pady = 10)
        self.button_rock.grid(row = 2, column=0)
        self.button_paper.grid(row = 2, column=1)
        self.button_scissors.grid(row = 2, column=2)
        self.button_lizard.grid(row = 2, column=3)
        self.button_spock.grid(row = 2, column=4)
        self.player_score.grid(row = 6, column = 1)
        self.result.grid(row = 8, columnspan = 5)

        self.cpu_text = Label(self.root, text = "CPU",font = ('arial', 18))
        self.cpu_text.grid(row = 4, column = 3)

        self.player_text = Label(self.root, text = "YOU", font = ('arial', 18))
        self.player_text.grid(row = 4, column = 1)






        # self.rock_photo = PhotoImage(file="rock.png")


    def run(self):
        self.widgets()
        self.root.mainloop()
        

app = Game()

if __name__ =="__main__":
    app.run()

