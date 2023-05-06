from Model.Model import *
from Model.Poop import *
from Model.Person import *

class DataSaver:
    def __init__(self, _directory, _model):
        self.directory = _directory
        self.model = _model

    def importTextFromData(self):
        file = open(self.directory, encoding="utf8")
        lines = file.readlines()
        for index, line in enumerate(lines):
            if index!=1:
                if "💩" in line:               
                    data = line.split(" ") 
                    self.savePoop(data)
                    
        file.close()
        
    def savePoop(self, data):
        
        date = data[0]  
        hour = data[1]
        personName = data[3]
        
        index = self.personIsAlreadyInTheList(personName)
        if(index == -1):
            self.createNewPerson(personName)
            index = len(self.model.peopleList) - 1
            self.addNewPoop(index, date, hour)
        else:
            self.addNewPoop(index, date, hour)

    def createNewPerson(self, personName):
        self.model.peopleList.append(Person(personName))

    def addNewPoop(self, index, date, hour):
        sD = date.split("/")
        sH = hour.split(":")
        self.model.peopleList[index].poopsList.append(Poop(len(self.model.peopleList[index].poopsList) + 1, sD[0], sD[1], sD[2], sH[0], sH[1]))
        
    def personIsAlreadyInTheList(self, personName):
        
        found = False
        position = -1
        index = 0
        for index, element in enumerate(self.model.peopleList):
            if(found == False):
                if(element.name == personName):
                    found = True
                    position = index
        
        return position
