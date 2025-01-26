import random
score = 0
computer_score = 0

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

ROCK!
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

PAPER!
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

SCISSORS!
'''

# ------------------------------------------------------------------
rock_paper_scissors = [rock,paper,scissors]
print("Want to play a game of Rock, Paper, Scissors? First to three!")

while score < 3 and computer_score < 3:
    turn = input("What do you choose? ")
    computer_choice = random.choice(rock_paper_scissors)

    if turn == "rock" and computer_choice == rock:
        print(rock)
        print(computer_choice)
        print("Its a Draw.")
        print(f"The Scores are: Your Score: {score}. Computer Score {computer_score}")
    elif turn == "rock" and computer_choice == paper:
        computer_score += 1
        print(rock)
        print(computer_choice)
        print("You Lose.")
        print(f"The Scores are: Your Score: {score}. Computer Score {computer_score}")
    elif turn == "rock" and computer_choice == scissors:
        score += 1
        print(rock)
        print(computer_choice)
        print("You Win!")
        print(f"The Scores are: Your Score: {score}. Computer Score {computer_score}")
    elif turn == "paper" and computer_choice == paper:
        print(paper)
        print(computer_choice)
        print("Its a Draw.")
        print(f"The Scores are: Your Score: {score}. Computer Score {computer_score}")
    elif turn == "paper" and computer_choice == scissors:
        computer_score += 1
        print(paper)
        print(computer_choice)
        print("You Lose.")
        print(f"The Scores are: Your Score: {score}. Computer Score {computer_score}")
    elif turn == "paper" and computer_choice == rock:
        score += 1
        print(paper)
        print(computer_choice)
        print("You Win!")
        print(f"The Scores are: Your Score: {score}. Computer Score {computer_score}")
    elif turn == "scissors" and computer_choice == scissors:
        print(scissors)
        print(computer_choice)
        print("Its a Draw.")
        print(f"The Scores are: Your Score: {score}. Computer Score {computer_score}")
    elif turn == "scissors" and computer_choice == rock:
        computer_score += 1
        print(scissors)
        print(computer_choice)
        print("You Lose.")
        print(f"The Scores are: Your Score: {score}. Computer Score {computer_score}")
    elif turn == "scissors" and computer_choice == paper:
        score += 1
        print(scissors)
        print(computer_choice)
        print("You Win!")
        print(f"The Scores are: Your Score: {score}. Computer Score {computer_score}")

if score == 3:
    print("You Won! Congratulations")
    exit()
elif computer_score == 3:
    print("You Lost! Better luck next time.")
    exit()