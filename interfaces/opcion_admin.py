import tkinter as tk
from tkinter import filedialog, ttk

# counter = 0

def opcion_admin() -> None:
    wventana = 1200
    hventana = 640

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
        global counter; counter = 0
        if botonPedidos.cget("state") == tk.ACTIVE:
            for t in toggle_buttons:
                t.grid(row=counter, column=0)
                counter += 1
        else:
            for t in toggle_buttons:
                t.grid_forget()
    

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
            botonAddProm.place(x=69+246+30,y=73+139+30)
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

    # Vinculos Botones de Barra -> Menu
    def mAddPlato() -> None:
        pass
    def mDelPlato() -> None:
        pass
    def mModPlato() -> None:
        pass
    def mAddProm() -> None:
        pass
    def mAddMesa() -> None:
        pass
    def mDelMesa() -> None:
        pass


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
    # frame1 = tk.Frame(ventana, width=200, height=200, relief=tk.RAISED, borderwidth=2)
    # frame1.pack(side=tk.LEFT)
    pedidos = [1,2,3]
    def toggle(i):
        print('I es igual a', i)
        print(len(toggle_buttons))
        if toggle_vars[i].get():
            # Mostrar los detalles del pedido
            clientes[i].grid(row= counter, column=0)
            counter += 1
        else:
            clientes[i].grid_forget()
            
    # TOCA HACER IN LISTA DE PEDIDOS PARA ITERARLA Y MOSTRARLA EN PANTALLA
    toggle_vars = []
    toggle_buttons = []
    clientes = []
    for z in range(len(pedidos)):
        toggle_vars.append(tk.BooleanVar(value=False)) # command=lambda index=i: toggle_state(index)
        toggle_buttons.append(tk.Checkbutton(ventana, text="Toggle", variable=toggle_vars[z], command= lambda index = z: toggle(index)))
        clientes.append(tk.Label(ventana, text="Cliente", bg='white', font=("Arial", 14)))
        print(z)

    # inventario
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

    table.insert(parent='', index='end', iid=0, values=('John Doe', 30, 'USA'))
    table.insert(parent='', index='end', iid=1, values=('Jane Smith', 25, 'UK'))
    table.insert(parent='', index='end', iid=2, values=('Bob Johnson', 40, 'Canada'))

    for i in range(15):
        table.insert(parent='', index='end', iid=3+i, values=('Bob Johnson', 40, 'Canada'))

    nomrbre_item = tk.Label(ventana, text="Nombre", bg='white', font=("Arial", 14))
    nomrbre_item_entry = tk.Entry(ventana)
    cantidad_item = tk.Label(ventana, text="Cantidad", bg='white', font=("Arial", 14))
    cantidad_item_entry = tk.Entry(ventana)
    save_item = tk.Button(ventana, text="Añadir ingrediente", bg='blue', fg='white')

    
    #Botones de Barra -> menu
    botonAddPlato = tk.Button(ventana, image=addPlato, command=mAddPlato, width=246, height=139)
    botonDelPlato = tk.Button(ventana, image=delPlato, command=mDelPlato, width=246, height=139)
    botonModPlato = tk.Button(ventana, image=modPlato, command=mModPlato, width=246, height=139)
    botonAddProm = tk.Button(ventana, image=addProm, command=mAddProm, width=246, height=139)
    botonAddMesa = tk.Button(ventana, image=addMesa, command=mAddMesa, width=246, height=139)
    botonDelMesa = tk.Button(ventana, image=delMesa, command=mDelMesa, width=246, height=139)
    botonesMenu = (botonAddPlato,botonDelPlato,botonModPlato,botonAddProm,botonAddMesa,botonDelMesa)

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


if __name__ == '__main__':
    opcion_admin()