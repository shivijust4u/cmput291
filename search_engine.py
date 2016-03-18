from tkinter import *
import quit
import session

class MainSearchPage(object):
    """

    """
    def __init__(self, master):
        frame = Frame(master, width = 1000, height = 1000)
        frame.grid()
        self.formData = {}
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
        """
        for parent use self.frame
        """
        title = Label(parent, text=text)
        title.grid(row=row, column=column)
        return title

    def quit(self):
        self.frame.destroy()


class GeneralSearchPage(object):
    """

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
        
        self.errorMsg = ""
        self.pageTitle = self.makeTitle(frame, "General Search", 0, 1)
        self.pageTitle.config(justify=CENTER)

        self.resultText = ["name: \n", "licence_no: \n", "addr: \n","birthday: \n","class: \n", "driving_condition: \n", "expires: "]
        self.labels = ["name: ", "licence_no: ", "addr: ","birthday: ","class: ", "expires: ", "driving_condition: "]
        self.formData = {}
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
        print ("\nGeneral Search Results\n")
        n=0
        for entry in self.entries:
                self.formData[self.formText[n]] = entry.get()
                n+=1
        querynum = 0
        if not self.formData[self.formText[0]]:
               query = "select p.name,d.licence_no,p.addr,p.birthday,d.class,d.expiring_date,dc.description from people p,drive_licence d,driving_condition dc, restriction r where p.sin = d.sin AND d.licence_no = r.licence_no AND r.r_id = dc.c_id AND p.name ='" + str(self.formData["given name"] )+ "'"
               rs = session.db.execute_sql(query)
               if not rs:
                    query = "select p.name,d.licence_no,p.addr,p.birthday,d.class,d.expiring_date from people p,drive_licence d where p.sin = d.sin AND p.name='" + str(self.formData["given name"] )+ "'"
                    querynum = 1       
               self.executequery(query,querynum)
        
        elif not self.formData[self.formText[1]]:
               query = "select p.name,d.licence_no,p.addr,p.birthday,d.class,d.expiring_date,dc.description from people p,drive_licence d,driving_condition dc, restriction r where p.sin = d.sin AND d.licence_no = r.licence_no AND r.r_id = dc.c_id AND d.licence_no ='" + str(self.formData["licence_no"] )+ "'"
               rs = session.db.execute_sql(query)
               if not rs:
                    query = "select p.name,d.licence_no,p.addr,p.birthday,d.class,d.expiring_date from people p,drive_licence d where p.sin = d.sin AND d.licence_no='" + str(self.formData["licence_no"] )+ "'"
                    querynum = 1       
               self.executequery(query,querynum)
        
        elif  (self.formData[self.formText[0]] and self.formData[self.formText[1]]) :
              
              query = "select p.name,d.licence_no,p.addr,p.birthday,d.class,d.expiring_date,dc.description from people p,drive_licence d,driving_condition dc, restriction r where p.sin = d.sin AND d.licence_no = r.licence_no AND r.r_id = dc.c_id AND d.licence_no ='" + str(self.formData["licence_no"] )+ "'"
              
              rs = session.db.execute_sql(query)
              if not rs:
                   query = "select p.name,d.licence_no,p.addr,p.birthday,d.class,d.expiring_date from people p,drive_licence d where p.sin = d.sin AND d.licence_no='" + str(self.formData["licence_no"] )+ "'"
                   querynum = 1       
              print("Result of First Input: ")
              self.executequery(query,querynum)
                           
              querynum = 0
              query = "select p.name,d.licence_no,p.addr,p.birthday,d.class,d.expiring_date,dc.description from people p,drive_licence d,driving_condition dc, restriction r where p.sin = d.sin AND d.licence_no = r.licence_no AND r.r_id = dc.c_id AND p.name ='" + str(self.formData["given name"] )+ "'"
              rs = session.db.execute_sql(query)
              if not rs:
                   query = "select p.name,d.licence_no,p.addr,p.birthday,d.class,d.expiring_date from people p,drive_licence d where p.sin = d.sin AND p.name='" + str(self.formData["given name"] )+ "'"
                   querynum = 1       
              print("Result of Second Input: ")
              self.executequery(query,querynum)
              
        else:
              print("Invalid licence_no or name/ No Data Found") 
              self.displayText("Invalid licence_no or name", 23, 1) 

    def executequery(self,query,querynum):
        rs = session.db.execute_sql(query) 
        
        for elements in rs:
               n = 0
               for item in elements:
                    print(self.labels[n] + str(item).strip().rstrip('\n') )
                    n+=1 
               if querynum:
                    print("driving_condition: None" )           
               print("\n\n")
        if not rs:
                self.displayText("Invalid licence_no or name", 23, 1)  
                print("Invalid licence_no or name/ No Data Found\n")       
    
    def displayResults(self, text, row, column):
        resultText = text
        self.result = Label(self.frame, text=resultText)
        self.result.grid(row=row, column=column)
        return self.result

    def displayText(self, text, row, column):
        resultText = text
        self.searchResults = Label(self.frame, text=resultText)
        self.searchResults.grid(row=row, column=column)
    
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
    """

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
        self.labels = ["ticket_no: ", "violator_no: ","vehicle_no: ","office_no: ","vtype: ","vdate: ","place: ","descriptions: "]

        self.outputData = []
        self.pageTitle = self.makeTitle(frame, "Violation Search", 0, 1)
        self.pageTitle.config(justify=CENTER)
        self.formData = {}
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
        print ("\nViolations Search Results\n")
        self.formData = {}
        n=0
        for entry in self.entries:
                self.formData[self.formText[n]] = entry.get()
                n+=1
     
        if not self.formData[self.formText[0]]:
               
               query = "select t.* from people p,ticket t where p.sin = t.violator_no AND p.sin = '" + str(self.formData["sin"] )+ "'"
               self.executequery(query)  
                    
        elif not self.formData[self.formText[1]]:
               query = "select t.* from drive_licence d,ticket t where d.sin = t.violator_no AND d.licence_no = '" + str(self.formData["licence_no"] )+ "'"
               self.executequery(query)
        
        elif (self.formData[self.formText[0]] and  self.formData[self.formText[1]]) :
               
               query = "select t.* from drive_licence d,ticket t where d.sin = t.violator_no AND d.licence_no = '" + str(self.formData["licence_no"] )+ "'"
               print("Result of First Input: ")
               self.executequery(query)  
               
               query = "select t.* from people p,ticket t where p.sin = t.violator_no AND p.sin = '" + str(self.formData["sin"] )+ "'"
               print("Result of Second Input: ")
               self.executequery(query)
        
        else:
               self.displayText("Invalid licence_no or sin", 23, 1) 
               print("Invalid licence_no or name/ No Data Found\n") 

    def executequery(self,query):
        rs = session.db.execute_sql(query)
        #print("rs: "+ str(rs))
        
        for elements in rs:
               n = 0
               for item in elements:
                    print(self.labels[n] + str(item).strip().rstrip('\n') )
                    n+=1 
                    
               print("\n")
        if not rs:
                self.displayText("Invalid licence_no or sin", 23, 1)        
                print("Invalid licence_no or sin/ No Data Found\n")      
      
    def displayResults(self, text, row, column):
        resultText = text
        self.result = Label(self.frame, text=text)
        self.result.grid(row=row, column=column)
        return self.result

    def displayText(self, text, row, column):
        resultText = text
        self.searchResults = Label(self.frame, text=resultText)
        self.searchResults.grid(row=row, column=column)
    
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
    """


            Print out the vehicle_history, including the
            number of times that a vehicle has been changed
            hand, the average price, and the number of
            violations it has been involved by entering the
            vehicle's serial number.

    """
    def __init__(self, master):
        self.master = master
        frame = Frame(master, width = 1000, height = 1000)
        frame.grid()
        self.frame = frame
        self.newFrame = Frame(self.master)
        self.newFrame.grid()
        

        self.successor = -1

        self.resultText = [ "Number of times changed hands: ", "Average Price: ", "Number of Violations " ]
        self.labels = [ "Number of times changed hands: ", "Average Price: ", "Number of Violations: " ]

        
      

        self.pageTitle = self.makeTitle(frame, "Vehicle History Search", 0, 1)
        self.pageTitle.config(justify=CENTER)
        self.formData = {}
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
        print ("\nVehicle History Search Results\n")
        self.formData[self.formText[0]] = self.entries[0].get()
        #print("input value :" +  self.formData["VIN: "])
        query = "select DISTINCT s.vehicle_id, COUNT ( DISTINCT s.transaction_id), AVG(s.price), COUNT (DISTINCT t.ticket_no) from  auto_sale s left join ticket t on s.vehicle_id = t.vehicle_id where s.vehicle_id = '" + str(self.formData["VIN: "] )+ "' GROUP BY s.vehicle_id"
        
           
        rs = session.db.execute_sql(query)
       
        for elements in rs:
                n = 0
                for item in elements[1:]:
                    print(self.labels[n] + str(item).strip().rstrip('\n') )
                    n+=1 
                    
                print("\n")
        if not rs:
                self.displayText("Invalid Vehicle Id", 23, 1)   
                print ("Invalid Vehicle Id/ No Data Found\n")     
       
    def displayResults(self, text, row, column):
        resultText = text
        rs = Label(self.frame, text=text)
        rs.grid(row=row, column=column)
        return rs

    def displayText(self, text, row, column):
        resultText = text
        self.searchResults = Label(self.frame, text=resultText)
        self.searchResults.grid(row=row, column=column)

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
        self.newFrame.destroy()
        self.frame.destroy()

