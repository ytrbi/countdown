from tkinter import *

root = Tk()

root.title('Countdown Timer')
root.geometry("840x530") # sizing the window size

icon = PhotoImage(file='icon.png')
root.iconphoto(True, icon) # adding image for the winform

root.config(background='#31363F')

# label attribute contain relief -border style- padx pady
msg = Label(root, text="Countdown Timer", font=('Arial', 30, 'bold'), fg='#76ABAE', bg='#31363F')
msg.place(x=240, y=150) # adding image using label within image attribute, and within the compound attribute we can place the image based on where to be relating to the text: bottom, top, left, or right

clicks = 0
click_lbl = Label(root, text=f"Countdown Timer: {clicks} clicks")
click_lbl.place(x=340, y=150)
def on_click():
    ++ clicks
    click_lbl.config(text=f"Countdown Timer: {clicks} clicks")

click_btn = Button(root, text='Click me!', command=on_click, bg='#76ABAE', fg='#EEEEEE')
click_btn.pack()


# def countdown():
#     return

# Label(root, text="Enter Hours".grid(row=0))

# hours = Entry(root)
# mins= Entry(root)

# button = Button(root, text="Start Timer", command=countdown)




mainloop()
