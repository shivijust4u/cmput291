from tkinter import *
import quit
import session

class AutoTransactionPage(object):
	"""docstring for ClassName
	
		vehicle( serial_no, maker, model, year, color, type_id )
		owner(owner_id, vehicle_id, is_primary_owner)
		auto_sale( transaction_id,seller_id, buyer_id, vehicle_id, s_date, price )	
	
	"""
	def __init__(self, master):
		frame = Frame(master, width = 500, height = 500)
		frame.grid()
		self.frame = frame		
		self.successor = -1
		
		#This is where the user entered data gets stored
		self.formData = {}
		
		self.formText = ["transaction_id", "seller_id","buyer_id", "vehicle_id","s_date","price", "is_primary_owner"]
        
		#Create the Entry Forms and display them
		self.forms = self.makeForm(frame)

		self.entries[4].insert(20, "(DD-MMM-YY)")

		self.pageTitle = self.makeTitle(frame, "New Auto Transaction", 0, 1)

		self.submitButton = Button(frame, text="Submit", command=self.submitCallBack)
		self.submitButton.grid(row=10, column=1)

		self.homeButton = Button(frame, text="Home", command=self.homeCB)
		self.homeButton.grid(row=10, column=2)

		self.quitButton = Button(frame, text="Quit", command=lambda:quit.quit_callback(self.frame))
		self.quitButton.grid(row=10, column=0)


	def homeCB(self):
		print("Home")
		self.successor = 0

	def submitCallBack(self):
		n=0
		for entry in self.entries:
				self.formData[self.formText[n]] = entry.get()
				n += 1
		#check transaction_id is unique:
		query = "SELECT transaction_id FROM auto_sale where transaction_id = '" + str(self.formData["transaction_id"] )+ "'"
		
		if (self.validateForm(query) and self.checkOwnership()): # Transaction ID is okay
			#id was not in database and can be used
			# prepare statement to insert new row
			
			data = [(self.formData["transaction_id"], self.formData["seller_id"], self.formData["buyer_id"], self.formData["vehicle_id"], self.formData["s_date"],self.formData["price"])]		 	
			session.db.curs.executemany("INSERT INTO auto_sale(transaction_id,seller_id, buyer_id, vehicle_id, s_date, price) " 
					"VALUES(:1, :2, :3, :4, :5, :6)", data)
			self.updateOwner()			
			
			print("Transaction complete")
			
			session.db.connection.commit()
			self.successor = 0;
			self.quit()
		elif( not self.validateForm(query)):
			print("transaction_id already exists")
			
		else:
			print("Seller does not own the vehicle")
		# delete previous owner entry in database
		# update new owner entry in database
         
	def validateForm(self, statement):                  
		rs = session.db.execute_sql(statement)
		print("rs: "+ str(rs))              
		if not rs:      
			print("NONE")           
			return True
		else: return False
	
	def checkOwnership(self):
		query = "SELECT * FROM owner where owner_id = " + self.formData["seller_id"] +  " and vehicle_id = " + self.formData["vehicle_id"]  	
		rs = session.db.execute_sql(query)	
		if rs: #seller does own vehicle
			return True
		else:
			return False
	
	def updateOwner(self):
		#delete old owner
		query = "DELETE FROM owner WHERE owner_id = " + self.formData["seller_id"] + " and vehicle_id = " + self.formData["vehicle_id"]
		session.db.passive_update(query)		
		# update new owner
		#owner(owner_id, vehicle_id, is_primary_owner)
		data = [ ( self.formData["buyer_id"], self.formData["vehicle_id"], self.formData["is_primary_owner"] ) ]
		session.db.curs.executemany("INSERT INTO owner(owner_id, vehicle_id, is_primary_owner) " 
					"VALUES(:1, :2, :3)", data)
		
	def makeButton(self, parent, caption, width, row, column):
		button = Button(parent, text=caption, command=submitCallback)
		button.grid(row=row, column=column)
		return button

	def makeentry(self, parent, caption, width, row, column):
		if caption == "is_primary_owner":	
			l = Label(parent, text=caption, width=20, justify=RIGHT).grid(row=3,column=2, sticky=E)

		else:
			Label(parent, text=caption, width=20, justify=RIGHT).grid(row=row,column=column[0])
		entry = Entry(parent)
		if width:
				entry.config(width=width)
		if caption == "is_primary_owner":
			entry.grid(row=3, column=column[1] + 2, sticky=E)
			entry.config(width=5)		
		else:		
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

