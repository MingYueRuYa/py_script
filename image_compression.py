# coding utf-8

# 批量resize 图片的大小

from tkinter import *
from tkinter.filedialog import *
from PIL import Image as Img

# 将指定的像素大小存到list变量中
size_list = [50, 100, 120, 180, 512]
info = {
    'path':[]
}

def make_app():
    Label(app, text='Image compress tool', font=('hack', 20, 'bold')).grid(row=0, columnspan=3)
    Listbox(app, name='lbox', bg='#f2f2f2').grid(row=2, column=0)
    Button(app, text ='open', command=ui_getdata).grid(row=2,column=1, columnspan=2)
    Button(app, text='resize', command=resize_pic).grid(row=3,column=1,columnspan=2)
    Label(app, text='Set output path:').grid(row=4, column=0)
    Entry(app, textvariable=out_path).grid(row=4,column=1)
    Button(app, text='Select', command=select_path).grid(row=4,column=2)

    app.geometry('300x400')
    return app

# 获取文件，并将其展示在listbox组件中
def ui_getdata():
    f_names = askopenfilenames()
    lbox = app.children['lbox']
    info['path'] = f_names
    if info['path']:
        for name in f_names:
            lbox.insert(END, name.split('/')[-1])
    return

def resize_pic():
    for f_path in info['path']:
        output = out_path.get()
        os.mkdir(output)
        name = f_path.split('/')[-1]
        image = Img.open(f_path)
        for s in size_list:
            # image.resize(s,s).save(output+str(s)+"_"+name)
            image.resize((s, s)).save(output + str(s) + "_" + name)
    return

# 利用askdirectory函数，选择输出文件路径
def select_path():
    path = askdirectory()
    out_path.set(path)

app = Tk()

# 输出路径是实例化的StringVar对象
out_path = StringVar()

make_app()

app.mainloop()