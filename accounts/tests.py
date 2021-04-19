from django.test import TestCase

from django.core.mail import send_mail

subject = 'Django'
from_email = 'no-reply@engmedapp.com'
message = 'This is my message'
recepient_list = ['sirdarknight1366@gmail.com']
html_message = '<h1>This is my HTML test</h1>'

send_mail(subject, message, from_email, recepient_list,
          fail_silently=False, html_message=html_message)
