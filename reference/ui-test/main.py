from tkinter import *
import screeninfo
screen_width, screen_height = 0, 0
for monitor in screeninfo.get_monitors():
    screen_width = monitor.width
    screen_height = monitor.height
    break
def run():
    window = Tk()
    window.geometry(f'{int(screen_width/2)}x{int(screen_height/2)}')
    window.title('Main')
    
    left_side(window)
    right_top(window)
    right_bottom(window)

    window.mainloop()


def left_side(win:Tk):
    l_frame=Frame(win, bd=2, bg='coral4', cursor='star', width=screen_width/4, height=screen_height/2)
    l_frame.pack(side=LEFT)
    l_button=Button(l_frame, text='Quit', activeforeground='blue violet', command=quit)
    l_button.place(x=0, y=screen_height/4)

def right_top(win:Tk):
    canvas=Canvas(win, width=screen_width/4, height=screen_height/4)
    canvas.configure(bg='light blue')
    canvas.create_text(25, 10, text='CANVAS')
    canvas.create_text(86, 23, text=f'Canvas Dimensions: {screen_width/4}, {screen_height/4}')
    canvas.create_text(86, 36, text=f'Mouse Coords: {canvas.winfo_pointerxy()}')
    canvas.place(x=screen_width/4, y=0)
    win.after(50, right_top, win)

def right_bottom(win:Tk):
    r_frame=Frame(win, bg='blanched almond', cursor='heart', width=screen_width/4, height=screen_height/4)
    r_frame.place(x=screen_width/4, y=screen_height/4)

    r_button1=Button(r_frame, bg='burlywood', text='Button 1')
    r_button1.grid(column=0, row=0)
    r_button1=Button(r_frame, bg='burlywood', text='Button 2')
    r_button1.grid(column=1, row=0)

if __name__=='__main__':
    run()