from . import constants


class Appointment:
    """
    Class that implement the scheduling for each counsellor.
    """

    def __init__(self, counsellor_ID):
        """

        :param counsellor_ID: Unique ID of the counsellor this schedule belongs to
        :type counsellor_ID: uuid
        """
        self.__time_slots = [False] * constants.MAX_NO_OF_APPOINTMENTS
        self.__scheduler_ID = counsellor_ID

    @property
    def time_slots(self):
        """

        :rtype: list
        :return: list of time slots of the particular counsellor
        """
        return self.__time_slots

    @property
    def scheduler_ID(self):
        return self.__scheduler_ID

    def book_slot(self, time_slot):
        """

        :param time_slot: The time slot number to book
        :type time_slot: int
        :return: bool
        """
        self.__time_slots[time_slot] = True
        return True
