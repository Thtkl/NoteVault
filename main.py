import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry('400x500')
window.configure(background='gray')


# Logo image
logo_image = PhotoImage(file='vaultlogo1.png')

top_logo_label = tk.Label(window, image=logo_image, bg='gray')
top_logo_label.pack(side='top', pady=10)

title_label = tk.Label(window, text="Enter Title : ", font=('Arial', 14), bg='gray', fg="black")
title_label.pack(pady=(20, 5))

# title entry
title_entry = tk.Entry(window, font=('Arial', 14))
title_entry.pack(pady=10)

tk.mainloop()
