# Order superclass
import routingUtil
from datetime import datetime


class Order:
    def __init__(self, user_id, service_type, address, values={}):
        if len(values) != 0:
            self._date_created = values["date_created"]
            self._geolocation = values["geolocation"]
            self._order_id = values["order_id"]
            self._dispatch_id = values['dispatch_id']
        else:
            self._date_created = datetime.now()
            now = str(self._date_created).split(" ")
            now[1] = now[1].split('.')
            self._order_id = service_type.upper()[:2] + user_id.lower() + now[0]+now[1][0]
            self._geolocation = routingUtil.get_geolocation(address)  # (longitude, latitude)
            self._dispatch_id = None

        self._user_id = user_id.lower()
        self._address = routingUtil.get_address(address)
        self._price = 0
        self._date_processed = None
        self._date_fulfilled = None
        self._service_type = service_type.lower()
        self._is_confirmed = False
        self._is_complete = False
        self._is_paid = False
        self._av_plate_num = None

    def start_processing(self, dispatch_id):
        if self.is_confirmed:
            raise Exception('The order has already been processed.')
        self._dispatch_id = dispatch_id
        print('\n', 'received id: ', dispatch_id, '\n', 'set id: ', self._dispatch_id, '\n')
        self._date_processed = datetime.now()
        self._is_confirmed = True

    def complete_order(self):
        if not self._is_confirmed:
            raise Exception('The order has not been processed.')
        elif self.is_complete:
            raise Exception('The order has already been completed.')
        self.__pay_order()
        self._date_fulfilled = datetime.now()
        self._is_complete = True

    def __pay_order(self):
        if self._is_paid:
            raise Exception('The order has already been paid.')
        self._is_paid = True
        # we could add this to complete order to have payment be made automatically.

    @property
    def is_paid(self):
        return self._is_paid

    @property
    def is_complete(self):
        return self._is_complete

    @property
    def is_confirmed(self):
        return self._is_confirmed

    @property
    def address(self):
        return self._address

    @property
    def geolocation(self):
        return self._geolocation

    @property
    def order_id(self):
        return self._order_id

    @property
    def date_created(self):
        return self._date_created

    @property
    def date_processed(self):
        if not self._is_confirmed:
            raise Exception('The order has not been processed.')
        return self._date_processed

    @property
    def date_fulfilled(self):
        if not self._is_complete:
            raise Exception('The order has not been completed.')
        return self._date_fulfilled

    @property
    def service_type(self):
        return self._service_type

    @property
    def av_plate_num(self):
        return self._av_plate_num

    @av_plate_num.setter
    def av_plate_num(self, plate_num):
        self._av_plate_num = plate_num

    @property
    def dispatch_id(self):
        return self._dispatch_id

    def __dict__(self):
        o = {'date_created': str(self._date_created), 'geolocation': self._geolocation, 'order_id': self._order_id,
             'user_id': self._user_id, 'address': self._address, 'price': self._price,
             'date_processed': str(self._date_processed), 'date_fulfilled': str(self._date_fulfilled),
             'service_type': self._service_type, 'is_confirmed': self._is_confirmed, 'is_complete': self._is_complete,
             'is_paid': self._is_paid, 'dispatch_id': self._dispatch_id}
        return o

    def __str__(self):
        return str(self.__dict__())
