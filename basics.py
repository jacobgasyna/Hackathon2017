from Tkinter import *
from PIL import *

def commandTest():
    print "test"

root = Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (screenWidth, screenHeight, 0, 0))

filePath = '~/HackIllinois2017/Hackathon2017/Icons/HalfResticon.png'
iconImage = Image.open(filePath)
icon = PhotoImage(iconImage)

# main area
mainarea = Frame(root, bg='#FFA', width=screenWidth-200)
mainarea.pack(expand=True, fill='both', side='right')

# sidebar
sidebar = Frame(root, bg='#FFF', width=200)
sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

testButton = Button(sidebar, image=icon, command=commandTest)
testButton.place(x=0,y=0)

root.mainloop()

