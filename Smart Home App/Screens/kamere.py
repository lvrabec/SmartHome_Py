from tkinter import * 
from PIL import Image,ImageTk


class Kamere():
    def __init__(self):
        self.frame_cam = Frame( width=898,
                                height=598,
                                highlightbackground= 'black',
                                highlightthickness=2, )
        self.frame_cam.grid(row=0,column=0)

    def kamera(self):
        self.chck_box_var_1 = IntVar()
        self.chck_box_var_2 = IntVar()
        self.chck_box_var_3 = IntVar()
        
        checkBox_1 = Checkbutton(text='Soba1',
                                 variable=self.chck_box_var_1,
                                 onvalue=1,
                                 offvalue=0,
                                 command=self.viewCam1                                
                                 )
        checkBox_1.place(x=10,y=10)
        

        #________________________________________________________________________________
        checkBox_2 = Checkbutton(text='Soba2',
                                 variable=self.chck_box_var_2,
                                 onvalue=1,
                                 offvalue=0,
                                 command=self.viewCam2                                
                                 )
        checkBox_2.place(x=300,y=10)



        #________________________________________________________________________________
        checkBox_3 = Checkbutton(text='Ulaz',
                                 variable=self.chck_box_var_3,
                                 onvalue=1,
                                 offvalue=0,
                                 command=self.viewCam3                                
                                 )
        checkBox_3.place(x=600,y=10)


        #________________________________________________________________________________

    def viewCam1(self):
            if self.chck_box_var_1.get() == 1:
                image=Image.open("./Images/soba1.png") 
                image_1= ImageTk.PhotoImage(image)
                self.label_1= Label(image=image_1)
                self.label_1.image = image_1
                self.label_1.place(x=10,y=30)
            else:
                exists= self.label_1.winfo_exists()
                if exists == 1:
                    self.label_1.destroy()
                    
        
    def viewCam2(self):
            if self.chck_box_var_2.get() == 1:
                image2=Image.open("./Images/soba2.png") 
                image_2= ImageTk.PhotoImage(image2)
                self.label_2= Label(image=image_2)
                self.label_2.image = image_2
                self.label_2.place(x=300,y=30)
            else:
                exists= self.label_2.winfo_exists()
                if exists == 1:
                    self.label_2.destroy()
                    
        
    def viewCam3(self):
            if self.chck_box_var_3.get() == 1:
                image3=Image.open("./Images/ulaz.png") 
                image_3= ImageTk.PhotoImage(image3)
                self.label_3= Label(image=image_3)
                self.label_3.image = image_3
                self.label_3.place(x=600,y=30)
            else:
                exists= self.label_3.winfo_exists()
                if exists == 1:
                    self.label_3.destroy()
                    