import tkinter as tk

Edit=tk.Tk()
Edit.geometry("550x200")
Edit.title("Remove")


lblDate=tk.Label(Edit,text="Date(mm-dd-yyyy)",font=("Arial",16))
lblDate.grid(row=0,column=0)
entDate=tk.Entry()
entDate.grid(row=1,column=0)

lblNDate=tk.Label(Edit,text="New Date(mm-dd-yyyy)",font=("Arial",16))
lblNDate.grid(row=0,column=1)
entNDate=tk.Entry()
entNDate.grid(row=1,column=1)

lblTime=tk.Label(Edit,text="Time(00:00)",font=("Arial",16))
lblTime.grid(row=2,column=0)
entTime=tk.Entry()
entTime.grid(row=3,column=0)

lblNTime=tk.Label(Edit,text="New Time(00:00)",font=("Arial",16))
lblNTime.grid(row=2,column=1)
entNTime=tk.Entry()
entNTime.grid(row=3,column=1)


lblNDur=tk.Label(Edit,text="New Duration(Minutes)",font=("Arial",16))
lblNDur.grid(row=4,column=1)
entNDur=tk.Entry()
entNDur.grid(row=5,column=1)

lblDes=tk.Label(Edit,text="New Desciption",font=("Arial",16))
lblDes.grid(row=6,column=1)
entDes=tk.Entry()
entDes.grid(row=7,column=1)


btnEdit=tk.Button(Edit,text="Edit")
btnEdit.grid(row=0,column=2)

btnMain=tk.Button(Edit,text="Main Menu")
btnMain.grid(row=1,column=2)

btnExit=tk.Button(Edit,text="Exit")
btnExit.grid(row=2,column=2)
