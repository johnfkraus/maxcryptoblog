# import django
from django.conf import settings
import os
from django.core.mail import send_mail
from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%A, %d, %B %Y %I:%M %p")
print(formatted_date)

# os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
os.environ['DJANGO_SETTINGS_MODULE'] = 'allauthdemo.settings'

subject = 'Subject: Cryptoblog email sent ' + formatted_date

message_text = 'Greetings from Cryptoblog.  This message was sent: ' + formatted_date

num_emails_sent = send_mail(subject, message_text, settings.DEFAULT_FROM_EMAIL, ['johnkraus3@gmail.com'], fail_silently=False)

print('num_emails_sent =', num_emails_sent)
