import subprocess
from Tkinter import *
import threading
import subprocess




labelList = list()

def scan():
    output = subprocess.check_output(("arp", "-a"))
    for line in output.splitlines():
        print(line)
        list = str(line).split(' ')
        label = Label(root, text="Device Name: "  + list[0] + "; Hardware Address: " + list[3] + " is active at IP: " + list[1], fg="green4", borderwidth = 2, relief = "groove")
        labelList.append(label)
        label.pack()



def button1():
    threading.Thread(target=scan).start()

def button2():
    for label in labelList:
        label.destroy()


root = Tk()
root.title("Network Scanner")
root.geometry("650x650")
frame = Frame(root,width=1000,height=1000,bd=2,relief=GROOVE)
frame.pack()

button1 = Button(frame, text = "Scan Your Network", command = button1)
button2 = Button(frame, text = "Clear Screen", command = button2)
button1.pack()
button2.pack()

root.mainloop()