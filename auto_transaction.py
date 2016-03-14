from Tkinter import *


class AutoTransactionPage(object):
    """docstring for ClassName"""
    def __init__(self, master):
        frame = Frame(master, bg = "white", width = 500, height = 500)
        frame.grid()
        self.successor = -1

        self.frame = frame
        self.formText = ["Seller Name: ","Buyer Name: ","Date: ","Price: "]
        self.forms = self.makeForm(frame)
        for entry in self.entries:
            entry.insert(0,"null")


        self.entries[0].delete(0, END)
        self.entries[1].delete(0,END)    
        self.entries[2].delete(0, END)    

        self.entries[2].insert(20, "(YYYY-MM-DD)")

        self.pageTitle = self.makeTitle(frame, "New Auto Transaction", 0, 1)

        self.submitButton = Button(frame, text="Submit", command=self.submitCallBack)
        self.submitButton.grid(row=10, column=1)

        self.homeButton = Button(frame, text="Home", command=self.homeCB)
        self.homeButton.grid(row=10, column=2)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.grid(row=10, column=0)


    def homeCB(self):
        print "Home"
        self.successor = 0

    def submitCallBack(self):
        print "Process Data Here..."
        n=0
        for entry in self.entries:
            print self.formText[n]
            print entry.get()
            n += 1
        #newFrame = Frame(self.frame)
        #newFrame.grid()
        #Button(newFrame, text="TEXT").grid(row=0,column=0)

        # delete previous owner entry in database
        # update new owner entry in database
         

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
            self.entries.append(self.makeentry(parent, text, 40, baseRow, [0,1]))
            baseRow += 1


    def quit(self):
        self.frame.destroy()


