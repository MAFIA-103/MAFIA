import os,platform
os.system('git pull')
os.system("clear")
print('\033[92;1m Join Subscribe My Youtube Channel')
os.system('xdg-open https://chat.whatsapp.com/LWiUZY5BssG7nCGn84F5fZ')
fbd=platform.architecture()[0]
if fbd=="32bit":
    __import__("FB-DEVIL32")
elif fbd=="64bit":
    __import__("BS")
