from fastapi.responses import JSONResponse
from settings import db


def post_allocation(db, allocation_data):
    print(allocation_data)
    # Validation for existing allocated data for the requested date
    if db.allocations.find_one(
        {"vehicle_id": allocation_data.vehicle_id, "date": allocation_data.date}
    ):
        return JSONResponse(
            {"error": "Vehicle is already occupied for the given date"}, status_code=400
        )

    db.allocations.insert_one(allocation_data.dict())
    return JSONResponse({"message": "Vehicle allocated"}, status_code=202)
