import subprocess
import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=643
        height=472
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_629=tk.Label(root)
        ft = tkFont.Font(family='Arial',size=33)
        GLabel_629["font"] = ft
        GLabel_629["fg"] = "#333333"
        GLabel_629["justify"] = "center"
        GLabel_629["text"] = "Gender Recognition by Voice"
        GLabel_629.place(x=30,y=10,width=571,height=93)

        GButton_730=tk.Button(root)
        GButton_730["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_730["font"] = ft
        GButton_730["fg"] = "#000000"
        GButton_730["justify"] = "center"
        GButton_730["text"] = "Recorder"
        GButton_730.place(x=260,y=170,width=143,height=43)
        GButton_730["command"] = self.GButton_730_command

        GButton_973=tk.Button(root)
        GButton_973["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_973["font"] = ft
        GButton_973["fg"] = "#000000"
        GButton_973["justify"] = "center"
        GButton_973["text"] = "Database"
        GButton_973.place(x=260,y=240,width=143,height=43)
        GButton_973["command"] = self.GButton_973_command

        GButton_837=tk.Button(root)
        GButton_837["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Arial',size=10)
        GButton_837["font"] = ft
        GButton_837["fg"] = "#000000"
        GButton_837["justify"] = "center"
        GButton_837["text"] = "Exit"
        GButton_837.place(x=260,y=310,width=143,height=43)
        GButton_837["command"] = self.GButton_837_command

    def GButton_730_command(self):
        root.destroy()
        subprocess.Popen(["python", "recorder.py"])

        subprocess.Popen(["python", "LiveGraph.py"])









    def GButton_973_command(self):
        root.destroy()
        subprocess.run(["python", "database.py"])

    def GButton_837_command(self):
        root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
