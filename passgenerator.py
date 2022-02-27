import random
import string
import tkinter
import array

def generate_password():

    count = 0
    while count < 4:

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
        print("".join(passwords))

generate_password()

""" KNOWN ISSUES and TO DO LIST:

1. Create a GUI.

2. Some password is generated with 3 or more of the same symbols or alphabets. For instance, it generated one password with 4 % symbols.

3. Add more functionalities. """




