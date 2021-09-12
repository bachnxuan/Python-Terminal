import os
import getpass
import pytube
import psutil
import platform

discordpath = 'C:\\Users\\Administrator\\AppData\\Local\\Discord\\Update.exe'
chromepath = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
msedgepath = 'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
iepath = 'C:\Program Files\Internet Explorer\iexplore.exe'
firefoxpath = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
def run():
    print('''
    1. Google Chrome
    2. Microsoft Edge
    3. IE
    4. Fire Fox
    5. File Explorer
    6. Discord
    7. More...
    ''')
    runinp = input('[?]: ')
    if runinp == '1':
        os.startfile(chromepath)
    if runinp == '2':
        os.startfile(msedgepath)
    if runinp == '3':
        os.startfile(iepath)
    if runinp == '4':
        os.startfile(firefoxpath)
    if runinp == '5':
        os.system('explorer.exe')
    if runinp == '6':
        os.system(f'cmd /c "{discordpath} --processStart Discord.exe"')
    if runinp == '7':
        runinp1 = input('Enter program path >>> ')
        try:
            os.startfile(runinp)
        except FileNotFoundError:
            print('PROGRAM NOT EXIST :(')
        
def createuser():
    username = input('USER NAME: ')
    userpassquestion = input('ARE YOU WANT TO SET PASSWORD (Y or N): ')
    if userpassquestion == 'Y':
        userpass = getpass.getpass('ENTER THE PASSWORD: ')
        print(f'IS OK ? USER : {username}, PASS: {userpass}')
        user = input('Y or N: ')
        if user == 'Y':
            print('CREATE USER...')
            os.system(f'cmd /c "net user /add {username} {userpass}"')
    if userpassquestion == 'N':
        print(f'IS OK ? USER : {username}')
        print('CREATE USER...')
        os.system(f'cmd /c "net user /add {username}"')


def deleteuser():
    usernamedel = input('ENTER YOUR USER YOU WANT TO DELETE: ')
    usernamedelquestion = input(f'ARE YOU WANT DELETE {usernamedel} (Y or N): ')
    if usernamedelquestion == 'Y':
        os.system(f'cmd /c "net user {usernamedel} /delete"')
    if usernamedelquestion == 'N':
        print(':( DELETE USER NOT COMPLETE')

def deletefile():
    delfile = input('Enter full path: ')
    delfilequest = input(f'Are you want to delete {delfile}: ')
    if delfilequest == 'Y':
        os.system(f'cmd /c "del {delfile}"')
    if delfilequest == 'N':
        print(':( DELETE FILE NOT COMPLETE')

def copyfile():
    source = input('Enter full source path: ')
    dest = input('Enter full destination path: ')
    copyfilequest = input(f'Are you want to copy {source} to {dest} (Y or N): ')
    if copyfilequest == 'Y':
        os.system(f'cmd /c "copy {source} {dest}"')
    if copyfilequest == 'N':
        print(':( COPY FILE NOT COMPLETE')
  
def copyfilefast():
    source = input('Enter full source path: ')
    dest = input('Enter full destination path: ')
    filename = input('Enter file name: ')
    copyfilequest = input(f'Are you want to copy {filename} in {source} to {dest} (Y or N): ')
    if copyfilequest == 'Y':
        os.system(f'cmd /c "robocopy {source} {dest} {filename} /W:1 /R:1 /NFL /MT:128"')
    if copyfilequest == 'N':
        print(':( COPY FILE NOT COMPLETE')

def downloadyoutubevideo():
    url = input('Give URL: ')
    pytube.YouTube(url).streams.get_highest_resolution().download(f'{pathtocd}')
    print(f'THE VIDEO HAVE BEEN DOWNLOAD ON {pathtocd}')

def downloadyoutubevideoFR():
    url = input('Give URL: ')
    pytube.YouTube(url).streams.first().download(f'{pathtocd}')
    print(f'THE VIDEO HAVE BEEN DOWNLOAD ON {pathtocd}')

def turnwifionoff(onoff):
    os.system('cmd /c "netsh interface show interface"')
    if onoff == 'on':
        os.system('cmd /c "netsh interface set interface \'Wifi\' enabled"')
    if onoff == 'off':
        os.system('cmd /c "netsh interface set interface \'Wifi\' disabled"')

def computerinfo():
    def get_size(bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    print("="*40, "System Information", "="*40)
    uname = platform.uname()
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")

    print("="*40, "CPU Info", "="*40)
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

    print("="*40, "Memory Information", "="*40)
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")
    print("="*20, "SWAP", "="*20)
    swap = psutil.swap_memory()
    print(f"Total: {get_size(swap.total)}")
    print(f"Free: {get_size(swap.free)}")
    print(f"Used: {get_size(swap.used)}")
    print(f"Percentage: {swap.percent}%")

    print("="*40, "Disk Information", "="*40)
    print("Partitions and Usage:")
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}")
        print(f"  Used: {get_size(partition_usage.used)}")
        print(f"  Free: {get_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")
    disk_io = psutil.disk_io_counters()
    print(f"Total read: {get_size(disk_io.read_bytes)}")
    print(f"Total write: {get_size(disk_io.write_bytes)}")

    print("="*40, "Network Information", "="*40)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"=== Interface: {interface_name} ===")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"  IP Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"  MAC Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast MAC: {address.broadcast}")
    net_io = psutil.net_io_counters()
    print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
