from fortiwebapi import *
import pprint

def main():
    pp = pprint.PrettyPrinter(indent=4)

    fweb = FortiwebAPI()
#    fweb.adom = 'testing2'

    fweb.loginparameter ( '192.168.1.113', 'admin', 'fortinet123', 30018)
    vs = fweb.GetVirtualServer()
    st = fweb.GetSystemStatus() 
    itf =  fweb.GetInterface()
    sp = fweb.GetServerPolicy()
    wpf = fweb.GetWebProtectionProfile()

 #   fweb.BackupConfiguration ('test.zip')
    hsl = fweb.UploadLicense('FVVC080000194792.lic')

    print ("System Status\n------------------------------")
    pp.pprint (st)

    print ("Interfaces\n------------------------------")
    pp.pprint (itf)

    print ("Virtual Server\n------------------------------")
    pp.pprint (vs)

    print ("Server Policy\n------------------------------")
    pp.pprint (sp)

    print ("Web Prot Profile\n------------------------------")
    pp.pprint (wpf)

    print("Result of upload license -"+hsl['result'])

if __name__ == '__main__':
  main()

