from django.core.mail import EmailMultiAlternatives, get_connection
from django.template import loader

from server.settings import EMAIL_HOST_USER


class BaseEmailService(object):
    @classmethod
    def _send(  # noqa: WPS210, WPS211
        cls,
        subject_template_name,
        email_template_name,
        context,
        from_email,
        to_email,
        html_email_template_name=None,
        attachments=None,
        connection=None,
    ):
        if connection is None:
            connection = get_connection(fail_silently=False)

        subject, body = cls._get_subject_and_body(context, subject_template_name, email_template_name)
        receivers = to_email if isinstance(to_email, list) else [to_email]
        email_message = EmailMultiAlternatives(
            subject,
            body,
            from_email,
            bcc=receivers,
            connection=connection,
        )
        if html_email_template_name is not None:
            html_email = loader.render_to_string(html_email_template_name, context)
            email_message.attach_alternative(html_email, 'text/html')
        if attachments:
            for attachment in attachments:
                email_message.attach_file(attachment.path)

        return email_message.send()

    @classmethod
    def _get_subject_and_body(cls, context, subject_template_name, email_template_name):
        subject = loader.render_to_string(subject_template_name, context)
        subject = ''.join(subject.splitlines())
        body = loader.render_to_string(email_template_name, context)
        return subject, body


class EmailService(BaseEmailService):
    @classmethod
    def send_reset_password(cls, context):
        email_options = {
            'subject_template_name': 'registration/password_reset_subject.txt',
            'email_template_name': 'registration/password_reset_email.html',
            'from_email': EMAIL_HOST_USER,
            'to_email': context.get('email'),
            'html_email_template_name': None,
            'context': context,
        }
        return cls._send(**email_options)

    @classmethod
    def send_contact_form_message(cls, context):
        email_options = {
            'subject_template_name': 'emails/contact_form/contact_form_subject.txt',
            'email_template_name': 'emails/contact_form/contact_form_email.html',
            'from_email': EMAIL_HOST_USER,
            'to_email': EMAIL_HOST_USER,
            'html_email_template_name': None,
            'context': context,
        }
        return cls._send(**email_options)
