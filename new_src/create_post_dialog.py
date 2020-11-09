from tkinter import *
from tkinter import font
from tkinter.filedialog import askopenfilename
from new_src.databaseOperations import add_post, get_new_post_id, update_last_postid
from PIL import ImageTk, Image
from pickle import dumps, loads


class Create_post_dialog(Frame):
    def __init__(self, parent, user_email):
        super(Create_post_dialog, self).__init__(parent)
        self.parent = parent
        self.user_email = user_email
        self.font_size = font.Font(size=20)
        self.setup_create_post()
        # to hold all the image path the user selects
        # the post element is currently limited to only image per post
        # hence i am using only one image ie image_paths[0] as post image
        self.image_paths = []
        # to hold all the preview images
        self.images_prev = []
        # to hold all the image objects
        self.image_actual = []

    def setup_create_post(self):
        Label(self, text="Create Post", font=self.font_size).pack()
        self.main_frame = Frame(self)
        self.main_frame.pack(fill=X)
        Label(self.main_frame, text="Caption:", font=self.font_size).grid(padx=20)
        self.caption_bar = Entry(self.main_frame, font=self.font_size)
        self.caption_bar.grid(row=0, column=1, padx=20, pady=20)
        Label(self.main_frame, text="Image upload:", font=self.font_size).grid(row=1, column=0, padx=20, pady=20)
        self.image_btn = Button(self.main_frame, text="Browse images", command=self.browse_image_path,
                                font=self.font_size)
        self.image_btn.grid(row=1, column=1, padx=20, pady=20)

        Label(self.main_frame, text="Post type:", font=self.font_size).grid(row=2, column=0, padx=20, pady=20)
        self.type = StringVar(self)
        self.type.set("public")
        self.type_select = OptionMenu(self.main_frame, self.type, "public", "friends")
        self.type_select.grid(row=2, column=1, padx=20, pady=20)

        self.preview_canv_frame = Frame(self)
        self.preview_canv_frame.pack()
        self.okay_btn = Button(self, text="Post", font=self.font_size, command=self.on_post)
        self.okay_btn.pack(padx=20, pady=20)

    def browse_image_path(self):
        image_path = askopenfilename()
        print(image_path)
        if image_path is not None:
            self.image_paths.append(image_path)
            c = Canvas(self.preview_canv_frame, height=100, width=100, bg="green")
            # to align three preview images in a row
            img = self.resize_image(image_path, 100, 100)
            self.image_actual.append(img)
            c.create_image(50, 50, image=img)
            c.grid(row=len(self.images_prev) // 3, column=len(self.images_prev) % 3)
            self.images_prev.append(c)
        else:
            print("No images selected!!")

    def on_post(self):
        post_id = get_new_post_id()
        type = self.type.get()  # get from a box! default for now!
        # add_post(post_id,self.user_email,type,self.caption_bar.get(),0,self.image_paths)
        # using dumps to directly store  all the array as a blob data!
        data = dumps(self.image_paths)
        add_post(post_id, self.user_email, type, self.caption_bar.get(), 0, data)
        print("Posted successfully!!")
        update_last_postid()
        self.destroy()
        self.parent.destroy()

    def resize_image(self, img_path, h, w):
        img = Image.open(img_path)
        img = img.resize((h, w), Image.ANTIALIAS)
        return (ImageTk.PhotoImage(img))

# root=Tk()
# root.geometry('500x500')
# Create_post_dialog(root,"b@gmail").pack()
# root.mainloop()
