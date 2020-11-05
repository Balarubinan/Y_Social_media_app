from tkinter import *
from threading import *
from tkinter import font
from new_src.post_element import Post_element
# use the above import if in the other directory!
# from src.post_element import Post_element
from new_src.databaseOperations import fetch_user_posts,fetch_friends
from new_src.customComponents.Custom_Scrollable_Frame_widget import ScrollableFrame


class Feed_page(Frame):
    def __init__(self,parent,user_email):
        self.user_email=user_email
        super(Feed_page, self).__init__(parent)
        self.main_frame=ScrollableFrame(self,10,150)
        self.bottom_frame=Frame(self)
        self.main_frame.pack(fill=X)
        self.bottom_frame.pack(fill=X)
        self.set_up_feed_page()

    def set_up_feed_page(self):
        Button(self.bottom_frame,text="Create Post",font=font.Font(size=20),command=self.on_create_post_clicked).pack(side=LEFT,fill=X)
        Button(self.bottom_frame,text="Refresh",font=font.Font(size=20),command=self.on_refresh_clicked).pack(side=LEFT,fill=X)
        self.res=fetch_user_posts([x[0] for x in fetch_friends(self.user_email)])
        print(self.res)
        self.frames=[]
        for post_id,posted_by,type,caption,likes,images_id in self.res:
            # f=Post_element(self.main_frame,posted_by=posted_by,type=type,image=images_id,caption=caption)
            # self.main_frame.insert_frame_end(f)
            f=Post_element(self.main_frame,font_size=20)
            f.intialise_using_id(self.user_email,post_id)
            f.set_up_post()
            self.main_frame.insert_frame_end(f)


    def on_refresh_clicked(self):
        pass

    def on_create_post_clicked(self):
        pass

root=Tk()
Feed_page(root,'b@gmail').pack()

root.mainloop()

