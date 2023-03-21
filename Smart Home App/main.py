from tkinter import *
from Screens.kamere import *
from Screens.robot import *
from Screens.vremenska import *
from Screens.heat import *
from Screens.light import * 


if __name__ == '__main__':
    root= Tk()
    root.title('Smart Home - Vrabec Luka')
    root.geometry('900x600')

    def kamere_():
        cam=Kamere()
        cam.kamera()

    def grijanje_():
        pass

    def robot_():
        romba=Robot()
        romba.robot()

    def weather_():
        vrijeme=Vremenska()
        vrijeme.vremenska_prognoza()


    def heat_():
        heating=Heat()
        heating.heat()
    
    def light_():
        lighting=Light()
        lighting.light()



    menubar  = Menu(root)
    filemenu = Menu(menubar,tearoff=0)
    filemenu.add_command(label='Kamere',command=kamere_)
    filemenu.add_command(label='Robot-usisavac',command=robot_)
    filemenu.add_command(label='Vremenska Prognoza',command=weather_)
    filemenu.add_command(label='Grijanje',command=heat_)
    filemenu.add_command(label='Svijetlo',command=light_)

    menubar.add_cascade(label='File',menu=filemenu)
    root.config(menu=menubar)



    root.mainloop()
