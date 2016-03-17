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
		self.personalFormData = {}

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
		licenceAvailable = self.validateForm("SELECT licence_no FROM drive_licence where licence_no = '" + str(self.formData["licence_no"] ) + "'")
		personValid = self.validateForm("SELECT sin FROM people where sin = '" + str(self.formData["sin"] )+ "'")
		noLicence = self.validateForm("SELECT licence_no FROM drive_licence where sin = '" + str(self.formData["sin"] )+ "'")

		if(licenceAvailable and not personValid and noLicence):
			self.submitLicense()
			
		elif (not noLicence):
			print("Person already has licence")
		elif (not licenceAvailable):
			print("licence number already exists")
		else:
			print("Person does no exist in database")
			self.makePersonalForm(self.frame)
			self.displayResults("Please Enter Buyer's Personal Information", 39, 1)

			self.personalEntries[0].insert(0, self.formData["sin"])

			self.submitButton2 = Button(self.frame, text="Submit Personal Data", command=self.submitPersonal)
			self.submitButton2.grid(row=50, column=1)

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

	def makePersonalForm(self, parent):
		self.personalFormText = ["sin", "name", "height", "weight", "eyecolor", "haircolor", "addr", "gender", "birthday"]
		
		baseRow = 30
		self.personalEntries = []
		for text in self.personalFormText:
			self.personalEntries.append(self.makeentry(parent, text, 40, baseRow, [0,1]),)
			baseRow += 1  

	def submitLicense(self):
		data = [(self.formData["licence_no"], self.formData["sin"], self.formData["class"], self.image, self.formData["issuing_date"],self.formData["expiring_date"])]		 	
		session.db.curs.executemany("INSERT INTO drive_licence(licence_no,sin,class,photo,issuing_date,expiring_date) " 
				"VALUES(:1, :2, :3, :4, :5, :6)", data)			
		print("Licence Registered!")
		
		session.db.connection.commit()
		# GO Home
		self.successor = 0;
		self.quit()

	def submitPersonal(self):
		n=0
		submitted_person = False
		for entry in self.personalEntries:
			self.personalFormData[self.personalFormText[n]] = entry.get()			
			if not entry.get():
				entry.insert(0,"null")
			n+=1

		notNull = True
		# check for null entries
		if self.personalEntries[0].get() == "null" or not self.personalEntries[0].get():
			print("can't be null")
			notNull = False

		data3 = [(self.personalFormData["sin"], self.personalFormData["name"], self.personalFormData["height"], self.personalFormData["weight"], self.personalFormData["eyecolor"],self.personalFormData["haircolor"],self.personalFormData["addr"],self.personalFormData["gender"],self.personalFormData["birthday"])]

		if notNull == True:
			session.db.curs.executemany("INSERT INTO people( sin, name, height,weight,eyecolor, haircolor,addr,gender,birthday) " 
					"VALUES(:1, :2, :3, :4, :5, :6, :7, :8, :9)", data3 )

			print("Person Registered!")
			submitted_person = True

		if submitted_person:
			self.submitLicense()

	def displayResults(self, text, row, column):
		resultText = text
		self.searchResults = Label(self.frame, text=resultText)
		self.searchResults.grid(row=row, column=column)			


