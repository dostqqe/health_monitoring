from pydantic import BaseModel
from datetime import date
from typing import Optional


class HealthIndicatorBase(BaseModel):
    patient_id: int
    day: Optional[date] = None
    result: Optional[str] = None
    metric_type_id: Optional[int] = None
    status: Optional[str] = None
    next_action: Optional[str] = None
    bot_transcript: Optional[str] = None
    source_type: Optional[str] = None
    is_valid: Optional[bool] = None
    expires_at: Optional[date] = None

class HealthIndicatorCreate(HealthIndicatorBase):
    pass

class HealthIndicatorUpdate(HealthIndicatorBase):
    pass

class HealthIndicator(HealthIndicatorBase):
    id: int

    model_config = {
        "from_attributes": True
    }

