from tkinter import *
from tkinter.ttk import *
import sys

class MainWindow(Frame):
    '''
    main window with menu bar
    '''

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()                

        self.master.title('Main Window')

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)   

        editMenu = Menu(menubar)
        editMenu.add_command(label="Add Item", command=self.subWindow)
        menubar.add_cascade(label="Edit", menu=editMenu)

        helpMenu = Menu(menubar)
        helpMenu.add_command(label="About", command="")
        menubar.add_cascade(label="Help", menu=helpMenu)                
        

    def onExit(self):
        '''
        on click exit close window and exit
        '''        
        self.master.destroy()

    def subWindow(self):
        '''
        sub window using toplevel and set focus on child and disable access to parent window
        '''
        sub = Toplevel(self)
        sub.title("Sub Window")
        sub.geometry("600x300+100+100")        
        sub.focus_force()
        sub.grab_set()
        sub.transient(self)

        self.nunameLabel = Label(sub, text="User Name")
        self.nunameLabel.grid(row=4, column=0)

        self.nuname = StringVar()
        self.nunameEntry = Entry(sub, textvariable=self.nuname)
        self.nunameEntry.grid(row=4, column=1)        

        #sub.grab_release()
        sub.mainloop()


if __name__ == '__main__':    
    root = Tk()
    root.state('zoomed')
    guiFrame = MainWindow(root)    
    root.mainloop()
