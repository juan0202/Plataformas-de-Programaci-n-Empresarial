from tkinter import Tk
from tkinter import Frame
from tkinter import Text
from tkinter import Button
from tkinter import Entry
from tkinter import StringVar
from tkinter import Label

root = Tk()
root.title("B I N G O")

frame = Frame(root, width = 500, height = 500, bg="blue", cursor = "right_ptr" )
frame.pack(fill='both', expand=1)

bingoLabel = Label(frame, text = "B I N G O", bg = "blue", fg = "white")
bingoLabel.grid(row = 1, column = 1, columnspan = 5, padx = 10, pady = 10) 

#----- change color ----- # 
def changeColorone():
    buttonone['bg']="red"

def changeColortwo():
    buttontwo['bg']="red"

def changeColorthree():
    buttonthree['bg']="red"

def changeColorfour():
    buttonfour['bg']="red"

def changeColorfive():
    buttonfive['bg']="red"

def changeColorsix():
    buttonsix['bg']="red"

def changeColorseven():
    buttonseven['bg']="red"

def changeColoreight():
    buttoneight['bg']="red"

def changeColornine():
    buttonnine['bg']="red"

def changeColorten():
    buttonten['bg']="red"

def changeColoreleven():
    buttoneleven['bg']="red"

def changeColortwelve():
    buttontwelve['bg']="red"

def changeColorthreeteen():
    buttonthreeteen['bg']="red"

def changeColorfourteen():
    buttonfourteen['bg']="red"

def changeColorfiveteen():
    buttonfiveteen['bg']="red"

def changeColorsixteen():
    buttonsixteen['bg']="red"

def changeColorseventeen():
    buttonseventeen['bg']="red"

def changeColoreightteen():
    buttoneightteen['bg']="red"

def changeColornineteen():
    buttonnineteen['bg']="red"

def changeColortwenty():
    buttontwenty['bg']="red"

def changeColortwentyone():
    buttontwentyone['bg']="red"

def changeColortwentytwo():
    buttontwentytwo['bg']="red"

def changeColortwentytheree():
    buttontwentythree['bg']="red"

def changeColortwentyfour():
    buttontwentyfour['bg']="red"

def changeColortwentyfive():
    buttontwentyfive['bg']="red"

#----- Fila 1 ----- # 
buttonone = Button(frame,text = "8", background="white", command = lambda:changeColorone(), width = 3, padx = 10, pady = 10)
buttonone.grid(row = 2, column = 1) 

buttonsix = Button(frame,text = "28", background="white", command = lambda:changeColorsix(), width = 3, padx = 10, pady = 10)
buttonsix.grid(row = 2, column = 2) 

buttoneleven = Button(frame,text = "31", background="white", command = lambda:changeColoreleven(), width = 3, padx = 10, pady = 10)
buttoneleven.grid(row = 2, column = 3)

buttonsixteen = Button(frame,text = "50", background="white", command = lambda:changeColorsixteen(), width = 3, padx = 10, pady = 10)
buttonsixteen.grid(row = 2, column = 4)

buttontwentyone = Button(frame,text = "75", background="white", command = lambda:changeColortwentyone(), width = 3, padx = 10, pady = 10)
buttontwentyone.grid(row = 2, column = 5)

#----- Fila 2 ----- # 
buttontwo = Button(frame,text = "9", background="white", command = lambda:changeColortwo(), width = 3, padx = 10, pady = 10)
buttontwo.grid(row = 3, column = 1) 

buttonseven = Button(frame,text = "19", background="white", command = lambda:changeColorseven(), width = 3, padx = 10, pady = 10)
buttonseven.grid(row = 3, column = 2) 

buttontwelve = Button(frame,text = "36", background="white", command = lambda:changeColortwelve(), width = 3, padx = 10, pady = 10)
buttontwelve.grid(row = 3, column = 3)

buttonseventeen = Button(frame,text = "48", background="white", command = lambda:changeColorseventeen(), width = 3, padx = 10, pady = 10)
buttonseventeen.grid(row = 3, column = 4)

buttontwentytwo = Button(frame,text = "73", background="white", command = lambda:changeColortwentytwo(), width = 3, padx = 10, pady = 10)
buttontwentytwo.grid(row = 3, column = 5)

#----- Fila 3 ----- # 
buttonthree = Button(frame,text = "14", background="white", command = lambda:changeColorthree(), width = 3, padx = 10, pady = 10)
buttonthree.grid(row = 4, column = 1) 

buttoneight = Button(frame,text = "22", background="white", command = lambda:changeColoreight(), width = 3, padx = 10, pady = 10)
buttoneight.grid(row = 4, column = 2) 

buttonthreeteen = Button(frame,text = "35", background="white", command = lambda:changeColorthreeteen(), width = 3, padx = 10, pady = 10)
buttonthreeteen.grid(row = 4, column = 3)

buttoneightteen = Button(frame,text = "46", background="white", command = lambda:changeColoreightteen(), width = 3, padx = 10, pady = 10)
buttoneightteen.grid(row = 4, column = 4)

buttontwentythree = Button(frame,text = "63", background="white", command = lambda:changeColortwentytheree(), width = 3, padx = 10, pady = 10)
buttontwentythree.grid(row = 4, column = 5)

#----- Fila 4 ----- # 
buttonfive = Button(frame,text = "1", background="white", command = lambda:changeColorfive(), width = 3, padx = 10, pady = 10)
buttonfive.grid(row = 6, column = 1) 

buttonten = Button(frame,text = "27", background="white", command = lambda:changeColorten(), width = 3, padx = 10, pady = 10)
buttonten.grid(row = 6, column = 2) 

buttonfiveteen = Button(frame,text = "45", background="white", command = lambda:changeColorfiveteen(), width = 3, padx = 10, pady = 10)
buttonfiveteen.grid(row = 6, column = 3)

buttontwenty = Button(frame,text = "58", background="white", command = lambda:changeColortwenty(), width = 3, padx = 10, pady = 10)
buttontwenty.grid(row = 6, column = 4)

buttontwentyfive = Button(frame,text = "61",background="white", command = lambda:changeColortwentyfive(), width = 3, padx = 10, pady = 10)
buttontwentyfive.grid(row = 6, column = 5)

#----- Fila 5 ----- # 
buttonfour = Button(frame,text = "10", background="white", command = lambda:changeColorfour(), width = 3, padx = 10, pady = 10)
buttonfour.grid(row = 5, column = 1) 

buttonnine = Button(frame,text = "20", background="white", command = lambda:changeColornine(), width = 3, padx = 10, pady = 10)
buttonnine.grid(row = 5, column = 2) 

buttonfourteen = Button(frame,text = "39", background="white", command = lambda:changeColorfourteen(), width = 3, padx = 10, pady = 10)
buttonfourteen.grid(row = 5, column = 3)

buttonnineteen = Button(frame,text = "57", background="white", command = lambda:changeColornineteen(), width = 3, padx = 10, pady = 10)
buttonnineteen.grid(row = 5, column = 4)

buttontwentyfour = Button(frame,text = "74", background="white", command = lambda:changeColortwentyfour(), width = 3, padx = 10, pady = 10)
buttontwentyfour.grid(row = 5, column = 5)


root.mainloop()