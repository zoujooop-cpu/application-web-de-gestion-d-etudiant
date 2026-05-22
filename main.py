from fastapi import FastAPI

from app.routes import matieres
from app.routes import etudiants
from app.routes import statistiques
from app.routes import classes
from app.routes import importation

app = FastAPI()

app.include_router(matieres.router)
app.include_router(etudiants.router)
app.include_router(statistiques.router)
app.include_router(classes.router)
app.include_router(importation.router)