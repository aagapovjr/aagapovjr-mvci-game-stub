import curses

class View:
    def __init__(self, model, interface):
        self.model = model
        self.interface = interface

        # curses screen setup
        self.screen = curses.initscr()
        self.screen.keypad(True)
        curses.noecho()
        curses.curs_set(0)
        curses.cbreak()
 
    def draw(self):
        '''
        updates screen
        '''
        self.screen.clear()
        
        if self.interface.state == 'main':
            self.screen.addstr(3, 3, 'Game state is {0}.'.format(self.model.thing.state))
        elif self.interface.state == 'end_prompt':
            self.screen.addstr(15, 15, 'Are you sure you want to exit? [y/n]')
    
    def close(self):
        '''reverts changes to terminal settings'''
        curses.nocbreak()
        curses.curs_set(1)
        curses.echo()
        self.screen.keypad(False)
