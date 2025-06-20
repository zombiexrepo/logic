import customtkinter as ctk
import subprocess
import os
import json
import mysql.connector
from tkinter import messagebox

# ========== MySQL DB Config ==========
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "mta_accounts"
}

# ========== MTA Config ==========
mta_path = r"C:\Program Files (x86)\MTA San Andreas 1.6\Multi Theft Auto.exe"
server_ip = "mtasa://127.0.0.1:22003"

# ========== Functions ==========


def check_login():
    username = entry_user.get()
    password = entry_pass.get()

    if not username or not password:
        messagebox.showerror("Login Error", "Please enter both username and password.")
        return

    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM accounts WHERE username=%s AND password=%s", (username, password))
        result = cursor.fetchone()
        conn.close()

        if result:
            messagebox.showinfo("Success", "Login successful!")
            btn_play.configure(state="normal")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"MySQL error: {err}")


def launch_game():
    if not os.path.exists(mta_path):
        messagebox.showerror("Error", "MTA executable not found.")
        return
    subprocess.Popen([mta_path, server_ip])


# ========== UI ==========
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

root = ctk.CTk()
root.title("MTA:SA Launcher with Login")
root.geometry("400x400")

ctk.CTkLabel(root, text="Login to Continue", font=("Arial", 20)).pack(pady=20)

entry_user = ctk.CTkEntry(root, placeholder_text="Username", width=300)
entry_user.pack(pady=10)

entry_pass = ctk.CTkEntry(root, placeholder_text="Password", show="*", width=300)
entry_pass.pack(pady=10)

btn_login = ctk.CTkButton(root, text="Login", command=check_login)
btn_login.pack(pady=15)

btn_play = ctk.CTkButton(root, text="Launch Game", command=launch_game, state="disabled")
btn_play.pack(pady=30)

root.mainloop()
