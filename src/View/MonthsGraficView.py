import matplotlib.pyplot as plt
import numpy as np
import random
import datetime

class MonthsGraficView:    
    def __init__(self, _model):
        self.model = _model

    def MonthPoopsGrafic(self):
        
        # set width of bar
        barWidth = 0.15
        fig = plt.subplots(figsize =(10, 4))
        ExistingMonthsData = []
        intMonths = self.MonthsInData()    
        for month in intMonths:
            ExistingMonthsData.append(datetime.date(1900,int(month), 1).strftime('%B'))          
        
        ListOfPeopleWithListOfPopMonthly = []    
        # set height of bar
        for person in self.model.peopleList:
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
            plt.bar(brsum, person, color = self.PersonColor(cont), width=barWidth, edgecolor = 'black' , label = self.model.peopleList[cont].name, zorder=2, linewidth=0.5)
            cont += 1 
                
        # Adding Xticks
        plt.grid(zorder=1)
        plt.title("Nº of poops per month")
        plt.xlabel("Months", fontweight ='bold', fontsize = 15)
        plt.ylabel("Nº of Poops", fontweight ='bold', fontsize = 15)
        plt.xticks([r + barWidth for r in range(len(ListOfPeopleWithListOfPopMonthly[0]))], ExistingMonthsData)
        plt.legend()

    def randonColor(self):
        return ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]

    def PersonColor(self,i):
        #              Yellow, Dark Green, Purple,  Light green, Pink      
        color_list = ['#FFFF00','#228B22','#AB82FF','#CAFF70', '#FF1493']
        return color_list[i]

    def MonthsInData(self):
        intMonths = []
        
        for pop in self.model.peopleList[0].poopsList:
            if pop.month not in intMonths:
                intMonths.append(pop.month)
        
        return intMonths
