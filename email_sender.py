import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(recipient_email, subject, body, calendar_link):
    sender_email = os.getenv('SENDER_EMAIL')
    sender_password = os.getenv('SENDER_PASSWORD')

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject

    email_body = f"""
    Dear Valued Customer,

    Thank you for choosing Bayou Movers for your upcoming move. Here's a summary of your conversation with our AI assistant:

    {body}

    Your move has been scheduled and added to our calendar. You can view the details and add it to your own calendar using this link:
    {calendar_link}

    If you need to make any changes or have any questions, please don't hesitate to contact us.

    Best regards,
    Bayou Movers Team
    """

    message.attach(MIMEText(email_body, 'plain'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, sender_password)
            server.send_message(message)
        print(f"Email sent successfully to {recipient_email}")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False

