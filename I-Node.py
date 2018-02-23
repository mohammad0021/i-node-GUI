#!/usr/bin/python

__author__="Mohammad_reza"
__date__ ="$December 10, 2017$"


import os, sys

try:
	from Tkinter import *
except:
	os.system("sudo apt-get install python-tk")
	from Tkinter import *

import tkFileDialog, Tkconstants 
import tkMessageBox
import ttk
from stat import *

root = Tk()

root.title('I-nod Show')

Size_file = StringVar()
Size_file.set("1,100")
Search_name_file = StringVar()

Size_file2="2,4"
dirname = ""

def walktree(top):
	global Size_file2
	Size_file2=Size_file.get()
   	for f in os.listdir(top):
		pathname = os.path.join(top, f)
		if int(os.stat(pathname).st_size) > int(Size_file2.split(",")[0]) and os.stat(pathname).st_size < int(Size_file2.split(",")[1]): 
			Lb1.insert(Lb1.size(), f) 

def show_State_Size_file():
	Label(root, text="Size : ").place(x = 55, y = 93)
	Label(root, text=Size_file2).place(x = 100, y = 93)


def Search():
	state=0;
	i=0
	while i < Lb1.size():
		if Lb1.get(i) == Search_name_file.get():
			state=1;
			break;
		i+=1
	if state==1:	
		tkMessageBox.showinfo("Success", "This name has been found.")
	else:
		tkMessageBox.showinfo("Error", "This name could not be found.")
Button(root, text ="Search", command = Search).place(x = 155, y = 55)
Entry(root, bd =2,width=15 ,textvariable=Search_name_file).place(x = 230, y = 60)

def openDirectory():
	global dirname
    	dirname = tkFileDialog.askdirectory(parent=root, initialdir='/home/', title='Select your pictures folder')	
	Label(root, text=dirname).place(x = 155, y = 20)
	walktree(dirname)
	show_State_Size_file()
Button(root, text ="Select Directory", command = openDirectory).place(x = 30, y = 15)


def Show_Information():
	try:
		addr=dirname +"/"+ Lb1.get(int(Lb1.curselection()[0]))
	except:
		tkMessageBox.showinfo("Error", "Select for list")
		return
	print 
	Label(root, text=os.stat(addr).st_mode).place(x = 560, y = 160)
	Label(root, text=os.stat(addr).st_ino).place(x = 540, y = 185)
	Label(root, text=os.stat(addr).st_dev).place(x = 600, y = 210)
	Label(root, text=os.stat(addr).st_nlink).place(x = 500, y = 235)
	Label(root, text=os.stat(addr).st_uid).place(x = 485, y = 260)
	Label(root, text=os.stat(addr).st_gid).place(x = 590, y = 285)
	Label(root, text=os.stat(addr).st_size).place(x = 485, y = 310)
	Label(root, text=os.stat(addr).st_atime).place(x = 570, y = 335)
	Label(root, text=os.stat(addr).st_mtime).place(x = 605, y = 360)
	Label(root, text=os.stat(addr).st_ctime).place(x = 495, y = 385)
	root.minsize(width=765, height=666)



Button(root, text ="Show Information", command = Show_Information).place(x = 480, y = 100) 


def Delete():
	Lb1.delete(Lb1.curselection()[0])
Button(root, text ="Delete For list", command = Delete).place(x = 30, y = 55) 

Label(root, text="Size File (4,8) :").place(x = 375, y = 62)
Entry(root, bd =2,width=15 ,textvariable=Size_file).place(x = 470, y = 60)

# label Information
Label(root, text="protection mode : ").place(x = 445, y = 160)
Label(root, text="Inode number : ").place(x = 445, y = 185)
Label(root, text="Device inode resides on : ").place(x = 445, y = 210)
Label(root, text="NLINK : ").place(x = 445, y = 235)
Label(root, text="UID : ").place(x = 445, y = 260)
Label(root, text="Group id of the owner : ").place(x = 445, y = 285)
Label(root, text="Size : ").place(x = 445, y = 310)
Label(root, text="Time of last access : ").place(x = 445, y = 335)
Label(root, text="Time of last modification : ").place(x = 445, y = 360)
Label(root, text="ctime : ").place(x = 445, y = 385)





# listBox
Lb1 = Listbox(root,width=50,height=33,selectmode=EXTENDED)
Lb1.place(x = 30, y = 110)

root.minsize(width=666, height=666)
root.resizable(width=False, height=False)

root.mainloop()
