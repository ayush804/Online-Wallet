import sys
try:
    from Tkinter import *
except ImportError:
    from tkinter import *
try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1
def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
def destroy_window():
    global top_level
    top_level.destroy()
    top_level = None
if __name__ == '__main__':
    import submit
    submit.vp_start_gui()