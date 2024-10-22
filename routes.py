from settings import db
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
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
        vehicle_id: int = None,
    ):
        return allocation_history(db, date, date_from, date_to, employee_id, vehicle_id)


# ---------------------- Home url ---------------------- #
class Home:

    @app.get("/", response_class=HTMLResponse, include_in_schema=False)
    async def home():
        return """
            <html>
                <head>
                    <title>Welcome to FastAPI</title>
                    <style>
                        body {
                            display: flex;
                            flex-direction: column;
                            align-items: center;
                            justify-content: center;
                            height: 100vh;
                            margin: 0;
                            font-family: Arial, sans-serif;
                            background-color: #f0f8ff;
                            color: #333;
                        }
                        h1 {
                            font-size: 3rem;
                            color: #4CAF50;
                        }
                        p {
                            font-size: 1.2rem;
                            text-align: center;
                        }
                        a {
                            color: #2196F3;
                            text-decoration: none;
                            font-weight: bold;
                        }
                        a:hover {
                            text-decoration: underline;
                        }
                    </style>
                </head>
                <body>
                    <h1>Hey there! 🎉</h1>
                    <p>Welcome to the FastAPI project.</p>
                    <p>Please visit the <a href="/docs">/docs</a> URL to explore the available APIs!</p>
                </body>
            </html>
            """
