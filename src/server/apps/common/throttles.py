from rest_framework.throttling import AnonRateThrottle


class UserLoginThrottle(AnonRateThrottle):
    rate = '7/minute'


class UserRegistrationThrottle(AnonRateThrottle):
    rate = '2/hour'


class OrderMakingThrottle(AnonRateThrottle):
    rate = '2/hour'


class ContactFormThrottle(AnonRateThrottle):
    rate = '2/day'
