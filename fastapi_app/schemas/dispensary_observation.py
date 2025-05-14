from pydantic import BaseModel
from typing import Optional
from datetime import date


class DispensaryObservationBase(BaseModel):
    patient_id: Optional[int]
    disorder_id: Optional[int]
    start_date: Optional[date]
    end_date: Optional[date]
    note: Optional[str]

class DispensaryObservationCreate(DispensaryObservationBase):
    pass

class DispensaryObservationUpdate(DispensaryObservationBase):
    pass

class DispensaryObservation(DispensaryObservationBase):
    id: int

    model_config = {"from_attributes": True}
