#!/usr/bin/env python
#License upload using FORTIOSAPI from Github
# tested by TAS 
# to get geoip POST to /geoip/geoip-query/select

import logging
import sys
import pdb
import pprint

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
    vdom = "root"

    fgt = FortiOSAPI()

    fgt.login( '192.168.1.99', 'admin', 'tas19751975', verify=False)
    hasil = fgt.monitor('virtual-wan', 'health-check' )
    
    print ("----------------")
    print (pprint.pprint(hasil['results']))
    print ("----------------")

    fgt.logout()

if __name__ == '__main__':
  main()
