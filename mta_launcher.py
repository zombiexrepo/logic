import customtkinter as ctk
import subprocess

def start_launcher():
    ctk.set_appearance_mode("dark")
    root = ctk.CTk()
    root.geometry("400x300")
    root.title("MTA:SA Remote Launcher")

    ctk.CTkLabel(root, text="Connected to latest launcher.", font=("Arial", 18)).pack(pady=20)

    def launch_game():
        subprocess.Popen([
            r"C:\Program Files (x86)\MTA San Andreas 1.6\Multi Theft Auto.exe",
            "mtasa://127.0.0.1:22003"
        ])

    ctk.CTkButton(root, text="Launch Game", command=launch_game).pack(pady=20)
    root.mainloop()

start_launcher()
