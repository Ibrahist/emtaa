from pydantic import BaseModel, field_validator


class PinCodeRequest(BaseModel):
    pincode: str

    # Pincode must be a 6-digit number.
    @field_validator("pincode")
    @classmethod
    
    def validate_pincode(cls, value):
        if len(value) != 6 or not value.isdigit():
            raise ValueError("Pincode must be a 6-digit number.")
        return value
    
class LocationResponse(BaseModel):
    pincode: str
    city: str
    state: str
    district: str
    # pincode: str
    # region: str
    # district: str
    
class BulkLocationRequest(BaseModel):
    pincodes: list[str]
    
    
    @field_validator("pincodes")
    @classmethod
    def validate_pincodes(cls, values):
        for pincode in values:
            if len(values) == 0:
                raise ValueError("Pincodes list cannot be empty. At least one pincode is required.")
            if len(values) > 10:
                raise ValueError("Pincodes list cannot contain more than 10 pincodes.")
            
            for code in values:
                if len(code) != 6 or not code.isdigit():
                    raise ValueError(f"Pincode '{code}' must be a 6-digit number.")
            return values
        
        
class BulkLocationResponse(BaseModel):
    status: str = "success"
    found: int
    not_found: int
    results: list[LocationResponse]
    missing: list[str]