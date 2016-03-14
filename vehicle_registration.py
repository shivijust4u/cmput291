from Tkinter import *


class VehicleRegPage(object):
    """docstring for ClassName"""
    def __init__(self, master):
        frame = Frame(master, bg = "white", width = 500, height = 500)
        frame.grid()
        self.frame = frame
        self.successor = -1
        self.makeForm(frame)

        for entry in self.entries:
            entry.insert(0,"null")



        self.pageTitle = self.makeTitle(frame, "Register a New Vehicle", 0, 1)

        self.submitButton = Button(frame, text="Submit", command=self.submitCB)
        self.submitButton.grid(row=10, column=1)

        self.homeButton = Button(frame, text="Home", command=self.homeCB)
        self.homeButton.grid(row=10, column=2)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.grid(row=10, column=0)
    
    def homeCB(self):
        print "Home"
        self.successor = 0

    def submitCB(self):
        print "submitted data..."
        for entry in self.entries:
            print "Entry: "
            print entry.get()
        #self.displayResults("Success", 40, 0)
        self.makePersonalForm(self.frame)
        self.displayResults("Please Enter Driver Information", 16, 1)
        for entry in self.personalEntries:
            entry.insert(0,"null")        
        self.submitButton2 = Button(self.frame, text="Submit Personal Data", command=self.submitCB2)
        self.submitButton2.grid(row=50, column=1)

    def submitCB2(self):
        print "submitted personal data..."
        for entry in self.personalEntries:
            print "Entry: "
            print entry.get()



    def displayResults(self, text, row, column):
        resultText = text
        self.searchResults = Label(self.frame, text=resultText)
        self.searchResults.grid(row=row, column=column)

    def makeButton(self, parent, caption, width, row, column):
        button = Button(parent, text=caption, command=submitCallback)
        button.grid(row=row, column=column)
        return button

    def makeentry(self, parent, caption, width, row, column):
        Label(parent, text=caption, width=20, justify=RIGHT).grid(row=row,column=column[0])
        entry = Entry(parent)
        if width:
            entry.config(width=width)
        entry.grid(row=row, column=column[1], sticky=E)
        return entry

    def makeTitle(self, parent, text, row, column):
        title = Label(parent, text=text)
        title.grid(row=row, column=column)
        return title

    def quit(self):
        self.frame.destroy()

    def makeForm(self, parent):
        
        self.entries = [
        self.makeentry(parent, "serial_no", 40, 2, [0,1]),
        self.makeentry(parent, "make", 40, 3, [0,1]),
        self.makeentry(parent, "model", 40, 4, [0,1]),
        self.makeentry(parent, "year", 40, 5, [0,1]),
        self.makeentry(parent, "color", 40, 6, [0,1]),
        self.makeentry(parent, "type_id", 40, 7, [0,1])]
    
    def makePersonalForm(self, parent):
        self.personalFormText = ["sin", "name", "weight", "eyecolor", "haircolor", "addr", "gender", "birthday"]
        
        baseRow = 20
        self.personalEntries = []
        for text in self.personalFormText:
            self.personalEntries.append(self.makeentry(parent, text, 40, baseRow, [0,1]),)
            baseRow += 1            

