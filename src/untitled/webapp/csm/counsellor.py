if __name__ == '__main__' and __package__ is None:
    __package__ = 'csm'

from . import staff
from . import appointment
from . import prescription

class Counsellor(staff.Staff):
    """
    Class that implements feature the concellor performs
    """
    def __init__(self, counsellor_name):
        super().__init__(counsellor_name)
        self.__schedule = appointment.Appointment(self.staff_ID)
        #self._name = counsellor_name

    def prescribe_medicines(self, patient_name, medicines_):
        """
        This method is used to prescribe medicide for the patient.
        It uses object composition to get prescription objects
        :param patient_name: Name of the patient
        :type patient_name: str
        :param medicines_: List of medicines specified by the counsellor
        :type medicines_: ste
        :return: Prescription object with relevant details
        """
        prescription_sheet = prescription.PrescriptionFactory.get_prescription_sheet(self.staff_ID)
        prescription_sheet.patient = patient_name
        prescription_sheet.prescribe_medicine(medicines_)
        return prescription_sheet

    @property
    def schedule(self):
        """

        :return: List of slots for appointments for each counsellor
        """
        return self.__schedule

    @property
    def name(self):
        return self._name

    def print_schedule(self):
        print(self.__schedule)


if __name__ == '__main__':
    counsellor = Counsellor("abc")
    #print(counsellor.print_schedule())
    print(counsellor.schedule.time_slots)
    prescription_sheet = counsellor.prescribe_medicines("Punith Patil", "Medicine A")
    print(prescription_sheet.patient)
    print(prescription_sheet.medicines)

