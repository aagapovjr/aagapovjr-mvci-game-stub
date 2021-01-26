class Controller:
    def __init__(self, model, view, interface):
        self.model = model
        self.view = view
        self.interface = interface
    
    def turn(self):            
        
        user_input = self.view.screen.getch()

        if self.interface.state == 'main':
            if user_input == 97: # A
                self.model.decrease()
            elif user_input == 100: # D
                self.model.increase()
            elif user_input == 27: # ESC
                self.interface.state = 'end_prompt'
        
        elif self.interface.state == 'end_prompt':
            if user_input == 121: # Y
                self.interface.state = 'end'
            elif user_input == 110: # N
                self.interface.state = 'main'

        self.view.draw()