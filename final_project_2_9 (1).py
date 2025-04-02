def printMenuAndGetUserSelection():
    print("1. Save a new Entry")
    print("2. Search by ID")
    print("3. Print ages avg")
    print("4. Print all names")
    print("5. Print all IDs")
    print("6. Print all entries")
    print("7. Print entry by index")
    print("8. Exit")
    userSelection = input("Please enter your choice : ")
    return userSelection

def saveNewEntry(db):      
        id =  input("ID: ")
        if id.isdigit():
            if (id in db.keys()):
                 print("Error: ID already exists: " + id)
            else:
                name = input("Name: ")
                age = int(input("Age: "))
                db[id] = [name,age]
                print("ID [ " + id + " ] saved successfuly")       
        else:
             print("Error: ID must be a number " + id + " is not a number")
           

def searchById(db):
    id =  input("Please enter the ID you want to look for: ")
    if (id not in db.keys()):
        print("Error: ID " + id + " is not saved")
    else:
        details = db[id]
        print("ID: " + id)
        print("Name: " + details[0])
        print("Age: " + str(details[1]))


def avgAges(db):
    sum = 0.0
    if (len(db) > 0):
        for value in db.values():
            sum = sum + value[1]
        return (sum / len(db))
    else:
        return 0

def printAllNames(db):
    for index, value in enumerate(db.values()):
        print(str(index) + "." + " " + value[0])

def printAllIds(db):
    for index, value in enumerate(db.keys()):
        print(str(index) + "." + " " + value)

def printAllEntries(db):
    for index, idxValue in enumerate(db.keys()):
        print(str(index) + "." + " " + idxValue)   
        person = db[idxValue]
        print("     Name: " + person[0])
        print("     Age: " + str(person[1]))

def printEntryByIndex(db,indexToCheck):
    for index, idxValue in enumerate(db.keys()):
                if (indexToCheck == index):
                    print(str(index) + "." + " " + idxValue)   
                    person = db[idxValue]
                    print("     Name: " + person[0])
                    print("     Age: " + str(person[1]))


def printEntryByIdx(db):
    inputIdx = input("Please enter the index of the entry you want to print: ")
    if inputIdx.isdigit():
        maxIdx = len(db.keys()) - 1
        numericInputIdx = int(inputIdx)
        if (maxIdx == -1):
            print("Error: The DB is empty ")
        elif ( numericInputIdx < 0 or numericInputIdx > maxIdx):
            print("Error: Index out of range. the max index allowed is " + str(maxIdx))
        else:
            printEntryByIndex(db,numericInputIdx)
    else:
        print("Error: ID must be a number " + inputIdx + " is not a number")



persons = {}

userSelection = printMenuAndGetUserSelection()
while (userSelection != "y" ):
    if userSelection == "1" :
        saveNewEntry(persons)
    elif userSelection == "2" :
        searchById(persons)
    elif userSelection == "3" : 
        print(avgAges(persons))  
    elif userSelection == "4" : 
        printAllNames(persons)
    elif userSelection == "5" : 
        printAllIds(persons)
    elif userSelection == "6" : 
        printAllEntries(persons)
    elif userSelection == "7" : 
       printEntryByIdx(persons)
    elif userSelection == "8" : 
         userSelection = input("Are you sure ? (y/n)") 
         while ( userSelection != "y" and userSelection != "n"):
             userSelection = input("Are you sure ? (y/n)") 
         if (userSelection == "y"):
            print("Goodbye!")
    else:
       print("Option [" + userSelection + "] does not exist. Please try again") 
    if (userSelection != "y"):
        userSelection = printMenuAndGetUserSelection()   
     
    