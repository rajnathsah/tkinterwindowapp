# import tkinter and tkinter.ttk to override and use ttk widgets
from tkinter import *
from tkinter.ttk import *

from main_window import MainWindow

class Login(Frame):
    '''
    Login form
    '''
    def __init__(self, master=None):
        '''
        Initialize frame
        '''
        Frame.__init__(self, master)        
        self.grid()        

        self.master.title('Login')

        self.winLabel = Label(master, text="Login")
        self.winLabel.grid(row=1, column=1)
        
        self.winLabel = Label(master)
        self.winLabel.grid(row=2, column=1)        

        self.nunameLabel = Label(master, text="User Name")
        self.nunameLabel.grid(row=4, column=0)

        self.nuname = StringVar()
        self.nunameEntry = Entry(master, textvariable=self.nuname)
        self.nunameEntry.grid(row=4, column=1)
                        
        self.npwdLabel = Label(master, text="Password")
        self.npwdLabel.grid(row=5, column=0)

        self.npwd = StringVar()
        self.npwdEntry = Entry(master, show='*', textvariable=self.npwd)
        self.npwdEntry.grid(row=5, column=1)               

        self.button = Button(master, text = "Submit", command=self.openMainWindow)
        self.button.grid(row = 6, column = 1)  
        

    def openMainWindow(self):
        '''
        openMainWindow function closes login window and opens main window
        '''
        self.master.destroy()
        mainroot = Tk()    
        # set size of main window in maximize state
        mainroot.state('zoomed')
        MainWindow(mainroot)    
        mainroot.mainloop()      
  

# main methods start the program
if __name__ == '__main__':    
    loginRoot = Tk()
    # set default size
    loginRoot.geometry("250x150+300+300")
    # disable maximize option
    loginRoot.resizable(0,0)
    # set position in middle of screen
    loginRoot.eval('tk::PlaceWindow . center')    
    Login(loginRoot)    
    loginRoot.mainloop()    
