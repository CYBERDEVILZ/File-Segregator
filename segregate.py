import platform
import os
import tkinter as tk
from tkinter import Tk, font
from tkinter.constants import LEFT
from tkinter.filedialog import Directory, askdirectory

def windows(dir, ext):
    for folder in ext:
        destPath = "\"" + dir + "/" + folder + "\""
        os.system("mkdir " + destPath)
        for files in ext[folder]:
           final_path = ("\"" + dir + "/" + files + "\" " + destPath).replace("/", "\\")
           os.system("move /Y " + final_path)
        exit(0)
    



def linux(dir, ext):
    for folder in ext:
        destPath = "\"" + dir + "/" + folder + "\""
        os.system("mkdir " + destPath)
        for files in ext[folder]:
            os.system("mv " + "\"" + dir + "/" + files + "\" " + destPath)
        exit(0)

def darwin(dir, ext):
    for folder in ext:
        destPath = "\"" + dir + "/" + folder + "\""
        os.system("mkdir " + destPath)
        for files in ext[folder]:
            os.system("mv " + "\"" + dir + "/" + files + "\" " + destPath)
        exit(0)

def extension_grabber(array):
    ext = {}
    for files in array:
        for index, value in enumerate(files[-1::-1]):
            if value == "." and (index != 0 and index != len(files)-1):
                try:
                    ext[files[len(files)-index:]].append(files)
                except KeyError:    
                    ext[files[len(files)-index:]]=[]
                    ext[files[len(files)-index:]].append(files)
                finally:
                    break
    return ext

def segregate(dir):
    global ext
    listDir = dir.replace('"', '')
    files = os.listdir(listDir)
    ext = extension_grabber(files)
    for i in ext.keys():
        LIST.append(i)
    for i in LIST:
        var = tk.StringVar()
        var.set("1")
        checkbox = tk.Checkbutton(frame2, text=i, variable=var, font = ("Helvetica", 10), padx = 5, pady = 30)
        checkdict[i] = var
        checkbox.pack(side=LEFT)

    

def opendir():
    global PATH
    path = askdirectory()
    if not path:
        return
    else:
        PATH = path
        path_lbl.config(text=PATH)

def find():
    global PATH
    if PATH == "Your folder path appears here...":
        return
    else:
        segregate(PATH)
    
def printme():
    global checkdict
    for i in checkdict.keys():
        print(i)
        if str(checkdict[i].get()) == '0':
            popped = ext.pop(str(i))

    if platform.system() == "Windows":
        windows(PATH, ext)
    
    elif platform.system() == "Linux":
        linux(PATH, ext)
    
    elif platform.system() == "Darwin":
        darwin(PATH, ext)

    else:
        exit(1)


        

    

if __name__ == "__main__":
    ext = {}
    LIST = []
    PATH = "Your folder path appears here..."
    window = tk.Tk()
    window.geometry("800x800")
    window.resizable(0,0)
    window.title("File Segregator")

    title_lbl = tk.Label(window, text = "FILE SEGREGATOR", font = ("Helvetica", 30))
    title_lbl.pack(padx=20, pady=20)

    frame1 = tk.Frame(window)
    frame1.pack()
    dir_btn = tk.Button(frame1, text = "Choose Folder", font = ("Helvetica", 12), command = opendir)
    dir_btn.pack(pady = 20, side=LEFT)

    find_btn = tk.Button(frame1, text = "Find", font = ("Helvetica", 12), command = find)
    find_btn.pack(pady = 20, padx = 20, side=LEFT)

    path_lbl = tk.Label(window, text = PATH, font = ("Helvetica", 12))
    path_lbl.pack()

    checkdict = {}

    frame2 = tk.Frame(window)
    frame2.pack()

    seg_btn = tk.Button(window, text = "BEGIN SEGREGATION!", font=("Helvetica", 15), pady = 40, command = printme)
    seg_btn.pack()


    window.mainloop()
