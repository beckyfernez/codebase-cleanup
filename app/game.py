



from random import choice

def determine_winner(user_choice, computer_choice):
  
    """
    Assesses two choices, user input and computer random generation, in line with 
    the classic rock, paper, scissors game rules to determine which choice is the winner

    Param: user_choice (string) and computer_choice (string) in accordance to valid_selections

    Example: determine_winner(rock, paper)

    Returns: paper 
    """
  
    #return "paper"
    winners = {
        "rock": {
            "rock": None,
            "paper": "paper",
            "scissors": "rock",
        },
        "paper": {
            "rock": "paper",
            "paper": None,
            "scissors": "scissors",
        },
        "scissors": {
            "rock": "rock",
            "paper": "scissors",
            "scissors": None,
        }
    }
    winning_choice = winners[user_choice][computer_choice]
    return winning_choice
    #return "OOPS"

if __name__ == "__main__":

    #single place for updates in the future
    valid_selections = ["rock", "paper", "scissors"]

    #
    # USER SELECTION
    #

    u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
    print("USER CHOICE:", u)
    if u not in valid_selections:
        print("OOPS, TRY AGAIN")
        exit()

    #
    # COMPUTER SELECTION
    #

    c = choice(valid_selections)
    print("COMPUTER CHOICE:", c)

    #
    # DETERMINATION OF WINNER
    #


    # OLD LOGIC
    #if u == "rock" and c == "rock":
    #    print("It's a tie!")
    #elif u == "rock" and c == "paper":
    #    print("The computer wins")
    #elif u == "rock" and c == "scissors":
    #    print("The user wins")
    #
    #elif u == "paper" and c == "rock":
    #    print("The computer wins")
    #elif u == "paper" and c == "paper":
    #    print("It's a tie!")
    #elif u == "paper" and c == "scissors":
    #    print("The user wins")
    #
    #elif u == "scissors" and c == "rock":
    #    print("The computer wins")
    #elif u == "scissors" and c == "paper":
    #    print("The user wins")
    #elif u == "scissors" and c == "scissors":
    #    print("It's a tie!")

    # NEW LOGIC

    winner = determine_winner(u,c)
    if winner == u:
        print("YOU WON")
    elif winner == c:
        print("COMPUTER WON")
    else:
        print("TIE")