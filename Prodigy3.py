import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont


def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = not any(char.isupper() for char in password)
    lowercase_error = not any(char.islower() for char in password)
    digit_error = not any(char.isdigit() for char in password)
    special_error = not any(
        char in '!@#$%^&*()_+-=[]{}|;:,.<>?`~' for char in password)

    errors = [length_error, uppercase_error,
              lowercase_error, digit_error, special_error]
    error_count = sum(errors)

    if error_count == 0:
        return "Strong", "#2ecc71"  # Green color
    elif error_count == 1:
        return "Moderate", "#f39c12"  # Orange color
    else:
        return "Weak", "#e74c3c"  # Red color


def check_password():
    password = password_entry.get()
    strength, color = check_password_strength(password)
    feedback_label.config(text=f"Password Strength: {strength}", fg=color)

    suggestion_text = "Suggestions for a strong password:\n\n" \
                      "- Include a mix of uppercase and lowercase letters\n" \
                      "- Add digits and special characters\n" \
                      "- Avoid using common words or phrases\n" \
                      "- Make it at least 8 characters long"
    suggestion_label.config(text=suggestion_text)


root = tk.Tk()
root.title("Password Strength Checker")
root.configure(bg="#1e3799")  # Set background color to dark blue

poppins_font = tkfont.Font(family="Poppins", size=12)

label = tk.Label(root, text="Enter your password:",
                 fg="white", bg="#1e3799", font=poppins_font)
label.pack(pady=10)

password_entry = tk.Entry(root, show="*", font=poppins_font)
password_entry.pack(pady=5, padx=20, fill=tk.BOTH, expand=True)  # Make the input wide and flowing

check_button = tk.Button(root, text="Check Strength",
                         command=check_password, bg="#3498db", fg="white", font=poppins_font)
check_button.pack(pady=10, side=tk.TOP)  # Position the button at the top

preview_label = tk.Label(root, text="Password Preview: ", bg="#1e3799", fg="white", font=poppins_font)
preview_label.pack(pady=5)

feedback_label = tk.Label(root, text="", bg="#1e3799", font=poppins_font)
feedback_label.pack()

suggestion_label = tk.Label(root, text="", bg="#1e3799", fg="white", font=poppins_font, justify=tk.LEFT)
suggestion_label.pack(pady=10)

root.mainloop()
