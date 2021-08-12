import tkinter.messagebox as mb
from tkinter import *  # 同时载入两个库，优先使用 ttk，如果没有再用 tkinter
from tkinter.ttk import *  #

win = Tk()
win.title("开方计算")
win.geometry("300x400")
win.resizable(0, 0)

label1 = Label(win, text="输入数字：")
label1.place(x=8, y=8, width=64, height=21)

entry1 = Entry(win)
entry1.place(x=72, y=8, width=220, height=21)

label2 = Label(win, text="选择被开方数的乘方：")
label2.place(x=8, y=37, width=124, height=21)

list1 = Listbox(win)
for i in range(49):
    list1.insert(END, i + 2)
list1.place(x=132, y=37, width=160, height=94)


def calculate(entry: Entry, listbox: Listbox):
    num1 = entry.get()
    num2 = listbox.get("active")

    try:
        num1 = int(num1)
        num2 = int(num2)
    except ValueError:
        mb.showerror(title="类型错误", message="请检查是否输入了正确的数字")
        return None

    result = pow(num1, 1 / num2)
    mb.showinfo(title="计算完毕", message=result)


button1 = Button(win, text="开始计算", command=lambda: calculate(entry1, list1))
button1.place(x=206, y=139, width=87, height=27)

win.mainloop()
