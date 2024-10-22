from typing import Optional
from pydantic import BaseModel, UUID4


class Employee(BaseModel):
    id: Optional[UUID4]
    name: str
    employee_id: int


class Driver(BaseModel):
    id: Optional[UUID4]
    name: str
    driver_id: int


class Vehicle(BaseModel):
    id: Optional[UUID4]
    vehicle_id: int
    driver_id: int


class Allocation(BaseModel):
    id: Optional[UUID4]
    vehicle_id: int
    employee_id: int
    date: str
