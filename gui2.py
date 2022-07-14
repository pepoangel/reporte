from PIL import ImageTk, Image
import sys
from tkinter import messagebox
from openpyxl.styles.borders import Border, Side
import xlsxwriter
import subprocess
import os.path
import os
import tkinter as tk
from tkinter import Entry, Label, StringVar, Toplevel, ttk
from tkinter.font import Font
# Prueba para agregar producto a la linea
#df_bravo = pd.read_excel("/home/pepo/Descargas/inventarios/Lista_Bravo.xlsx")
# Rutas de los archivos PDF
inventario7 = "/home/pepo/Descargas/inventarios/Lista_Bravo.pdf"
inventario6 = "/home/pepo/Descargas/inventarios/Lista_Pricesmart.pdf"
inventario5 = "/home/pepo/Descargas/inventarios/Lista_Almacenes.pdf"
inventario4 = "/home/pepo/Descargas/inventarios/Lista_barriochino.pdf"
inventario3 = "/home/pepo/Descargas/inventarios/inventarioAdentro.pdf"
inventario2 = "/home/pepo/Descargas/inventarios/inventarioAfuera.pdf"
inventario8 = "/home/pepo/Descargas/inventarios/inventarioCarnesVegetales.pdf"
reporte = "/home/pepo/Descargas/inventarios/control.pdf"
# Los xlsx que seran pasados a PDF
pdf8 = "/home/pepo/Descargas/inventarios/inventarioCarnesVegetales.xlsx"
pdf2 = "/home/pepo/Descargas/inventarios/inventarioAfuera.xlsx"
pdf3 = "/home/pepo/Descargas/inventarios/inventarioAdentro.xlsx"
pdf4 = "/home/pepo/Descargas/inventarios/Lista_barriochino.xlsx"
pdf5 = "/home/pepo/Descargas/inventarios/Lista_Almacenes.xlsx"
pdf6 = "/home/pepo/Descargas/inventarios/Lista_Pricesmart.xlsx"
pdf7 = "/home/pepo/Descargas/inventarios/Lista_Bravo.xlsx"
archivo = "/home/pepo/Descargas/inventarios/texto.txt"
lineas = list()



class Principal:
   #Funcion para obtener las impresoras disponibles y meterlas en el comboBox3 
    def capta():
        # Requiere tener instaldo escputil herramienta para limpiar cabezales desde la linea de comandos
        def limpiar():
            
            impresora = str(comboBox3.get())
            subprocess.run(["bash", "-c","escputil -c -P 'impresora'"])
            tk.messagebox.showinfo(parent=ventanaSecundaria, title="Enviado a Limpiar impresora      ", message="Su comando fue enviado a la impresora.\n El boton de encendido deberia empezar a parpadear. ")
            
        impresoras = list()
        impresoras = subprocess.run(["bash", "-c", "lpstat -v > texto.txt"])
        # Abrimos el texto.txt para sacar las impresoras disponibles.
        with open("/home/pepo/Descargas/inventarios/texto.txt", "r") as file:
            for linea in file:
                # Separamos la linea para tomar la posicion 2 que es la posicion de la impresora
                b = linea.split()
                # Le quitamos los : que es el ultimo caracter para obetener el nombre exacto, b[2] es la posicion de la impresora
                c = b[2][:-1]
                # cargamos la lista de las impresoras
                lineas.append(c)
        #la ventana toplevel para elegir la impresora a limpiar
        ventanaSecundaria = tk.Toplevel()
        img = ImageTk.PhotoImage(Image.open("impresora3.gif"))
        panel = Label(ventanaSecundaria, image = img)
        panel.place(x = 20, y = 20 )     
        ventanaSecundaria.title("Limpieza de cabezales")
        ventanaSecundaria.config(width=480, height=500, bg="blue")
        #labelSecundaria = tk.Label(ventanaSecundaria, font=(
        #    "Arial", 18), text="Limpieza de Cabezales", bg="green")
        comboBox3 = ttk.Combobox(ventanaSecundaria, state="readonly", width=18, font=text_font)
        comboBox3.place(x=100, y=200)
        comboBox3['values'] = lineas
        #labelSecundaria.place(x=120, y=80)
        botonLimpiar = ttk.Button(
            ventanaSecundaria, text="Iniciar", command=limpiar)
        botonLimpiar.place(x=100, y=340)
        botonCerrar = ttk.Button(
           ventanaSecundaria, text="Cerrar", command=ventanaSecundaria.destroy)
        botonCerrar.place(x=260, y=340)
        ventanaSecundaria.mainloop()
        
        return 
        
    # Sin uso por ahora.
    def abrirVentanaSecundaria():
        ventanaSecundaria = tk.Toplevel()
        ventanaSecundaria.title("Impresion")
        ventanaSecundaria.config(width=300, height=300, bg="yellow")
        labelSecundaria = tk.Label(ventanaSecundaria, font=(
            "Arial", 18), text="Reportes Impresos", bg="blue")
        labelSecundaria.place(x=40, y=100)
        botonCerrar = ttk.Button(
            ventanaSecundaria, text="Cerrar",
            command=ventanaSecundaria.destroy
        )
        botonCerrar.place(x=105, y=235)
        labelSecundaria.place(x=40, y=100)
        botonCerrar = ttk.Button(
            ventanaSecundaria, text="Cerrar",
            command=ventanaSecundaria.destroy
        )
        botonCerrar.place(x=105, y=235)
        
        
    #Los log sin uso por ahora.
    def log(*args):
        logging.basicConfig(filename='example.log', encoding='utf-8',
                            level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logging.warning('Reporte impreso.')
    #Funcion para cerrar la ventana
    def cerrar():
        ventana.destroy()

    # Imprime la hoja de los reportes de despachos
    def reporte(reporte):
        subprocess.run(["lpr", "-P", "L3250-Series", reporte])
        return reporte
    #Conbierte a PDF el xlsx y lo impreme en formato PDF
    def impresion(exToPdf, pdf):
        subprocess.run(["libreoffice", "--convert-to", "pdf", exToPdf])
        subprocess.run(["lpr", "-P", "EPSON-TM-T20II", pdf])
        return exToPdf, pdf
    #Obtiene el reporte a imrpimir en la pantalla principal
    def obtener():
        if comboBox.get() == "Todos":
            Principal.impresion(pdf4, inventario4)
            Principal.impresion(pdf5, inventario5)
            Principal.impresion(pdf6, inventario6)
            Principal.impresion(pdf7, inventario7)
            Principal.impresion(pdf8, inventario8)
        if comboBox.get() == "Adentro":
            Principal.impresion(pdf2, inventario2)
        if str(comboBox.get()) == "Afuera":
            Principal.impresion(pdf3, inventario3)
        if comboBox.get() == "Hoja De Control":
            Principal.reporte(reporte)
        if comboBox.get() == "Barrio Chino":
            Principal.impresion(pdf4, inventario4)
        if comboBox.get() == "Almacenes":
            Principal.impresion(pdf5, inventario5)
        if comboBox.get() == "Pricesmart":
            Principal.impresion(pdf6, inventario6)
        if comboBox.get() == "Bravo":
            Principal.impresion(pdf7, inventario7)
        if comboBox.get() == "Vegetales":
            Principal.impresion(pdf8, inventario8)
    # Para agregar un Producto mas al archivo xlsx usando xlsxwriter
    def agregarLinea():
        ventanaNueva = Toplevel()
        ventanaNueva.title("Agregando linea de Producto")
        ventanaNueva.geometry("550x450")
        ventanaNueva.config(bg="blue")
        entrada = Entry(ventanaNueva, width=20)
        entrada.place(x=160, y=200)
        label2 = tk.Label(ventanaNueva, font=("Arial", 28),
                          text="Agregar A Lista: ", bg="blue")
        label2.place(x=120, y=60)
        comboBox2 = ttk.Combobox(
            ventanaNueva, values=["Pricesmart", "Barrio Chino", "Bravo", "Almacenes", "Vegetales"], state="readonly", width=13, font=text_font)
        comboBox2.place(x=150, y=140)
        comboBox2.current(0)
        label3 = tk.Label(ventanaNueva, font=("Arial", 16),
                          text="Producto ", bg="blue")
        label3.place(x=40, y=200)
        boton4 = tk.Button(ventanaNueva, text="Cerrar ", bg="red",
                           command=Principal.cerrar)
        boton4.place(x=400, y=350)
        boton5 = tk.Button(ventanaNueva, text="Agregar  ", bg="red",
                           command=Principal.cerrar)
        boton5.place(x=100, y=350)


# Ventana Principal
ventana = tk.Tk()
ventana.geometry("600x400")
ventana.title("Control de utilidades asia express")
ventana.configure(bg="blue")
ventana.resizable(0, 0)
#img = ImageTk.PhotoImage(Image.open('impresora3.gif'))
#imageLabel = tk.Label(ventana, image = img)   
#imageLabel.pack(side = "bottom", fill = "both", expand = "yes")

# Menu de ventana Opciones
menubar = tk.Menu(ventana)
filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label="Agregar")
filemenu.add_command(label="ELiminar")
filemenu.add_command(label="Modificar")
menubar.add_cascade(label="Opciones", menu=filemenu)

ventana.config(menu=menubar)

# Menu de ventana Impresoras.
impresora = tk.Menu(ventana)
impremenu = tk.Menu(menubar, tearoff=0)
impremenu.add_command(label="Limpieza", command=Principal.capta)
menubar.add_cascade(label="impresoras", menu=impremenu)

#impresora.add_cascade(label="Impresoras", menu=impremenu)
# ventana.config(menu=impresora)
valor = StringVar()
label = tk.Label(ventana, font=("Arial", 24),
                 text="Reportes De Inventarios", bg="blue")
label.place(x=130, y=100)
boton2 = tk.Button(ventana, text="Imprimir", bg="green",
                   command=Principal.obtener)
boton2.place(x=100, y=350)
boton3 = tk.Button(ventana, text="Cerrar  ", bg="red",
                   command=Principal.cerrar)
boton3.place(x=400, y=350)
text_font = ('Courier New', '16')
comboBox = ttk.Combobox(
    ventana, values=["Todos", "Pricesmart", "Barrio Chino", "Bravo", "Almacenes", "Vegetales", "Hoja De Control"], state="readonly", width=13, font=text_font)
comboBox.place(x=200, y=200)
comboBox.current(0)


ventana.mainloop()
