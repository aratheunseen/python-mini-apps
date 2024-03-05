import smtplib, ssl

username = 'smtp-address'
password = 'smtp-password'

receiver_email = 'site-owner-email'

host = 'smtp.gmail.com'
port = 465
context = ssl.create_default_context()

def send_email(name, email, message):
    message = f"""\
Subject: You have a mail from {name}

{message}

This message is sent from {email}."""
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, message)