
import smtplib

server = smtplib.SMTP('smtp.gmail.com:587')

server.ehlo()
server.starttls()
server.login('joseph.p.seidel@gmail.com','Bfi@2013')

msg = "\r\n".join([
    "From: joseph.p.seidel@gmail.com",
    "To: seidel.jp@gmail.com",
    "Subject: Crontabtest",
    "",
    "It worked!",
    ])

server.sendmail('joseph.p.seidel@gmail.com', "seidel.jp@gmail.com", msg)
