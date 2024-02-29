import csv
import os
import random

# გლობალურად გამოსაყენებელი ცვლადები
user_id = 0
logged_in_user_id = None
user_data = []

# ნახულობს სკრიპტის გაშვების ზუსტ მისამართს და იყენებს მას ცსვ ფაილისთვის
script_directory = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(script_directory, 'user_data.csv')

# იღებს user_data -ს ცსვ ფაილიდან
def load_user_data():
    global user_data
    try:
        with open(csv_file_path, mode='r') as file:
            reader = csv.reader(file)
            user_data = [list(map(float, row)) for row in reader]
    except FileNotFoundError:
        # თუ ვერ იპოვა იმ შემთხვევაში იქნება ცარიელი
        user_data = []

load_user_data()

# ვაგენერირებ მომხმარებლის არსებულ წარმოსახვით ბალანსს
def generate_random_balance():
    return round(random.uniform(1000, 10000))

# პინის დარეგისტრირება
def pin_register():
    global user_id, user_data
    if not user_data:
        user_id = 1
    else:
        user_id = max(user[0] for user in user_data) + 1

    print("\nPlease Set-up your PIN [first time only]")
    while True:
        print("\n1st attempt ↓")
        user_input = input("XXXX:")
        # ვალიდაციები
        if not (user_input.isdigit() and len(user_input) == 4):
            print(f"\n[{user_input}] does not match the correct criteria for the PIN, Please enter a valid 4 digits number")
            continue

        print("\nPlease Repeat the pin for confirmation\n2nd attempt ↓\n")
        user_input_repeat = input("XXXX:")
        # განმეორებითი შეყვანის ვალიდაცია
        if not (user_input_repeat.isdigit() and len(user_input_repeat) == 4) or user_input != user_input_repeat:
            print("\nPins provided do not match, Please try again from the beginning\n")
            continue

        # დარეგისტრირების შემდეგ ვამატებ ცსვ ფაილში
        user_data.append([int(user_id), int(user_input), generate_random_balance()])
        print("\nYour PIN was Successfully Registered ✓")
        write_user_data_to_csv()
        return user_id

# პინით დალოგინება, შესაძებელია მხოლოდ იმ შემთხვევაში თუ ცვს ფაილში არსებობს უკვე რეგისტირებული მოხმარებლის ინფორმაცია
def pin_login():
    global user_data, logged_in_user_id

    print("Please Enter your User ID and PIN to login")

    if not user_data:
        print("No users registered. Please register first.")
        return None

    while True:
        try:
            user_input_id = int(input("User ID: "))
            user_input_pin = int(input("XXXX: "))
        except ValueError:
            print("Invalid input. User ID and PIN must be numeric. Please try again.")
            continue

        # ვამოწმებ შეყვანილი ინფორმაციის არსებობას/დამთხვევას
        for user in user_data:
            if user_input_id == user[0] and user_input_pin == user[1]:
                print("Login Successful!")
                logged_in_user_id = user_input_id
                return logged_in_user_id

        print("Incorrect User ID or PIN, Please try again")

# ვწერთ ცსვ ფაილში
def write_user_data_to_csv():
    global user_data
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(user_data)

# ფუნქცია რომელიც აჩვენებს მომხმარებლის ინფორმაციას
def display_user_details(user_id):
    global user_data
    for user in user_data:
        if user_id == user[0]:
            print(f"User ID: {user[0]}")
            print(f"Registered PIN: {user[1]}")
            print(f"User Balance: ${user[2]}")
            break

# თანხის შეტანა/დამატება
def add_money(user_id):
    global user_data
    try:
        amount = int(input("Enter the amount to add to your balance: $"))
    except ValueError:
        print("Invalid input. Please enter a valid whole numeric amount.")
        return

    for user in user_data:
        if user_id == user[0]:
            user[2] += amount
            print(f"${amount} added to your balance. New balance: ${user[2]}")
            write_user_data_to_csv()
            break

# თანხის გამოტანა
def withdraw_money(user_id):
    global user_data
    try:
        amount = int(input("Enter the amount to withdraw from your balance: $"))
    except ValueError:
        print("Invalid input. Please enter a valid whole numeric amount.")
        return

    for user in user_data:
        if user_id == user[0]:
            if user[2] >= amount:
                user[2] -= amount
                print(f"${amount} withdrawn from your balance. New balance: ${user[2]}")
                write_user_data_to_csv()
            else:
                print("Insufficient balance. Withdrawal not allowed.")
            break

# მენიუ
def main_menu():
    global user_data, logged_in_user_id
    print("Welcome to the ATM")
    while True:
        print("\nMain Menu:")
        if logged_in_user_id is None:
            print("1. Register")
            print("2. Login")
        else:
            print(f"Logged in as User ID: {int(logged_in_user_id)}")
            print("3. Display User Details")
            print("4. Add Money to Balance")
            print("5. Withdraw Money from Balance")
            print("6. Logout")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if logged_in_user_id is None:
            if choice == "1":
                user_id = pin_register()
                logged_in_user_id = user_id
            elif choice == "2":
                if not user_data:
                    print("No users registered. Please register first.")
                else:
                    logged_in_user_id = pin_login()
            elif choice == "7":
                print("Exiting the ATM. Goodbye!")
                write_user_data_to_csv()
                break
        elif logged_in_user_id is not None:
            if choice == "3":
                display_user_details(logged_in_user_id)
            elif choice == "4":
                add_money(logged_in_user_id)
            elif choice == "5":
                withdraw_money(logged_in_user_id)
            elif choice == "6":
                print("Logging out.")
                logged_in_user_id = None
            elif choice == "7":
                print("Exiting the ATM. Goodbye!")
                write_user_data_to_csv()
                break
            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main_menu()
