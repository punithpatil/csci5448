import uuid
from uuid import UUID

from csm.person import Person

class Patient(Person):
    __patient_ID: UUID

    def __init__(self, patientName, patientAge):
        self.__patient_ID = uuid.uuid4()
        super().__init__(patientName)
        self.__age = patientAge

    @property
    def patient_ID(self):
        return self.__patient_ID

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        assert isinstance(value, int)
        self.__age = value



