import os
import json
import environ
import smtplib, ssl
from email.message import EmailMessage

env = environ.Env()
# reading .env file
environ.Env.read_env()

# Parent Directory path, where new directories for each month will be created
parent_dir = "C:\\Users\Fessy\Desktop\\"
# Get directory name as the salary month from user
directory = input('Enter the pay month in word: ').capitalize()
# Path to where new payslip files will be saved
path = os.path.join(parent_dir, directory)
  
# Create the directory 'Month' in \Desktop if if no such directory already exists
if not os.path.isdir(path):
    try: 
        os.mkdir(path) 
    except OSError as error: 
        print(error)

print(os.listdir(path))

EMAIL_ADDRESS = env.str('EMAIL_ADDRESS') #os.environ.get('EMAIL_USER') 
EMAIL_PASSWORD = env.str('EMAIL_PASSWORD') #os.environ.get('EMAIL_PASS')

staffs = json.loads(env.str("STAFFS"))


emails_sent = 0
files = os.listdir(path)

for file in files:
    print(file)
    print(file in staffs.keys())
    if  file in staffs.keys():
        msg = EmailMessage()
        msg['Subject'] = 'Payslip'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = staffs[file]
        msg.set_content(f'Goodday!\n\nAttached please find your payslip for {directory} as received from Salary.\n\nRegards,\nFessy')
        print(msg['To'])
        print(os.path.join(path, file))
        with open(os.path.join(path, file),'rb') as f:
            file_data = f.read()
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            try:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                print(f"Sending to: {msg['To']}")
                smtp.send_message(msg)
                print('Sending message...')
                emails_sent +=1
            except Exception as e:
                print(e)
print(f'Successfully sent {emails_sent} emails!')


# msg.add_alternative("""\
# <!DOCTYPE html>
# <html>
#     <body>
#         <h1 style="color:SlateGray;">This is an HTML Email!</h1>
#     </body>
# </html>
# """, subtype='html')


    # file name without extension: os.path.splitext(os.path.basename(file))[0] / with extension os.path.basename(file)