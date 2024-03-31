"""_summary_
Let's rock-paper-scissor

It is switch-case function for the game
param: player1, player2
args: the choice -> scissor, rock

Minimal Implementation
"""

Player1 = input("Player 1: ").lower()
Player2 = input("Player 2: ").lower()

# Function arrives switch-case

def rock_paper_scissor(player1, player2):
    match player1, player2:
        # player 1 wins
        case "rock", "scissor":
            print("Player 1 Wins!")
        case "paper", "rock":
            print("Player 1 Wins!")
        case "scissor", "paper":
            print("Player 1 Wins!")

        # player 2 wins
        case "scissor", "rock":
            print("Player 2 Wins!")
        case "paper", "scissor":
            print("Player 2 Wins!")
        case "rock", "paper":
            print("Player 2 Wins!")
    
rock_paper_scissor(Player1, Player2)