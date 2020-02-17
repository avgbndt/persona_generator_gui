from tkinter import *
from tkinter import messagebox
from tkinter import font
from sys import exit
from PIL import Image, ImageTk
import faker
import random
import string
import requests
import shutil
import os
"""Functions"""

# init faker


fake = faker.Faker()
photo = None


def getTemp():
    bytestring = requests.get("https://thispersondoesnotexist.com/image", headers={'User-Agent': 'My User Agent 1.0'}).content
    with open(r'.temp.jpg', 'wb') as temp:
        temp.write(bytestring)


def mountPhoto():
    global photo
    image = Image.open('.temp.jpg')
    image = image.resize((250, 250), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    return photo


def generatePersona():
    getTemp()
    mountPhoto()
    fake_name = fake.name()
    fake_username = ''.join([i[:random.randint(2, 4)] for i in fake_name.lower().split(' ')] + [str(random.randint(1000, 9999))])
    username_text.set(fake_username)
    mail_text.set(''.join([fake_username, "@gmail.com"]))
    password_text.set(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)))
    name_text.set(fake_name)
    address_text.set(fake.address())
    phone_text.set(' '.join(['+001'] + [str(random.randint(100, 999))] + [str(random.randint(100, 999))] + [str(random.randint(100, 999))]))
    X.configure(image=photo)


def closeProgram():
    try:
        clearStuff()
    finally:
        exit()


def clearStuff():
    global photo
    username_text.set('')
    mail_text.set('')
    password_text.set('')
    name_text.set('')
    address_text.set('')
    phone_text.set('')
    photo = None
    os.remove('.temp.jpg')
    X.configure(image=photo)


def savePersona():
    with open('my_personas.txt', 'a') as db:
        db.write(f'''{{
username: "{username_text.get()}",
mail: "{mail_text.get()}",
password: "{password_text.get()}",
full_name: "{name_text.get()}",
address: "{address_text.get()}",
phone: "{phone_text.get()}"
}}, \n''')
    shutil.copy('.temp.jpg', f"{username_text.get().replace(' ','_')}.jpeg")
    clearStuff()


"""GUI"""

app = Tk()
app.configure(background='#37474f')

# fonts
titleFont = font.Font(family='verdana', size=11, weight='bold')
buttonFont = font.Font(family='verdana', size=10, weight='bold')
outputFont1 = font.Font(family='verdana', size=9, weight='bold')
outputFont2 = font.Font(family='verdana', size=8, weight='normal')
signatureFont = font.Font(family='verdana', size=8, weight='normal')
#


# Title
app.title('Random Persona Generator')

# App Icon
app.wm_attributes('-toolwindow', 'true')

# App Title
top_title = Label(app, padx=5, pady=20, fg="#f5f5f5", font=titleFont)
top_title.configure(background='#D32F2F')
top_title.grid(row=0, column=0, columnspan=3, padx=0, pady=0, sticky='wens')

title_caption = Label(top_title, text='Looking for a new name chief?', padx=5, pady=13, fg="#f5f5f5", bg='#D32F2F', font=titleFont)
title_caption.grid(sticky=E)


app.columnconfigure(2, weight=1)
app.rowconfigure(6, weight=1)
top_title.rowconfigure(0, weight=1)
top_title.columnconfigure(0, weight=1)

# workspace
workspace = Frame(app)
workspace.configure(background='#FF5252', relief='sunken')
workspace.grid(row=1, column=0, columnspan=1, rowspan=7, sticky=W + N + S + E)

# workspace credits
signature = Label(workspace, text='By AvgBndt', font=signatureFont, bg='#FF5252', fg='#BDBDBD')

# workspace buttons

generate_btn = Button(workspace, text='Generate', height=4, width=25, command=generatePersona, bg='#F44336', fg="#f5f5f5", font=buttonFont)
generate_btn.configure(border=0)
generate_btn.grid(pady=(20, 10), sticky=W + E)

save_btn = Button(workspace, text='Save', height=4, width=25, command=savePersona, bg='#F44336', fg="#f5f5f5", font=buttonFont)
save_btn.configure(border=0)
save_btn.grid(pady=10, sticky=W + E)

exit_btn = Button(workspace, text='Exit', height=3, width=25, command=closeProgram, bg='#757575', fg="#f5f5f5", font=buttonFont)
exit_btn.configure(border=0)
exit_btn.grid(pady=(300, 10), sticky=W + E)

signature.grid(sticky=S)
# Results
results = Frame(app, padx=1, pady=1)
results.configure(background='#37474f', relief='sunken')
results.grid(row=1, column=1, columnspan=2, rowspan=7, sticky=W + N + S + E)

# Results Fields
# username
username_text = StringVar(results)
username_label = Label(results, text='USERNAME', font=outputFont1, border=0, bg='#37474f', fg='#BDBDBD')
username_label.grid(row=0, column=0, padx=10, pady=40)
username_entry = Entry(results, textvariable=username_text, font=outputFont2, border=0, bg='#37474f', fg='#BDBDBD')
username_entry.grid(row=0, column=1, padx=(50,))
# mail
mail_text = StringVar(results)
mail_label = Label(results, text='MAIL', font=outputFont1, border=0, bg='#37474f', fg='#BDBDBD')
mail_label.grid(row=1, column=0, padx=10, pady=40)
mail_entry = Entry(results, textvariable=mail_text, font=outputFont2, border=0, bg='#37474f', fg='#BDBDBD')
mail_entry.grid(row=1, column=1, padx=(50,))
# pw
password_text = StringVar(results)
password_label = Label(results, text='PASSWORD', font=outputFont1, border=0, bg='#37474f', fg='#BDBDBD')
password_label.grid(row=2, column=0, padx=10, pady=40)
password_entry = Entry(results, textvariable=password_text, font=outputFont2, border=0, bg='#37474f', fg='#BDBDBD')
password_entry.grid(row=2, column=1, padx=(50,))
# name
name_text = StringVar(results)
name_label = Label(results, text='NAME', font=outputFont1, border=0, bg='#37474f', fg='#BDBDBD')
name_label.grid(row=3, column=0, padx=10, pady=40)
name_entry = Entry(results, textvariable=name_text, font=outputFont2, border=0, bg='#37474f', fg='#BDBDBD')
name_entry.grid(row=3, column=1, padx=(50,))
# phone
phone_text = StringVar(results)
phone_label = Label(results, text='PHONE', font=outputFont1, border=0, bg='#37474f', fg='#BDBDBD')
phone_label.grid(row=4, column=0, padx=10, pady=40)
phone_entry = Entry(results, textvariable=phone_text, font=outputFont2, border=0, bg='#37474f', fg='#BDBDBD')
phone_entry.grid(row=4, column=1, padx=(50,))
# address
address_text = StringVar(results)
address_label = Label(results, text='ADDRESS', font=outputFont1, border=0, bg='#37474f', fg='#BDBDBD')
address_label.grid(row=5, column=0, padx=10, pady=40)
address_entry = Entry(results, textvariable=address_text, font=outputFont2, border=0, bg='#37474f', fg='#BDBDBD')
address_entry.grid(columnspan=3, row=5, column=1, padx=(50,), sticky='wens')
# photo

X = Label(results, bg='#37474f')
X.image = None
X.grid(rowspan=6, row=0, column=2, pady=(30,), sticky=N)
# Default Size
app.geometry('900x650')
# Start program
app.mainloop()
