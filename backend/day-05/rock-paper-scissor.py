
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

print(rock_paper_scissor(Player1, Player2))


# # Test case 1: Player 1 wins with rock against scissors

# assert rock_paper_scissor("rock", "scissors") == "Player 1 Wins!"

# # Test case 2: Player 1 wins with paper against rock
# assert rock_paper_scissor("paper", "rock") == "Player 1 Wins!"

# # Test case 3: Player 1 wins with scissors against paper
# assert rock_paper_scissor("scissors", "paper") == "Player 1 Wins!"

# # Test case 4: Player 2 wins with scissors against rock
# assert rock_paper_scissor("scissors", "rock") == "Player 2 Wins!"

# # Test case 5: Player 2 wins with rock against paper
# assert rock_paper_scissor("rock", "paper") == "Player 2 Wins!"

# # Test case 6: Player 2 wins with paper against scissors
# assert rock_paper_scissor("paper", "scissors") == "Player 2 Wins!"