import tkinter

window = tkinter.Tk()
# to rename the title of the window
window.title("GUI")
# pack is used to show the object in the window
label = tkinter.Label(window, text = "Welcome to DataCamp's Tutorial on Tkinter!").pack()
# You will first create a division with the help of Frame class and align them on TOP and BOTTOM with pack() method.
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side = "bottom")

# Once the frames are created then you are all set to add widgets in both the frames.
btn1 = tkinter.Button(top_frame, text = "Button1", fg = "red").pack() #'fg or foreground' is for coloring the contents (buttons)

btn2 = tkinter.Button(top_frame, text = "Button2", fg = "green").pack()

btn3 = tkinter.Button(bottom_frame, text = "Button3", fg = "purple").pack(side = "left") #'side' is used to left or right align the widgets

btn4 = tkinter.Button(bottom_frame, text = "Button4", fg = "orange").pack(side = "right")

window.mainloop()
