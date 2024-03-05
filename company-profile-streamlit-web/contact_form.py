import smtplib,ssl

username = 'smtp-address'
password = 'smtp-password'

receiver_email = 'site-owner-email'

host = "smtp.google.com"
port = 465
context = ssl.create_default_context()

def send_mail(email,topic,text):
    message = f"""\
Subject: New email from {email}

From: {email}
{topic}
{text}"""
    with smtplib.SMTP_SSL(host,port,context=context) as server:
        server.login(username,password)
        server.send(email,message)
