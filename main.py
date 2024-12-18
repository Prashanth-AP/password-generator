from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters=[random.choice(letters) for _ in range(nr_letters)]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]
    password_list=password_letters+password_symbols+password_numbers
    random.shuffle(password_list)

    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={
        website:{
            "email":email,
            "password":password
        }
              }


    if len(website)==0 or len(password)==0:
        messagebox.showinfo(message="dont let the fields empty")

    # else:
        # is_ok=messagebox.askokcancel(title=website,message=f"These are the details entered:\n"
        #                                              f"Email:{email}\nWebsite:{website}\nPassword:{password}\nAre you okey with the entries ")
    else:
         with open("data.json","w") as data_file:
            json.dump(new_data,data_file)

            data_file.write(f"{website}|{email}|{password}\n|")
            data=json.load(data_file)
            print(data)
            website_entry.delete(0,END)
            password_entry.delete(0,END)



window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
window.minsize(width=300,height=300)
canvas=Canvas(width=200,height=200)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)

website_label=Label(text="website :")
website_label.grid(column=0,row=1)

email_label=Label(text="Email :")
email_label.grid(column=0,row=2)

password_label=Label(text="password :")
password_label.grid(column=0,row=3)

website_entry=Entry(width=50)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()

email_entry=Entry(width=50)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"apprashanth11@gmail.com")

password_entry=Entry(width=21)
password_entry.grid(row=3,column=0,columnspan=2)

password_button=Button(text="Generete Password",command=generate_password)
password_button.grid(row=3,column=2,columnspan=1)
password_button.place(x=230,y=250)


add_button=Button(text="Add",width=36,command=save)
add_button.grid(row=4,column=1,columnspan=2)
add_button.place(x=80,y=280)

window.mainloop()


































