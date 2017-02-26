from tkinter import *
from PIL import Image, ImageTk
from time import time

initial = 445
currentNoteIndex = 0
expectedNoteTimes = [initial]

# milisecond window user has to "hit" a note
# length is twice timeRadiusInMili centered around the exact expected time
timeRadiusInMili = 90
checkDelay = 100
performCheck = False

# the duration of a 32nd note in miliseconds given a tempo
duration32InMili = 185

def increment_current_note_index():
    global currentNoteIndex
    if (currentNoteIndex < len(expectedNoteTimes) - 1):
        currentNoteIndex += 1
    else:
        #print ("No more notes")
        performCheck = False

def key_press(event):
    global currentNoteIndex
    global startTime
    currentTime = int(round(time() * 1000)) - startTime
    expectedTime = expectedNoteTimes[currentNoteIndex]
    delta = currentTime - expectedTime
    currentTime
    if (delta < -timeRadiusInMili):
        print ("Rushing!")
    elif (delta > timeRadiusInMili):
        print ("Dragging!")
    else:
        print ("You hit it!")
    print("now: ", currentTime, " - expected: ", expectedTime)

def check():
    global currentNoteIndex
    currentTime = int(round(time() * 1000)) - startTime
    delta = currentTime - expectedNoteTimes[currentNoteIndex]
    if(delta > timeRadiusInMili):
        #print ("missed")
        increment_current_note_index()
    if performCheck:
        root.after(checkDelay, check)

def add_note_time(noteType, isRest):
    lastIndex = len(expectedNoteTimes) - 1
    lastTime = expectedNoteTimes[lastIndex]
    nextNoteTime = lastTime + (noteType * duration32InMili)
    # if the thing we're adding is a rest, we don't add another time but replace the last
    # that's because if we added another index, the user would be expected to "hit" a rest
    if (isRest):
        expectedNoteTimes[lastIndex] = nextNoteTime
    else:
        expectedNoteTimes.append(nextNoteTime)
        


root = Tk()
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (screenWidth, screenHeight, 0, 0))

# main area
mainarea = Canvas(root, bg='#FFF', width = 1000, height=550)
mainarea.pack(expand=True, fill='both', side='top', anchor='n')
mainarea.create_line(100,370,1350,370,width=1)
mainarea.create_line(100,385,1350,385,width=1)
mainarea.create_line(100,355,1350,355,width=1)
mainarea.create_line(100,340,1350,340,width=1)
mainarea.create_line(100,325,1350,325,width=1)
logoimage=ImageTk.PhotoImage(file='Logo.png')
label=Label(image=logoimage)
label.image= logoimage
label.pack
mainarea.create_image(1100, 150, image=logoimage)



# sidebar
sidebar = Frame(root, bg='#d8d8d8', width=1000, height=200)
sidebar.pack(expand=False, fill='both', side='bottom')

# button calls

pixelplace=110
counter=0

def wnbutton():
    global pixelplace
    global counter
    if counter+32<33:
        wnbimage=ImageTk.PhotoImage(file='WholeNoteicon.png')
        label=Label(image=wnbimage)
        label.image= wnbimage
        label.pack
        mainarea.create_image(pixelplace, 355, image=wnbimage)
        pixelplace+=1650
        counter+=32
        add_note_time(32, False)
    else:
        print("too many notes")
        
def wnrbutton():
    global counter
    global pixelplace
    if counter+32<33:
        wnrbimage=ImageTk.PhotoImage(file='WholeResticon.png')
        label=Label(image=wnrbimage)
        label.image= wnrbimage
        label.pack
        mainarea.create_image(pixelplace, 355, image=wnrbimage)
        pixelplace+=1650
        counter+=32
        add_note_time(32, True)
    else:
        print("too many notes")

def hnbutton():
    global pixelplace
    global counter
    if counter+16<33:
        hnbimage=ImageTk.PhotoImage(file='HalfNoteicon.png')
        label=Label(image=hnbimage)
        label.image= hnbimage
        label.pack
        mainarea.create_image(pixelplace, 340, image=hnbimage)
        pixelplace+=550
        counter+=16
        add_note_time(16, False)
    else:
        print("too many notes")

def hnrbutton():
    global pixelplace
    global counter
    if counter+16<33:
        hnrbimage=ImageTk.PhotoImage(file='HalfResticon.png')
        label=Label(image=hnrbimage)
        label.image= hnrbimage
        label.pack
        mainarea.create_image(pixelplace, 355, image=hnrbimage)
        pixelplace+=550
        counter+=16
        add_note_time(16, True)
    else:
        print("too many notes")

def qnbutton():
    global pixelplace
    global counter
    if counter+8<33:
        qnbimage=ImageTk.PhotoImage(file='QuarterNoteicon.png')
        label=Label(image=qnbimage)
        label.image= qnbimage
        label.pack
        mainarea.create_image(pixelplace, 340, image=qnbimage)
        pixelplace+=337
        counter+=8
        add_note_time(8, False)
    else:
        print("too many notes")
    

def qnrbutton():
    global pixelplace
    global counter
    if counter+8<33:
        qnrbimage=ImageTk.PhotoImage(file='QuarterResticon.png')
        label=Label(image=qnrbimage)
        label.image= qnrbimage
        label.pack
        mainarea.create_image(pixelplace, 355, image=qnrbimage)
        pixelplace+=337
        counter+=8
        add_note_time(8, True)
    else:
        print("too many notes")

def enbutton():
    global pixelplace
    global counter
    if counter+4<33:
        enbimage=ImageTk.PhotoImage(file='EigthNoteicon.png')
        label=Label(image=enbimage)
        label.image= enbimage
        label.pack
        mainarea.create_image(pixelplace, 340, image=enbimage)
        pixelplace+=147
        counter+=4
        add_note_time(4, False)
    else:
        print("too many notes")


def enrbutton():
    global pixelplace
    global counter
    if counter+4<33:
        enrbimage=ImageTk.PhotoImage(file='EigthResticon.png')
        label=Label(image=enrbimage)
        label.image= enrbimage
        label.pack
        mainarea.create_image(pixelplace, 373, image=enrbimage)
        pixelplace+=147
        counter+=4
        add_note_time(4, True)
    else:
        print("too many notes")

def snbutton():
    global pixelplace
    global counter
    if counter+2<33:
        snbimage=ImageTk.PhotoImage(file='SixteenthNoteicon.png')
        label=Label(image=snbimage)
        label.image= snbimage
        label.pack
        mainarea.create_image(pixelplace, 340, image=snbimage)
        pixelplace+=68
        counter+=2
        add_note_time(2, False)
    else:
        print("too many notes")

def snrbutton():
    global pixelplace
    global counter
    if counter+2<33:
        snrbimage=ImageTk.PhotoImage(file='SixteenthResticon.png')
        label=Label(image=snrbimage)
        label.image= snrbimage
        label.pack
        mainarea.create_image(pixelplace, 373, image=snrbimage)
        pixelplace+=68
        counter+=2
        add_note_time(2, True)
    else:
        print("too many notes")

def tnbutton():
    global pixelplace
    global counter
    if counter+1<33:
        tnbimage=ImageTk.PhotoImage(file='ThirtysecondNoteicon.png')
        label=Label(image=tnbimage)
        label.image= tnbimage
        label.pack
        mainarea.create_image(pixelplace, 340, image=tnbimage)
        pixelplace+=32
        counter+=1
        add_note_time(1, False)
    else:
        print("too many notes")

def tnrbutton():
    global pixelplace
    global counter
    if counter+1<33:
        tnrbimage=ImageTk.PhotoImage(file='ThirtysecondResticon.png')
        label=Label(image=tnrbimage)
        label.image= tnrbimage
        label.pack
        mainarea.create_image(pixelplace, 373, image=tnrbimage)
        pixelplace+=32
        counter+=1
        add_note_time(1, True)
    else:
        print("too many notes")


# placement line
line=mainarea.create_line(10,0,10,700,tags= 'line')

runline=False

def animation(x_move, y_move):
    global runline
    global line
    if runline:
        mainarea.move(line, x_move, y_move)
        mainarea.update()
        mainarea.after(20)

        root.after_idle(animation,x_move, y_move)

def reset_line():
    global line
    global runline
    global performCheck
    global currentNoteIndex
    currentNoteIndex = 0
    performCheck = False
    runline=False
    line = mainarea.create_line(10,0,10,700, tags='line')

def pbutton():
    global runline
    global performCheck
    global startTime
    startTime = int(round(time() * 1000))
    performCheck = True
    root.after(checkDelay,check)
    runline=True
    animation(5,0)

def delbutton():
    global pixelplace
    global counter
    global runline
    global performCheck
    global expectedNoteTimes
    expectedNoteTimes = [initial]
    performCheck = False
    mainarea.create_rectangle(0,0,1600,1600,fill='white')
    pixelplace = 110
    counter=0
    mainarea.create_line(100,370,1350,370,width=1)
    mainarea.create_line(100,385,1350,385,width=1)
    mainarea.create_line(100,355,1350,355,width=1)
    mainarea.create_line(100,340,1350,340,width=1)
    mainarea.create_line(100,325,1350,325,width=1)
    logoimage=ImageTk.PhotoImage(file='Logo.png')
    label=Label(image=logoimage)
    label.image= logoimage
    label.pack
    mainarea.create_image(1100, 150, image=logoimage)
    if runline:
        reset_line()
    
    

    
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
startButton.place(x=1075, y=30)


stopbPath = 'StopIcon.png'   
stopbImage = Image.open(stopbPath)
stopb = ImageTk.PhotoImage(stopbImage)
stopButton = Button(sidebar, image=stopb, border=0, command=reset_line)
stopButton.place(x=1000, y=30)

delbPath = 'Trash.png'   
delbImage = Image.open(delbPath)
delb = ImageTk.PhotoImage(delbImage)
delButton = Button(sidebar, image=delb, border=0,command=delbutton)
delButton.place(x=1050, y=120)


if __name__ == '__main__':
    root.bind("<Key>", key_press)
    root.mainloop()
    
#Button calls and looping
    

    

