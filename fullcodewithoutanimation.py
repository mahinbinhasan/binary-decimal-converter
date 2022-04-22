###########################
#                         #
# Binary-Decimal Converter #
#        Mahin Bin Hasan  #
###########################
ban = """

 ▄▄▄▄    ██▓       ▓█████▄ ▓█████  ▄████▄  
▓█████▄ ▓██▒       ▒██▀ ██▌▓█   ▀ ▒██▀ ▀█  
▒██▒ ▄██▒██▒  ____ ░██   █▌▒███   ▒▓█    ▄ 
▒██░█▀  ░██░ /___/ ░▓█▄   ▌▒▓█  ▄ ▒▓▓▄ ▄██▒
░▓█  ▀█▓░██░       ░▒████▓ ░▒████▒▒ ▓███▀ ░
░▒▓███▀▒░▓          ▒▒▓  ▒ ░░ ▒░ ░░ ░▒ ▒  ░
▒░▒   ░  ▒ ░        ░ ▒  ▒  ░ ░  ░  ░  ▒   
 ░    ░  ▒ ░        ░ ░  ░    ░   ░        
 ░       ░            ░       ░  ░░ ░      
      ░             ░             ░        

"""

import time
import os
import sys
os.system('cls')

R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'
C = '\033[1;36m'
W = '\033[1;37m'
print(C + '')
print(ban)
os.system('pyfiglet Converter')
print('')
print(R + "Launching\n" + G + "  Mahin's Binary-Decimal Number Converter...")
print(C + '')


def convert(string):
    list1 = []
    list1[:0] = string
    return string


def func():
    bina = input(R + 'Enter Binary Number: ' + C)
    binarystring = convert(bina)
    length = len(binarystring)
    number = 0
    l = length
    s = 2
    i = 0
    while i < length:

        m = int(binarystring[i])

        if m == 1:
            if i == length - 1:
                number = number + 1
            else:
                for g in range(1, l - 1):
                    s = 2 * s
                number = number + s
            s = 2
        elif m == 0:
            number = number + 0
            s = 2
        else:
            print("It's not binary!!")
            number = "[Error]"
            break
        i = i + 1
        l = l - 1
    print(G + 'Decimal number:>> ', number)
    yn = int(input(Y + "\nAnother one?\n1.Yes\n2.Exit\n3.Decimal to Binary\n==>>" + C))
    if yn == 1:
        func()
    elif yn == 2:
        os.system('cls')
        print(R + 'Quitting .. ')
        time.sleep(2)
        os.system('cls')
    elif yn == 3:
        dectob()
    else:
        print('Invalid Option')


def dtob(nm):
    global binary
    c = nm // 2
    d = nm % 2
    raw.append(d)
    if c == 0:
        binary = ''
        i = len(raw) - 1
        while i >= 0:
            binary = binary + str(raw[i])
            i = i - 1
    else:
        dtob(c)
    return binary


raw = []
binary = ''


def dectob():
    num = int(input(R + 'Enter Decimal Number: ' + C))
    num = dtob(num)
    print('Binary number :>>', num)
    dn = int(input(Y + "\nAnother one?\n1.Yes\n2.Exit\n3.Binary to Decimal\n==>>" + C))
    if dn == 1:
        dectob()
    elif dn == 2:
        os.system('cls')
        print(R + 'Quitting .. ')
        time.sleep(2)
        os.system('cls')
    elif dn == 3:
        func()
    else:
        print('Invalid Option')


def startup():
    mode = int(input(C + "Select mode :\n1.Binary to Decimal\n2.Decimal to Binary\n3.EXIT\n==>"))
    if mode == 1:
        func()
    elif mode == 2:
        dectob()
    elif mode == 3:
        print(R + 'Quitting .. ')
        time.sleep(2)
        os.system('cls')
    else:
        print(R + 'Invalid Option')
        startup()


startup()
