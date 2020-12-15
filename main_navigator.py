from tkinter import *
import cv2
from PIL import Image, ImageTk

def projectcar_func():
    exec(open('projectcar.py').read())

def projectdrawer_func():
    exec(open('projectdrawer.py').read())

def projectface_func():
    exec(open('projectface.py').read())

def projectreadcolour_func():
    exec(open('projectreadcolour.py').read())

def projectbody_func():
    exec(open('projectbody.py').read())
    
def main():
    root = Tk()
    root.title("opencv")
    root.geometry("600x600")


    my_entries = []
    my_button = Button(root, text="Project Car!", command=projectcar_func)
    my_button.grid(row=1, column=0, pady=20)

    my_button = Button(root, text="Project Drawer!", command=projectdrawer_func)
    my_button.grid(row=2, column=0, pady=20)

    my_button = Button(root, text="Project Face!", command=projectface_func)
    my_button.grid(row=3, column=0, pady=20)

    my_button = Button(root, text="Project Readcolour!", command=projectreadcolour_func)
    my_button.grid(row=4, column=0, pady=20)

    my_button = Button(root, text="Project Body!", command=projectbody_func)
    my_button.grid(row=5, column=0, pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()