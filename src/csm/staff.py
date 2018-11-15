import uuid
from uuid import UUID

import csm.person

class Staff(csm.person.Person):
    staff_ID: UUID

    def __init__(self, name):
        super().__init__(name)
        self.staff_ID = uuid.uuid4()


