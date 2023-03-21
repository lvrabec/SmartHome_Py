from tkinter import *
from PIL import Image,ImageTk


class Robot():
    def __init__(self) -> None:
        self.frame_robot = Frame(width=898,height=598,highlightbackground='black',highlightthickness=2)
        self.frame_robot.grid(row=0,column=0)

    def robot(self):
        self.check_box_var = IntVar()
        check_box= Checkbutton(text='Robotski usisavac (On/Off)',
                               variable=self.check_box_var,
                               onvalue=1,
                               offvalue=0,
                               command=self.robot_vacum)
        check_box.place(x=350,y=10)
        
    def robot_vacum(self):
        if self.check_box_var.get() == 1:
            image=Image.open("./Images/robot.jpg")
            image1=ImageTk.PhotoImage(image)
            self.labela_robot=Label(image=image1)
            self.labela_robot.image=image1
            self.labela_robot.place(x=325,y=75)

            self.labela_poruka=Label(text='Vaš robot je u procesu čišćenja')
            self.labela_poruka.place(x=250,y=550)
            
        else:
            exists= self.labela_robot.winfo_exists()
            if exists == 1:
                self.labela_robot.destroy()
                self.labela_poruka.destroy()
