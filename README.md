# Vehicle Allocation System

## Overview

The Vehicle Allocation System is a web application built with FastAPI and MongoDB designed to manage vehicle allocations for employees. This system allows employees to allocate vehicles for specific days, ensuring efficient vehicle management within a company.

## Features

- **Unrestricted APIs**: All APIs are accessible without authentication, facilitating ease of testing and integration.
- **Vehicle Allocation**: Employees can allocate vehicles for a day, provided the vehicle is not already allocated.
- **History Reports**: View historical allocations for tracking and analysis.
- **Data Filtering**: Filter allocations based on various criteria for easier data management.
- **Containerization**: The application is containerized using Docker for easy deployment and management.
- **Swagger Documentation**: Automatic API documentation is provided via Swagger for easy exploration and testing of the API endpoints.

## Requirements

- Python >= 3.10
- FastAPI
- MongoDB
- Docker (for containerization)

## Getting Started

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd vehicle-allocation-system

2. Run docker
   ```bash
   docker compose up --build -d
