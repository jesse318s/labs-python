import tkinter as tk
import tkinter.font as tkFont

# create tkinter object
app = tk.Tk()
#set app title
app.winfo_toplevel().title("Python GUI Mastery")
# set object's size
app.geometry("640x480")

#create font style to use in app
fontStyle = tkFont.Font(family="Segoe UI", size=24)

# create a label
labelExample = tk.Label(app, text="The system is idle.", font=fontStyle)


def SystemOn():
    # change label text
    labelExample.config(text = "System Running.")


def SystemOff():
    # change label text
    labelExample.config(text = "System Off.")



# create a virtual image to be used for sizing the buttons in pixels instead of text units
pixelVirtual = tk.PhotoImage(width=1, height=1)

# put the label in the app using pack example (TOP, BOTTOM, LEFT, RIGHT)
labelExample.pack(side=tk.TOP)

# button example - what window, button text, background color, foreground color, use virtual image for sizing, width, height, compound ="c" to show text
buttonExample1 = tk.Button(app, text="System On", bg="green", fg="white", image=pixelVirtual, width=200, height=100, compound="c", command = SystemOn)
# use place to give the button a pixel location on screen
buttonExample1.place(x=100, y=400)

buttonExample2 = tk.Button(app, text="System Off", bg="red", fg="white", image=pixelVirtual, width=200, height=100, compound="c", command = SystemOff)
buttonExample2.place(x=340, y=400)

#minimal exit button and pack example (TOP, BOTTOM, LEFT, RIGHT)
buttonExample3 = tk.Button(app, text="EXIT", command = app.quit)
buttonExample3.pack(side=tk.TOP)

app.mainloop()