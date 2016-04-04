'''
Created on Apr 4, 2016

@author: Noe
'''
import Tkinter
import cchatbot


apptittle='Crypto Coin Exchange Chat Bot'

class Gcchat(Tkinter.Tk):
    tsnames = ('C-cex','Bittrex')
    def __init__(self, *args, **kwargs):
        Tkinter.Tk.__init__(self, *args, **kwargs)
        
        container = Tkinter.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage, Ccex, Yobit):
            page_name = F.__name__
            frame = F(container, self)
            self.frames[page_name] = frame
            
            frame.grid(row=0, column=0, sticky='nsew')
            
        
            
        self.show_frame("StartPage")
    

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class StartPage(Tkinter.Frame):

    
        
    
    def __init__(self, parent, controller):
        
        
        Tkinter.Frame.__init__(self, parent)
        self.controller = controller
        label = Tkinter.Label(self, text = apptittle)
        label.pack()
    
    
class Ccex(Tkinter.Frame):

    
        
    
    def __init__(self, parent, controller):
        
        
        Tkinter.Frame.__init__(self, parent)
        self.controller = controller
        label = Tkinter.Label(self, text = apptittle)
        label.pack()    
        
class Yobit(Tkinter.Frame):

    
        
    
    def __init__(self, parent, controller):
        
        
        Tkinter.Frame.__init__(self, parent)
        self.controller = controller
        label = Tkinter.Label(self, text = apptittle)
        label.pack()   
        
#         self.ftitle = Tkinter.Frame(parent, bg='red')
#         self.ftitle.pack()
#         upper buttons Frame
#         self.fubuttons = Tkinter.Frame(parent, bg='yellow')
#         self.fubuttons.pack()
# #         list of text to send area place all 3 text boxes into one frame
#         self.fchat = Tkinter.Frame(parent, bg='white')
#         self.fchat.pack()
# #         self.flts = Tkinter.Frame(parent, bg='white')
# # #         frame for chat messages
# #         self.fcmsgs = Tkinter.Frame(parent, bg='blue')
# #         manual input of text frame 
# #         self.fminput = Tkinter.Frame(parent, bt='yellow')         
#         self.flbuttons = Tkinter.Frame(parent, bg='blue')
#         self.flbuttons.pack()
        
        
                        
        
    
    
if __name__ == '__main__':
    app = Gcchat()
    

    app.mainloop()
    pass