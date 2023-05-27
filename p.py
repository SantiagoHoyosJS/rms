import tkinter as tk

# Create a Tkinter window
window = tk.Tk()

# Create widgets and place them using the grid system
label1 = tk.Label(window, text="Label 1")
label1.grid(row=0, column=0)

label2 = tk.Label(window, text="Label 2")
label2.grid(row=0, column=1)

button = tk.Button(window, text="Button")
button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

# Run the Tkinter event loop
window.mainloop()
