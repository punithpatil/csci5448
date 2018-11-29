import uuid
import abc

if __name__ == '__main__' and __package__ is None:
    __package__ = 'csm'
from . import exceptions


class AbstractBill(metaclass=abc.ABCMeta):
    """
    Abstract Bill class that defines the method amount()
    for Bill and BillProxy to define
    """
    @abc.abstractmethod
    def amount(self, patient_ID):
        pass


class Bill(AbstractBill):
    """
    The Bill class that contains all attributes of the bill
    such as bill_ID, amount due etc
    """
    def __init__(self, bill_amount, patient_ID):
        self.__bill_ID = uuid.uuid4()
        self.__amount = bill_amount
        self.__payment = 0
        self.patient_ID = patient_ID

    @property
    def bill_ID(self):
        return self.__bill_ID

    @property
    def amount(self):
        return self.__amount

    @property
    def payment(self):
        return self.__payment

    @amount.setter
    def amount(self, value):
        assert isinstance(value, int)
        self.__amount = value

    @payment.setter
    def payment(self, value):
        assert isinstance(value, int)
        self.__payment = value

    def payBill(self, value):
        self.__payment = value


class BillProxy(AbstractBill):
    """
    The BillProxy class that implements the authentication to
    check if the incomming request has the right access to the
    requested Bill object
    """
    def __init__(self, bill):
        self.__bill = bill

    def amount(self, patient_ID):
        if self.__bill.patient_ID == patient_ID:
            return self.__bill.amount - self.__bill.payment
        else:
            raise exceptions.PatientIDMissMatch("patient ID miss match")

    def __getattr__(self, item):
        return getattr(self.__bill, item)


if __name__ == '__main__':
    # Counsellor generated bill
    patient_one_bill = Bill(200, 'abc123')
    patient_two_bill = Bill(300, 'xyz123')

    # Patient viewing his own bill
    patien_one_bill_proxy = BillProxy(patient_one_bill)
    patien_two_bill_proxy = BillProxy(patient_two_bill)
    print("Patient One's Bill: ", patien_one_bill_proxy.amount('abc123'))
    print("Patient Two's Bill: ", patien_two_bill_proxy.amount('xyz123'))

    # Patient trying to print another persons bill

    print("Patient One's Bill with Patient Two's ID: ")
    print(patien_one_bill_proxy.amount('xyz123'))
