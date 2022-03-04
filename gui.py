import tkinter as tk
from tkinter import Label, StringVar, ttk
from tkinter.font import Font

def cerrar():
    ventana.destroy()

def obtener():
    print(comboBox.get())


ventana = tk.Tk()
ventana.geometry("400x300")
ventana.title("Imprimir Reportes para Inventarios")
ventana.configure(bg="blue")
ventana.resizable(0,0)
valor = StringVar()
boton2 = tk.Button(ventana, text="Imprimir",bg="green",command=obtener )
boton2.place(x=150, y=150)
boton3 = tk.Button(ventana, text="Cerrar",  command=cerrar)
boton3.place(x=150, y=220)
comboBox = ttk.Combobox(
    ventana, values=["Todos", "Carnes", "Adentro", "Afuera"])
comboBox.place(x=120, y=80)
comboBox.current(0)
etiqueta = Label(ventana, textvariable=obtener).place(x=150, y=280)





ventana.mainloop()
