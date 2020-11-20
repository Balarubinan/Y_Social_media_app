from tkinter import *
from threading import *
from tkinter import font
from new_src.post_element import Post_element
# use the above import if in the other directory!
# from src.post_element import Post_element
from new_src.databaseOperations import fetch_user_posts,fetch_friends
from new_src.customComponents.Custom_Scrollable_Frame_widget import ScrollableFrame
from new_src.create_post_dialog import Create_post_dialog

class Feed_page(Frame):
    def __init__(self,parent,user_email):
        self.user_email=user_email
        super(Feed_page, self).__init__(parent)
        self.main_frame=ScrollableFrame(self,100,150)
        self.bottom_frame=Frame(self)
        self.main_frame.pack(fill=X)
        self.bottom_frame.pack(fill=X)
        self.set_up_feed_page()
        Button(self.bottom_frame, text="Create Post", font=font.Font(size=20),
               command=self.on_create_post_clicked).pack(side=LEFT, fill=X)
        Button(self.bottom_frame, text="Refresh", font=font.Font(size=20), command=self.on_refresh_clicked).pack(
            side=RIGHT, fill=X)

    def set_up_feed_page(self):
        self.res=fetch_user_posts([x[0] for x in fetch_friends(self.user_email)])
        print(self.res)
        self.frames=[]
        for post_id,posted_by,type,caption,likes,images_id in self.res:
            # f=Post_element(self.main_frame)
            f=Post_element(self.main_frame,posted_by=posted_by,type=type,image=images_id,caption=caption)
            f.intialise_using_id(self.user_email, post_id)
            # f.pack(fill=X)
            f.set_up_post()
            self.frames.append(f)
            self.main_frame.insert_frame_end(f)


    def on_refresh_clicked(self):
        # clearing all the items in the feed shown
        for x in self.frames:
            x.destroy()

        # for x in self.bottom_frame.winfo_children():
        #     x.destroy()

        # loading new contents into the frame
        self.set_up_feed_page()

    def on_create_post_clicked(self):
        self.pop_up=Tk()
        # grabset not working!
        # self.pop_up.grab_set()
        Create_post_dialog(self.pop_up,"b@gmail").pack()
        self.pop_up.mainloop()
        # self.pop_up.grab_release()

# root=Tk()
# # Feed_page(root,'rick@gmail.com').pack()
# Feed_page(root,'rick@gmail.com').pack()
# # finish up ths GUI and finsih the whole damn project!
# root.mainloop()

