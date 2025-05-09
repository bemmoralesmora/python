from programas.sumar import sumar2
from programas.resta import restar2
from vistas.menu import menu
from vistas.lineas import lineas

# Módulos
import os
from datetime import datetime
import time

programa = True

# while True:
#    os.system("clear")  
#    print("Hora actual:", datetime.now().strftime("%H:%M:%S"))
#    time.sleep(1)

while(programa):
    lineas(10)
    print("Hora actual:", datetime.now().strftime("%H:%M:%S"))
    menu()
    res = int(input("[?]:"))
    
    if res == 1:
        sumar2()
    elif res == 2:
        restar2()
    elif res == 3:
        print("Ha salido del programa")
        programa = False 

os.system("clear")
