from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from models import Package, Shipper


class PackageService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Package).all()

    def create(self, package_data):
        try:
            package = Package(**package_data.dict())
            self.db.add(package)
            self.db.commit()
            self.db.refresh(package)
            return package
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=400, detail=f"Error creating package: {str(e)}")

    def get_by_id(self, package_id):
        return self.db.query(Package).filter(Package.id == package_id).first()

    def update(self, package_id, package_data):
        with self.db.begin():
            self.db.query(Package).filter(Package.id == package_id).update(package_data.dict())
        return self.get_by_id(package_id)

    def delete(self, package_id):
        package_to_delete = self.get_by_id(package_id)
        if package_to_delete:
            with self.db.begin():
                self.db.delete(package_to_delete)
            return {"message": "Package deleted successfully"}
        return {"message": "Package not found"}


class ShipperService:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Shipper).all()

    def create_shipper(self, shipper):
        try:
            new_shipper = Shipper(**shipper.dict())
            self.db.add(new_shipper)
            self.db.commit()
            self.db.refresh(new_shipper)
            return new_shipper
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=400, detail=f"Error creating shipper: {str(e)}")


    def get_shipper_by_id(self, shipper_id: int):
        return self.db.query(Shipper).filter(Shipper.id == shipper_id).first()

    def update_shipper(self, shipper_id: int, shipper):
        old_shipper = self.get_shipper_by_id(shipper_id)
        if shipper:
            if shipper.name:
                old_shipper.name = shipper.name
            if shipper.address:
                old_shipper.address = shipper.address
            if shipper.contact_information is not None:
                old_shipper.contact_information = shipper.contact_information
            self.db.commit()
            self.db.refresh(old_shipper)
            return old_shipper
        return None

    def delete_shipper(self, shipper_id: int):
        shipper = self.get_shipper_by_id(shipper_id)
        if shipper:
            self.db.delete(shipper)
            self.db.commit()
            return {"message": "Shipper deleted successfully"}
        return {"message": "Shipper not found"}
