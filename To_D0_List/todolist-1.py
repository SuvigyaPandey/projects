from distutils import command
from textwrap import fill
from tkinter import *
from tkinter import messagebox
from tkinter import font

def newTask():
    task = my_entry.get()
    if task!="":
        lb.insert(END,task)
        my_entry.delete(0,'end')
    else:
        messagebox.showwarning("warning","please enter some task")
def deleteTask():
    lb.delete(ANCHOR)

ws=Tk()
ws.geometry('500x450+500+200')
ws.title('My_To_Do_List')
ws.config(bg='#223430')
ws.resizable(width=False,height=False)
frame=Frame(ws)
frame.pack(pady=10)

#CREATE LISTBOX

lb=Listbox(
    frame,
    width=50,
    height=6,
    font=('Times',18),
    bd=0,
    fg='#555555',
    highlightthickness=0,
    selectbackground='#a6a6a7',
    activestyle="none",
)
lb.pack(side=LEFT,fill=BOTH)

#Adding Dummy DATA

task_list=['study',
    'eat banana'
]

for item in task_list:
    
    lb.insert(END,item)

#add scrollbar

sb=Scrollbar(frame)
sb.pack(side=RIGHT,fill=BOTH)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

#adding entry box

my_entry=Entry(
    ws,
    font=('Times',24)
)
my_entry.pack(pady=20)


#add buttons

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn=Button(
    button_frame,
    text='Add Task',
    font=('Times',14),
    bg='#c5f776',
    padx=20,
    pady=10,
    command = newTask
)
addTask_btn.pack(fill=BOTH,expand=True,side=LEFT)

delTask_btn=Button(
    button_frame,
    text="Delete Task",
    font=('Times',14),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH,expand=True,side=LEFT)
ws.mainloop()
