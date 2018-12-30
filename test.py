from tkinter import *

tk = Tk()

frame1 = Frame(tk)
frame2 = Frame(tk)

b1 = Label(frame1, text='test')
b2 = Label(frame2, text="test 2")

b1.pack()
b2.pack()
b1.lift()

tk.mainloop()