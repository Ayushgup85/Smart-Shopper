import requests

from bs4 import BeautifulSoup  

import pywhatkit as kit
import smtplib


URL='https://www.amazon.in/Bourge-Vega-5-Running-Shoes-9-Vega-5-09/dp/B07RQ2BCN6?ref_=Oct_DLandingS_D_c5ef14b4_60&smid=AT95IG9ONZD7S'

headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64)', 'Cache-Control': 'no-cache', "Pragma": "no-cache"} 

def check_price():

    page =requests.get(URL,headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    title=soup.find(id="productTitle").get_text()

    price=soup.find(id="priceblock_ourprice").get_text()
    
    converted_price=float(price[2:5])
    print(converted_price)
    
    if(converted_price < 11250):
        send_mail()
    
    # print(title.strip())
    
    


def send_mail():
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls() # Secure the connection
    server.ehlo()

    server.login('ag7159441@gmail.com','zthdhqbtufevcldl')

    subject='price fell down!'

    body='https://www.amazon.in/Oppo-Mystery-Storage-Additional-Exchange/dp/B08444S68L/ref=sr_1_3?dchild=1&keywords=oppo+a31&qid=1616780266&sr=8-3'
    msg=f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'engineersop5@gmail.com',
        'ag7159441@gmail.com',
        msg
    )
    print('Hey Email has been sent')
    server.quit()


check_price()


