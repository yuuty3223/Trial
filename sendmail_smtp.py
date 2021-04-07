import os
import smtplib
from email.mime.text import MIMEText

#SMTP認証情報
host = 'smtp.sendgrid.net'
port = 587
user = 'apikey'
passwd = os.environ.get('SENDGRID_API_KEY')
server = smtplib.SMTP(host, port)
server.starttls()
server.login(user, passwd)

#送受信アドレス
from_email = 'sender@example.jp'
to_email = ['sender@exampke.jp']
#メール本文
body = 'This is a test email using SMTP.'
message = MIMEText(body)
message['From'] = from_email
message['To'] = ",".join(to_email)
message['Subject'] = 'SMTP Test Mail'
#メール送信
server.sendmail(from_email, to_email, message.as_string())
server.quit()

