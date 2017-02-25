from tkinter import *
from PIL import Image, ImageTk 

def commandTest():
    print ("test")

#def makeButtons(sidebar):
    #""" place all the buttons in the sidebar"""
    #TODO add commands for each button

root = Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (screenWidth, screenHeight, 0, 0))

# main area
mainarea = Canvas(root, bg='#FFF', width=screenWidth-200)
mainarea.pack(expand=True, fill='both', side='right')

# sidebar
sidebar = Frame(root, bg='#d8d8d8', width=200)
sidebar.pack(expand=False, fill='both', side='left', anchor='nw')

# make buttons
wnPath = 'WholeNoteicon.png'
wnImage = Image.open(wnPath)
wn = ImageTk.PhotoImage(wnImage)
wnButton = Button(sidebar, image=wn, border=0)
wnButton.place(x=25, y=0)

wnRestPath = 'WholeResticon.png'   
wnRestImage = Image.open(wnRestPath)
wnRest = ImageTk.PhotoImage(wnRestImage)
wnRestButton = Button(sidebar, image=wnRest, border=0)
wnRestButton.place(x=100, y=0)

hnPath = 'HalfNoteicon.png'
hnImage = Image.open(hnPath)
hn = ImageTk.PhotoImage(hnImage)
hnButton = Button(sidebar, image=hn, border=0)
hnButton.place(x=25, y=0)

hnRestPath = 'HalfResticon.png'   
hnRestImage = Image.open(hnRestPath)
hnRest = ImageTk.PhotoImage(hnRestImage)
hnRestButton = Button(sidebar, image=hnRest, border=0)
hnRestButton.place(x=100, y=75)

qnPath = 'QuarterNoteicon.png'
qnImage = Image.open(qnPath)
qn = ImageTk.PhotoImage(qnImage)
qnButton = Button(sidebar, image=qn, border=0)
qnButton.place(x=25, y=75)

qnRestPath = 'QuarterResticon.png'   
qnRestImage = Image.open(qnRestPath)
qnRest = ImageTk.PhotoImage(qnRestImage)
qnRestButton = Button(sidebar, image=qnRest, border=0)
qnRestButton.place(x=100, y=150)

enPath = 'EigthNoteicon.png'
enImage = Image.open(enPath)
en = ImageTk.PhotoImage(enImage)
enButton = Button(sidebar, image=en, border=0)
enButton.place(x=25, y=150)

enRestPath = 'EigthResticon.png'   
enRestImage = Image.open(enRestPath)
enRest = ImageTk.PhotoImage(enRestImage)
enRestButton = Button(sidebar, image=enRest, border=0)
enRestButton.place(x=100, y=150)

snPath = 'SixteenthNoteicon.png'
snImage = Image.open(snPath)
sn = ImageTk.PhotoImage(snImage)
snButton = Button(sidebar, image=sn, border=0)
snButton.place(x=25, y=225)

snRestPath = 'SixteenthResticon.png'   
snRestImage = Image.open(snRestPath)
snRest = ImageTk.PhotoImage(snRestImage)
snRestButton = Button(sidebar, image=snRest, border=0)
snRestButton.place(x=100, y=225)

tnPath = 'ThirtysecondNoteicon.png'
tnImage = Image.open(tnPath)
tn = ImageTk.PhotoImage(tnImage)
tnButton = Button(sidebar,image=tn, border=0)
tnButton.place(x=25, y=300)

tnRestPath = 'ThirtysecondResticon.png'   
tnRestImage = Image.open(tnRestPath)
tnRest = ImageTk.PhotoImage(tnRestImage)
tnRestButton = Button(sidebar, image=tnRest, border=0)
tnRestButton.place(x=100, y=300)

startbpath = ''   
startbImage = Image.open(startpathPath)
startb = ImageTk.PhotoImage(startbImage)
startButton = Button(sidebar, image=startb, border=0)
startButton.place(x=60, y=375)

pausebpath = ''
pausebImage = Image.open(pausebPath)
pauseb = ImageTk.PhotoImage(pausebImage)
pauseButton = Button(sidebar, image=pauseb, border=0)
pauseButton.place(x=60, y=450)

stopbpath = ''   
stopbImage = Image.open(stopbPath)
stopb = ImageTk.PhotoImage(stopbImage)
stopButton = Button(sidebar, image=stopb, border=0)
stopButton.place(x=60, y=525)





if __name__ == '__main__':
    root.mainloop()
