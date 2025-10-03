import random
import csv
import sys
from string import ascii_letters, digits, punctuation

def main():
    password_list = []
    saved_passwords = []
    password_options = []
    with open("passwords.csv", "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            saved_passwords.append(row[0])
    password_string = ""
    print("------------------------------")
    print("Welcome to the offline password generator")
    print("Enter one of the following options:")
    print("1. Generate")
    print("2. Add Password")
    print("3. Saved Passwords")
    print("4. Quit")
    print("------------------------------")
    selection = input()
    selection_lower = selection.lower()
    if selection_lower == "1" or selection_lower == "generate":
        print("------------------------------")
        print("Please make sure you are not sharing your screen in any for your safety")
        print("Type Ready when ready")
        print("------------------------------")
        ready = input()
        if ready.lower() == "ready":
            letter_count = 0
            number_count = 0
            symbol_count = 0
            password_length = random.randint(10, 16)
            num_letters = random.randint(8 , password_length - 2)
            num_numbers = random.randint(1, password_length - num_letters - 1)
            number_symbols = random.randint(1, password_length - num_letters - num_numbers)
            if num_letters + num_numbers + number_symbols < password_length:
                added = random.choice(["number", "symbol"])
                if added == "number":
                    num_numbers += 1
                if added == "symbol":
                    number_symbols += 1
            for i in range(num_letters):
                password_options.append("letter")
            for i in range(num_numbers):
                password_options.append("number")
            for i in range(number_symbols):
                password_options.append("symbol")
            for i in range(password_length):
                var = random.choice(password_options)
                if var == "letter":
                    next_var = random.choice(ascii_letters)
                    password_list.append(next_var)
                    password_options.remove("letter")
                    letter_count += 1
                if var == "number":
                    next_var = random.choice(digits)
                    password_list.append(next_var)
                    password_options.remove("number")
                    number_count += 1
                if var == "symbol":
                    next_var = random.choice(punctuation)
                    password_list.append(next_var)
                    password_options.remove("symbol")
                    symbol_count += 1
            password_string = "".join(password_list)
            print("------------------------------")
            print("Generated Password:", password_string)
            print("Would you like to save this password? Yes or No")
            print("------------------------------")
            save = input()
            save_lower = save.lower()
            if save_lower == "yes":
                saved_passwords.append(password_string)
                print("------------------------------")
                print("Saved")
                print(saved_passwords)
                print("------------------------------")
                with open("passwords.csv", "w", newline="") as f:
                    writer = csv.writer(f)
                    for item in saved_passwords:
                        writer.writerow([item])
            if save_lower == "no":
                print("------------------------------")
                print("Password Deleted")
                print("------------------------------")
            elif save_lower != "yes" and "no":
                print("------------------------------")
                print("Invalid response. Reenter option.")
                print("------------------------------")
                ready = input()
    elif selection_lower == "3" or selection_lower == "saved passwords":
        if len(saved_passwords) == 0:
                print("------------------------------")
                print("No saved passwords.")
                print("------------------------------")
                return
        print("------------------------------")
        print("Please make sure you are not sharing your screen in any for your safety")
        print("Type Ready when ready")
        print("------------------------------")
        ready = input()
        if ready.lower() == "ready":
            print(saved_passwords)
            print("------------------------------")
            print("If you would like to delete a password, enter the password's number(starting at 0)")
            print("Otherwise, enter Return to return")
            print("------------------------------")
            delete = input()
            if delete == "":
                print("------------------------------")
                print("Returning")
                print("------------------------------")
                return
            if delete in digits:
                delete_int = int(delete)
                print("------------------------------")
                print("Deleting password '{}'. Enter Confirm to delete".format(saved_passwords[delete_int]))
                print("------------------------------")
                finalize = input()
                if finalize == "Confirm":
                    saved_passwords.pop(delete_int)
                    with open("passwords.csv", "w", newline="") as f:
                        writer = csv.writer(f)
                        for item in saved_passwords:
                            writer.writerow([item])
                    print("------------------------------")
                    print("Password Deleted")
                    print("------------------------------")
                else:
                    print("------------------------------")
                    print("Password Not Deleted")
                    print("------------------------------")
            else:
                print("------------------------------")
                print("Returning")
                print("------------------------------")
        else:
            print("------------------------------")
            print("Returning")
            print("------------------------------")
    elif selection_lower == "4" or selection_lower == "quit":
        sys.exit(0) 
    else: 
        print("------------------------------")
        print("Invalid response. Reenter option.")
        print("------------------------------")
main()


if __name__ == "__main__":
    main()