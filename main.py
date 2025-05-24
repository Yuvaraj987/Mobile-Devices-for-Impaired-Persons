import tkinter as tk
from tkinter import ttk
import subprocess

def run_Face():
    subprocess.run(["python", "Face Guesture.py"])

def run_Navigation():
    subprocess.run(["python", "Navigation.py"])

def run_Speech():
    subprocess.run(["python", "Speech-Text.py"])

def run_Text():
    subprocess.run(["python", "Text-Speech.py"])

def close_app(event):
    root.destroy()

# Create the main application window
root = tk.Tk()
root.title("Mobile Device for Impaired Person")

# Adding a background color and setting window size
root.configure(bg='#34495e')
root.geometry('400x300')

# Changing the color and font of the label
welcome_label = tk.Label(root, text="Welcome to our App", font=("Helvetica", 16), bg='#34495e', fg='#ecf0f1')
welcome_label.pack(pady=10)

# Using themed button for a more modern look
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=5, background='#3498db', foreground='#3498db')
style.map('TButton', background=[('active', '#2980b9')])

# Create buttons and associate them with functions
button_Face = ttk.Button(root, text="Run Face.py", command=run_Face)
button_Navigation = ttk.Button(root, text="Run Navigation.py", command=run_Navigation)
button_Speech = ttk.Button(root, text="Run Speech.py", command=run_Speech)
button_Text = ttk.Button(root, text="Run Text.py", command=run_Text)

# Pack buttons into the window
button_Face.pack(pady=10)
button_Navigation.pack(pady=10)
button_Speech.pack(pady=10)
button_Text.pack(pady=10)

# Bind the Enter key to close the application
root.bind('<Return>', close_app)

# Start the GUI event loop
root.mainloop()
