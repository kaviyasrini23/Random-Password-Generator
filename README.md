# Password Generator

This is a ""Password Generator"" application built using ""Python"" and ""Tkinter"". The application allows users to create secure, random passwords based on selected criteria, such as including uppercase letters, lowercase letters, digits, and special characters.

# Features

 Select the desired **password length** (minimum of 6 characters, default is 10).
 Choose which types of characters to include in the password:
    Uppercase letters (A-Z)
    Lowercase letters (a-z)  
    Digits (0-9)
    Special characters (!@#$%^&* etc.)   
    Displays the generated password in the GUI.

# How to Run the Application

# Prerequisites

You need to have "Python 3.x" installed on your system. The "tkinter" library is usually included with Python, but you can ensure it’s installed using:

# bash:

pip install tk


# Running the Application

1. Clone this repository or download the Python file to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.
3. Run the following command to start the password generator:

   # bash:
   
    python password_generator.py
    

# GUI Overview

  "Password Length": Enter the desired length of the password (default is 10). The length must be at least 6 characters. 
  "Character Options": Select checkboxes to include uppercase letters, lowercase letters, digits, or special characters in the password.
  "Generate Password Button": Click the "Generate Password" button to create a password with the specified options.
  "Password Display": The generated password will be shown in a text field, where you can copy it for use.

# Example Screenshot

+----------------------------------------+
| Password Length (Default: 10)          |
| +------------------------------------+ |
| | 10                                 | |
| +------------------------------------+ |
| [x] Include Uppercase Letters          |
| [x] Include Lowercase Letters          |
| [ ] Include Digits                     |
| [ ] Include Special Characters         |
|                                        |
| +----------------------------+        |
| | Generate Password           |        |
| +----------------------------+        |
| +------------------------------------+ |
| | GkfjLfaDLq                         | |
| +------------------------------------+ |
+----------------------------------------+



## License

This project is licensed under the MIT License.
