import requests
from bs4 import BeautifulSoup
import smtplib
import os
import time

# Asus Dual NVIDIA GeForce GTX 1650 4GB, GDDR5 - DUAL-GTX1650-4G
URL_grapicCard = 'https://bit.ly/3qFgDUb'
# Forno de embutir elétrico Consul 84 litros prata com Grill e Timer Autodesligamento - COB84AR
URL_consulOven = 'https://bit.ly/34fnuvW'
  
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

def cp_grapic_card():
  page = requests.get(URL_grapicCard, headers=headers)
  soup = BeautifulSoup(page.content, 'html.parser')
  body_message = "Damn, can you even run Pecman on this machine bro?! Too weak! Please, check this out: "

  price = soup.find("h4", itemprop="price").get_text()
  print(price)
  converted_price = float(price[3:8])

  print(converted_price) # pass this information to a db

  if(converted_price < 1.800):
    send_mail(URL_grapicCard, body_message)

def cp_consul_oven():
  page = requests.get(URL_consulOven, headers=headers)
  soup = BeautifulSoup(page.content, 'html.parser')
  body_message = "Is your kitchen ready to look badass?! Well, so check this link: "
  
  price = soup.find("span", "vtex-product-price-1-x-spotPrice").get_text()
  print(price)
  converted_price = float(price[3:8])

  print(converted_price) # pass this information to a db

  if(converted_price < 1.400):
    send_mail(URL_consulOven, body_message)

def send_mail(url, body_msg):
  server = smtplib.SMTP('smtp-mail.outlook.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login(os.environ.get('EMAIL'), os.environ.get('PW'))
  subject = 'The Manager Finally Went Nuts!'
  body = f'{body_msg} {url}'
  to_addr = os.environ.get("EMAIL")
  from_addr = "Rafaelo <" + os.environ.get("EMAIL") + ">"

  msg = "From: %s\nTo: %s\nSubject: %s\n\n %s" %(from_addr, to_addr, subject, body)

  server.sendmail(from_addr, to_addr, msg )

  print("HEY EMAIL HAS BEEN SENT!")

  server.quit()

while(True):
  cp_consul_oven()
  cp_grapic_card()
  time.sleep(21600)