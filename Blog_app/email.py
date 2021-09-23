from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


def send_email(name, receiver):
    subject = 'Post recommendation'
    sender = 'nuer911@gmail.com'

    text_content = render_to_string('blog/post/share.html', {"name": name})
    html_content = render_to_string('blog/post/share.html', {'name': name})

    msg = EmailMultiAlternatives(subject, text_content, sender, [receiver])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
