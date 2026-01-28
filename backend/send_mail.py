import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()
def send_mail_reciever(subject, allnews, receivermail ):
    
    sender_email_id = os.getenv("SENDER_EMAIL_ID")
    sender_email_password = os.getenv("SENDER_EMAIL_PASSWORD")
    receiver_mail = receivermail

    msg = MIMEMultipart()
    msg["From"] = sender_email_id
    msg["To"] = receiver_mail
    msg["Subject"] = "Latest " + subject

    body = f"""
    Hello,

    How are you?

    Here are some important news
    {allnews}

    Regards,
    Your Script
    """
    msg.attach(MIMEText(body, "plain"))

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email_id, sender_email_password)

    server.sendmail(sender_email_id, receiver_mail, msg.as_string())
    server.quit()
    return {"message": "Welcome to the News Mail Agent Backend!"}
