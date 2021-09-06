import platform
import os
import tkinter as tk
from tkinter import Tk, font
from tkinter.constants import LEFT
from tkinter.filedialog import askdirectory
from PIL import Image, ImageTk


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
        checkbox = tk.Checkbutton(frame2, text=i, variable=var, font = ("Helvetica", 10), padx = 5, pady = 20, bg = "white")
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
    window.geometry("800x470")
    window.resizable(0,0)
    window.config(bg = "white")
    window.title("File Segregator")

    #----------------------------------- images --------------------------------------#
    image0 = Image.open("./images/file-segegator.png")
    image0 = image0.resize((round(image0.size[0] * 0.5), round(image0.size[1] * 0.5)))
    image0 = ImageTk.PhotoImage(image0)
    image1 = Image.open("./images/segregate-button.png")
    image1 = image1.resize((round(image1.size[0] * 0.28), round(image1.size[1] * 0.28)))
    image1 = ImageTk.PhotoImage(image1)
    image2 = Image.open("./images/choose-folder-button.png")
    image2 = image2.resize((round(image2.size[0] * 0.2), round(image2.size[1] * 0.2)))
    image2 = ImageTk.PhotoImage(image2)
    image3 = Image.open("./images/find.png")
    image3 = image3.resize((round(image3.size[0] * 0.2), round(image3.size[1] * 0.2)))
    image3 = ImageTk.PhotoImage(image3)

    title_lbl = tk.Label(window, image = image0, font = ("Helvetica", 30), bg = "white")
    title_lbl.pack(padx=20, pady=20)

    frame1 = tk.Frame(window, bg = "white")
    frame1.pack()
    dir_btn = tk.Button(frame1, image = image2, borderwidth= 0, command = opendir, bg = "white")
    dir_btn.pack(pady = 20, side=LEFT)

    find_btn = tk.Button(frame1, image = image3, borderwidth= 0, command = find, bg = "white")
    find_btn.pack(pady = 20, padx = 20, side=LEFT)

    none_frm = tk.Frame(window, height = 5, bg = "white")
    none_frm.pack()

    path_lbl = tk.Label(window, text = PATH, font = ("Helvetica", 12), bg = "white", fg = "black")
    path_lbl.pack()

    checkdict = {}

    frame2 = tk.Frame(window, bg = "white")
    frame2.pack()

    none_frm = tk.Frame(window, height = 30, bg = "white")
    none_frm.pack()

    seg_btn = tk.Button(window, image = image1, borderwidth = 0, command = printme, bg = "white")
    seg_btn.pack()


    window.mainloop()
