import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('vaishnaviroyya123@gmail.com','cnhvmrqhobcunakq')
    msg=EmailMessage()
    msg['From']='vaishnaviroyya123@gmail.com'
    msg['Subject']='account sign up'
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()
