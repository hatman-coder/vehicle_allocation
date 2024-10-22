from pydantic import BaseModel, Field
from bson import ObjectId


class Employee(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    name: str
    employee_id: int


class Driver(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    name: str
    driver_id: int


class Vehicle(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    vehicle_id: int
    driver_id: int


class Allocation(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    vehicle_id: int
    employee_id: int
    date: str
