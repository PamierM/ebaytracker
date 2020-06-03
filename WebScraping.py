#You need 2-Step Verification enabled for Gmail or Authorization for Less Secure Apps for this program to function

from bs4 import BeautifulSoup
import requests
import smtplib
import time

url = input("Enter a space then your desired eBay listing link: ")
desired_price_string = input("Enter your desired price:")
desired_price = float(desired_price_string)
#Insert your header here (look up your header to find it), optional if not wanted deleted line of code
headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'}
email = input("Enter your Gmail: ")
password = input("Enter your Gmail password: ")

def check_price():
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    title = soup.find(id="itemTitle").get_text()
    price = soup.find(id="prcIsum").get_text().replace('/ea', '')
    converted_price = float(price[4:20])

    if(converted_price <= desired_price):
        send_mail()

def send_mail():
    subject = "Price Drop"
    mailtext = "Subjects:"+subject+'\n\n'+'Your item is at your desired price: ' + url

    server = smtplib.SMTP(host = 'smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()
    #Type your password in the password string
    server.login(email,password)
    server.sendmail(email, email, mailtext)
    pass

#Checks the price every 86400 seconds (24 hours)
while(True):
    check_price()
    time.sleep(86400)
