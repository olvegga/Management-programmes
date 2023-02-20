# Libraries are imported.
import datetime
today = datetime.date.today()
import math

# Several user-defined functions are implemented to execute a number of tasks based on user-input.
# A new user is registered and added to the user file.
def reg_user(userlogin, userdictionary):
    if userlogin == "admin":
        print(f"\nFollow the instructions below to register a new user.")
        new_username = input("Please enter the username: ")    
        while new_username in userdictionary:
            print("The username is already taken. Please select a different username.")
            new_username = input("Please enter the username: ")
        new_password = input("Please enter the password for the username here: ")
        confirm_password = input("Please confirm the password: ")
        while new_password != confirm_password:
            print("The passwords do not match. Please try again.")
            new_password = input("Please enter the password for the username here: ")
            confirm_password = input("Please confirm the password: ")
        print(f"\nA new user has been added.")
        login_ID[new_username] = new_password
        with open('user.txt', 'a') as f:
            f.write(f"\n{new_username}, {new_password}")
    else:
        print("You are not authorised to select this option.")

# A new task is created and added to the task file.
def add_task(userdictionary):
    print("\nFollow the instructions below to add a new task.")
    task_user = input("Please enter the username the task is assigned to: ")
    while task_user not in userdictionary:
        print("The user entered is not registered. Please enter a registered user.")
        task_user = input("Please enter the username the task is assigned to: ")
    task_title = input("Please enter the title of the task: ")
    task_desc = input("Please add a description of the task here: ")
    due_date = input("Please add the due date of the task in this format - DD Mon YYYY - here: ")
    date_today = today.strftime("%d %b %Y")
    task_completion = "No"
    print(f"A new task has been added.")
    with open('tasks.txt', 'a') as tasks:
        tasks.write(f"\n{task_user}, {task_title}, {task_desc}, {date_today}, {due_date}, {task_completion}")
    return

# The user can view all tasks in the task file (complete and incomplete).
def view_all():
    print("\nAll tasks will be shown below.")
    with open('tasks.txt', 'r') as alltasks: 
        for line in alltasks: 
            line = line.split(', ')
            print(f"""
Task:\t\t{line[1].strip()}
Assigned to:\t{line[0].strip()}
Date assigned:\t{line[3].strip()}
Due date:\t{line[4].strip()}
Task Complete?\t{line[5].strip()}
Task Description:
    {line[2].strip()}""")

# The user can view tasks assigned to them.
def view_mine(userdictionary, userlogin):
    with open('tasks.txt', 'r') as mytasks:
        mytasks_dict = {}
        task_line = {}
        tasknumber = 0
        for i, line in enumerate(mytasks):
            line = line.split(', ')
            if userlogin == line[0]:
                tasknumber += 1
                print(f"""\nTask {tasknumber}                
Task:\t\t{line[1].strip()}
Assigned to:\t{line[0].strip()}
Date assigned:\t{line[3].strip()}
Due date:\t{line[4].strip()}
Task Complete?\t{line[5].strip()}
Task Description:
    {line[2].strip()}""")
                mytasks_dict[str(tasknumber)] = line
                task_line[str(tasknumber)] = i
        if tasknumber == 0:
            print("There are no tasks assigned to you.")
            return
# The user can edit a task assigned to them if the task is incomplete by changing 
# the user it is assigned to or the due date.           
    task_select = input(f"\nPlease enter a number of a task to edit or enter '-1' to go back to the main menu.\n")
    while True:
        if task_select == "-1":
            print("\nYou will be taken back to the main menu.")
            return
        elif task_select in mytasks_dict:
            print("You have selected the task below: ")
            print(f"""Task {task_select}                
Task:\t\t{mytasks_dict[task_select][1].strip()}
Assigned to:\t{mytasks_dict[task_select][0].strip()}
Date assigned:\t{mytasks_dict[task_select][3].strip()}
Due date:\t{mytasks_dict[task_select][4].strip()}
Task Complete?\t{mytasks_dict[task_select][5].strip()}
Task Description:
    {mytasks_dict[task_select][2].strip()}""")
            complete = input("Is the task complete? Yes/No: ").lower()
            if complete == "yes":
                mytasks_dict[task_select][5] = "Yes"
                with open('tasks.txt', 'r') as file: 
                    data = file.readlines()
                    data[task_line[task_select]] = (", ".join(mytasks_dict[task_select]))
                    if task_line[task_select] < len(data) - 1:
                                    data[task_line[task_select]] += "\n"
                with open('tasks.txt', 'w') as file:
                    file.writelines(data)
                print(f"\nYou will be brought back to the main menu.")
                return
            else:
                mytasks_dict[task_select][5] = "No"
                edit_choice = input("Do you wish to edit the task? Yes/No: ").lower()
                if edit_choice == "no":
                    print("You will be brought back to the main menu.")
                    return
                elif edit_choice == "yes":
                    while True: 
                        new_user = input(f"Enter the name of the user this task is assigned to:\n")
                        while new_user not in userdictionary:
                            print("The user is not registered. Please enter a registered user.")
                            new_user = input(f"Enter the name of the user this task is assigned to:\n")
                        mytasks_dict[task_select][0] = new_user
                        new_due_date = input(f"Please add the due date of the task in this format - DD Mon YYYY - here: ")
                        mytasks_dict[task_select][4] = new_due_date
                        print(f"""Your edited task is as follows: 
Task {task_select}                
Task:\t\t{mytasks_dict[task_select][1].strip()}
Assigned to:\t{mytasks_dict[task_select][0].strip()}
Date assigned:\t{mytasks_dict[task_select][3].strip()}
Due date:\t{mytasks_dict[task_select][4].strip()}
Task Complete?\t{mytasks_dict[task_select][5].strip()}
Task Description:
    {mytasks_dict[task_select][2].strip()}""")
                        confirmation = input("Please confirm your changes by typing 'confirm' (all lowercase): ")
                        if confirmation == "confirm":
                            with open('tasks.txt', 'r') as file: 
                                data = file.readlines()
                                data[task_line[task_select]] = (", ".join(mytasks_dict[task_select]))
                                if task_line[task_select] < len(data) - 1:
                                    data[task_line[task_select]] += "\n"
                            with open('tasks.txt', 'w') as file:
                                file.writelines(data)
                            print(f"\nChanges have been made. You will be brought back to the main menu now.\n")
                            return
                        else:
                            print("You have not confirmed the task. Please enter the details again before confirming the changes.")
                            continue
                else:
                    print("Your selection is not recognised. Please try again") #loop
        else:
            print("Your selection is not recognised. Please try again.")
            task_select = input(f"Please enter a number of a task to edit or enter '-1' to go back to the main menu.\n")
            print(mytasks_dict)



# The admin can generate reports using information in the user file and task file,
# which are ouputted to a task_overview file and an user_overview file.
def generate_report(userdictionary):
    with open('task_overview.txt', 'w') as task_overview, open('tasks.txt', 'r') as alltasks:
        task_total = 0
        complete_tasks = 0
        incomplete_tasks = 0
        overdue_tasks = 0
        incomplete_overdue_task = 0
        for line in alltasks:
            line = line.split(', ')
            duedate = datetime.datetime.strptime(line[4],("%d %b %Y"))
            task_total += 1
            if line[5].strip() == "Yes":
                complete_tasks += 1
            else:
                incomplete_tasks += 1
                if duedate.date() < today:
                    incomplete_overdue_task += 1            
            if duedate.date() < today:
                overdue_tasks += 1
        percent_incomplete = (incomplete_tasks/task_total) * 100
        percent_overdue = (incomplete_overdue_task/task_total) * 100
        task_overview.write(f"""Task Overview
Total of tasks generated and tracked with task_manager.py = {task_total}
Number of completed tasks: {complete_tasks}
Number of incomplete tasks: {incomplete_tasks}
Number of incomplete tasks that are overdue: {incomplete_overdue_task}
Percentage of incomplete tasks: {percent_incomplete:.2f}%
Percentage of overdue tasks: {percent_overdue:.2f}%""")
    with open ('user_overview.txt', 'w') as user_overview, open('tasks.txt', 'r') as alltasks:
        total_users = len(userdictionary)
        user_overview.write(f"""User Overview
Total of users registered with task_manager.py: {total_users}
Total of tasks generated and tracked with task_manager.py = {task_total}\n""")
        for user in userdictionary.keys():
            user_task_total = 0
            user_task_complete = 0
            user_task_incomplete = 0
            user_task_overdue = 0
            user_task_overdue_incomplete = 0
            alltasks.seek(0)
            for line in alltasks:
                line = line.split(', ')
                duedate = datetime.datetime.strptime(line[4],("%d %b %Y"))
                if line[0].strip() == user:
                    user_task_total += 1
                    if line[5].strip() == "Yes":
                        user_task_complete += 1
                    else:
                        user_task_incomplete += 1
                        if duedate.date() < today:
                            user_task_overdue_incomplete += 1            
                    if duedate.date() < today:
                        user_task_overdue += 1
            if user_task_total == 0:
                userpercent_total = "N/A"
            else:
                userpercent_total = round((user_task_total/task_total) * 100, 2)
            if user_task_total == 0:
                userpercent_complete = "N/A"
            else:
                userpercent_complete = round((user_task_complete/user_task_total) * 100, 2)
            if user_task_total == 0:
                user_percent_incomplete = "N/A"
            else:
                user_percent_incomplete = round((user_task_incomplete/user_task_total) * 100, 2)
            if user_task_total == 0:
                user_percent_overdue = "N/A"
            else:
                user_percent_overdue = round((user_task_overdue_incomplete/user_task_total) * 100, 2)
            user_overview.write(f"""\n{user} Report:
Total of tasks assigned to {user}: {user_task_total}
Percentage of total tasks assigned to {user}: {userpercent_total}%
Percentage of completed tasks: {userpercent_complete}%
Percentage of incomplete tasks: {user_percent_incomplete}%
Percentage of incomplete tasks that are also overdue: {user_percent_overdue}%\n""")
    print("\nYour reports have been generated.")

# The admin can display the contents of the task overview and the user overview files
# in the terminal.
def display_statistics(userdictionary):
    try:
        with open('task_overview.txt', 'r') as task_overview, open('user_overview.txt', 'r') as user_overview:
            pass
    except:
        generate_report(userdictionary)
    with open('task_overview.txt', 'r') as task_overview, open('user_overview.txt', 'r') as user_overview:
        print(f"\nStatistics are displayed below.\n")
        print("-" * 75 + "\n")
        for line in task_overview:
            print(line)
        print(f"\n" + ("-" * 75) + "\n")
        for line in user_overview:
            print(line)
    

# An username and password is required from the user, which is validated
# against a record of usernames and passwords.
login_ID = {}
with open('user.txt', 'r') as logins:
    for line in logins:
        line = line.split(', ')
        login_ID[line[0].strip()] = line[1].strip()
    username_login = input("Username: ")
    password_login = input("Password: ")
    while username_login not in login_ID or login_ID[username_login] != password_login:
        print("Your details are incorrect. Please try again.")
        username_login = input("Username: ")
        password_login = input("Password: ")

# Once login is complete, this menu will be presented. Depending on the selection, a function will 
# be executed. The user input is converted into lowercase for comparison against options.
while True:    
    if username_login == "admin":
        menu = input(f"\nSelect one of the following options below:\nr - Registering a user\na - Adding a task\nva - View all tasks\nvm - View my tasks\ngr - Generate reports\ns - Display statistics\ne - Exit\n").lower()
    else:
        menu = input(f"\nSelect one of the following options below:\nr - Registering a user\na - Adding a task\nva - View all tasks\nvm - View my task\ne - Exit\n").lower()    
    if menu == "r":
        reg_user(username_login, login_ID)
    elif menu == "a":
        add_task(login_ID)
    elif menu == "va":
        view_all()
    elif menu == "vm":                
        view_mine(login_ID, username_login)
    elif menu == "gr":
        generate_report(login_ID)        
    elif menu == "s":
        display_statistics(login_ID)
# If selected, the option below will close the program.
    elif menu == "e":
        print(f"\nGoodbye!")
        exit()
# The code below prints the statement below if the input is not recognised as one of seven options.
    else:
        print("Your choice is not recognised. Please try again.")