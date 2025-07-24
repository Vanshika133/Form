# Form
✅ 1. Importing Libraries
import tkinter as tk
from tkinter import *
tkinter is the standard Python library for creating GUIs.

from tkinter import * imports all Tkinter classes and functions.

✅ 2. Creating the Main Window
root = Tk()
root.title("Form")
Tk() creates the main application window.

root.title("Form") sets the window title to "Form".

✅ 3. Adding Labels
python
Copy
Edit
Name = Label(root, text=' Name :').grid(row=1, column=0)
Father_name = Label(root, text='Father Name : ').grid(row=2, column=0)
Email = Label(root, text='Email : ').grid(row=3, column=0)
Couser = Label(root, text='Couser : ').grid(row=4, column=0)
Label widgets display text in the window.

.grid(row, column) places each label in the specified row and column (like a table layout).

✅ 4. Adding Input Fields

Name = Entry(root, width=10, bg='white')
Name.insert(0, ' ')
Entry() creates a single-line text input box.
width=10 sets its width.
insert(0, ' ') adds a blank space initially.

The same logic applies to Father_name, Email, and Courser fields:
Father_name = Entry(root, width=10, bg='white')
Email = Entry(root, width=10, bg='white')
Courser = Entry(root, width=10, bg='white')

Grid placement for inputs:
Name.grid(row=1, column=1, padx=5)
Father_name.grid(row=2, column=1, padx=5)
Email.grid(row=3, column=1, padx=5)
Courser.grid(row=4, column=1, padx=5)
Inputs are placed next to their respective labels.

✅ 5. Defining Functions
a) submit()
def submit():
    name = Label(root, text=' ' + Name.get())
    father = Label(root, text=' ' + Father_name.get())
    email = Label(root, text=' ' + Email.get())
    couser = Label(root, text=' ' + Courser.get())
    name.grid()
    father.grid()
    email.grid()
    couser.grid()

When Submit is clicked:
It retrieves text from each entry using .get().
Creates new Labels with the entered text and displays them on the screen.

b) reset()
def reset():
    Name.delete(0, 'end')
    Father_name.delete(0, 'end')
    Email.delete(0, 'end')
    Courser.delete(0, 'end')
Clears all input fields by deleting text from position 0 to 'end'.

✅ 6. Adding Buttons
button = Button(root, text='Submit', command=submit, justify='left')
button1 = Button(root, text='reset', command=reset, justify='left')
button.grid(row=5, column=0, pady=10)
button1.grid(row=5, column=1, pady=10)
Submit button calls submit() when clicked.

Reset button calls reset() when clicked.

✅ 7. Start GUI Loop
root.mainloop()
Keeps the application running and responsive.


