import tkinter as tk

Search=tk.Tk()
Search.geometry("677x180")
Search.title("Search")


lblDate=tk.Label(Search,text="Date(mm-dd-yyyy)",font=("Arial",16))
lblDate.grid(row=0,column=0)
entDate=tk.Entry()
entDate.grid(row=1,column=0)

lblFound=tk.Label(Search,text="Entry Found",font=("Arial",16))
lblFound.grid(row=3,column=1)
entFound=tk.Entry()
entFound.grid(row=4,column=1)

lblTime=tk.Label(Search,text="Time(00:00)",font=("Arial",16))
lblTime.grid(row=0,column=2)
entTime=tk.Entry()
entTime.grid(row=1,column=2)



btnSearch=tk.Button(Search,text="Search")
btnSearch.grid(row=0,column=3)

btnMain=tk.Button(Search,text="Main Menu")
btnMain.grid(row=1,column=3)

btnExit=tk.Button(Search,text="Exit")
btnExit.grid(row=2,column=3)
