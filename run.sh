#!/bin/bash

B0="$(printf '\033[100m')" S0="$(printf '\033[30m')"
B1="$(printf '\033[91m')" S1="$(printf '\033[31m')"
B2="$(printf '\033[92m')" S2="$(printf '\033[32m')"
B3="$(printf '\033[93m')" S3="$(printf '\033[33m')"
B4="$(printf '\033[94m')" S4="$(printf '\033[34m')"
B5="$(printf '\033[95m')" S5="$(printf '\033[35m')"
B6="$(printf '\033[96m')" S6="$(printf '\033[36m')"
B7="$(printf '\033[97m')" S7="$(printf '\033[37m')"
R1="$(printf '\033[0;1m')" R0="$(printf '\033[00m')"

trap 'printf "\n";rm -rf .torCache;stop;exit 1' 2

stop() {
  torkill
  if [[ $(uname -o) != *'Android'* ]]; then
    service tor stop
  fi
}
dependencies() {

command -v php > /dev/null 2>&1 || { echo >&2 "I require php but it's not installed. Install it. Aborting."; exit 1; }
command -v curl > /dev/null 2>&1 || { echo >&2 "I require curl but it's not installed. Install it. Aborting."; exit 1; }

}

menu() {
echo '          DarkSearch' | lolcat
echo '         <×====================×>' | lolcat

echo '<×<><><><><><><><><><><><><><><><><><>=×>' | lolcat
echo '        <==StranArmy==>' | lolcat
echo '<×<><><><><><><><><><><><><>><><><><><>×>' | lolcat
echo '1.Do you want to start tor service' | lolcat
echo '<×=<><><><><><><><><><><><><>=×>' | lolcat
echo '2.Do you want to stop tor service' | lolcat
echo '<×=<><><><><><><><><><><><><>=×>' | lolcat
echo '3.Exit' | lolcat
echo '<×=<><><><><><><><><><><><><>=×>' | lolcat
python2 f.py
read -p $'>>=>\e[0m\en' option

torkill() {
pidtor=$(ps aux | grep "tor" | awk '{print $2}')
kill -9 $pidtor>/dev/null 2>&1
}
if [[ $option == 1 || $option == 01 ]]; then
  if [[ $(uname -o) == *'Android'* ]]; then
    if ! hash tor>/dev/null 2>&1; then apt install tor -y; fi
    torkill
    tor >.torCache.txt &
    while true; do
      word=$(cat .torCache.txt | grep -o '100%')
      if [ -z $word ]; then
        printf "\033[?25l"
        printf "\r\033[32mStarting tor service......."
      elif [[ $word == '100%' ]]; then
        printf "\r\033[?12l\033[?25h\033[00m Tor service started successfully......!!\n"
        break
      else
        continue
      fi
    done
  else
    service tor start
  fi
bash vpn.sh
elif [[ $option == 2 || $option == 02 ]]; then
  if [[ $(uname -o) == *'Android'* ]]; then torkill
  else
    service tor stop
  fi
exit
start1

elif [[ $option == 3 ]]; then
bash jai.sh
exit 1

else
printf "\e[1;93m Wrong Option!\e[0m\n"
mpg123 lion.mp3 >/dev/null 2>&1
sleep 1
clear
menu
fi
}

banner() {
chafa -c 16 --color-space din99d --symbols -dot-stipple logo1.jpg
echo "

      ×DarkSearchx
<×=====================×>
  ×StranArmy
<×=====================×>
 
" | lolcat
read -p $'Do you wanna use it: Y/N:' option
clear
sleep 2
echo $B1 'LOADING............COK'
sleep 2
clear
echo $B2 '█▒▒▒▒▒▒▒▒▒10%' 
sleep 0.2
clear
echo $B1 '██▒▒▒▒▒▒▒▒20%' 
sleep 0.2
clear
echo $B2 '███▒▒▒▒▒▒▒30%' 
sleep 0.2
clear
echo $B3 '████▒▒▒▒▒▒40%' 
sleep 0.2
clear
echo $B4 '█████▒▒▒▒▒50%' 
sleep 0.4
clear
echo $B5 '██████▒▒▒▒60%'
sleep 0.2
clear
echo $B6 '███████▒▒▒70%'
sleep 0.2
clear
echo $B7 '████████▒▒80%'
sleep 0.2
clear
echo $B1 '█████████▒90%'
sleep 0.2
clear
echo $B3'██████████100%'
clear
printf "\n"

chafa -c 256 --color-space din99d --symbols -dot-stipple logo5.webp
sleep 0.2
clear
chafa -c 256 --color-space din99d --symbols -dot-stipple logo4.jpeg
sleep 0.2
clear
chafa -c 256 --color-space din99d --symbols -dot-stipple logo5.webp
mpg123 lion.mp3 >/dev/null 2>&1
sleep 0.2
clear

}

macchanger()
{
    macchanger=$1
    cd "${macchanger}" || exit 1
}

banner
dependencies
menu
