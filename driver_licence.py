from tkinter import *
from database_class import Database
import session
import quit

class DriverLicencePage(object):
	"""docstring for ClassName

		drive_licence(licence_no,sin,class,photo,issuing_date,expiring_date)

	"""
	def __init__(self, master):
		frame = Frame(master, width = 500, height = 500)
		frame.grid()
		self.frame = frame
		self.successor = -1
		self.formData = {}

		self.formText = ["licence_no","sin","class","photo name","issuing_date", "expiring_date"]
		self.forms = self.makeForm(frame)
		self.entries[3].insert(0, "photo.png")

		self.pageTitle = self.makeTitle(frame, "New Driver Licence", 0, 1)

		self.submitButton = Button(frame, text="Submit", command=self.submitCB)
		self.submitButton.grid(row=10, column=1)

		self.homeButton = Button(frame, text="Home", command=self.homeCB)
		self.homeButton.grid(row=10, column=2)
		
		self.quitButton = Button(frame, text="Quit", command=lambda:quit.quit_callback(self.frame))
		self.quitButton.grid(row=10, column=0)

	def homeCB(self):
		self.successor = 0

	def submitCB(self):
		n=0
		for entry in self.entries:
			if (self.formText[n] == "photo name"):

				f_image  = open(entry.get(),'rb')
				self.image  = f_image.read()

			self.formData[self.formText[n]] = entry.get()           
			n +=1
		#drive_licence(licence_no,sin,class,photo,issuing_date,expiring_date)
		query = "SELECT licence_no FROM drive_licence where licence_no = '" + str(self.formData["licence_no"] ) + "'"
		if(self.validateForm(query)):
			data = [(self.formData["licence_no"], self.formData["sin"], self.formData["class"], self.image, self.formData["issuing_date"],self.formData["expiring_date"])]		 	
			session.db.curs.executemany("INSERT INTO drive_licence(licence_no,sin,class,photo,issuing_date,expiring_date) " 
					"VALUES(:1, :2, :3, :4, :5, :6)", data)			
			print("Transaction complete")
			
			session.db.connection.commit()
			# GO Home
			self.successor = 0;
			self.quit()
		else:
			print("licence number already exists")
		
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


