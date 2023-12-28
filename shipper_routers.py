# Shipper service instance
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from crud import ShipperService
from database import get_db
from schema import Shipper, ShipperCreate

router = APIRouter(tags=["Shipper API"], prefix="")


@router.get("/shippers/", response_model=list[Shipper])
def get_shippers(db: Session = Depends(get_db)):
    shipper_service = ShipperService(db)
    return shipper_service.get_all()


@router.post("/shippers/", response_model=Shipper)
def create_shipper(shipper_data: ShipperCreate, db: Session = Depends(get_db)):
    shipper_service = ShipperService(db)
    return shipper_service.create_shipper(shipper_data)


@router.get("/shipper/{shipper_id}", response_model=Shipper)
def get_shipper(shipper_id: int, db: Session = Depends(get_db)):
    shipper_service = ShipperService(db)
    shipper = shipper_service.get_shipper_by_id(shipper_id)
    if shipper is None:
        raise HTTPException(status_code=404, detail="Shipper not found")
    return shipper


@router.put("/shipper/{shipper_id}", response_model=Shipper)
def update_shipper(shipper_id: int, shipper_data: ShipperCreate,
                   db: Session = Depends(get_db)):
    shipper_service = ShipperService(db)
    updated_shipper = shipper_service.update_shipper(shipper_id, shipper_data)
    if updated_shipper is None:
        raise HTTPException(status_code=404, detail="Shipper not found")
    return updated_shipper


@router.delete("/shipper/{shipper_id}")
def delete_shipper(shipper_id: int, db: Session = Depends(get_db)):
    shipper_service = ShipperService(db)
    result = shipper_service.delete_shipper(shipper_id)
    if "message" not in result:
        raise HTTPException(status_code=404, detail="Shipper not found")
    return result
