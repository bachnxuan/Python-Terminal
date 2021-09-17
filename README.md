# Python-Terminal
### -ADD :
1. SEE ON [`TODO`] FILE
2. NEW THEME : POWERSHELL THEME [`PT C:\> `] 
3. NEW GAMES [`FLAPPY BIRD`]
4. NEW COMMAND [`bugrp`] FOR BUG REPORT

### -LOGIN SCRIPT (NEW):
```python
# -*- coding: utf-8 -*-

import os

def register():
    username_info = input('Enter Your Username: ')
    password_info = input('Enter Your Password: ')

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    print('Register Successfully!')

def login():
    user1 = input('Enter Your Username: ')
    pass1 = input('Enter Your Password: ')

    list_of_files = os.listdir()
    if user1 in list_of_files:
        file1 = open(user1, "r")
        verify = file1.read().splitlines()
        if pass1 in verify:
            login_sucess()

        else:
            password_not_recognised()

    else:
        user_not_found()

def login_sucess():
    print('Login Successfully!') 

def password_not_recognised():
    print('Invalid Password!')

def user_not_found():
    print('User Not Found')

def loginmain():
    print('''
    [1].Register
    [2].Login
    ''')
    askoption = input('[?]: ')
    if askoption == '1':
        register()
    if askoption == '2':
        login()
```

### -HOW TO USE LOGIN SCRIPT:
```python
# -*- coding: utf-8 -*-

from **** import loginmain
loginmain()

# **** IS A NAME OF LOGIN SCRIPT FILE
```

### -BUG REPORT SCRIPT (OLD):
```python
# -*- coding: utf-8 -*-

#IMPORT MODULE
import smtplib, ssl
from getpass import getpass

#PORT FOR SSL
port = 465

#COLORS
BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

#MAIN
def bugrp():
	print('\n {0}WARNING: Enable access to less secure apps on your email account.{2} \n {1}https://www.google.com/settings/security/lesssecureapps{2}'.format(RED, GREEN, END))
	smtp_server = "smtp.gmail.com"
	sender_email = input('Type your gmail: ')
	receiver_email = "****@gmail.com"
	password = getpass("Type your password: ")

	message1 = input('Your bug: ')
	massage = f"A BUG IS : {massage}"

	context = ssl.create_default_context()


	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)
		
#THIS SCRIPT USE GMAIL ACCOUNT 
# **** IS YOUR RECEIVE BUG GMAIL
```

### -HOW TO USE THIS BUG REPORT SCRIPT: 
```python
# -*- coding: utf-8 -*-
form  **** import bugrp
bugrp()

# **** IS A NAME OF BUG REPORT SCRIPT FILE
```

### -CHANGE:
1. I put all the files in the archive

My Github : https://github.com/bachnxuan/

