import smtplib, ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "benjaminmc1004@gmail.com"
    password = "imhldvhijgnzguoi"

    receiver = "jaden.stauch@cartrack.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
        

