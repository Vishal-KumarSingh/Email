from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
msg = MIMEMultipart()
print("Before Proceed Make sure you have turned on the email for less secure apps.. Turn it on here https://myaccount.google.com/lesssecureapps")

msg['From'] = input("Enter your gmail Id ")
password = input("Enter your gmail password ")
msg['To'] = input("Enter receiver's email address ")
msg['Subject'] = input("Enter Subject of your Email ")
message = input("Enter your message ")

#Attaching email with message
msg.attach(MIMEText(message, 'plain'))
 
#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()
 
print("successfully sent email to %s:" % (msg['To']))

input()