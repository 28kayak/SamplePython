from Tkinter import *
#Error: Frame is not defined 
class Application(Frame):
    def say_hi(self):
        print "Hi, there, everyone!"
    def createWindgets(self):
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        
        self.QUIT.pack({"side":"left"})
        
        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi
        
        self.hi_there.pack({"side":"left"})
    
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

root = Tk()#create an instance of Tkinter 
app = Application(master = root)# create an instance of Application class
app.mainloop()#where does this come from?
root.destroy()#a function in Tkinter class