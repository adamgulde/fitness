### Really really really simply UI to handle starting and stopping image downloading
from tkinter import *

def start():
    with open('cmds.txt', 'w') as f:
        f.write('start')
def pause():
    with open('cmds.txt', 'w') as f:
        f.write('stop')
def end():
    with open('cmds.txt', 'w') as f:
        f.write('stop')
    quit()

WIDTH = 200
HEIGHT = 100
def create_ui():
    root = Toplevel()
    root.title('FCP')
    root.geometry(newGeometry='200x100')
    root.resizable(False, False)
    t=Label(root, text='Fitness Control Panel')
    # t.pack()
    frame=Frame(root, bd=2, bg='light blue', width=WIDTH, height=HEIGHT)
    frame.place(x=0, y=0)
    Button(frame, text='START image DL', command=start).grid(row=0, column=0)
    Button(frame, text='PAUSE image DL', command=pause).grid(row=0, column=1)
    Button(frame, text='Quit', command=end).grid(row=1, column=0)
    root.mainloop()

if __name__=='__main__':
    create_ui()

# class UI(Toplevel):
#     def __init__(self,master,message):
#         Toplevel.__init__(self,master) #master have to be Toplevel, Tk or subclass of Tk/Toplevel
#         self.title('FCP')
#         self.resizable(False,False)
#         Label(self,text=message).pack(fill=BOTH,expand=True)
#         frame=Frame(self, bd=2, bg='light blue', width=WIDTH, height=HEIGHT)
#         frame.place(x=0, y=0)
#         Button(frame, text='START image DL', command=start).grid(row=0, column=0)
#         Button(frame, text='PAUSE image DL', command=pause).grid(row=0, column=1)
#         Button(frame, text='Quit', command=end).grid(row=1, column=0)
#         self.geometry('200x100')

#     def callback(self): pass