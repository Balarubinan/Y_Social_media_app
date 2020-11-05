# This is a Custom widget capabale of containing many frames(Sub custom widgets)
# inside a single scrollable Frame containing a parent canvas
from tkinter import *


class ScrollableFrame(Frame):
    def __init__(self, parent, spacing, margin):
        super(ScrollableFrame, self).__init__(parent)
        self.last_end = 0
        self.spacing = spacing
        self.margin = margin
        self.canv = Canvas(self, bg='lightgreen', height='300', width='500', scrollregion=(0, 0, 0, 1000))

        # to use scrollbar
        self.scrollbar = Scrollbar(self, orient="vertical", command=self.canv.yview)
        self.canv.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side="right", fill="y")

        self.canv.pack()
        self.canv.bind_all("<MouseWheel>", self.on_mouse_wheel)
        self.frames = []

    def insert_frame_end(self, frame):
        self.frames.append(frame)
        frame.update()
        self.canv.create_window((self.margin, self.last_end), window=frame)
        self.last_end+=frame.winfo_reqheight()
        # self.last_end += (self.spacing + frame.winfo_reqheight())
        # total_occupied=len(self.frames)*frame.winfo_reqheight()
        # # total_occupied=sum([x.winfo_reqheight() for x in self.frames])
        # if total_occupied>self.canv.winfo_height():
        #     prev = self.canv['scrollregion']
        #     print(prev[6])
        #     self.canv['scrollregion'] = (0, 0, 0, int(prev[6]) + self.spacing + frame.winfo_reqheight())

    def insert_frame_beg(self):
        pass

    def on_mouse_wheel(self, event):
        # -1 is for direction inversion
        self.canv.yview_scroll(-1 * (event.delta // 200), "units")

    def remove_frame(self,frame_object):
        for x in self.frames:
            if x is frame_object:
                x.destroy()
                self.frames.remove(x)



# root = Tk()
# sr = ScrollableFrame(root, 100, 60)
# sr.pack()
# # Tk.update(fr)
# # print(fr.winfo_reqheight())
# for x in range(100):
#     fr = Frame()
#     label = Label(fr, text="Hello text")
#     label.pack()
#     entry = Entry(fr)
#     entry.pack()
#     sr.insert_frame_end(fr)
#
# root.mainloop()
