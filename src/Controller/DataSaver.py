from Model.Person import *
from Model.Poop import *

class DataSaver:
    def __init__(self, _directory):
        self.directory = _directory

def importTextFromData():
    file = open('data.txt', encoding="utf8")
    lines = file.readlines()
    for index, line in enumerate(lines):
        if index!=1:
            if "💩" in line:               
                data = line.split(" ") 
                savePoop(data)
                
    file.close()
    
def savePoop(data):
    global peopleList
    
    date = data[0]  
    hour = data[1]
    personName = data[3]
    
    index = personIsAlreadyInTheList(personName)
    if(index == -1):
        createNewPerson(personName)
        index = len(peopleList) - 1
        addNewPoop(index, date, hour)
    else:
        addNewPoop(index, date, hour)

def createNewPerson(personName):
    global peopleList
    peopleList.append(Person(personName))

def addNewPoop(index, date, hour):
    global peopleList
    sD = date.split("/")
    sH = hour.split(":")
    peopleList[index].PoopsList.append(Poop(len(peopleList[index].PoopsList) + 1, sD[0], sD[1], sD[2], sH[0], sH[1]))
    
def personIsAlreadyInTheList(personName):
    
    global peopleList
    found = False
    position = -1
    index = 0
    for index, element in enumerate(peopleList):
        if(found == False):
            if(element.name == personName):
                found = True
                position = index
    
    return position
