import sys, os  
from tkinter import *
from tkinter import filedialog
from yt_turing import turing_machine_from_file
from yt_turing import tape_from_file
from yt_turing import Tape
import win32ui
 
class Note():
      def __init__(self):  
          self.tk = Toplevel(takefocus=True)
          self.tk.lift(aboveThis=None)
          self.tk.title('编辑')
          self.createUI()  
          self.tk.mainloop()  
 
 
      def createUI(self):  
          menubar = Menu(self.tk)  
          fmenu = Menu(menubar,tearoff=0)  
          fmenu.add_command(label='打开',command=self.open)  
          fmenu.add_command(label='保存',command=self.save)  
          menubar.add_cascade(label="文件", menu=fmenu)  
          self.tk.config(menu=menubar)  
          self.text=Text(self.tk, font = (None, 13))
          self.text.pack()
      
      def save(self):  
        txtContent = self.text.get(1.0,END)  
        self.saveFile(content=txtContent)  
           
 
      def open(self):  
          self.filename = filedialog.askopenfilename(initialdir = '..')  #默认打开位置
          filecontent=self.openFile(fname=self.filename)  
          if filecontent is not -1:  
               self.text.delete(1.0,END)  
               self.text.insert(1.0,filecontent)  

      def openFile(self,fname=None):  
          if fname is None:  
               return -1
          self.fname = fname  
          file = open(fname,'r+')  
          content = file.read()  
          file.close()  
          return content  
 
      def saveFile(self,content=None):  
          if content is None:  
               return -1
          file=open(self.fname,'w')  
          file.write(content)  
          file.flush()  
          file.close()  
          return 0 
 
def mopen():
      dlg = win32ui.CreateFileDialog(1) # 1表示打开文件对话框
      dlg.SetOFNInitialDir('../') # 设置打开文件对话框中的初始显示目录
      dlg.DoModal()
      m_filename = dlg.GetPathName() # 获取选择的文件名称

      global yt_machine
      yt_machine = turing_machine_from_file(m_filename)


def topen():
      dlg = win32ui.CreateFileDialog(1)
      dlg.SetOFNInitialDir('../')
      dlg.DoModal()
      t_filename = dlg.GetPathName()
      global yt_tape 
      yt_tape = t_filename

def run(empty=False):
      tape, yt_str = yt_machine.compute(yt_tape, print_results=True, display_blank_as_empty=empty)

def exit_chile(child):
      child.destroy()
      
def pop_up_help():
      top = Toplevel()
      top.geometry('500x300')
      text = Text(top, font=(None, 13))
      text.insert(END, '请按照template.txt, template_input.txt文件格式输入\n注意：文件中不能出现全角字符\n')
      b1 = Button(text,text='知道了',command=lambda m = top :exit_chile(m))
      text.pack()
      text.window_create(INSERT,window=b1)
    
def editor():
      Note()
