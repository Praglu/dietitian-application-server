from server.apps.contactform.models import ContactForm
from server.datastore.commands.abstract import AbstractCommand
from server.services.email import EmailService


class ContactFormCommand(AbstractCommand):
    def __init__(self, first_and_last_name, email, phone, message):
        self.first_and_last_name = first_and_last_name
        self.email = email
        self.phone = phone
        self.message = message

    def send_contact_form(self):
        self._create_contact_form_object()
        self._send_email()

    def _create_contact_form_object(self):
        ContactForm.objects.create(
            first_and_last_name=self.first_and_last_name,
            email=self.email,
            phone=self.phone,
            message=self.message,
        )

    def _send_email(self):
        context = {
            'first_and_last_name': self.first_and_last_name,
            'email': self.email,
            'phone': self.phone,
            'message': self.message,
        }
        EmailService.send_contact_form_message(context=context)
