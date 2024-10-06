import tkinter as tk  # Import tkinter for creating GUI applications
from tkinter import messagebox  # Import messagebox for error handling in the GUI
import random  # Import random for random selection of characters
import string  # Import string for character sets (letters, digits, punctuation)

# Function to generate the password
def generate_password():
    try:
        length = int(entry_length.get()) if entry_length.get() else 10  # Default value is 10
    except ValueError:  # Catch invalid numbers
        messagebox.showerror("Error", "Please enter a valid number for password length")
        return

    if length < 6:  # Ensure password length is at least 6
        messagebox.showerror("Error", "Password length should be at least 6 characters")
        return

    characters = ""  # Initialize the character set
    if var_uppercase.get():  # Include uppercase if selected
        characters += string.ascii_uppercase
    if var_lowercase.get():  # Include lowercase if selected
        characters += string.ascii_lowercase
    if var_digits.get():  # Include digits if selected
        characters += string.digits
    if var_special.get():  # Include special characters if selected
        characters += string.punctuation

    if not characters:  # Ensure at least one character type is selected
        messagebox.showerror("Error", "Please select at least one character type")
        return

    password = ''.join(random.choice(characters) for i in range(length))  # Generate the password

    entry_password.delete(0, tk.END)  # Clear the password field
    entry_password.insert(0, password)  # Insert the new password

# Create the main tkinter window
root = tk.Tk()
root.title("Password Generator")  # Set window title
root.geometry("400x350")  # Set the size of the window
root.configure(bg="#7868e6")  # Set the background color to a soft purple

# Label and entry for password length
label_length = tk.Label(root, text="Password Length (Default: 10):", bg="#7868e6", fg="white")
label_length.pack(pady=10)  # Add padding to the label
entry_length = tk.Entry(root, width=20)
entry_length.pack()
entry_length.insert(0, "10")  # Set default value to 10

# Variables for checkbox options
var_uppercase = tk.BooleanVar()
var_lowercase = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_special = tk.BooleanVar()

# Checkboxes for character options
check_uppercase = tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_uppercase, bg="#7868e6", fg="white")
check_uppercase.pack(pady=5)
check_lowercase = tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lowercase, bg="#7868e6", fg="white")
check_lowercase.pack(pady=5)
check_digits = tk.Checkbutton(root, text="Include Digits", variable=var_digits, bg="#7868e6", fg="white")
check_digits.pack(pady=5)
check_special = tk.Checkbutton(root, text="Include Special Characters", variable=var_special, bg="#7868e6", fg="white")
check_special.pack(pady=5)

# Button to generate the password
btn_generate = tk.Button(root, text="Generate Password", command=generate_password)
btn_generate.pack(pady=20)

# Entry field to display the generated password
entry_password = tk.Entry(root, width=30, font=("Courier", 14))  # Use a monospaced font for the password
entry_password.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
