from datetime import datetime
import uuid
from server.apps.offer.models import Offer

from server.apps.order.models import Order, ProductWithQuantity
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
        payment_method,
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
        self.payment_method = payment_method
        self.sum = sum

    def make_new_order(self):
        self._make_product_with_quantity()
        self._get_user()
        self._make_order()
        self._send_confirmation_email()

    def _make_product_with_quantity(self):
        self.chosen_products = []
        self.all_products_details = ''
        for product in self.products:
            product_id = product['id']
            product_quantity = product['quantity']
            offer_id = Offer.objects.get(pk=product_id)
            chosen_product = ProductWithQuantity.objects.create(
                offer=offer_id,
                quantity=product_quantity,
            )
            self.chosen_products.append(chosen_product)
            product_details = ''
            product_details += f'{str(chosen_product.quantity)}x '
            product_details += str(chosen_product.offer.title)
            self.all_products_details += f'\n {product_details},'

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
            payment_method=self.payment_method,
            additional_info=self.additional_info
        )
        self.new_order.products.set(self.chosen_products)
        self.new_order.save()

    def _send_confirmation_email(self):
        context = {
            'email': self.email,
            'order_id': f'{str(self.new_order.uuid)[:12]}',
            'first_and_last_name': f'{self.first_name} {self.last_name}',
            'order_details': self.all_products_details,
            'sum_of_order': self.sum,
        }
        EmailService.send_confirmation_order_message(context=context)
