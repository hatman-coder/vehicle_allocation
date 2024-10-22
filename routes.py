from fastapi import FastAPI
from settings import db
from apps.vehicle_allocation.crud import (
    post_allocation,
    update_allocation,
    delete_allocation,
    allocation_history,
)
from apps.vehicle_allocation.schemas import AllocationCreate, AllocationUpdate

app = FastAPI()


# ---------------------- Vehicle allocation app urls ---------------------- #
class VehicleAllocationRoutes:

    @app.post("/allocations/", tags=["Vehicle Allocation"])
    async def create_allocation(schema: AllocationCreate):
        return post_allocation(db, schema)

    @app.put("/allocations/{allocation_id}", tags=["Vehicle Allocation"])
    async def update_vehicle_allocation(allocation_id: str, schema: AllocationUpdate):
        return update_allocation(db, allocation_id, schema)

    @app.delete(
        "/allocations/{allocation_id}",
        tags=["Vehicle Allocation"],
    )
    async def delete_vehicle_allocation(allocation_id: str):
        return delete_allocation(db, allocation_id)

    @app.get(
        "/allocations/history/",
        tags=["Vehicle Allocation"],
    )
    async def vehicle_allocation_history(
        date: str = None,
        date_from: str = None,
        date_to: str = None,
        employee_id: int = None,
        vehicle_id: int = None
    ):
        return allocation_history(db, date, date_from, date_to, employee_id, vehicle_id)
