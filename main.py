import json
import os
import sys
from prettytable import PrettyTable
from cryptography.fernet import Fernet


def replace_key(obj, old_key, new_key):
    if isinstance(obj, dict):
        new_obj = {}
        for k, v in obj.items():
            if k == old_key:
                new_obj[new_key] = replace_key(v, old_key, new_key)
            else:
                new_obj[k] = replace_key(v, old_key, new_key)
        return new_obj
    elif isinstance(obj, list):
        return [replace_key(elem, old_key, new_key) for elem in obj]
    else:
        return obj


def edit_course():
    while True:
        try:
            # Load the JSON data from the file
            with open('data.json', 'r') as f:
                data = json.load(f)

            # Create a PrettyTable object
            table = PrettyTable(["Option", "Course"])

            count = 0
            # Add the rows to the table
            for course, (_, _, _, _, _) in data.items():
                table.add_row([count + 1, course])
                count += 1

            # Print and Align the table
            table.align = 'l'
            print(table)

            while True:
                try:
                    # Prompt the user for the key to update
                    key = input("Select an option from the list: ")

                    row = table[int(key) - 1]
                    row.border = False
                    row.header = False
                    option_key = row.get_string(fields=['Course']).strip()

                    # Check if the key exists in the JSON data
                    if option_key in data:
                        while True:
                            t = PrettyTable(["What would you like to edit?"])
                            t.add_rows(
                                [
                                    ["1. Course Name"],
                                    ["2. Number of Credits"],
                                    ["3. Final Grade"],
                                    ["4. Semester & Year"],
                                    ["5. Session"],
                                    ["6. All"]
                                ]
                            )
                            t.align = 'l'
                            print(t)
                            user_option = str(input("Select an option from the list: "))
                            if user_option == "1":
                                print(f"Current Course Name: {option_key}")
                                course_nm = input("Enter Course Name: ")
                                data = replace_key(data, option_key, course_nm)
                                break
                            elif user_option == "2":
                                while True:
                                    t = PrettyTable([f"Current # of Credits: {data[option_key][0]}"])
                                    t.add_rows(
                                        [
                                            ["1. 1 credit"],
                                            ["2. 2 credits"],
                                            ["3. 3 credits"],
                                            ["4. 4 credits"],
                                            ["5. 5 credits"]
                                        ]
                                    )
                                    print(t)

                                    user_option = str(input("Select the # of credits from the list: "))

                                    if user_option == "1":
                                        data[option_key][0] = "1"
                                        break
                                    elif user_option == "2":
                                        data[option_key][0] = "2"
                                        break
                                    elif user_option == "3":
                                        data[option_key][0] = "3"
                                        break
                                    elif user_option == "4":
                                        data[option_key][0] = "4"
                                        break
                                    elif user_option == "5":
                                        data[option_key][0] = "5"
                                        break
                                    else:
                                        print("INVALID, TRY AGAIN.")
                                        continue
                                break
                            elif user_option == "3":
                                while True:
                                    t = PrettyTable([f"Current Final Grade: {data[option_key][1]}"])
                                    t.add_rows(
                                        [
                                            ["1. A"],
                                            ["2. B"],
                                            ["3. C"],
                                            ["4. D"],
                                            ["5. E"],
                                            ["0. Leave Empty"]
                                        ]
                                    )
                                    print(t)

                                    user_option = str(input("Select a final grade from the list: "))

                                    if user_option == "1":
                                        data[option_key][1] = "A"
                                        break
                                    elif user_option == "2":
                                        data[option_key][1] = "B"
                                        break
                                    elif user_option == "3":
                                        data[option_key][1] = "C"
                                        break
                                    elif user_option == "4":
                                        data[option_key][1] = "D"
                                        break
                                    elif user_option == "5":
                                        data[option_key][1] = "E"
                                        break
                                    elif user_option == "0":
                                        data[option_key][1] = ""
                                        break
                                    else:
                                        print("INVALID, TRY AGAIN.")
                                        continue
                                break
                            elif user_option == "4":
                                while True:
                                    t = PrettyTable(
                                        [f"Current Semester & Year: {data[option_key][2]} {data[option_key][3]}"])
                                    t.add_rows(
                                        [
                                            ["1. Fall"],
                                            ["2. Spring"],
                                            ["3. Summer"]
                                        ]
                                    )
                                    t.align = 'l'
                                    print(t)

                                    user_option = str(input("Select a semester from the list: "))

                                    if user_option == "1":
                                        data[option_key][2] = "Fall"
                                        break
                                    elif user_option == "2":
                                        data[option_key][2] = "Spring"
                                        break
                                    elif user_option == "3":
                                        data[option_key][2] = "Summer"
                                        break
                                    else:
                                        print("INVALID, TRY AGAIN.")
                                        continue
                                # Year
                                data[option_key][3] = input("Enter Year: ")
                                break
                            elif user_option == "5":
                                while True:
                                    t = PrettyTable([f"Current Session {data[option_key][4]}"])
                                    t.add_rows(
                                        [
                                            ["1. Reg."],
                                            ["2. 7W-1"],
                                            ["3. 7W-2"],
                                            ["4. 5W-1"],
                                            ["5. 5W-2"],
                                            ["6. 5W-3"]
                                        ]
                                    )
                                    t.align = 'l'
                                    print(t)

                                    user_option = str(input("Select a session from the list: "))

                                    if user_option == "1":
                                        data[option_key][4] = "Reg."
                                        break
                                    elif user_option == "2":
                                        data[option_key][4] = "7W-1"
                                        break
                                    elif user_option == "3":
                                        data[option_key][4] = "7W-2"
                                        break
                                    elif user_option == "4":
                                        data[option_key][4] = "5W-1"
                                        break
                                    elif user_option == "5":
                                        data[option_key][4] = "5W-2"
                                        break
                                    elif user_option == "6":
                                        data[option_key][4] = "5W-3"
                                        break
                                    else:
                                        print("INVALID, TRY AGAIN.")
                                        continue
                                break
                            elif user_option == "6":
                                add_new_course()
                            else:
                                print("INVALID, TRY AGAIN.")
                                continue
                    else:
                        print('Key not found in data')

                    # Write the updated JSON data back to the file
                    with open('data.json', 'w') as f:
                        json.dump(data, f)
                    break
                except:
                    print("Invalid option.")
                    continue
            encrypt()
            break
        except:
            decrypt()
            continue
    menu()


def add_new_course():
    while True:
        try:
            # Load the JSON data from the file
            with open('data.json', 'r') as f:
                data = json.load(f)
            # Prompt the user for the new value
            # Course
            course = input("Enter Course Name: ")
            # Credits
            while True:
                t = PrettyTable(["Number of Credits"])
                t.add_rows(
                    [
                        ["1. 1 credit"],
                        ["2. 2 credits"],
                        ["3. 3 credits"],
                        ["4. 4 credits"],
                        ["5. 5 credits"]
                    ]
                )
                print(t)

                user_option = str(input("Select the # of credits from the list: "))

                if user_option == "1":
                    cred = "1"
                    break
                elif user_option == "2":
                    cred = "2"
                    break
                elif user_option == "3":
                    cred = "3"
                    break
                elif user_option == "4":
                    cred = "4"
                    break
                elif user_option == "5":
                    cred = "5"
                    break
                else:
                    print("INVALID, TRY AGAIN.")
                    continue
            # Final Grade
            while True:
                t = PrettyTable(["Final Grade"])
                t.add_rows(
                    [
                        ["1. A"],
                        ["2. B"],
                        ["3. C"],
                        ["4. D"],
                        ["5. E"],
                        ["0. Leave Empty"]
                    ]
                )
                print(t)

                user_option = str(input("Select a final grade from the list: "))

                if user_option == "1":
                    grd = "A"
                    break
                elif user_option == "2":
                    grd = "B"
                    break
                elif user_option == "3":
                    grd = "C"
                    break
                elif user_option == "4":
                    grd = "D"
                    break
                elif user_option == "5":
                    grd = "E"
                    break
                elif user_option == "0":
                    grd = ""
                    break
                else:
                    print("INVALID, TRY AGAIN.")
                    continue
            # Semester
            while True:
                t = PrettyTable(["Semester"])
                t.add_rows(
                    [
                        ["1. Fall"],
                        ["2. Spring"],
                        ["3. Summer"]
                    ]
                )
                t.align = 'l'
                print(t)

                user_option = str(input("Select a semester from the list: "))

                if user_option == "1":
                    sem = "Fall"
                    break
                elif user_option == "2":
                    sem = "Spring"
                    break
                elif user_option == "3":
                    sem = "Summer"
                    break
                else:
                    print("INVALID, TRY AGAIN.")
                    continue
            # Year
            yr = input("Enter Year: ")
            # Session
            while True:
                t = PrettyTable(["Session"])
                t.add_rows(
                    [
                        ["1. Reg."],
                        ["2. 7W-1"],
                        ["3. 7W-2"],
                        ["4. 5W-1"],
                        ["5. 5W-2"],
                        ["6. 5W-3"]
                    ]
                )
                t.align = 'l'
                print(t)

                user_option = str(input("Select a session from the list: "))

                if user_option == "1":
                    ses = "Reg."
                    break
                elif user_option == "2":
                    ses = "7W-1"
                    break
                elif user_option == "3":
                    ses = "7W-2"
                    break
                elif user_option == "4":
                    ses = "5W-1"
                    break
                elif user_option == "5":
                    ses = "5W-2"
                    break
                elif user_option == "6":
                    ses = "5W-3"
                    break
                else:
                    print("INVALID, TRY AGAIN.")
                    continue
            # Update the JSON data with the new value
            data[course] = cred, grd, sem, yr, ses
            # Write the updated JSON data back to the file
            with open('data.json', 'w') as f:
                json.dump(data, f)
            encrypt()
            break
        except:
            decrypt()
            continue
    menu()


def del_course():
    while True:
        try:
            # Load the JSON data from the file
            with open('data.json', 'r') as f:
                data = json.load(f)

            # Create a PrettyTable object
            table = PrettyTable(["Option", "Course"])

            count = 0
            # Add the rows to the table
            for course, (_, _, _, _, _) in data.items():
                table.add_row([count + 1, course])
                count += 1

            # Print and Align the table
            table.align = 'l'
            print(table)

            # Prompt the user for the key to update
            while True:
                try:
                    key = input("Select an option from the list: ")

                    row = table[int(key) - 1]
                    row.border = False
                    row.header = False
                    option_key = row.get_string(fields=['Course']).strip()

                    if option_key in data:
                        # Remove the key-value pair from the JSON data
                        del data[option_key]
                        print('Course-info pair removed')
                    else:
                        print('Course not found in data')

                    # Write the updated JSON data back to the file
                    with open('data.json', 'w') as f:
                        json.dump(data, f)
                    break
                except:
                    print("Invalid option.")
                    continue
            encrypt()
            break
        except:
            decrypt()
            continue
    menu()


def course_info():
    while True:
        t = PrettyTable(["Add New or Edit Course"])
        t.add_rows(
            [
                ["1. Add New Course"],
                ["2. Edit Course"],
                ["0. Back"]
            ]
        )
        t.align = 'l'
        print(t)

        user_option = str(input("Select an option from the list: "))

        if user_option == "1":
            add_new_course()
            break
        elif user_option == "2":
            edit_course()
            break
        elif user_option == "0":
            menu()
        else:
            print("INVALID, TRY AGAIN.")
            continue


def display_courses():
    while True:
        try:
            # Load the JSON data from the file
            with open('data.json', 'r') as f:
                data = json.load(f)

            # Create a PrettyTable object
            table = PrettyTable(["Course Name", "Number of Credits", "Grade", "Semester", "Year", "Session"])

            # Add the rows to the table
            for course, (creds, grade, semester, year, session) in data.items():
                table.add_row([course, creds, grade, semester, year, session])
            table.align = 'c'

            # Print the table
            print(table)
            input("Press enter to continue")
            encrypt()
            break
        except:
            decrypt()
            continue
    menu()


def gpa():
    while True:
        try:
            # initialize variables
            points = 0
            num_credits = 0

            # Load the JSON data from the file
            with open('data.json', 'r') as f:
                data = json.load(f)

            for value in data.values():
                # print(value[0])
                if value[1] == "A":
                    grade = 4.0
                    points = points + int(value[0]) * grade
                    num_credits = num_credits + int(value[0])
                    # print(points)
                elif value[1] == "B":
                    grade = 3.0
                    points = points + int(value[0]) * grade
                    num_credits = num_credits + int(value[0])
                    # print(points)
                elif value[1] == "C":
                    grade = 2.0
                    points = points + int(value[0]) * grade
                    num_credits = num_credits + int(value[0])
                    # print(points)
                elif value[1] == "D":
                    grade = 1.0
                    points = points + int(value[0]) * grade
                    num_credits = num_credits + int(value[0])
                    # print(points)
                elif value[1] == "E":
                    points = points + int(value[0])
                    num_credits = num_credits + int(value[0])
                    # print(points)
                else:
                    continue

            t = PrettyTable(["Total Grading Points", "Total Number of Credits", "Overall GPA"])
            try:
                overall_gpa = points / num_credits
            except:
                overall_gpa = "N/A"
            t.add_row([points, num_credits + 44, overall_gpa])
            print(t)

            input("Press enter to continue")
            encrypt()
            break
        except:
            decrypt()
            continue
    menu()


def encrypt():
    key = os.environ.get('SECRET_KEY')
    f_key = Fernet(key)

    # Load the JSON data from the file
    with open('data.json', 'r') as f:
        data = f.read().encode()

    # Encrypt the data
    encrypted_data = f_key.encrypt(data)

    # Write the encrypted data to the file
    with open('data.json', 'wb') as f:
        f.write(encrypted_data)


def decrypt():
    key = os.environ.get('SECRET_KEY')
    f_key = Fernet(key)

    # Load the encrypted data from the file
    with open('data.json', 'rb') as f:
        encrypted_data = f.read()

    # Decrypt the data
    decrypted_data = f_key.decrypt(encrypted_data)

    # Write the encrypted data to the file
    with open('data.json', 'wb') as f:
        f.write(decrypted_data)


def menu():
    t = PrettyTable(["Options"])
    t.add_rows(
        [
            ["1. Add/Edit Course"],
            ["2. Delete Course"],
            ["3. Display Courses"],
            ["4. GPA"],
            ["0. Quit"]
        ]
    )
    t.align = 'l'
    print(t)

    user_option = str(input("Select an option from the list: "))

    if user_option == "1":
        course_info()
    elif user_option == "2":
        del_course()
    elif user_option == "3":
        display_courses()
    elif user_option == "4":
        gpa()
    elif user_option == "0":
        sys.exit()
    else:
        print("INVALID, TRY AGAIN.")
        menu()


if __name__ == '__main__':
    menu()
