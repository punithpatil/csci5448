import uuid
import abc

if __name__ == '__main__' and __package__ is None:
    __package__ = 'csm'

from . import exceptions


class InsuranceCreator(metaclass=abc.ABCMeta):
    """
    Abstract Creator class
    """
    @abc.abstractmethod
    def create_insurance_profile():
        pass


class InsuranceGoldCreator(InsuranceCreator):
    """
    Concrete Gold Insurance Creater
    """
    @classmethod
    def create_insurance_profile(cls):
        return InsuranceGold()


class InsuranceSilverCreator(InsuranceCreator):
    """
    Concrete Silver Insurance Creator
    """
    @classmethod
    def create_insurance_profile(cls):
        return InsuranceSilver()


class Insurance():
    @classmethod
    def create_insurance_profile(cls, type):
        if type.lower() == 'gold':
            return InsuranceGoldCreator().create_insurance_profile()
        if type.lower() == 'silver':
            return InsuranceSilverCreator().create_insurance_profile()


class InsuranceProduct(metaclass=abc.ABCMeta):
    """
    Abstract Insurance Product Class
    """
    @abc.abstractmethod
    def claim_insurance(self):
        pass


class InsuranceGold(InsuranceProduct):
    """
    Concrete class for Gold Product Insurance
    """
    def __init__(self):
        self.__inusrance_ID = uuid.uuid4()
        self.__inusrance_max_amount = 2000
        self.__insurance_claim_amount = 0

    def claim_insurance(self, claim_amount):
        if self.__insurance_claim_amount + claim_amount <= self.__inusrance_max_amount:
            self.__insurance_claim_amount += claim_amount
        else:
            raise exceptions.InsuranceMaxLimitExceeded


class InsuranceSilver(InsuranceProduct):
    """
    Concrete class for Siliver Product Insurance
    """
    def __init__(self):
        self.__inusrance_ID = uuid.uuid4()
        self.__inusrance_max_amount = 1000
        self.__insurance_claim_amount = 0

    def claim_insurance(self, claim_amount):
        if self.__insurance_claim_amount + claim_amount <= self.__inusrance_max_amount:
            self.__insurance_claim_amount += claim_amount
        else:
            raise exceptions.InsuranceMaxLimitExceeded


if __name__ == '__main__':
    testObj = Insurance.create_insurance_profile('gold')
    testObj.claim_insurance(3000)
