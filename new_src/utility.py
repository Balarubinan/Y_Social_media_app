from tkinter import *

def change_in_window(upper_parent,child1,child2_func,*child2_params):
    child1.destroy()
    child2=child2_func(upper_parent,*child2_params)
    # child2.pack()
    return child2
