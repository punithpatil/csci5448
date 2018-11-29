import uuid

if __name__ == '__main__' and __package__ is None:
    __package__ = 'csm'

from . import person
from . import insurance


class Patient(person.Person):
    """
    This class represents the patient and all functionalities patients can perform
    """

    def __init__(self, patientName, patientAge, insurance_type):
        """

        :param patientName: Name of patient
        :type patientName: str
        :param patientAge: Age of patient
        :type patientAge: int
        :param insurance_type: Type of insurance patient has
        :type insurance_type: str
        """
        self.__patient_ID = uuid.uuid4()
        super().__init__(patientName)
        self.__age = patientAge
        self.__insurance = insurance.Insurance().create_insurance_profile(insurance_type)
        self.__outstanding_bills = []
        self.__paid_bills = []

    @property
    def patient_ID(self):
        """
        :rtype: uuid
        :return: Patient ID
        """
        return self.__patient_ID

    @property
    def age(self):
        """
        :rtype: int
        :return: Age of the patient
        """
        return self.__age

    @property
    def outstanding_bills(self):
        """
        :rtype: list
        :return: List of outstanding bills for the patient
        """
        return self.__outstanding_bills

    def add_bill(self, bill):
        """

        :param bill: Bill object with patient details
        :type bill: bill
        :return:
        """
        self.__outstanding_bills.append(bill)

    def remove_bill(self):
        """
        Once the bill has been paid the bill be removed from
        outstanding bills and added to paid bills
        :return: None
        """
        self.__paid_bills.append(self.__outstanding_bills[0])
        self.__outstanding_bills.pop(0)

    @property
    def name(self):
        return self._name


if __name__ == '__main__':
    patient_one = Patient("Punith Patil", 22, 'Gold')



