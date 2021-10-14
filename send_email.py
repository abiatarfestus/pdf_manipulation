import os
import json
import environ
import smtplib
from make_dir import path, directory
from email.message import EmailMessage

env = environ.Env()
environ.Env.read_env()
EMAIL_ADDRESS = env.str('EMAIL_ADDRESS') #os.environ.get('EMAIL_USER') 
EMAIL_PASSWORD = env.str('EMAIL_PASSWORD') #os.environ.get('EMAIL_PASS')
staffs = json.loads(env.str("TEST_STAFFS"))


def email_payslip():
    emails_sent = 0
    files = os.listdir(path)
    for file in files:
        print(f'Current file: {file}')
        if  file in staffs.keys():
            msg = EmailMessage()
            msg['Subject'] = 'Payslip'
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = staffs[file]
            msg.set_content(f'Good day!\n\nAttached please find your payslip for {directory} as received from Salary.\n\nRegards,\nFessy')
            print(f'Recipient: {msg["To"]}')
            with open(os.path.join(path, file),'rb') as f:
                file_data = f.read()
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                try:
                    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                    smtp.send_message(msg)
                    print('Sending email...')
                    emails_sent +=1
                except Exception as e:
                    print(e)
    print(f'Successfully sent {emails_sent} emails!')
    return