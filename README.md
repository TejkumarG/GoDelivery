# Go Delivery

## Overview
This project implements CRUD (Create, Read, Update, Delete) operations for Shipper and Package APIs.

## Installation
- **Python Version:** 3.9.13
- Use the provided `requirements.txt` file to install necessary dependencies:

```
pip install -r requirements.txt
```

## Running the Application
Run the application using Uvicorn:

```
uvicorn main:app --reload
```

## Routes
### Shipper API
```
POST /shippers/: Create a new shipper.
GET /shippers/: Retrieve all shippers.
GET /shipper/{shipper_id}: Retrieve a shipper by ID.
PUT /shipper/{shipper_id}: Update a shipper by ID.
DELETE /shipper/{shipper_id}: Delete a shipper by ID.
```

### Package API
```
POST /packages/: Create a new package.
GET /packages/: Retrieve all packages.
GET /package/{package_id}: Retrieve a package by ID.
PUT /package/{package_id}: Update a package by ID.
DELETE /package/{package_id}: Delete a package by ID.
```