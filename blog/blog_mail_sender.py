# blog/send_email.py

#  import os ## required to generate salt
import sys
# import inspect

#  =====================
from django.conf import settings
import os
from django.core.mail import send_mail
from datetime import datetime
from allauthdemo import utils as allauthdemo_utils
# sys.exit(1)


os.environ['DJANGO_SETTINGS_MODULE'] = 'allauthdemo.settings'

# subject = 'Subject: Cryptoblog email sent ' + formatted_date
# message_text = 'Greetings from Cryptoblog.  This message was sent: ' + formatted_date
# destin_addresses_list = []
# destin_addresses_list.append('johnkraus3@gmail.com')
# print('destin_addresses_list = ', destin_addresses_list)

# num_emails_sent = send_mail(subject, message_text, settings.DEFAULT_FROM_EMAIL, ['johnkraus3@gmail.com'], fail_silently=False)
# print('num_emails_sent =', num_emails_sent)


# password = b'password'
# print('password = ', password, 'password.__class__ = ', password.__class__)
db = True  # debugging? > verbose output


def formatted_date():
    return datetime.now().strftime("%A, %d, %B %Y %I:%M %p")


def send(email_message):
    # sys.exit(1)
    subject = email_message.post.title
    content_string = ''
    content_string += 'Sender: ' + email_message.sender.name + '\n'
    content_string += 'Message content: ' + email_message.post.get_content() + '\n'
    content_string += 'To: ' + email_message.destin_email + '\n'
    destin_addresses_list = []
    destin_addresses_list.append(email_message.destin_email)
    print('destin_addresses_list = ', destin_addresses_list)

    num_emails_sent = send_mail(subject, content_string, settings.DEFAULT_FROM_EMAIL, destin_addresses_list, fail_silently=False)

    print('num_emails_sent =', num_emails_sent)

    if db:
        print(allauthdemo_utils.lineno(), 'content_string = ', content_string)

    return num_emails_sent


def send_to(email_address):

    if db:
        print(allauthdemo_utils.lineno())

    return True


def test1():
    email_address = 'johnkraus3@gmail.com'
    return test2(email_address)


def test2(email_address):

    subject = 'Subject: Max Cryptoblog: Title  = ?? ' + formatted_date
    message_text = 'Greetings from Cryptoblog.  This message was sent: ' + formatted_date
    destin_addresses_list = []
    destin_addresses_list.append(email_address)
    print(allauthdemo_utils.lineno(), 'destin_addresses_list = ', destin_addresses_list)

    num_emails_sent = send_mail(subject, message_text, settings.DEFAULT_FROM_EMAIL, ['johnkraus3@gmail.com'], fail_silently=False)

    print(allauthdemo_utils.lineno(), 'num_emails_sent =', num_emails_sent)
    return num_emails_sent


def main():
    """ Define a main() function that parses parameters and runs a test."""
    args = sys.argv[1:]
    if db:
        print(allauthdemo_utils.lineno(), 'args =', args)
    args = sys.argv[1:]
    if not args or len(args) > 1:
        #  or (len(args) == 1 and args[0] != '--test'):
        print('usage: [--test | destin_email]')
        sys.exit(1)
    if args[0] == '--test':
        print('testing!')
        test1()
    else:
        email_address = sys.argv[0]
        test2(email_address)

    print(allauthdemo_utils.lineno())


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()
