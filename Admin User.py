'''
Admin User Page

Phase 3
'''
import tkinter as tk

Admin=tk.Tk()
Admin.geometry("550x150")
Admin.title("Admin")


lblUser=tk.Label(Admin,text="Username",font=("Arial",16))
lblUser.grid(row=0,column=0)
entUser=tk.Entry(Admin,text="Username",font=("Arial",16))
entUser.grid(row=1,column=0)

lblPass=tk.Label(Admin,text="Password",font=("Arial",16))
lblPass.grid(row=0,column=1)
entPass=tk.Entry(Admin,text="Password",font=("Arial",16))
entPass.grid(row=1,column=1)

btnAdd=tk.Button(Admin,text="Add\nUser")
btnAdd.grid(row=0,column=2)

btnRemove=tk.Button(Admin,text="Remove\nUser")
btnRemove.grid(row=1,column=2)

btnMain=tk.Button(Admin,text="Main\nMenu")
btnMain.grid(row=2,column=2)

