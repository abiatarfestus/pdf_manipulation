import send_email
import split_pdf

#====================================MAKE DIRECTORY=======================================#
send_email.create_dir()
#==================================SPLIT AND EXTRACT PDF==================================#
src = fitz.open(r'C:\Users\Fessy\Desktop\January\payslips.pdf')
split_pdf.extract_payslips()
#======================================SEND EMAIL=========================================#
send_email.email_payslip()
#======================================EXIT APP===========================================#
quit()