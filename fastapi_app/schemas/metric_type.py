from pydantic import BaseModel
from typing import Optional


class MetricTypeBase(BaseModel):
    name: str
    description: Optional[str] = None
    external_code: Optional[str] = None
    external_system: Optional[str] = None

class MetricTypeCreate(MetricTypeBase):
    pass

class MetricTypeUpdate(MetricTypeBase):
    pass

class MetricType(MetricTypeBase):
    id: int

    model_config = {"from_attributes": True}
