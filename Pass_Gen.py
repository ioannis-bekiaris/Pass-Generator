import random


def password():

    Numbers = "0123456789"
    Alphabet = "abcdefghijklmnopqrstuvwxyz"
    Upper = Alphabet.upper()
    Symbols = "!@#$%^&*()-_=+[]{'}<>\/,.?|"
    c = Numbers+Alphabet+Upper+Symbols
    index = int(input("How many characters do you need? "))

    d = []

    for i in range(index):
        b = random.choice(c)
        d.append(b)
        password = "".join(d)
    print(password)


if __name__ == "__main__":
    password()
