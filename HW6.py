"""
HW6
William Gao
Section A04
GT ID: 903250681
wgao.63@gatech.edu

Collaboration statement: I did not collaborate on this with any persons and
used materials only from this course and python api.
"""
#helper functions
def countOpenBrackets(string):
    opBracket = []
    for i in range(len(string)):
        if string[i] == "[":
            opBracket.append(i)
    return opBracket

def countCloseBrackets(string):
    closeBracket = []
    for i in range(len(string)):
        if string[i] == "]":
            closeBracket.append(i)
    return closeBracket

#Actual Functions

def getDict(file):
    aDict = {}
    aFile = open(file, "r")
    lines = aFile.readlines() #this gets us all the lines
    #first let's store the names correctly in the dictionary
    for item in lines:
        if item != "\n":
            loc1 = item.index(",")
            loc2 = item.index(":")
            lastName = (item[:loc1]).strip()
            firstName = (item[loc1+1:loc2]).strip()
            correctName = firstName+" "+lastName
            aDict[correctName] = []
    names = aDict.keys()
    #names have been stored correctly
    #lines has all the lines
    #now we have to store stuff
    for item in lines:
        if item != "\n":
            opBracket = countOpenBrackets(item)
            closeBracket = countCloseBrackets(item)
            recurrence = len(closeBracket)
            loc1 = item.index(",")
            loc2 = item.index(":")
            lastName = (item[:loc1]).strip()
            firstName = (item[loc1+1:loc2]).strip()
            correctName = firstName+" "+lastName
            for i in range(recurrence): #runs # of times there is a string
                oloc = opBracket[i]
                cloc = closeBracket[i]
                wholeEntryAsString = item[oloc+1:cloc]
                entries = wholeEntryAsString.split(",")
                entries[1] = int(entries[1])
                entries[2] = int(entries[2])
                aDict[correctName].append(entries)
                #print(entries)
                    
    return aDict

##student = "rachel Golding"
def calcGPA(student, aDict):
    if len(aDict) == 0: #dict empty
        return 0.0
    else:
        try:
            if len(aDict[student]) == 0: #no classes
                return 0.0
            else:
                totalCreditHours = 0
                totalCredits = 0
                workList = aDict[student] #worklist is a list of lists
                L = len(workList)
                for i in range(L):
                    grade = workList[i][1]
                    if grade >= 90:
                        grade = 4
                    elif (grade >= 80):
                        grade = 3
                    elif grade >= 70:
                        grade = 2
                    elif grade >= 60:
                        grade = 1
                    else:
                        grade = 0
                    creditHours = workList[i][2]
                    totalCreditHours = totalCreditHours + creditHours
                    credit = creditHours * grade
                    totalCredits = totalCredits + credit
                gpa = round(totalCredits/totalCreditHours, 2)
                return gpa
        except: #not in dictionary
            return 0.0
##file = "text_original.txt"
##aDict = getDict(file)
##outputFile = "out.txt"
##classList = ["CS1301", "CS101", "CS", "Establishing the Proletarian Dictatorship", "CS9999", "CS1332"]
def newFile(classList, aDict, outputFile):
    newF = open(outputFile, "w")
    
    studentNames = aDict.keys()
    for className in classList:
        newF.write(className+":")
        listOfPeople = []
        for name in studentNames:
            L = len(aDict[name])
            
            for i in range(L):
                if className == aDict[name][i][0]:
                    listOfPeople.append(name)
        string = ""
        try:
            L = len(listOfPeople)
            for name in listOfPeople:
                if listOfPeople.index(name) != L-1:
                    name = name+","
                string = string + name
            newF.write(string+"\n")
        except:
            newF.write(string+"\n")
    newF.close()

    
    

                                
