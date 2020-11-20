from tkinter import *
from tkinter import font
from new_src.customComponents.TabbedWidget import TabbedWidget
from new_src.login_page import Login_form,set_child_1
from new_src.sign_up_form import Sign_up_page
from new_src.feed_main_page import Feed_page
from new_src.utility import change_in_window
from new_src.secondary_main import setup_secondary_tabbed_widget
from new_src.session_handler import get_current_user_info

root=Tk()
root.title("Social media-ish App")
root.geometry("800x600")
w=TabbedWidget(root,25,300,font=font.Font(size=15))
w.pack()
set_child_1(w)

login_tab=Login_form(w.get_tab_area(),root)

# change root to w.get_tab_area()
# due to the custom widget property!

sign_up_tab=Sign_up_page(w.get_tab_area())
w.add_tab("login",login_tab)
w.add_tab("Sign up",sign_up_tab)
# Button(login_tab,text="Auto sigin ",command=call_change).pack()
root.mainloop()