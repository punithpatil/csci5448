class Person:
    __name: str

    def __init__(self, personName):
        self.__name = personName

    @property
    def name(self):
        return self.__name

