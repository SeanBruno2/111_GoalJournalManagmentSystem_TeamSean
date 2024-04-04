'''
Main Menu

Phase 3
'''
import tkinter as tk

main=tk.Tk()
main.title("Main Meu")
main.geometry("300x300")

btnAdd=tk.Button(text="Add\nEntry")
btnAdd.grid(row=0,column=0,sticky='news')

btnRemove=tk.Button(text="Remove\nEntry")
btnRemove.grid(row=0,column=2,sticky='news')

btnEdit=tk.Button(text="Edit\nEntry")
btnEdit.grid(row=1,column=0,sticky='news')

btnSearch=tk.Button(text="Search\nEntry")
btnSearch.grid(row=1,column=2,sticky='news')

btnExit=tk.Button(text="Exit")
btnExit.grid(row=3,column=1,sticky='N')
