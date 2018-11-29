import uuid
import abc
import copy

class PrescriptionPrototype(metaclass=abc.ABCMeta):
    """
    Prescription Protoype abstract class
    This class defines the clone abstract method that
    classes inherit must implement
    """
    @abc.abstractmethod
    def clone(self):
        pass

class Prescription(PrescriptionPrototype):
    """
    Prescription class that defines attributes of
    the prescipiton object
    """
    def __init__(self, counsellor):
        self.__prescription_ID = uuid.uuid4()
        self.__medicines = None
        self.__patient = None
        self.__prescriber = counsellor

    @property
    def prescription_ID(self):
        return self.__prescription_ID

    @property
    def medicine_list(self):
        return self.__medicines

    @property
    def medicines(self):
        return self.__medicines

    @medicines.setter
    def medicines(self, value):
        self.__medicines = value


    @property
    def patient(self):
        return self.__patient

    @patient.setter
    def patient(self, patient_name):
        self.__patient = patient_name

    @property
    def prescriber(self):
        return self.__prescriber

    def clone(self):
        return copy.copy(self)

    def prescribe_medicine(self, medicines):
        self.__medicines = medicines

class PrescriptionFactory():
    """
    Prescription factory that generates
    Prescription objects if not created.
    If created returns the copy of that object
    """
    prescription_pads = {}

    @classmethod
    def get_prescription_sheet(cls, counsellor):
        if counsellor not in cls.prescription_pads:
            cls.prescription_pads[counsellor] = Prescription(counsellor)
        return cls.prescription_pads.get(counsellor).clone()

if __name__ == '__main__':
    prescription_sheet = PrescriptionFactory.get_prescription_sheet('abc')
    prescription_sheet1 = PrescriptionFactory.get_prescription_sheet('abc')
    prescription_sheet2 = PrescriptionFactory.get_prescription_sheet('abc')
    print(prescription_sheet,prescription_sheet1,prescription_sheet2)


