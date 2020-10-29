from tkinter import *
from tkinter import font
from new_src.customComponents.TabbedWidget import TabbedWidget
from new_src.login_page import Login_form
from new_src.sign_up_form import Sign_up_page

root=Tk()
w=TabbedWidget(root,25,300,font=font.Font(size=15))
w.pack()
login_tab=Login_form(root)

# change root to w.get_tab_area()
# due to the custom widget property!

sign_up_tab=Sign_up_page(root)
w.add_tab("login",login_tab)
w.add_tab("Sign up",sign_up_tab)
root.mainloop()