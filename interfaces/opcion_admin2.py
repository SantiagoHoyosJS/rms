from __future__ import annotations
import tkinter as tk
from tkinter import filedialog, ttk
import subprocess
import csv

from abc import ABC
from typing import List
# from inventory.pedido import Pedido
# from person.mesa import Plato

# counter = 0

def opcion_admin() -> None:
    wventana = 1200
    hventana = 640

    counter = [0]

    ventana = tk.Tk()
    folder = "interfaces/images/"
    fOpciones = tk.PhotoImage(file=folder+"tabla.png")
    #Imagenes Barra
    bPedidos = (tk.PhotoImage(file=folder+"bPedidos_des.png"),tk.PhotoImage(file=folder+"bPedidos_act.png"))
    bInventario = (tk.PhotoImage(file=folder+"bInventario_des.png"),tk.PhotoImage(file=folder+"bInventario_act.png"))
    bMenu = (tk.PhotoImage(file=folder+"bMenu_des.png"),tk.PhotoImage(file=folder+"bMenu_act.png"))
    bConfig = (tk.PhotoImage(file=folder+"bConfig_des.png"),tk.PhotoImage(file=folder+"bConfig_act.png"))
    #Imagenes Barra -> Menu
    addPlato = tk.PhotoImage(file=folder+"MenuAddPlato.png")
    delPlato = tk.PhotoImage(file=folder+"MenuDelPlato.png")
    modPlato = tk.PhotoImage(file=folder+"MenuModPlato.png")
    addProm = tk.PhotoImage(file=folder+"MenuAddProm.png")
    addMesa = tk.PhotoImage(file=folder+"MenuAddMesa.png")
    delMesa = tk.PhotoImage(file=folder+"MenuDelMesa.png")

    def BotonMenuPresionado(boton:tk.Button, n_boton) -> None:
        # Cambia la imagen del boton al presionarlo
        for button in botones:
            if button == boton: button.config(image=button.cget("text")[1], state=tk.ACTIVE)
            else: button.config(image=button.cget("text")[0], state=tk.NORMAL)

        pedidosF()
        inventario()
        StateMenu()
        configuracion()
    
    def pedidosF():
        if botonPedidos.cget("state") == tk.ACTIVE:
            scroll_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)
            canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            for lp in labels_pedidos:
                lp[0].pack()
                lp[1].pack()
                for plato in lp[2]:
                    plato.pack()

            
            codigo.place(x=500,y=200)
            codigo_entry.place(x=500,y=250)
            pedido_completado.place(x=500,y=300)
                
        else:
            scroll_frame.pack_forget()
            canvas.pack_forget()
            scrollbar.pack_forget()

            for lp in labels_pedidos:
                lp[0].pack_forget()
                lp[1].pack_forget()
                for plato in lp[2]:
                    plato.pack_forget()

            codigo.place_forget()
            codigo_entry.place_forget()
            pedido_completado.place_forget()


    def inventario():
        if botonInventario.cget("state") == tk.ACTIVE:
            table.place(x=350,y=100)
            nomrbre_item.place(x=100,y=100)
            nomrbre_item_entry.place(x=100,y=150)
            cantidad_item.place(x=100,y=250)
            cantidad_item_entry.place(x=100,y=300)
            save_item.place(x=100,y=400)
        else:
            table.place_forget()
            nomrbre_item.place_forget()
            nomrbre_item_entry.place_forget()
            cantidad_item.place_forget()
            cantidad_item_entry.place_forget()
            save_item.place_forget()

    def StateMenu() -> None:
        if botonMenu.cget("state") == tk.ACTIVE:
            for boton in botonesMenu:
                boton.config(state = tk.NORMAL)
                
            botonAddPlato.place(x=69,y=73)
            botonDelPlato.place(x=69+246+30,y=73)
            botonModPlato.place(x=69,y=73+139+30)
            botonAddMesa.place(x=69,y=73+(139+30)*2)
            botonDelMesa.place(x=69+246+30,y=73+(139+30)*2)
        else:
            for boton in botonesMenu:
                boton.config(state = tk.DISABLED)
                boton.place_forget()

    def configuracion():
        if botonConfig.cget("state") == tk.ACTIVE:
            nombre_res.place(x=100,y=100)
            res_entry.place(x=100,y=150)
            logo.place(x=100,y=250)
            select_img.place(x=100,y=300)
            save.place(x=100,y=400)
        else:
            nombre_res.place_forget() 
            res_entry.place_forget()
            logo.place_forget()
            select_img.place_forget()
            save.place_forget()
    
    def select_image():
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])

    file_path = None

    def cambioVentana(directorio:str) -> None:
        ventanaAdmin = tk.Toplevel(ventana)
        ventanaAdmin.deiconify()
        subprocess.Popen(['python', directorio])
        ventana.destroy()

    def mAddPlato() -> None:
        cambioVentana("interfaces/addPlato.py")  
    def mDelPlato() -> None:
        cambioVentana("interfaces/eliminar_plato.py")  
    def mModPlato() -> None:
        cambioVentana("interfaces/modPlato.py")
    def mAddMesa() -> None:
        cambioVentana("interfaces/a､adir_mesa.py")
    def mDelMesa() -> None:
        cambioVentana("interfaces/eliminar_mesa.py")



    pwidth = round((ventana.winfo_screenwidth() - wventana) / 2)
    pheight = round((ventana.winfo_screenheight() - hventana) / 2)

    ventana.geometry(str(wventana) + "x" + str(hventana) + "+" + str(pwidth) + "+" + str(pheight))
    ventana.configure(bg='white')
    ventana.resizable(False, False)

    fondoOpciones = tk.Label(ventana, image=fOpciones, width=393, height=517)
    fondoOpciones.place(x=707,y=49)

    #Botones Barra // a la izquierda de la aplicacion
    botonPedidos = tk.Button(ventana,text=bPedidos, image=bPedidos[0], width=335, height=35)
    botonInventario = tk.Button(ventana, text=bInventario, image=bInventario[0], width=335,height=35)
    botonMenu = tk.Button(ventana,text=bMenu ,image=bMenu[0], width=335,height=35)
    botonConfig = tk.Button(ventana, text=bConfig, image=bConfig[0], width=335,height=35)
    botones = (botonPedidos,botonInventario,botonMenu,botonConfig)

    for boton in botones:
        boton.config(borderwidth=0,activebackground="#F6F1F1", bg="#F6F1F1")

    botonPedidos.config(command=lambda:BotonMenuPresionado(botonPedidos, 0))
    botonInventario.config(command=lambda:BotonMenuPresionado(botonInventario, 1))
    botonMenu.config(command=lambda:BotonMenuPresionado(botonMenu, 2))
    botonConfig.config(command=lambda:BotonMenuPresionado(botonConfig, 3))

    # pedidos
    codigo = tk.Label(ventana, text="Codigo:", bg='white', font=("Arial", 14))
    codigo_entry = tk.Entry(ventana)
    pedido_completado = tk.Button(ventana, text="Pedido completado", bg='blue', fg='white')

    bg_color_pedidos_frame = 'white'
    scroll_frame = ttk.Frame(ventana)
    # Create a canvas
    canvas = tk.Canvas(scroll_frame)
    # Create a scrollbar
    scrollbar = ttk.Scrollbar(scroll_frame, orient=tk.VERTICAL, command=canvas.yview)
    # Configure the canvas and scrollbar    
    canvas.configure(yscrollcommand=scrollbar.set, bg=bg_color_pedidos_frame)
    canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    # Create a frame inside the canvas   
    inner_frame = ttk.Frame(canvas)
    canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

    pedidos = [Pedido('Juan', [Plato('Pizza'), Plato('Hamburguesa')]), Pedido('Luis', [Plato('Salchipapa'), Plato('Perro caliente')]), Pedido('Andrea', [Plato('Hamburguesa'), Plato('Pollo asado')]), Pedido('Javier', [Plato('Carne asada'), Plato('Pollo asado')]), Pedido('Laura', [Plato('Pizza'), Plato('Salchipapa')]), Pedido('Carlos', [Plato('Perro caliente'), Plato('Pollo asado')])]
    labels_pedidos = []
            
    # TOCA HACER IN LISTA DE PEDIDOS PARA ITERARLA Y MOSTRARLA EN PANTALLA
    for pedido in pedidos:
        pedido_id = tk.Label(inner_frame, text=f"Pedido {pedido.id}", bg=bg_color_pedidos_frame, font=("Arial", 14), width=20, anchor="w")
        pedido_cliente = tk.Label(inner_frame, text=f"Cliente {pedido.cliente}", bg=bg_color_pedidos_frame, font=("Arial", 14), width=20, anchor="center")
        plato_labels = []
        for plato in pedido.platos:
            plato_label = tk.Label(inner_frame, text=plato.nombre, bg=bg_color_pedidos_frame, font=("Arial", 14), width=20, anchor="e")
            plato_labels.append(plato_label)
        labels_pedidos.append([pedido_id, pedido_cliente, plato_labels])




    # inventario
    last_id = [0]
    def guardar_item(nombre, cantidad):
        last_id[0] += 1
        item = (last_id[0],nombre,cantidad)
        with open("interfaces/items.csv", 'a', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(item)
        datos_inventario.append(item)
        table.place_forget()
        table.insert(parent='', index='end', iid=len(datos_inventario), values=datos_inventario[-1])
        table.place(x=350,y=100)
        nomrbre_item_entry.delete(0, tk.END)
        cantidad_item_entry.delete(0, tk.END)
        return
    
    datos_inventario = []
    table = ttk.Treeview(ventana)
    table['columns'] = ('id', 'nombre', 'cantidad')
    table.column('#0', width=0, stretch=tk.NO)  # Hide the first column
    table.column('0', width=100)
    table.column('1', width=70)
    table.column('2', width=100) 

    table.heading('#0', text='', anchor=tk.W)
    table.heading('0', text='Id', anchor=tk.W)
    table.heading('1', text='Nombre', anchor=tk.W)
    table.heading('2', text='Cantidad', anchor=tk.W)


    with open("interfaces/items.csv", 'r', newline='') as archivo:
        reader = csv.reader(archivo)
        for row in reader:
            print(len(row))
            item = (row[0],row[1],row[2])
            last_id[0] = int(row[0])
            datos_inventario.append(item)
    
    # datos_inventario = [('001', 'Jamon', 10), ('002', 'Queso', 15), ('003', 'Harina', 23), ('004', 'Salsa de tomate', ),('005', 'Pollo', 7),('006', 'Carne', 6),('007', 'Mayonesa', 3)]


    for i in range(len(datos_inventario)):
        table.insert(parent='', index='end', iid=i, values=datos_inventario[i])
        

    nomrbre_item = tk.Label(ventana, text="Nombre", bg='white', font=("Arial", 14))
    nomrbre_item_entry = tk.Entry(ventana)
    cantidad_item = tk.Label(ventana, text="Cantidad", bg='white', font=("Arial", 14))
    cantidad_item_entry = tk.Entry(ventana)
    save_item = tk.Button(ventana, text="Añadir ingrediente", bg='blue', fg='white', command= lambda: guardar_item(nomrbre_item_entry.get(), cantidad_item_entry.get()))

    
    #Botones de Barra -> menu
    botonAddPlato = tk.Button(ventana, image=addPlato, command=mAddPlato, width=246, height=139)
    botonDelPlato = tk.Button(ventana, image=delPlato, command=mDelPlato, width=246, height=139)
    botonModPlato = tk.Button(ventana, image=modPlato, command=mModPlato, width=246, height=139)
    botonAddMesa = tk.Button(ventana, image=addMesa, command=mAddMesa, width=246, height=139)
    botonDelMesa = tk.Button(ventana, image=delMesa, command=mDelMesa, width=246, height=139)
    botonesMenu = (botonAddPlato,botonDelPlato,botonModPlato,botonAddMesa,botonDelMesa)

    # Configuracion
    nombre_res = tk.Label(ventana, text="Nombre del restaurante:", bg='white', font=("Arial", 14))
    res_entry = tk.Entry(ventana)
    logo = tk.Label(ventana, text="Añade tu logo", bg='white', font=("Arial", 14))
    select_img = tk.Button(ventana, text="Select Image", command=select_image) 
    save = tk.Button(ventana, text="Guardar cambios", bg='blue', fg='white')


    for boton in botonesMenu:
        boton.config(borderwidth=0,activebackground="white", bg="white")

    #Botones Barra - Separacion de 30 en y
    botonPedidos.place(x=733, y=231)
    botonInventario.place(x=733, y=296)
    botonMenu.place(x=733, y=361)
    botonConfig.place(x=733, y=426)

    ventana.mainloop()
    return





class Pedido(ABC):
    ID = 0

    def __init__(self, cliente, platos: List['Plato']) -> None:
        self.__id = Pedido.ID
        self.__cliente = cliente
        self.__platos: List['Plato'] = platos
        Pedido.ID += 1

    @property
    def id(self):
        return self.__id

    @property
    def cliente(self) -> 'Cliente': 
        return self.__cliente

    @property
    def platos(self) -> list['Plato']:
        return self.__platos

class PedidoPresencial(Pedido):
    def __init__(self, cliente, platos: List['Plato'], mesa) -> None:
        super().__init__(cliente, platos)
        self.__mesa = mesa

class PedidoDomicilio(Pedido):
    def __init__(self, cliente, platos: List['Plato'], telefono: str) -> None:
        super().__init__(cliente, platos)
        self.__telefono: str = telefono

class Plato:
    def __init__(self, nombre, descripcion='', precio=0):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        self._nombre = value

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        self._precio = value

    def __str__(self):
        return f"{self.nombre}: {self.descripcion} - ${self.precio}"
    
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio


if __name__ == '__main__':
    opcion_admin()