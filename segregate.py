import platform
import os
import sys

def windows(dir, ext):
    for folder in ext:
        destPath = dir + "\\" + folder
        os.system("mkdir " + dir + "\\" + folder)
        for files in ext[folder]:
            os.system("move /Y " + dir + "\\" + "\"" + files + "\" " + destPath)



def linux(dir, ext):
    for folder in ext:
        destPath = dir + "/" + folder
        os.system("mkdir " + dir + "/" + folder)
        for files in ext[folder]:
            os.system("mv " + dir + "/" + "\"" + files + "\" " + destPath)

def darwin(dir, ext):
    for folder in ext:
        destPath = dir + "/" + folder
        os.system("mkdir " + dir + "/" + folder)
        for files in ext[folder]:
            os.system("mv " + dir + "/" + "\"" + files + "\" " + destPath)

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
    listDir = dir.replace('"', '')
    files = os.listdir(listDir)
    ext = extension_grabber(files)
    print(ext)

    if platform.system() == "Windows":
        windows(dir, ext)
    
    elif platform.system() == "Linux":
        linux(dir, ext)
    
    elif platform.system() == "Darwin":
        darwin(dir, ext)

    else:
        print("Unknown Sytem")
        print("Press any key to exit..")
        x = input()
        exit()


if __name__ == "__main__":
    dir = input("Enter the path(s): ")
    for i in dir.split(','):
        segregate(i.strip())
