import os
import platform
import sys

pathtocd = ""
print('PYTHON CMD [Based on cmd]')
while True:
    if platform.system() == 'Windows':
        pass
    else:
        print('SORRY, THIS TERMINAL NOT USE FOR THIS OS :(')
        break
    cmdscr = input(f"PYTHON TERMINAL | File: {pathtocd} |=> ")
    os.system(f'cmd /c "{cmdscr}"')
    if cmdscr == 'cd':
        try:
            pathtocd = input('Enter full path >>> ')
            os.chdir(pathtocd)
            print(':) Complete')
        except FileNotFoundError:
            print('The file does not exist')
            pathtocd = ''
    if cmdscr == "exit":
        break

