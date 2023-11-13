import tkinter as tk
from tkinter import ttk, messagebox
from capturandoRostros import capturador

import cv2
import os
import numpy as np
import time


window1=tk.Tk()
window1.geometry("300x100")

def evento_rostros():
	#dataPath = 'C:/Users/jorge/OneDrive/Escritorio/Reconocimiento de Emociones/capturandoRostros.py'
	#exec(open(dataPath).read())
	messagebox.showinfo('Mensaje Informativo','Se capturará rostros "Enojo"')
	capturador('Enojo')
	messagebox.showinfo('Registro completado','Rostros de Enojo capturados')
	messagebox.showinfo('Mensaje Informativo','Se capturará rostros "Felicidad"')
	capturador('Felicidad')
	messagebox.showinfo('Registro completado','Rostros de Felicidad capturados')
	messagebox.showinfo('Mensaje Informativo','Se capturará rostros "Sorpresa"')
	capturador('Sorpresa')
	messagebox.showinfo('Registro completado','Rostros de Sorpresa capturados')
	messagebox.showinfo('Mensaje Informativo','Se capturará rostros "Tristeza"')
	capturador('Tristeza')
	messagebox.showinfo('Registro completado','Rostros de Tristeza capturados')
	messagebox.showinfo('Mensaje Informativo','Se capturará rostros "Serio"')
	capturador('Serio')
	messagebox.showinfo('Registro completado','Rostros de Serio capturados')

	messagebox.showinfo('Registro completado','Todos los rostros han sido capturados')
	

def entrenador():
	dataPath = 'C:/Users/jorge/OneDrive/Escritorio/Reconocimiento de Emociones/entrenando.py'
	exec(open(dataPath).read())
	
def evento_reconocerEmociones():
	dataPath = 'C:/Users/jorge/OneDrive/Escritorio/Reconocimiento de Emociones/reconocimientoEmociones.py'
	exec(open(dataPath).read())


rostros= ttk.Button(window1,text="Capturar Rostros", command=evento_rostros)
rostros.place(x=30,y=10)
entrenador= ttk.Button(window1,text="Entrenar",command=entrenador)
entrenador.place(x=160,y=10)
reconocerEmociones= ttk.Button(window1,text="Reconocimiento Emociones",command=evento_reconocerEmociones)
reconocerEmociones.place(x=80,y=50)
window1.mainloop()