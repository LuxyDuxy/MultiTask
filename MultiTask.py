pip install pyautogui
pip install keyboard
python

############################################################

import os
clear = lambda: os.system("cls")

############################################################ 

def secret():
    import webbrowser
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    start()

############################################################

def spam():
    clear()
    import pyautogui, time
    print('What to spam?')
    a = input()
    clear()
    print('Delay in seconds between text:')
    d = int(input())
    clear()
    print('How many times to spam?')
    f = int(input())
    clear()
    print('Time in seconds before starting to spam:')
    g = int(input())
    clear()
    time.sleep(g)
    for e in range(f):
        time.sleep(d)
        pyautogui.typewrite(a)
        pyautogui.press('enter')      
    start()

############################################################ 

def start():
    os.system('cls')    
    print('Welcome!')

############################################################ 

def opened():
    os.system('cls') 
    print('Type "help()" for the list of commands!')   
    print('Welcome!')

############################################################ 

def timer():
    import time
    a = 0
    b = 0
    c = 0
    clear()
    print('How many seconds to count:')
    d = int(input())
    for h in range(d):
            clear()
            print(c,':',b,':',a)
            a = a + 1
            time.sleep(1)
            if a == 60:
                a = 0
                b = b + 1  
            if b == 60:
                b = 0
                c = c + 1  
    print('Done!')  

############################################################ 

def github():
    import webbrowser
    webbrowser.open('https://github.com/LuxyDuxy') 
    start()       

############################################################

def mine():
    import webbrowser
    webbrowser.open('https://miner.w3spaces.com')
    start()  

################################################################################################ 

def help():
    clear()
    print('Commands you can use:')
    print('start() - go to beginning of the program')
    print('spam() - spam someone')
    print('timer() - start counting to as many seconds as you want')
    print('github() - go to my GitHub page')
    print('mine() - go to web page that mines Monero with your CPU')
    print('time() - shows the time right now')
    print('reminder() - reminds you of whatever you want in time you want it to remind you')
    print('randomnumber() - picks random number from the number you want to the other number you want')
    print('youtube() - opens youtube')
    print('mother() - asks you "Are you hungry?"')
    print('subtraction() - trains you subtract faster')
    print('addition() - trains you add up faster')
    print('division() - trains you divide faster')
    print('multiplication() - trains you multiply faster')
    print('secret() - secret')
    print('binarycode() - converts anything you want to binary code')
    print('messagingserver() - creates private server for messaging')
    print('messagereader() - shows you sent messages')
    print('messagewriter() - allows you to write messages on the private server')
    

################################################################################################ 

def time():
    import time
    from datetime import datetime
    clear()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time) 

############################################################ 

def randomnumber():
    import random
    clear()
    print('Choose random number from:')
    a = int(input())
    clear()
    print('to:')
    b = int(input())
    clear()
    print(random.randint(a,b))         

############################################################ 

def reminder():
    clear()
    print('How many times to remind:')
    d = int(input())
    clear()
    print('What to remind:')
    a = input()
    clear()
    print('When to remind you in seconds:')
    b = int(input())
    clear()
    for c in range(d):
        import time
        time.sleep(b)
        clear()
        print('It is time for:',a)
        import winsound
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

##############################################################

def youtube():
    import webbrowser
    webbrowser.open('https://youtube.com')
    start()

############################################################ 

def mother():
    import time
    clear()
    print('Are you hungry? yes/no')
    a = input()
    if a == 'no':
        clear()
        print('OK!')
        time.sleep(1.5)
        mother()
    else:
        if a == 'yes':
            clear()
            print('Here you go! Eat some mahune! :)')
            time.sleep(2.5) 
            mother()   
    if a != 'no' or 'yes':
        clear()
        print('Ok, but:')
        time.sleep(1.5)
        mother()

############################################################

def subtraction():
    import random
    import time
    clear()
    print('How many tasks do you want?')
    f = int(input())
    clear()
    print('The highest number can be:')
    n = int(input())
    clear()
    g = 0
    k = 0
    l = f
    m = 0
    for e in range(f):
        a = random.randint(0, n)
        b = random.randint(0, a)
        c = a - b
        k = k + 1
        l = l - 1
        print('Current task:',k)
        print('Tasks left:',l)
        print('Correct answers:',g)
        print('Wrong answers:',m)
        print('How much is:',a,'-',b)
        d = int(input())
        clear()
        if d == c:
            g = g + 1
            print('Current task:',k)
            print('Tasks left:',l)
            print('Correct answers:',g)
            print('Wrong answers:',m)
            print('Correct!')
        else:
            m = m + 1
            print('Current task:',k)
            print('Tasks left:',l)
            print('Correct answers:',g)
            print('Wrong answers:',m)
            print('Wrong, the answer was:',c)    
        time.sleep(3)
        clear()
    clear()
    print('Number of points:',g,'/',f)
    h = g / f 
    i = h * 100
    j = round(i)  
    print('Percentage: ',j,'%',sep = '')
    if j >= 90:
        print('Your grade: A') 
    if j >= 80 and j < 90:
        print('Your grade: B')  
    if j >= 70 and j < 80:
        print('Your grade: C')
    if j >= 60 and j < 70:
        print('Your grade: D')
    if j < 60:
        print('Your grade: F')              

############################################################

def addition():
    import random
    import time
    clear()
    print('How many tasks do you want?')
    f = int(input())
    clear()
    print('The highest number can be:')
    n = int(input())
    clear()
    g = 0
    k = 0
    l = f
    m = 0
    for e in range(f):
        a = random.randint(0, n)
        b = random.randint(0, n)
        c = a + b
        k = k + 1
        l = l - 1
        print('Current task:',k)
        print('Tasks left:',l)
        print('Correct answers:',g)
        print('Wrong answers:',m)
        print('How much is:',a,'+',b)
        d = int(input())
        clear()
        if d == c:
            g = g + 1
            print('Current task:',k)
            print('Tasks left:',l)
            print('Correct answers:',g)
            print('Wrong answers:',m)
            print('Correct!')
        else:
            m = m + 1
            print('Current task:',k)
            print('Tasks left:',l)
            print('Correct answers:',g)
            print('Wrong answers:',m)
            print('Wrong, the answer was:',c)    
        time.sleep(3)
        clear()
    clear()
    print('Number of points:',g,'/',f)
    h = g / f 
    i = h * 100
    j = round(i)  
    print('Percentage: ',j,'%',sep = '') 
    if j >= 90:
        print('Your grade: A') 
    if j >= 80 and j < 90:
        print('Your grade: B')  
    if j >= 70 and j < 80:
        print('Your grade: C')
    if j >= 60 and j < 70:
        print('Your grade: D')
    if j < 60:
        print('Your grade: F') 
         
############################################################

def multiplication():
    import random
    import time
    clear()
    print('How many tasks do you want?')
    f = int(input())
    clear()
    print('The highest number can be:')
    n = int(input())
    clear()
    g = 0
    k = 0
    l = f
    m = 0
    for e in range(f):
        a = random.randint(0, n)
        b = random.randint(0, n)
        c = a * b
        k = k + 1
        l = l - 1
        print('Current task:',k)
        print('Tasks left:',l)
        print('Correct answers:',g)
        print('Wrong answers:',m)
        print('How much is:',a,'x',b)
        d = int(input())
        clear()
        if d == c:
            g = g + 1
            print('Current task:',k)
            print('Tasks left:',l)
            print('Correct answers:',g)
            print('Wrong answers:',m)
            print('Correct!')
        else:
            m = m + 1
            print('Current task:',k)
            print('Tasks left:',l)
            print('Correct answers:',g)
            print('Wrong answers:',m)
            print('Wrong, the answer was:',c)    
        time.sleep(3)
        clear()
    clear()
    print('Number of points:',g,'/',f)
    h = g / f 
    i = h * 100
    j = round(i)  
    print('Percentage: ',j,'%',sep = '')
    if j >= 90:
        print('Your grade: A') 
    if j >= 80 and j < 90:
        print('Your grade: B')  
    if j >= 70 and j < 80:
        print('Your grade: C')
    if j >= 60 and j < 70:
        print('Your grade: D')
    if j < 60:
        print('Your grade: F')  
         
############################################################

def division():
    import random
    import time
    clear()
    print('How many tasks do you want?')
    f = int(input())
    clear()
    print('''(NEEDS TO BE HIGHER THAN 10!)
The highest number can be:''')
    p = int(input())
    clear()
    g = 0
    m = 0
    n = f
    o = 0
    for e in range(f):
        a = random.randint(10, p)
        b = random.randint(0, p)
        c = a // b
        l = a % b
        m = m + 1
        n = n - 1
        print('Current task:',n)
        print('Tasks left:',m)
        print('Correct answers:',g)
        print('Wrong answers:',o)
        print('How much is:',a,':',b)
        d = int(input())
        clear()
        print('Current task:',n)
        print('Tasks left:',m)
        print('Correct answers:',g)
        print('Wrong answers:',o)
        print('What is the rest:')
        k = int(input())
        clear()
        if d == c and k == l:
            g = g + 1
            print('Current task:',n)
            print('Tasks left:',m)
            print('Correct answers:',g)
            print('Wrong answers:',o)
            print('Correct!')
        else:
            o = o + 1
            print('Current task:',n)
            print('Tasks left:',m)
            print('Correct answers:',g)
            print('Wrong answers:',o)
            print('Wrong, the answer was: ',c,'and',l,'was the rest')    
        time.sleep(3)
        clear()
    clear()
    print('Number of points:',g,'/',f)
    h = g / f 
    i = h * 100
    j = round(i)  
    print('Percentage: ',j,'%',sep = '')
    if j >= 90:
        print('Your grade: A') 
    if j >= 80 and j < 90:
        print('Your grade: B')  
    if j >= 70 and j < 80:
        print('Your grade: C')
    if j >= 60 and j < 70:
        print('Your grade: D')
    if j < 60:
        print('Your grade: F')  
         
############################################################

def binarycode():
    clear()
    print('What do you want to turn into binary code?')
    a = input()
    clear()
    c = ' '.join(format(ord(b), '08b') for b in a) 
    print('"'+a+'"',"when converted to binary code is:")
    print(str(c))
        
############################################################

def timeschedule():
    clear()
    print('Number of seconds:')
    a = int(input())
    clear()
    b, a = divmod(a, 60)
    c, b = divmod(b, 60)
    d, c = divmod(c, 24)
    print('That is:')
    print(d,'d ',c,'h ',b,'m ',a,'s ',sep='')

############################################################

def messagingserver():
    import os
    clear = lambda: os.system("cls")
    import socket
    from threading import Thread
    SERVER_HOST = "0.0.0.0"
    SERVER_PORT = 5002
    separator_token = "<SEP>"
    client_sockets = set()
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(5)
    clear()
    print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")
    def listen_for_client(cs):
        while True:
            try:
                msg = cs.recv(1024).decode()
            except Exception as e:
                print(f"[!] Error: {e}")
                client_sockets.remove(cs)
            else:
                msg = msg.replace(separator_token, ":")
            for client_socket in client_sockets:
                client_socket.send(msg.encode())
    while True:
        client_socket, client_address = s.accept()
        print(f"[+] {client_address} connected.")
        client_sockets.add(client_socket)
        t = Thread(target=listen_for_client, args=(client_socket,))
        t.daemon = True
        t.start()
    
############################################################

         
os.system("cls") 
opened()
