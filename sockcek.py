#!/usr/bin/python3

# module
import requests as r
from bs4 import BeautifulSoup as Bs
from time import sleep
import re
from os import system as cmd
import sys

class sokcek():
      def __init__(self,inputIp):
         dat = {'ip':inputIp,"submit":"IP search","xip1":1,"xip2":2}
         res = r.post(url='http://spys.one/ipinfo/',data=dat,headers={'User-Agent':'bang-tebe version 1.0'})
         bs = Bs(res.text,'html.parser')
         for whois in bs.findAll('tr' ,class_='spy1x'):
             if 'OK!' in whois.text:pass
             elif 'IP address:PortTypeAdd' in whois.text:pass
             elif 'IPs found (Max=' in whois.text:pass
             elif 'Location=' in whois.text:
                  try:
                      print()
                      print('GeoIp      :',dat['ip'])
                      try:
                          print('Country    :',re.findall(r'Country (.*?)Region',whois.text)[0])
                      except:pass
                      try:
                          print('Region     :',re.findall(r'Region  (.*?)TimeZone=',whois.text)[0])
                      except:pass
                      #print('PostalCode :',re.findall(r'PostalCode=(.*?)Location=',whois.text)[0],
                      try:
                          print('Location   :',re.findall(r'Location=(.*?)REG',whois.text)[0])
                      except:pass
                      try:
                         print('ORG/ASN    :',re.findall(r'ORG/ASN (.*)',whois.text)[0])
                      except:pass
                      print()
                  except:pass;print()
             else:
                 pass

         sleep(1)
         for tab in bs.findAll('tr',class_="spy1xx"):
             for all in tab.findAll('td'):
                 if '.' in all.text:
                    if not 'GeoIP' in all.text:
                       self.px = all.text
                 else:
                     for typ in all.findAll('font',class_='spy2'):
                         if not '-' in typ.text:
                            self.typ = typ.text
                     for lv in all.findAll('font',class_='spy1'):
                         if 'never' == lv.text:
                             print('{ DIE  }  '+self.px+' type: '+self.typ);sleep(1)
                         else:
                              print('{ LIVE }  '+self.px+' type: '+self.typ);sleep(1)
         print()

         '''sleep(4)
         for whois in bs.findAll('tr' ,class_='spy1x'):
             if 'OK!' in whois.text:pass
             elif 'IP address:PortTypeAdd' in whois.text:pass
             elif 'IPs found (Max=' in whois.text:pass
             elif 'Location=' in whois.text:
                  pass
             else:
                 print()
                 print(whois.text)'''

bnr = r'''

   ▄████████  ▄██████▄   ▄████████    ▄█   ▄█▄  ▄████████    ▄████████    ▄█   ▄█▄ 
  ███    ███ ███    ███ ███    ███   ███ ▄███▀ ███    ███   ███    ███   ███ ▄███▀ 
  ███    █▀  ███    ███ ███    █▀    ███▐██▀   ███    █▀    ███    █▀    ███▐██▀   
  ███        ███    ███ ███         ▄█████▀    ███         ▄███▄▄▄      ▄█████▀    
▀███████████ ███    ███ ███        ▀▀█████▄    ███        ▀▀███▀▀▀     ▀▀█████▄    
         ███ ███    ███ ███    █▄    ███▐██▄   ███    █▄    ███    █▄    ███▐██▄   
   ▄█    ███ ███    ███ ███    ███   ███ ▀███▄ ███    ███   ███    ███   ███ ▀███▄ 
 ▄████████▀   ▀██████▀  ████████▀    ███   ▀█▀ ████████▀    ██████████   ███   ▀█▀ 
                                     ▀                                   ▀         

   Github  : https://github.com/bangtebe/sockcek
   Author  : bangtebe
   Tools   : ip scanner
   Version : 1.0

'''

def main():
    try:
       cmd('clear')
       if len(sys.argv) > 1:
          print(bnr)
          sokcek(sys.argv[1])
       else:
           print(bnr)
           ip = input('[?] ip : ')
           sokcek(ip)
    except Exception as err:print(err)
    except KeyboardInterrupt:exit('\nkeluar')


main()
