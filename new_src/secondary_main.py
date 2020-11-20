from new_src.customComponents.TabbedWidget import TabbedWidget
from tkinter.font import Font
from new_src.user_settings_page import User_settings
from new_src.friends_main import *
from new_src.feed_main_page import Feed_page

w=None
def setup_secondary_tabbed_widget(parent,user_email):
    global w
    w = TabbedWidget(parent, 25, 300, font=Font(size=15),tab_dir='left')
    w.pack()
    w.add_tab('user setting',User_settings(w.get_tab_area(),user_email))
    w.add_tab('friends page',Friends_main_tab(w.get_tab_area(),user_email))
    w.add_tab('feed page', Feed_page(w.get_tab_area(), user_email))
    return w

