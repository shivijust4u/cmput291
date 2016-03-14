from Tkinter import *


class DriverLicencePage(object):
    """docstring for ClassName

        drive_licence(licence_no,sin,class,photo,issuing_date,expiring_date)

    """
    def __init__(self, master):
        frame = Frame(master, bg = "white", width = 500, height = 500)
        frame.grid()
        self.successor = -1

        self.frame = frame
        self.formText = ["licence_no","sin","class","photo name","issuing_date", "expiring_date"]
        self.forms = self.makeForm(frame)

        self.entries[2].insert(0, "null")
        self.entries[3].insert(0, "mugshot.png")
        self.entries[4].insert(0, "null")
        self.entries[5].insert(0, "null")

        self.pageTitle = self.makeTitle(frame, "New Driver Licence", 0, 1)

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
        print "Process Data Here..."
        n=0
        for entry in self.entries:
            if (self.formText[n] == "photo name"):
                #(Assumes a file by this name exists 
                #in the directory you are running from)
                f_image  = open(entry.get(),'rb')
                self.image  = f_image.read()
                print("image succesfully read!\n should send to database to insert")
            
            print "Form {}".format(n)
            print entry.get()
            n +=1

        
        
        

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

    def makeForm(self, parent):
        baseRow = 2
        self.entries = []
        for text in self.formText:
            self.entries.append(self.makeentry(parent, text, 40, baseRow, [0,1]),)
            baseRow += 1

    def quit(self):
        self.frame.destroy()


