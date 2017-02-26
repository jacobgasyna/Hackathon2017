# Copywrite © 2017 Joe Rogge, Jacob Gasyna and Adele Rehkemper

#This file is part of Rhythm Trainer Pro.    Rhythm Trainer Pro is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.    Rhythm Trainer Pro is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.    You should have received a copy of the GNU General Public License
#along with Rhythm Trainer Pro.  If not, see <http://www.gnu.org/licenses/>.


from PIL import Image

class Noteclass():
    Note=0

class Wholenote(Noteclass):
    len_Wholenote = 32
    img_Wholenote = Image.open("WholeNote.png")
    

class Halfnote(Noteclass):
    len_Halfnote = 16
    img_Halfnote = Image.open("HalfNote.png")
        

class Quarternote(Noteclass):
    len_Quarternote = 8
    img_Quarternote = Image.open("QuarterNote.png")
        

class Eigthnote(Noteclass):
    len_Eighthnote = 4
    img_Eighthnote = Image.open("EigthNote.png")
        

class Sixteenthnote(Noteclass):
    len_Sixteenthnote = 2
    img_Sixteenthnote = Image.open("SixteenthNote.png")
        

class Thirtysecondnote(Noteclass):
    len_Thirtysecondnote = 1
    img_Thirtysecondnote = Image.open("ThirtysecondNote.png")

class Wholerest(Noteclass):
    len_Wholerest = 32
    img_Wholerest = Image.open("ThirtysecondNote.png")
    

class Halfrest(Noteclass):
    len_Halfrest = 16
    img_Halfrest = Image.open("HalfRest.png")
    
    

class Quarterrest(Noteclass):
    len_Quarterrest = 8
    len_Quarterrest = Image.open("QuarterRest.png")
    

class Eigthrest(Noteclass):
    len_Eightrest = 4
    img_Eighthrest = Image.open("EigthRest.png")
    

class Sixteenth(Noteclass):
    len_Sixteenth = 2
    img_Sixteenth = Image.open("SixteenthRest.png")
    

class Thirtysecondrest(Noteclass):
    len_Thirtysecondrest = 1
    img_Thirtysecondrest = Image.open("ThirtysecondRest.png")



