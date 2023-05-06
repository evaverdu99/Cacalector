import matplotlib.pyplot as plt

class OneGraficView:    
    def __init__(self, _model):
        self.model = _model
    
    def TotalPoopsGrafic(self):   
        namesData = []
        poopsTotalData = []
        for person in self.model.peopleList:
            namesData.append(person.name)
            poopsTotalData.append(len(person.poopsList))
        
        self.showOneBarGrafic(namesData, poopsTotalData, "Nº of Poops","Total number of poops per person")
    
    def showOneBarGrafic(self, names, data, textylabel, title):
        fig = plt.figure(figsize = (6, 4))
        
        # creating the bar plot
        plt.barh(names, data, color ='green')
        
        for index, value in enumerate(data):
            plt.text(value, index,str(value))
    
        plt.ylabel(textylabel)
        plt.title(title)
