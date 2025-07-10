# 📧 MailSenderAutomation

**MailSenderAutomation** is a lightweight Python script that automates sending personalized emails to multiple recipients using a CSV contact list and a pre-written message template.

---

## ✨ Features

- ✅ Send bulk emails in one click
- 📂 Read recipient names and emails from a CSV file
- 💬 Customize email content with dynamic names
- 🔒 Uses Gmail App Password for secure login
- 🧾 Simple and minimal setup

---

## 💻 Tech Stack

- **Python 3**
- **smtplib**
- **ssl**
- **email.message**
- **csv**

- ## 📁 Folder Structure

- MailSenderAutomation/
│
├── mail_sender.py # Main script
├── message.txt # Email content (template message)
└── recipients.csv # List of recipients (Name,Email)


---

## 🧪 Example `recipients.csv`

```csv
Name,Email
Alice,alice@example.com
Bob,bob@example.com

- ## 🧾 Example message.txt
pgsql
Copy
Edit
Hello {name},

This is a test email sent from my automated Python script.

Best regards,  
Harshitha
🔐 Gmail Setup
Enable 2-Step Verification on your Gmail account.

Create an App Password from your Google Account → Security → App Passwords.

Paste the App Password into mail_sender.py where prompted.

🔗 Google App Password Help

🚀 Run the Project
Make sure all files are in the same folder.

bash
Copy
Edit
cd MailSenderAutomation
python mail_sender.py
📌 Notes
This script uses Gmail’s SMTP_SSL (port 465) for secure email sending.

Only works with Gmail accounts that have app passwords enabled.

- Messages are sent sequentially, not in parallel.

📜 License
This project is open-source and free to use under the MIT License.

yaml
Copy
Edit

---

Let me know if you’d like me to generate a matching `LICENSE` file too (MIT or other).

---

## 🗂️ Folder Structure

