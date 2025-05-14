from pydantic import BaseModel
from typing import Optional


class DisorderBase(BaseModel):
    mkd_code: Optional[str] = None
    name: Optional[str] = None
    diagnosis_role: Optional[str] = None
    description: Optional[str] = None

class DisorderCreate(DisorderBase):
    pass

class DisorderUpdate(DisorderBase):
    pass

class Disorder(DisorderBase):
    id: int

    model_config = {
        "from_attributes": True
    }

