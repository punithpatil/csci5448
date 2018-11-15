from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

import webapp.csm.patient
import webapp.csm.counsellor
import webapp.csm.appointment


def index(request):
    print("Add new patient")
    new_patient = webapp.csm.patient.Patient("Punith Patil", 23)
    print(new_patient.patient_ID)
    print(new_patient.name)
    print(new_patient.age)

    print("Create counsellor")
    new_counsellor = webapp.csm.counsellor.Counsellor("Kelly")
    print("Kelly's appointment slots")
    print(new_counsellor.schedule.time_slots)

    print("Book Kellys available slot")
    new_appointment = new_counsellor.schedule
    new_appointment.book_slot(0)
    print("Available slots")
    print(new_appointment.time_slots)

    return HttpResponse(
        "Add new patient" + "\n" +
        str(new_patient.patient_ID) + "\n" +
        str(new_patient.name) + "\n" +
        str(new_patient.age) + "\n" +
        "Create counsellor" + "\n" +
        "Kelly's appointment slots" + "\n" +
        str(new_counsellor.schedule.time_slots) + "\n" +
        "Book Kellys available slot" + "\n" +
        "Available slots" + "\n" +
        str(new_appointment.time_slots)
    )