from tkinter import *
import sqlite3
from tkinter import messagebox
import re

from PIL import ImageTk, Image
#GUI
   
root = Tk()
root.geometry("1000x700")
root.title("More Information")                        
root["bg"] = "#3d4e54"  

root.resizable(False,False)

frame = Frame(root, width=960, height=555)
frame.pack()
frame.place(x=20,y=70)

label_title = Label(root,text ="For Your Information",fg="#3d4e54",width = 18,bg="white",font = ("bold",20)).place(x=360,y=17)

image = Image.open("GrowthRate.png")

# Resize the image using resize() method
resize_image = image.resize((930,520))
 
img = ImageTk.PhotoImage(resize_image)
# create label and add resize image
label1 = Label(frame,image=img)
label1.image = img
label1.pack()
label1.place(x=10,y=10)

def home():
    root.destroy()
    import homepage
    
homep= Button(root,width=6,text='Back',border=0,
                bg='white',font=("Arial", 15)
                ,command=home)
homep.place(x=19,y=16)

root.mainloop()