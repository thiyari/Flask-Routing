from flask import session
import imaplib
import email

mail = imaplib.IMAP4_SSL('imap.gmail.com')

## login to server
mail.login(uname,pwd)

mail.select('Inbox')

status, data = mail.search(None, 'ALL')
mail_ids = []
for block in data:
   mail_ids += block.split()
for  i in mail_ids:
   status, data = mail.fetch(i, 'RFC822')
   for response_part in data:
      if isinstance(response_part, tuple):
         message = email.message_from_bytes(response_part[1])
         mail_from = message['from']
         mail_subject = message['subject']
         if message.is_multipart():
            mail_content = ''
            for part in message.get_payload():
               if part.get_content_type() == 'text/plain':
                  mail_content += part.get_payload()
         else:
            mail_content = message.get_payload()
         print(f'From:{mail_from}')
         print(f'Subject:{mail_subject}')
         print(f'Content:{mail_content}')