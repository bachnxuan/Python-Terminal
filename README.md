# Python-Terminal
### -ADD :
1. SEE ON [`TODO`] FILE
2. NEW THEME : POWERSHELL THEME [`PT C:\> `] 
3. NEW GAMES [`FLAPPY BIRD`]
4. NEW COMMAND [`bugrp`] FOR BUG REPORT

### -BUG REPORT SCRIPT (NEW):
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
def bugreport():
	print('\n {0}WARNING: Enable access to less secure apps on your email account.{2} \n {1}https://www.google.com/settings/security/lesssecureapps{2}'.format(RED, GREEN, END))
	smtp_server = "smtp.gmail.com"
	sender_email = input('Type your gmail: ')
	receiver_email = "****@gmail.com"
	password = getpass("Type your password: ")

	message = input('Your bug: ')

	context = ssl.create_default_context()


	with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)
		
#THIS SCRIPT USE GMAIL ACCOUNT 
# **** IS YOUR RECEIVE BUG GMAIL
```

### -HOW TO USE THIS SCRIPT: 
```python
import ****
bugreport()

# **** IS A NAME OF SCRIPT FILE
```
My Github : https://github.com/bachnxuan/
