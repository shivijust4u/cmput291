from tkinter import *
import quit
import session

class ViolationRecordPage(object):
	"""docstring for ClassName

		This component is used by a police officer to 
		issue a traffic ticket and record the violation. 
		You may assume that all the information about 
		ticket_type has been loaded in the 
		initial database.
		
		ticket( ticket_no, violator_no,vehicle_no, office_no,vtype,vdate,place,descriptions )

	"""
    
	def __init__(self, master):
		frame = Frame(master, width = 500, height = 500)
		frame.grid()
		self.frame = frame
		self.successor = -1
        
		self.formData = {}
		self.formText = ["ticket_no","violator_no","vehicle_id","office_no","vtype", "vdate", "place", "descriptions"]
		self.forms = self.makeForm(frame)

		self.pageTitle = self.makeTitle(frame, "Violation Record", 0, 1)

		self.submitButton = Button(frame, text="Submit", command=self.submitCallBack)
		self.submitButton.grid(row=10, column=1)

		self.homeButton = Button(frame, text="Home", command=self.homeCallBack)
		self.homeButton.grid(row=10, column=2)

		self.quitButton = Button(frame, text="Quit", command=lambda:quit.quit_callback(self.frame))
		self.quitButton.grid(row=10, column=0)

	def homeCallBack(self):
		self.successor = 0

	def submitCallBack(self):
		n=0
		for entry in self.entries:
				self.formData[self.formText[n]] = entry.get()
				n += 1
		#ticket( ticket_no, violator_no,vehicle_id, office_no,vtype,vdate,place,descriptions )
		query = "SELECT ticket_no FROM ticket WHERE ticket_no = '" + str(self.formData["ticket_no"] )+ "'"
		
		if (self.validateForm(query)): # Ticket_no is okay
			
			statement = "insert into ticket values('" + self.formData["ticket_no"] +"', '" +  self.formData["violator_no"]  +"', '" +  self.formData["vehicle_id"] +"', '" +  self.formData["office_no"] +"', '" +  self.formData["vtype"] + "', '" +  self.formData["vdate"] +"', '" +  self.formData["place"] +"', '" +  self.formData["descriptions"] + "')"
			print(statement)			
			session.db.passive_update(statement)
			
			
			#print("step 1")
			#data = (self.formData["ticket_no"], self.formData["violator_no"], self.formData["vehicle_id"], self.formData["office_no"], self.formData["vtype"], self.formData["vdate"], self.formData["place"], self.formData["descriptions"])		 	
			#print("step 2")			
			#session.db.curs.executemany("INSERT INTO ticket(ticket_no, violator_no,vehicle_id, office_no, vtype, vdate, place, descriptions) " 
			#		"VALUES(:1, :2, :3, :4, :5, :6, :7, :8)", data)
			
			#print("INSERT INTO ticket(ticket_no, violator_no,vehicle_id, office_no, vtype, vdate, place, descriptions) " 
			#		"VALUES(:1, :2, :3, :4, :5, :6, :7, :8)", data)
			#print("Insert complete")

			session.db.connection.commit()
			self.successor = 0;
			self.quit()
			    
	def validateForm(self, statement):                  
		rs = session.db.execute_sql(statement)
		print("rs: "+ str(rs))              
		if not rs:      
			print("NONE")           
			return True
		else: return False
		
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


