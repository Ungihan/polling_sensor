import requests
import smtplib

# headers = {
#     # Already added when you pass json= but not when you pass data=
#     # 'Content-Type': 'application/json',
# }

# json_data = {
#     'data': 'string',
#     'status': 'pending',
#     'rule': 'rule2',
# }

# response = requests.post('http://653e-43-252-251-77.ngrok.io/order', headers=headers, json=json_data)

gmail_user = 'vaibhavpicdump@gmail.com'
gmail_password = '4Saurav@90'

sent_from = gmail_user
to = 'vaibhav.chaudhary@ivedha.com'
subject = "tesr"
body = 'sent from stackstorm'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, to, subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print("email sent")
except:
    print('Something went wrong...')