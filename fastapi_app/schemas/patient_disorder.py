from pydantic import BaseModel

class PatientDisorderBase(BaseModel):
    patient_id: int
    disorder_id: int

class PatientDisorderCreate(PatientDisorderBase):
    pass

class PatientDisorderRead(PatientDisorderBase):
    pass

    model_config = {"from_attributes": True}
