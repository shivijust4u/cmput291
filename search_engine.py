from tkinter import *
import quit

class MainSearchPage(object):
    """docstring for ClassName"""
    def __init__(self, master):
        frame = Frame(master, width = 1000, height = 1000)
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

        self.quitButton = Button(frame, text="Quit", command=lambda:quit.quit_callback(self.frame))
        self.quitButton.grid(row=10, column=0)

    def callbackHome(self):

        self.successor = 0

    def callback0(self):

        self.successor = 6

    def callback1(self):
        self.successor = 7

    def callback2(self):

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
    """docstring for ClassName

        List the name, licence_no, addr, birthday, driving class, 
        driving_condition, and the expiring_data of a driver by 
        entering either a licence_no or a given name. It shall 
        display all the entries if a duplicate name is given.

    """
    def __init__(self, master):
        frame = Frame(master, width = 1000, height = 1000)
        frame.grid()
        self.frame = frame
        self.successor = -1

        self.pageTitle = self.makeTitle(frame, "General Search", 0, 1)
        self.pageTitle.config(justify=CENTER)

        self.resultText = ["name: \n", "licence_no: \n", "addr: \n","birthday: \n","class: \n", "driving_condition: \n", "expires: "]

        self.resultLabels = ["name: ", "licence_no: ", "addr: " , "birthday: " , , , , ,  ]

        self.formText = ["licence_no","given name"]
        self.makeForm(self.frame)

        self.submitButton = Button(frame, text="Search", command=self.searchCB)
        self.submitButton.grid(row=10, column=1)

        self.homeButton = Button(frame, text="Home", command=self.callbackHome)
        self.homeButton.grid(row=10, column=2)

        self.quitButton = Button(frame, text="Quit", command=lambda:quit.quit_callback(self.frame))
        self.quitButton.grid(row=10, column=0)


    def callbackHome(self):
        self.successor = 0


    def searchCB(self):
        #resultText = "\t\tResults:\nMake: Ford\nModel: Focus\nYear: 1990"
        resultTitle = self.displayResults("Search Results: ", 39, 1)
        resultTitle.grid(columnspan=4)
		
		#resultsSet = session.db.execute_sql("SELECT")		
	
        self.nullData = []
        for text in self.resultText:
            self.nullData.append("null")

        self.searchResults = []
        baseRow = 40
        for result in self.resultText:
            result = Label(self.frame, text=result)
            result.grid(row=baseRow, column=0, sticky=E)
            result.config(anchor=E,justify=RIGHT)
            self.searchResults.append(result)
            baseRow +=1

        baseRow = 40
        for result in self.nullData:
            result = Label(self.frame, text=result)
            result.grid(row=baseRow, column=1, sticky=W)
            result.config(anchor=E,justify=RIGHT)
            self.searchResults.append(result)
            baseRow +=1

        # photo = PhotoImage(file="img.png")
        # w = Label(self.frame, image=photo)
        # w.photo = photo
        # w.grid(row=50, column=10)

    def displayResults(self, text, row, column):
        resultText = text
        self.searchResults = Label(self.frame, text=resultText)
        self.searchResults.grid(row=row, column=column)
        return self.searchResults


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
    """docstring for ClassName

        List all violation records received by a person 
        if  the drive licence_no or sin of a person  
        is entered.

    """
    def __init__(self, master):
        frame = Frame(master, width = 1000, height = 1000)
        frame.grid()
        self.frame = frame
        self.successor = -1
        self.resultText = []
        self.resultText.append("violation: ")
        self.resultText.append("violation: ")

        self.nullData = []
        for text in self.resultText:
            self.nullData.append("null")

        self.pageTitle = self.makeTitle(frame, "Violation Search", 0, 1)
        self.pageTitle.config(justify=CENTER)

        self.formText = ["licence_no","sin"]
        self.makeForm(self.frame)

        self.submitButton = Button(frame, text="Search", command=self.searchCB)
        self.submitButton.grid(row=10, column=1)

        self.homeButton = Button(frame, text="Home", command=self.callbackHome)
        self.homeButton.grid(row=10, column=2)

        self.quitButton = Button(frame, text="Quit", command=lambda:quit.quit_callback(self.frame))
        self.quitButton.grid(row=10, column=0)


    def callbackHome(self):
        self.successor = 0

    def searchCB(self):
        resultTitle = self.displayResults("Violation Report", 39, 1)
        resultTitle.grid(columnspan=4)

        self.searchResults = []
        baseRow = 40
        for result in self.resultText:
            result = Label(self.frame, text=result)
            result.grid(row=baseRow, column=0, sticky=E)
            result.config(anchor=E,justify=RIGHT)
            self.searchResults.append(result)
            baseRow +=1

        baseRow = 40
        for result in self.nullData:
            result = Label(self.frame, text=result)
            result.grid(row=baseRow, column=1, sticky=E)
            result.config(anchor=E,justify=RIGHT)
            self.searchResults.append(result)
            baseRow +=1

    def displayResults(self, text, row, column):
        resultText = text
        self.result = Label(self.frame, text=text)
        self.result.grid(row=row, column=column)
        return self.result

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
    """docstring for ClassName

            
 out the vehicle_history, including the 
            number of times that a vehicle has been changed 
            hand, the average price, and the number of 
            violations it has been involved by entering the 
            vehicle's serial number.

    """
    def __init__(self, master):
        frame = Frame(master, width = 1000, height = 1000)
        frame.grid()
        self.frame = frame
        self.successor = -1

        self.resultText = [ "Number of times changed hands: ", "Average Price: ", "Number of Violations" ]

        self.nullData = []
        for text in self.resultText:
            self.nullData.append("null")

        self.pageTitle = self.makeTitle(frame, "Vehicle History Search", 0, 1)
        self.pageTitle.config(justify=CENTER)

        self.formText = ["VIN: "]
        self.makeForm(self.frame)

        self.submitButton = Button(frame, text="Search", command=self.searchCB)
        self.submitButton.grid(row=10, column=1)

        self.homeButton = Button(frame, text="Home", command=self.callbackHome)
        self.homeButton.grid(row=10, column=2)

        self.quitButton = Button(frame, text="Quit", command=lambda:quit.quit_callback(self.frame))
        self.quitButton.grid(row=10, column=0)

    def callbackHome(self):
        self.successor = 0


    def searchCB(self):
        
        resultTitle = self.displayResults("Vehicle History Report", 39, 1)
        resultTitle.grid(columnspan=4)
        
        #rt = self.displayResults("Results: ", 38, 1)

        self.searchResults = []
        baseRow = 40
        for result in self.resultText:
            result = Label(self.frame, text=result)
            result.grid(row=baseRow, column=0, sticky=E)
            result.config(anchor=E,justify=RIGHT)
            self.searchResults.append(result)
            baseRow +=1

        baseRow = 40
        for result in self.nullData:
            result = Label(self.frame, text=result)
            result.grid(row=baseRow, column=1, sticky=E)
            result.config(anchor=E,justify=RIGHT)
            self.searchResults.append(result)
            baseRow +=1

    def displayResults(self, text, row, column):
        resultText = text
        rs = Label(self.frame, text=text)
        rs.grid(row=row, column=column)
        return rs


    def makeButton(self, parent, caption, width, row, column):
        button = Button(parent, text=caption)
        button.grid(row=row, column=column)
        return button

    def makeentry(self, parent, caption, width, row, column):
        Label(parent, text=caption, width=20, justify=RIGHT).grid(row=row,column=column[0], sticky=E)
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
        
