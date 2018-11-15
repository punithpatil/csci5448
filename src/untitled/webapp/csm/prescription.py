import uuid


class Prescription:
    def __init__(self, patient_ID):
        self.__prescription_ID = uuid.uuid4()
        self.___medicine_list = []
        self.

    def get_medicine_list(self):
        return self.___medicine_list

    def prescribe_medicine(self, new_medicine):
        self.___medicine_list.extend(new_medicine)
