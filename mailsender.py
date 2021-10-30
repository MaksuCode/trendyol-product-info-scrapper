import smtplib, ssl


def send(mail_address, password, message):
    smtp_server = 'smtp.gmail.com'
    port = 587
    sender_email = 'testautomationwithmaksu@gmail.com'

    context = ssl.create_default_context()
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(sender_email, password)
        server.sendmail(sender_email, mail_address, message)
    except Exception as e:
        print('Can not logged in to the mail : ', e)
    finally:
        server.quit()
