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