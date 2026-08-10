from fastapi.responses import JSONResponse
from fastapi import Request

class PincodeNotFoundError(Exception):
    def __init__(self, pincode: str):
        self.pincode = pincode
        
class InvalidPincodeError(Exception):
    def __init__(self, pincode: str, reason: str = "Invalid pincode format"):
        self.pincode = pincode
        self.reason = reason
        
#Custom Handlers

async def pincode_not_found_exception_handler(request: Request, exc: PincodeNotFoundError):
    return JSONResponse(
        status_code=404,
        content={
            "error": "Pincode not found",
            "message": f"No location for specified pincode {exc.pincode} not found.",
            "pincode": exc.pincode
        }
    )

async def invalid_pincode_exception_handler(request: Request, exc: InvalidPincodeError):
    return JSONResponse(
        status_code=400,
        content={
            "error": "Invalid pincode",
            "message": f"Pincode {exc.pincode}: {exc.reason}",
            "pincode": exc.pincode
        },
    )