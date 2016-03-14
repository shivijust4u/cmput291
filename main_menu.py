from Tkinter import *


class MainMenu(object):
    """docstring for ClassName

        Buttons:
            Register New Vehicle
            New Auto Transaction
            Driver License Registration
            Violation Record
            Search Engine

    """

    def __init__(self, master):
        frame = Frame(master, bg = "white", width = 500, height = 500)
        frame.grid()
        self.frame = frame

        self.successor = -1

        self.buttonText = [
            "Register New Vehicle",
            "New Auto Transaction",
            "Driver License Registration",
            "Violation Record",
            "Search"]

        self.pageTitle = self.makeTitle(frame, "Main Menu", 0, 2)
        self.pageTitle.config(justify=CENTER)

        self.buttons = [self.makeButton(self.frame, self.buttonText[0], 15, 5,0),
                        self.makeButton(self.frame, self.buttonText[1], 15, 5,1),
                        self.makeButton(self.frame, self.buttonText[2], 15, 5,2),
                        self.makeButton(self.frame, self.buttonText[3], 15, 5,3),
                        self.makeButton(self.frame, self.buttonText[4], 15, 5,4),
                        ]

        self.buttons[0].config(command=self.callback0)
        self.buttons[1].config(command=self.callback1)
        self.buttons[2].config(command=self.callback2)
        self.buttons[3].config(command=self.callback3)
        self.buttons[4].config(command=self.callback4)

        self.quitButton = Button(frame, text="Quit", command=frame.quit)
        self.quitButton.grid(row=10, column=2)
   
    def callback0(self):
        print "Register New Vehicle"
        # Kill this frame --> bootup new frame
        self.successor = 1
        self.quit()

    def callback1(self):
        print "New Auto Transaction"
        self.successor = 2
        self.quit()

    def callback2(self):
        print "Driver License Registration"
        self.successor = 3
        self.quit()

    def callback3(self):
        print "Violation Record"
        self.successor = 4
        self.quit()

    def callback4(self):
        print "Search"
        self.successor = 5
        self.quit()

    def quit(self):
        self.frame.destroy()

    def makeButton(self, parent, caption, width, row, column):
        button = Button(parent, text=caption)
        button.grid(row=row, column=column)
        return button

    def makeTitle(self, parent, text, row, column):
        title = Label(parent, text=text)
        title.grid(row=row, column=column)
        return title



