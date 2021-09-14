@echo off
python -m pip install --upgrade pip
pip install psutil
pip install speedtest-cli
python -m smtpd -c DebuggingServer -n localhost:1025
python -m pip install git+https://github.com/Zeecka/pytube@fix_1060
python -m pip install --upgrade pytube
