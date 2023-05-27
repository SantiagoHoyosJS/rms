from tkinter import *

def eliminar_plato():
    
    def save_changes():
        name = name_entry.get()
        email = email_entry.get()
        password = password_entry.get()
        print(f"Name: {name}\nEmail: {email}\nPassword: {password}")
        # Add code here to save the changes to a file or database

    # Create the main window
    ventana = Tk()
    ventana.title("Eliminar plato")

    # Creacion de ventana principal
    wventana = 1200
    hventana = 640


    pwidth = round(ventana.winfo_screenwidth() / 2 - wventana / 2)
    pheight = round(ventana.winfo_screenheight() / 2 - hventana / 2)

    ventana.geometry(str(wventana) + "x" + str(hventana) + "+" + str(pwidth) + "+" + str(pheight))
    ventana.configure(bg='white')
    ventana.resizable(False, False)


    title_label = Label(ventana, text="Eliminar plato de la carta", font=("Arial", 18, "bold"), bg='white')
    title_label.pack(pady=10)

    # Create labels and entry fields for name, email, and password
    name_label = Label(ventana, text="Nombre:", bg='white', font=("Arial", 14))
    name_label.pack(pady=30)
    name_entry = Entry(ventana)
    name_entry.pack()

    name_label2 = Label(ventana, text="Tipo de plato:", bg='white', font=("Arial", 14))
    name_label2.pack(pady=30)
    name_entry2 = Entry(ventana)
    name_entry2.pack()

    # Create a "Save" button
    save_button = Button(ventana, text="Guardar cambios", command=save_changes, bg='red', fg='white')
    save_button.pack(pady=50)

    # Start the Tkinter event loop
    ventana.mainloop()


if __name__ == '__main__':
    eliminar_plato()