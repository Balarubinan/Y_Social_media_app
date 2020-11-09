from tkinter import *
from tkinter import font
from PIL import ImageTk,Image
from new_src.customComponents.TileButton import TiledButton
from pickle import loads

class Multiple_image_view(Frame):
    # the image_paths recieved here must the dumps(image_paths) given directly!
    def __init__(self,parent,image_paths):
        super().__init__(parent)
        self.images=[]
        self.img=None
        # holds the current image index shown by the viewer
        self.cur_img = 0
        self.image_paths=image_paths
        self.image_canvas=[]
        self.left_btn=TiledButton(self,50,100,text="<--",font=font.Font(size=20),command=self.on_leftbtn)
        self.left_btn.pack(side=LEFT)
        self.main_canvas=Canvas(self,height=500,width=500,bg="lightblue")
        self.main_canvas.pack(side=LEFT)
        self.right_btn=TiledButton(self,50,100,text="-->",font=font.Font(size=20),command=self.on_rightbtn)
        self.right_btn.pack(side=LEFT)
        self.load_images()
        self.setup_multiview()

    def load_images(self):
        print(self.image_paths)
        for x in self.image_paths:
            # try:
            # y=loads(x)
            img = self.resize_image(x, 500, 500)
            self.images.append(img)
            # except:
            #     print("a loads error occured!")
        print(self.images)

    def setup_multiview(self):
        # intialise only one image here!!!
        # and just update the cur_img pointer to +1 on right and -1 on left!!
        if self.img is not None:
            self.main_canvas.delete(self.pointer)
        # not efficient as each time a new image object is created!
        # self.img=self.resize_image(self.image_paths[self.cur_img],500,500)
        # self.pointer=self.main_canvas.create_image(250,250,image=self.img)

        # more efficient as it uses aldready loaded images
        # print(self.images[self.cur_img])
        self.pointer=self.main_canvas.create_image(250,250,image=self.images[self.cur_img])


    def on_leftbtn(self):
        self.cur_img-=1
        if self.cur_img<0:
            self.cur_img=len(self.image_paths)-1
        self.setup_multiview()

    def on_rightbtn(self):
        self.cur_img+=1
        if self.cur_img >=len(self.image_paths):
            self.cur_img = 0
        self.setup_multiview()

    def resize_image(self, img_path, h, w):
        img = Image.open(img_path)
        img = img.resize((h, w), Image.ANTIALIAS)
        return (ImageTk.PhotoImage(img))

# root=Tk()
# Multiple_image_view(root,["C:\\Users\\Balarubinan\\Desktop\\thumbnails\\classes_demo.png",
#                           "C:\\Users\\Balarubinan\\Desktop\\thumbnails\\context.jpg",
#                           "C:\\Users\\Balarubinan\\Desktop\\thumbnails\\CPVSCOMP.png"]).pack()
# # works perfectly!!!
# root.mainloop()
#
#
