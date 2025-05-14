from pydantic import BaseModel
from typing import Optional
from datetime import date


class PatientBase(BaseModel):
    name: Optional[str]
    age: Optional[int]
    sex: Optional[str]
    created_at: Optional[date]

    model_config = {
        "from_attributes": True
    }

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int

class PatientUpdate(PatientBase):
    pass



