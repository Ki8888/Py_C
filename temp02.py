class Athelete:
    def __init__(self, value='Jane'):
        self.thing=value
    def getAthelete(self):
        return self.thing
        
a=Athelete()
print(a.getAthelete())

b=Athelete('Holy')
Athelete.__init__(a,'Holy')
print(b.getAthelete())
