import smtplib
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
# import ssl

# import socket

# print(socket.getaddrinfo("smtp.gmail.com", 587))

load_dotenv()

sender_email = os.getenv("EMAIL")
app_password = os.getenv("APP_PASSWORD")

def send_mail(msg):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.send_message(msg)
    server.quit() 

def send_otp(to_email, otp):

    subject = "Your OTP Code"
    body = f"Your OTP is: {otp}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.send_message(msg)
    server.quit()

def send_pass(to_email, passtemp):

    subject = "Your Password"
    body = f"Your Password is: {passtemp}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    # server = smtplib.SMTP("smtp.gmail.com", 587)
    # server.starttls()
    # server.login(sender_email, app_password)
    # server.send_message(msg)
    # server.quit()

    send_mail(msg)

def send_login_info(to_email):

    subject = "Login Info"
    body = f"Someone Login Into Your Account"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email


    send_mail(msg)

def clg_register_info(to_email):

    subject = "Your Collage Has Been Added"
    body = f"Your Collage Has Been Register, Now You Can Login"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    send_mail(msg)