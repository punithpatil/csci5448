import uuid
from uuid import UUID

from csm.person import Person

class Staff(Person):
    __staffID: UUID

    def __init__(self):
        self.__staffID = uuid.uuid4()

