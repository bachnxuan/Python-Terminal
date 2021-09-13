# -*- coding: utf-8 -*-

from datetime import datetime
from getpass import getpass
from MINESWEEPER import *
from BUGREPORT import *
from FUNCTION import *
import smtplib, ssl
from time import *
import platform
import getpass
import pytube
import psutil
import sys
import os

BLUE, RED, WHITE, YELLOW, MAGENTA, GREEN, END = '\33[94m', '\033[91m', '\33[97m', '\33[93m', '\033[1;35m', '\033[1;32m', '\033[0m'

print('CHECKING SYSTEM...')
if platform.system() == 'Windows':
    pass
else:
    print(f'Sorry, This Terminal Not Use For {platform.system()} :(')
    exit()

pathcache = os.getcwd()
pathtocd = os.getcwd()
pyterver = '3.0 BETA1'
user = os.getlogin()

print('LOADING TERMINAL...')

print('''
██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██╗  ████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗░█████╗░██╗░░░░░
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██║  ╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗██║░░░░░
██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██║  ░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║███████║██║░░░░░
██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████║  ░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██╔══██║██║░░░░░
██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║  ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██║░░██║███████╗
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝
''')
while True:
    cmdscr = input(f"PT {pathtocd}>")
    if cmdscr == 'exit':
        break
    elif cmdscr == 'help':
        print('''PYTHON TERMINAL HELP :
        exit : EXIT THE TERMINAL
        cd : CHANGE DIRECTORY [YOU CAN USE PYTHON TERMINAL FILE SHORTCUT]
        help : OPEN THE PYTHON TERMINAL HELP 
        python : OPEN PYTHON SHELL AND PYTHON PROJECT (NOTE : PLEASE USE PYTHON ADD TO PATH)
        crtuser : CREATE USER
        color : CHANGE COLOR
        sdcolor : SET TO DEFAULT COLOR
        deluser : DELETE USER
        cptinfo : YOUR COMPUTER INFO
        ver : PYTHON TERMINAL VERSION
        del :  DELETE FILE
        copy : COPY FILE
        copyfst : COPY FILE FAST [USING ROBUST COPY]
        ptfschelp : PYTHON TERMINAL FILE SHORTCUT HELP
        speedtst : SPEED TEST
        downvHR : DOWNLOAD VIDEO ON YOUTUBE [HIGH RESOLUTION]
        downvFR : DOWNLOAD VIDEO ON YOUTUBE [FIRST RESOLUTION]
        clear : CLEAR TERMINAL SCREEN
        wsl : WINDOWS SUBSYSTEM FOR LINUX [NOTE : LOGOUT TO EXIT WSL]
        twifi : TURN WIFI ON OR OFF
        plgames : PLAY GAMES
        bugrp : BUG REPORT
        ''')
    elif cmdscr == 'ptfschelp':
        print('''PYTHON TERMINAL FILE SHORTCUT HELP:
        USERF = USER FOLDER
        APPDF = APPDATA FOLDER
        ALOCALF = LOCAL FOLDER
        AROAMF = ROAMING FOLDER
        ALLF = LOCALLOW FOLDER
        SUF = STARTUP FOLDER
        WDF = WINDOWS FOLDER
        SYS32F = SYSTEM32 FOLDER
        SYSW64F = SYSWOW64 FOLDER [FOR 64 BIT MACHINE]
        ''')
    elif cmdscr == 'python':
        print('[1].OPEN THE PYTHON PROJECT    [2].OPEN PYTHON SHELL')
        pyinp = input('[?]: ')
        if pyinp == '1':
            try:
                pjpinp = input('ENTER FULL PROJECT PATH >>> ')
                pjninp = input('ENTER PROJECT NAME >>> ')
                os.system(f'cmd /c "py {pjpinp}\{pjninp}"')
            except FileNotFoundError:
                print('PROJECT NOT EXIST :(')
        if pyinp == '2':
            os.system(f'cmd /c "py"')
    elif cmdscr == 'run':
        run()
    elif cmdscr == 'crtuser':
        createuser()
    elif cmdscr == 'deluser':
        deleteuser()
    elif cmdscr == 'color':
        color = input('INPUT COLOR CODE FORM CMD: ')
        os.system(f'cmd /c "color {color}"')
    elif cmdscr == 'sdcolor':
        os.system('cmd /c "color 07"')
    elif cmdscr == 'cptinfo':
        computerinfo()
    elif cmdscr == 'ver':
        print(f'''
        PYTHON TERMINAL |VER {pyterver}|
        ''')
    elif cmdscr == 'del':
        deletefile()
    elif cmdscr == 'copy':
        copyfile()
    elif cmdscr == 'copyfst':
        copyfilefast()
    elif cmdscr == 'speedtst':
        os.system('cmd /c "speedtest-cli"')
    elif cmdscr == 'downvHR':
        downloadyoutubevideo()
    elif cmdscr == 'downvFR':
        downloadyoutubevideoFR()
    elif cmdscr == 'wsl':
        os.system('cmd /c "wsl"')
    elif cmdscr == 'twifi':
        tonoff = input('Turn wifi (ON or OFF): ')
        if tonoff == 'ON':
            turnwifionoff(onoff='on')
        if tonoff == 'OFF':
            turnwifionoff(onoff='off')
    elif cmdscr == 'plgames':
        print('''LIST OF GAME:
        [1].MINESWEEPER
        [2].FLAPPY BIRD''')
        askgame = input('[?]: ')
        if askgame == '1':
            gamemine()
            print('NOTE : \'Shift + Click\' TO PUT THE FLAGS')
        if askgame == '2':
            gameflappy()
    elif cmdscr == 'bugrp':
        bugreport()
    elif cmdscr == 'clear':
        os.system('cmd /c "cls"')
        print('''
██████╗░██╗░░░██╗████████╗██╗░░██╗░█████╗░███╗░░██╗  ████████╗███████╗██████╗░███╗░░░███╗██╗███╗░░██╗░█████╗░██╗░░░░░
██╔══██╗╚██╗░██╔╝╚══██╔══╝██║░░██║██╔══██╗████╗░██║  ╚══██╔══╝██╔════╝██╔══██╗████╗░████║██║████╗░██║██╔══██╗██║░░░░░
██████╔╝░╚████╔╝░░░░██║░░░███████║██║░░██║██╔██╗██║  ░░░██║░░░█████╗░░██████╔╝██╔████╔██║██║██╔██╗██║███████║██║░░░░░
██╔═══╝░░░╚██╔╝░░░░░██║░░░██╔══██║██║░░██║██║╚████║  ░░░██║░░░██╔══╝░░██╔══██╗██║╚██╔╝██║██║██║╚████║██╔══██║██║░░░░░
██║░░░░░░░░██║░░░░░░██║░░░██║░░██║╚█████╔╝██║░╚███║  ░░░██║░░░███████╗██║░░██║██║░╚═╝░██║██║██║░╚███║██║░░██║███████╗
╚═╝░░░░░░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚══╝  ░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝
        ''')
    elif cmdscr == 'cd':
        try:
            pathtocd = input('Enter path >>> ')
            if pathtocd == 'USERF':
                pathtocd = f'C:\\Users\\{user}'
            if pathtocd == 'APPDF':
                pathtocd = f'C:\\Users\\{user}\\AppData'
            if pathtocd == 'ALOCALF':
                pathtocd = f'C:\\Users\\{user}\\AppData\\Local'
            if pathtocd == 'AROAMF':
                pathtocd = f'C:\\Users\\{user}\\AppData\\Roaming'
            if pathtocd == 'ALLF':
                pathtocd = f'C:\\Users\\{user}\\AppData\\LocalLow'
            if pathtocd == 'SUF':
                pathtocd = f'C:\\Users\\{user}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'
            if pathtocd == 'WDF':
                pathtocd = 'C:\Windows'
            if pathtocd == 'SYS32F':
                pathtocd = 'C:\Windows\System32'
            if pathtocd == 'SYSW64F':
                print('CHECKING SYSTEM...')
                if '32bit' in platform.architecture():
                    print(f'IT\'S NOT FOR {platform.architecture()} :(')
                    print('USE PATH CACHE...')
                    pathtocd = pathcache
                else:
                    pathtocd = 'C:\Windows\SysWOW64'
            os.chdir(pathtocd)
            print(':) Complete')
        except FileNotFoundError:
            print('DIRECTORY NOT EXIST :(')
            print('USE PATH CACHE...')
            pathtocd = pathcache
            os.chdir(pathtocd)
    elif cmdscr == '':
        print('PLEASE TYPE A COMMAND, TYPE \'help\' TO HELP')
    else:
        print('INCORRECT COMMAND, PLEASE TYPE A CORRECT COMMAND, TYPE \'help\' TO HELP')

print('GOOOOOOOOOOOOD BYYYYYYYYYYE !!!!')
