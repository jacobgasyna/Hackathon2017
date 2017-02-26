# Copywrite © 2017 Joe Rogge, Jacob Gasyna and Adele Rehkemper

#This file is part of Rhythm Trainer Pro.    Rhythm Trainer Pro is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.    Rhythm Trainer Pro is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.    You should have received a copy of the GNU General Public License
#along with Rhythm Trainer Pro.  If not, see <http://www.gnu.org/licenses/>.

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
mainarea = Canvas(root, bg='#FFA', width=screenWidth-200)
mainarea.pack(expand=True, fill='both', side='right')

# sidebar
sidebar = Frame(root, bg='#FFF', width=200)
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

#hnPath = 'HalfNoteicon.png'
#hnImage = Image.open(hnPath)
#hn = ImageTk.PhotoImage(hnImage)
#hnButton = Button(sidebar, image=hn, border=0)
#hnButton.place(x=25, y=0)

hnRestPath = 'HalfResticon.png'   
hnRestImage = Image.open(hnRestPath)
hnRest = ImageTk.PhotoImage(hnRestImage)
hnRestButton = Button(sidebar, image=hnRest, border=0)
hnRestButton.place(x=100, y=75)

qnPath = 'QuarterNoteicon.png'
qnImage = Image.open(qnPath)
qn = ImageTk.PhotoImage(qnImage)
qnButton = Button(sidebar, image=qn, border=0)
qnButton.place(x=25, y=150)

qnRestPath = 'QuarterResticon.png'   
qnRestImage = Image.open(qnRestPath)
qnRest = ImageTk.PhotoImage(qnRestImage)
qnRestButton = Button(sidebar, image=qnRest, border=0)
qnRestButton.place(x=100, y=150)

#enPath = 'EighthNoteicon.png'
#enImage = Image.open(enPath)
#en = ImageTk.PhotoImage(enImage)
#enButton = Button(sidebar, image=en, border=0)
#enButton.place(x=25, y=150)

#enRestPath = 'EighthResticon.png'   
#enRestImage = Image.open(enRestPath)
#enRest = ImageTk.PhotoImage(enRestImage)
#enRestButton = Button(sidebar, image=enRest, border=0)
#enRestButton.place(x=100, y=150)

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

if __name__ == '__main__':
    root.mainloop()
