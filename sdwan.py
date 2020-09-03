#!/usr/bin/env python
#License upload using FORTIOSAPI from Github
# tested by TAS 
# to get geoip POST to /geoip/geoip-query/select

import logging
import sys
import pdb

from fortiosapi import FortiOSAPI

formatter = logging.Formatter(
    '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
logger = logging.getLogger('fortiosapi')
hdlr = logging.FileHandler('testfortiosapi.log')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)
filename = 'config-fgt.txt'

def main():

    # Parse for command line argument for fgt ip
    if len(sys.argv) < 2:
        # Requires fgt ip and password
        print ("Please specify fgt ip address")
        exit()

    # Initilize fgt connection
    ip = sys.argv[1]
    try:
        passwd = sys.argv[2]
    except:
        passwd = ''
    #fgt = FGT(ip)

    # Hard coded vdom value for all requests
    vdom = "root"

    # Login to the FGT ip

    fgt = FortiOSAPI()

    fgt.login(ip, 'admin', passwd, verify=False)
    # take note that below srcintf, dstintf, etc is not checked whether it exists or not... it can be error if not exists !

    hasil = fgt.monitor('virtual-wan', 'health-check' )
    
    print (hasil['results'])

    data = { "interface" : "wan1", "seconds" : "120" } 
    hasil = fgt.monitor('virtual-wan', 'interface-log', parameters=data )

    print (hasil['results'])

    fgt.logout()

if __name__ == '__main__':
  main()
