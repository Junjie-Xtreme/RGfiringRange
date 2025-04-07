import tkinter as tk
import math
from tkinter import *
from PIL import Image, ImageTk
from tkinter import Canvas

window = Tk()
window.geometry('1366x768+75+20')  #16:9窗口大小+细调位置
window.title('RoboGrinder Aim Test (Designed by 林俊杰与他的雪豹：张远志)')  #窗口标题
window.iconbitmap('logo32.ico')  #窗口图标，必须使用ico(32x32)格式进行向下重采样，不可用其他图片格式
window.resizable(False, False)  #固定窗口长宽比例

canvas = tk.Canvas(window, width=768, height=768)  #创建画布
pic_file = tk.PhotoImage(file='bazi_xy.png')  #创建图片
pic = canvas.create_image(384, 384,  anchor='center', image=pic_file)

reset_btn_img = tk.PhotoImage(file='reset.png')

tk.Label(window, text='X:').place(relx=0.88, rely=0.45, anchor=CENTER)
x_entry = Entry(window, width=4)
x_entry.pack()
x_entry.place(relx=0.9, rely=0.45, anchor=CENTER)

tk.Label(window, text='Y:').place(relx=0.88, rely=0.5, anchor=CENTER)
y_entry = Entry(window, width=4)
y_entry.pack()
y_entry.place(relx=0.9, rely=0.5, anchor=CENTER)

tk.Label(window, text='Size:').place(relx=0.874, rely=0.55, anchor=CENTER)
z_entry = Entry(window, width=4)
z_entry.pack()
z_entry.place(relx=0.9, rely=0.55, anchor=CENTER)


def paint(x0, y0, z):
    x0 = int(x_entry.get())
    y0 = -int(y_entry.get())
    z = int(z_entry.get())
    x0 += 384
    y0 += 384
    x1 = x0 - (6 if z == 1 else 4)
    y1 = y0 - (6 if z == 1 else 4)
    x2 = x0 + (6 if z == 1 else 4)
    y2 = y0 + (6 if z == 1 else 4)
    z = ('blue' if z == 0 else 'green')
    return canvas.create_oval(x1, y1, x2, y2, fill=z, outline='white')

#class GUI:
  #  def __init__(self, master, x, y):
        #self.master = master
        #self.canvas = tk.Canvas(master, width=x, height=y)
        #self.canvas.pack()
        #self.canvas.create_oval(384, 384, 500, 500, fill='blue', outline='white')
        #self.canvas.create_oval(0, 0, 500, 600, fill='green', outline='white')


#x, y = 500, 500
#gui = GUI(window, x, y)

#canvas.create_oval(384, 384, 389, 389, fill="blue", alpha=.5, outline='white')

paint_btn_img = tk.PhotoImage(file='paint.png')
paint_btn = tk.Button(window, image=paint_btn_img, bd=3, command=lambda: paint(1, 1, 1))  #bd上世纪阴影粗细
paint_btn.place(relx=0.9, rely=0.8, anchor=CENTER)  #relx长位置（0为左，1为右），rely宽位置（0为上，1为下）


reset_btn_img = tk.PhotoImage(file='reset.png')
reset_btn = tk.Button(window, image=reset_btn_img, bd=3, command=lambda: canvas.delete("all"))
reset_btn.place(relx=0.9, rely=0.9, anchor=CENTER)

canvas.pack()
window.mainloop()  #窗口输出

#任务栏RG图标：颜色反转。如果用户任务栏是暗色背景，黑转白。如否，保持。
#打击点半透明，重叠处加深颜色
#可变环数