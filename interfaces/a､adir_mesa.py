from tkinter import *
import tkinter as tk
import subprocess

def add_mesa():
    
    def save_changes():
        name = name_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        print(f"Name: {name}\nEmail: {email}\nPassword: {password}")
        # Add code here to save the changes to a file or database

    # Create the main window
    ventana = Tk()
    ventana.title("Añadir mesa")

    # Creacion de ventana principal
    wventana = 1200
    hventana = 640


    pwidth = round(ventana.winfo_screenwidth() / 2 - wventana / 2)
    pheight = round(ventana.winfo_screenheight() / 2 - hventana / 2)

    ventana.geometry(str(wventana) + "x" + str(hventana) + "+" + str(pwidth) + "+" + str(pheight))
    ventana.configure(bg='white')
    ventana.resizable(False, False)

    imagenLamina = tk.PhotoImage(file="interfaces/images/tAddMesa.png")
    lamina = tk.Label(ventana, image=imagenLamina, width=1235,height=87,borderwidth=0)
    lamina.place(x=-20,y=0)

    title_label = Label(ventana, font=("Arial", 18, "bold"), bg='white')
    title_label.pack(pady=70)
    
    # Create labels and entry fields for name, email, and password
    name_label = Label(ventana, text="Número de la mesa:", bg='white', font=("Arial", 14,"bold"))
    name_label.pack(pady=30)
    name_entry = Entry(ventana)
    name_entry.pack()

    name_label2 = Label(ventana, text="Capacidad de la mesa:", bg='white', font=("Arial", 14,"bold"))
    name_label2.pack(pady=30)
    name_entry2 = Entry(ventana)
    name_entry2.pack()

    # Create a "Save" button
    save_button = Button(ventana, text="Guardar cambios", command=save_changes, bg='blue', fg='white', width=32, height=3)
    save_button.pack(pady=80)

    #Boton Volver
    def bVolver() -> None:
        ventanaAdmin = tk.Toplevel(ventana)
        ventanaAdmin.deiconify()
        subprocess.Popen(['python', 'interfaces/opcion_admin2.py'])
        ventana.destroy()

    volver = tk.Button(ventana,command=bVolver,text="Volver",width=6,height=3,font=("Arial", 12, "bold"))
    volver.place(x=30,y=550)    

    # Start the Tkinter event loop
    ventana.mainloop()


if __name__ == '__main__':
    add_mesa()