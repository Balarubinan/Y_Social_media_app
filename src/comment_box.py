from tkinter import *
from tkinter import font
from threading import Thread
from src.databaseOperations import fetch_comments,add_comment

class Comment_dialog(Frame):
    def __init__(self,parent,user_name,post_id,font_size=15):
        # here the user name is the username of the person who requests the Post
        # post_id is the post_id of the Post that conatins this comment box
        super(Comment_dialog, self).__init__(parent)
        self.font_size=font_size
        self.post_id=post_id
        self.username=user_name
        self.top_frame=Frame(self)
        self.top_frame.pack()
        self.comment_box=Entry(self.top_frame,font=font.Font(size=font_size),width=50)
        self.comment_box.pack(side=LEFT)
        self.comment_okay_btn=Button(self.top_frame,text="Post Comment",font=font.Font(size=10),command=self.button_clicked)
        self.comment_okay_btn.pack(side=LEFT)
        Label(self,text="Comments:").pack()
        self.result_frame=Frame(self)
        self.result_frame.pack()
        # active variable controls the runnning of the loop of the thread
        self.active=True
        # a list to hold all the temporary frames
        self.results=[]

        self.load_comments()

    def load_comments(self):
        """loads all the previously given comments for the particular post"""
        res=fetch_comments(self.post_id)
        print("res returned ",res)
        for id,comment,username in res:
            if (id,comment,username) not in self.results:
                t=Frame(self.result_frame)
                Label(t,text=username,font=font.Font(size=10)).pack()
                Label(t,text=comment,font=font.Font(size=15)).pack()
                t.pack(padx=10,side=TOP)
            self.results.append((id,comment,username))

    def button_clicked(self):
        # clearing funtion doesn't work! check on that!!
        add_comment(self.post_id,self.comment_box.get(),self.username)
        self.load_comments()
        self.comment_box['text']=""


# root=Tk()
# w=Comment_dialog(root,"Mr.Balarubinan",1)
# w.pack()
# root.mainloop()

