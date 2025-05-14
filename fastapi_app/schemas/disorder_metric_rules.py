from pydantic import BaseModel
from typing import Optional


class DisorderMetricRuleBase(BaseModel):
    disorder_code: Optional[int]
    metric_type_id: Optional[int]
    note: Optional[str]

class DisorderMetricRuleCreate(DisorderMetricRuleBase):
    pass

class DisorderMetricRuleUpdate(DisorderMetricRuleBase):
    pass

class DisorderMetricRule(DisorderMetricRuleBase):
    id: int

    model_config = {"from_attributes": True}

