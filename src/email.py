import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from datetime import date
from dotenv import load_dotenv
import os

load_dotenv()
my_email = os.getenv("EMAIL")
my_acc = os.getenv("ACC")

def send_diagnosis_mail(patient_name, patient_email):
    '''
    Given the patient name and email, sends an email with a pdf attachment that hold a diagnosis report
    
    Takes: patient name and patient email
    Returns: none    
    '''
    # TODO change receiver email to patient email after testing
    # TODO change file name of pdf attachment
    
    # set sender and receiver emails
    sender_email = my_email
    receiver_email = patient_email
    
    # create multipart object for storing all the MIMEText and MIMEImage objects
    msg = MIMEMultipart()
    msg['Subject'] = 'Health Care Inc. diagnosis'
    msg['From'] = sender_email
    msg['To'] = receiver_email
    
    # create text object
    body = f'Hello {patient_name}, attached you can find the results for your Pneumonia test.<br />Best,'
    signature = '<br /><br />Dr. Durden<br />Health Care Inc.<br />1999 Paper Street<br />Mayhem, USA'
    msgText = MIMEText('%s</>' % (body + signature), 'html')
    msg.attach(msgText)
    
    # create pdf object
    file_name = f'{patient_name} - {date.today()}'
    pdf = MIMEApplication(open(f'diagnosis_PDFs/{file_name}', 'rb').read(), _subtype="pdf")
    pdf.add_header('Content-Disposition', 'attachment', file_name = file_name)
    msg.attach(pdf)
    
    # send email
    try:
        with smtplib.SMTP('smtp.office365.com', 587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login(my_email, my_acc)
            smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(e)