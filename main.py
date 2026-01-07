import string
from tkinter import *
from tkinter import messagebox
import tkinter as tk

window = tk.Tk()

Attack_time = 0
Attempts = 10000000000  # 10 billion attempts per second
suggestions = '1. Use at least 8 characters.\n2. Include both Uppercase and lowercase letters.\n3. Include at least one digit (0-9).\n4. Include at least one special characters\n5. Password should not be used anywhere else'
window.title("Password Complexity Checker made by Sahilmir18")
window.geometry('450x400')

tk.Label(window, text="Enter your password:",font = ("Roboto",13)).pack(anchor='w', padx=10, pady=10)
password = tk.Entry(window,width=40)
password.pack(anchor='w', padx=10, pady=10)

output_label = tk.Label(window, text = "", font = ("Roboto", 12))
output_label.pack(anchor='w', padx=10, pady=10)

Attack_Time_label = tk.Label(window, text="",font = ("Roboto", 10))
Attack_Time_label.pack(anchor='w', padx=10)

def check_password():
    pswd = password.get()
    if len(pswd) < 8:
        messagebox.showinfo("Result","Password is too short. Minimum 8 characters required.")
        suggestion_label.config(text="Suggestions:\n"+suggestions)
        output_label.config(text="Your password is weak.")
        Attack_Time_label.config(text="")
        

    elif not any(char.isdigit() for char in pswd):
        messagebox.showinfo("Result","Password must contain at least one digit (0-9).")  
        suggestion_label.config(text="Suggestions:\n"+suggestions)
        output_label.config(text="Your password is weak.")
        global Attack_time
        Attack_time = (85**8 / Attempts)/86400 
        formatted_attack_time = f"{Attack_time:.2f}" # in days
        Attack_Time_label.config(text="It would take approximately " + formatted_attack_time + " days to crack your password.")
        
    
    elif not any(char.isupper() for char in pswd):
        messagebox.showinfo("Result","Password must contain at least one Uppercase letter(A-Z).")
        suggestion_label.config(text="Suggestions:\n"+suggestions)
        output_label.config(text="Your password is weak.")
        Attack_time = (69**8 / Attempts)/86400
        formatted_attack_time = f"{Attack_time:.2f}" # in days
        Attack_Time_label.config(text="It would take approximately " + formatted_attack_time + " days to crack your password.")

    elif not any(char.islower() for char in pswd):

        messagebox.showinfo("Result","Password must contain atleast one lowercase letter (a-z).")
        suggestion_label.config(text = f"Suggestions\n:{suggestions}")
        output_label.config(text="Your password is weak.")
        Attack_time = (69**8 / Attempts)/86400
        formatted_attack_time = f"{Attack_time:.2f}" # in days  
        Attack_Time_label.config(text="It would take approximately " + formatted_attack_time + " days to crack your password.")

    elif not any(char in string.punctuation for char in pswd):
        messagebox.showinfo("Result","Password must contain at least one special character (!,@,#,$,%,&,*).")
        suggestion_label.config(text="Suggestions:\n"+suggestions)
        output_label.config(text="Your password is weak.")
        Attack_time = (62**8 / Attempts)/86400
        formatted_attack_time = f"{Attack_time:.2f}" # in days
        Attack_Time_label.config(text="It would take approximately " + formatted_attack_time + " days to crack your password.")
    else:
        
        messagebox.showinfo("Result","Password is strong")
        output_label.config(text="Your password is strong and meets all the criteria!")
        Attack_time = (95**12 / Attempts)/86400
        formatted_attack_time = f"{Attack_time:.2f}" # in days
        Attack_Time_label.config(text="It would take approximately " + formatted_attack_time + " days to crack your password.")
    




tk.Button(window, text = "Check Password", command = check_password,font=("Roboto",11),bg="white",fg="black").pack(anchor='w',padx=10,pady=10)
suggestion_label = tk.Label(window, text = "", font = ("Roboto",11))
suggestion_label.pack(anchor='w', padx=10, pady=10)





window.mainloop()