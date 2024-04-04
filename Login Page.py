'''
Login Page

Phase 3
'''
import tkinter as tk

login=tk.Tk()
login.title('Login')
login.geometry("500x130")

lblUser=tk.Label(text="Username",font=("Arial",16))
lblUser.grid(row=0,column=0)
entUser=tk.Entry()
entUser.grid(row=1,column=0)

lblPass=tk.Label(text="Password",font=("Arial",16))
lblPass.grid(row=0,column=2)
entPass=tk.Entry()
entPass.grid(row=1,column=2)

btnLogin=tk.Button(text="Login")
btnLogin.grid(row=2,column=1)

btnExit=tk.Button(text="Exit")
btnExit.grid(row=3,column=1)

