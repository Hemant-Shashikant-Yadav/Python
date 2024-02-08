import random

choices = ["rock", "paper", "scissors"]


def user_won():
    print("You Won!!!")


def user_lost():
    print("You Lost!")


print("Enter you choice : ")


def game_engine():
    try:
        user_input = 10
        while user_input != 0:
            computer_choice = random.choice(choices)
            user_input = int(input("1.Rock\t2.Paper\t3.Scissors\t0.EXIT"))
            if user_input == 0:
                print("Terminating program.......")
                exit(0)

            user_choice = choices[user_input - 1]
            print(f"You chose {user_choice} and computer chose {computer_choice}")
            if computer_choice == user_choice:
                print("Match Draw!!")

            if computer_choice == "rock":
                if user_choice == "paper":
                    user_won()
                else:
                    user_lost()

            if computer_choice == "paper":
                if user_choice == "scissors":
                    user_won()
                else:
                    user_lost()

            if computer_choice == "scissors":
                if user_choice == "rock":
                    user_won()
                else:
                    user_lost()

    except TypeError:
        print("Please Enter number as input")
        game_engine()
    except IndexError:
        print("Please Enter the valid input")
        game_engine()
    except Exception as e:
        print(f"Error occurred {e}")



def chat_gpt_code():
    import random

    CHOICES = ["rock", "paper", "scissors"]

    OUTCOMES = {
        ("rock", "scissors"): "You Won!!!",
        ("paper", "rock"): "You Won!!!",
        ("scissors", "paper"): "You Won!!!",
        ("scissors", "rock"): "You Lost!",
        ("rock", "paper"): "You Lost!",
        ("paper", "scissors"): "You Lost!",
    }

    def game_engine():
        while True:
            try:
                user_input = int(input("1.Rock\t2.Paper\t3.Scissors\t0.EXIT: "))
                if user_input == 0:
                    print("Terminating program.......")
                    break

                if user_input not in [1, 2, 3]:
                    print("Please Enter a valid input (1, 2, 3, or 0 to exit).")
                    continue

                user_choice = CHOICES[user_input - 1]
                computer_choice = random.choice(CHOICES)

                print(f"You chose {user_choice} and computer chose {computer_choice}")

                if user_choice == computer_choice:
                    print("Match Draw!!")
                else:
                    outcome = OUTCOMES.get((user_choice, computer_choice), "Invalid Input")
                    print(outcome)

            except ValueError:
                print("Please Enter a valid number.")
            except KeyboardInterrupt:
                print("\nTerminating program.......")
                break

    if __name__ == "__main__":
        print("Welcome to Rock-Paper-Scissors!")
        game_engine()
