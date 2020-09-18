from fortiwebapi import *
import pprint

def main():
    pp = pprint.PrettyPrinter(indent=4)

    fweb = FortiwebAPI()
#    fweb.adom = 'testing2'

    fweb.loginparameter ( '3.1.211.245', 'admin', 'xxxx')
    vs = fweb.GetVirtualServer()
    st = fweb.GetSystemStatus() 
    itf =  fweb.GetInterface()
    sp = fweb.GetServerPolicy()
    wpf = fweb.GetWebProtectionProfile()

#    fweb.BackupConfiguration ('test.zip')

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
    
if __name__ == '__main__':
  main()
