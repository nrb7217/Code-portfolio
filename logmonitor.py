"""
Author: Nathan Belcher
"""

from collections import Counter
import re
import sys
import os

"""
main function of program
takes in program arguements and sets the second argument to the name of the file being read.
"""
def main(argv):

    ############  FILE READING  ###############
    """
    opens logfile, locates the ip addresses listed in the file,
    and counts the number of times the ones that failed occur.
    """
    try:
        filename = sys.argv[1]
        with open(filename) as f_authlog:
            authlog = f_authlog.read() # reads each line of the file
            ip_addresses = Counter(re.findall(r'authentication failure.*?rhost=([0-9.]*)\s', authlog))
            sorted_ips = {}
            #sorts the counted ip addresses by highest to lowest count
            sorted_counts = sorted(ip_addresses, key = ip_addresses.get, reverse = True)

            #populates the sorted_counts list
            for w in sorted_counts:
                sorted_ips[w] = ip_addresses[w]
        
    
        ############  LISTING IP's WITH ATTEMPTS <10 ##############
        print ("Count  IP  Country (top line)")
        """
        if the count for the IP is greater than 10, it prints the count and 
        the ip address in question.
        """
        for ip_address, count in sorted_ips.items():
            if count >= 10:
                print(count, ip_address, os.system("geoiplookup " + ip_address))

    ############  BAD FILE HANDLING  ############   
          
    except:
        os.system('clear')
        sys.exit ("invalid or missing file \n exit code 1")
    
main(sys.argv[1:2])
