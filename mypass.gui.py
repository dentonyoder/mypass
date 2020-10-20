#!/usr/bin/env python3
"""
Author : denton <denton@localhost>
Date   : 2020-09-13
Purpose: hash a phrase
"""

from tkinter import *
import hashlib

def myGenerate():
	ans = eb2.get() + eb1.get()
	# use selected hash
	if rbvar.get() == 1 : ans = hashlib.sha1(ans.encode('utf8')).hexdigest().upper()
	elif rbvar.get() == 2 : ans = hashlib.sha256(ans.encode('utf8')).hexdigest().upper()
	elif rbvar.get() == 3 : ans = hashlib.sha512(ans.encode('utf8')).hexdigest().upper()
	# truncate to selected length
	if rbvar2.get() == 2 : ans = ans[0:40]
	elif rbvar2.get() == 3 : ans = ans[0:20]
	elif rbvar2.get() == 4 : ans = ans[0:10]
	
	ans2 = eb3.get() + ans + eb4.get()
	eb5.delete(0,END)
	eb5.insert(0,ans2)

def myClearForm():
	eb1.delete(0,END)
	eb2.delete(0,END)
	eb3.delete(0,END)
	eb4.delete(0,END)
	eb5.delete(0,END)

def hidesecret():
	if var1.get() == 1 : eb1["bg"] = "black"
	else: eb1["bg"] = "white"
	
def hideservice():
	if var2.get() == 1 : eb2["bg"] = "black"
	else: eb2["bg"] = "white"
	
def hideprefix():
	if var3.get() == 1 : eb3["bg"] = "black"
	else: eb3["bg"] = "white"

def hidesuffix():
	if var4.get() == 1 : eb4["bg"] = "black"
	else: eb4["bg"] = "white"
	
def hideans():
	if var5.get() == 1 : eb5["bg"] = "black"
	else: eb5["bg"] = "white"
	
#def sel():
	#print("Hash ")
	#print(rbvar.get())
	#print(" limited to ")
	#print(rbvar2.get())
	
def myClearCache():
	import time
	import random
	for i in range (30) :
		os.system('echo ' + str(random.randint(1,65360)) + '| clip')
		time.sleep(0.2)




  

# Define the main form
f1 = Tk()
f1.title("mypass.gui by: Denton Yoder denton@vt.edu v:1.2")

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var5 = IntVar()

# Add text labels... 
lab1 = Label(f1,text="Secret").grid(row=0,column=0)
lab2 = Label(f1,text="Service").grid(row=1,column=0)
lab3 = Label(f1,text="Prefix").grid(row=2,column=0)
lab4 = Label(f1,text="Suffix").grid(row=3,column=0)
lab5 = Label(f1,text="Hash").grid(row=4,column=0)

#Add and place edit boxes.  They can't be pushed directly like above, or they then can't be edited...
eb1 = Entry(f1)
eb1.grid(row=0,column=1)

eb2 = Entry(f1)
eb2.grid(row=1,column=1)

eb3 = Entry(f1)
eb3.grid(row=2,column=1)

eb4 = Entry(f1)
eb4.grid(row=3,column=1)
eb4.insert(0,".H0k")

eb5 = Entry(f1)
eb5.grid(row=4,column=1)

#Add obfuscate option.
cb1 = Checkbutton(f1, text="Hide",variable=var1, command = hidesecret)
cb1.grid(row=0, column=2)

cb2 = Checkbutton(f1, text="Hide",variable=var2, command=hideservice)
cb2.grid(row=1, column=2)

cb3 = Checkbutton(f1, text="Hide",variable=var3, command=hideprefix)
cb3.grid(row=2, column=2)

cb4 = Checkbutton(f1, text="Hide",variable=var4, command=hidesuffix)
cb4.grid(row=3, column=2)

cb5 = Checkbutton(f1, text="Hide",variable=var5, command=hideans)
cb5.grid(row=4, column=2)

#Add hash types
lab6 = Label(f1,text="  Hash Type  ").grid(row=0,column=3)

rbvar = IntVar()
rb1 = Radiobutton(f1, text = "Sha1", variable = rbvar, value = 1)
rb1.grid(row=1,column=3)
rb1.select()
rb2 = Radiobutton(f1, text = "Sha256", variable = rbvar, value = 2)
rb2.grid(row=2,column=3)
rb3 = Radiobutton(f1, text = "Sha512", variable = rbvar, value = 3)
rb3.grid(row=3,column=3)

#Add max length
lab7 = Label(f1,text="Max length").grid(row=0,column=4)
rbvar2 = IntVar()
rb4 = Radiobutton(f1,text="None", variable = rbvar2, value = 1)
rb4.grid(row=1,column=4)
rb5 = Radiobutton(f1,text="40", variable = rbvar2, value = 2)
rb5.grid(row=2,column=4)
rb5.select()
rb6 = Radiobutton(f1,text="20", variable = rbvar2, value = 3)
rb6.grid(row=3,column=4)
rb7 = Radiobutton(f1,text="10", variable = rbvar2, value = 4)
rb7.grid(row=4,column=4)
	
# Add control buttons.
but1 = Button(f1, text="Generate",command=myGenerate)
but1.grid(row=0, column=5)

but2 = Button(f1, text="Clear Form",command=myClearForm)
but2.grid(row=1, column=5)

import os
if os.name == "nt" :
	but3 = Button(f1, text="Clear Cache", command=myClearCache)
	but3.grid(row=2,column=5)


f1.mainloop()

