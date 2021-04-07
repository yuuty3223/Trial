import sendgrid
import os
from sendgrid.helpers.mail import

sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("sender@example.jp")
to_email = To("to@example.jp")
subject = "Web API Test mail"
content = Content("text/plain", "This is a test email using Web API.")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)

