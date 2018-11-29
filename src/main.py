import csm.insurance
import csm.patient
import csm.counsellor
import csm.appointment
import csm.bill
import csm.prescription

patient = None
counsellor = None
prescription = None
bill = None

def create_patient():
    global patient
    print("Enter Patient Name, Patient Age and Insurance Type")
    patient_name, patient_age, insurance_type = input().split()
    patient =  csm.patient.Patient(patient_name, patient_age, insurance_type)
    return patient


def create_counsellor():
    global counsellor
    print("Enter counsellor name")
    counsellor_name = input()
    counsellor = csm.counsellor.Counsellor(counsellor_name)
    return counsellor


def book_appointment(counsellor, time_slot):
    counsellor_scheduler = counsellor.schedule
    counsellor_scheduler.book_slot(time_slot)
    return counsellor_scheduler

def prescribe_medicine(patinet, counsellor, medicines):
    prescription = csm.prescription.Prescription(patinet, counsellor)
    prescription.prescribe_medicine(medicines)
    return prescription

def pay_bill(patient):
    bill_to_pay = patient.outstanding_bills[0]

def patient_io():
    while True:
        print("1. Book appointment\n"
              "2. Reschedule appointment\n"
              "3. View Bill\n"
              "4. Pay Bill\n"
              "5. Claim Insurance\n"
              "6. View Prescription\n"
              )
        choice = int(input("Enter choice: "))
        if choice == 1:
            print("Councellors Available:", counsellor.name)
            selected_counsellor = input()
            print("Counsellors schedule, select slot", counsellor.schedule.time_slots)
            selected_slot = int(input())
            counsellor.schedule.time_slots[selected_slot] = True
            print("The time slot has been selected", counsellor.schedule.time_slots)
        elif choice == 3:
            print("You bill ID: ", csm.bill.BillProxy(bill).bill_ID)
            print("You bill amount Due: ", csm.bill.BillProxy(bill).amount(patient.patient_ID))
        elif choice == 4:
            print("Payment gateway")
            csm.bill.BillProxy(bill).payBill(100)
            print(csm.bill.BillProxy(bill).payment)
        elif choice == 6:
            print("The prescribed medicines: ", prescription.medicines)

        else:
            break

def counsellor_io():
    global prescription, bill
    while True:
        print("1. Check your schedule\n"
              "2. Write Prescription"
              )
        choice = int(input("Enter choice: "))
        if choice == 1:
            print("Your schedule is: ", counsellor.schedule.time_slots)
        elif choice == 2:
            print("Enter medicine list")
            medicine_list = input()
            prescription = counsellor.prescribe_medicines(patient.name, medicine_list)
            bill = csm.bill.Bill(100, patient.patient_ID)
        else:
            break

def main_screen_options(choice):
    return {
        1: create_patient,
        2: create_counsellor,
        3: patient_io,
        4: counsellor_io
    }.get(choice, None)

def main_screen():
    print("1. Add new Patient\n"
          "2. Add new Counsellor\n"
          "3. Login in as Patient\n"
          "4. Login in as Counsellor\n")

def main():
    """
    Main Driver program
    :return:
    """
    while True:
        main_screen()
        choice = int(input("Enter Choice: "))
        if choice == 0:
            break
        main_screen_options(choice)()



if __name__ == "__main__":
    main()
    print("Add new patient")
    new_patient = create_patient("Punith Patil", 23, 'gold')
    print(new_patient.patient_ID)
    print(new_patient.name)
    print(new_patient.age)

    print("Create counsellor")
    new_counsellor = create_counsellor("Kelly")
    print("Kelly's appointment slots")
    print(new_counsellor.schedule.time_slots)

    print("Book Kellys available slot")
    counsellor_scheduler = book_appointment(new_counsellor, 0)
    print("Available slots")
    print(counsellor_scheduler.time_slots)

    bill_obj = csm.bill.Bill(100, 100)
    test_bill_proxy = csm.bill.BillProxy(bill_obj)
    print(test_bill_proxy.amount(100))