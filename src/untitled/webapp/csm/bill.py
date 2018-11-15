import uuid
class Bill:
    def __init__(self, bill_amount):
        self.__bill_ID = uuid.uuid4()
        self.__amount = bill_amount

    @property
    def bill_ID(self):
        return self.__bill_ID

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self, value):
        assert isinstance(value, int)
        self.__amount = value

    def payBill(self):
        pass
