from factory.factory_thing import FactoryThing

class Model:
    def __init__(self):
        self.f_thing = FactoryThing()
    
    def build(self):
        self.thing = self.f_thing.make()
    
    def increase(self):
        self.thing.state += 1
    
    def decrease(self):
        self.thing.state -= 1