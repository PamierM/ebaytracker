#You need 2-Step Verification enabled for Gmail or Authorization for Less Secure Apps for this program to function

from bs4 import BeautifulSoup
import requests
import smtplib
import time

#Insert the URL of the desired eBay product here
url = "https://www.ebay.com/itm/Canon-PIXMA-MG3620-Home-Office-Wireless-All-In-One-Inkjet-Printer-INK-INCLUDED/313100926099?epid=232027656&hash=item48e644fc93:g:Gt0AAOSwASZevsMc"
#Insert your header here (look up your header to find it), optional if not wanted deleted line of code
headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'}
#insert your gmail here that you want the server to send/receive from
email = 'mail@gmail.com'

def check_price():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="itemTitle").get_text()
    price = soup.find(id="prcIsum").get_text()
    converted_price = float(price[4:10])

    if(converted_price > 50):
        send_mail()

def send_mail():
    subject = "Price Drop"
    mailtext = "Subjects:"+subject+'\n\n'+'Your item is at your deisred price: ' + url

    server = smtplib.SMTP(host = 'smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    #Type your password in the password string
    server.login(email,'password')
    server.sendmail(email, email, mailtext)
    pass

#Checks the price every 86400 seconds (24 hours)
while(True):
    check_price()
    time.sleep(86400)
