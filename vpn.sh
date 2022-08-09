trap 'printf "\n";stop;exit 1' 2


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
echo '1.Do you want to use vpn' | lolcat
echo '<×=<><><><><><><><><><><><><>=×>' | lolcat
echo '2.I dont want to use vpn' | lolcat
echo '<×=<><><><><><><><><><><><><>=×>' | lolcat
echo '3.Exit' | lolcat
echo '<×=<><><><><><><><><><><><><>=×>' | lolcat
read -p $'>>=>\e[0m\en' option

if [[ $option == 1 || $option == 01 ]]; then
python3 stranarmy.py darknet


elif [[ $option == 2 || $option == 02 ]]; then
exit
start1

elif [[ $option == 3 ]]; then
exit 1

else
printf "\e[1;93m Wrong Option!\e[0m\n"
sleep 1
clear
menu
fi
}


banner() {
echo "


 ██▀▀▀▀███▀▀▀▀███▀▀▀▀██
█┌─┐┌─┐█┌─┐┌─┐█┌─┐┌─┐█
█└─┘└─┘█└─┘└─┘█└─┘└─┘█
██▌└┘▐███▌└┘▐███▌└┘▐██
██┼┼┼┼███┼┼┼┼███┼┼┼┼██
██▄▄▄▄███▄▄▄▄███▄▄▄▄██
      ×DarkSearchx
<×=====================×>
  ×StranArmy
<×=====================×>
 
" | lolcat
    
read -p $'Do you wanna use it: Y/N:' option



clear
printf "\n"
}


banner
dependencies
menu