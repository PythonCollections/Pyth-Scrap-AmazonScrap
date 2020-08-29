import requests
from bs4 import BeautifulSoup
import smtplib


def checkprice():
    url = 'https://www.amazon.com/Alienware-Gaming-Notebook-Intel-i7-9750H/dp/B086DD63LZ/ref=sr_1_1?dchild=1&keywords=Dell+Alienware+m17&qid=1598639430&sr=8-1'
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    # print(soup.prettify())
    title = soup.find(id="productTitle").getText()
    print(title.strip())
    price = soup.find(id='priceblock_ourprice').getText()
    print(price)


def SendEmail():
    password = 'anhgdnkjowfxtjsc' #get the password fromt eh google app password
    server = smtplib.SMTP('SMTP.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('yppg.learning@gmail.com',password=password)

    subject = "Check the Price"
    body = 'Check the email'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'yppg.learning@gmail.com',
        'yppg.shopping@gmail.com',
        msg
    )

    print("Email has been sent")
    server.quit()

SendEmail()