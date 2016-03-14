from Tkinter import *
from main_menu import MainMenu
from vehicle_registration import VehicleRegPage
from search_engine import MainSearchPage, GeneralSearchPage, ViolationsSearchPage, VehicleHistorySearchPage
from auto_transaction import AutoTransactionPage
from violation_record import ViolationRecordPage
from driver_licence import DriverLicencePage

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


root = Tk()


page = MainMenu(root)


#search = SearchPage(root)

#main.quit()

#newpage = VehicleRegPage(root)


def task():
    global page
    
    if page.successor != -1:
        if page.successor == 0:
            page.quit()
            page.successor = -1 # Reset flag
            page = MainMenu(root)

        if page.successor == 1:
            page.quit()
            page.successor = -1 # Reset flag
            page = VehicleRegPage(root)

        elif page.successor == 2:
            page.quit()
            page.successor = -1 # Reset flag
            page = AutoTransactionPage(root)

        elif page.successor == 3:
            page.quit()
            page.successor = -1 # Reset flag
            page = DriverLicencePage(root)

        elif page.successor == 4:
            page.quit()
            page.successor = -1 # Reset flag
            page = ViolationRecordPage(root)

        elif page.successor == 5:
            page.quit()
            page.successor = -1 # Reset flag
            page = MainSearchPage(root)

        elif page.successor == 6:
            page.quit()
            page.successor = -1 # Reset flag
            page = GeneralSearchPage(root)

        elif page.successor == 7:
            page.quit()
            page.successor = -1 # Reset flag
            page = ViolationsSearchPage(root)

        elif page.successor == 8:
            page.quit()
            page.successor = -1 # Reset flag
            page = SearchVehicleHistory(root)

    root.after(700, task)  # reschedule event in 1 seconds

root.after(700, task)
root.mainloop()


