import tkinter as tk

gui = tk.Tk()

gui.geometry("300x400")

ypos = [0, 40, 80, 100]

for i in range(len(ypos)):
    lab1 = tk.Label(gui, text = "This is a test!")
    lab1.place(x=20, y = 40+ypos[i])

gui.mainloop()