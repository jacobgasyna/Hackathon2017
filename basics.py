from Tkinter import *
from PIL import Image, ImageTk 

def commandTest():
    print "test"

#def makeButtons(sidebar):
    #""" place all the buttons in the sidebar"""
    #TODO add commands for each button

root = Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (screenWidth, screenHeight, 0, 0))

# main area
mainarea = Frame(root, bg='#FFA', width=screenWidth-200)
mainarea.pack(expand=True, fill='both', side='right')

# sidebar
sidebar = Frame(root, bg='#FFF', width=200)
sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

# make buttons
qnPath = 'QuarterNoteicon.png'
qnImage = Image.open(qnPath)
qn = ImageTk.PhotoImage(qnImage)
qnButton = Button(sidebar, image=qn, border=0)
qnButton.place(x=25, y=0)


qnRestPath = 'QuarterResticon.png'   
qnRestImage = Image.open(qnRestPath)
qnRest = ImageTk.PhotoImage(qnRestImage)
qnRestButton = Button(sidebar, image=qnRest, border=0)
qnRestButton.place(x=100, y=0)

wnPath = 'WholeNoteicon.png'
wnImage = Image.open(wnPath)
wn = ImageTk.PhotoImage(wnImage)
wnButton = Button(sidebar, image=wn, border=0)
wnButton.place(x=25, y=75)


wnRestPath = 'WholeResticon.png'   
wnRestImage = Image.open(wnRestPath)
wnRest = ImageTk.PhotoImage(wnRestImage)
wnRestButton = Button(sidebar, image=wnRest, border=0)
wnRestButton.place(x=100, y=75)

root.mainloop()
