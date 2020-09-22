import smtplib
import os
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


#variable name server, which will store the specific server we are going to use 
#Note: this is current setup is for gmail, you can find info about your email provider 
#      online. Browse for SMTP of the the email provider you use
server = smtplib.SMTP('smtp.gmail.com', 587)


server.ehlo()

with open("PATH/password.txt", "r") as f:
    password = f.read()

server.connect("smtp.gmail.com",587)
server.ehlo()
server.starttls()
server.login('Senders.email@gmail.com', password)

msg =MIMEMultipart()
msg['From'] = 'NAME'
msg['To'] = 'Recipient.Email@gmail.com'
msg['Subject'] = 'Email Subject'

with open('PATH/message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'PATH/what-is-coding-1024x683.jpg'
attachment = open(filename, 'rb')

p = MIMEBase('application', 'octet-stream')
p.set_payload(attachment.read())

encoders.encode_base64(p)

p.add_header('Content-Disposition', f'attachment; filename={filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('SENDER.EMAIL@gmail.com', 'RECIPIENT.EMAIL@gmail.com', text)

server.quit()