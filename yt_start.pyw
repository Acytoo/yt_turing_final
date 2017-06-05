from yt_ofun import *

root = Tk()
root.geometry('300x157')
root.title('通用图灵机')
root.iconbitmap('yt.ico')

Button(root, text='打开图灵机', width = 10, command=mopen)\
             .grid(row=0, column=0, sticky=W, padx = 10, pady = 5)

Button(root, text='纸带数据', width = 10, command=topen)\
             .grid(row=0, column=2, sticky=W, padx = 10, pady = 5)

Button(root, text='开始执行', width = 10, command=lambda:run(0))\
             .grid(row=1, column=1, sticky=W, padx = 10, pady = 5)

Button(root, text="帮助", width = 10, command=pop_up_help)\
             .grid(row=3, column=0, sticky=W, padx = 10, pady = 5)

Button(root, text='退出', width = 10, command=root.destroy)\
             .grid(row=3, column=2, sticky=W, padx = 10, pady = 5)

Button(root, text='编辑', width = 10, command=editor)\
             .grid(row=2, column=1, sticky=W, padx = 10, pady = 5)

root.mainloop()
