import tkinter as tk
from tkinter import Text, filedialog
import os

root = tk.Tk()
apps = []


def addApp():
    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(
        initialdir="/", title="select command", filetypes=(("executables", "*.exe"), ("all files", "*.*")))

    apps.append(filename)
    print(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()


def runApps():
    for app in apps:
        os.startfile(app)


canvas = tk.Canvas(root, heigh=700, width=700, bg="#4354da")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="open file", padx=10,
                     pady=5, fg="white", bg="#555562", command=addApp)
openFile.pack()
runApps = tk.Button(root, text="open apps", padx=10,
                    pady=5, fg="white", bg="#543462", command=runApps)
runApps.pack()


root.mainloop()
