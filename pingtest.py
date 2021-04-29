import subprocess #allows shell command execution
import os
import platform
from time import sleep
import netifaces #this is causing problems, maybe replace with OS


def clear_window():
    #clears window. command based on if system is windows or unix based
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')



def test_start():
    #informs user the test has begun
    print("------------------------------")
    print("**Beginning Test**")
    sleep(2)
    print("5")
    sleep(1)
    print("4")
    sleep(1)
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)

def default_gate():
    gateway = netifaces.gateways() #finds systems' available gateways
    default = gateway['default'][netifaces.AF_INET][0] #finds default gateway from list
    print("default gateway: " + default)

def ping_gateway(): #pings default gateway
    gateway = netifaces.gateways()
    default = gateway['default'][netifaces.AF_INET][0]
    result = os.system("ping " + default + " -c 4")
    if result == 0:
        print("DNS Connection: SUCCESS!" )
    else:
        print("DNS Connection: FAILED!")


def ping_ext(): #pings external server google
    hostname = "google.com"
    result = os.system("ping " + hostname + " -c 4") #might need to change

    if result == 0:
        print("Remote Connection: SUCCESS!")
    else:
        print("Remote Connection: FAILED!")

def ping_dns(): #tests DNS
    dns = "8.8.8.8" #temporary
    result = os.system("ping " + dns + " -c 4")

    if result == 0:
        print("DNS Connection: SUCCESS!" )
    else:
        print("DNS Connection: FAILED!")
    #try using 8.8.8.8 for this part

def end_test():
    #prints end message
    print("**Test Complete!**")
    print("--------------------------")

def main():
    clear_window()
    test_start()
    default_gate()
    sleep(2)
    ping_gateway()
    sleep(2)
    ping_ext()
    sleep(2)
    ping_dns()
    sleep(2)
    end_test()
main()