# -*- coding: utf-8 -*-
# CODED BY JOHN KENER @ CYBER WARRIORS
# DON'T COPYRIGHT THIS TOOL

import os
from time import sleep

a ='\033[92m'
b ='\033[91m'
c ='\033[0m'


os.system('clear')
print(a+'''\t
 █████╗ ███╗   ███╗ █████╗ ███████╗██╗███╗   ██╗ ██████╗ 
██╔══██╗████╗ ████║██╔══██╗╚══███╔╝██║████╗  ██║██╔════╝ 
███████║██╔████╔██║███████║  ███╔╝ ██║██╔██╗ ██║██║  ███╗
██╔══██║██║╚██╔╝██║██╔══██║ ███╔╝  ██║██║╚██╗██║██║   ██║
██║  ██║██║ ╚═╝ ██║██║  ██║███████╗██║██║ ╚████║╚██████╔╝
╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═══╝ ╚═════╝ 

██████╗ ██╗   ██╗████████╗████████╗ ██████╗ ███╗   ██╗███████╗
██╔══██╗██║   ██║╚══██╔══╝╚══██╔══╝██╔═══██╗████╗  ██║██╔════╝
██████╔╝██║   ██║   ██║      ██║   ██║   ██║██╔██╗ ██║███████╗
██╔══██╗██║   ██║   ██║      ██║   ██║   ██║██║╚██╗██║╚════██║
██████╔╝╚██████╔╝   ██║      ██║   ╚██████╔╝██║ ╚████║███████║
╚═════╝  ╚═════╝    ╚═╝      ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝
                                                              
''') 



print('\n[+] Proses..')
sleep(1)
print(b+'\n[+] making termux properties directory..')
sleep(1)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print(a+'[√] Successfully !')
sleep(1)
print(b+'\n[+] Making setup file..')
sleep(1)

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"

kontol = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
kontol.write(key)
kontol.close() 

sleep(1)
print(a+'[√] Successfull!')
sleep(1)
print(b+'\n[+] Setting up..')
sleep(1)
os.system('termux-reload-settings')
print(a+'[√] Successfull !!') 
