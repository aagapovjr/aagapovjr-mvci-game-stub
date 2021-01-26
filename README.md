# What is this
This is a very basic bit of code which can be expanded upon to build any kind of console application or game in Python. It uses the Curses library as a means to display text and get input.

I built this thing for myself in order to make my game code more readable and extensible, and I thought someone out there could find a use for it as well.

In its current form, this repository implements a "game" with the following rules:
1. You see a number on the screen
1. Pressing A decreases the number
1. Pressing D increases the number
1. Pressing ESC quits the game (with a confirmation prompt)

# How to use
First of all, you need to install the Curses library if you don't have it: https://pypi.org/project/windows-curses/

Now, once you've installed Curses and downloaded the repo, let's take a quick look at what's inside, file by file:

> Note: being familiar with the MVC pattern helps here, since the only real difference here is the addition of the `Interface` class. If you're not familar with MVC, a quick read on that will definitely help - the concept itself is very simple.

1. `object` is a folder containing objects. Objects are business-level items required for the game to make sense. Player character is an object. The goblin the player has to fight is an object. The sword to be used in said fighting is an object. The ground upon which the sword lies is also an object
1. `factory` is a folder containing factories. Factories are classes responsible for creating instances of objects. For example, a `FactoryEnemy` instance would be able to create `Enemy` instances, ready for use by the game. This approach allows the programmer (you) to separate concepts and set up the whole game's state with a set of controlled, easily modified statements like "make me a level", "make me some enemies" and "make me a player character" instead of just hardcoding everything
1. `interface.py` is a class responsible for storing the interface-related data, such as "what screen should the game display right now" or "which item is currently selected in the inventory screen". Strictly speaking, interface isn't a part of the Model, because it doesn't represent hardcore game data. But you can't attribute interface details to View with a straight face either. Creating this class was my answer to this issue. Now I can easily remember what screen do I have to draw, as well as some data required to draw it
1. `model.py` is a class responsible for storing all in-game data such as levels, character health, enemy coordinates, etc. Everything that matters for the game mechanically is a part of Model. In this example, the only property of the Model is an object called Thing
1. `view.py` is a class responsible for drawing stuff on the screen as the Model is getting updated. It does so using the `draw` method. As can be seen in the code, the method is divided into blocks handling various values of the `Interface.state` variable. This is because this variable dictates what "window" or "screen" needs to be displayed. For example, if the player is currently checking out his inventory, the game needs to display a list of items; but if they are fighting a goblin - it needs to draw the goblin. In both cases, the Model remains the same
1. `controller.py` is a class responsible for taking user input and ordering the Model to update itself and the View to reflect the changes on the screen 
1. `main.py` is where the magic happens. It initializes everything and hits the "start" button, launching the input-update-display loop that will only end when the interface's state becomes `end`. You don't need to specifically handle exiting the program - just assign `end` to the `Interface.state` and the program will quit right as it hits the next iteration of the loop

# Making changes
Building a game or a command line tool out of this stub is a matter of adding new components and, if you so choose, maintaining the intended code structure. It's nice to always have a simple structure to rely on; it allows you to keep your head relatively decluttered on all stages of development since there's not a lot to remember at any given moment.

Add new objects whenever there's need for a distinct new entity class in your program. For example, if you're implementing ranged combat - `missile` might be an object you will need.

Add factories if you think those are necessary for a certain purpose. For example, you might need a factory to spawn enemies or loot hoards based on difficulty level.

Add new interface states when there's a new menu or screen in the program. For example, a fancy character screen displaying different stats and abilities warrants a new state, complete with a separate block in the View's `draw` method.

# Working with Curses
Curses is a simple enough module to work with. At its core, it allows getting user input and displaying text at specific coordinates of the screen. This guide covers the Python implementation really well: https://docs.python.org/3/howto/curses.html
