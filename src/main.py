from src.customComponents.TabbedWidget import TabbedWidget
from tkinter import *
from src.login_page_copy import set_up_login


root=Tk()
root.geometry('850x500')
set_up_login(root)
root.mainloop()