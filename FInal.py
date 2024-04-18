'''
Title: Goal Journal Managment System

BY: Sean Bruno

About: This program is used to journal your daily tasks that lead to your goals, such as going to the gym
or doing your homework, or going to work. It helps you write down things you have accomplished.
'''
#import all packages needed
import tkinter as tk 
from tkinter import messagebox 
import csv 
import os 
from PIL import Image, ImageTk


#def exit function for login page
def Exit():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):#pops up box if ok to close
        root.destroy()#deystroys window
#def Login function
def login(username, password):
    with open("users.csv", "r") as file:#open csv of login info in read mode
        csv_reader = csv.reader(file)
        for row in csv_reader:#iterate over each row
            if row[0] == username and row[1] == password:#check if username and password match
                return {"username": username, "role": row[2]}# if found return credentials
    return None #if none found , return none

def check_login():
    username = username_var.get() # get value that user entered in a string var
    password = password_var.get()
    user = login(username, password)#call the login function with the right username and password
    if user:
        if user["role"] == "admin":#check if the users role is admin
            messagebox.showinfo("Login Successful", "Welcome Admin!")
            root.withdraw()  
            admin_menu()#calls admin menu to display 
        else:
            messagebox.showinfo("Login Successful", f"Welcome {username}!")
            root.withdraw()  
            user_menu(username)#calls the user menu
    else:
        messagebox.showerror("Login Failed", "Invalid username or password.")

def user_menu(username):#creating the user menu
    user_menu_window = tk.Toplevel(root)
    user_menu_window.title(f"Welcome {username}")
    user_menu_window.configure(bg="slategrey")
    

    user_menu_frame = tk.Frame(user_menu_window,bg="slategrey")
    user_menu_frame.pack(padx=10, pady=10)


    def add_journal_entry():
        title = title_var.get()# get values of entries in stringvar
        date = date_var.get()
        time = time_var.get()
        duration = duration_var.get()
        description = description_var.get()
        entry = f"{title}, {date}, {time}, {duration}, {description}\n" #format the entry string
        journal_file = f"{username}_journal.txt"
        with open(journal_file, "a") as file: #open journal in append mode
            file.write(entry)#write the entry in the txt file
        view_journal()# call the view journal function to update displayed journal entries

    def clear_entry(): #clears the entry boxes
        title_var.set("")
        date_var.set("")
        time_var.set("")
        duration_var.set("")
        description_var.set("")

    def view_journal():
        journal_listbox.delete(0, tk.END)#clears the contents of the listbox
        journal_file = f"{username}_journal.txt"
        if os.path.exists(journal_file):#checks if journal file exists
            with open(journal_file, "r") as file:
                for line in file:
                    entry = line.strip().split(", ")
                    if len(entry) >= 5:#check if entry has less than 5 components
                        title = entry[0]
                        date = entry[1]
                        time = entry[2]
                        journal_listbox.insert(tk.END, f"{title}: {date}, {time}")#display in listbox

    def search_by_date():
        date_to_search = search_entry.get()
        found_entries = []#create empty list
        journal_file = f"{username}_journal.txt" 
        if os.path.exists(journal_file):
            with open(journal_file, "r") as file:
                for line in file:
                    entry = line.strip().split(", ")#split entry by ,
                    if len(entry) >= 5 and date_to_search in entry[1]:#check for 5 components and then for date
                        found_entries.append(entry) #if conditions met append entry

        if found_entries:
            search_result_window = tk.Toplevel(root)#creat window to display results
            search_result_window.title("Search Result")

            for entry in found_entries:
                title, date, time, duration, description = entry
                entry_label = tk.Label(search_result_window, text=f"Title: {title}\nDate: {date}\nTime: {time}\nDuration: {duration}\nDescription: {description}\n")
                entry_label.pack(pady=5)
        else:
            journal_listbox.delete(0, tk.END)#clear entrys in journal list box
            journal_listbox.insert(tk.END, "No entries found for the specified date.")#display no entries found

   
    def edit_selected_entry():
        
        selected_index = journal_listbox.curselection()
        
        
        if not selected_index:
            messagebox.showerror("Error", "No entry selected to edit.")
            return
        
        
        selected_entry = journal_listbox.get(selected_index[0])
        
        
        entry_components = selected_entry.split(", ")
        
        
        edit_window = tk.Toplevel()#create new window to edit
        edit_window.title("Edit Entry")
        edit_window.configure(bg="slategrey")
        
        
        title_var = tk.StringVar(value=entry_components[0] if len(entry_components) >= 1 else "")
        title_label = tk.Label(edit_window, text="Title:",bg="slategrey",fg="white")
        title_label.grid(row=0, column=0, padx=5, pady=5)
        title_entry = tk.Entry(edit_window, textvariable=title_var, width=30,bg="slategrey",fg="white")
        title_entry.grid(row=0, column=1, padx=5, pady=5)
        
        
        date_var = tk.StringVar(value=entry_components[1] if len(entry_components) >= 2 else "")
        date_label = tk.Label(edit_window, text="Date:",bg="slategrey",fg="white")
        date_label.grid(row=1, column=0, padx=5, pady=5)
        date_entry = tk.Entry(edit_window, textvariable=date_var, width=30,bg="slategrey",fg="white")
        date_entry.grid(row=1, column=1, padx=5, pady=5)

        time_var = tk.StringVar(value=entry_components[2] if len(entry_components) >= 3 else "")
        time_label = tk.Label(edit_window, text="Time:",bg="slategrey",fg="white")
        time_label.grid(row=2, column=0, padx=5, pady=5)
        time_entry = tk.Entry(edit_window, textvariable=time_var, width=30,bg="slategrey",fg="white")
        time_entry.grid(row=2, column=1, padx=5, pady=5)

        description_var = tk.StringVar(value=", ".join(entry_components[3:]) if len(entry_components) >= 4 else "")
        description_label = tk.Label(edit_window, text="Description:",bg="slategrey",fg="white")
        description_label.grid(row=3, column=0, padx=5, pady=5)
        description_entry = tk.Entry(edit_window, textvariable=description_var, width=30,bg="slategrey",fg="white")
        description_entry.grid(row=3, column=1, padx=5, pady=5)

        

        def save_changes():
            
            edited_title = title_var.get()#get values entered from above as string var
            edited_date = date_var.get()
            edited_time = time_var.get()
            edited_description = description_var.get()
            
            
            if not edited_title or not edited_date or not edited_time or not edited_description:
                messagebox.showerror("Error", "One or more components are missing.")
                return
            
            #combine the new edited components into an entry            
            edited_entry = ", ".join([edited_title, edited_date, edited_time, edited_description])
            
            
            journal_listbox.delete(selected_index[0])#delete original entry from listbox
            
            
            journal_listbox.insert(selected_index[0], edited_entry)#insert edited entry into listbox
            journal_file= f'{username}_journal.txt'
            
            with open(journal_file, "r") as file:#read all lines in txt
                entries = file.readlines()
            
           
            entries[selected_index[0]] = edited_entry + "\n"#this will rewrite the entries without the old one
            
            
            with open(journal_file, "w") as file:#write the new updated entry
                file.writelines(entries)
            
            
            edit_window.destroy()#closes edit window

                    
                   

        
        save_button = tk.Button(edit_window, text="Save Changes", command=save_changes)
        save_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
        
    def remove_entry():
        selection = journal_listbox.curselection()
        if selection:
            index = int(selection[0])#index of selected item
            journal_listbox.delete(index)#delete selected item from the listbox
            journal_file = f"{username}_journal.txt"
            with open(journal_file, "r") as file:
                lines = file.readlines()
            with open(journal_file, "w") as file:
                for i, line in enumerate(lines):#iterate for all lines
                    if i != index:#check if line is the one removes
                        file.write(line)#write lines that are not the one removed

    def Quit():
        user_menu_window.destroy()#quit from login screen

   

    add_entry_frame = tk.Frame(user_menu_window,bg="slategrey")
    add_entry_frame.pack(pady=10)

    title_label = tk.Label(add_entry_frame, text="Title:",bg="slategrey",fg="white")
    title_label.grid(row=0, column=0, padx=5, pady=5)
    title_var = tk.StringVar()
    title_entry = tk.Entry(add_entry_frame, textvariable=title_var, width=30,bg="slategrey",fg="white")
    title_entry.grid(row=0, column=1, padx=5, pady=5)

    date_label = tk.Label(add_entry_frame, text="Date(mm/dd/yy):",bg="slategrey",fg="white")
    date_label.grid(row=1, column=0, padx=5, pady=5)
    date_var = tk.StringVar()
    date_entry = tk.Entry(add_entry_frame, textvariable=date_var, width=10,bg="slategrey",fg="white")
    date_entry.grid(row=1, column=1, padx=5, pady=5)

    time_label = tk.Label(add_entry_frame, text="Time(hh:mm):",bg="slategrey",fg="white")
    time_label.grid(row=2, column=0, padx=5, pady=5)
    time_var = tk.StringVar()
    time_entry = tk.Entry(add_entry_frame, textvariable=time_var, width=10,bg="slategrey",fg="white")
    time_entry.grid(row=2, column=1, padx=5, pady=5)

    duration_label = tk.Label(add_entry_frame, text="Duration(minutes):",bg="slategrey",fg="white")
    duration_label.grid(row=3, column=0, padx=5, pady=5)
    duration_var = tk.StringVar()
    duration_entry = tk.Entry(add_entry_frame, textvariable=duration_var, width=10,bg="slategrey",fg="white")
    duration_entry.grid(row=3, column=1, padx=5, pady=5)

    description_label = tk.Label(add_entry_frame, text="Description:",bg="slategrey",fg="white")
    description_label.grid(row=4, column=0, padx=5, pady=5)
    description_var = tk.StringVar()
    description_entry = tk.Entry(add_entry_frame, textvariable=description_var, width=40,bg="slategrey",fg="white")
    description_entry.grid(row=4, column=1, padx=5, pady=5, columnspan=4)

    add_entry_btn = tk.Button(add_entry_frame, text="Add Entry", command=add_journal_entry)
    add_entry_btn.grid(row=0, column=5, padx=5, pady=5)

    clear_btn = tk.Button(add_entry_frame, text="Clear Entry", command=clear_entry)
    clear_btn.grid(row=1, column=5, padx=5, pady=5)

    edit_button = tk.Button(add_entry_frame, text="Edit Entry", command=edit_selected_entry)
    edit_button.grid(row=2,column=5)

    remove_btn = tk.Button(add_entry_frame, text="Remove Entry", command=remove_entry)
    remove_btn.grid(row=3,column=5)

    search_frame = tk.Frame(user_menu_window,bg="slategrey")
    search_frame.pack(pady=10)

    search_label = tk.Label(search_frame, text="Search by Date:",bg="slategrey",fg="white")
    search_label.grid(row=0, column=0, padx=5, pady=5)
    search_var = tk.StringVar()
    search_entry = tk.Entry(search_frame, textvariable=search_var, width=15,bg="slategrey",fg="white")
    search_entry.grid(row=0, column=1, padx=5, pady=5)
    search_btn = tk.Button(search_frame, text="Search", command=search_by_date)
    search_btn.grid(row=0, column=2, padx=5, pady=5)

    journal_listbox = tk.Listbox(user_menu_frame, width=50,font=("Arial",16))
    journal_listbox.grid(padx=10, pady=10)

    quit_button = tk.Button(search_frame, text="Log Out", command=Quit)
    quit_button.grid(row=5,column=1)
    
    
    view_journal()

def admin_menu():
    admin_menu_window = tk.Toplevel(root)
    admin_menu_window.title("Admin Menu")
    admin_menu_window.configure(bg="slategrey")

    
    users_frame = tk.Frame(admin_menu_window,bg="slategrey")
    users_frame.pack(padx=10, pady=10)

    def populate_users_list():
        users_listbox.delete(0, tk.END)#clears list box
        with open("users.csv", "r") as file:#opens user info in read
            csv_reader = csv.reader(file)
            for row in csv_reader:
                
                user_info = f"Username: {row[0]}, Password: {row[1]}, Role: {row[2]}"
                users_listbox.insert(tk.END, user_info)#displays users.csv in listbox


    def add_user():
        username = username_var.get()
        password = password_var.get()
        role = role_var.get()
        with open("users.csv", "a") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow([username, password, role])
        populate_users_list()

    def remove_user():
        selection = users_listbox.curselection()
        if selection:
            index = int(selection[0])#gets index
            users_listbox.delete(index)
            with open("users.csv", "r") as file:
                data = list(csv.reader(file))
            with open("users.csv", "w", newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerows(data[:index] + data[index+1:])#writes the users again excluding the one slected

    users_listbox = tk.Listbox(users_frame, width=50)
    users_listbox.pack(padx=10, pady=10)
    populate_users_list()

    add_user_frame = tk.Frame(admin_menu_window,bg="slategrey")
    add_user_frame.pack(pady=10)
    username_lbl = tk.Label(add_user_frame, text="Username:",bg="slategrey",fg="white")
    username_lbl.grid(row=0, column=0, padx=5, pady=5)
    username_var = tk.StringVar()
    username_ent = tk.Entry(add_user_frame, textvariable=username_var, width=30,bg="slategrey",fg="white")
    username_ent.grid(row=0, column=1, padx=5, pady=5)

    password_lbl = tk.Label(add_user_frame, text="Password:",bg="slategrey",fg="white")
    password_lbl.grid(row=1, column=0, padx=5, pady=5)
    password_var = tk.StringVar()
    password_ent = tk.Entry(add_user_frame, textvariable=password_var, width=30,bg="slategrey",fg="white")
    password_ent.grid(row=1, column=1, padx=5, pady=5)

    role_lbl = tk.Label(add_user_frame, text="Role:",bg="slategrey",fg="white")
    role_lbl.grid(row=0, column=2, padx=5, pady=5)
    role_var = tk.StringVar()
    role_ent = tk.Entry(add_user_frame, textvariable=role_var, width=10,bg="slategrey",fg="white")
    role_ent.grid(row=0, column=3, padx=5, pady=5)

    add_user_btn = tk.Button(add_user_frame, text="Add User", command=add_user)
    add_user_btn.grid(row=0, column=4, padx=5, pady=5)

    remove_user_btn = tk.Button(admin_menu_window, text="Remove User", command=remove_user)
    remove_user_btn.pack(pady=5)

    def back_to_Login():
        admin_menu_window.destroy()
        root.deiconify()

    back_to_Login = tk.Button(admin_menu_window, text="Go to Login", command=back_to_Login)
    back_to_Login.pack(pady=5)

    


root = tk.Tk()
root.title("Login")

root.configure(bg="slategrey")

login_frame = tk.Frame(root,bg="slategray")
login_frame.pack(padx=20, pady=20)

image_path = "Mountain.jpg"
image = Image.open(image_path)
tk_image = ImageTk.PhotoImage(image)
label = tk.Label(login_frame, image=tk_image)
label.grid(row=0,column=1,padx=5,pady=5)

username_lbl = tk.Label(login_frame, text="Username:",bg="slategray",fg="white")
username_lbl.grid(row=1, column=0, padx=5, pady=5)
username_var = tk.StringVar()
username_ent = tk.Entry(login_frame, textvariable=username_var, width=30,bg="slategray",fg="white")
username_ent.grid(row=1, column=1, padx=5, pady=5)

password_lbl = tk.Label(login_frame, text="Password:",bg="slategray",fg="white")
password_lbl.grid(row=2, column=0, padx=5, pady=5)
password_var = tk.StringVar()
password_ent = tk.Entry(login_frame, textvariable=password_var, show="*", width=30,bg="slategray",fg="white")
password_ent.grid(row=2, column=1, padx=5, pady=5)

login_btn = tk.Button(login_frame, text="Login", command=check_login)
login_btn.grid(row=1, column=2, padx=5, pady=5)

exit_btn=tk.Button(login_frame, text="Exit",command=Exit)
exit_btn.grid(row=2,column=2,padx=5,pady=5)

title_lbl=tk.Label(login_frame,text="GOAL JOURNAL",font=("Arial",20),bg="slategray",fg="white")
title_lbl.grid(row=3,column=1)

root.mainloop()
