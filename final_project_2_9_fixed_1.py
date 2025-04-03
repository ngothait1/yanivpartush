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

def intPropertyChecker(digit_property_name):
    intValue = input(digit_property_name + ": ")
    while (not intValue.isdigit()):
        print("Error: " + digit_property_name + "  must be a number " + intValue + " is not a number")
        intValue =  input(digit_property_name + ": ")
    return int(intValue)


def saveNewEntry(db,counter):      
    id = intPropertyChecker("ID")
    id_str = str(id)
    if id_str in db:
        print("Error: ID already exists: " + id)
        return 0
    name = input("Name: ")
    age = intPropertyChecker("Age")
    db[id_str] = [name,age]
    persons_map_by_idx[counter] = id_str
    
    print("ID [ " + id_str + " ] saved successfuly")
    return age
        
def printPersonDetails(person):
    print("     Name: " + person[0])
    print("     Age: " + str(person[1]))


def searchById(db):
    id =  input("Please enter the ID you want to look for: ")
    if id not in db:
        print("Error: ID " + id + " is not saved")
        return
    details = db[id]
    print("ID: " + id)
    printPersonDetails(details)


def avgAges(total_ages,db):
    if len(db) > 0:
        return total_ages / len(db)
    else:
        return 0.0

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
        printPersonDetails(person)


def printEntryByIdx(db):
    inputIdx = intPropertyChecker("Index")
    maxIdx = len(db.keys()) - 1
    if maxIdx == -1:
        print("Error: The DB is empty ")
        return
    if inputIdx < 0 or inputIdx > maxIdx:
        print("Error: Index out of range. the max index allowed is " + str(maxIdx))
        return
    print(str(inputIdx) + "." + " " + persons_map_by_idx[inputIdx])
    printPersonDetails(db[persons_map_by_idx[inputIdx]])
    
    
persons = {}
total_ages = 0.0
persons_map_by_idx ={}
personIndex = 0
exitFlag = False
while ( True ):
    userSelection = printMenuAndGetUserSelection()
    if userSelection == "1":
        total_ages = total_ages + saveNewEntry(persons,personIndex)
        personIndex = personIndex + 1
    elif userSelection == "2":
        searchById(persons)
    elif userSelection == "3": 
        print(avgAges(total_ages,persons))  
    elif userSelection == "4": 
        printAllNames(persons)
    elif userSelection == "5": 
        printAllIds(persons)
    elif userSelection == "6": 
        printAllEntries(persons)
    elif userSelection == "7": 
       printEntryByIdx(persons)
    elif userSelection == "8": 
        while ( True ):
            userSelection = input("Are you sure ? (y/n)")
            if userSelection == "y":
                exitFlag = True
                break
            elif userSelection == "n":
                break
        if exitFlag:
            break
    else:
       print("Option [" + userSelection + "] does not exist. Please try again")

print("Goodbye!")