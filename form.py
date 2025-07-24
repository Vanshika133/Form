import tkinter as tk
from tkinter import *

# To create a window or root wigdet
root=Tk()
root.title("Form")

#LABEL 
Name=Label(root,text=' Name :').grid(row=1,column=0)
Father_name=Label(root,text='Father Name : ').grid(row=2,column=0)   
Email=Label(root,text='Email : ').grid(row=3,column=0)
Couser=Label(root,text='Couser : ').grid(row=4,column=0)

#INPUT FIELD
Name=Entry(root,width=10,bg='white')
Name.insert(0,' ')
Father_name=Entry(root,width=10,bg='white')
Father_name.insert(0,' ')
Email=Entry(root,width=10,bg='white')
Email.insert(0,' ')
Courser=Entry(root,width=10,bg='white')
Courser.insert(0,' ')

Name.grid(row=1,column=1,padx=5)
Father_name.grid(row=2,column=1,padx=5)
Email.grid(row=3,column=1,padx=5)
Courser.grid(row=4,column=1,padx=5)
#function
def submit():
    name=Label(root,text=' ' +Name.get())
    father=Label(root,text=' '+Father_name.get())
    email=Label(root,text=' '+Email.get())
    couser=Label(root,text=' '+Courser.get())
    name.grid()
    father.grid()
    email.grid()
    couser.grid()

def reset():
     Name.delete(0,'end')
     Father_name.delete(0,'end')
     Email.delete(0,'end')
     Courser.delete(0,'end')

# create submit and reset button
button=Button(root,text='Submit',command=submit,justify='left')
button1=Button(root,text='reset',command=reset,justify='left')
button.grid(row=5, column=0, pady=10)
button1.grid(row=5, column=1, pady=10)
root.mainloop()