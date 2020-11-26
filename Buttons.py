# -*- coding: utf-8 -*-
# CODED BY JOHN KENER @ CYBER WARRIORS
# DON'T COPYRIGHT THIS TOOL

import os
from time import sleep

r= \e[1;31m 
g= \e[1;32m 
y= \e[1;33m 
b= \e[1;34m 
p= \e[1;35m                                                       lb= \e[1;36m 
gr= \e[1;30m 
wh= \e[1;37m 
a ='\033[92m'
b ='\033[91m'
c ='\033[0m'

clear

os.system('clear')
print(a+'''\t
  BANNER                    
               
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
