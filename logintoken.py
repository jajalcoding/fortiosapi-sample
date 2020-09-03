#!/usr/bin/python
import logging
import pprint

from fortiosapi import FortiOSAPI

formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
logger = logging.getLogger('fortiosapi')
hdlr = logging.FileHandler('testfortiosapi.log')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)

fgt = FortiOSAPI()


def main():
    # Login to the FGT ip
    fgt.debug('on')
    fgthost = '192.168.1.99'
    # token is generated from fortigate > system > administrators > edit restapi admin 
    token = '5gs1yh0cyctttQ5hs3GsHczpxdg6b0'
    fgt.tokenlogin(fgthost,token, verify=False)
    pp = pprint.PrettyPrinter(indent=4)
    resp = fgt.license()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(resp)

if __name__ == '__main__':
    main()
