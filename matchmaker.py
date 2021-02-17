# importing modules
import random
import time
from tkinter import Tk , Button , DISABLED


# Function to display Icons
def show_symbol(x,y):
    global first
    global previousx , previousy
    buttons[x,y]['text'] = button_symbols[x,y]        # accessing the text on button
    buttons[x,y].update_idletasks()

    if first:
        previousx = x
        previousy = y
        first = False
    elif previousx != x or previousy != y:
        if buttons[previousx,previousy]['text'] != buttons[x,y]['text']:
            time.sleep(0.5)
            buttons[previousx,previousy]['text'] = ' '
            buttons[x,y]['text'] = ' '
        else:
            buttons[previousx,previousy]['command'] = DISABLED
            buttons[x,y]['command'] = DISABLED
        first = True

# Create main window
win = Tk()
# Set window title and icon
win.title('Matchmaker')
 # to fix the size of window
win.resizable(width=False , height=False)    

# Variables
first = True
previousx = 0
previousy = 0
buttons = { }
button_symbols = { }

# Matchmaker Symbols
symbols = [u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
            u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728',
            u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
            u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728']

# To shuffle the symbols
random.shuffle(symbols)

for x in range(6):
    for y in range(4):
        button = Button(command = lambda x=x , y=y: show_symbol(x,y) , width = 12, height = 8)
        button.grid(column = x , row = y)
        buttons[x,y] = button
        button_symbols[x,y] = symbols.pop()

win.mainloop()
