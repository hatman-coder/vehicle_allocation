import datetime
from bson import ObjectId
from settings import db
from fastapi.responses import JSONResponse
from serializer import serialized_data


def post_allocation(db, request_data):
    # Validation for existing allocated data for the requested date
    if db.allocations.find_one(
        {"vehicle_id": request_data.vehicle_id, "date": request_data.date}
    ):
        return JSONResponse(
            {"error": "Vehicle is already occupied for the given date"}, status_code=400
        )

    db.allocations.insert_one(request_data.dict())
    return JSONResponse({"message": "Vehicle allocated"}, status_code=201)


def update_allocation(db, allocation_id, request_data):
    allocation_instance = db.allocations.find_one({"_id": ObjectId(allocation_id)})

    if not allocation_instance:
        return JSONResponse({"error": "Allocation not found"}, status_code=404)

    # Validation for past date
    if (
        datetime.datetime.now().date()
        > datetime.datetime.strptime(allocation_instance["date"], "%Y-%m-%d").date()
    ):
        return JSONResponse(
            {"error": "Past date allocation modification is prohibited"},
            status_code=406,
        )

    # Validation for restrict date manipulation
    if (
        datetime.datetime.now().date()
        > datetime.datetime.strptime(request_data.date, "%Y-%m-%d").date()
    ):
        return JSONResponse(
            {"error": "You can not override future allocation into past allocation"},
            status_code=406,
        )

    db.allocations.update_one(
        {"_id": ObjectId(allocation_id)}, {"$set": request_data.dict()}
    )
    return JSONResponse({"message": "Allocation updated"}, status_code=202)


def delete_allocation(db, allocation_id):
    allocation_instance = db.allocations.find_one({"_id": ObjectId(allocation_id)})

    if not allocation_instance:
        return JSONResponse({"error": "Allocation not found"}, status_code=404)

    if (
        datetime.datetime.now().date()
        > datetime.datetime.strptime(allocation_instance["date"], "%Y-%m-%d").date()
    ):
        return JSONResponse(
            {"error": "Can not delete past allocations"}, status_code=406
        )

    db.allocations.delete_one({"_id": ObjectId(allocation_id)})
    return JSONResponse({"message": "Allocation deleted"}, status_code=200)


def allocation_history(db, date, date_from, date_to, employee_id, vehicle_id):
    filters = {}
    if date:
        filters["date"] = date

    if date_from:
        filters["date"] = {"$gte": date_from}

    if date_to:
        filters["date"] = {"$lte": date_to}

    if employee_id:
        filters["employee_id"] = employee_id

    if vehicle_id:
        filters["vehicle_id"] = vehicle_id

    queryset = db.allocations.find(filters)

    return JSONResponse({"data": serialized_data(queryset)}, status_code=200)
