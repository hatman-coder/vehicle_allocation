from fastapi import FastAPI
from settings import db
from apps.vehicle_allocation.crud import post_allocation
from apps.vehicle_allocation.schemas import AllocationCreate

app = FastAPI()


# ---------------------- Vehicle allocation app urls ---------------------- #
class VehicleAllocationRoutes:

    @app.post(
        "/allocations/",
        responses={
            200: {
                "content": {
                    "application/json": {"example": {"message": "Vehicle allocated"}}
                }
            },
            400: {
                "content": {
                    "application/json": {
                        "example": {
                            "error": "Vehicle is already occupied for the given date"
                        }
                    }
                }
            },
        },
    )
    async def create_allocation(allocation: AllocationCreate):
        return post_allocation(db, allocation)
