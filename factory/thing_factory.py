from object.thing import Thing

class ThingFactory:
    def __init__(self):
        pass
    
    def make(self):
        return Thing(123)