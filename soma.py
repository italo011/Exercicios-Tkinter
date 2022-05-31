from tkinter import *

def diminuir():
    if lb1['text'] > -10:
        lb1['text'] -=1
    else:
        pass


def aumentar():
    if lb1['text'] < 10:
        lb1['text'] += 1
    else:
        pass

root = Tk()
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)




lb1 = Label(root, text=0, padx=20, pady=10, width=3, font='Arial 26')
btn1 = Button(root,text='-',command=diminuir, padx=10, pady=10, width=3, font='Arial 30')
btn2 = Button(root,text='+',command=aumentar, padx=10, pady=10, width=3, font='Arial 30')



btn1.grid(row=0, column=2, sticky=NSEW)
btn2.grid(row=0, column=0, sticky=NSEW)
lb1.grid(row=0, column=1, sticky=NSEW)





root.mainloop()