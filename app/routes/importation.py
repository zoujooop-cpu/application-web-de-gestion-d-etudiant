from fastapi import APIRouter
from app.services.import_csv import importer_csv

router = APIRouter()


@router.post("/import-csv")
def import_csv():

    result = importer_csv()

    return {
        "message": result
    }