import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Apple-MacBook-Pro-8th-Generation-Intel-Core-i5/dp/B0883KXHG3/ref=sr_1_1_sspa?dchild=1&keywords=macbook+pro&qid=1604778924&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFaTEFEMlk5NTI2WjMmZW5jcnlwdGVkSWQ9QTAyNDA2NjYzRjlDWUMwV0VROURMJmVuY3J5cHRlZEFkSWQ9QTA4MjIzNDExMUxOTjI4UzY4U0oxJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'}


def check_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    # print(soup.prettify())

    title = soup.find(id="productTitle").get_text()
    print(title.strip())
    price = soup.find(id="priceblock_ourprice").get_text()[2:]
    real_price = ""
    for i in range(len(price)):
        if price[i] != ',':
            real_price += price[i]
    real_price = int(float(real_price))
    print(real_price)

    if(real_price > 100000):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('algomessiaha@gmail.com', '<YOUR PASSWORD>')

    subject = 'Price fell down! Hurry up!'
    body = 'Check the amazon link https://www.amazon.in/Apple-MacBook-Pro-8th-Generation-Intel-Core-i5/dp/B0883KXHG3/ref=sr_1_1_sspa?dchild=1&keywords=macbook+pro&qid=1604778924&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFaTEFEMlk5NTI2WjMmZW5jcnlwdGVkSWQ9QTAyNDA2NjYzRjlDWUMwV0VROURMJmVuY3J5cHRlZEFkSWQ9QTA4MjIzNDExMUxOTjI4UzY4U0oxJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'algomessiaha@gmail.com',  # from mail
        'f786jamil@gmail.com',  # to mail
        msg
    )
    print('HEY EMAIL HAS BEEN SENT!')

    server.quit()


while (True):
    # check_price()
    time.sleep(60*60)  # after every hour
