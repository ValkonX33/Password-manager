from cProfile import label
from distutils.cmd import Command
import email
from email import message
from email.mime import image
from mimetypes import common_types
from secrets import choice
from sqlite3 import Row
from tkinter import messagebox

from tkinter import *
from turtle import title
from random import choice,randint,shuffle
import pyperclip
def GenratePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # print("Welcome to the PyPassword Generator!")
    # nr_letters= int(input("How many letters would you like in your password?\n")) 
    # nr_symbols = int(input(f"How many symbols would you like?\n"))
    # nr_numbers = int(input(f"How many numbers would you like?\n"))

    # #Eazy Level - Order not randomised:
    #e.g. 4 letter, 2 symbol, 2 number = JduE&!91


    #Hard Level - Order of characters randomised:
    #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

    password_letters = [choice(letters) for _ in range(randint(8,18))]
    password_symbols =[choice(symbols) for _ in range(randint(2,4))]
    password_numbers =[choice(numbers) for _ in range(randint(2,4))]
    password_list = (password_letters+password_numbers+password_symbols)
    shuffle(password_list)
    # final = list(password)
    # final2 = random.shuffle(final)
    password = "".join(password_list)
    
    input3.insert(0,password)
    pyperclip.copy(password)
def save():
    website = input1.get()
    email= input2.get()
    password = input3.get()

    if len(website)==0 or len(password)==0 or len(email)==0:
        messagebox.showinfo(title="Oops", message="You have left some feilds empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f'Is this Ok?\nEmail:{email} \nPassword:{password}')
        if is_ok:
            
            
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website}|{email}|{password} \n")
                input1.delete(0,END)
                input3.delete(0,END)
            

window = Tk()
# window.minsize(500,400)
window.title("Password Manager")
window.config(padx=50, pady= 50)
canvas  = Canvas(width=200, height=200)
img = PhotoImage(file="tkinter\logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=2)

label1= Label(text="Website: ", font=("Helvetica", 15))
label1.grid(row=1,column=1)


label2 = Label(text="Email/Username: ", font=("Helvetica", 15))
label2.grid(row=2,column=1)

label3 = Label(text="Password: ", font=("Helvetica", 15))
label3.grid(row=3,column=1)

input1 = Entry(width=40,)
input1.grid(row=1, column=2)
input1.focus()
input2= Entry(width=40)
input2.grid(row=2,column=2,)
input3= Entry(width=35)
input3.grid(row=3,column=2)

button1 = Button(text="Genrate Password", command=GenratePassword)
button1.grid(row=3,column=3)
button2 = Button(text="Add", command=save)
button2.grid(row= 4, column=2, columnspan=2)


window.mainloop()