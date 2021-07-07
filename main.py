from Google import Create_Service
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
  
now = datetime.now()
#changed to absolute path(change to your path to use)
CLIENT_SECRET_FILE = '/Users/ryanchoi/Desktop/SADA U/Project/gmail output/Gmail_output/client_secret.json'
API_NAME = 'gmail'
API_VERSION = 'v1'
SCOPES = ['https://mail.google.com/']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

emailMsg = '<h1 style="text-align:center">SADA U Cohort 3 Project</h1>\n\
    <p style="font-size:18px"> Hello everyone,</p>\n\
        <p style="font-size:18px; text-align:justify; line-height:27px"> We are here to inform you that we have created a wonderful project to check out. We have provided a link below to check our work and attached some of the power point and informaiton.</p>\n\
            <p style="font-size:18px; text-align:justify;line-height:127px"> webpage link: www.googel.com</p>\n\
                <p style="font-size:18px; text-align:justify"> Sincerely yours,</p>\n\
                    <p style="font-size:18px; "> SADA U Cohort 3</p>'

mimeMessage = MIMEMultipart()
mimeMessage['to'] = 'examplegmail.com'
mimeMessage['from'] = 'example@sada.com' 
mimeMessage['subject'] = 'Check our wonderful SADA U project!'
#change plain to html to send emsil html format
mimeMessage.attach(MIMEText(emailMsg, 'html'))
raw_string = base64.urlsafe_b64encode(mimeMessage.as_bytes()).decode()

message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
print(message)