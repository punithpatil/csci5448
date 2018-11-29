class Person:
    """
    Person class that initilises the name
    of counsellor, receptionist and other staff objects
    """
    _name: str

    def __init__(self, person_name):
        self._name = person_name


