from http.client import MOVED_PERMANENTLY
import os
import shutil
from tkinter import Button, Entry, Label, Tk

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
ROOT = ".../../GARY"
TARGET_FOLDER = "/2020"
DEST_REPO = "/Bannerz Work/", "/Test/"

def copy_folders():
    root_path = ROOT
    target = TARGET_FOLDER
    folder_list = [ folder[0] for folder in os.walk(root_path) if target in folder[0]]

    for folder in folder_list:
        dest_path = folder.replace(DEST_REPO)
        shutil.copytree(folder, dest_path)

#TODO full path of the root directory where to start walk from
# C:\...\Root_Directory\

#TODO get only target folder name .i.e no back or front slashes

#TODO Path of the Target directory where to save
# C:\...\Target, E:\...\Target

#TODO label to show status
# traversing folders, Moving folder from x to y, x folder already exists

#TODO Also print the status on the terminal


window = Tk()
window.title("Copy Folder")
window.config(padx=50, pady= 50, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

### textbox for root directory
label_root = Label(text="Root Directory")
label_root.grid(column=1, row=1)

txt_root = Entry(width=40)
txt_root.grid(column=2, row=1)
#### TODO Add folder finder buttons to each row

### Entry for target location
label_target_loc = Label(text="Target Folder")
label_target_loc.grid(column=1, row=2)

txt_target = Entry(width=40)
txt_target.grid(column=2, row=2)


### Entry for target forlder
label_target = Label(text="Dest. Directory")
label_target.grid(column=1, row=3)

txt_target = Entry(width=40)
txt_target.grid(column=2, row=3)

### Start Button

btn_start = Button(text="Copy Folder(s)", command= copy_folders)

btn_start.grid(column=1, row=4, columnspan=2)

window.mainloop()




