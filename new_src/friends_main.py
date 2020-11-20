from tkinter import *
from new_src.customComponents.TabbedWidget import TabbedWidget
from new_src.friends_request_tab import RequestTab
from new_src.friends_search_tab import Friend_search
from new_src.friends_view_tab import ViewFriends

class Friends_main_tab(Frame):
    def __init__(self,parent,useremail):
        super(Friends_main_tab, self).__init__(parent)
        self.user_email=useremail
        self.setup_friends_tab()

    def setup_friends_tab(self):
        self.main_tab=TabbedWidget(self,h=50,w=100)
        self.main_tab.pack()
        self.main_tab.add_tab('request',RequestTab(self.main_tab.get_tab_area(),self.user_email))
        self.main_tab.add_tab('search', Friend_search(self.main_tab.get_tab_area()))
        self.main_tab.add_tab('view', ViewFriends(self.main_tab.get_tab_area(),self.user_email))

