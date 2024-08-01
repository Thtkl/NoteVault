import tkinter as tk
from tkinter import *

window = tk.Tk()
window.geometry('500x700')
window.title("Note Vault")
window.configure(background='gray')


# Logo image
logo_image = PhotoImage(file='vaultlogo1.png')

top_logo_label = tk.Label(window, image=logo_image, bg='gray')
top_logo_label.pack(side='top', pady=10)

# text for entr title
title_label = tk.Label(window, text="Enter Title : ", font=('Arial', 14), bg='gray', fg="black")
title_label.pack(pady=(20, 5))

# title entry
title_entry = tk.Entry(window, font=('Arial', 14))
title_entry.pack(pady=10)

# text for notes
notes_label = tk.Label(window, text="Enter Notes : ", font=('Arial', 14), bg='gray', fg="black")
notes_label.pack(pady=(20, 5))

# notes
notes_entry = tk.Text(window, font=('Arial', 14), height=5, width=40)
notes_entry.pack(pady=10, ipady=50)
notes_entry.config(borderwidth=2, relief="groove")

# function for encrypt data
def encrypt_notes():
    title = title_entry.get()
    notes = notes_entry.get("1.0", tk.END)
    # Placeholder for encryption logic
    print(f"Title: {title}")
    print(f"Notes: {notes}")
    # encrypt logic

# decrypt notes function
def decrypt_notes():
    title = title_entry.get()
    notes = notes_entry.get("1.0", tk.END)
    print(f"Title: {title}")
    print(f"Notes: {notes}")
    # decrypt logic


# save and encrypt button
encrypt_button = tk.Button(window, text="Save & Encrypt", font=('Arial', 14), command=encrypt_notes, bg='gray', fg="black")
encrypt_button.pack(pady=20)

# decrypt button
decrypt_button = tk.Button(window, text="Decrypt Notes", font=('Arial', 14), command=decrypt_notes, bg='gray', fg="black")
decrypt_button.pack(pady=10)

tk.mainloop()
