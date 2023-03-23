from tkinter import  *
from tkinter import  messagebox
import  random
import pyperclip
YELLOW = "#f7f5dd"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    ## Hard Level

    nr_letters = random.randint(3,5)
    nr_numbers = random.randint(1,3)
    nr_symbols = random.randint(1,4)

    password_list = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)

    #print (f"Your password is : {password}")
    password_input.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_input.get()
    password = password_input.get()
    email = email_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="OOps",message="Please make sure you haven't left any field empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"You have Entered: \n Email: {email} "
                                f"\n Password as {password} \n Press 'ok' to Save")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website}| {email} | {password} \n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
#window.minsize(width=300, height=300)
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
password_img_logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img_logo)
canvas.grid(column=1,row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0,row=2)
password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

website_input = Entry(width=35)
website_input.grid(column=1,row=1,columnspan=2)
website_input.focus()
email_input = Entry(width=35)
email_input.grid(column=1,row=2,columnspan=2)
email_input.insert(0,"hitesh@gmail.com")
password_input =Entry(width=17)
password_input.grid(column=1,row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2,row=3)
add_button = Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)

mainloop()










