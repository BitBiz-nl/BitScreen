from tkinter import *
import tkinter as tk
import tkinter
from tkinter import messagebox
import urllib.request  as urllib2
import webbrowser
import os
from pynotifier import Notification
import sys

from infi.systray import SysTrayIcon

def say_hello(systray):
    root = Tk()
def on_quit_callback(systray):
    sys.exit()
menu_options = (("Menu", None, say_hello),)
systray = SysTrayIcon("icon.ico", "BitBizScreenShare is running in your background", menu_options, on_quit=on_quit_callback)
systray.start()


def new_winF():
    newwin = Toplevel(root)
    display = Label(newwin, text="current keybind: f2 or f12")
    display.pack()

    
    print(f.read()) 
def update_window():
    tkinter.messagebox.askokcancel("Info", "You are currently running on " + data + " If there is an update you will be notified");

def new_infobox():
    newwin = Toplevel(root)
    display = Label(newwin, text="Current keybind: f2 or f12")
    display.pack()
    display = Label(newwin, text="After starting the process this window will dissapear, you can then make screenshots.")
    display.pack()

def screenshot():
    root.destroy()
    Notification(
	title='BitBizScreenShare',
	description='BitBiz ScreenShare is now running in your background, use f2 or f12 to make a screenshot',
	icon_path='icon.ico',
	duration=5,
	urgency=Notification.URGENCY_CRITICAL
    ).send()

    from mss import mss
    import ftplib
    import string
    import random



    from pynput import keyboard
    read_keybind = open("key.txt", "r")

    COMBINATIONS = [
        {keyboard.Key.f2},
        {keyboard.Key.f12}
        ]

    current = set()

    def execute():
        with mss() as sct:
            sct.shot()


        def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
            return ''.join(random.choice(chars) for _ in range(size))

        randomstring = id_generator()

        session = ftplib.FTP('','','')
        file = open('monitor-1.png','rb')                  # file to send
        session.storbinary('STOR ' + randomstring + ".png", file)     # send the file
        file.close()                                    # close file and FTP
        session.quit()

        # print("Your link: https://bitbiz.nl/screenshots/" + randomstring + ".png")

        import pyperclip
        pyperclip.copy("https://bitbiz.nl/screenshots/" + randomstring + ".png")
        spam = pyperclip.paste()

    def on_press(key):
        if any ([key in COMBO for COMBO in COMBINATIONS]):
            current.add(key)
            if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
                execute()
    def on_release(key):
        if any([key in COMBO for COMBO in COMBINATIONS]):
            current.remove(key)
    with keyboard.Listener(on_press=on_press, on_release=on_release) as Listener:
        Listener.join()




root = Tk()
root.geometry('600x400')
root.iconbitmap('images/icon.ico')
root.title("BitBiz-Screen")

root.configure(background='white')

text = Label(root, text='Thank you for installing BitBiz-screen', bg="white")
text.pack()
keyb_button = PhotoImage(file='images/button.png')
info_button = PhotoImage(file='images/info.png')
startp_button = PhotoImage(file='images/Start_process.png')
update_button = PhotoImage(file='images/search_updates.png')
stop_button = PhotoImage(file='images/stop_button.png')

button = tk.Button(root, text='Keybinds', bg="white", command =new_winF, relief="flat", image = keyb_button)
button.pack()
button = tk.Button(root, text='Info', command=new_infobox, bg="white", relief="flat", image = info_button)
button.pack()
button = tk.Button(root, text='Start process', command=screenshot, bg="white", relief="flat", image = startp_button)
button.pack()
button = tk.Button(root, text='Search for updates', command=update_window, bg="white", relief="flat", image = update_button)
button.pack()
button = tk.Button(root, text='Stop', command=root.destroy, bg="white", relief="flat", image = stop_button)
button.pack()
process_description = Label(root, text='After starting the process this window will dissapear, you can then use f2 or f12 to make a screenshot', bg='white')
process_description.pack()
from tkinter import messagebox
tkinter.messagebox.showinfo("Info", "This app is currently in development, which means that functions may not work");

os.system("curl https://bitbiz.nl/API/appversion.txt -O")
file = open("appversion.txt", "r")
data = file.read()

text = Label(root, text=(data), bg="white")
text.pack()
if data =="v0.3":
    answer = tkinter.messagebox.askyesno(title='Update', message='There is an update! do you want to update?')
    if answer == True:
        webbrowser.open_new("https://bitbiz.nl/software/updates")


root.mainloop()
