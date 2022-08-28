import time
import sys
import os

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0. / 100)

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)
slowprint("\t\t                                         \033[93mꝈҽէ'ʂ Ɛ×քӀօɾҽ էհҽ 𝘿𝙖𝙧𝙠 𝙒𝙚𝙗\033[97m")
print(" ")
print("1-Do you want to check the above File:")
print("")

print("2-Exit")
print(" ")
print("")
x=input("\033[92m[?] \033[96mEnter any option ==>")
if x==('1') :
               slowprint("")          
               os.system('bash scrap.sh')
               
if x==('2') :
               slowprint("")
               os.system('exit')
               os.system('mpg123 lion.mp3 >/dev/null 2>&1')

  
slowprint("")
slowprint("")


def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(8. / 100)


