import pickle
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from datetime import date
import pygame

def exitPushed():
    save_data()
    app.destroy()

def createPushed():
    name = name_entry.get()
    phone =phone_entry.get()
    date = date_entry.get() 
    location = combobox_location.get() if entry_other_location.winfo_ismapped() == 0 else entry_other_location.get()
    info = info_entry.get()

    if not all([name, phone, date, location, info]):
        messagebox.showwarning("Error", "All fields are required")
        return
    if not phone.isdigit():
        messagebox.showerror("Input Error", "Please input numbers only for the phone field")
        return
    
    event_info = f"{name} - {phone} - {date} - {location} - {info}"
    event_listbox.insert(END, event_info)
    events.append(event_info)
    clearPushed()

def clearPushed():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    date_entry.set_date(date.today())
    combobox_location.set("")
    entry_other_location.delete(0, END)
    entry_other_location.grid_remove()
    label_other_location.grid_remove()
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
    if not phone.isdigit():
        messagebox.showerror("Input Error", "Please input numbers only for the phone field")
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
            name, phone, date, *location_parts = parts[:-2]
            location = '-'.join(location_parts)
            info = parts[-1]

        name_entry.delete(0, END)
        name_entry.insert(0, name)
        
        phone_entry.delete(0, END)
        phone_entry.insert(0, phone)
        
        date_entry.set_date(date)

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
        label_other_location.grid(row=6, column=0, padx=10, pady=5, sticky='e')
        entry_other_location.grid(row=6, column=1, padx=10, pady=5, sticky='w')
    
    else:
        label_other_location.grid_remove() 
        entry_other_location.grid_remove()

def manual():
    userManual=Toplevel(app)
    userManual.title('User Manual')
    userManual.geometry("730x400")
    userManual.resizable(False,False)
    userManual.iconbitmap(r"c:\\Users\\Hakim\\Downloads\\195927.ico")

    bg_image_path = "c:\\Users\\Hakim\\Documents\\canselori.jpeg"
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((1000,500),Image.LANCZOS)
    bg_read = ImageTk.PhotoImage(bg_image)

    bg_label_read = Label(userManual, image=bg_read)
    bg_label_read.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label_read.image = bg_read

    table_title = Label(userManual,text="**Make sure to state the correct information before proceeding**", font=("Bahnschrift SemiBold SemiConden", 16), bg="gold")
    table_title.grid(row=0, column=0, padx=10, pady= 10, sticky='n')
    table_title = Label(userManual,text="1. Fill in all the entry boxes then push (Create) button", font=("Bahnschrift SemiBold SemiConden", 12), bg="blue4", fg="white")
    table_title.grid(row=1, column=0, padx=10, pady= 10, sticky='w')
    table_title = Label(userManual,text="2. If you want to see more details about the information, click the (Read) button", font=("Bahnschrift SemiBold SemiConden", 12), bg="blue4", fg="white")
    table_title.grid(row=2, column=0, padx=10, pady= 10, sticky='w')
    table_title = Label(userManual,text="3. If you see any errors, you can update the information by selecting the appropriate item from the listbox\nand entering the correct information.",justify="left", font=("Bahnschrift SemiBold SemiConden", 12), bg="blue4", fg="white")
    table_title.grid(row=3, column=0, padx=10, pady= 10, sticky='w')
    table_title = Label(userManual,text="4. After correcting the problem, click the (Update) button", font=("Bahnschrift SemiBold SemiConden", 12), bg="blue4", fg="white")
    table_title.grid(row=4, column=0, padx=10, pady= 10, sticky='w')
    table_title = Label(userManual,text="5. To delete information, select the appropriate item from the listbox, then click the (Delete) button.", font=("Bahnschrift SemiBold SemiConden", 12), bg="red", fg="white")
    table_title.grid(row=5, column=0, padx=10, pady= 10, sticky='w')
    table_title = Label(userManual,text="6. Once you’re done, click the (Exit) button to save your information. Your data will be saved automatically", font=("Bahnschrift SemiBold SemiConden", 12), bg="blue4", fg="white")
    table_title.grid(row=6, column=0, padx=10, pady= 10, sticky='w')

def Read_event():
    read_window = Toplevel(app)
    read_window.title('Listed Data')
    read_window.geometry("700x400")
    read_window.resizable(False,False)
    read_window.iconbitmap(r"c:\\Users\\Hakim\\Downloads\\195927.ico")

    style = ttk.Style()
    style.configure("Treeview.Heading", foreground="blue4", font=("Bahnschrift SemiBold SemiConden", 10))
    
    bg_image_path = "c:\\Users\\Hakim\\Documents\\canselori.jpeg"
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((800,500),Image.LANCZOS)
    bg_read = ImageTk.PhotoImage(bg_image)

    bg_label_read = Label(read_window, image=bg_read)
    bg_label_read.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label_read.image = bg_read

    table_title = Label(read_window,text="INFORMATION",font=("Cooper Black", 16), bg="gold")
    table_title.grid(row=0, column=0, padx=10, pady= 10)
    table_title = Label(read_window,text="Check your information, and if there is any incorrect information, you can update it later.",
                        font=("Bahnschrift SemiBold SemiConden", 11), bg="blue4", fg="white")
    table_title.grid(row=2, column=0, padx=0, pady= 0)
    table_title = Label(read_window,text="Contact us : 666-666-666-666",
                        font=("Bahnschrift SemiBold SemiConden", 11), bg="blue4", fg="white")
    table_title.grid(row=3, column=0, padx=0, pady= 0)    

    table = ttk.Treeview(read_window,columns=('name','phone','date','location','info'), show= 'headings')
    table.heading('name', text= 'Name')
    table.heading('phone', text= 'Phone')
    table.heading('date', text= 'Date')
    table.heading('location', text= 'Location')
    table.heading('info', text= 'Info')
    table.column('name',width=150)
    table.column('phone',width=80)
    table.column('date',width=80)
    table.column('location',width=155)
    table.column('info',width=240)
    
    table.grid(row=1, column=0, padx=0, pady= 30)
    table.tag_configure("even", foreground= "blue4", background="gold", font=("Bahnschrift SemiBold SemiConden", 10))
    table.tag_configure("odd", foreground= "gold", background="blue4", font=("Bahnschrift SemiBold SemiConden", 10))

    for index in range(event_listbox.size()):
        event = event_listbox.get(index)
        name, phone, date, location, info = event.split(" - ")
        tag = 'even' if index % 2 == 0 else 'odd'
        table.insert('', END, values=(name.strip(), phone.strip(), date.strip(), location.strip(), info.strip()), tags=(tag,))
           

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

def stop():
    pygame.mixer.music.stop()

app=Tk()
app.title("Event Management System")
app.geometry("570x570")
app.resizable(False,False)

app.iconbitmap(r"c:\\Users\\Hakim\\Downloads\\195927.ico")

pygame.mixer.init()
pygame.mixer.music.load("c:\\Users\\Hakim\\Downloads\\unimap song.mp3")
pygame.mixer.music.play(loops=-1)

bg_image = Image.open ("c:\\Users\\Hakim\\Documents\\canselori.jpeg")
bg_image = bg_image.resize((570,570),Image.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = Label(app, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)
bg_label.image = bg_photo

appLabel = Label(app,text="UniMap Event Booking",font=("Cooper Black", 16), bg="gold")
appLabel.grid(row=0, column=1, columnspan=1, padx=10, pady=10)

Label(app, text="Name:", bg="gold" , fg="black", font=("Bahnschrift SemiBold SemiConden", 10)).grid(row=1, column=0, padx=10, pady=5, sticky='e')
name_entry = Entry(app, width=60, font=("Bahnschrift SemiBold SemiConden", 10), bg="gold")
name_entry.grid(row=1, column=1, padx=10, pady=5)

Label(app, text="Phone:", bg="gold" , fg="black", font=("Bahnschrift SemiBold SemiConden", 10)).grid(row=2, column=0, padx=10, pady=5, sticky='e')
phone_entry = Entry(app, width=60, font=("Bahnschrift SemiBold SemiConden", 10), bg="gold")
phone_entry.grid(row=2, column=1, padx=10, pady=5)

Label(app, text="Event Info:", bg="gold" , fg="black", font=("Bahnschrift SemiBold SemiConden", 10)).grid(row=3, column=0, padx=10, pady=5, sticky='e')
info_entry = Entry(app, width=60, font=("Bahnschrift SemiBold SemiConden", 10), bg="gold")
info_entry.grid(row=3, column=1, padx=10, pady=5)

Label(app, text="Date:", bg="gold" , fg="black", font=("Bahnschrift SemiBold SemiConden", 10)).grid(row=4, column=0, padx=10, pady=5, sticky='e')
date_entry = DateEntry(app, width=57, date_pattern='y-mm-dd', font=("Bahnschrift SemiBold SemiConden", 10), background='gold', foreground='blue4', borderwidth=2)
date_entry.grid(row=4, column=1, padx=10, pady=5)

Label(app, text="Location:", bg="gold" , fg="black", font=("Bahnschrift SemiBold SemiConden", 10)).grid(row=5, column=0, padx=10, pady=5, sticky='e')
location_options = ["Dewan Ilmu", "Canselori", "Library", "Cafeteria", "Dewan Kuliah 1", "Dewan Kuliah 2", 
                    "Dewan Kuliah 3", "Dewan Kuliah 4", "Dewan Kuliah 5", "Dewan Kuliah 6", "Dewan Kuliah 7", 
                    "Dewan Kuliah 8", "Dewan Kuliah 9", "Sports Complex", "Computer Lab", "Science Lab", 
                    "Administration Office", "Student Center"]

label_other_location = ttk.Label(app, text="Other:", font=("Bahnschrift SemiBold SemiConden", 10), background="gold")
entry_other_location = ttk.Entry(app, width=60, font=("Bahnschrift SemiBold SemiConden", 10))
label_other_location.grid(row=6, column=0, padx=10, pady=5, sticky='e')
entry_other_location.grid(row=6, column=1, padx=10, pady=5)
label_other_location.grid_remove()
entry_other_location.grid_remove()

location_options.append("Other Location")

combobox_location = ttk.Combobox(app, values=location_options, width=57)
combobox_location.grid(row=5, column=1, padx=10, pady=5, sticky='e')
combobox_location.bind("<<ComboboxSelected>>", on_location_selected)

buttonFrame = Frame(app)
buttonFrame.grid(row=1, column=1, columnspan=3, pady=10)

appButton = Button(app, text="Create",command=createPushed, width=10, font=("Bahnschrift SemiBold SemiConden", 10), bg="blue4", fg="white").grid(row=7, column=0, padx=10, pady=5)
appButton = Button(app, text="Update",command=update_event, width=10, font=("Bahnschrift SemiBold SemiConden", 10), bg="blue4", fg="white").grid(row=7, column=1, padx=10, pady=5)
appButton = Button(app, text="Clear",command=clearPushed,width=10, font=("Bahnschrift SemiBold SemiConden", 10), bg="blue4", fg="white").grid(row=7, column=2, padx=10, pady=5)
appButton = Button(app, text="Exit",command=exitPushed,width=10, font=("Bahnschrift SemiBold SemiConden", 10), bg="blue4", fg="white").grid(row=9, column=2, padx=10, pady=5)
appButton = Button(app, text="Delete", command=delete_event, width=10, font=("Bahnschrift SemiBold SemiConden", 10), bg="blue4", fg="white").grid(row=9, column=0, padx=10, pady=5)
appButton = Button(app, text="Read",command=Read_event,width=10, font=("Bahnschrift SemiBold SemiConden", 10), bg="blue4", fg="white").grid(row=9, column=1, padx=10, pady=5)
appButton = Button(app, text="Stop Song",command=stop,width=10, font=("Bahnschrift SemiBold SemiConden", 10), bg="blue4", fg="white").grid(row=10, column=0, padx=10, pady=5)
appButton = Button(app, text="User Manual",command=manual,width=10, font=("Bahnschrift SemiBold SemiConden", 10), bg="blue4", fg="white").grid(row=10, column=2, padx=10, pady=5)

event_listbox = Listbox(app, width=60, height=11, font=("Bahnschrift SemiBold SemiConden", 10))
event_listbox.grid(row=8, column=0, columnspan=3, padx=10, pady=10)
event_listbox.bind('<<ListboxSelect>>', onSelect)
event_listbox.config(bg="blue4", fg="white")

load_data()
 
for event in events:
    event_listbox.insert(END, event)

app.mainloop()

