import tkinter as tk
import subprocess


ventana = tk.Tk()

pwidth = (ventana.winfo_screenwidth() - 1200) // 2 # width ventana = 1200
pheight = (ventana.winfo_screenheight() - 640) // 2 # height ventana = 640

ventana.geometry(f"1200x640+{str(pwidth)}+{str(pheight)}")
ventana.configure(bg='white')
ventana.resizable(False, False)

# imagenLamina = tk.PhotoImage(file="imagenes/admin/menu/tModPlato.png") #Cambiar Imagen

# lamina = tk.Label(ventana, image=imagenLamina, width=1235,height=87,borderwidth=0)
# lamina.place(x=-20,y=0)

#Insert nombre
labelNombre = tk.Label(ventana, text="Nombre", width = 32, height=3)
labelNombre.place(x=350, y = 100)

txtNombre = tk.Text(ventana, width = 32, height=1, bg="lightgrey")
txtNombre.place(x=350, y = 170)

#Insert tipo de plato
labelPlatos = tk.Label(ventana, text="Tipo de plato", width = 32, height=3)
labelPlatos.place(x=350, y = 200)

txtPlatos = tk.Text(ventana, width = 32, height=1, bg="lightgrey")
txtPlatos.place(x=350, y = 270)

#Insert precio
labelPrecio = tk.Label(ventana, text="precio", width = 32, height=3)
labelPrecio.place(x=350, y = 300)

txtPrecio = tk.Text(ventana, width = 32, height=1, bg="lightgrey")
txtPrecio.place(x=350, y = 370)

#Insert descripcion
labelDesc = tk.Label(ventana, text="Descripción", width = 32, height=3)
labelDesc.place(x=650, y = 100)

txtDesc = tk.Text(ventana, width = 32, height=8, bg="lightgrey")
txtDesc.place(x=650, y = 170)

#Insert lista de ingredientes
labelIngre = tk.Label(ventana, text="ingrese lista de ingredientes\n(separados por \",\")", width = 32, height=4)
labelIngre.place(x=920, y = 100)

txtIngre = tk.Text(ventana, width = 32, height=8, bg="lightgrey")
txtIngre.place(x=920, y = 170)

#Insert nombre del plato a modificar
labelMod = tk.Label(ventana, text="Nombre del plato a modificar", width = 32, height=3)
labelMod.place(x=50, y = 100)

txtMod = tk.Text(ventana, width = 32, height=1, bg="lightgrey")
txtMod.place(x=50, y = 170)

#Boton
def mGuardar() -> None:
    pass

guardar = tk.Button(ventana, command=mGuardar, bg="green", text="Guardar cambions", width=32, height=3,foreground="white")
guardar.place(x=536, y=500)

#Boton Volver
def bVolver() -> None:
    ventanaAdmin = tk.Toplevel(ventana)
    ventanaAdmin.deiconify()
    subprocess.Popen(['python', 'interfaces/opcion_admin2.py'])
    ventana.destroy()

volver = tk.Button(ventana,command=bVolver,text="Volver",width=6,height=3,font=("Arial", 12, "bold"))
volver.place(x=30,y=550)

ventana.mainloop()