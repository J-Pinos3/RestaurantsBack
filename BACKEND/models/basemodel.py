from pydantic import BaseModel, validator

class Item(BaseModel):
    name: str
    price: float
    description: str  = None
    tax: float  = None

    @validator("tax")
    def validate_tax(cls, v):
        if v is not None and v < 0:
            raise ValueError("Tax must be a non-negative value")
        return v
