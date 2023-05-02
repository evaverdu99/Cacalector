import matplotlib.pyplot as plt
import numpy as np
import datetime 
from tkinter import *
from tkinter import filedialog

import random

peopleList = []
 
class Person:    
    def __init__(self, name):
        self.name = name
        self.PoopsList = []

    def __str__(self):
        return f"{self.name}"
    
    def poopsInAMonth(self, monthToSearch):
        count = 0
        for pop in self.PoopsList:
            if pop.month == monthToSearch:
                count += 1
        return count

class Poop:
    def __init__(self, num: int, month, day, year, hour, minute):
        self.num = num
        self.month = month
        self.day = day
        self.year = year
        self.hour = hour
        self.minute = minute

    def __str__(self):
        return f"Mi caca número {self.num} se realizó el día {self.day}/{self.month}/{self.year} a las {self.hour}:{self.minute}"

def randonColor():
    return ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
 
def importTextFromData():
     
    root = Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(title="Open the export chat to analise", filetypes=(("text    files","*.txt"), ("all files","*.*")))
  
    file = open(file_path, encoding="utf8")
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

def printAllData():
    global peopleList
    for person in peopleList:
        for poop in person.PoopsList:
            print(person)
            print(poop)      

def showTotalGrafic():
    global peopleList
    
    peopleData = []
    poopsTotalData = []
    for person in peopleList:
        peopleData.append(person.name)
        poopsTotalData.append(len(person.PoopsList))
    
    fig = plt.figure(figsize = (4, 4))
    
    # creating the bar plot
    plt.bar(peopleData, poopsTotalData, color ='green',
            width = 0.5)
    
    plt.ylabel("No. de cacas")
    plt.title("Numero total de cacas por persona")
    plt.show()

def TotalPoopsGrafic():
    global peopleList
    
    namesData = []
    poopsTotalData = []
    for person in peopleList:
        namesData.append(person.name)
        poopsTotalData.append(len(person.PoopsList))
    
    showOneBarGrafic(namesData, poopsTotalData, "No. de cacas","Numero total de cacas por persona")

def MonthsInData():
    global peopleList
    intMonths = []
    stringMonths = []
    
    for pop in peopleList[0].PoopsList:
        if pop.month not in intMonths:
            intMonths.append(pop.month)
    
    return intMonths

def MonthPoopsGrafic():
    global peopleList
    
    
    # set width of bar
    barWidth = 0.15
    fig = plt.subplots(figsize =(10, 4))
    ExistingMonthsData = []
    intMonths = MonthsInData()    
    for month in intMonths:
        ExistingMonthsData.append(datetime.date(1900,int(month), 1).strftime('%B'))          
       
    ListOfPeopleWithListOfPopMonthly = []    
    # set height of bar
    for person in peopleList:
        listOfPopMonthly = []
        for month in intMonths:
            cont = person.poopsInAMonth(month)
            listOfPopMonthly.append(cont)
        ListOfPeopleWithListOfPopMonthly.append(listOfPopMonthly)   
        
        
  
    
    cont = 0
    for person in ListOfPeopleWithListOfPopMonthly:
        if cont == 0:
            brsum = np.arange(len(ListOfPeopleWithListOfPopMonthly[0]))
        else:
            brsum = [x + barWidth for x in brsum] 
        plt.bar(brsum, person, color = randonColor(), width=barWidth, edgecolor = 'grey' , label = peopleList[cont].name)
        cont += 1 
            
    # Adding Xticks
    plt.title("No. de cacas por meses")
    plt.xlabel("Meses", fontweight ='bold', fontsize = 15)
    plt.ylabel("No. de cacas", fontweight ='bold', fontsize = 15)
    plt.xticks([r + barWidth for r in range(len(ListOfPeopleWithListOfPopMonthly[0]))], ExistingMonthsData)
    plt.legend()

def notes():
    IT = [12, 30, 1, 8]
    ECE = [28, 6, 16, 5]
    CSE = [29, 3, 24, 25]
    
    barWidth = 0.25   # Set position of bar on X axis
    br1 = np.arange(len(IT))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    
    # Make the plot
    plt.bar(br1, IT, color ='r', width = barWidth,
            edgecolor ='grey', label ='IT')
    plt.bar(br2, ECE, color ='g', width = barWidth,
            edgecolor ='grey', label ='ECE')
    plt.bar(br3, CSE, color ='b', width = barWidth,
            edgecolor ='grey', label ='CSE')   
    
def showOneBarGrafic(names, data, textylabel, title):
    fig = plt.figure(figsize = (6, 4))
    
    # creating the bar plot
    plt.barh(names, data, color ='green')
    
    for index, value in enumerate(data):
        plt.text(value, index,str(value))
 
    plt.ylabel(textylabel)
    plt.title(title)
    
  
def main(): 
    #month = datetime.date(1900, monthtoconvert, 1).strftime('%B') 

    importTextFromData()
    TotalPoopsGrafic()
    MonthPoopsGrafic()
    
    plt.show()
    
    print("end")
    

if __name__ == "__main__":
    main()