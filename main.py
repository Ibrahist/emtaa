from fastapi import FastAPI
from exceptions import PincodeNotFoundError, InvalidPincodeError, pincode_not_found_exception_handler, invalid_pincode_exception_handler
from models import LocationResponse, BulkLocationRequest, BulkLocationResponse
from data import pincode_db


app = FastAPI(
    title= "Pincode lookup API",
    description= "Autofill regions and districts from Tanzania based on pincode during checkout",
)

#Cusom exception handlers
app.add_exception_handler(PincodeNotFoundError, pincode_not_found_exception_handler)
app.add_exception_handler(InvalidPincodeError, invalid_pincode_exception_handler)

@app.get("/")
def root():
    return {"message": "Welcome to the Pincode lookup API!"}

@app.get("/pincode/{code}", response_model=LocationResponse)
def get_location_by_pincode(code: str):
    # Validate the pincode format
    if len(code) != 6 or not code.isdigit():
        raise InvalidPincodeError(f"Pincode '{code}' must be a 6-digit number.")

    # Lookup the pincode in the database
    if code not in pincode_db:
        raise PincodeNotFoundError(code)
    return pincode_db[code]


app.post("/pincodes", response_model=BulkLocationResponse)
def bulk_lookup_locations(request: BulkLocationRequest):
    found_results = []
    missing_pincodes = []

    for code in request.pincodes:
        if code in pincode_db:
            found_results.append(pincode_db[code])
            found_results.append(pincode_db[code])
        else:
            missing_pincodes.append(code)

    return BulkLocationResponse(
        found=len(found_results),
        not_found=len(missing_pincodes),
        results=found_results,
        missing=missing_pincodes
    )