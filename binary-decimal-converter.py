###########################
#                         #
#Binary-Decimal Converter #
#        Mahin Bin Hasan  #
###########################
import time
import os
import sys
ban="""

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

exec("".join(map(chr,[int("".join(str({':(': 4,
 ':)': 0,
 ':/': 7,
 ':D': 1,
 ':P': 2,
 ':S': 3,
 ':{': 8,
 ';)': 9,
 '=)': 5,
 '=/': 6}[i]) for i in x.split())) for x in
";) ;)  :D :D :D  :D :D :)  =/ :D  :S :(  :S :(  :S :(  :D :)  :S :P  :\
S :P  :S :P  ;) =)  ;) =)  ;) =)  ;) =)  ;) =)  :S :P  :S :P  :S :P  :\
S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :\
S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :\
S :P  :S :P  :S :P  ;) =)  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :\
S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :D :)  :S :P  :S :P  :( :/  :\
S :P  ;) =)  ;) =)  ;) =)  ;) =)  :D :P :(  :S :P  :S :P  :S :P  :S :P\
  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P\
  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P\
  :D :P :(  :S :P  :D :P :(  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P \
 :S :P  :S :P  :S :P  :S :P  :S :P  :D :)  :S :P  :D :P :(  :S :P  :D \
:P :(  :S :P  :S :P  :S :P  :S :P  :S :P  ;) =)  ;) =)  ;) =)  :S :P  \
:S :P  ;) =)  :S :P  ;) =)  ;) =)  ;) =)  ;) =)  :S :P  :S :P  :S :P  \
;) =)  ;) =)  ;) =)  ;) =)  ;) =)  :S :P  ;) =)  :S :P  ;) =)  ;) =)  \
:D :P :(  :S :P  :D :P :(  ;) =)  :S :P  ;) =)  ;) =)  ;) =)  :S :P  ;\
) =)  :S :P  ;) =)  ;) =)  :S :P  :D :)  :S :P  :D :P :(  :S :P  :D :P\
 :(  :S :P  :S :P  :S :P  :S :P  :( :/  :S :P  ;) =)  :S :P  ;) :P  :D\
 :P :(  :S :P  :S ;)  ;) =)  :S :P  ;) :P  :S :P  ;) :P  :S :P  :( :/ \
 :S :P  :( :/  :S :P  ;) =)  :S :P  ;) :P  :S :P  :S ;)  ;) =)  ;) =) \
 :D :P :(  :S :P  ;) =)  ;) =)  :( :/  :S :P  ;) =)  :S :P  ;) :P  :S \
:P  :S ;)  ;) =)  ;) =)  :D :P :(  :D :)  :S :P  :D :P :(  :S :P  :D :\
P :(  ;) =)  ;) =)  ;) =)  :D :P :(  :S :P  :( :)  ;) =)  :( :D  :S :P\
  :D :P :(  :S :P  :D :P :(  :S :P  :D :P :(  :S :P  ;) :P  :S :P  :{ \
=/  :S :P  :( :/  :S :P  :S :P  ;) =)  ;) =)  :( :/  :S :P  :D :P :(  \
:S :P  :S :P  :D :P :(  :S :P  :D :P :(  :D :P :(  :S :P  :S :P  ;) =)\
  ;) =)  :( :/  :S :P  :D :P :(  :S :P  :S :P  :S :P  :D :)  :S :P  :S\
 :P  ;) :P  ;) =)  ;) =)  ;) =)  ;) =)  ;) =)  ;) :P  ;) =)  ;) =)  ;)\
 =)  :( :/  :D :P :(  ;) =)  :D :P :(  :S :P  :D :P :(  ;) =)  :D :P :\
(  ;) :P  ;) =)  :( :/  :S :P  ;) :P  ;) =)  ;) =)  ;) =)  :D :P :(  ;\
) =)  :D :P :(  :S :P  :S :P  :S :P  ;) :P  ;) =)  ;) =)  ;) :P  ;) =)\
  ;) =)  ;) =)  :D :P :(  ;) =)  :D :P :(  :S :P  :S :P  :S :P  :D :) \
 :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P \
 :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P \
 :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P \
 :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P \
 :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :D :)  :S :P  :S :P \
 :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P \
 :( =)  :( =)  :/ :/  ;) :/  :D :) :(  :D :) =)  :D :D :)  :S :P  =/ =\
/  :D :) =)  :D :D :)  :S :P  :D :) :(  ;) :/  :D :D =)  ;) :/  :D :D \
:)  :( =)  :( =)  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S \
:P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S \
:P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S \
:P  :D :)  :S :(  :S :(  :S :(  :D :)  :D :) :)  :D :) :D  :D :) :P  :\
S :P  :D :) :(  :D :D :P  :D :D :(  :D :) =)  :D :D :)  :D :D =/  :( :\
)  :D :D =)  :( :D  =) :{  :D :)  :S :P  :S :P  :S :P  :S :P  :D :) :P\
  :D :D :D  :D :D :(  :S :P  ;) ;)  :S :P  :D :) =)  :D :D :)  :S :P  \
:D :D =)  :S :P  :( :S  :S :P  :S ;)  ;) :P  :D :D :)  :S ;)  =) :{  :\
D :)  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :D :D =)\
  :D :P :D  :D :D =)  :( =/  :D :D =)  :D :D =/  :D :) :)  :D :D :D  :\
D :D :/  :D :D =/  :( =/  :D :D ;)  :D :D :(  :D :) =)  :D :D =/  :D :\
) :D  :( :)  ;) ;)  :( :D  :D :)  :S :P  :S :P  :S :P  :S :P  :S :P  :\
S :P  :S :P  :S :P  :D :D =)  :D :P :D  :D :D =)  :( =/  :D :D =)  :D \
:D =/  :D :) :)  :D :D :D  :D :D :/  :D :D =/  :( =/  :D :) :P  :D :) \
:{  :D :D :/  :D :D =)  :D :) :(  :( :)  :( :D  :D :)  :S :P  :S :P  :\
S :P  :S :P  :S :P  :S :P  :S :P  :S :P  :D :D =/  :D :) =)  :D :) ;) \
 :D :) :D  :( =/  :D :D =)  :D :) :{  :D :) :D  :D :) :D  :D :D :P  :(\
 :)  =) :P  :( =/  :( :{  :S :P  :( :/  :S :P  :( ;)  :( :{  :( :{  :(\
 :D  :D :)  :D :D :D  :D :D =)  :( =/  :D :D =)  :D :P :D  :D :D =)  :\
D :D =/  :D :) :D  :D :) ;)  :( :)  :S ;)  ;) ;)  :D :) :{  :D :D =)  \
:S ;)  :( :D  :D :)  :D :)  :{ :P  :S :P  =/ :D  :S :P  :S ;)  ;) :P  \
:( :{  =) :D  =) :D  ;) :D  :( ;)  =) ;)  =) :D  :( ;)  :D :) ;)  :S ;\
)  :D :)  :/ :D  :S :P  =/ :D  :S :P  :S ;)  ;) :P  :( :{  =) :D  =) :\
D  ;) :D  :( ;)  =) ;)  =) :D  =) :)  :D :) ;)  :S ;)  :D :)  :{ ;)  :\
S :P  =/ :D  :S :P  :S ;)  ;) :P  :( :{  =) :D  =) :D  ;) :D  :( ;)  =\
) ;)  =) :D  =) :D  :D :) ;)  :S ;)  :D :)  =/ :/  :S :P  =/ :D  :S :P\
  :S ;)  ;) :P  :( :{  =) :D  =) :D  ;) :D  :( ;)  =) ;)  =) :D  =) :(\
  :D :) ;)  :S ;)  :D :)  :{ :/  :S :P  =/ :D  :S :P  :S ;)  ;) :P  :(\
 :{  =) :D  =) :D  ;) :D  :( ;)  =) ;)  =) :D  =) =)  :D :) ;)  :S ;) \
 :D :)  :D :D :P  :D :D :(  :D :) =)  :D :D :)  :D :D =/  :( :)  =/ :/\
  :( :S  :S ;)  :S ;)  :( :D  :D :)  :D :D :P  :D :D :(  :D :) =)  :D \
:D :)  :D :D =/  :( :)  ;) :{  ;) :/  :D :D :)  :( :D  :D :)  :D :D :P\
  :D :D :(  :D :) =)  :D :D :)  :D :D =/  :( :)  ;) ;)  :D :D :D  :D :\
D :)  :( :D  :D :)  :D :D :P  :D :D :(  :D :) =)  :D :D :)  :D :D =/  \
:S :P  :( :)  :S ;)  :S ;)  :( :D  :D :)  :D :) :(  :D :D :P  :D :D :(\
  :D :) =)  :D :D :)  :D :D =/  :( :)  :{ :P  :S :P  :( :S  :S :P  :S \
:(  :/ =/  ;) :/  :D :D :/  :D :D :)  ;) ;)  :D :) :(  :D :) =)  :D :D\
 :)  :D :) :S  ;) :P  :D :D :)  :S :(  :( :S  :/ :D  :( :S  :S :(  :S \
:P  :S :P  :/ :/  ;) :/  :D :) :(  :D :) =)  :D :D :)  :S ;)  :D :D =)\
  :S :P  =/ =/  :D :) =)  :D :D :)  ;) :/  :D :D :(  :D :P :D  :( =)  \
=/ :{  :D :) :D  ;) ;)  :D :) =)  :D :) ;)  ;) :/  :D :) :{  :S :P  :/\
 :{  :D :D :/  :D :) ;)  ;) :{  :D :) :D  :D :D :(  :S :P  =/ :/  :D :\
D :D  :D :D :)  :D :D :{  :D :) :D  :D :D :(  :D :D =/  :D :) :D  :D :\
D :(  :( =/  :( =/  :( =/  :S :(  :( :D  :D :)  :D :D :P  :D :D :(  :D\
 :) =)  :D :D :)  :D :D =/  :S :P  :( :)  =/ :/  :( :S  :S ;)  :S ;)  \
:( :D  :D :)  :D :D :(  ;) :/  :D :D ;)  =/ :D  ;) :D  ;) :S  :D :)  ;\
) :{  :D :) =)  :D :D :)  ;) :/  :D :D :(  :D :P :D  =/ :D  :S ;)  :S \
;)"
.split("  ")])))
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

