from selenium import webdriver
import smtplib
import os

phantomjs_path = "/Users/joseph/bin/phantomjs"

browser = webdriver.PhantomJS(executable_path=phantomjs_path,service_log_path=os.path.devnull)
browser.get("https://www.python.org")

title = browser.title

server = smtplib.SMTP('smtp.gmail.com:587')

server.ehlo()
server.starttls()
server.login('joseph.p.seidel@gmail.com','Bfi@2013')

msg = "\r\n".join([
    "From: joseph.p.seidel@gmail.com",
    "To: seidel.jp@gmail.com",
    "Subject: Crontabtest",
    "",
    title,
    ])

server.sendmail('joseph.p.seidel@gmail.com', "seidel.jp@gmail.com", msg)
