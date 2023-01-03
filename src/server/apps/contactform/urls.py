from django.urls import path

from server.apps.contactform.views.contact_form import ContactFormView

urlpatterns = [
    path(
        '',
        ContactFormView.as_view({
            'post': 'send_contact_form',
        }),
        name='contact_form',
    ),
]
