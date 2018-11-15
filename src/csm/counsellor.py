from csm import staff
from csm import appointment


class Counsellor(staff.Staff):
    def __init__(self, counsellor_name):
        super().__init__(counsellor_name)
        self.__schedule = appointment.Appointment(self.staff_ID)

    def prescribe_meds(self):
        print("Medicine A")

    @property
    def schedule(self):
        return self.__schedule

    def print_schedule(self):
        print(self.__schedule)


if __name__ == '__main__':
    counsellor = Counsellor("abc")
    #print(counsellor.print_schedule())
    print(counsellor.schedule.time_slots)
