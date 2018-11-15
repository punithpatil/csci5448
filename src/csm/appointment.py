import csm.constants
class Appointment:
    def __init__(self, counsellor_ID):
        self.__time_slots = [False] * csm.constants.MAX_NO_OF_APPOINTMENTS
        self.__scheduler_ID = counsellor_ID

    @property
    def time_slots(self):
        return self.__time_slots

    @property
    def scheduler_ID(self):
        return self.__scheduler_ID

    def book_slot(self, time_slot):
        self.__time_slots[time_slot] = True
        return True