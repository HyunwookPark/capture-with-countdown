import time
import pygetwindow as gw
import pyautogui
from PIL import ImageGrab
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import os

# Countdown function
def countdown(count, label, root, callback):
    if count > 0:
        label.config(text=f"Starting capture in: {count} seconds")
        root.after(1000, countdown, count - 1, label, root, callback)
    else:
        callback()

# Capture process
def capture_window():
    # Get all current windows
    windows = gw.getAllTitles()

    # Exclude empty window titles
    windows = [w for w in windows if w.strip()]

    if not windows:
        messagebox.showerror("Error", "No available windows found.")
        return

    # GUI for selecting a window
    def select_window():
        choice = listbox.curselection()
        if not choice:
            messagebox.showwarning("Warning", "Please select a window.")
            return

        window_title = windows[choice[0]]
        target_window = gw.getWindowsWithTitle(window_title)[0]

        # Bring the window to the front
        target_window.activate()

        # Countdown label
        countdown_label = tk.Label(root, text="Starting capture in: 3 seconds", font=("Arial", 14))
        countdown_label.pack(pady=10)

        def take_screenshot():
            # Get the window's coordinates
            left, top, right, bottom = target_window.left, target_window.top, target_window.right, target_window.bottom

            # Take a screenshot
            screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

            # Use timestamp for the file name
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            save_path = os.path.abspath(f"captured_window_{timestamp}.jpg")
            screenshot.convert("RGB").save(save_path, "JPEG")

            messagebox.showinfo("Success", f"Screenshot saved at:\n{save_path}")
            countdown_label.destroy()

        countdown(3, countdown_label, root, take_screenshot)

    # Build the window selection screen
    listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Arial", 12), height=15, width=50)
    for title in windows:
        listbox.insert(tk.END, title)
    listbox.pack(pady=10)

    select_button = tk.Button(root, text="Capture", command=select_window, font=("Arial", 12))
    select_button.pack(pady=10)

# Main GUI setup
root = tk.Tk()
root.title("Capture in 3 Seconds")
root.geometry("600x600")

label = tk.Label(root, text="Select a window to capture and click 'Capture'", font=("Arial", 14))
label.pack(pady=10)

capture_window()

root.mainloop()
