from Tkinter import *
from main_menu import MainMenu
from vehicle_registration import VehicleRegPage
from search_engine import MainSearchPage, GeneralSearchPage, ViolationsSearchPage, VehicleHistorySearchPage
from auto_transaction import AutoTransactionPage
from violation_record import ViolationRecordPage
from driver_licence import DriverLicencePage
from log_in import LogInPage
import getpass # the package for getting password from user without displaying it


###---   PROGRAM LOGIC  ---###

#   Boot main menu
#   user makes selection        
#   teardown main menu
#   create new page
#
#
###---  END  ---###

"""
Page Ordering:
    {
    0:"Main Menu", 
    1:"VehicleRegPage", 
    2:"Auto Transaction",
    3:"Driver Licence Registration",
    4:"Violation Record",
    5:"Search Main",
    6:"Search1",
    7:"Search2"
    8:"Search3"
    }
"""



class App(object):
    """docstring for ClassName"""
    def __init__(self):
        self.root = Tk()
        self.root.geometry('{}x{}'.format(1000, 600))
        self.root.wm_title("CMPUT 291 Database Application")

        #self.page = LogInPage(self.root)

        self.page = MainMenu(self.root)

        self.root.after(300, self.mainTask)
        self.root.mainloop()

    def mainTask(self):
        

        if self.page.successor != -1:
            if self.page.successor == 0:
                self.page.quit()
                self.page.successor = -1 # Reset flag
                self.page = MainMenu(self.root)

            if self.page.successor == 1:
                self.page.quit()
                self.page.successor = -1 # Reset flag
                self.page = VehicleRegPage(self.root)

            elif self.page.successor == 2:
                self.page.quit()
                self.page.successor = -1 # Reset flag
                self.page = AutoTransactionPage(self.root)

            elif self.page.successor == 3:
                self.page.quit()
                self.page.successor = -1 # Reset flag
                self.page = DriverLicencePage(self.root)

            elif self.page.successor == 4:
                self.page.quit()
                self.page.successor = -1 # Reset flag
                self.page = ViolationRecordPage(self.root)

            elif self.page.successor == 5:
                self.page.quit()
                self.page.successor = -1 # Reset flag
                self.page = MainSearchPage(self.root)

            elif self.page.successor == 6:
                self.page.quit()
                self.page.successor = -1 # Reset flag
                self.page = GeneralSearchPage(self.root)

            elif self.page.successor == 7:
                self.page.quit()
                self.page.successor = -1 # Reset flag
                self.page = ViolationsSearchPage(self.root)

            elif self.page.successor == 8:
                self.page.quit()
                self.page.successor = -1 # Reset flag
                self.page = VehicleHistorySearchPage(self.root)

        self.root.after(300, self.mainTask)  # reschedule event in 0.3 seconds

    

"""
Main Tkinter Object window
"""

if __name__=="__main__":
    app = App()



