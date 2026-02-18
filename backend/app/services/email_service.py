import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailService:
    def __init__(self, smtp_server, smtp_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.username = username
        self.password = password

    def send_email(self, recipient, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = recipient
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
            server.starttls()
            server.login(self.username, self.password)
            server.sendmail(self.username, recipient, msg.as_string())

    def send_password_reset_email(self, recipient, reset_link):
        subject = 'Password Reset Request'
        body = f'Click the link to reset your password: {reset_link}'
        self.send_email(recipient, subject, body)

    def send_notification_email(self, recipient, message):
        subject = 'Notification'
        body = f'You have a new notification: {message}'
        self.send_email(recipient, subject, body)
