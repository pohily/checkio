import sendgrid
from sendgrid.helpers.mail import Email,  Mail, Content

API_KEY = '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'
SUBJECT = 'Welcome'


sg = sendgrid.SendGridAPIClient(apikey=API_KEY)

def send_email(email, name):
    #sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
    from_email = Email("test@example.com")
    to_email = Email(email)
    subject = SUBJECT
    content = Content("text/plain", f'Hi {name}')
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
    return response.status_code

print(send_email('somebody@gmail.com', 'Some Body'))
    



"""

"""               



