# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# <Tasean Cunningham>,<11/13/2020>,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = ""   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open("ToDoList.txt", "r")
for row in objFile:
    strData = row.split(",")
    dicRow = {"Task": strData[0], "Priority": strData[1].strip()}
    lstTable.append(dicRow)
objFile.close

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("The Current Data Is: \n")
        for row in lstTable:
            print(row["Task"] + "," + row["Priority"])
        continue
    # Step 4 - Add a new item to the list/Table
    #promt the user to enter two values
    #values from the user will be added to the lsttable
    #appended to lsttable
    elif (strChoice.strip() == '2'):
        newTask = input("What new task would you like to add: ")
        newPriority = input("What new priority would you like to add: ")
        dicRow = {"Task": newTask, "Priority": newPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strDelete = input("What task or priority would you like to be deleted?: ")
        for row in lstTable:
            if strDelete in row["Task"]:
                lstTable.remove(row)
                if strDelete in row["Priority"]:
                    lstTable.remove(row)
                if strDelete not in lstTable:
                    print("Insert a new task or priority, task not found on table")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        print("Are you ready to save your data?")
        saveData = input("Enter 'Yes' or 'No': ")
        if saveData == "Yes":
            objFile = open("ToDoList.txt", "w")
        for row in lstTable:
            objFile.write(row["Task"] + "," + row["Priority"] + "\n")
        objFile.close()
        print("Your Data has been saved to the File")
    elif saveData == "No":
        print("Your Data Has Not Been Saved")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        userDone = input("Please press 'enter' to exit the program")
        break  # and Exit the program
