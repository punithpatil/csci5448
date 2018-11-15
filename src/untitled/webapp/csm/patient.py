import uuid
from uuid import UUID

#import csm.person

from . import person

class Patient(person.Person):
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

    def book_appointment(self, counsellor, time_slot):
        counsellor.book_slot(time_slot)



