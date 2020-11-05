from tkinter import *
from tkinter import font
from PIL import Image
from threading import Thread
from os import system
from new_src.databaseOperations import *
from PIL import ImageTk
from new_src.comment_box import Comment_dialog

# decide how to set the intial size of the box!


# to create a new post :
# fetch the last post number and then use the create post box to get all the info
# wirte the info directly to the database using the add_post function
# after that intialise a new post_element object using the id just written to the base
# that way we always access a post only after it's been written to the base!
# the user name of the user who requests the post_element then can directly be used to comment on the post!

class Post_element(Frame):
    # type = F,P (F->friends only , P->Public)
    # image refers to image path the image file uploaded to DB
    def __init__(self, parent, posted_by=None, type='F', image=None, caption=None, font_size=15):
        super(Post_element, self).__init__(parent)
        self.type = type
        self.image = image
        self.posted_by = posted_by
        self.caption = caption
        self.font_size = font_size
        self.post_id=None
        # comment when using auto_mode!
        # self.set_up_post()

        # testing purpose

    def set_up_post(self):
        # self.caption_frame=Frame(self)
        if self.caption is None and self.image is None:
            print("Initalising error!")
            self.destroy()
        else:
            # write code here to create user handle!
            # find how to align the handle and to the left!
            self.user_frame = Frame(self)
            self.user_frame.pack()
            # write code to fetch user handle image here and add it to the canvas
            self.canv_user = Canvas(self.user_frame, height=25, width=25, bg='lightgreen')
            # self.user_image=fetch_user_image("somthing like this function!!")
            # self.canv_user.create_image(25//2,25//2,image=self.user_image)

            self.canv_user.pack(side=LEFT)
            Label(self.user_frame, text=fetch_user_name(self.posted_by), font=font.Font(size=self.font_size)).pack(side=LEFT)
            # part to insert the image and the caption of the Post
            if self.caption is not None:
                self.caption_label = Label(self, text=self.caption, font=font.Font(size=self.font_size))
                self.caption_label.pack()
            print(self.image)
            # if self.image is not "NO_IMAGE":
            if len(self.image)>9:
                self.canv = Canvas(self, height=500, width=500)
                self.img = self.resize_image(self.image, 500, 500)
                self.canv.create_image(250, 250, image=self.img)
                self.canv.pack()
            #  creating the like and comment buttons!

            self.button_frame = Frame(self)
            self.button_frame.pack()

            # create image buttons instead of text buttons!!!
            self.comment_button = Button(self.button_frame, text="Comment", font=font.Font(size=self.font_size),
                                         command=self.comment_button_clicked)
            self.comment_button.grid()
            self.like_button = Button(self.button_frame, text="like", font=font.Font(size=self.font_size),
                                      command=self.like_button_clicked)
            self.like_button.grid(row=0, column=1)

            # add a tiled button to let the user view the comments!

    def comment_button_clicked(self):
        # works perfectly!!
        # tk.top_level is another alternative
        self.pop_up=Tk()
        self.comment_box=Comment_dialog(self.pop_up,self.req_user,self.post_id)
        self.comment_box.pack()
        self.pop_up.mainloop()

    def like_button_clicked(self):
        if self.like_button['bg']=="lightblue":
            return
        else:
            increase_like(self.post_id)
            self.like_button['bg']="lightblue"

        # updating the image accordingly!

    def intialise_using_id(self,requested_user,post_id):
        # assuming that the Post aldready exists in the DB
        self.req_user=requested_user
        self.post_id=post_id
        self.post_id,self.posted_by,self.type,self.caption,self.likes,self.images_id=fetch_post_by_id(post_id)
        print(self.post_id,self.posted_by,self.type,self.caption,self.likes,self.images_id)
        # req_user is the one who is viewing the post and hence should be got from outside!

    def write_to_base(self,uploaded_image):
        '''function to save post to the DB'''
        # uploaded image is a path of the selected image and must be passed to this function!
        # fetch the last post_id and update
        # this method is obselete as we aldready would have written the post to the base
        # while using this object!
        pass

    def resize_image(self, img_path, h, w):
        img = Image.open(img_path)
        img = img.resize((h, w), Image.ANTIALIAS)
        return (ImageTk.PhotoImage(img))


# driver code!
# root = Tk()
# w = Post_element(root)
# w.intialise_using_id("Miss.Chizuru",1)
# w.pack()
# w.set_up_post()
# root.mainloop()
