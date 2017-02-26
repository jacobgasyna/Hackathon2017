import tkinter
from tkinter import *
from PIL import Image, ImageTk
from time import time

currentNoteIndex = 0
expectedNoteTimes = []

# milisecond window user has to "hit" a note
# length is twice timeRadiusInMili centered around the exact expected time
timeRadiusInMili = 500
checkDelay = 200
startTime = int(round(time() * 1000))

def increment_current_note_index():
    global currentNoteIndex
    if (currentNoteIndex < len(expectedNoteTimes) - 1):
        currentNoteIndex += 1
    else:
        print ("No more notes")

def key_press(event):
    currentTime = int(round(time() * 10000))
    delta = currentTime - expectedNoteTimes[currentNoteIndex]
    if (delta < -timeRadius):
        print ("Rushing!")
    elif (delta > timeRadius):
        print ("Dragging!")
    else:
        print ("You hit it!")

def check():
    currentTime = int(round(time() * 1000))
    delta = abs(currentTime - expectedNoteTimes[currentNodeIndex])
    if(delta > timeRadiusInMili):
        print ("missed")
        increment_current_note_index()
        
root = Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (screenWidth, screenHeight, 0, 0))

# main area
mainarea = Canvas(root, bg='#FFF', width = 1000, height=550)
mainarea.pack(expand=True, fill='both', side='top', anchor='n')
mainarea.create_line(100,370,1150,370,width=1)
mainarea.create_line(100,385,1150,385,width=1)
mainarea.create_line(100,355,1150,355,width=1)
mainarea.create_line(100,340,1150,340,width=1)
mainarea.create_line(100,325,1150,325,width=1)


# sidebar
sidebar = Frame(root, bg='#d8d8d8', width=1000, height=200)
sidebar.pack(expand=False, fill='both', side='bottom')

# button calls

pixelplace=15

def wnbutton():
    global pixelplace
    wnbimage=ImageTk.PhotoImage(file='WholeNoteicon.png')
    label=Label(image=wnbimage)
    label.image= wnbimage
    label.pack
    mainarea.create_image(pixelplace, 370, image=wnbimage)
    pixelplace+=3968

def wnrbutton():
    global pixelplace
    wnrbimage=ImageTk.PhotoImage(file='WholeResticon.png')
    label=Label(image=wnrbimage)
    label.image= wnrbimage
    label.pack
    mainarea.create_image(pixelplace, 370, image=wnrbimage)
    pixelplace+=39

def hnbutton():
    global pixelplace
    hnbimage=ImageTk.PhotoImage(file='HalfNoteicon.png')
    label=Label(image=hnbimage)
    label.image= hnbimage
    label.pack
    mainarea.create_image(pixelplace, 370, image=hnbimage)
    pixelplace+=1920

def hnrbutton():
    global pixelplace
    hnrbimage=ImageTk.PhotoImage(file='HalfResticon.png')
    label=Label(image=hnrbimage)
    label.image= hnrbimage
    label.pack
    mainarea.create_image(pixelplace, 370, image=hnrbimage)
    pixelplace+=39

def qnbutton():
    global pixelplace
    qnbimage=ImageTk.PhotoImage(file='QuarterNoteicon.png')
    label=Label(image=qnbimage)
    label.image= qnbimage
    label.pack
    mainarea.create_image(pixelplace, 370, image=qnbimage)
    pixelplace+=400

def qnrbutton():
    global pixelplace
    qnrbimage=ImageTk.PhotoImage(file='QuarterResticon.png')
    label=Label(image=qnrbimage)
    label.image= qnrbimage
    label.pack
    mainarea.create_image(pixelplace, 370, image=qnrbimage)
    pixelplace+=39

def enbutton():
    global pixelplace
    enbimage=ImageTk.PhotoImage(file='EigthNoteicon.png')
    label=Label(image=enbimage)
    label.image= enbimage
    label.pack
    mainarea.create_image(pixelplace, 370, image=enbimage)
    pixelplace+=200

def enrbutton():
    global pixelplace
    enrbimage=ImageTk.PhotoImage(file='EigthResticon.png')
    label=Label(image=enrbimage)
    label.image= enrbimage
    label.pack
    mainarea.create_image(pixelplace, 370, image=enrbimage)
    pixelplace+=39

def snbutton():
    global pixelplace
    snbimage=ImageTk.PhotoImage(file='SixteenthNoteicon.png')
    label=Label(image=snbimage)
    label.image= snbimage
    label.pack
    mainarea.create_image(pixelplace, 370, image=snbimage)
    pixelplace+=39

def snrbutton():
    global pixelplace
    snrbimage=ImageTk.PhotoImage(file='SixteenthResticon.png')
    label=Label(image=snrbimage)
    label.image= snrbimage
    label.pack
    mainarea.create_image(pixelplace, 370, image=snrbimage)
    pixelplace+=39

def tnbutton():
    global pixelplace
    tnbimage=ImageTk.PhotoImage(file='ThirtysecondNoteicon.png')
    label=Label(image=tnbimage)
    label.image= tnbimage
    label.pack
    mainarea.create_image(pixelplace, 370, image=tnbimage)
    pixelplace+=39

def tnrbutton():
    global pixelplace
    tnrbimage=ImageTk.PhotoImage(file='ThirtysecondResticon.png')
    label=Label(image=tnrbimage)
    label.image= tnrbimage
    label.pack
    mainarea.create_image(pixelplace, 370, image=tnrbimage)
    pixelplace+=39


line=mainarea.create_line(0,0,0,340,tags= 'line')

def animation(x_move, y_move):
    global line
    mainarea.move(line, x_move, y_move)
    mainarea.update()
    mainarea.after(20)

    root.after_idle(animation,x_move, y_move)

def pbutton():
    animation(5,0)
    
    


def delbutton():
    global pixelplace
    mainarea.create_rectangle(0,0,1600,1600,fill='white')
    pixelplace=15
    mainarea.create_line(0,200,screenWidth-200,200,width=3)
    mainarea.create_line(0,540,screenWidth-200,540,width=3)
    
    

    
# make buttons

wnPath = 'WholeNoteicon.png'
wnImage = Image.open(wnPath)
wn = ImageTk.PhotoImage(wnImage)
wnButton = Button(sidebar, image=wn, border=0,command=wnbutton)
wnButton.place(x=75, y=30)

wnRestPath = 'WholeResticon.png'   
wnRestImage = Image.open(wnRestPath)
wnRest = ImageTk.PhotoImage(wnRestImage)
wnRestButton = Button(sidebar, image=wnRest, border=0,command=wnrbutton)
wnRestButton.place(x=75, y=120)

hnPath = 'HalfNoteicon.png'
hnImage = Image.open(hnPath)
hn = ImageTk.PhotoImage(hnImage)
hnButton = Button(sidebar, image=hn, border=0,command=hnbutton)
hnButton.place(x=175, y=30)

hnRestPath = 'HalfResticon.png'   
hnRestImage = Image.open(hnRestPath)
hnRest = ImageTk.PhotoImage(hnRestImage)
hnRestButton = Button(sidebar, image=hnRest, border=0,command=hnrbutton)
hnRestButton.place(x=175, y=120)

qnPath = 'QuarterNoteicon.png'
qnImage = Image.open(qnPath)
qn = ImageTk.PhotoImage(qnImage)
qnButton = Button(sidebar, image=qn, border=0,command=qnbutton)
qnButton.place(x=275, y=30)

qnRestPath = 'QuarterResticon.png'   
qnRestImage = Image.open(qnRestPath)
qnRest = ImageTk.PhotoImage(qnRestImage)
qnRestButton = Button(sidebar, image=qnRest, border=0,command= qnrbutton)
qnRestButton.place(x=275, y=120)

enPath = 'EigthNoteicon.png'
enImage = Image.open(enPath)
en = ImageTk.PhotoImage(enImage)
enButton = Button(sidebar, image=en, border=0,command=enbutton)
enButton.place(x=375, y=30)

enRestPath = 'EigthResticon.png'   
enRestImage = Image.open(enRestPath)
enRest = ImageTk.PhotoImage(enRestImage)
enRestButton = Button(sidebar, image=enRest, border=0,command=enrbutton)
enRestButton.place(x=375, y=120)

snPath = 'SixteenthNoteicon.png'
snImage = Image.open(snPath)
sn = ImageTk.PhotoImage(snImage)
snButton = Button(sidebar, image=sn, border=0,command=snbutton)
snButton.place(x=475, y=30)

snRestPath = 'SixteenthResticon.png'   
snRestImage = Image.open(snRestPath)
snRest = ImageTk.PhotoImage(snRestImage)
snRestButton = Button(sidebar, image=snRest, border=0,command=snrbutton)
snRestButton.place(x=475, y=120)

tnPath = 'ThirtysecondNoteicon.png'
tnImage = Image.open(tnPath)
tn = ImageTk.PhotoImage(tnImage)
tnButton = Button(sidebar,image=tn, border=0,command=tnbutton)
tnButton.place(x=575, y=30)

tnRestPath = 'ThirtysecondResticon.png'   
tnRestImage = Image.open(tnRestPath)
tnRest = ImageTk.PhotoImage(tnRestImage)
tnRestButton = Button(sidebar, image=tnRest, border=0,command=tnrbutton)
tnRestButton.place(x=575, y=120)

startbPath = 'PlayIcon.png'   
startbImage = Image.open(startbPath)
startb = ImageTk.PhotoImage(startbImage)
startButton = Button(sidebar, image=startb, border=0,command=pbutton)
startButton.place(x=1075, y=0)


stopbPath = 'StopIcon.png'   
stopbImage = Image.open(stopbPath)
stopb = ImageTk.PhotoImage(stopbImage)
stopButton = Button(sidebar, image=stopb, border=0)
stopButton.place(x=1050, y=0)

delbPath = 'Trash.png'   
delbImage = Image.open(delbPath)
delb = ImageTk.PhotoImage(delbImage)
delButton = Button(sidebar, image=delb, border=0,command=delbutton)
delButton.place(x=1050, y=100)


if __name__ == '__main__':
    root.after(1000, check)
    root.mainloop()
    
#Button calls and looping
    

    

