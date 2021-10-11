import os
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

staffs = {'hanghome':'Hesekie.Hanghome@mha.gov.na','uugwanga':'Hileni.Uugwanga@mha.gov.na', 
'iita':'Laili.Iita@mha.gov.na', 'alugongo':'Hesekie.Hanghome@mha.gov.na', 'shimuningeni':'Selma.Shimuningeni@mha.gov.na',
'kashikuka':'Elizabeth.Kashikuka@mha.gov.na', 'nuuyoma':'Hilkka.Nuuyoma@mha.gov.na', 'iyagaya':'Bertha.Iyagaya@mha.gov.na',
'shikulo':'Josephine.Shikulo@mha.gov.na', 'ashipala':'Teofilia.Ashipala@mha.gov.na', 'aiyambo':'Uilika.Aiyambo@mha.gov.na',
'shimooshili':'Letitia.Shimooshili@mha.gov.na', 'kaapanda':'Emilia.Kaapanda@mha.gov.na', 'amadhila':'Isak.Amadhila@mha.gov.na',
'cardos':'Anna.Cardos@mha.gov.na', 'ndundu':'Stefanus.Ndundu@mha.gov.na', 'kashuupulwa':'Ndeshihafela.Kashuupulwa@mha.gov.na',
'itembu':'Petrina.Itembu@mha.gov.na', 'iipinge':'Josephine.Iipinge@mha.gov.na', 'matheus':'Sara.Matheus@mha.gov.na'
}

current_staff = ''

msg = EmailMessage()
msg['Subject'] = 'Payslip'
msg['From'] = EMAIL_ADDRESS
msg['To'] = current_staff

msg.set_content('Goodday!\n\nAttached please find your payslip as received from Salary.\n\nRegards,\nFessy')

files = ['file1.pdf', 'file2.pdf', 'file2.pdf']

for file in files:
    # file name with extension
    file_name = os.path.splitext(os.path.basename(file))[0]
    if  file_name in staffs.keys:
        current_staff = staffs[file_name]
        with open(file, 'rb') as f:
            file_data = f.read()

        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename='file_name')
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)


# msg.add_alternative("""\
# <!DOCTYPE html>
# <html>
#     <body>
#         <h1 style="color:SlateGray;">This is an HTML Email!</h1>
#     </body>
# </html>
# """, subtype='html')