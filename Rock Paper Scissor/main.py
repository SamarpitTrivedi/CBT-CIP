import tkinter as tk
from random import choice
from PIL import Image, ImageTk

class RockPaperScissors:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Rock Paper Scissors")
        self.root.geometry("1000x400")
        self.player_score = 0
        self.computer_score = 0

        self.player_score_label = tk.Label(self.root, text="Player Score: 0", font=("Arial", 24, "bold"))
        self.player_score_label.pack()

        self.computer_score_label = tk.Label(self.root, text="Computer Score: 0", font=("Arial", 24, "bold"))
        self.computer_score_label.pack()

        self.result_label = tk.Label(self.root, text="", font=("Arial", 24, "bold"))
        self.result_label.pack()

        self.rock_image = ImageTk.PhotoImage(Image.open("rock.png"))
        self.paper_image = ImageTk.PhotoImage(Image.open("paper.png"))
        self.scissor_image = ImageTk.PhotoImage(Image.open("scissor.png"))

        self.rock_button = tk.Button(self.root, image=self.rock_image, command=self.rock, width=200, height=200)
        self.rock_button.pack(side=tk.LEFT, padx=30, pady=30)

        self.paper_button = tk.Button(self.root, image=self.paper_image, command=self.paper, width=200, height=200)
        self.paper_button.pack(side=tk.LEFT, padx=30, pady=30)

        self.scissor_button = tk.Button(self.root, image=self.scissor_image, command=self.scissor, width=200, height=200)
        self.scissor_button.pack(side=tk.LEFT, padx=30, pady=30)

        self.reset_button = tk.Button(self.root, text="RESET", command=self.reset, font=("Arial", 24, "bold"), width=10, height=2)
        self.reset_button.pack(padx=20, pady=20)

    def computer_choice(self):
        return choice(["rock", "paper", "scissor"])

    def rock(self):
        computer = self.computer_choice()
        if computer == "rock":
            self.result_label['text'] = "It's a tie!"
        elif computer == "paper":
            self.computer_score += 1
            self.computer_score_label['text'] = f"Computer Score: {self.computer_score}"
            self.result_label['text'] = "Paper covers rock! Computer wins!"
        else:
            self.player_score += 1
            self.player_score_label['text'] = f"Player Score: {self.player_score}"
            self.result_label['text'] = "Rock smashes scissor! Player wins!"

    def paper(self):
        computer = self.computer_choice()
        if computer == "paper":
            self.result_label['text'] = "It's a tie!"
        elif computer == "rock":
            self.player_score += 1
            self.player_score_label['text'] = f"Player Score: {self.player_score}"
            self.result_label['text'] = "Paper covers rock! Player wins!"
        else:
            self.computer_score += 1
            self.computer_score_label['text'] = f"Computer Score: {self.computer_score}"
            self.result_label['text'] = "Scissor cuts paper! Computer wins!"

    def scissor(self):
        computer = self.computer_choice()
        if computer == "scissor":
            self.result_label['text'] = "It's a tie!"
        elif computer == "paper":
            self.player_score += 1
            self.player_score_label['text'] = f"Player Score: {self.player_score}"
            self.result_label['text'] = "Scissor cuts paper! Player wins!"
        else:
            self.computer_score += 1
            self.computer_score_label['text'] = f"Computer Score: {self.computer_score}"
            self.result_label['text'] = "Rock smashes scissor! Computer wins!"

    def reset(self):
        self.player_score = 0
        self.computer_score = 0
        self.player_score_label['text'] = "Player Score: 0"
        self.computer_score_label['text'] = "Computer Score: 0"
        self.result_label['text'] = ""

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = RockPaperScissors()
    game.run()