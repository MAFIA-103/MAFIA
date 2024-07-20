import os,platform

os.system("clear")
print('\033[92;1m Join Subscribe My Youtube Channel')
os.system('xdg-open https://www.youtube.com/@zombieyt155')
fbd=platform.architecture()[2]
if fbd=="32bit":
    __import__("FB-DEVIL32")
elif fbd=="64bit":
    __import__("BS")
