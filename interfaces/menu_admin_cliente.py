from tkinter import *
import csv
from interfaces.opcion_admin2 import opcion_admin
from interfaces.Menu import Menu


def admin_login():
    ventana = Tk()
    def check():
        user = user_entry.get()
        password = password_entry.get()
        with open('interfaces/users.csv', "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                column1 = row[0]
                column2 = row[1]
                if column1 == user and column2 == password:
                    ventana.destroy()
                    opcion_admin()
                    return True  
                else:
                    user_entry.delete(0, END)
                    password_entry.delete(0, END)
                    wrong = Label(ventana, text="Parece que cometiste un error!", bg='white', font=("Arial", 12))
                    wrong.pack(pady=20)


    # Create the main window
   
    ventana.title("Login")

    # Creacion de ventana principal
    wventana = 1200
    hventana = 640


    pwidth = round(ventana.winfo_screenwidth() / 2 - wventana / 2)
    pheight = round(ventana.winfo_screenheight() / 2 - hventana / 2)

    ventana.geometry(str(wventana) + "x" + str(hventana) + "+" + str(pwidth) + "+" + str(pheight))
    ventana.configure(bg='white')
    ventana.resizable(False, False)


    title_label = Label(ventana, text="Admin login", font=("Arial", 18, "bold"), bg='white')
    title_label.pack(pady=10)

    # Create labels and entry fields for name, email, and password
    name_label = Label(ventana, text="Usuario:", bg='white', font=("Arial", 14))
    name_label.pack(pady=30)
    user_entry = Entry(ventana)
    user_entry.pack()

    name_label2 = Label(ventana, text="Contraseña:", bg='white', font=("Arial", 14))
    name_label2.pack(pady=30)
    password_entry = Entry(ventana, show="*")
    password_entry.pack()

    # Create a "Save" button
    save_button = Button(ventana, text="Login", command=check, bg='red', fg='white')
    save_button.pack(pady=50)

    # Start the Tkinter event loop
    ventana.mainloop()

def menu_admin_cliente() -> bool: # main
    next = None
    wventana = 1200
    hventana = 640

    ventana = Tk()
    imagenCliente = PhotoImage(file="interfaces/images/bCliente.png") #Puede que tengas que cambiar la referencia
    imagenAdmin = PhotoImage(file="interfaces/images/bAdmin.png")

    pwidth = round((ventana.winfo_screenwidth() - wventana) / 2)
    pheight = round((ventana.winfo_screenheight() - hventana) / 2)

    ventana.geometry(str(wventana) + "x" + str(hventana) + "+" + str(pwidth) + "+" + str(pheight))
    ventana.configure(bg='white')
    ventana.resizable(False, False)

    def commCliente(): # Ejecutal al presionar Cliente
        ventana.destroy()
        Menu()

    def commAdmin(): # Ejecuta al presionar Admin
        ventana.destroy()
        admin_login()

    bx = 257

    botonCliente = Button(ventana,command=commCliente, image=imagenCliente, width=215, height=320, borderwidth=0, activebackground="white", bg="white")
    botonCliente.place(x=bx, y=160)

    botonAdmin = Button(ventana,command=commAdmin, image=imagenAdmin, width=215, height=320, borderwidth=0, activebackground="white", bg="white")
    botonAdmin.place(x = 215+bx*2, y = 160)

    ventana.mainloop()


if __name__ == '__main__':
    menu_admin_cliente()