#all module required to run the programs
import datetime
import os
import pyinputplus as pypi
import csv
from tabulate import tabulate


def clear_screen():

    """
    A function to clean the user interface/terminal
    """
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')
def greetings():
    """
    a fuction to display time as (Good morning, Good afternoon, Good evening based on time we accesing the terminal)

    Returns:
        _type_: String
    """    
    # Get the current time
    now = datetime.datetime.now()

    # Determine the greetings
    if now.hour < 12:
        greeting = "Good morning"
    elif now.hour < 17:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    return greeting


def create_student_data():
    """
    this function use for inputing new student data into database called data.csv, it consist of defining variable that
    inputed as student data information such as below:
    """    
    # Read the existing data
    found = False
    students = []
    with open("data/data.csv", mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
            found = True

    if not found:
        print("database is empty, procced to input new data..\n")

    # Check for duplicate Student_ID
    new_student_id = pypi.inputInt("Enter student ID: ")
    found_duplicate = False

    for student in students:
        if int(student['Student_ID']) == new_student_id:
            found_duplicate = True
            exit = pypi.inputYesNo('Im sorry ID has already taken, press ENTER..', blank=True)
            if exit == "yes" or exit == "":
                break
    
    if not found_duplicate:
        # Input student data
        Name = pypi.inputStr("Enter student name: ")
        Address = pypi.inputStr("Enter student address: ")
        Age = pypi.inputInt("Enter student age: ")
        Gender = pypi.inputChoice(prompt=" 'Male' or 'Female' : ", choices=["Male", "Female"])

        # Create the new student dictionary
        new_student = {'Student_ID': new_student_id, 'Name': Name,
                       'Address': Address, 'Age': Age, 'Gender': Gender}

        # Add the new student data to the existing list
        students.append(new_student)

        # Write the updated data back to the CSV file
        with open("data/data.csv", mode='w', newline='') as file:
            fieldnames = ['Student_ID', 'Name', 'Address', 'Age', 'Gender']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students)

def create_student_score():
    """
    this function use for inputing new student data into database called data.csv, it consist of defining variable that
    inputed as student data information such as below:
    """
    # Read the existing data
    found = False
    students_score = []
    with open("data/student_score.csv", mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students_score.append(row)
            found = True

    if not found:
        print("database is empty, procced to input new data..\n")

    # Check for duplicate Student_ID
    Student_Score_ID = pypi.inputInt("Enter student ID: ")
    found_duplicate = False

    for student in students_score:
        if int(student['Student_ID']) == Student_Score_ID:
            found_duplicate = True
            exit = pypi.inputYesNo(
                'Im sorry ID has already taken, press ENTER..', blank=True)
            if exit == "yes" or exit == "":
                break

    if not found_duplicate:
        # Input student data
        Name = pypi.inputStr("Enter student name: ")
        GrossMotorDev = pypi.inputInt("Enter GMD(gross motor development): ")
        FineMotorDev = pypi.inputInt("Enter FMD(fine motor development): ")
        LangComm = pypi.inputInt("Enter Language & Communication): ")
        SocEmo = pypi.inputInt("Enter Social & Emotional): ")
        CogAbility = pypi.inputInt("Enter Cognitive & Ability): ")

        # Create the new student dictionary
        new_student = {'Student_ID': Student_Score_ID, 'Name': Name, 'GMD': GrossMotorDev,
                       'FMD': FineMotorDev, 'LangComm': LangComm, 'SocEmo': SocEmo, 'CogAbility': CogAbility}

        # Add the new student data to the existing list
        students_score.append(new_student)

        # Write the updated data back to the CSV file
        with open("data/student_score.csv", mode='w', newline='') as file:
            fieldnames = ['Student_ID', 'Name', 'GMD',
                          'FMD', 'LangComm', 'SocEmo', 'CogAbility']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students_score)

def read_students_data():
    """this function created for displaying the outcome or the database by iterating each row in the reader which based on student data database
        and storing them into readStudentData variable, showing the into more readable output using tabulate then suggested to come back to
        previous menu after that and cleaning the interface using clear_screen function
    """    
    found = False
    readStudentsData = []
    with open("data/data.csv", mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            readStudentsData.append(row)
            clear_screen()
            print("Student Data of Tadika Mesra preschool")
            table = tabulate(readStudentsData, headers="keys", tablefmt="pretty")
            print(table)
            found = True

    if not found:
        clear_screen()
        print("Database is empty..\n")

    exit = pypi.inputYesNo(
        prompt="Press 'ENTER' to back to previous menu or (yes/no)", blank=True
        )
    if exit == "yes" or exit == "":
        clear_screen()

def read_students_data_score():
    """
    this function created for displaying the outcome or the database by iterating each row in the reader which based on student score database
        and storing them into readStudentaScore variable, showing the into more readable output using tabulate then suggested to come back to
        previous menu after that and cleaning the interface using clear_screen function
    
    """    
    found = False
    ReadStudentsScore = []
    with open("data/student_score.csv", mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            ReadStudentsScore.append(row)
            clear_screen()
            print("Student Score of Tadika Mesra preschool")
            table = tabulate(ReadStudentsScore, headers="keys", tablefmt="pretty")
            print(table)
            found = True

    if not found:
        clear_screen()
        print("Database is empty..\n")
    exit = pypi.inputYesNo(
            prompt="Press 'ENTER' to back to previous menu or (yes/no)", blank=True
            )
    if exit == "yes" or exit == "":
        clear_screen()

def read_certain_students_data():
    """the function itself have a purpose to select desired data (student data), first it defining which data we want to select
        by inserting an input, the next step is to iterating the .csv file named data.csv, if the value of iteration is 
        identical as we already inputed it will start cleaing the terminal and print the result
    """     
    student_id = pypi.inputInt("Enter certain student_ID: ")   
    # Read the existing data
    students_data = []
    with open("data/data.csv", mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students_data.append(row)

    # Find and show choosen student data
    found = False
    for student in students_data:
        if student['Student_ID'] == str(student_id):
            clear_screen()
            print("Showing certain student data..")
            print(student)
            found = True
    if not found:
        clear_screen()
        print("data is not found..\n")

    exit = pypi.inputYesNo(
        prompt="\n Press 'ENTER' to back to previous menu or (yes/no)", blank=True
        )
    if exit == "yes" or exit == "":
        clear_screen()        

def read_certain_students_data_score():
    """the function itself have a purpose to select desired data (student_score), first it defining which data we want to select
        by inserting an input, the next step is to iterating the .csv file named student_score.csv, if the value of iteration is 
        identical as we already inputed it will start cleaing the terminal and print out the result
    """    
    student_id = pypi.inputInt("Enter certain student_ID: ")   
    
    # Read the existing data
    students_score = []
    with open("data/student_score.csv", mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students_score.append(row)
    print(students_score)
    
    # Find and show choosen student data
    found = False
    for student in students_score:
        if student['Student_ID'] == str(student_id):
            clear_screen()
            print("Showing certain student score..")
            print(student)
            found = True
    if not found:
        clear_screen()
        print("Data not found..\n")

    exit = pypi.inputYesNo(
        prompt="\n Press 'ENTER' to back to previous menu or (yes/no)", blank=True
        )
    if exit == "yes" or exit == "":
        clear_screen()                 

def update_student_data():
    
    """update_student_data function is use for changing each value on certain column, first the function need to defining which

    """
    #Select desired input
    student_id = pypi.inputInt("Enter certain student_ID: ")

    # Read the existing data
    found = False
    students_data = []
    with open("data/data.csv", mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students_data.append(row)

    # Find and show choosen student data
    for student in students_data:
        if student['Student_ID'] == str(student_id):
            print(student)
            found = True

            New_Name = pypi.inputStr(prompt="Enter New Name: ",blank=True)
            if New_Name != "":
                student['Name'] = New_Name
            
            New_Address = pypi.inputStr(prompt="Enter New Address: ",blank=True)
            if New_Address != "":
                student["Address"] = New_Address

            New_Age = pypi.inputStr(prompt="Enter New Age: ",blank=True)
            if New_Age!="":
                student['Age'] = New_Age

            New_Gender = pypi.inputChoice(prompt=" 'Male' or 'Female' : ", choices=["Male", "Female"], blank=True)
            if New_Gender != '':
                student['Gender'] = New_Gender
            
            clear_screen()
            print("Showing certain student data updated..")
            print(student)

    if not found:
        print("\n Data not found..\n")

    #updating new values on csv file
    with open("data/data.csv", mode='w', newline='') as file:
        fieldnames = ['Student_ID', 'Name', 'Address', 'Age', 'Gender']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students_data)

    exit = pypi.inputYesNo(
        prompt="\n Press 'ENTER' to back to previous menu or (yes/no)", blank=True
        )
    if exit == "yes" or exit == "":
        clear_screen()

def update_student_score_data():
    """
    update_student_data function is use for changing each value on certain column, first the function need to defining which
        
    """
    #Select desired input by accessing its ID (Student_ID)
    student_id = pypi.inputInt("Enter certain student_ID: ")

    # Read the existing data

    students_score = []
    with open("data/student_score.csv", mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students_score.append(row)
   
    # Find and show choosen student data
    found = False
    for student in students_score:
        if student['Student_ID'] == str(student_id):
            print(student)
            found = True

            New_Name = pypi.inputStr(prompt="Enter New Name: ",blank=True)
            if New_Name != "":
                student['Name'] = New_Name
            
            New_GrossMotorDev = pypi.inputInt(prompt="Enter GMD: ", blank=True)
            if New_GrossMotorDev != "":
                student["GMD"] = New_GrossMotorDev

            New_FineMotorDev = pypi.inputInt(prompt="Enter New FMD: ",blank=True)
            if New_FineMotorDev != "":
                student['FMD'] = New_FineMotorDev

            New_LangComm = pypi.inputInt(prompt="Enter New LangComm: ",blank=True)
            if New_LangComm != "":
                student['LangComm'] = New_LangComm
            
            New_SocEmo = pypi.inputInt(prompt="Enter New SocEmo: ",blank=True)
            if New_SocEmo != "":
                student['SocEmo'] = New_SocEmo
            
            New_CogAbility = pypi.inputInt(prompt="Enter New CogAbility: ",blank=True)
            if New_CogAbility != "":
                student['CogAbility'] = New_CogAbility

            clear_screen()
            print("Showing certain student score updated..")
            print(student)
    if not found:
        print("\n Data not found..\n")

    #updating new values on csv file
    with open("data/student_score.csv", mode='w', newline='') as file:
        fieldnames = ['Student_ID', 'Name', 'GMD', 'FMD', 'LangComm', 'SocEmo', 'CogAbility']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students_score)

    exit = pypi.inputYesNo(
        prompt="Press 'ENTER' to back to previous menu or (yes/no)", blank=True
        )
    if exit == "yes" or exit == "":
        clear_screen()

def delete_student_data():
    clear_screen()
    print("Deleting student data..")
    students_data = []
    with open("data/data.csv", mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students_data.append(row)
            clear_screen()
            print("Showing student data of Tadika Mesra preschool")
            table = tabulate(students_data, headers="keys", tablefmt="pretty")
            print(table)

    #Input student_ID        
    student_id = pypi.inputInt("Enter student_ID to delete: ")

    # Read the existing data
    students_data = []
    with open("data/data.csv", mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students_data.append(row)
            
    # Find and remove the student data
    removed = False
    for student in students_data:
        if student['Student_ID'] == str(student_id):
            students_data.remove(student)
            removed = True
            break

    if removed:
        # Write the updated data back to the CSV file
        with open("data/data.csv", mode='w', newline='') as file:
            fieldnames = ['Student_ID', 'Name', 'Address', 'Age', 'Gender']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(students_data)
            print(f"Deleted student with Student_ID: {student_id}")            
    else:
        print(f"there is't any Student_ID with the number of: {student_id}.")

    exit = pypi.inputYesNo(
        prompt="Press 'ENTER' to back to previous menu or (yes/no)", blank=True
        )
    if exit == "yes" or exit == "":
        clear_screen()
        
def delete_student_score_data():
    clear_screen()
    print("Deleting student score..")
    students_score = []
    with open("data/student_score.csv", mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students_score.append(row)
            clear_screen()
            print("Showing student Score of Tadika Mesra Preschool")
            table = tabulate(students_score, headers="keys", tablefmt="pretty")
            print(table)
    
    #input student_ID
    student_id = pypi.inputInt("Enter student_ID to delete: ")

    # Read the existing data
    students_score = []
    with open("data/student_score.csv", mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            students_score.append(row)

    # Find and remove the student score data
    removed = False
    for student in students_score:
        if student['Student_ID'] == str(student_id):
            students_score.remove(student)
            removed = True
            break

    if removed:
        # Write the updated data back to the CSV file
        with open("data/student_score.csv", mode='w', newline='') as file:
            fieldnames = ['Student_ID', 'Name', 'GMD', 'FMD', 'LangComm', 'SocEmo', 'CogAbility']
            writer = csv.DictWriter(file, fieldnames = fieldnames)
            writer.writeheader()
            writer.writerows(students_score)
            print(f"Deleted student score with Student_ID: {student_id}")
    else:
        print(f"there is't any Student_ID with the number of: {student_id}.")

    exit = pypi.inputYesNo(
        prompt="Press 'ENTER' to back to previous menu or (yes/no)", blank=True
        )
    if exit == "yes" or exit == "":
        clear_screen()
                
#Terminal Functions
def Show():
    """_summary_
    this function means to display an interface of show menu which consist on how we going to do with the data, 
    in this case this function mean to display a data inside database, the function also can display a certain data we choose.
    """    
    # to display the interface of the show data menu.
    while True:
        clear_screen()
        print(f"========================================================")
        print("---------------SHOWING STUDENT DATA---------------------")
        print("========================================================")

        print(f"1. Show all of student data.. ")
        print(f"2. Show all of student score data..")
        print(f"3. Show particular student data..")
        print(f"4. Show particular student score data..")
        print(f"5. Back to previous menu..")
        print("========================================================")

        # a function which giving an order to execute which program will run based on choices we made
        Choose_show = pypi.inputInt("Choose 1-5: ", min=1, max=5, default=1)

        # a function that gave us an option on which program on display menu interface will be executed
        if Choose_show == 1:
            read_students_data()
        elif Choose_show == 2:
            read_students_data_score()
        elif Choose_show == 3:
            read_certain_students_data()
        elif Choose_show == 4:
            read_certain_students_data_score()
        elif Choose_show == 5:
            print("5. Back to previous menu..")
            exit = pypi.inputYesNo(prompt="Press 'ENTER' for back to main terminal or (yes/no)", blank=True)
            if exit == "yes" or exit == "":
                clear_screen()
                break
                         
def Add():
    """_summary_
    this function means to display an interface of add menu which consist on how we going to do with the data, 
    in this case this function mean to add a new data to database.
    """    
    # to display the interface of the delete menu.
    while True:
        clear_screen()
        print(f"========================================================")
        print("-----------------ADDING STUDENT DATA-------------------")
        print("========================================================")

        print(f"1. Input new student data.. ")
        print(f"2. Input new student score..")
        print(f"3. Back to previous menu..")
        print("========================================================")

        # a function which giving an order to execute which program will run based on choices we made
        Choose_add= pypi.inputInt("Choose 1-3: ", min=1, max=3, default=1)

        # a function that gave us an option on which program on add menu interface will be executed
        if Choose_add == 1:
            create_student_data()
        elif Choose_add == 2:
            create_student_score()
        elif Choose_add == 3:
            print("3. Back to previous menu..")
            exit = pypi.inputYesNo(prompt="Press 'ENTER' for back to main terminal or (yes/no)", blank=True)
            if exit == "yes" or exit == "":
                clear_screen()
                break
                
def Update():
    """_summary_
    this function means to display an interface of update menu which consist on how we going to do with the data, 
    in this case this function mean to changing the content of selected data.
    """    
    # to display the interface of the update menu.
    while True:
        clear_screen()
        print(f"========================================================")
        print("------------------UPDATE STUDENT DATA-------------------")
        print("========================================================")

        print(f"1. Changing student data..  ")
        print(f"2. Changing student score data..")
        print(f"3. Back to previous menu..")
        print("========================================================")

        # a function which giving an order to execute which program will run based on choices we made
        Choose_update= pypi.inputInt("Choose 1-3: ", min=1, max=3, default=1)

        # a function that gave us an option on which program on update menu interface will be executed
        if Choose_update == 1:
            update_student_data()
        elif Choose_update == 2:
            update_student_score_data()
        elif Choose_update == 3:
            print("3. Back to previous menu..")
            exit = pypi.inputYesNo(
                prompt="Press 'ENTER' for back to main terminal or (yes/no)", blank=True)
            if exit == "yes" or exit == "":
                clear_screen()
                break
                
def Delete():
    """_summary_
    this function means to display an interface of delete menu which consist on how we going to do with the data, 
    in this case this function mean to deleting data we choose.
    """    
    # to display the interface of the delete menu.
    while True:
        clear_screen()
        print(f"========================================================")
        print("------------------DELETE STUDENT DATA-------------------")
        print("========================================================")

        print(f"1. Deleting student data..  ")
        print(f"2. Deleting student score data..")
        print(f"3. Back to previous menu..")
        print("========================================================")

        # a function which giving an order to execute which program will run based on choices we made
        Choose_delete= pypi.inputInt("Choose 1-3: ", min=1, max=3, default=1)

        # a function that gave us an option on which program on delete menu interface will be executed
        if Choose_delete == 1:
            print(f"1. Deleting student data..  ")
            delete_student_data()
        elif Choose_delete == 2:
            print(f"2. Deleting student score data..  ")
            delete_student_score_data()
        elif Choose_delete == 3:
            print("3. Back to previous menu..")
            exit = pypi.inputYesNo(prompt="Press 'ENTER' for back to main terminal or (yes/no)", blank=True)
            if exit == "yes" or exit == "":
                clear_screen()
                break
                
                
                
        
