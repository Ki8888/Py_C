class add1:
    def __init__(self, x=0):
        self.x = x
    def getPredict(self,x):
        y = x * 2
        print('y=',y)    


class add3:
    def __init__(self, x1=0, x2=0):
        self.x1 = x1
        self.x2 = x2
    def getPredict3(self,x1,x2):
        y = x1 * x2
        print('y3=',y) 
