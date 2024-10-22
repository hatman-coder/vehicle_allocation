from pydantic import BaseModel


class AllocationCreate(BaseModel):
    vehicle_id: int
    employee_id: int
    date: str = "2024-10-22"


class AllocationUpdate(BaseModel):
    vehicle_id: int
    date: str = "2024-10-22"


class AllocationHistory(BaseModel):
    id: str
    vehicle_id: int
    employee_id: int
    date: str = "2024-10-22"
