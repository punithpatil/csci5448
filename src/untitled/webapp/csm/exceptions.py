class InsuranceMaxLimitExceeded(Exception):
    """Insurance claim exceeded"""
    pass

class PatientIDMissMatch(Exception):
    """The patient ID does not match the ID present in the bill.
        You can only view bills for you.
    """