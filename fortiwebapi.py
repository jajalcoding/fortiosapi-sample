import base64
import requests
import json
import pdb

class FortiwebAPI:

    def __init__(self):
        self.host = None
        self._https = True
        self._logged = False
        self.timeout = 120
        self.cert = None
        self._apitoken = None
        self._license = None
        self.url_prefix = None
        self.headers = None
        self.verify = False
        self.adom = 'root'

    def loginparameter ( self, host, username, password ):
        self.url_prefix = "/api/v1.0/"
        self.host = host+":90"
        if (self.adom == 'root'):
            token = username+":"+password
        else:
            token = username+":"+password+":"+self.adom
            
        self._apitoken = base64.b64encode( token.encode('utf-8') )
        self._apitoken = self._apitoken.decode('utf-8')
        self.headers = { 'Authorization' : self._apitoken }

    def get ( self, nodeurl ):
        finalurl = "https://"+self.host+self.url_prefix+nodeurl
        res = requests.request ( "GET", finalurl, headers = self.headers, verify = self.verify )
        return res
    
    def formathasil(self, teks):
        try:
            resp = json.loads(teks)
            return resp     # return value is a dict python object
        except:
            # that means res.content does not exist (error in general)
            # in that case return raw result TODO fix that with a loop in case of global
            print ("error during json convert format !!")
            return teks

    def GetSystemStatus (self):
        nodeurl = "System/Status/Status"
        hasil = self.get( nodeurl )
        return self.formathasil(hasil.text)

    def GetInterface (self):
        nodeurl = "System/Network/Interface"
        hasil = self.get( nodeurl )
        return self.formathasil(hasil.text)

    def BackupConfiguration (self , namafilezip ):
        nodeurl = "System/Maintenance/BackupConfiguration"
        para = { "type" : 'entire' }
        finalurl = "https://"+self.host+self.url_prefix+nodeurl
        res = requests.get (finalurl, params=para, headers=self.headers, verify=False ) 
        open( namafilezip, 'wb').write(res.content)

    def GetVirtualServer (self):
        nodeurl = 'ServerObjects/Server/VirtualServer'
        hasil = self.get ( nodeurl )
        return self.formathasil(hasil.text)

    def GetServerPolicy (self):
        nodeurl = 'Policy/ServerPolicy/ServerPolicy'
        hasil = self.get ( nodeurl )
        return self.formathasil(hasil.text)

    def GetWebProtectionProfile (self):
        nodeurl = "Policy/WebProtectionProfile/InlineProtectionProfile"
        hasil = self.get (nodeurl)
        return self.formathasil(hasil.text)
    