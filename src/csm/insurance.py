import uuid

from csm import customExceptions


class Insurance:
    def __init__(self):
        self.__inusrance_ID = uuid.uuid4()
        self.__inusrance_max_amount = 2000
        self.__insurance_claim_amount = 0

    def claim_insurance(self, claim_amount):
        if self.__insurance_claim_amount + claim_amount <= self.__inusrance_max_amount:
            self.__insurance_claim_amount += claim_amount
        else:
            raise customExceptions.InsuranceMaxLimitExceeded




if __name__ == '__main__':
    testObj = Insurance()
    testObj.claim_insurance(3000)
