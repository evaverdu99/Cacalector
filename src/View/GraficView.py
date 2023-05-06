import random

class GraficView:
    def randonColor(self):
        return ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
