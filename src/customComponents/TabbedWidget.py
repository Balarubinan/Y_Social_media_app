from tkinter import *
from src.customComponents.TileButton import TiledButton

class TabbedWidget(Frame):
    def __init__(self,parent,h,w,tab_dir=None,font=None,button_loc="Top"):
        self.h,self.w=h,w
        self.font=font
        self.tab_dir=tab_dir
        super(TabbedWidget, self).__init__(parent)
        self.frames={}
        self.main_frame=Frame(self,bg='yellow')
        self.button_frame=Frame(self,bg='blue')
        self.button_frame.pack(side=tab_dir)
        self.main_frame.pack(side=tab_dir)
        # bb=Button(self.main_frame,text="tthis").pack()
        # bb1=Button(self.button_frame,text="tthis").pack()
        self.buttons={}
        self.current_frame=None

    def get_tab_area(self):
        return self.main_frame

    def add_tab(self,name,frame):
        stick='left'
        if self.tab_dir=='left':
            stick=''
        self.temp=self.current_frame
        if self.temp is not None:
            self.temp.pack_forget()
        but = TiledButton(self.button_frame, text=name, command=self.resolve_click(name), h=self.h, w=self.w,
                          font=self.font)
        self.buttons[name] = but
        self.frames[name] =frame
        but.pack(side=stick)
        self.current_frame=self.frames[name]
        self.current_frame.pack()
        # but=Button(self.button_frame,text=name,command=self.resolve_click(name))

    def resolve_click(self,name):
        print("resolve click called")
        def return_click():
            print("Name given is ",name)
            # to not unecssarily  load an aldready loaded window
            if self.current_frame is not self.frames[name]:
                self.current_frame.pack_forget()
                self.frames[name].pack()
                self.current_frame=self.frames[name]
                print("Called")
        return return_click

# driver code
# root=Tk()
# from tkinter import font
# w=TabbedWidget(root,h=25,w=70,font=font.Font(size=10))
# w.pack()
# f=Frame(w.get_tab_area())
# f2=Frame(w.get_tab_area())
# Label(f2,text="Shittyer").pack()
# Entry(f2).pack()
# Button(f,text="Fuck this").pack()
# w.add_tab(name="f1 frame",frame=f)
# w.add_tab(name="f2 frame",frame=f2)
# root.mainloop()



