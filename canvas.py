import math
from tkinter import *

root = Tk()
root.title("graphics")
root.geometry("1010x620")

canvas = Canvas(root, width=968, height=620, bg="#002")
canvas.pack()

for y in range(21):
    k = 50 * y
    canvas.create_line(10+k, 610, 10+k, 10, width=1, fill="#5F9EA0")

for x in range(13):
    k = 50 * x
    canvas.create_line(10, 10+k, 960, 10+k, width=1, fill="#5F9EA0")

root.mainloop()
