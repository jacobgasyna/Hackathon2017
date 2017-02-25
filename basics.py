from Tkinter import *
from PIL import Image, ImageTk 

def commandTest():
    print "test"

def makeButtons(root)
root = Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (screenWidth, screenHeight, 0, 0))

filePath = 'QuarterNoteicon.png'
iconImage = Image.open(filePath)
icon = ImageTk.PhotoImage(iconImage)

# main area
mainarea = Frame(root, bg='#FFA', width=screenWidth-200)
mainarea.pack(expand=True, fill='both', side='right')

# sidebar
sidebar = Frame(root, bg='#FFF', width=200)
sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

testButton = Button(sidebar, image=icon, command=commandTest)
testButton.place(x=25,y=0)

root.mainloop()

