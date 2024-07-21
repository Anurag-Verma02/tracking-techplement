import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time
from winotify import Notification, audio


clicks = 0

def onClick():
  global clicks
  clicks += 1



toast = Notification(app_id="Email Tracking", title="Email Tracking", 
    msg="Email sent successfully\nReport sent successfully", duration="short")

# Email account credentials
EMAIL = 'hriday.has.spam@gmail.com'
PASSWORD = 'ekow hslz wtvl ayic'

# SMTP server configuration
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

# Email details
sender_email = EMAIL
receiver_email = '0208anuverma@gmail.com'
subject = 'This is a test email with tracking'
body = '''
    Hello,

    This is a test email with tracking and reporting.

    Please click the following link to verify it works:
    <a href="https://your-tracking-server.com/click?id=12345"  onClick="onClick()">Click here</a>

    <img src="https://your-tracking-server.com/open?id=12345" width="1" height="1" border="0" alt="">
'''

def send_email(sender, receiver, subject, body):
    try:
        # Create a MIMEMultipart object
        msg = MIMEMultipart('alternative')
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = subject

        # Attach the email body to the message
        msg.attach(MIMEText(body, 'html'))

        # Create an SMTP session
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

        # Start TLS for security
        server.starttls()

        # Log in to the email account
        server.login(sender, PASSWORD)

        # Send the email
        text = msg.as_string()
        server.sendmail(sender, receiver, text)

        # Close the SMTP session
        server.quit()

        print("Email sent successfully")
        
        toast.show()
        
    except Exception as e:
        print(f"Failed to send email: {e}")

# Send the email
send_email(sender_email, receiver_email, subject, body)

# import smtplib
# from email.mime.text import MIMEText
# import os

def send_report(sender, receiver, subject, body):
    try:
        # Create a MIMEText object
        msg = MIMEText(body)
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = subject

        # Create an SMTP session
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)

        # Start TLS for security
        server.starttls()

        # Log in to the email account
        server.login(sender, PASSWORD)

        # Send the email
        text = msg.as_string()
        server.sendmail(sender, receiver, text)

        # Close the SMTP session
        server.quit()

        print("Report sent successfully")
    except Exception as e:
        print(f"Failed to send report: {e}")


def generate_report():
    if os.path.exists('open_log.txt'):
        with open('open_log.txt', 'r') as f:
            open_log = f.read()
    else:
        open_log = "No opens yet."
    if os.path.exists('click_log.txt'):
        with open('click_log.txt', 'r') as f:
            click_log = f.read()
    else:
        click_log = "No clicks yet."
    body = f"""
    Tracking Report:
    Opens:{clicks}
    {open_log}
    Clicks:{clicks}
    {click_log}
    """
    send_report(sender_email, receiver_email, "Tracking Report", body)
# Generate and send the report
generate_report()

