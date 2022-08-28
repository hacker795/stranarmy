trap 'printf "\n";stop;exit 1' 2


dependencies() {

command -v php > /dev/null 2>&1 || { echo >&2 "I require php but it's not installed. Install it. Aborting."; exit 1; }
command -v curl > /dev/null 2>&1 || { echo >&2 "I require curl but it's not installed. Install it. Aborting."; exit 1; }

}
bash red1.sh
echo 'Enter the text File: '
read -p $'>>=>\e[0m\en' username
 
python3  TORsearcher.py $username

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
    
read -p $'Do you wanna Continue: Y/N:' option


clear
printf "\n"
}

bash run.sh

macchanger()
{
    macchanger=$1
    cd "${macchanger}" || exit 1
}

banner
dependencies
menu