import random
# ქვედა ზღვარის მითითება
def get_min_value():
    while True:
        a = input("To Begin, Choose the MIN value for the secret number (must be greater than or equal to 0): ")
        if not a.isdigit():
            continue
        else:
            return int(a)
# ზედა ზღვარის მითითება
def get_max_value(min_value):
    while True:
        b = input(f"Now, Choose the MAX value for the secret number (Must be greater than {min_value}): ")
        if not b.isdigit():
            continue
        else:
            if int(b) > min_value:
                return int(b)
# შემთხვევით შერჩეული რიცვის გენერეაცია
def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)

# ფუნქცია რომელიც გვიბრუნებს მოხმარებლის ცდას არჩეულ რიცხვთა შუალედში
def get_user_guess(min_value, max_value):
    while True:
        user_guess = input(f"Enter your guess ({min_value}-{max_value}): ")
        if not user_guess.lstrip("+-").isdigit():
            continue
        elif not min_value <= int(user_guess) <= max_value:
            print(f"Your guess is out of range of the possible number, make sure to guess between {min_value} and {max_value}")
            continue
        return int(user_guess)
# თამაშის ფუნქციონალური ბლოკი ლუპით
def play_game():
    min_value = get_min_value()
    max_value = get_max_value(min_value)
    random_number = generate_random_number(min_value, max_value)
    guess_counter = 0

    while True:
        user_guess = get_user_guess(min_value, max_value)
        guess_counter += 1

        if user_guess > random_number:
            print(f"Try lower than {user_guess}")
        elif user_guess < random_number:
            print(f"Try higher than {user_guess}")
        else:
            print(f"You guessed the right answer: {random_number} in {guess_counter} guesses\nEND OF THE GAME")
            break

    return input("Do you want to play again? (yes/no): ").lower()
# გაშვება / რესტარტი
if __name__ == "__main__":
    print("Welcome to the game: GUESS THE NUMBER")
    replay = 'yes'
    while replay == 'yes':
        replay = play_game()
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
