from Controller.DataSaver import *
from View.OneGraficView import *
from View.MonthsGraficView import *
import matplotlib.pyplot as plt

class App:    
    def __init__(self, _directory):
        self.directory = _directory
        self.dataSaver = DataSaver(_directory, Model())
    
    def startApplication(self):
        self.dataSaver.importTextFromData()
        oneGrafficView = OneGraficView(self.dataSaver.model)
        oneGrafficView.TotalPoopsGrafic()
        monthsGraficView = MonthsGraficView(self.dataSaver.model)
        monthsGraficView.MonthPoopsGrafic()
        
        plt.show()
        
    
    