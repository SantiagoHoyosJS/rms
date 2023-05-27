import tkinter as tk
from PIL import ImageTk, Image
#from tkinter import ttk
import ttkbootstrap as ttk


def inicio() -> None:

    # Creacion de ventana principal
    wventana = 1200
    hventana = 640

    ventana = tk.Tk()

    pwidth = round(ventana.winfo_screenwidth() / 2 - wventana / 2)
    pheight = round(ventana.winfo_screenheight() / 2 - hventana / 2)

    ventana.geometry(str(wventana) + "x" + str(hventana) + "+" + str(pwidth) + "+" + str(pheight))
    ventana.title("¡Bienvenido!")
    ventana.configure(bg='white')
    ventana.resizable(False, False)


    # Imagen Inicial
    imagen = Image.open("interfaces/images/inicio.jpeg")  
    imagen = imagen.resize((wventana, hventana), Image.ANTIALIAS)
    imagen_fondo = ImageTk.PhotoImage(imagen)

    etiqueta_imagen = tk.Label(ventana, image=imagen_fondo)
    etiqueta_imagen.place(x=0, y=0, relwidth=1, relheight=1)


    #Boton siguiente
    original_image = Image.open("interfaces/images/derecha.png")  
    original_image = original_image.resize((80, 80))  
    image_width, image_height = original_image.size
    photo1 = ImageTk.PhotoImage(original_image)
    resized_image = original_image.resize((int(image_width * 1.1), int(image_height * 1.1)))  
    photo1_resized = ImageTk.PhotoImage(resized_image)

    canvas = tk.Canvas(ventana, width=image_width, height=image_height, bd=0, highlightthickness=0, bg="white")
    canvas.place(x=1020, y=500)  
    image_item = canvas.create_image(0, 0, anchor='nw', image=photo1)

    def on_enter(event):
        canvas.config(cursor="hand2")
        canvas.itemconfig(image_item, image=photo1_resized)
        canvas.config(width=image_width * 1.1, height=image_height * 1.1)

    def on_leave(event):
        canvas.config(cursor="")
        canvas.itemconfig(image_item, image=photo1)
        canvas.config(width=image_width, height=image_height)

    def on_click(event):
        canvas.config(relief='flat')
        canvas.destroy()
        etiqueta_imagen.destroy()
        ventana.destroy()



    canvas.bind("<Enter>", on_enter)
    canvas.bind("<Leave>", on_leave)
    canvas.bind("<Button-1>", on_click) 

    ventana.mainloop()
    
    return

if __name__ == '__main__':
    inicio()