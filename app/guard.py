import tkinter as tk

window = None

def lock_screen():
    global window
    if window is None:
        window = tk.Tk()
        window.title("USBKeyGuard Lock")
        window.attributes("-fullscreen", True)
        window.configure(bg="black")
        label = tk.Label(window, text="🔒 LOCKED - Insert USB Key", fg="red", bg="black", font=("Arial", 40))
        label.pack(expand=True)
        window.update()

def unlock_screen():
    global window
    if window:
        window.destroy()
        window = None
