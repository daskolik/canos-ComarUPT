print("canOS - UI+ Script for B01 izmir efes")

import tkinter as tk
from tkinter import ttk

def create_windows_style_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Windows-like GUI")

    # Configure window size and position
    root.geometry("400x300")
    root.resizable(width=False, height=False)

    # Create a style that mimics the Windows theme
    style = ttk.Style()
    style.theme_use('winnative')  # Use the Windows theme

    # Create and configure labels
    label1 = ttk.Label(root, text="Label 1:")
    label1.grid(row=0, column=0, padx=10, pady=10, sticky="e")

    label2 = ttk.Label(root, text="Label 2:")
    label2.grid(row=1, column=0, padx=10, pady=10, sticky="e")

    # Create and configure entry widgets
    entry1 = ttk.Entry(root)
    entry1.grid(row=0, column=1, padx=10, pady=10, sticky="we")

    entry2 = ttk.Entry(root)
    entry2.grid(row=1, column=1, padx=10, pady=10, sticky="we")

    # Create and configure a button
    button = ttk.Button(root, text="Submit", command=on_submit)
    button.grid(row=2, column=0, columnspan=2, pady=20)

    # Start the Tkinter event loop
    root.mainloop()

def on_submit():
    # Add your code here to handle the button click
    print("Button clicked!")

if __name__ == "__main__":
    create_windows_style_gui()
