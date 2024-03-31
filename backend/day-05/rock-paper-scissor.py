
"""
Application using the Random function
"""
import random

element = ["rock", "paper", "scissors"]
Player1 = random.choice(element)
Player2 = random.choice(element)

def rock_paper_scissor(player1, player2):
    """
    Determines the winner of a rock-paper-scissors game between two players.

    Parameters:
    player1 (str): The choice of player 1 (rock, paper, or scissor).
    player2 (str): The choice of player 2 (rock, paper, or scissor).

    Returns:
    None
    """
    match player1, player2:
        # player 1 wins
        case "rock", "scissors":
            return("Player 1 Wins!")
        case "paper", "rock":
            return("Player 1 Wins!")
        case "scissors", "paper":
            return("Player 1 Wins!")

        # player 2 wins
        case "scissors", "rock":
            return("Player 2 Wins!")
        case "rock", "paper":
            return("Player 2 Wins!")
        case "paper", "scissors":
            return("Player 2 Wins!")
        
    # Tie? by default? No Checking error seriously? Yea..
    return "It's a tie!"

print(rock_paper_scissor(Player1, Player2))