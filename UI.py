from tkinter import *
root = Tk()
enter = Entry(root)
enter.pack()
from OScript import *
def runbtn():
    entcmd = enter.get()
    main(entcmd)
run = Button(root, text = "Run Script!", command = runbtn)
run.pack()
root.mainloop()



