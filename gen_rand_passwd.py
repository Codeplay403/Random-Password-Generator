import random
import os
os.system('clear')

#banner
print("""\033[1;94m
   _______                                          __
  <  / __ \____ ____________      ______  _________/ /
  / / /_/ / __ `/ ___/ ___/ | /| / / __ \/ ___/ __  /
 / / ____/ /_/ (__  |__  )| |/ |/ / /_/ / /  / /_/ /
/_/_/    \__,_/____/____/ |__/|__/\____/_/   \__,_/
                        -code by Devi's Code
""")


lower ="abcdefghijklmnopqrstuvwxyz"
upper ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbol ="[]{}()*;/,._-"
number ="0123456789"
all =lower+upper+symbol+number
length =int(input("Enter the Length of password: "))
password ="".join(random.sample(all,length))
print('')
print("New password         : ",password)
print("Length of charactors : ",len(password))
print('')
