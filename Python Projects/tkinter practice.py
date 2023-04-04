from tkinter import *
from PIL import Image, ImageTk
"""
root = Tk()

root.geometry("800x450")

# photo = PhotoImage(file="qr1.png")
image = Image.open("coding wallpaper.jpg")
photo = ImageTk.PhotoImage(image)
l1 = Label(image=photo)
l1.pack()

shakib = Label(text="Shakib is a good boy and this is his GUI")
shakib.pack()

root.mainloop()
"""
#######################################################################################
"""
#Attributies & Widgets
root = Tk()
root.geometry("555x333")
root.title("My GUI With Darshan")
# Important Label Content
# text - add he text
# bd - background
# fg -foreground
# font - sets the fontToolspad
# x - x padding
# y - y padding
# relif - border styling - SUNKEN, RAISED, GROOVE, RIDGE
title_label = Label(text='''The hartebeest (Alcelaphus buselaphus) is a large African antelope. Standing 
                         just over 1 m (3.3 ft) at the shoulder, it has a typical head-and-body length 
                         of 200 to 250 cm (80 to 90 in) and weighs 100 to 200 kg (220 to 440 lb). 
                         Coat colour varies among the eight subspecies, from the sandy brown of the 
                         western hartebeest to the chocolate brown of Swayne's hartebeest.
                         Both sexes have an elongated forehead, back-curving horns, a short neck, pointed 
                         ears, and unusually long legs. Herds typically have up to 300.''',bg="aqua",
                      foreground="red",padx=10,pady=50,font=("comicsansms",19,"bold"),borderwidth=13,relief=SUNKEN
                    )
title_label.pack(side=LEFT,anchor="ne",fill=Y,pady=34)


root.mainloop()
"""
#######################################################################################
"""
#Frames
root = Tk()
root.geometry("565x333")
f1 = Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root,borderwidth=8,bg="grey", relief=SUNKEN)
f2.pack(side=TOP,fill="x")

l = Label(f1,text="project tkinter- pycharm")
l.pack(pady=42)

l = Label(f2,text="Welcome to sublime text", font="Helvetica 16 bold",fg="red")
l.pack()

root.mainloop()
"""
#######################################################################################
"""

#Buttons
root = Tk()
root.geometry("655x333")
def hello():
    print("Hello tkinter buttons")

def name():
    print("My name is darshan")
frame = Frame(root,borderwidth=6,bg="grey",relief=SUNKEN)
frame.pack(side=LEFT, anchor="nw")

b1 = Button(frame,fg='red',text="Print now",command=hello)
b1.pack(side=LEFT)

b2 = Button(frame,fg='red',text="Tell me name",command=name)
b2.pack(side=LEFT,padx=23)

b3 = Button(frame,fg='red',text="Print now")
b3.pack(side=LEFT,padx=23)

b4 = Button(frame,fg='red',text="Print now")
b4.pack(side=LEFT)

root.mainloop()
"""
""" """
# Grid layouts and entry widgets
root = Tk()
root.geometry("655x333")
user = Label(root,text="Username")
password = Label(root, text="password")
user.pack()

root.mainloop()
