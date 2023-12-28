# Package service instance
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from crud import PackageService
from database import get_db
from schema import Package, PackageCreate

router = APIRouter(tags=["Package API"], prefix="")


# Routes for CRUD operations
@router.get("/packages/", response_model=list[Package])
def get_packages(db: Session = Depends(get_db)):
    package_service = PackageService(db)
    return package_service.get_all()


@router.post("/packages/", response_model=Package)
def create_package(package_data: PackageCreate, db: Session = Depends(get_db)):
    package_service = PackageService(db)
    return package_service.create(package_data)


@router.get("/package/{package_id}", response_model=Package)
def get_package(package_id: str, db: Session = Depends(get_db)):
    package_service = PackageService(db)
    package = package_service.get_by_id(package_id)
    if package is None:
        raise HTTPException(status_code=404, detail="Package not found")
    return package


@router.put("/package/{package_id}", response_model=Package)
def update_package(package_id: str, package_data: PackageCreate, db: Session = Depends(get_db)):
    package_service = PackageService(db)
    package = package_service.update(package_id, package_data)
    if package is None:
        raise HTTPException(status_code=404, detail="Package not found")
    return package


@router.delete("/package/{package_id}")
def delete_package(package_id: str, db: Session = Depends(get_db)):
    package_service = PackageService(db)
    result = package_service.delete(package_id)
    if "message" not in result:
        raise HTTPException(status_code=404, detail="Package not found")
    return result

