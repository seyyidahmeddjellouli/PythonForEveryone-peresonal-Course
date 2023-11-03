import random
choice = input("Enter your choice (rock, paper, or scissors): ").lower()
if choice not in ['rock', 'paper', 'scissors']:
    print("Invalid choice. Please try again.")
else:
    computer=random.choice(['rock', 'paper', 'scissors'])
    if choice == computer:
        print("it is a tie!")
        print("computer choice",computer)
    elif (choice == 'rock' and computer == 'scissors') or (choice == 'paper' and computer== 'rock') or (choice == 'scissors' and computer == 'paper'):
        print("You win!")
        print("computer choice",computer)
    else:
        print("computer choice",computer)
        print("You lose!")
        