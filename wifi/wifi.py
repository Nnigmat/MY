# /usr/bin/python
from os import system
from sys import exit


wishList = [(10, 'wlp3s0-ILITALITSEY'), (9, 'wlp3s0-Innopolis')]


system('ip link set wlp3s0 down')
system('cat ~/.config/pass | sudo -S systemctl stop NetworkManager.service')
system('netctl list > interfaces')

interfaces = open('interfaces', 'r').readlines()

for ifc in sorted([(1, i) for i in interfaces] + wishList, reverse=True):

    system('netctl list > interfaces')

    # Look at the list of all interfaces in netctl and if there exists '*' sign 
    # one of the interfaces is active
    if '*' in open('interfaces').read():
        exit(0)

    # Each time we go through all of the interfaces and try to up it
    system('cat ~/.config/pass | sudo -S netctl start ' + ifc[1])

    # Clear the 'interfaces' file 
    open('interfaces', 'w').close()

system('cat ~/.config/pass | sudo -S netctl start wlp3s0-Innopolis')
