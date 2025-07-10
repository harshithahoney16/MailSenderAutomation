# MailSenderAutomation

This is a simple Python project that sends emails to multiple people using a message template and a list of recipients.

## Files

- mail_sender.py – main script
- message.txt – email message with {name} placeholder
- recipients.csv – list of Name,Email

## Example recipients.csv

Name,Email  
Alice,alice@example.com  
Bob,bob@example.com  

## Example message.txt

Hello {name},  
This is a test email sent from my Python script.  

Best regards,  
Harshitha

## How to Run

1. Put all 3 files in the same folder
2. Open terminal in that folder
3. Run:

```
python mail_sender.py
```

Note: Use your Gmail App Password in the script, not your regular password.
