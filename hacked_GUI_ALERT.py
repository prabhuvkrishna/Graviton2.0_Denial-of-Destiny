import csv
import tkinter as tk
from tkinter import messagebox

# Create a Tkinter root window without displaying it
root = tk.Tk()
root.attributes("-alpha", 0)  # Set window transparency to 0, making it invisible

# Define the values
values = ["hacked", "hacked", "not hacked", "hacked", "hacked", "hacked"]

# Check for consecutive occurrences of "hacked"
hacked_count = 0
for value in values:
    if value == "hacked":
        hacked_count += 1
        if hacked_count >= 3:
            messagebox.showinfo("Alert", "Got hacked")
            break
    else:
        hacked_count = 0

# Close the Tkinter root window
root.destroy()
