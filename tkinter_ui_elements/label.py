import tkinter as tk

root = tk.Tk()

root.geometry("800x500")

root.title("My New App")

label = tk.Label(root, text="Hello World", font=('Arial', 18))

label.pack(padx=20, pady=20)


# Displays the window
root.mainloop()