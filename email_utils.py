import smtplib
from email.mime.text import MIMEText

def send_email(to_email, otp):
    sender_email = "vajabhavin96@gmail.com"
    app_password = "xvos vtfv xsew xggs"

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
    sender_email = "vajabhavin96@gmail.com"
    app_password = "xvos vtfv xsew xggs"

    subject = "Your Password"
    body = f"Your Password is: {passtemp}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = to_email

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.send_message(msg)
    server.quit()