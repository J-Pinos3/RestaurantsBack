from pydantic import BaseModel, validator, Field

class Item(BaseModel):
    name: str  = Field(..., min_length=3) 
    #ge means greater than or equal, gt means greater than
    price: float = Field(..., gt=0)
    description: str  = None
    tax: float  = None

    @validator("tax")
    def validate_tax(cls, v):
        if v is not None and v < 0:
            raise ValueError("Tax must be a non-negative value")
        return v
