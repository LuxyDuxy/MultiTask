from random import *
import time
import os
clear = lambda: os.system("cls")
clear()
print('What is your password?')
user_pass = input()
clear()
print('Cracking...')
password = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',]
guess = ""
a = 0
while (guess != user_pass):
    guess = ""
    for letter in range(len(user_pass)):
        guess_letter = password[randint(0, 9)]
        guess = guess_letter + guess
    a = a + 1
    b = time.process_time()
    c = round(b)
clear()    
print("Your password is:",guess)
print("It taked",a,"tries and",c,"seconds to crack!")
d = input()
