from tkinter import *
from tkinter import messagebox

def exitPushed():
    app.destroy()

def createPushed():
    name = name_entry.get()
    phone = phone_entry.get()
    date = date_entry.get()
    location = location_entry.get()
    info = info_entry.get()

    if not all([name, phone, date, location, info]):
        messagebox.showwarning("Error", "All fields are required")
        return
    
    event_info = f"{name} - {phone} - {date} - {location} - {info}"
    event_listbox.insert(END, event_info)
    clearPushed()

def clearPushed():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    date_entry.delete(0, END)
    location_entry.delete(0,END)
    info_entry.delete(0,END)

app=Tk()
app.title("Event Management System")
app.geometry("530x530")

appLabel = Label(app,text="UniMap Event Booking",font=("Cooper Black", 16))
appLabel.grid(row=0, column=1, columnspan=1, padx=10, pady=10)

Label(app, text="Name:").grid(row=1, column=0, padx=10, pady=5)
name_entry = Entry(app, width=50)
name_entry.grid(row=1, column=1, padx=10, pady=5)

Label(app, text="Phone:").grid(row=2, column=0, padx=10, pady=5)
phone_entry = Entry(app, width=50)
phone_entry.grid(row=2, column=1, padx=10, pady=5)

Label(app, text="Date:").grid(row=3, column=0, padx=10, pady=5)
date_entry = Entry(app, width=50)
date_entry.grid(row=3, column=1, padx=10, pady=5)

Label(app, text="Location:").grid(row=4, column=0, padx=10, pady=5)
location_entry = Entry(app, width=50)
location_entry.grid(row=4, column=1, padx=10, pady=5)

Label(app, text="Event Info:").grid(row=5, column=0, padx=10, pady=5)
info_entry = Entry(app, width=50)
info_entry.grid(row=5, column=1, padx=10, pady=5)

buttonFrame = Frame(app)
buttonFrame.grid(row=1, column=1, columnspan=3, pady=10)

appButton = Button(app,text="Create",command=createPushed, width=10).grid(row=6, column=0, padx=10, pady=5)
appButton = Button(app,text="Update",width=10).grid(row=6, column=1, padx=10, pady=5)
appButton = Button(app,text="Clear",command=clearPushed,width=10).grid(row=6, column=2, padx=10, pady=5)
appButton = Button(app,text="Exit",command=exitPushed,width=10).grid(row=9, column=2, padx=10, pady=5)
appButton = Button(app,text="Delete",width=10).grid(row=9, column=0, padx=10, pady=5)

event_listbox = Listbox(app, width=60, height=13)
event_listbox.grid(row=8, column=0, columnspan=3, padx=10, pady=10)

app.mainloop()

