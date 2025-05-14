from pydantic import BaseModel
from typing import Optional

class PatientContactRuleBase(BaseModel):
    patient_id: Optional[int]
    rule_type: Optional[str]
    note: Optional[str]

class PatientContactRuleCreate(PatientContactRuleBase):
    pass

class PatientContactRuleUpdate(PatientContactRuleBase):
    pass

class PatientContactRule(PatientContactRuleBase):
    id: int

    model_config = {"from_attributes": True}
