from tkinter import *
import quit
import session

class VehicleRegPage(object):
	"""docstring for ClassName"""
	def __init__(self, master):
		frame = Frame(master, width = 500, height = 500)
		frame.grid()
		self.frame = frame
		self.successor = -1
		
		self.formData = {}
		self.ownerFormData = {}
		self.personalFormData = {}
		self.formText = ["serial_no", "make", "model", "year", "color", "type_id"]
		self.makeForm(frame)
		self.pageTitle = self.makeTitle(frame, "Register a New Vehicle", 0, 1)

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
			self.formData[self.formText[n]] = entry.get()
			n+=1
		#print(self.formData)
		querry = "SELECT serial_no FROM vehicle where serial_no = " + str(self.formData["serial_no"])
		
		validation = False
		if self.formData["serial_no"]:		
			validation = self.validateForm(querry)
		
		if validation:
			if self.errorMsg:			
				self.errorMsg.config(text="Vehicle Not In Database")
			self.submitButton.config(state=DISABLED)
			#self.displayResults("Success", 40, 0)
			self.makeOwnerForm(self.frame)
			self.displayResults("Please Enter Owner Information", 25, 1)


			self.ownerEntries[1].insert(0, self.formData["serial_no"])
		
			self.submitOwnerButton = Button(self.frame, text="Submit Owner Data", command=self.submitOwnerCallback)
			self.submitOwnerButton.grid(row=29, column=1)
		
		else:
			if self.formData["serial_no"]:
				self.errorMsg = self.displayResults( "Vehicle already registered", 8, 1)
	
	def validateForm(self, statement):                  
		rs = session.db.execute_sql(statement)
		print("rs: "+ str(rs))              
		if not rs:      
			print("NONE")           
			return True
		else: return False

	def submitOwnerCallback(self):
		n=0
		for entry in self.ownerEntries:
			self.ownerFormData[self.ownerFormText[n]] = entry.get()
			n+=1
		querry = "SELECT sin from people where sin = " + str(self.ownerFormData["owner_id"])    
		validation = self.validateForm(querry)
		if validation:
			self.submitOwnerButton.config(state=DISABLED)
			#self.displayResults("Success", 40, 0)
			self.makePersonalForm(self.frame)
			self.displayResults("Please Enter Personal Information", 39, 1)

			self.personalEntries[0].insert(0, self.ownerFormData["owner_id"])

			self.submitButton2 = Button(self.frame, text="Submit Personal Data", command=self.finalCallback)
			self.submitButton2.grid(row=50, column=1)

	def finalCallback(self):
		print("FINAL CALLBACK") 
	
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
		baseRow = 2
		self.entries = []
		for text in self.formText:
			self.entries.append(self.makeentry(parent, text, 40, baseRow, [0,1]),)
			baseRow += 1
	
	def makePersonalForm(self, parent):
		self.personalFormText = ["sin", "name", "weight", "eyecolor", "haircolor", "addr", "gender", "birthday"]
		
		baseRow = 30
		self.personalEntries = []
		for text in self.personalFormText:
			self.personalEntries.append(self.makeentry(parent, text, 40, baseRow, [0,1]),)
			baseRow += 1  

	def makeOwnerForm(self, parent):
		self.ownerFormText = ["owner_id", "vehicle_id", "is_primary_owner"]
		baseRow = 20
		self.ownerEntries = []
		for text in self.ownerFormText:
			self.ownerEntries.append(self.makeentry(parent, text, 40, baseRow, [0,1]),)
			baseRow += 1           

