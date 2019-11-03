import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(receiver_email, text_message, collection):
    try:
        sender_email = "blbotcrew@gmail.com"
        password = "BlueLogic@123"

        message = MIMEMultipart("alternative")
        message["Subject"] = "No-reply Generated CSV Unhandled intent Fallback"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Create the plain-text and HTML version of your message
        text = text_message

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        # part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part1)
        # message.attach(part2)
        # Create secure connection with server and send email
        filename = collection+"_default_fallback.csv"
        attachment = open(collection+"_default_fallback.csv", "rb")
        part2 = MIMEBase('application', 'octet-stream')
        part2.set_payload(attachment.read())
        encoders.encode_base64(part2)
        part2.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        message.attach(part2)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
    except ValueError as e:
        print(e)

