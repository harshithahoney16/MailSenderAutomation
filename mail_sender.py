import smtplib, ssl
from email.message import EmailMessage
import csv

# Gmail credentials
sender_email = "23b01a0579@svecw.edu.in"
password = "zfmdxvkhjvnktbbd"  # Your Gmail App Password
subject = "Automated Email from Python"

# Load the message template
with open("message.txt", "r") as f:
    message_template = f.read()

# Read recipients with name and email
with open("recipients.csv", newline='') as file:
    reader = csv.DictReader(file)  # <-- Use DictReader to read columns by name
    for row in reader:
        name = row['Name'].strip()
        receiver_email = row['Email'].strip()

        # Personalize the message
        message_body = message_template.format(name=name)

        # Compose email
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg.set_content(message_body)

        # Send the email
        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
                server.login(sender_email, password)
                server.send_message(msg)
                print(f"✅ Email sent to {name} ({receiver_email})")
        except Exception as e:
            print(f"❌ Failed to send to {receiver_email}: {e}")
