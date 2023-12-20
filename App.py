import tkinter as tk
from tkinter import ttk, filedialog, Menu, colorchooser
from PIL import Image, ImageTk
import string
import ImageGen as IG
import ctypes
import os
from ttkthemes import ThemedStyle
import webbrowser

currentWallpaper = "" 

def submit():
    global currentWallpaper

    # Fetching values from the UI elements
    selected_bgn = bgn_var.get()
    if selected_bgn == "custom":
        selected_bgn = url_entry.get()

    is_colorful = colorful_var.get()
    selected_sbgn = sbgn_var.get()
    entered_letters = letters_entry.get().upper()
    selected_color = color_var.get()
    selected_type = type_var.get()

    # Check for empty inputs
    if not selected_bgn or (selected_bgn == "custom" and not url_entry.get()):
        set_error("Please select or provide a background.")
        return
    
    if not selected_sbgn:
        set_error("Please enter an effect for the wallpaper.")
        return

    if not entered_letters:
        set_error("Please enter letters for the wallpaper.")
        return
    
    if not selected_color:
        set_error("Please enter a color for the wallpaper.")
        return
    
    if not selected_type:
        set_error("Please enter a letter type.")
        return

    # Verify if the letters are correct
    for letter in entered_letters:
        if letter not in valid_letters:
            set_error(f"Invalid letter: {letter}")
            return

    # Clear any previous errors
    clear_error()

    # Process submission
    path = IG.walpaperPremium(selected_bgn, is_colorful, selected_sbgn, entered_letters.upper(), selected_color, selected_type)
    currentWallpaper = path
    changeWallpaper(path)

def set_error(message):
    error_label.config(text=message)

def clear_error():
    error_label.config(text="")

def changeWallpaper(path):
    # Change the wallpaper on the canvas
    example_image = Image.open(path)
    example_image = example_image.resize((872, 490))
    tk_image = ImageTk.PhotoImage(example_image)
    canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)
    # Keep a reference to tk_image to prevent it from being garbage collected
    canvas.image = tk_image

def open_file_dialog():
    # Open file dialog and set the selected path to the entry widget
    file_path = filedialog.askopenfilename(title="Select Background Image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    url_entry.delete(0, tk.END)
    url_entry.insert(0, file_path)

def set_wallpaper():
    global currentWallpaper

    absolute_path = os.path.abspath(currentWallpaper)
    print("Setting wallpaper to:", absolute_path)

    SPI_SETDESKWALLPAPER = 20
    file_path_unicode = absolute_path.encode('utf-16le') + b'\x00\x00'  # Convert to UTF-16LE
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, file_path_unicode, 3)

# Creating the main window
root = tk.Tk()
root.title("Wallpaper Generator")

# Configure the theme
style = ThemedStyle(root)
style.set_theme("arc")

def open_github():
    webbrowser.open("https://github.com/C0MPL3Xscs/Desktop-Wallpaper-Generator")

def open_PayPal():
    webbrowser.open("https://paypal.me/SamuelSampaio13")

# Menu Bar
menubar = Menu(root)
root.config(menu=menubar)

# App Menu
App_menu = Menu(menubar, tearoff=0)
about_menu = Menu(menubar, tearoff=0)
plugins_menu = Menu(menubar, tearoff=0)
donate_menu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="App", menu=App_menu)
App_menu.add_command(label="Exit", command=root.destroy)

# About Menu
menubar.add_cascade(label="Plugins", menu=plugins_menu)
plugins_menu.add_command(label="Plugins not available yet")

# About Menu
menubar.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="Github", command=open_github)

menubar.add_cascade(label="Donate", menu=donate_menu)
donate_menu.add_command(label="PayPal", command=open_PayPal)

# Container Frame
container_frame = ttk.Frame(root, padding="20")
container_frame.grid(row=0, column=0, padx=20, pady=20, sticky=tk.NSEW)

# Left Frame (Inputs)
left_frame = ttk.Frame(container_frame)
left_frame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.NSEW)

# Dropdown options
bgn_options = ["0","1", "2", "3", "4", "5", "custom"]
sbgn_options = ["0", "1", "2", "3", "4", "5"]
valid_letters = list(string.ascii_uppercase)
valid_letters.append(" ")
type_options = ["1", "2", "3", "4"]

# Variables to store selected values
bgn_var = tk.StringVar()
colorful_var = tk.BooleanVar()
sbgn_var = tk.StringVar()
color_var = tk.StringVar()
type_var = tk.StringVar()

# Label and Dropdown for BGN
bgn_label = ttk.Label(left_frame, text="BackGround:")
bgn_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
bgn_dropdown = ttk.Combobox(left_frame, textvariable=bgn_var, values=bgn_options, state="readonly")
bgn_dropdown.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

# Custom background label and Entry
url_label = ttk.Label(left_frame, text="Background path:")
url_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
url_entry = ttk.Entry(left_frame)
url_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

# Button to open file dialog
browse_button = ttk.Button(left_frame, text="Browse", command=open_file_dialog)
browse_button.grid(row=1, column=2, padx=10, pady=5, sticky=tk.W)

# Toggle Button for Colorful
colorful_label = ttk.Label(left_frame, text="Colorful:")
colorful_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
colorful_checkbox = ttk.Checkbutton(left_frame, variable=colorful_var)
colorful_checkbox.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

# Label and Dropdown for SBGN
sbgn_label = ttk.Label(left_frame, text="Effect:")
sbgn_label.grid(row=3, column=0, padx=10, pady=5, sticky=tk.W)
sbgn_dropdown = ttk.Combobox(left_frame, textvariable=sbgn_var, values=sbgn_options, state="readonly")
sbgn_dropdown.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

# Text Entry for Letters
letters_label = ttk.Label(left_frame, text="Text:")
letters_label.grid(row=4, column=0, padx=10, pady=5, sticky=tk.W)
letters_entry = ttk.Entry(left_frame)
letters_entry.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

# Label and Color Picker for Color
color_label = ttk.Label(left_frame, text="Color:")
color_label.grid(row=5, column=0, padx=10, pady=5, sticky=tk.W)


def choose_color():
    color = colorchooser.askcolor()[1]  # Get the hex value of the selected color
    color_var.set(color)
    
    # Update the color display canvas
    color_display_canvas.delete("all")
    color_display_canvas.create_rectangle(0, 0, 20, 20, fill=color, outline="")

color_picker_button = ttk.Button(left_frame, text="Pick Color", command=choose_color)
color_picker_button.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

color_display_canvas = tk.Canvas(left_frame, width=20, height=20, relief="solid", borderwidth=1)
color_display_canvas.grid(row=5, column=2, padx=10, pady=5, sticky=tk.W)

# Label and Dropdown for Type
type_label = ttk.Label(left_frame, text="Letter Type:")
type_label.grid(row=6, column=0, padx=10, pady=5, sticky=tk.W)
type_dropdown = ttk.Combobox(left_frame, textvariable=type_var, values=type_options, state="readonly")
type_dropdown.grid(row=6, column=1, padx=10, pady=5, sticky=tk.W)

# Label for displaying errors
error_label = ttk.Label(left_frame, text="", foreground="red")
error_label.grid(row=8, column=0, columnspan=2, pady=5)

# Submit Button
submit_button = ttk.Button(left_frame, text="Generate Wallpaper", command=submit)
submit_button.grid(row=7, column=0, columnspan=2, pady=20)


# Submit Button
submit_button = ttk.Button(left_frame, text="Generate Wallpaper", command=submit)
submit_button.grid(row=7, column=0, columnspan=2, pady=20)

# Right Frame (Preview and additional widgets)
right_frame = ttk.Frame(container_frame)
right_frame.grid(row=0, column=1, padx=10, pady=10, sticky=tk.NSEW)

# Label for Preview
preview_label = ttk.Label(right_frame, text="PREVIEW", font=("Helvetica", 16, "bold"))
preview_label.grid(row=0, column=0, pady=0, sticky=tk.NW)

# Canvas for Image Display
canvas = tk.Canvas(right_frame, width=872, height=490)  # Adjusted width
canvas.grid(row=1, column=0, padx=20, pady=20, sticky=tk.NSEW)

# Apply Wallpaper Button
apply_wallpaper_button = ttk.Button(right_frame, text="Apply Wallpaper", command=lambda: set_wallpaper())
apply_wallpaper_button.grid(row=2, column=0, pady=0)

# Example Image (Replace with your image path)
example_image_path = "./defaultWallpaper.png"
example_image = Image.open(example_image_path)
example_image = example_image.resize((872, 490))
tk_image = ImageTk.PhotoImage(example_image)
canvas.create_image(0, 0, anchor=tk.NW, image=tk_image)

# Adjust the window size and center it on the screen
root.update()

# Configure grid weights to make the container frame and canvas expandable
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Run the main loop
root.mainloop()
