from datetime import datetime
import uuid

from server.apps.order.models import Order
from server.apps.order.validators import ProductsJsonValidator
from server.apps.user.models import BonusUser
from server.datastore.commands.abstract import AbstractCommand
from server.services.email import EmailService


class MakeNewOrderCommand(AbstractCommand):
    def __init__(
        self,
        first_name,
        last_name,
        street,
        house_number,
        post_code,
        city,
        email,
        phone,
        are_service_terms_accepted,
        additional_info,
        products,
        sum,
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.street = street
        self.house_number = house_number
        self.post_code = post_code
        self.city = city
        self.email = email
        self.phone = phone
        self.are_service_terms_accepted = are_service_terms_accepted
        self.additional_info = additional_info
        self.products = products
        self.sum = sum

    def make_new_order(self):
        # self._validate_products()
        self._get_user()
        self._make_order()
        self._send_confirmation_email()

    def _get_user(self):
        try:
            self.bonus_user = BonusUser.objects.get(
                user__email=self.email,
            )
        except:
            self.bonus_user = None
    
    def _make_order(self):
        self.new_order = Order.objects.create(
            uuid=uuid.uuid4(),
            user=self.bonus_user,
            first_name=self.first_name,
            last_name=self.last_name,
            street=self.street,
            house_number=self.house_number,
            post_code=self.post_code,
            city=self.city,
            email=self.email,
            phone=self.phone,
            are_service_terms_accepted=self.are_service_terms_accepted,
            date_of_order=datetime.utcnow(),
            products_with_quantity=self.products,
            sum=self.sum,
            additional_info=self.additional_info
        )

    def _send_confirmation_email(self):
        context = {
            'email': self.email,
            'order_id': f'{str(self.new_order.uuid)[:12]}',
            'first_and_last_name': f'{self.first_name} {self.last_name}',
            'sum_of_order': self.sum,
        }
        EmailService.send_confirmation_order_message(context=context)
