import csm.insurance
import csm.patient

def main():
    print("Add new patient")
    new_patient = csm.patient.Patient("Punith Patil", 23)
    print(new_patient.patient_ID)
    print(new_patient.name)

if __name__ == "__main__":
    main()