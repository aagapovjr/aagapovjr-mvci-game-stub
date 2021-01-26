from model import Model
from view import View
from controller import Controller
from interface import Interface

model = Model()
interface = Interface()
view = View(model, interface)
controller = Controller(model, view, interface)

model.build()
view.draw()
while interface.state != 'end':
    controller.turn()
view.close()
exit()