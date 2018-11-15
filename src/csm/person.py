class Person:
    __name: str

    def __init__(self, person_name):
        self.__name = person_name

    @property
    def name(self):
        return self.__name

