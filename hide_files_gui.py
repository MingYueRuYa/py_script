# coding utf-8
from tkinter import *
import os

# installed_packages = pip.get_installed_distributions()

# app = Tk()
# label = Label(text='python Packages', font=('Hack', 20, 'bold'))
# label.pack()

# listbox = Listbox(bg='#f2f2f2', fg='red')
# for i in range(1,10):
    # listbox.insert(END, i);
# listbox.pack()

# app.mainloop()

app = Tk()
label = Label(text='all files', font=('hack', 20, 'bold'))
label.pack()

listbox = Listbox(bg='#f2f2f2', fg='red')
path = 'E:/'
files = os.listdir(path)
for f in files:
    listbox.insert(END, f);
listbox.pack(fill=BOTH, expand=True)

app.mainloop()

