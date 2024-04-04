import tkinter as tk

Remove=tk.Tk()
Remove.geometry("550x140")
Remove.title("Remove")


lblDate=tk.Label(Remove,text="Date(mm-dd-yyyy)",font=("Arial",16))
lblDate.grid(row=0,column=0)
entDate=tk.Entry()
entDate.grid(row=1,column=0)

lblTime=tk.Label(Remove,text="Time(00:00)",font=("Arial",16))
lblTime.grid(row=0,column=1)
entTime=tk.Entry()
entTime.grid(row=1,column=1)


btnRemove=tk.Button(Remove,text="Remove")
btnRemove.grid(row=0,column=2)

btnMain=tk.Button(Remove,text="Main Menu")
btnMain.grid(row=1,column=2)

btnExit=tk.Button(Remove,text="Exit")
btnExit.grid(row=2,column=2)
