import random
import string
from tkinter import *

def generate_password():

    count = 0
    while count < 1:

        max_length = 14
        lowercase = list(string.ascii_lowercase)
        uppercase = list(string.ascii_uppercase)
        digits = list(string.digits)
        punctuation = list(string.punctuation)

        combined_set = lowercase + uppercase + digits + punctuation

        rand_lowercase = random.choice(lowercase)
        rand_uppercase = random.choice(uppercase)
        rand_digits = random.choice(digits)
        rand_punctuation = random.choice(punctuation)

        temp = rand_lowercase + rand_uppercase + rand_digits + rand_punctuation
        passwords = []

        for x in range(max_length):
            temp = random.choice(combined_set)
            passwords.append(temp)

            """if temp not in passwords:
                passwords.append(temp)"""

        random.shuffle(passwords)
        count += 1
        final_output = "".join(passwords)
        lbl.config(text=final_output)
        print(final_output)


window = Tk()
window.title("DIY Password Generator")
window.geometry('384x288')
window.resizable(False, False)

lbl = Label(window, text='Generate a 14-Character Password')
lbl.pack(side="top", fill="both", expand="yes")


button = Button(window, text='Generate', command=generate_password)
button.place(x=165, y=170)
window.mainloop()



""" KNOWN ISSUES and TO DO LIST:

1. Create a GUI.

2. Some password is generated with 3 or more of the same symbols or alphabets. For instance, it generated one password with 4 % symbols.

3. Add more functionalities. """




