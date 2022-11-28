from tkinter import *  # libreria

raiz = Tk()


raiz.title("Ventana de Prueba")

# cambio de icono(conversor.icon)
# raiz.iconbitmap.("gato.ico")


raiz.resizable(0,0)

# cambiar tamaño de ventana

raiz.geometry("650x350")

# cambio de color

raiz.config(bg="green")

raiz.title("Aplicacion gráfica en python")

etiqueta = Label(raiz, text="Hola mundo con Python")

boton = Button(raiz, text="OK")

etiqueta.pack()

boton.pack()

raiz.mainloop()
