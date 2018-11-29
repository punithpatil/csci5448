import uuid

from . import person

class Staff(person.Person):
    """
    Staff class that Counsellor, Receptionsit inherit
    """
    def __init__(self, name):
        super().__init__(name)
        self.staff_ID = uuid.uuid4()
        #self.name = super(Staff, self)._name
        self.name_staff = name


