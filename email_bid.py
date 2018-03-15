
import os
from os.path import join, getsize, abspath, dirname
import re
import urllib
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders
import sys


oldamt = "21.98" #this is the current price
amt = oldamt
gmail_user = "youremail@gmail.com" #sends the email
gmail_pwd = "somepassword" #sends the email
to_addr = "anotheremail@gmail.com" #destination mail
#example url for auction item. can be any item auctioned on ebay
url = 'https://www.ebay.com/itm/LOT-OF-ACTION-FIGURE-CAPN-CAPTAIN-CRUNCH-Pirate-Jean-LaFoote-CEREAL-LOOSE/391994457903?hash=item5b44b0bf2f:g:1N8AAOSwNSxVXrqO'

def mail(to, subject, text):
   msg = MIMEMultipart()

   msg['From'] = gmail_user
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   part = MIMEBase('application', 'octet-stream')
   Encoders.encode_base64(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   mailServer.close()


def getURL(url):
    amt = ""
    #example target html dom element to get price
    #<span class="notranslate" id="prcIsum_bidPrice" itemprop="price" content="21.99">US $21.99</span>
    rcom = re.compile(r'(price"\s*content="[0-9\.]+">US\s*.[0-9]+.[0-9][0-9])')
    f = urllib.urlopen(url)
    foundMatch = 0
    for line in f:
        comelems = rcom.findall(line)
        if len(comelems) > 0:
            amt = comelems[0].split("$")[1]	
            foundMatch = 1
            if amt != oldamt:
                body=amt
                mail(to_addr,"oh no! price changed: ",body)
                print "oh no! price changed! new price is: ",amt
                sys.exit()
            else:                
                print "Ok price didn't change",time.strftime('%X %x %Z')
        
    if not foundMatch:
        print "Could not find bid. Regular expression may be outdated or url is invalid"
        sys.exit()
            

while oldamt == amt:

    getURL(url)
    time.sleep(30) #sleep for 5 mins
