
import matplotlib.pyplot as plt

import matplotlib.animation as animation
from math import pi, tan, cos, sin #cosas trig
from math import radians
import pandas as pd
from re import S
from IPython.display import HTML
import numpy as np
import seaborn as sns
print("Ingresa tus valores de entrada")

while True:
    try: 
        velocidadInicial = float(input("Ingrese su velocidad inicial en m/s: "))
        break
    except ValueError: 
        print("Error: el valor ingresado no es un número válido.")

while True:
    try: 
        angulo = float(input("Ingrese su ángulo en grados: "))
        break
    except ValueError: 
        print("Error: el valor ingresado no es un número válido.")

gravedad = round(9.81)
grados = radians(angulo) #convierte a radianes

while True:  #Esto fue para crear un ciclo supuestamente inf me facilita pedir posicion cuando la pide sale y eso con demas while true
    try:
        posicionHorizontal = round(float(input("Posición horizontal en metros: ")))
        break
    except ValueError: 
        print("Error: el valor ingresado no es un número válido.")

while True:
    try:
        posicionVertical = round(float(input("Posición vertical en metros: ")))
        break
    except ValueError: 
        print("Error: el valor ingresado no es un número válido.")

gradosNew = tan(grados)
b = round((gravedad)/(2*velocidadInicial*2)*cos(grados)*2, 2) #corrección de fórmula

# calcula maximaAltura y maximaPosicion
maximaAltura = ((velocidadInicial*2)*np.sin(grados)*2)/(2*gravedad)
maximaPosicion = (velocidadInicial*2)*(np.sin(2*grados))/gravedad

velocidadAltura = (velocidadInicial*(cos(radians(angulo))))
velocidadVer = velocidadInicial*(sin(radians(angulo)))

tiempoMaximo = round((velocidadInicial*np.sin(grados))/gravedad)
tiempoVuelo = round(2*tiempoMaximo)

print("\nSus valores serían: ")
print("Altura máxima: ", round(maximaAltura, 2), "metros")
print("Distancia máxima: ", round(maximaPosicion, 2), "metros")
print("Tiempo de vuelo: ", tiempoVuelo, "segundos")

print("\nEl gráfico es:")

#
x = np.linspace(0, maximaPosicion) #Esto es para que cubra toda la distancia que yo como desarrollador elegí, hace tipo un array pero
#ahora donde empieza, termine en max posicion, no puse mas entradas por que pesaba el codigo

def funcion(x): #La ecuación de la trayectoria del balín
    return(gradosNew * x-b *(x**2))  #ecuacion fisica

#del original este codigo tiene animacion 

# Crear la figura y los ejes
figura, ejes = plt.subplots()

# En general aqui se ajusta para  que se logre ver la maxima posicion
ejes.set_xlim(0, maximaPosicion) 
ejes.set_ylim(0, maximaAltura*1.1) #que porque 1.1 porque es 10% mas alto que la maxima simplemente dejar un espacio mas

# Solo seteo el texto si se quita no aparece este tambien se adapto del codigo 
ejes.set_xlabel('Distancia (m)', fontsize=16, color='#FFDEDE')
ejes.set_ylabel('Altura (m)', fontsize=16, color='#FFDEDE')


plt.plot(x, funcion(x),'#84342d', label = ("Y"+str(format(gradosNew,".5f"))+"x-"+str(format(b,".5f"))))#Grafica la trayectoria respecto a la horizontal si le pongo y queda feo 
#el '“b- -”, línea discontinua “– ”, de color azul “b”'  es la linea y el label es el texto

plt.legend(loc = 4, fontsize=12) #La leyenda si no se pone no aparece  esto si lo quito sale error

# Definir el título  ojo con los colores tambien se adapto y lo cambiamos
ejes.set_title("PROYECTO NÚCLEO", fontsize=28, color='#ABC9FF', verticalalignment="baseline", horizontalalignment="center")

# Crear el objeto scatter que representa la bolita   #Aqui se crea un diagrama de dispersion y como son varias bolitas se puede representare
scatter = ejes.scatter([], [])

# Definir la función de inicialización
def init():
    scatter.set_offsets([[posicionHorizontal, posicionVertical]])  #Establece las coordenadas en el crafico
    #Inicializa el grafico de dispecion si se borra no va a haber posicion inicial
    return scatter,

# Definir la función de actualización
def update(frame):
    x = frame / 100.0
    y = funcion(x)
    scatter.set_offsets([[x, y]])  #aqui va actualizando 
    return scatter,

# Crear la animación en el intervalo y permite que se vaya actualizando
ani = animation.FuncAnimation(figura, update, frames=np.arange(0, 700), interval=20, init_func=init)

# Muestra la animacion en colab con esos graficos especiales 
HTML(ani.to_jshtml()) #ubclase que hace que la animacion se ejecute y se muestre sin esto paila
