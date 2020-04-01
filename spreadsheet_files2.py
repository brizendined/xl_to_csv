# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:35:27 2020

@author: d_bri
"""
from tkinter import *
from tkinter import filedialog
import xl_to_csv as xc

root = Tk()
root.title('XL to csv')
root.geometry("400x200")
root.iconbitmap('icons/Iconicon-Alpha-Magnets-Letter-d.ico')



def open_file():
    root.filename=filedialog.askopenfilename(initialdir="/Users/d_bri/.spyder-py3",
                                         title="Select Source File",
                                         filetypes=(("Excel files","*.xlsx"),))
                                                    #("csv files","*.csv"),
                                                    #("any file","*.*")))

    my_label=Label(root, text=root.filename).pack()
    global infile
    infile=root.filename
    

   
    
def save_file():
    root.savefile=filedialog.asksaveasfilename(initialdir="/Users/d_bri/.spyder-py3",
                                               title="Save As",
                                               defaultextension='.csv',
                                               filetypes=(("CSV Files","*.csv"),))
    
    save_label=Label(root,text=root.savefile).pack()
    global outfile
    outfile=root.savefile
    
def makefile():
    try:
        xc.make_csv(infile,outfile)
    except NameError:
        print('Could not find file')
    


btn=Button(root, text="Source File", command=open_file).pack()

save_btn=Button(root, text='Target File', command=save_file).pack()

btn_submit=Button(root,text='Submit', command=makefile).pack()








root.mainloop()