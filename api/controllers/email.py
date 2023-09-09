from emaileasily import email_to, email_subject, email_content, email_send

def sendEmailOTP(receiver):
    email_to(receiver)
    email_subject('UEIS Email functionality test')
    email_content('This is an example of sending emails with emaileasily')
    email_send('ueissystem@gmail.com','czlzzgoatysyoksf')
