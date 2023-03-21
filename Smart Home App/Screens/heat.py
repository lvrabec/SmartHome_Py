from tkinter import *
from tkinter import ttk




class Heat:
        def __init__(self):
                self.frame_heat = Frame( width=898,
                                        height=598,
                                        highlightbackground= 'black',
                                        highlightthickness=2, )
                self.frame_heat.grid(row=0,column=0)
    
        def heat(self):
                self.check_box_var_1=IntVar() # za povezivanje s checkoboxom za odabir soba 
                self.check_box_var_2=IntVar()

                self.slider_var_1= DoubleVar()
                self.slider_var_2= DoubleVar()
                self.slider_var_3= DoubleVar()
                self.slider_var_4= DoubleVar()


                self.checkbox_1=Checkbutton(self.frame_heat,text='Soba1',variable=self.check_box_var_1,onvalue=1,offvalue=0)
                self.checkbox_1.place(x=10,y=10)

                self.checkbox_2=Checkbutton(self.frame_heat, text='Soba2',variable=self.check_box_var_2,onvalue=1,offvalue=0)
                self.checkbox_2.place(x=350,y=10)

                
                self.slider_1_label=ttk.Label(self.frame_heat,text='Slider1')
                self.slider_1_label.place(x=10,y=350)
                self.slider_1=ttk.Scale(self.frame_heat, from_=0, to=60 ,orient='horizontal',variable= self.slider_var_1,command=self.on_slider_1_change)
                self.slider_1.place(x=50,y=350)
                        
                self.slider_2_label=ttk.Label(self.frame_heat,text='Slider2')
                self.slider_2_label.place(x=250,y=350)
                self.slider_2=ttk.Scale(self.frame_heat, from_=0, to=60 ,orient='horizontal',variable= self.slider_var_2,command=self.on_slider_2_change)
                self.slider_2.place(x=300,y=350)
                        
                self.slider_3_label=ttk.Label(self.frame_heat,text='Slider3')
                self.slider_3_label.place(x=700,y=150)
                self.slider_3=ttk.Scale(self.frame_heat, from_=0, to=60 ,orient='vertical',variable= self.slider_var_3,command=self.on_slider_3_change)
                self.slider_3.place(x=750,y=100)
                        
                self.slider_4_label=ttk.Label(self.frame_heat,text='Slider4')
                self.slider_4_label.place(x=700,y=450)
                self.slider_4=ttk.Scale(self.frame_heat, from_=0, to=60 ,orient='vertical',variable= self.slider_var_4,command=self.on_slider_4_change)
                self.slider_4.place(x=750,y=400)

                self.checkTemp() ## ovo nije nuzno ali ajde nek provjeri odmah kad se pokrene program 


        def get_current_value_1(self):
                return '{: .2f}'.format(self.slider_var_1.get())
        
        def on_slider_1_change (self,event):
                self.slider_1_label.config(text=self.get_current_value_1())
                self.checkTemp()
                
                
        def get_current_value_2(self):
                return '{: .2f}'.format(self.slider_var_2.get())
        
        def on_slider_2_change (self,event):
                self.slider_2_label.config(text=self.get_current_value_2())
                self.checkTemp()
                
        def get_current_value_3(self):
                return '{: .2f}'.format(self.slider_var_3.get())
        
        def on_slider_3_change (self,event):
                self.slider_3_label.config(text=self.get_current_value_3())
                self.checkTemp()
                
        def get_current_value_4(self):
                return '{: .2f}'.format(self.slider_var_4.get())
        
        def on_slider_4_change (self,event):
                self.slider_4_label.config(text=self.get_current_value_4())
                self.checkTemp()
                


 
        def checkTemp(self):
                if self.slider_var_1.get()>=self.slider_var_3.get():
                        self.check_box_var_1.set(1)

                else:
                        self.check_box_var_1.set(0)

                if self.slider_var_2.get()>=self.slider_var_4.get():
                        self.check_box_var_2.set(1)

                else:
                        self.check_box_var_2.set(0)
