from imap_tools import MailBox, AND 
import time
import os


os.chdir(os.path.join(os.path.dirname(__file__), 'CSV'))
kmail = MailBox(host='mail.XXXXXXXXX.com.ar')
kmail.login(username='user@mail.com.ar',
            password='PASSWORD',
            initial_folder='INBOX')


for msg in kmail.fetch():
    for i, att in enumerate(msg.attachments):
        if att.filename[-20:] == 'device_ocupation.csv':
            print(msg.subject, ' - ', att.filename)
            open(att.filename, 'wb').write(att.payload)
        try:
            kmail.move(msg.uid, 'INBOX.Procesados')
        except:
            print(f"Error al mover {msg.subject}")
#Necesita que se cree una subfolder que se llame "./CSV"
