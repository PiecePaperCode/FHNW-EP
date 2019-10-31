from tkinter import *
from tkinter import messagebox
from functools import partial
from Filehandler import write_Basisroutine, read_Basisroutine


# Messagebox with custom Message text
def msgbox(text):
    messagebox.showinfo('message', text)


# Messagebox that is created with the read_Basisroutine as text
def routine_box():
    msgbox(read_Basisroutine())


# Create a buttons that will print out corresponding routine execute corresponding functions
def create_button(window, name, function, row):
    Button(window,
           text=name,
           width='30',
           height='2',
           command=function).grid(row=row, column=0, pady=1)


# +1 Texteditor window function
def Tk_Texteditor():
    editor = Tk()
    editor.geometry('440x420')
    editor.wm_title('Morgenroutine')
    editor.config(background='#FFFFFF')
    entry = Text(editor, height=21)
    entry.grid(row=0)
    entry.insert(END, read_Basisroutine())
    create_button(editor, 'Save', lambda: write_Basisroutine(entry.get('1.0', 'end-1c')), 1)
    editor.mainloop()


# Create Window and configure it
window = Tk()
window.geometry('220x480')
window.wm_title('Morgenroutine')
window.config(background='#FFFFFF')

# Dictionary with Button Name and command(function)
buttons = {'Button1': partial(msgbox, 'Hi i am a Button1 text'),
           'Button2': partial(msgbox, 'Hi i am a Button2 text'),
           'Monday': routine_box,
           'Tuesday': routine_box,
           'Wednesday': routine_box,
           'Thursday': routine_box,
           'Friday': routine_box,
           'Saturday': partial(msgbox, 'Am Samstag wird gechillt'),
           'Sunday': partial(msgbox, 'Am Sonntag wird Netflix geschaut'),
           'Edit Morgenroutine': Tk_Texteditor,
           'Exit': exit}

# Loop for creating Buttons
for row, (name, function) in enumerate(buttons.items()):
    create_button(window, name, function, row)

# Main Loop
window.mainloop()
