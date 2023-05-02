from Controller.DataSaver import *

class App:    
    def __init__(self, _directory):
        self.directory = _directory
        self.dataSaver = DataSaver(_directory)
    
    def startApplication(self):
        self.dataSaver
    
    