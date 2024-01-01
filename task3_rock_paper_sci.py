import random

def get_user_choice():
    choice = input("\nEnter your choice (R, P, S): ").lower()
    if (choice == 'r'):
        choice = 'Rock'
        return choice
    
    elif (choice == 'p'):
        choice = 'Paper'
        return choice
    
    elif (choice == 's'):
        choice = 'Scissors'
        return choice
    
    else:
        print("Invalid Choice")
    
def get_computer_choice():
    choices = ['Rock', 'Paper', 'Scissors']
    return random.choice(choices)

def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "\nIt's a tie!"
    elif ( user_choice == 'Rock' and computer_choice == 'Scissors' ) or \
         ( user_choice == 'Paper' and computer_choice == 'Rock' ) or \
         ( user_choice == 'Scissors' and computer_choice == 'Paper' ):
        return "\nYou Win!\nCongratulations"
    else:
        return "\nComputer Wins!"  

def main():    
    print("A game of Rock, Paper, Scissors")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print("\nYou chose " + user_choice + ". Computer chose " + computer_choice)

        result = winner(user_choice, computer_choice)
        print(result)

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

main()