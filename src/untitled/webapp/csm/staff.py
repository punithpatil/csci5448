import uuid
from uuid import UUID

#import webapp.csm.person
from . import person

#class Staff(webapp.csm.person.Person):
class Staff(person.Person):
    staff_ID: UUID

    def __init__(self, name):
        super().__init__(name)
        self.staff_ID = uuid.uuid4()


