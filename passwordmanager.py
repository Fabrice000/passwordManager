from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


#-----------------------PASSWORD GENERATOR---------------------------------------#
def generate_password():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['&', '#', '{', '[', '(', '|', '-', '_', '^', '@', ')', ']', '}', '=', '+', '/', ':', ',', '?', ';', '.', '!', '%', '*', '$', '^']


    alphabet_chosen = [choice(alphabet) for i in range(randint(8, 10))]
    numbers_chosen = [choice(numbers) for i in range(randint(2, 4))]
    symbols_chosen = [choice(symbols) for i in range(randint(2, 4))]
        
    password_list = alphabet_chosen + numbers_chosen + symbols_chosen    
    
    # fonction pour melanger une liste
    shuffle(password_list)
    password = ''.join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)
#----------------- FIND PASSWORD -----------------------------------#
def find_password():
    website = web_input.get()
    try:
        with open("/home/carlos/Bureau/100 days of python/Day 30/data.json","r") as data:
            data_dict = json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops",message="No data File Found.")
    else:
        if website in data_dict:
            #searched_website = data_dict[website]
            #messagebox.showinfo(title=website,message=f"Email: {searched_website['email']}\nPassword: {searched_website['password']}")
            messagebox.showinfo(title=website,message=f"Email: {data_dict[website]['email']}\nPassword: {data_dict[website]['password']}")
            
        else:
            messagebox.showinfo(title="Oops", message=f"No details for the {website} exists!")
#------------------------- SAVE PASSWORD ---------------------------------------------#
def save_data():
    website = web_input.get()
    email = email_input.get()
    password = password_input.get()
    
    new_data = {
        website:{
            "email":email,
            "password":password,   
        }
    }
    if len(password) == 0 or len(website) == 0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!") 
    else:
        try:
            with open("/home/carlos/Bureau/100 days of python/Day 30/data.json","r") as data:
                json_data = json.load(data)
                
        except FileNotFoundError:
            with open("/home/carlos/Bureau/100 days of python/Day 30/data.json","w") as data:
                json.dump(new_data,data, indent=4)
        else:
            json_data.update(new_data, data)
                
            with open("/home/carlos/Bureau/100 days of python/Day 30/data.json","w") as data:
                json.dump(json_data,data, indent=4)
        finally:
            web_input.delete(0,END)
            password_input.delete(0,END)


#----------------------------- UI SETUP -----------------------#
window = Tk()
window.title("Password Manager")

window.config(padx=40,pady=40)
image = PhotoImage(file="/home/carlos/Bureau/100 days of python/Day 29/image.png")
canvas = Canvas(width=557,height=292)
canvas.create_image(278,146,image=image)
canvas.grid(column=1,row=0)


web_label = Label(text="Website:")
web_label.grid(column=0,row=1)
web_input = Entry(width=68)
web_input.focus()
web_input.grid(column=1,row=1)
search_button = Button(text="Search",padx=-4, width=15,command=find_password)
search_button.grid(column=2,row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)
email_input = Entry(width=85)
email_input.insert(0,"carlittohounkpe@gmail.com")
email_input.grid(column=1,row=2,columnspan=2)
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)
password_input = Entry(width=68)
password_input.grid(column=1,row=3)
password_button = Button(text="Generate Password",padx=-4, command=generate_password)
password_button.grid(column=2,row=3)

add_button = Button(text="Add", width=82, command=save_data)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()