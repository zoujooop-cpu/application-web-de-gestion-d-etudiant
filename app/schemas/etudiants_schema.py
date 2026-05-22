from pydantic import BaseModel
from datetime import date

class EtudiantsSchema(BaseModel):
    
    code: str
    
    numero: str

    prenom: str

    nom: str

    classze_id: int

    date_naissance: date

    classe_id: int