'''
Add Page

Phase 3
'''
import tkinter as tk

Add=tk.Tk()
Add.geometry("700x180")
Add.title("Add")


lblDate=tk.Label(Add,text="Date(mm-dd-yyyy)",font=("Arial",16))
lblDate.grid(row=0,column=0)
entDate=tk.Entry()
entDate.grid(row=1,column=0)

lblTime=tk.Label(Add,text="Time(00:00)",font=("Arial",16))
lblTime.grid(row=0,column=2)
entTime=tk.Entry()
entTime.grid(row=1,column=2)

lblDuration=tk.Label(Add,text="Duration(In minutes)",font=("Arial",16))
lblDuration.grid(row=2,column=0)
entDuration=tk.Entry()
entDuration.grid(row=3,column=0)

lblDescription=tk.Label(Add,text="Description",font=("Arial",16))
lblDescription.grid(row=4,column=1)
entDescription=tk.Entry()
entDescription.grid(row=5,column=1)

btnAdd=tk.Button(Add,text="Add")
btnAdd.grid(row=0,column=3)

btnMain=tk.Button(Add,text="Main Menu")
btnMain.grid(row=1,column=3)

btnExit=tk.Button(Add,text="Exit")
btnExit.grid(row=2,column=3)

