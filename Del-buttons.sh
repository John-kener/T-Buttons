# TOOL BY JOHN KENER ( OWNER OF CYBER WARRIORS COMMUNITY )
# DON'T COPYRIGHT 
clear

figlet Delete Buttons |lolcat -a -d 4
echo
echo -e "\e[1;31m                  BY JOHN KENER @ CYBER WARRIORS "
echo
echo
while true; do
    read -p " අලුත් Buttons ටික අයින් කරගන්න ඕනෙද ?  ( y /n )   :-  " yn
    case $yn in
        [Yy]* ) cd && cd .termux && rm -rf termux.properties ; break;;
        [Nn]* ) figlet THANK YOU |lolcat && exit   ;;
        * ) echo "Please answer   yes    or    no.";;
    esac
done
