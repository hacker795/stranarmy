import time
import sys
import os
import onionsearch
print('''

 ██▀▀▀▀███▀▀▀▀███▀▀▀▀██
█┌─┐┌─┐█┌─┐┌─┐█┌─┐┌─┐█
█└─┘└─┘█└─┘└─┘█└─┘└─┘█
██▌└┘▐███▌└┘▐███▌└┘▐██
██┼┼┼┼███┼┼┼┼███┼┼┼┼██
██▄▄▄▄███▄▄▄▄███▄▄▄▄██
      ×StranArmyx
<×=====================×>
  ×DarkExplorer
<×=====================×>
 
''') 


def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
slowprint("[!] Starting : ")
time.sleep(5)
os.system('clear')
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)
slowprint("    \033[91mOnionSearch")
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0. / 100)
slowprint('''\033[1;31m \033[91m    
 
 ____             _    _____            _                     
|  _ \  __ _ _ __| | _| ____|_  ___ __ | | ___  _ __ ___ _ __ 
| | | |/ _` | '__| |/ /  _| \ \/ / '_ \| |/ _ \| '__/ _ \ '__|
| |_| | (_| | |  |   <| |___ >  <| |_) | | (_) | | |  __/ |   
|____/ \__,_|_|  |_|\_\_____/_/\_\ .__/|_|\___/|_|  \___|_|   
                                 |_|                          
 \033[97m             
''')
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)
slowprint("\t\t                                         \033[93mBy :StranArmy\033[97m")
print(" ")
print("1-Enter the Keyword that you wanna search:")
print("")

print("2-Exit")
print(" ")
print("")
x=input("\033[92m[?] \033[96mEnter any option ==>")
if x==('1') :
               search = input("What are you searching for?")
               slowprint("")
               os.system('onionsearch search --engines onionland tor66 haystack --limit 2 --mp_units 2 --output file.txt')
               print(" ")
               alla=input('press any key to continue')
               os.system('clear') 
               os.system('python3 stranarmy.py')

if x==('2') :
               slowprint("")
               os.system('exit')
                        


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)


