# go over to your gmail account and setup 2 factor authentication
# generate app password
# create a function to send the mail

from email.message import EmailMessage
import ssl
import smtplib

email_sender = input("Email: ")
email_password = input("Password: ")


email_receiver = input('Receiver: ')

subject = input("Subject of Message: ")
body = input("Body of Message: ")

# create instance of email message

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

# create context, import lib ssl, smtplib
context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)  # login with your email
    smtp.sendmail(email_sender, email_receiver, em.as_string())  # send email
