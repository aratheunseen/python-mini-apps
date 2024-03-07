import smtplib,ssl

def send_mail(message):

    host = "smtp.gmail.com"
    port = 465

    username = "your-smtp-mail"
    password = "your-smtp-passpord"

    receiver_mail = "newsletter-receivers-mail"
    context = ssl.create_default_context()

    server = smtplib.SMTP_SSL(host=host, port=port, context=context)
    server.login(username,password)
    server.sendmail(username,receiver_mail,message)
        