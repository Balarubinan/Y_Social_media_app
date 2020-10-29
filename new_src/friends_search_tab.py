from tkinter import *
from tkinter import font
from threading import Thread
from new_src.databaseOperations import *
from new_src.session_handler import get_current_user_info,get_info_dict

class Friend_search(Frame):
    def __init__(self,parent):
        super(Friend_search, self).__init__(parent)
        self.set_up_search_frame()

    def set_up_search_frame(self):
        self.search_bar=Entry(self,font=font.Font(size=20))
        self.search_bar.pack()
        self.result_frame=Frame(self)
        self.result_frame.pack()
        self.results={}
        self.t=Thread(target=self.start_fetching)
        self.t.start()

    def start_fetching(self):
        # self.add_result()
        self.prev='^'
        while(True):
            self.res=[]
            search_str=self.search_bar.get()
            if search_str==self.prev:
                pass
            elif search_str is not '':
                self.res=fetch_starts_with(search_str)
                # [(we,wewe,wew)]
                for x in self.results:
                    print(self.results)
                    print("destroyed ", x)
                    # print(self.results)
                    self.results[x].destroy()
            self.prev=search_str
            for x in self.res:
                    self.add_result(x[0],x[1],x[2])



    def add_result(self,name,picture,email):
        print(name,picture)
        temp=Frame(self.result_frame)
        c=Canvas(temp,height=50,width=50,bg='lightgreen')
        c.pack(side=LEFT)
        # img=PhotoImage(file=picture)
        # c.create_image(0,0,image=img)
        Label(temp,text=name,font=font.Font(size=15)).pack(side=LEFT)
        Button(temp,text="Add friend",font=font.Font(size=10),command=self.add_friend_button(email)).pack(side=RIGHT,padx=70)
        temp.pack()
        self.results[name]=temp
        print(self.results)

    def add_friend_button(self,email):
        def add_friend_button_clicked():
            info_dict=get_info_dict(get_current_user_info())
            add_to_request(info_dict['email'],email)
            print("function called!!")
        return add_friend_button_clicked

root=Tk()
w=Friend_search(root)
w.pack()
root.mainloop()
