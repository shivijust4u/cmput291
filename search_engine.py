from Tkinter import *


class MainSearchPage(object):
    """docstring for ClassName"""
    def __init__(self, master):
        frame = Frame(master, bg = "white", width = 1000, height = 1000)
        frame.grid()
        self.frame = frame
        self.successor = -1

        self.buttonText = [
            "General Search",
            "List All Violations",
            "Print Vehicle History"]

        self.pageTitle = self.makeTitle(frame, "Main Menu", 0, 1)
        self.pageTitle.config(justify=CENTER)

        self.buttons = [self.makeButton(self.frame, self.buttonText[0], 5, 5,0),
                        self.makeButton(self.frame, self.buttonText[1], 5, 5,1),
                        self.makeButton(self.frame, self.buttonText[2], 5, 5,2)]

        self.buttons[0].config(command=self.callback0)
        self.buttons[1].config(command=self.callback1)
        self.buttons[2].config(command=self.callback2)

        self.homeButton = Button(frame, text="Home", command=self.callbackHome)
        self.homeButton.grid(row=10, column=2)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.grid(row=10, column=0)

    def callbackHome(self):
        print "Home"
        self.successor = 0

    def callback0(self):
        print "General Search"
        self.successor = 6

    def callback1(self):
        print "List All Violations"
        self.successor = 7

    def callback2(self):
        print "Print Vehicle History"
        self.successor = 8

    def makeButton(self, parent, caption, width, row, column):
        button = Button(parent, text=caption)
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


class GeneralSearchPage(object):
    """docstring for ClassName"""
    def __init__(self, master):
        frame = Frame(master, bg = "white", width = 1000, height = 1000)
        frame.grid()
        self.frame = frame
        self.successor = -1

        self.pageTitle = self.makeTitle(frame, "General Search", 0, 1)
        self.pageTitle.config(justify=CENTER)

        self.formText = ["NULL","NULL","NULL","NULL",]
        self.makeForm(self.frame)

        self.submitButton = Button(frame, text="Search", command=self.searchCB)
        self.submitButton.grid(row=10, column=1)

        self.homeButton = Button(frame, text="Home", command=self.callbackHome)
        self.homeButton.grid(row=10, column=2)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.grid(row=10, column=0)


    def callbackHome(self):
        self.successor = 0
        print "Home"

    def searchCB(self):
        resultText = "\t\tResults:\nMake: Ford\nModel: Focus\nYear: 1990"
        self.searchResults = Label(self.frame, text=resultText)
        self.searchResults.grid(row=40, column=0)

    def makeButton(self, parent, caption, width, row, column):
        button = Button(parent, text=caption)
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


class ViolationsSearchPage(object):
    """docstring for ClassName"""
    def __init__(self, master):
        frame = Frame(master, bg = "white", width = 1000, height = 1000)
        frame.grid()
        self.frame = frame
        self.successor = -1

        self.pageTitle = self.makeTitle(frame, "Violation Search", 0, 1)
        self.pageTitle.config(justify=CENTER)

        self.formText = ["NULL","NULL","NULL","NULL",]
        self.makeForm(self.frame)

        self.submitButton = Button(frame, text="Search", command=self.searchCB)
        self.submitButton.grid(row=10, column=1)

        self.homeButton = Button(frame, text="Home", command=self.callbackHome)
        self.homeButton.grid(row=10, column=2)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.grid(row=10, column=0)


    def callbackHome(self):
        self.successor = 0
        print "Home"

    def searchCB(self):
        resultText = "\t\tResults:\nMake: Ford\nModel: Focus\nYear: 1990"
        self.searchResults = Label(self.frame, text=resultText)
        self.searchResults.grid(row=40, column=0)

    def makeButton(self, parent, caption, width, row, column):
        button = Button(parent, text=caption)
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


class VehicleHistorySearchPage(object):
    """docstring for ClassName"""
    def __init__(self, master):
        frame = Frame(master, bg = "white", width = 1000, height = 1000)
        frame.grid()
        self.frame = frame
        self.successor = -1

        self.pageTitle = self.makeTitle(frame, "Vehicle History Search", 0, 1)
        self.pageTitle.config(justify=CENTER)

        self.formText = ["NULL","NULL","NULL","NULL",]
        self.makeForm(self.frame)

        self.submitButton = Button(frame, text="Search", command=self.searchCB)
        self.submitButton.grid(row=10, column=1)

        self.homeButton = Button(frame, text="Home", command=self.callbackHome)
        self.homeButton.grid(row=10, column=2)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.grid(row=10, column=0)

    def callbackHome(self):
        self.successor = 0
        print "Home"

    def searchCB(self):
        resultText = "Results:\nMake: Ford\nModel: Focus\nYear: 1990"
        self.searchResults = Label(self.frame, text=resultText)
        self.searchResults.grid(row=40, column=0)

    def makeButton(self, parent, caption, width, row, column):
        button = Button(parent, text=caption)
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
        
