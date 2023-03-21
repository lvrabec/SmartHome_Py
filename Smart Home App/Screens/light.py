from tkinter import *
from tkinter import ttk
from datetime import datetime
import time



class Light():
            def __init__(self):
                self.frame_light = Frame( width=898,
                                        height=598,
                                        highlightbackground= 'black',
                                        highlightthickness=2, )
                self.frame_light.grid(row=0,column=0)
    
            def light(self):
                self.check_box_var_1=IntVar() # za povezivanje s checkoboxom za odabir soba 
                self.check_box_var_2=IntVar()

                self.slider_var_1= DoubleVar()
                self.slider_var_2= DoubleVar()


                self.checkbox_1=Checkbutton(self.frame_light,text='Soba1',variable=self.check_box_var_1,onvalue=1,offvalue=0)
                self.checkbox_1.place(x=10,y=10)

                self.checkbox_2=Checkbutton(self.frame_light, text='Soba2',variable=self.check_box_var_2,onvalue=1,offvalue=0)
                self.checkbox_2.place(x=350,y=10)

                
                self.slider_1_label=ttk.Label(self.frame_light,text='Slider1')
                self.slider_1_label.place(x=10,y=350)
                self.slider_1=ttk.Scale(self.frame_light, from_=0, to=60 ,orient='horizontal',variable= self.slider_var_1,command=self.on_slider_1_change)
                self.slider_1.place(x=50,y=350)
                        
                self.slider_2_label=ttk.Label(self.frame_light,text='Slider2')
                self.slider_2_label.place(x=250,y=350)
                self.slider_2=ttk.Scale(self.frame_light, from_=0, to=60 ,orient='horizontal',variable= self.slider_var_2,command=self.on_slider_2_change)
                self.slider_2.place(x=300,y=350)



                self.timevar1 = time.time()
                self.timevar2 = time.time()

                self.counter_soba1()
                self.counter_soba2()


            def on_slider_1_change (self,event):
                   self.check_box_var_1.set(1)
                   self.timevar1 = time.time()


            def on_slider_2_change (self,event):
                   self.check_box_var_2.set(1)
                   self.timevar2 = time.time()

            def counter_soba1(self):
                if time.time() - self.timevar1>5 :
                          self.check_box_var_1.set(0)
            
                self.frame_light.after(2000,self.counter_soba1)
            
            def counter_soba2(self):
                if time.time() - self.timevar2>5 :
                          self.check_box_var_2.set(0)
            
                self.frame_light.after(2000,self.counter_soba2)