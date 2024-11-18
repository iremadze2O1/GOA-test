import random
import sys

def password_maker(length, spec_char, numbers):

    numbers = str(numbers)

    if length == 3:
        alpha = "j"
    elif length == 4:
        alpha = "sg"
    elif length == 5:
        alpha = "utr"
    elif length == 6:
        alpha = "afqr"
    elif length == 7:
        alpha = "tiafy"
    elif length == 8:
        alpha = "azfawj"
    elif length == 9:
        alpha = "afvsayj"
    elif length == 10:
        alpha = "rdhkjhtr"
    elif length == 11:
        alpha = "olitrgdsk"
    else:
        print ("to long of a password")
        exit()


    num = random.randint(0,1)
    if num == 0:
        password = spec_char + alpha + numbers
    elif num == 1:
        password = numbers + alpha + spec_char


    print(password)

password_maker(15, "%$" , 78)

