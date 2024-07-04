import pickle
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk

def exitPushed():
    save_data()
    app.destroy()

def createPushed():
    name = name_entry.get()
    phone = phone_entry.get()
    date = date_entry.get() 
    location = combobox_location.get() if entry_other_location.winfo_ismapped() == 0 else entry_other_location.get()
    info = info_entry.get()

    if not all([name, phone, date, location, info]):
        messagebox.showwarning("Error", "All fields are required")
        return
    
    event_info = f"{name} - {phone} - {date} - {location} - {info}"
    event_listbox.insert(END, event_info)
    events.append(event_info)
    clearPushed()

def clearPushed():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    date_entry.delete(0, END)
    combobox_location.set("")
    entry_other_location.delete(0, END)
    info_entry.delete(0,END)

def update_event():
    selected_index = event_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Input Error", "Please select an event to update")
        return
    
    name = name_entry.get()
    phone = phone_entry.get()
    date = date_entry.get()
    location = combobox_location.get() if entry_other_location.winfo_ismapped() == 0 else entry_other_location.get()
    info = info_entry.get()

    if not all([name, phone, date, location, info]):
        messagebox.showerror("Input Error", "All fields are required")
        return
    
    updated_event_info = f"{name} - {phone} - {date} - {location} - {info}"
    events[selected_index[0]] = updated_event_info
    event_listbox.delete(selected_index)
    event_listbox.insert(selected_index, updated_event_info)
    clearPushed()

def delete_event():
    selected_index = event_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Input Error", "Please select an event to delete")
        return
    del events[selected_index[0]]
    event_listbox.delete(selected_index[0])
    clearPushed()

def onSelect(event):
    selected_index = event_listbox.curselection()
    if selected_index:
        selected_event = event_listbox.get(selected_index)
        parts = selected_event.split(" - ")

        if len(parts) == 5:
            name, phone, date, location, info = parts
        else:
            # Handle case where there might be extra '-' in event info
            name, phone, date, *location_parts = parts[:-2]
            location = '-'.join(location_parts)
            info = parts[-1]

        name_entry.delete(0, END)
        name_entry.insert(0, name)
        
        phone_entry.delete(0, END)
        phone_entry.insert(0, phone)
        
        date_entry.delete(0, END)
        date_entry.insert(0, date)

        if location in location_options:
            combobox_location.set(location)
            entry_other_location.grid_remove()
            label_other_location.grid_remove()
        else:
            combobox_location.set("Other Location")
            entry_other_location.grid()
            label_other_location.grid()

            entry_other_location.delete(0, END)
            entry_other_location.insert(0, location)

        info_entry.delete(0, END)
        info_entry.insert(0, info)

def on_location_selected(event):
    selected_location = combobox_location.get()
    if selected_location == "Other Location":
        label_other_location.grid(row=5, column=0, padx=10, pady=5, sticky='e')
        entry_other_location.grid(row=5, column=1, padx=10, pady=5, sticky='w')
    else:
        label_other_location.grid_remove()
        entry_other_location.grid_remove()

def Read_event():
    read_window = Toplevel(app)
    read_window.title('Listed Data')
    read_window.geometry("700x400")
    read_window.config(bg="lightblue")
    read_window.resizable(False,False)

    bg_image_path = "C:\GAMBAR WALLPAPER GUI PYTHON\Screenshot 2024-06-27 230131.png"
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((800,500),Image.LANCZOS)
    bg_read = ImageTk.PhotoImage(bg_image)

    bg_label_read = Label(read_window, image=bg_read)
    bg_label_read.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label_read.image = bg_read

    table_title = Label(read_window,text="INFORMATION",font=("Cooper Black", 16))
    table_title.grid(row=0, column=0, padx=10, pady= 10)
    table_title = Label(read_window,text="Check your information and if there has any error information, you can update later :)",font=("Arial Black", 10))
    table_title.grid(row=2, column=0, padx=0, pady= 0)

    table = ttk.Treeview(read_window,columns=('name','phone','date','location','info'), show= 'headings')
    table.heading('name', text= 'Name')
    table.heading('phone', text= 'Phone')
    table.heading('date', text= 'Date')
    table.heading('location', text= 'Location')
    table.heading('info', text= 'Info')
    table.column('name',width=120)
    table.column('phone',width=120)
    table.column('date',width=120)
    table.column('location',width=120)
    table.column('info',width=220)
    
    table.grid(row=1, column=0, padx=0, pady= 30)

    for index in range(event_listbox.size()):
        event = event_listbox.get(index)
        name, phone, date, location, info = event.split(" - ")
        table.insert('', END, values=(name.strip(), phone.strip(), date.strip(), location.strip(), info.strip()))   

def load_data():
    try:
        with open("events.dat", 'rb') as f:
            global events
            events = pickle.load(f)
    except FileNotFoundError:
        events = []

def save_data():
    with open("events.dat", "wb") as f:
        pickle.dump(events,f)


app=Tk()
app.title("Event Management System")
app.geometry("535x545")
app.resizable(False,False)

bg_image = Image.open ("C:\GAMBAR WALLPAPER GUI PYTHON\Screenshot 2024-06-27 230131.png")
bg_image = bg_image.resize((530,540),Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(app, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = bg_photo

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
location_options = ["Dewan Ilmu", "Canselori", "Library", "Cafeteria", "Dewan Kuliah 1", "Dewan Kuliah 2", 
                    "Dewan Kuliah 3", "Dewan Kuliah 4", "Dewan Kuliah 5", "Dewan Kuliah 6", "Dewan Kuliah 7", 
                    "Dewan Kuliah 8", "Dewan Kuliah 9", "Sports Complex", "Computer Lab", "Science Lab", 
                    "Administration Office", "Student Center"]
label_other_location = ttk.Label(app, text="Enter Location:")
entry_other_location = ttk.Entry(app, width=47)
date_entry = Entry(app, width=50)
date_entry.grid(row=3, column=1, padx=10, pady=5)


location_options.append("Other Location")

label_location = ttk.Label(app, text="Select Location:")
label_location.grid(row=4, column=0, padx=10, pady=5, sticky='e')

combobox_location = ttk.Combobox(app, values=location_options, width=47)
combobox_location.grid(row=4, column=1, padx=10, pady=5)
combobox_location.bind("<<ComboboxSelected>>", on_location_selected)
label_other_location.grid(row=5, column=0, padx=10, pady=5, sticky='e')
entry_other_location.grid(row=5, column=1, padx=10, pady=5, sticky='w')
label_other_location.grid_remove()
entry_other_location.grid_remove()

Label(app, text="Event Info:").grid(row=6, column=0, padx=10, pady=5)
info_entry = Entry(app, width=50)
info_entry.grid(row=6, column=1, padx=10, pady=5)

buttonFrame = Frame(app)
buttonFrame.grid(row=1, column=1, columnspan=3, pady=10)

appButton = Button(app, text="Create",command=createPushed, width=10).grid(row=7, column=0, padx=10, pady=5)
appButton = Button(app, text="Update",command=update_event, width=10).grid(row=7, column=1, padx=10, pady=5)
appButton = Button(app, text="Clear",command=clearPushed,width=10).grid(row=7, column=2, padx=10, pady=5)
appButton = Button(app, text="Exit",command=exitPushed,width=10).grid(row=9, column=2, padx=10, pady=5)
appButton = Button(app, text="Delete", command=delete_event, width=10).grid(row=9, column=0, padx=10, pady=5)
appButton = Button(app, text="Read",command=Read_event,width=10).grid(row=9, column=1, padx=10, pady=5)

event_listbox = Listbox(app, width=60, height=13)
event_listbox.grid(row=8, column=0, columnspan=3, padx=10, pady=10)
event_listbox.bind('<<ListboxSelect>>', onSelect)
event_listbox.config(bg="lightskyblue3")

load_data()

for event in events:
    event_listbox.insert(END, event)

app.mainloop()
