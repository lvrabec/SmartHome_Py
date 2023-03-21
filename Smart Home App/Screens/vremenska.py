from tkinter import *
from tkinter import messagebox
import customtkinter
from customtkinter import *
from PIL import Image,ImageTk
import requests
import math









class Vremenska():
    def __init__(self) -> None:


        self.frame_vremenska_main = Frame(width=900,height=600)
        self.frame_vremenska_main.place(x=0,y=0)        


        photo_path_1 =Image.open("./Images/Background_gray.png")
        photo_image_1= ImageTk.PhotoImage(photo_path_1)
        self.photo_image_label_1=Label(self.frame_vremenska_main, image=photo_image_1,width=900,height=600)        
        self.photo_image_label_1.image=photo_image_1       
        self.photo_image_label_1.place(x=0,y=0)

        

    def vremenska_prognoza(self):      

        self.city_name_input_var=StringVar()
        self.label_temperature_var =StringVar()
        self.label_pressure_var=StringVar()
        self.label_humidity_var=StringVar()
        self.label_weather_var=StringVar()


        self.longitude_var=StringVar()
        self.latitude_var=StringVar()

        self.weather_data_tomorrow_var=StringVar()


        self.myApiKey= 'bb953d86a376e58dbfb65740c08a2fb2'
        self.base_URL= 'http://api.openweathermap.org/data/2.5/weather?'
        
        
        self.entry_bar=customtkinter.CTkEntry(master=self.frame_vremenska_main,   
                                placeholder_text="Enter City",
                                text_color='Black',
                                bg_color='#333333',
                                border_width=1,
                                corner_radius=7,                
                                width=200,
                                height=25,                                
                                )
        self.entry_bar.place(x=10,y=10)
          
        self.search_button_object =CTkButton(
                    master=self.frame_vremenska_main,
                    width=55,
                    height=10,
                    corner_radius=8, 
                    border_width=0,                                  
                    text='Search',
                    bg_color='#333333',
                    command=self.search
                    
                )
        self.search_button_object.place(x=215, y=12)
    

    def search(self):

        self.complete_URL=self.base_URL+"appid="+self.myApiKey+"&q="+self.entry_bar.get()
        str(self.complete_URL)
        print(self.complete_URL)
    
        self.city_name_requested = self.entry_bar.get()
        try:
            self.response = requests.get(self.complete_URL)
            self.data=self.response.json()        
            self.y=self.data['main'] 

        except:
            self.error_label=messagebox.showerror("ERROR!","City is not found , try again!")           

       
    
        if (self.data['cod']) !=404:        

            self.current_temperature_kelvin=self.y["temp"]
            self.current_temperature=str(math.ceil((self.current_temperature_kelvin-273.15)*100)/100)+" Celsius"
   
            self.current_pressure=str(self.y["pressure"])+" hPa units"
            self.current_humidity=str(self.y["humidity"])+" %"
            self.current_weather=self.data["weather"]
            self.current_weather_description=self.current_weather[0]["description"]
                       

            self.label_temperature=CTkLabel(master=self.frame_vremenska_main,          
                                            
                                            fg_color="#333333",
                                            bg_color="#333333",
                                            corner_radius=7,
                                            textvariable=self.label_temperature_var,
                                            font=CTkFont(size=13),
                                            text_color='White'
                                            )
            self.label_temperature.place(x=5,y=50)
            text_temperature=f"Current Temperature in {self.city_name_requested} is : "+ self.current_temperature
            self.label_temperature_var.set(text_temperature)
                  
                                              
            self.label_pressure=CTkLabel(master=self.frame_vremenska_main ,
                                            
                                            fg_color="#333333",
                                            bg_color="#333333",
                                            corner_radius=7,
                                            textvariable=self.label_pressure_var,
                                            font=CTkFont(size=13),
                                            text_color='White')
            self.label_pressure.place(x=5,y=75)
            text_pressure=f"Current Pressure in {self.city_name_requested} is : "+self.current_pressure
            self.label_pressure_var.set(text_pressure)
            

            self.label_humidity=CTkLabel(master=self.frame_vremenska_main,
                                         
                                            fg_color="#333333",
                                            bg_color="#333333",
                                            corner_radius=7,
                                            textvariable=self.label_humidity_var,
                                            font=CTkFont(size=13),
                                            text_color='White')
            self.label_humidity.place(x=5,y=100)
            text_humidity=f"Current Humidity in {self.city_name_requested} is : "+self.current_humidity
            self.label_humidity_var.set(text_humidity)

            
            self.label_weather_text=CTkLabel(master=self.frame_vremenska_main,                                            
                                            fg_color="#333333",
                                            bg_color="#333333",
                                            corner_radius=7,
                                            textvariable=self.label_weather_var,
                                            font=CTkFont(size=13),
                                            text_color='White',
                                            )
                                            
            self.label_weather_text.place(x=5,y=130)
            text_weather=f"Current Weather report for {self.city_name_requested} : \n "+self.current_weather_description
            self.label_weather_var.set(text_weather)
            

        if (self.data['cod']) == 404 :
          
            self.error_label=messagebox.showerror("ERROR!","City is not found , try again!")
            print(self.data["cod"],+" "+self.data["message"])



        #_____________________________________________________WEATHER FORECAST!__________________________________________________________________#

        self.appi_call_url_lon_lat="http://api.openweathermap.org/geo/1.0/direct?q="+self.city_name_requested+"&limit=5&appid="+self.myApiKey

        self.response_lonlat=requests.get(self.appi_call_url_lon_lat)
        self.data_lonlat=self.response_lonlat.json()

        self.data_listlon=[]
        self.res_lon=[sub['lon']for sub in self.data_lonlat]      
        result_1= str(self.res_lon[0])
        self.longitude_var.set(result_1)

        
        self.data_listlat=[]
        self.res_lat=[sub['lat']for sub in self.data_lonlat]
        self.data_listlat.append(self.res_lat[0])
        result_2=str(self.res_lat[0])
        self.latitude_var.set(result_2)

        URL_id="https://api.openweathermap.org/data/2.5/forecast?lat="+self.latitude_var.get()+"&lon="+self.longitude_var.get()+"&appid="+self.myApiKey

        self.five_day_weather=requests.get(URL_id)
        self.data_five_day_weather=self.five_day_weather.json()
        
      
        
        self.list_weather_tomorrow= []
        self.tomorrow_weather=self.data_five_day_weather['list']
        self.list_weather_tomorrow.append(self.tomorrow_weather[8])
  

        self.time_tomorrow=self.list_weather_tomorrow[0]['dt_txt']
    



        self.label_weather_tomorrow= CTkLabel(master=self.frame_vremenska_main,
                                         bg_color="#333333",
                                         text_color='white',
                                         text=f"Weather at {self.time_tomorrow} o`clock , \nin {self.city_name_requested}\nwill be : \n\n ' {self.list_weather_tomorrow[0]['weather'][0]['description']} '")        
        self.label_weather_tomorrow.place(x=10,y=175) 

        self.slicice()            


        #_________________________________________________________Slikice za prognozu______________________________________________________________

    def slicice(self): 

        if self.list_weather_tomorrow[0]['weather'][0]['id']>199 and self.list_weather_tomorrow[0]['weather'][0]['id']<233:
            self.display_pic="https://openweathermap.org/img/wn/11d@2x.png" #Thunderstorm

        elif self.list_weather_tomorrow[0]['weather'][0]['id']>299 and self.list_weather_tomorrow[0]['weather'][0]['id']<322:
            self.display_pic= "https://openweathermap.org/img/wn/09d@2x.png" #Drizzle 

        elif self.list_weather_tomorrow[0]['weather'][0]['id']>499 and self.list_weather_tomorrow[0]['weather'][0]['id']<505:
            self.display_pic="https://openweathermap.org/img/wn/10d@2x.png" #Light rain

        elif self.list_weather_tomorrow[0]['weather'][0]['id']==511:
            self.display_pic="https://openweathermap.org/img/wn/13d@2x.png" #Freezing rain

        elif self.list_weather_tomorrow[0]['weather'][0]['id']>519 and self.list_weather_tomorrow[0]['weather'][0]['id']<532:
            self.display_pic="https://openweathermap.org/img/wn/09d@2x.png" #Rain        

        elif self.list_weather_tomorrow[0]['weather'][0]['id']>599 and self.list_weather_tomorrow[0]['weather'][0]['id']<623:
            self.display_pic="https://openweathermap.org/img/wn/13d@2x.png" #Snow

        elif self.list_weather_tomorrow[0]['weather'][0]['id']>700 and self.list_weather_tomorrow[0]['weather'][0]['id']<782:
            self.display_pic="https://openweathermap.org/img/wn/50d@2x.png" # Atmosferske (magla,smog,mraz..Tornado..Armagedon i tak ..)
        
        elif self.list_weather_tomorrow[0]['weather'][0]['id']==800:
            self.display_pic="https://openweathermap.org/img/wn/01d@2x.png" # Clear sky    
              
        elif self.list_weather_tomorrow[0]['weather'][0]['id']==801:
            self.display_pic="https://openweathermap.org/img/wn/02d@2x.png" # Clouds 11-25 %

        elif self.list_weather_tomorrow[0]['weather'][0]['id']==802:
            self.display_pic= "https://openweathermap.org/img/wn/03d@2x.png" # Clouds 25-50 %      
        
        elif self.list_weather_tomorrow[0]['weather'][0]['id']==803:
            self.display_pic="https://openweathermap.org/img/wn/04d@2x.png" # Clouds 51-84%     

        elif self.list_weather_tomorrow[0]['weather'][0]['id']==804:
            self.display_pic="https://openweathermap.org/img/wn/04d@2x.png" # Clouds 85-100%     


        

        image=Image.open(requests.get(self.display_pic,stream=True).raw)
        image_photo_now=ImageTk.PhotoImage(image)
        self.weather_image_label_now=Label(image=image_photo_now,background="#333333")
        self.weather_image_label_now.image=image_photo_now
        self.weather_image_label_now.place(x=200,y=350)
        
        
        self.weather_text_icon_label=CTkLabel(master=self.frame_vremenska_main,fg_color="#333333",text_color='White',text='Weather icon \nfor tomorrow:')
        self.weather_text_icon_label.place(x=200,y=320)


        self.weather_today=self.current_weather[0]['id']
        # print(self.current_weather)
        # print(self.weather_today)
        
        if self.weather_today >199 and self.weather_today <233:
            self.display_pic_now="https://openweathermap.org/img/wn/11d@2x.png" #Thunderstorm

        elif self.weather_today >299 and self.weather_today <322:
            self.display_pic_now= "https://openweathermap.org/img/wn/09d@2x.png" #Drizzle 

        elif self.weather_today >499 and self.weather_today <505:
            self.display_pic_now="https://openweathermap.org/img/wn/10d@2x.png" #Light rain

        elif self.weather_today ==511:
            self.display_pic_now="https://openweathermap.org/img/wn/13d@2x.png" #Freezing rain

        elif self.weather_today >519 and self.weather_today <532:
            self.display_pic_now="https://openweathermap.org/img/wn/09d@2x.png" #Rain        

        elif self.weather_today >599 and self.weather_today <623:
            self.display_pic_now="https://openweathermap.org/img/wn/13d@2x.png" #Snow

        elif self.weather_today >700 and self.weather_today <782:
            self.display_pic_now="https://openweathermap.org/img/wn/50d@2x.png" # Atmosferske (magla,smog,mraz..Tornado..Armagedon i tak ..)
        
        elif self.weather_today ==800:
            self.display_pic_now="https://openweathermap.org/img/wn/01d@2x.png" # Clear sky    
              
        elif self.weather_today ==801:
            self.display_pic_now="https://openweathermap.org/img/wn/02d@2x.png" # Clouds 11-25 %

        elif self.weather_today ==802:
            self.display_pic_now= "https://openweathermap.org/img/wn/03d@2x.png" # Clouds 25-50 %      
        
        elif self.weather_today ==803:
            self.display_pic_now="https://openweathermap.org/img/wn/04d@2x.png" # Clouds 51-84%     

        elif self.weather_today ==804:
            self.display_pic_now="https://openweathermap.org/img/wn/04d@2x.png" # Clouds 85-100%  



        image=Image.open(requests.get(self.display_pic_now,stream=True).raw)
        image_photo_now=ImageTk.PhotoImage(image)
        self.weather_image_label_now=Label(image=image_photo_now,background="#333333")
        self.weather_image_label_now.image=image_photo_now
        self.weather_image_label_now.place(x=10,y=350)

        self.weather_text_icon_label=CTkLabel(master=self.frame_vremenska_main,fg_color="#333333",text_color='White',text='Weather icon \nNow:')
        self.weather_text_icon_label.place(x=10,y=320)