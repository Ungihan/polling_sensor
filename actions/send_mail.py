import smtplib
from st2common.runners.base_action import Action


class SendEmail(Action):
    def __init__(self, config) -> None:
        super(SendEmail, self).__init__(config=config)

    def run(self, data, sub):
        gmail_user = 'vaibhavpicdump@gmail.com'
        gmail_password = '4Saurav@90'

        sent_from = gmail_user
        to = 'vaibhav.chaudhary@ivedha.com'
        subject = "test subject" + str(data)
        body = sub

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