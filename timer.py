"""Egg timer program."""
import time
import os

in_min = input("Enter minute: ")
in_sec = int(in_min) * 60

for x in range(0, in_sec):
    print(in_sec, ' seconds, ', '{0:.1f}'.format(in_sec/60), ' minutes')
    time.sleep(1)
    in_sec -= 1
    os.system('cls') if os.name == 'nt' else os.system('clear')

print(in_sec, ' seconds, ', '{0:.1f}'.format(in_sec/60), ' minutes')
os.system('echo \a')  # plays system bell
# os.system('play -q /usr/share/sounds/gnome/default/alerts/glass.ogg')
