
# Function to check if a player wins in rock-paper-scissors game
def check_winner(player1, player2):
    if player1 == player2:
        return "It's a tie!"
    elif (player1 == 'rock' and player2 == 'scissors') or (player1 == 'paper' and player2 == 'rock') or (player1 == 'scissors' and player2 == 'paper'):
        return "Player 1 wins!"
    else:
        return "Player 2 wins!"

# Test cases
assert check_winner('rock', 'scissors') == "Player 1 wins!"
assert check_winner('paper', 'rock') == "Player 1 wins!"
assert check_winner('scissors', 'paper') == "Player 1 wins!"
assert check_winner('rock', 'paper') == "Player 2 wins!"
assert check_winner('paper', 'scissors') == "Player 2 wins!"
assert check_winner('scissors', 'rock') == "Player 2 wins!"
assert check_winner('rock', 'rock') == "It's a tie!"
assert check_winner('paper', 'paper') == "It's a tie!"
assert check_winner('scissors', 'scissors') == "It's a tie!"

print(check_winner('rock', 'scissor'))

print("All test cases passed!")
