import smtplib, ssl 
from email.mime.base import MIMEBase 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email import encoders 
smtp_server = 'smtp.gmail.com' 
port = 465 
destinateur = 'tutoriel.test0@gmail.com'
password = 'Testing445566'
destinataire = 'tutoriel.test0@gmail.com'
nom_fichier = 'fichier.png'
message = MIMEMultipart('alternative') 
message['Subject'] = 'envoie d\'un fichier'
message['From'] = destinateur 
message['To'] = destinataire
message.attach(MIMEText('envoyer une pièce jointe', 'plain'))
with open(file_name, 'rb') as attachment:  
    file_part = MIMEBase('application', 'octet-stream')  
    file_part.set_payload(attachment.read())  
    encoders.encode_base64(file_part) 
    file_part.add_header( 'Content-Disposition', 'attachment; filename='+ str(nom_fichier) )
    message.attach(file_part)
context = ssl.create_default_context() 
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:  
    server.login(destinateur, password)  
    server.sendmail(destinateur, destinataire, message.as_string())