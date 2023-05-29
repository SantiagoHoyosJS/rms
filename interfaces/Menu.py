import tkinter as tk, fontTools
from PIL import ImageTk, Image
#import ttkbootstrap as ttk
import tkinter as ttk
from PIL import Image, ImageDraw


def Menu():
    wventana = 1200
    hventana = 640

    ventana = tk.Tk()

    pwidth = round(ventana.winfo_screenwidth() / 2 - wventana / 2)
    pheight = round(ventana.winfo_screenheight() / 2 - hventana / 2)

    ventana.geometry(str(wventana) + "x" + str(hventana) + "+" + str(pwidth) + "+" + str(pheight))
    ventana.title("Compras")
    ventana.configure(bg='white')
    ventana.resizable(False, False)

    imagen = Image.open("interfaces/images/Shop bg.png")  
    imagen = imagen.resize((wventana, hventana), Image.ANTIALIAS)
    imagen_fondo = ImageTk.PhotoImage(imagen)

    etiqueta_imagen = tk.Label(ventana, image=imagen_fondo)
    etiqueta_imagen.place(x=0, y=0, relwidth=1, relheight=1)

    image = Image.open("interfaces/images/continuar.png") 
    continuar = ImageTk.PhotoImage(image)
    boton6 = tk.Button(ventana, image=continuar, width=279, height=51)
    boton6.place(x=579, y=137)




    # Crear arriba
    imagen1 = Image.open("interfaces/images/Component 7.png")
    imagen1 = imagen1.resize((34, 34), Image.ANTIALIAS)
    imagen_boton1 = ImageTk.PhotoImage(imagen1)

    arriba = tk.Button(ventana, image=imagen_boton1, width=34, height=34, bd=0, relief="solid", borderwidth=0, highlightthickness=0)
    arriba.place(x=813, y=220)

    # Crear abajo
    imagen2 = Image.open("interfaces/images/Component 8.png")
    imagen2 = imagen2.resize((44, 40), Image.ANTIALIAS)
    imagen_boton2 = ImageTk.PhotoImage(imagen2)

    abajo = tk.Button(ventana, image=imagen_boton2, width=34, height=34, bd=0, relief="solid", borderwidth=0, highlightthickness=0)
    abajo.place(x=813, y=570)

    # Etiqueta "Carlo's Restaurant"
    etiqueta_restaurante = tk.Label(ventana, text="Carlo's Restaurant", font=("Arial", 40), bg='white')
    etiqueta_restaurante.place(x=156, y=24, width=614, height=68)

    #carritos
    carrito = Image.open("interfaces/images/carritoanadir.png")
    carrito = carrito.resize((30, 30), Image.ANTIALIAS)
    carritoimagen = ImageTk.PhotoImage(carrito)

    agregar1 = tk.Button(ventana, image=carritoimagen, width=30, height=30, bd=0, relief="solid", borderwidth=0, highlightthickness=0)
    agregar1.place(x=770, y=293)

    agregar2 = tk.Button(ventana, image=carritoimagen, width=30, height=30, bd=0, relief="solid", borderwidth=0, highlightthickness=0)
    agregar2.place(x=770, y=418)

    agregar3 = tk.Button(ventana, image=carritoimagen, width=30, height=30, bd=0, relief="solid", borderwidth=0, highlightthickness=0)
    agregar3.place(x=770, y=550)





    
    
    # Etiqueta "Nombre"
    nombre1 = tk.StringVar()
    etiqueta_nombre1 = tk.Label(ventana, textvariable=nombre1, font=("Arial", 12))
    etiqueta_nombre1.place(x=164, y=229, width=163, height=28)

    # Etiqueta descripcion
    descripcion1 = tk.StringVar()
    descripcion1_etiqueta = tk.Label(ventana, textvariable=descripcion1, font=("Arial", 12))
    descripcion1_etiqueta.place(x=161, y=271, width=320, height=49)

    # Etiqueta precio
    precio1 = tk.DoubleVar()
    precio1_etiqueta = tk.Label(ventana, textvariable=precio1, font=("Arial", 12), fg='#F1404D')
    precio1_etiqueta.place(x=697, y=229, width=88, height=31)

    # Etiqueta imagen
    ruta1=tk.StringVar()
    ruta1_etiqueta = tk.Label(ventana , font=("Arial", 12))
    ruta1_etiqueta.place(x=34, y=220, width=102, height=102)
    





    # Etiqueta "Nombre"
    nombre2 = tk.StringVar()
    etiqueta_nombre2 = tk.Label(ventana, textvariable=nombre2, font=("Arial", 12),)
    etiqueta_nombre2.place(x=164, y=357, width=163, height=28)

    # Etiqueta descripcion
    descripcion2 = tk.StringVar()
    descripcion2_etiqueta = tk.Label(ventana, textvariable=descripcion2, font=("Arial", 12))
    descripcion2_etiqueta.place(x=161, y=399, width=320, height=49)

    # Etiqueta precio
    precio2 = tk.DoubleVar()
    precio2_etiqueta = tk.Label(ventana, textvariable=precio2, font=("Arial", 12),fg='#F1404D')
    precio2_etiqueta.place(x=697, y=357, width=88, height=31)

    # Etiqueta imagen
    ruta2=tk.StringVar()
    ruta2_etiqueta = tk.Label(ventana , font=("Arial", 12))
    ruta2_etiqueta.place(x=34, y=349, width=102, height=102)







    # Etiqueta "Nombre"
    nombre3 = tk.StringVar()
    etiqueta_nombre3 = tk.Label(ventana, textvariable=nombre3, font=("Arial", 12))
    etiqueta_nombre3.place(x=164, y=479, width=163, height=28)

    # Etiqueta descripcion
    descripcion3 = tk.StringVar()
    descripcion3_etiqueta = tk.Label(ventana, textvariable=descripcion3, font=("Arial", 12))
    descripcion3_etiqueta.place(x=161, y=532, width=320, height=49)

    # Etiqueta precio
    precio3 = tk.DoubleVar()
    precio3_etiqueta = tk.Label(ventana, textvariable=precio3, font=("Arial", 12), fg='#F1404D')
    precio3_etiqueta.place(x=697, y=490, width=88, height=31)

    # Etiqueta imagen
    ruta3=tk.StringVar()
    ruta3_etiqueta = tk.Label(ventana, font=("Arial", 12))
    ruta3_etiqueta.place(x=34, y=469, width=102, height=102)



    panel = ttk.Frame(ventana,bg='#FFBD59' ,borderwidth=1, padx=10, pady=10, bd=10, highlightcolor='#FFBD59', highlightbackground='#FFBD59')
    panel.place(x=880, y=70, width=280, height=530)




    def on_enter(event):
        boton1.config(cursor="hand2")
        boton2.config(cursor="hand2")
        boton3.config(cursor="hand2")
        boton4.config(cursor="hand2")
        boton5.config(cursor="hand2")
        arriba.config(cursor="hand2")
        abajo.config(cursor="hand2")
     
    def on_leave(event):
        boton1.config(cursor="")
        boton2.config(cursor="")
        boton3.config(cursor="")
        boton4.config(cursor="")
        boton5.config(cursor="")
        arriba.config(cursor="")
        abajo.config(cursor="")


    image = Image.open("interfaces/images/Component 5.png") 
    desayuno = ImageTk.PhotoImage(image)
    boton1 = tk.Button(panel, image=desayuno, width=158, height=51)
    boton1.pack(pady=5)


    image = Image.open("interfaces/images/Component 4.png") 
    entrada = ImageTk.PhotoImage(image)
    boton2 = tk.Button(panel, image=entrada, width=158, height=51)
    boton2.pack(pady=5)


    image = Image.open("interfaces/images/Component 3.png") 
    fuerte = ImageTk.PhotoImage(image)
    boton3 = tk.Button(panel, image=fuerte, width=158, height=51)
    boton3.pack(pady=5)


    image = Image.open("interfaces/images/Component 2.png") 
    postre = ImageTk.PhotoImage(image)
    boton4 = tk.Button(panel, image=postre, width=158, height=51)
    boton4.pack(pady=5)


    image = Image.open("interfaces/images/Component 1.png") 
    bebidas = ImageTk.PhotoImage(image)
    boton5 = tk.Button(panel, image=bebidas, width=158, height=51)
    boton5.pack(pady=5)

    







    boton1.bind("<Enter>", on_enter)
    boton1.bind("<Leave>", on_leave)

    boton2.bind("<Enter>", on_enter)
    boton2.bind("<Leave>", on_leave)

    boton3.bind("<Enter>", on_enter)
    boton3.bind("<Leave>", on_leave)

    boton4.bind("<Enter>", on_enter)
    boton4.bind("<Leave>", on_leave)

    boton5.bind("<Enter>", on_enter)
    boton5.bind("<Leave>", on_leave)

    arriba.bind("<Enter>", on_enter)
    arriba.bind("<Leave>", on_leave)

    abajo.bind("<Enter>", on_enter)
    abajo.bind("<Leave>", on_leave)

    ventana.mainloop()

if __name__ == '__main__':
    Menu()