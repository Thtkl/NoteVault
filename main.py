import tkinter as tk
from tkinter import *
from cryptography.fernet import Fernet
import os


key = Fernet.generate_key()
cipher_suite = Fernet(key)


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


# to save encrypted notes to a file
def save_to_file(title, encrypted_notes):
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, f"{title}.txt")
    with open(file_path, "wb") as file:
        file.write(encrypted_notes)
    print(f"Encrypted notes saved to {file_path}")


# function for encrypt data
def encrypt_notes():
    title = title_entry.get().strip()
    notes = notes_entry.get("1.0", tk.END).strip()
    if title and notes:
        encrypted_notes = cipher_suite.encrypt(notes.encode('utf-8'))
        save_to_file(title, encrypted_notes)
        print(f"Title: {title}")
        print(f"Encrypted Notes: {encrypted_notes}")
    else:
        print("Title or Notes are empty")


# decrypt notes function
def decrypt_notes():
    title = title_entry.get().strip()
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    file_path = os.path.join(desktop_path, f"{title}.txt")
    if os.path.exists(file_path):
        with open(file_path, "rb") as file:
            encrypted_notes = file.read()
        try:
            decrypted_notes = cipher_suite.decrypt(encrypted_notes).decode('utf-8')
            print(f"Title: {title}")
            print(f"Decrypted Notes: {decrypted_notes}")
            notes_entry.delete("1.0", tk.END)
            notes_entry.insert("1.0", decrypted_notes)
        except Exception as e:
            print("Error decrypting notes:", e)
    else:
        print(f"No file found for title: {title}")



# save and encrypt button
encrypt_button = tk.Button(window, text="Save & Encrypt", font=('Arial', 14), command=encrypt_notes, bg='gray', fg="black")
encrypt_button.pack(pady=20)

# decrypt button
decrypt_button = tk.Button(window, text="Decrypt Notes", font=('Arial', 14), command=decrypt_notes, bg='gray', fg="black")
decrypt_button.pack(pady=10)

tk.mainloop()
