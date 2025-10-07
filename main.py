import random
import csv
import sys
from string import ascii_letters, digits, punctuation

def main():
    while True:
        password_list = []
        saved_passwords = []
        password_options = []
        #opens csv file where the passwords are kept
        with open("passwords.csv", "r", newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                saved_passwords.append(row[0])
        password_string = ""
        print("------------------------------")
        print("Welcome to the Offline Password Generator!")
        print("Enter one of the following options:")
        print("1. Generate")
        print("2. Add Password")
        print("3. Saved Passwords")
        print("4. Quit")
        print("------------------------------")
        selection = input()
        selection_lower = selection.lower()
        #start of branches for choices on first screen
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
                note = ""
                #code used to figure out the length of the password and how many numbers and symbols there will be
                password_length = random.randint(10, 16)
                num_letters = random.randint(8 , password_length - 2)
                num_numbers = random.randint(1, password_length - num_letters - 1)
                number_symbols = random.randint(1, password_length - num_letters - num_numbers)
                #the amount of each are added to a list and then randomly picked from it to determine the next value
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
                if len(password_options) == password_length:
                    for i in range(password_length):
                        var = random.choice(password_options)
                        #this is done to prevent a lack of numbers and symbols and generating passwords multiple times
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
                    print("------------------------------")
                    print("Would you like to add a Note to this password? Yes or No")
                    print("------------------------------")
                    #notes are not saved as a new variable to keep important information together and saved in a simple csv file
                    add_note = input()
                    add_note_lower = add_note.lower()
                    if add_note_lower == "yes":
                        note = input("Enter Note:")
                    else:
                        print("------------------------------")
                        print("No Note added")
                        print("------------------------------")
                        main()
                    print("------------------------------")
                    print("Saved")
                    password_save = f'Password: {password_string} / Notes: {note}'
                    print(password_save)
                    saved_passwords.append(password_save)
                    with open("passwords.csv", "w", newline='', encoding='utf-8') as f:
                        writer = csv.writer(f)
                        for item in saved_passwords:
                            writer.writerow([item])
                    main()
                if save_lower == "no":
                    print("------------------------------")
                    print("Password Deleted")
                    print("------------------------------")
                    main()
                elif save_lower != "yes" and "no":
                    print("------------------------------")
                    ready = input("Invalid response. Reenter option.")
        elif selection_lower == "2" or selection_lower == "add passwords":
            number_count = 0
            symbol_count = 0
            #this was added to allow users to keep their passwords in a place convenient for them 
            print("------------------------------")
            print("Please enter password you wish to add.")
            print("------------------------------")
            added_password = input()
            for i in added_password:
                if i in digits:
                    number_count += 1
                if i in punctuation:
                    symbol_count += 1
            print (number_count, symbol_count)
            #this is just a warning to make sure that a lack of number and symbol is realized but not necessary
            if number_count == 0:
                print("------------------------------")
                print("No numbers in password. Are you sure you wish to save password? Yes or No")
                print("------------------------------")
                ok = input()
                ok_lower = ok.lower()
                if ok_lower == "yes":
                    if symbol_count == 0:
                        print("------------------------------")
                        print("No symbol in password. Are you sure you wish to save password? Yes or No")
                        print("------------------------------")
                        second_ok = input()
                        second_ok_lower = second_ok.lower()
                        if second_ok_lower == "yes":
                            saved_passwords.append(added_password)
                            print("------------------------------")
                            print("Saved")
                            print("------------------------------")
                            with open("passwords.csv", "w", newline='', encoding='utf-8') as f:
                                writer = csv.writer(f)
                                for item in saved_passwords:
                                    writer.writerow([item])
                            main()
                        else:
                            print("------------------------------")
                            print("Password not saved")
                            print("------------------------------")
                            main()
                    else:
                        saved_passwords.append(added_password)
                        print("------------------------------")
                        print("Saved")
                        print("------------------------------")
                        with open("passwords.csv", "w", newline='', encoding='utf-8') as f:
                            writer = csv.writer(f)
                            for item in saved_passwords:
                                writer.writerow([item])
                        main()
                else:
                    print("------------------------------")
                    print("Password not saved")
                    print("------------------------------")
                    main()
            if symbol_count == 0:
                print("------------------------------")
                print("No symbol in password. Are you sure you wish to save password? Yes or No")
                print("------------------------------")
                symbol_ok = input()
                symbol_ok_lower = symbol_ok.lower()
                if symbol_ok_lower == "yes":
                    saved_passwords.append(added_password)
                    print("------------------------------")
                    print("Saved")
                    print("------------------------------")
                    with open("passwords.csv", "w", newline='', encoding='utf-8') as f:
                        writer = csv.writer(f)
                        for item in saved_passwords:
                            writer.writerow([item])
                    main()
                else:
                    print("------------------------------")
                    print("Password not saved")
                    print("------------------------------")
                    main()
            else:
                saved_passwords.append(added_password)
                print("------------------------------")
                print("Saved")
                print("------------------------------")
                with open("passwords.csv", "w", newline='', encoding='utf-8') as f:
                    writer = csv.writer(f)
                    for item in saved_passwords:
                        writer.writerow([item])
                main()
        elif selection_lower == "3" or selection_lower == "saved passwords":
            if len(saved_passwords) == 0:
                print("------------------------------")
                print("No saved passwords.")
                print("------------------------------")
                main()
            print("------------------------------")
            print("Please make sure you are not sharing your screen in any for your safety")
            print("Type Ready when ready")
            print("------------------------------")
            ready = input()
            if ready.lower() == "ready":
                print(saved_passwords)
                print("------------------------------")
                print("If you would like to change a password's Notes or Delete a password, enter the password's number(starting at 0)")
                print("Otherwise, enter Return to return")
                print("------------------------------")
                choose_password = input()
                if choose_password == "":
                    print("------------------------------")
                    print("Returning")
                    print("------------------------------")
                    main()
                choose_password_int = int(choose_password)
                if choose_password_int > len(saved_passwords):
                    print("------------------------------")
                    print("Invalid Selection")
                    print("------------------------------")
                    choose_password = input()
                if choose_password in digits and choose_password_int < len(saved_passwords):
                    choose_password_int = int(choose_password)
                    print("------------------------------")
                    print("[{}] selected. Enter Notes to edit notes or Delete to delete chosen password.".format(saved_passwords[choose_password_int]))
                    print("------------------------------")
                    notes_or_delete = input()
                    notes_or_delete_lower = notes_or_delete.lower()
                    if notes_or_delete_lower == "notes" or notes_or_delete_lower == "note":
                        note_split = saved_passwords[choose_password_int].split("Notes: ")
                        print("------------------------------")
                        print("[Previous Note: {}]. Enter new Note.".format(note_split[1]))
                        print("------------------------------")
                        new_note = input("New Note: ")
                        note_split[1] = new_note
                        fixed_note = "Notes: ".join(note_split)
                        print("------------------------------")
                        print("Note changed to {}".format(fixed_note))
                        print("------------------------------")
                        saved_passwords[choose_password_int] = fixed_note
                        with open("passwords.csv", "w", newline='', encoding='utf-8') as f:
                            writer = csv.writer(f)
                            for item in saved_passwords:
                                writer.writerow([item])
                                main()
                    if notes_or_delete_lower == "delete":
                        print("------------------------------")
                        print("Deleting password '[{}]'. Enter Confirm to delete".format(saved_passwords[choose_password_int]))
                        print("------------------------------")
                        finalize = input()
                        if finalize == "Confirm":
                            saved_passwords.pop(choose_password_int)
                            with open("passwords.csv", "w", newline='', encoding='utf-8') as f:
                                writer = csv.writer(f)
                                for item in saved_passwords:
                                    writer.writerow([item])
                                    main()
                            print("------------------------------")
                            print("Password Deleted")
                            print("------------------------------")
                            main()
                        #all of the closing elses followed by the quit option
                        else:
                            print("------------------------------")
                            print("Password Not Deleted")
                            print("------------------------------")
                            main()
                else:
                    print("------------------------------")
                    print("Returning")
                    print("------------------------------")
                    main()
            else:
                print("------------------------------")
                print("Returning")
                print("------------------------------")
                main()
        elif selection_lower == "4" or selection_lower == "quit":
            sys.exit(0)
        else: 
            print("------------------------------")
            print("Invalid response. Reenter option.")
            print("------------------------------")
            main()


if __name__ == "__main__":
    main()